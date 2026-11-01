## PROMPT EVALUATION REPORT

### Task: Julia delegates Leonard's ZM difficulty baseline: build the register (Tickets + Rules in force) from the Trello card rules, its "Before Monday" checklist and Leonard's DM thread, file it in ZM Difficulty, share it with the Monday invite, comment on tickets per rule 6 as changed, reply to Leonard in the DM with counts, keys and when a new player gets their starting tier
### Assigned Persona: Julia Lawson - Product Manager (roster `julia_lawson`, julia.lawson@harmonygames.co)
### Assigned Business Function: Product
### Assigned Competency: Engineering Ops
### Assigned Task Skill: Retrieval
### Assigned Horizon: long-horizon (Task Type field; Difficulty Mode "medium" recorded as context)

Review: `/prompt`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode. Actual review date 2026-10-30. Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Universe `Universe_SynthCut` (hg4-synth-sep30cut v16), manifest sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a`. Eval release task-quality-v1 (manifest `0040c6a5…9c2e`, verified with `hg_eval_release.py snapshot prompt`). Check record: prompt sha256 `22f26066…1787`, review context `423ac833…80bb`.

Inputs:
- `04_Prompt.txt`: revision 21, 525 bytes, sha256 `22f26066…1787`. Attached as `04_Prompt (7).txt`; byte-identical to the prompt graded in the last /prompt round (PASS 5 on SQL revision 17).
- `00_Task_Assigned_Inputs.md`: all five fields stated, which clears intake.
- `01_Universe_Inject.sql`: revision 20, 88,927 bytes, sha256 `6972a45038e9f3dbb5cd7e8d32756af3a4d130c2b4f2416d059c7483a503858b`. Changed since the last /prompt round (revision 17, `10c1ee92…ce18`). Per the Eval 0 range diff, four things changed:
  - **Leonard's DM (line 44)** now ends "…with how many tickets made the list and how many of each status, and tell me when a new player gets their starting tier".
  - **Card #80 rule 1 (lines 58 and 66)** now reads "any ticket Blake counts as tier work even if the title doesn''t say so: his closing note on those starts with ''tiers:''" (was: Blake's tickets that he counts as tier work).
  - **Card #80 rule 5** gains "The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself; where a write-up and the build disagree, go by the build."
  - **New Linear comment (line 226)** on ZOM-281 by usr_cc3e90160f490686 (arthur.blake@): "tiers: closing. checked on the dev build", 2025-06-27T09:34:19Z.
  - Every other row is byte-identical.
- No error/async config, dynamic context or reference files were supplied, and the prompt references none. A saved Agent trajectory exists in the workspace; under stage ownership it was not opened for this review.
- Evidence contract `stage-evidence-v1`. **Reused:** prior `1_prompt.md` facts for byte-identical SQL rows and base records (checklist, thread reply, card comment, enrage sheet, Blake's mails, invite, folder, agenda, Linear states, enrage code). **NEW:** everything that depends on the four changes: ZOM-281's entry and status, the starting-tier answer, rule 5's build clause against the deck and ZOM-42, the counts, forks O–R and the B–N recomputation. TierManager.cs, WinRateRule.cs and WinHistory.cs were re-read in full this round.
- Line numbers: the report text uses physical (`\n`) SQL lines, as Eval 0 does. The generated UGT section uses the check helper's numbering, which also splits on bare `\r` inside Gmail bodies, so rows after line 78 show higher numbers there (for example the invite is physical line 112, helper line 182; the ZOM-281 comment is physical 226, helper 296).

**What this round changes.** The prompt is the same, but the answer moves: 30 tickets instead of 29 (ZOM-281 joins as Live, so Live 17), the comment set and shares are unchanged, and the DM reply must also say when a new player gets their starting tier (after their first 10 games played, from the average CPM of those games; above 90 goes to tier 1). It also leaves one fork open: rule 5's new build clause sends the reader to the code for promotion and demotion, and the code counts a different window from every write-up (fork S, Phase 2).

---

### Injection Gate
- **State:** NEVER_REVIEWED. The gate reads `reports/input_manifest.json`, which this portal's writer never creates.
- **Eval 0 handling:** `0_injection.md` (injection-static-v2) reviews the identical SQL hash `6972a450…858b` (revision 20): **FINAL VERDICT: PASS**, COMPLETE (lint: 164 INSERT, 1 UPDATE, 0 FAIL / 0 CHECK / 0 INFO). Static checks A–B are REUSED; the Check C items this prompt depends on were redone here (Phase 3.2).
- **Reviewed SQL sha256:** `6972a45038e9f3dbb5cd7e8d32756af3a4d130c2b4f2416d059c7483a503858b`. Eval 0 verdict: PASS.
- **Eval 0 downstream advisories on records this prompt depends on:**
  - **D1 (ZOM-281 in scope):** tested here as forks O (entry) and P (status). ZOM-281 is in and Live.
  - **D2 (starting-tier timing):** Eval 0 noted base ZOM-42's "gets assigned after the first 6-7 levels based on CPM, to be defined later" against "first 10 levels" elsewhere, and said Blake's mail doesn't state the timing. Tested here as fork Q. The build itself states it (`TierManager.cs` "if (totalGames == 10)"), and rule 5 now says to go by the build, so the answer is clear. This is base Linear text, not a Snowflake/Confluence conflict, and ZOM-42 marks its own 6-7 as provisional; not a coherence defect (Phase 3.2).
- **Advisories carried:** A1–A5 (schema-snapshot columns, Trello action `_id` fields and similar). None changes a graded value.

---

### Phase 0: Sources read

Docs and references read: Eval 1 in full; `prompt_rubric_reliability.md` release binding; `deep_recheck.md`; `common_errors.md`; `acl.md`; `roster.json`; tool catalog. The PDFs in `Evals/Docs` were not re-extracted; Eval 1's inline bands and Local Overrides were applied (evidence limit, unchanged from prior rounds).

Universe exploration (synth-cut base plus SQL overlay), NEW this round:
- **ZOM-281** (base Linear `/issues/3334`): "Win streak not lost when replaying without main menu", Bug, Done, parent ZOM-294, assignee usr_EMPLOYEE_0032, created 2025-06-19, completed 2025-06-27T09:56:19Z, no relations. None of rule 1's title words; it enters scope only through Blake's note "tiers: closing. checked on the dev build" (22 minutes before completion). Linear `/users/35` maps usr_cc3e90160f490686 to arthur.blake@. Not on Leonard's exclusion list (30, 49, 50, 161, 262, 275) and not an analytics or tutorial ticket.
- **ZOM-281 and GitHub:** a complete scan of the GitHub export finds no "ZOM-281" string; the "win streak" PRs are GameOfDominoes only. So an Agent looking for a merged PR finds none (fork P).
- **Shipped authority:** Blake's store builds mail (line 81): both store builds "were cut from main on Sep 26, and everything difficulty related was merged long before that"; only level editor, Editor folders and the debug menu are stripped. ZOM-281 is a gameplay fix.
- **Starting tier, every written source vs the build:**
  - Deck slide (line 37): "average CPM over the first 10 levels; 90 or more starts you on tier 1".
  - ZOM-199 (base): "first 10 level CPM >= 90, then tier 1".
  - ZOM-42 (base): "Players starts at default tier 0, but gets assigned after the first 6-7 levels based on CPM, to be defined later", and in the same ticket "1st 10 level avg CPM > 90 (top 20%) moves to tier 1".
  - Blake's reply (line 99): "the starting tier check in the build is cpm > 90, not >= 90 … so 90 exactly stays on tier 0".
  - Build: `TierManager.cs` lines 30–32 bucket when `totalGames == 10`; line 93 `cpm > 90.0f`; `WinHistory.cs` total games = wins + losses.
- **Promotion and demotion as built** (`WinRateRule.cs` Defaults): tier ≤ -2 promotes on 1 win; from tier -1 up, ≥ 80% over 10 games promotes, ≤ 50% over 10 demotes (worst/best-case early exit), 4 losses demote; tier range -2 to 5; every change resets the record; a demotion lowers the current level's retry tier (`RetryTierOffset--`). The deck slide lists only the 4-loss demotion; rule 5's build clause and ZOM-42 both give the 50% rule too.
- **Which games the build counts** (NEW, `WinHistory.cs`): results are appended at the end of the tier history (line 160 `tierWinHistory += win ? "W" : "L";`), the history is cleared on every tier change (line 26), and the win-rate loop counts from index 0 (line 46 `for (int i = 0; i < gamesCount; i++)`). So the build judges promotion and demotion on the first 10 (and first 4) games since the last tier change. The deck says "over the last 10 attempts" and "4 losses in a row"; ZOM-42 says "UP TO THE MOST RECENT 10 attempts" and that a 4-loss streak "can still trigger at any time". The same file's doc comment (line 58) says "Get win rate over last n games."

Status derivation (shows solvability, not a golden answer; earlier statuses REUSED from byte-identical rows, ZOM-281 NEW):
- **Live 17:** ZOM-23, 42, 45, 199, 221, 246, 258, 263, 274, 281, 282, 288, 295, 300, 303, 305, 378.
- **Editor only 9:** ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315.
- **Replaced 1:** ZOM-254, replaced by ZOM-282.
- **Not shipped 3:** ZOM-202, 280, 293.
- **Total 30** = 31 title matches minus Duplicates ZOM-203 and ZOM-276, plus the five "tiers:" tickets ZOM-221, 281, 300, 305, 378 (36), minus ZOM-30, 49, 50, 161, 262, 275.
- **Comments (14, unchanged):** ZOM-199 (what the build does: cpm > 90), ZOM-254 (replaced by ZOM-282), and the 12 Editor only and Not shipped tickets (the change isn't in the store builds). ZOM-281 is Live and gets none.
- **Shares (unchanged):** robert@ and brian.foster@ can edit; leonard.hayes@ and arthur.blake@ can comment.
- **DM reply:** total 30, the four status counts, the keys of the 3 Not shipped and 9 Editor only tickets, and when a new player gets their starting tier.

---

### Requirement ledger

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Find Leonard's Tuesday DM ask, including his thread reply | SQL lines 44 and 50 (D05HB64NMQU, 19:48:26Z and 20:07:18Z) | Slack DM history; thread via reply_count 1 | `slack_conversations_history`, `slack_conversations_replies` / `slack_read_thread`, search | Julia is a DM member | The ask: register; six tickets off; reply with total, per-status counts, the Not shipped and Editor only keys, and the starting-tier timing |
| "everything it points to": card rules | Card #80 (line 58), updateCard (66), commentCard (68), checklist and items (70–76) | DM names "the difficulty baseline card on the zm roadmap board" | `trello_get_cards_on_board`, `trello_get_card`, `trello_get_comments`, `trello_get_checklist` | Trello unscoped | Rules 1–7 (rule 1 with Blake's "tiers:" notes, rule 5 with the build clause), the attack-power addendum, and the rule 6 and rule 7 changes |
| Ticket scope | Linear ZOM issues; "tiers:" comments (incl. ZOM-281, line 226); Trello comment; DM thread reply | Linear search/list; per-ticket comments | Linear search/get, `linear_list_comments` | Unscoped | 30 tickets (36 rule-1 tickets minus the six named) |
| Status per ticket (rules 3–4) | Blake's mail and reply; Linear states and closing notes; GitHub | Gmail search; Linear; GitHub | Gmail read; Linear; GitHub reads | Julia's mailbox; unscoped | Live 17 / Editor only 9 / Replaced 1 / Not shipped 3 |
| Rules in force tab (rule 5) | Deck, ZOM-42, Blake's reply, enrage sheet Live tab, `TierManager.cs`, `WinRateRule.cs`, `WinHistory.cs` | GSlides, Linear, Gmail, GSheets, GitHub | `gslides_get_presentation_text`, `gsheets_values_batch_get`, `github_get_file_contents` | Deck shared; sheet owned by Julia; GitHub unscoped | Starting tier after the first 10 games played, cpm > 90; promotion; demotion with both rules and the level drop (which games the window counts is not settled: fork S); enrage Live tab as it stands |
| Build the register: one sheet, tabs Tickets + Rules in force | Agenda doc; card rule 2 | GDocs | `gsheets_create_spreadsheet`, `gsheets_batch_update`, `gsheets_values_update` | Write (ACL-free) | New spreadsheet |
| Put it in the ZM Difficulty folder | Prompt; card rule 7 | Drive folder d_96489e1e00a56685625939 | `gdrive_move_file` (or create with parent) | Julia is writer | File in folder |
| Share with everyone on Monday's invite | Prompt; card rule 7 as changed by the checklist | GCal event on Julia's calendar | `gdrive_share_file` (role param) | Julia's own calendar | robert@ and brian.foster@ writer; leonard.hayes@ and arthur.blake@ commenter |
| Ticket comments (rule 6 as changed) | Card rule 6; checklist item; Blake's reply; rule 4 | Linear | `linear_create_comment` | Write | ZOM-199, ZOM-254 and the 12 Editor only and Not shipped tickets |
| Reply to Leonard in the DM | DM and thread reply | Slack | `slack_send_message` | Write | Total 30, per-status counts, Not shipped and Editor only keys, and that a new player gets their starting tier after their first 10 games (from those games' average CPM) |

Output capability: spreadsheet/tab creation, moving into the folder, sharing, Linear comments and the Slack reply are SUPPORTED by declared catalog tools. The `commenter` role is a free-string parameter with no base example; runtime acceptance UNVERIFIED (evidence limit, not a failure).

---

### Phase 1: Prompt Structure & Persona (prompt text byte-identical; re-judged against the new sources)

**Persona:** PASS (5). The prompt matches the exact roster entry. It is a CEO-to-PM delegation; the card says "Julia owns this one", and Julia owns the enrage sheet.

**Assigned Competency:** PASS (5). Engineering Ops: reconciling tickets with what shipped in store builds, reading the build code for the tier rules, and 14 ticket comments.

**Assigned Task Skill:** PASS (5). Retrieval is the core work: every in-scope ticket (now including one found only through a closing note), state, shipped status and rule value, across six services, with two late instruction layers to find.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. PASS. Data seeding PASS.
- **Dynamic Change:** the checklist changes two card rules after Leonard wrote "rest of the card stands", and the thread reply narrows the scope after the DM.
- **Superseded sources:** the deck's "90 or more" vs Blake's "cpm > 90"; ZOM-42's provisional "6-7 levels" vs the build's 10 games; the deck's 4-loss-only demotion vs the build's two rules; the deck's blunder slide vs Arthur's Slack.
- **Decoys:** Brian's "+50% … every monster" and "the editor bits too"; Domino card #211; the "Next pass" tab; Vincent's channel request; ZOM-281 having no PR.

**Naturalness:** PASS. First person, lowercase and casual, with no document formatting, polished connectives or enumerated specs.

**Anti-Patterns:**
| Pattern | Status |
|---------|--------|
| Command List | PASS. One lowercase "then" with no first/finally, and the order is Leonard's own condition |
| Bolt-On | PASS. Every sentence serves the baseline |
| Pre-Solving | PASS. No counts, tickets, statuses, exclusions, timings or causes named |
| Tool Mention | PASS. "dm", "folder", "invite" and "tickets" are natural nouns |

**Diversity:** a two-tab sheet, folder placement, role-based sharing, a 14-ticket Linear comment batch and a DM reply over a 30-ticket cohort with a rules answer.

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** FAIL (2). One fork stays open: **S, the promotion/demotion window on the Rules in force tab** (raised independently by deep recheck passes P1 and P2, confirmed in the main session; see Deep Recheck).
- **Reading A (write-ups):** promotion at 80% or more over the latest 10 attempts, demotion on 4 losses in a row at any time or 50% or lower over the latest 10. Support: the deck, ZOM-42, the rule constants in `WinRateRule.cs`, and `WinHistory.cs`'s own doc comment "Get win rate over last n games." Blake's reply, the card's source on what the build does, flags only the cpm > 90 check "for the rules tab".
- **Reading S (build as it runs):** card rule 5 asks for promotion and demotion "as they work in the store builds today" and now adds "where a write-up and the build disagree, go by the build". The code counts the first 10 and first 4 games since the last tier change, so a player who neither promotes nor demotes in those games stays on the tier.
- **Why it isn't settled:** no ticket, closing note, mail or card line says which window the tab should state. Both readings apply the same card clause to the same file, so none of the five checks decides it. It is not a both-fair figure: it is a rule description, not one reported figure.
- **Everything else is unique.** The other new forks (O, P, Q, R) are excluded by quoted records, K now also covers the DM answer, and B–N stay excluded on the 30-ticket list. Score 2 rather than 1 because the fork is limited to one part of one tab.

### Unique Ground Truth comparison

Unique Ground Truth: FAIL 2

Basis: One fork stays open: S (deep recheck P1 DR2 / P2 DR3). Card rule 5 asks for promotion and demotion as they work in the store builds and says to go by the build where a write-up disagrees; the build (WinHistory.cs) counts the first 10 and first 4 games since the last tier change, while the deck and ZOM-42 say the latest 10 and 4 in a row at any time, and the same build file documents the method as 'last n games'. No record says which the Rules in force tab should state. Everything else resolves to one end state: O, P, Q and R are excluded by rule 1, the store builds mail, rule 5's build clause, Blake's reply and the tier code; B to N stay excluded on the 30-ticket list (Live 17, Editor only 9, Replaced 1, Not shipped 3). Score 2: the fork is in one part of one tab; the ticket list, statuses, comments, shares and DM answer are unique.

Alternative selection: B to N are every fork from earlier rounds, recomputed for the revision-20 overlay (only the DM text, card rules 1 and 5 and the new ZOM-281 comment changed; every other row is byte-identical). O and P test the new in-scope ticket: O its entry (assignee is not Blake), P its status (a complete GitHub scan finds no 'ZOM-281' string, so 'never-merged' is a natural reading). Q and R test the new DM question and rule 5 clause against the written starting-tier rules: Q is ZOM-42's 6-7 levels line, R the deck/ZOM-199 '90 or more'. K is extended to the DM answer. A title scan of the 30 for analytics, tutorial, FTUE, track, event and instrument still finds only ZOM-378 (M); ZOM-281's title 'Win streak not lost when replaying without main menu' is neither. S was added after the deep recheck (P1 DR2, P2 DR3): the promotion/demotion window on the Rules in force tab, now that rule 5 says to go by the build and WinHistory.cs counts from the oldest game since the last tier change.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Follow the card as Leonard left it, his checklist and his DM thread: scope is every difficulty ticket created up to Aug 31 by title word plus every ticket with Blake's 'tiers:' closing note (ZOM-221, 281, 300, 305, 378), attack power counting only when written out (ZOM-271 out), minus the six analytics and tutorial tickets his DM reply lists; status against Blake's store builds mail (ZOM-281 Done, gameplay, Live); Replaced only where another ticket's closing note says so (ZOM-282 on ZOM-254); comments on ZOM-199 (flagged by Blake's reply), on Replaced ZOM-254 and, per the checklist's rule 6 change, on every Editor only and Not shipped ticket; share with the invite attendees, Robert and Brian as editors; the Rules in force tab gives the tier rules as the build runs them (starting tier after the first 10 games played, cpm &gt; 90) and copies the enrage sheet's Live tab as it stands; the DM reply gives the total, per-status counts, the Not shipped and Editor only keys and when a new player gets their starting tier. | 30 tickets (six analytics/tutorial tickets off, ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Brian and Robert edit; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 30 rows: the 36 rule-1 tickets (31 title matches without Duplicates ZOM-203 and ZOM-276, plus tiers: tickets ZOM-221, 281, 300, 305, 378) minus the six Leonard leaves off (ZOM-30, 49, 50, 161, 262, 275); Live 17, Editor only 9, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force as the build runs them: starting tier set after the first 10 games played (wins and losses), average CPM above 90 to tier 1, everyone else tier 0 (90 exactly stays on tier 0); promotion at 80% or more over up to the last 10 attempts, one win on tier -2; demotion on 4 losses in a row or 50% or lower over up to the last 10; enrage from the sheet Live tab copied as it stands: nine monster rows and MonsterBase 0.8/0.8 with their numbers, and Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP) as not copied yet; DM gives the total 30, the per-status counts, the keys of the Not shipped (ZOM-202, 280, 293) and Editor only (ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315) tickets, and that a new player gets their starting tier after their first 10 games (levels played), from the average CPM of those games. | CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 298-298): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."; SHEET\_LIVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 22-22): "\["MonsterBase (base prefab)", "0.8", "0.8", "0"\], \["Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP)", "not copied yet", "not copied yet", "0"\]"; TCOMMENT\_W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 68-68): "written out (ATK on its own doesn''t)"; CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 72-72): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 74-74): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; CARD\_R1B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "any ticket Blake counts as tier work even if the title doesn''t say so: his closing note on those starts with ''tiers:''"; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 296-296): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "Both were cut from main on Sep 26, and everything difficulty related was merged long before that."; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself; where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; TM\_CPM (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 93-93): "case var cpm when cpm &gt; 90.0f:"; DMT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 44-44): "tell me when a new player gets their starting tier"; DECK\_PROMO (Evals/task\_inputs/01\_Universe\_Inject.sql lines 37-37): "Promotion: win rate of 80% or more over the last 10 attempts moves you up one tier."; Z42MR (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we evaluate UP TO THE MOST RECENT 10 attempts of the player"; WH\_DOC (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 58-58): "/// Get win rate over last n games." |
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
| S | Card rule 5 asks for promotion and demotion 'as they work in the store builds today' and says that where a write-up and the build disagree, go by the build. The build's tier history is appended at the end and cleared on every tier change, and the win-rate check counts from index 0, so promotion and demotion are judged on the first 10 (and first 4) games since the last tier change, not the most recent ones as the deck and ZOM-42 say. The Rules in force tab says that. | 30 tickets (six analytics/tutorial tickets off, ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-250 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Brian and Robert edit; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ and brian.foster@ as editors and leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the twelve Editor only and Not shipped tickets ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the twelve Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 30 rows: the 36 rule-1 tickets (31 title matches without Duplicates ZOM-203 and ZOM-276, plus tiers: tickets ZOM-221, 281, 300, 305, 378) minus the six Leonard leaves off (ZOM-30, 49, 50, 161, 262, 275); Live 17, Editor only 9, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force as the build runs them: starting tier set after the first 10 games played (wins and losses), average CPM above 90 to tier 1, everyone else tier 0 (90 exactly stays on tier 0); promotion and demotion judged on the first games played since the last tier change, not the latest: 80% or more over the first 10 games on the tier promotes, on tier -2 only if the first game there is a win; 50% or lower over the first 10, or losing the first 4 games on the tier, demotes; a player who does neither in those games stays on the tier; enrage from the sheet Live tab copied as it stands: nine monster rows and MonsterBase 0.8/0.8 with their numbers, and Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP) as not copied yet; DM gives the total 30, the per-status counts, the keys of the Not shipped (ZOM-202, 280, 293) and Editor only (ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315) tickets, and that a new player gets their starting tier after their first 10 games (levels played), from the average CPM of those games. | CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself; where a write-up and the build disagree, go by the build."; WH\_LOOP (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 46-46): "for (int i = 0; i &lt; gamesCount; i++)"; WH\_APPEND (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 160-160): "tierWinHistory += win ? "W" : "L";"; WH\_RESET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 26-26): "PlayerPrefs.SetString(TierWinHistoryKey, "");"; TM\_RULE (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 121-121): "WinHistory.GetWorstTierWinRatePossible(rule.NumGames) : WinHistory.GetBestTierWinRatePossible(rule.NumGames)" |

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
Resolution: EXCLUDED. Rule 5 asks for the tier rules as they work in the store builds today and now says that where a write-up (the deck or ZOM-42) and the build disagree, go by the build. The build buckets a player when total games reach 10, and total games are wins plus losses, so the window is the first 10 games played. Leonard's DM asks for the tier numbers 'as they are today', so the DM answer follows the same build fact. 'First 10 levels' read as level plays is the same answer; only 'ten distinct levels' differs, and the build clause excludes it.
Resolution evidence: CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself; where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; WH\_GAMES (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 147-147): "return GetTotalWins() + GetTotalLosses();"; DMNUM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 44-44): "plus the tier and enrage numbers as they are today"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and share list. |
| writes | SAME | Same spreadsheet, shares, Linear comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | Starting-tier window on the Rules in force tab and in the DM answer: first 10 games played (A) vs first 10 distinct levels (K). |

Authority chain: P → DMR → CARD\_R5W

Resolution relevance challenge: Not a strawman: three records (deck, ZOM-42, ZOM-199) say 'first 10 level(s)'. The card's own criterion is how the rules work in the store builds, and the build code fixes the unit as games, wins and losses.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied.
Challenge evidence: CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself; where a write-up and the build disagree, go by the build."; WH\_GAMES (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 147-147): "return GetTotalWins() + GetTotalLosses();"

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
Resolution: EXCLUDED. ZOM-42's 6-7 levels line is provisional ('to be defined later') and the same ticket's rule 1 gives the first 10 levels' average CPM; the deck and ZOM-199 also say first 10. Card rule 5 now says that where a write-up and the build disagree, go by the build, and the build buckets a player when total games reach 10. Leonard's DM asks for the tier numbers as they are today.
Resolution evidence: Z42TBD (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "to be defined later"; Z42S (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "1st 10 level avg CPM &gt; 90 (top 20%) moves to tier 1, rest stays in tier 0)"; DECK\_ST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 37-37): "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0."; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself; where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; DMNUM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 44-44): "plus the tier and enrage numbers as they are today"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Starting-tier timing on the Rules in force tab and in the DM answer: 10 games vs 6-7 levels. |

Authority chain: P → DMR → CARD\_R5W

Resolution relevance challenge: Not a strawman: ZOM-42 is the system ticket rule 4 sends to the rules tab, and its 6-7 sentence is the only text that answers 'when' in so many words. Its own 'to be defined later', its own rule 1, the deck, ZOM-199 and the build all give 10.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: Z42TBD (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "to be defined later"; Z42S (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "1st 10 level avg CPM &gt; 90 (top 20%) moves to tier 1, rest stays in tier 0)"; DECK\_ST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 37-37): "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0."; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself; where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; DMNUM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 44-44): "plus the tier and enrage numbers as they are today"

Compared alternative: R
Resolution: EXCLUDED. Blake's reply, which card rule 6 names as a source on what the build does, says the build checks cpm &gt; 90, not &gt;= 90, and that 90 exactly stays on tier 0; card rule 5 says to go by the build where a write-up disagrees; TierManager.cs line 93 is 'cpm &gt; 90.0f'.
Resolution evidence: REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 129-129): "ZOM-199 says &gt;= but the code never changed from the original spec"; REPLY90 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 129-129): "so 90 exactly stays on tier 0"; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself; where a write-up and the build disagree, go by the build."; TM\_CPM (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 93-93): "case var cpm when cpm &gt; 90.0f:"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set (the ZOM-199 comment is in both). |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Threshold: above 90 vs 90 or more. |

Authority chain: P → DMR → CARD\_R5W

Resolution relevance challenge: Not a strawman: the deck and ZOM-199 both say 90 or more. The reply and the build say otherwise, and rule 5 now settles write-up vs build in favour of the build.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 129-129): "ZOM-199 says &gt;= but the code never changed from the original spec"; REPLY90 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 129-129): "so 90 exactly stays on tier 0"; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself; where a write-up and the build disagree, go by the build."; TM\_CPM (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 93-93): "case var cpm when cpm &gt; 90.0f:"

Compared alternative: S
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. Both readings follow the card. S applies rule 5 literally: the card wants promotion and demotion 'as they work in the store builds today', and the code counts the oldest games in the tier history (appended at the end, cleared on each tier change). A is also a fair reading of the same build: the method's own doc comment says 'Get win rate over last n games', the rule constants (10 games, 80%, 4 games, 50%) match the deck and ZOM-42, and Blake's reply, the card's source on what the build does, flags only the cpm &gt; 90 check for the rules tab. No record (ticket, closing note, test, mail or card line) says which window the rules tab should state, so none of the five checks settles it: both sources are current, the card's authority clause is what both readings apply, and the source, scope and topic are the same. The Rules in force tab content differs.
Resolution evidence: CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself; where a write-up and the build disagree, go by the build."; WH\_LOOP (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 46-46): "for (int i = 0; i &lt; gamesCount; i++)"; WH\_APPEND (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 160-160): "tierWinHistory += win ? "W" : "L";"; WH\_RESET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 26-26): "PlayerPrefs.SetString(TierWinHistoryKey, "");"; WH\_DOC (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 58-58): "/// Get win rate over last n games."; DECK\_PROMO (Evals/task\_inputs/01\_Universe\_Inject.sql lines 37-37): "Promotion: win rate of 80% or more over the last 10 attempts moves you up one tier."; Z42MR (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we evaluate UP TO THE MOST RECENT 10 attempts of the player"; REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 129-129): "ZOM-199 says &gt;= but the code never changed from the original spec"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rules in force tab: promotion and demotion over the latest 10 (and 4 in a row at any time) vs over the first 10 and first 4 games since the last tier change. |

Resolution relevance challenge: Not a strawman: deep recheck passes P1 and P2 raised it independently. Rule 5's 'go by the build' and 'as they work in the store builds today' point to the code, and the code reads index 0 of a history that grows at the end. A is not ruled out either: the same file documents the method as 'last n games', and Blake's rules-tab note names only the cpm check. Not a both-fair figure: it is a rule description, not one reported figure.
Delegation challenge: NOT_CLAIMED. No record delegates the window wording to Julia or accepts either version.
Challenge evidence: CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself; where a write-up and the build disagree, go by the build."; WH\_LOOP (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 46-46): "for (int i = 0; i &lt; gamesCount; i++)"; WH\_DOC (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 58-58): "/// Get win rate over last n games."; REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 129-129): "ZOM-199 says &gt;= but the code never changed from the original spec"

Strongest-alternative challenge (S): S is the strongest alternative and is not excluded: rule 5 sends the reader to the build for promotion and demotion, and the build counts the first games since the last tier change, unlike every write-up; the build's own doc comment and Blake's rules-tab note support A. P remains excluded by rule 3 and the store builds mail.
Challenge evidence: CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself; where a write-up and the build disagree, go by the build."; WH\_LOOP (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 46-46): "for (int i = 0; i &lt; gamesCount; i++)"; WH\_DOC (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 58-58): "/// Get win rate over last n games."

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

**Feasibility:** PASS (5).
- Every ask maps to cataloged tools, and the needed data exists and is tool-visible: card text, checklist items, the DM thread, sheet cells, Linear states and comments (including ZOM-281's note), mail, calendar attendees and repo files (`TierManager.cs`, `WinRateRule.cs`, `WinHistory.cs`).
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
- **Write set:** the same under every reading that survives: one spreadsheet in the folder, four shares (two editors, two commenters), 14 Linear comments (rule 6 with the checklist change and rule 4), and one DM reply. Readings L and P would change the comment set, but quoted records exclude both (UGT above). Fork S changes only what the Rules in force tab says, not the write set; it comes from the sources, not the prompt's wording, and is scored once under UGT.
- **The new DM question has one answer:** "tell me when a new player gets their starting tier" is answered by the build (after the 10th game played), which rule 5 now names as the tie-breaker and which every written source except ZOM-42's provisional "6-7 levels … to be defined later" already agrees with on the number 10.
- A top-level DM message and a thread reply carry the same content to the same recipient.
- There are no "I'll [verb]" statements.
- **Not a fork:** ticking the two checklist items after doing them. The prompt doesn't ask for it, and it changes no register, comment, share or reply content.

**Contrived / Unnatural:** PASS (5).
- Destination and audience are named the way the persona knows them.
- No staged typos, opaque IDs, exact timestamps, trap hints, riddles, audit wording or if-chains.
- "if his rules say something needs to happen on the tickets" is one conditional whose rule lives on the card. It does not hint at the checklist, the thread reply or ZOM-281.

**Alignment with Today's Date:** PASS (5). "tuesday" resolves to 2025-09-30: the DM is at 19:48:26Z (12:48 PT) and the thread reply at 20:07:18Z (13:07 PT). "monday's tuning session/invite" resolves to 2025-10-06T17:00Z (10:00 PT).

**Originality:** N/A (no comparison samples supplied).

**Truthfulness:** PASS (5). Premises PR1–PR5 are verified against revision 20 (the DM, folder, card and invite rows keep their keys, authors and times):
- Leonard's Tuesday DM exists;
- the Monday session and its invite exist;
- the ZM Difficulty folder is unique;
- Leonard's rules are on the card the DM names, with the checklist changes and the revision-20 rule 1 and rule 5 wording.

**Tool Use & Cross-service:** PASS (5). Each service changes a graded fact:
- **Slack:** the six-ticket exclusion, the reply's key lists and the starting-tier question.
- **Linear:** the cohort (including ZOM-281 through its note), the states and the Replaced trigger.
- **Trello:** the rules, the attack-power scope, the build tie-breaker, the comment set and Brian's role.
- **Gmail:** shipped vs Editor only, the cpm rule and the ZOM-199 comment.
- **GitHub:** the tier rules as built, including the 10-game starting window.
- **Sheets:** enrage.
- **Calendar:** the share list.

Writes span Sheets, Drive, Linear and Slack.

**Investigation + Action:** PASS (5). **Coherence (Bolt-on):** PASS (5). **Business Function:** PASS (5), Product. **Complexity Dimensions & Data Seeding:** PASS (5).

---

### Phase 3: Universe Feasibility

**Data Existence:** PASS (5). Every needed entity is verified and retrievable through cataloged reads, including the ZOM-281 note and the tier code.

**Cross-Service Coherence:** PASS (5).
- **New and changed rows (NEW checks):**
  - ZOM-281 note (line 226): author usr_cc3e90160f490686 is arthur.blake@ (Linear `/users/35`); 2025-06-27T09:34:19Z is after the ticket's start (06-26T14:38:06Z) and 22 minutes before completed_at 09:56:19Z, the same pattern as the other four "tiers:" notes; before the clock.
  - Card rule 1 now matches the note: it keys on Blake's "tiers:" closing note, not on his being the assignee.
  - Card rule 5's build clause agrees with Blake's reply (build cpm > 90 vs written >= 90) and with the code; line 58 desc = line 66 `card.desc`.
  - Store builds mail: strips only editor/debug code; ZOM-281 is a gameplay fix, so nothing contradicts it being Live.
  - DM text change (line 44) adds a question and no fact. Apostrophes are doubled throughout.
- **ZOM-42's "6-7 levels" (base Linear, Eval 0 D2):** the ticket marks it "to be defined later" and gives "1st 10 level avg CPM" two paragraphs on; the deck, ZOM-199 and the build all give 10. A provisional line overtaken by the same ticket's rule and the build is not a data inconsistency, and rule 5 tells the reader what to do with it. Not a Snowflake/Confluence conflict.
- **Unchanged rows:** REUSED (byte-identical): thread reply and checklist rows, in-scope closing notes, ZOM-282 naming ZOM-254, Slack authors as channel members.
- **Known base-data issues (not scored):** none touched; the task uses no Snowflake or Confluence data.
- **Build vs write-ups on the promotion/demotion window (task-touched now, scored under UGT, not here):** `WinHistory.GetWinRate` counts from index 0 of a history that grows at the end, while its doc comment, the deck and ZOM-42 describe the latest games. A build differing from its write-ups is the situation rule 5 is written for, not inconsistent data; what is missing is a record saying which version the tab states (fork S).
- **Not task-touched (not scored):** `Monster.cs` passes a single `enrageDamagePercentage`. Keep rubric rows off stacking behaviour.
- Injection SQL considered: Yes. Static integrity evidence: REUSED from `0_injection.md` (same hash, checks A–B); task-relevant Check C items redone above.

---

### Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|-----------|--------------|-------------|---------------|
| Prompt | Unique Ground Truth | 2 | Fork S open: Rules in force promotion/demotion window, latest 10 / 4 in a row (write-ups, doc comment) vs first 10 / first 4 since the last tier change (code, under rule 5). O, P, Q, R and B–N excluded |
| Prompt | Feasibility | 5 | All asks cataloged; data exists |
| Prompt | Persona ACL Reachability | 5 | Every scoped read visible to Julia |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 5 | Same write set under every reading; the starting-tier question has one answer; fork S scored under UGT |
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
| Universe | Cross-Service Coherence | 5 | No inconsistent data; build vs write-up differences are what rule 5 addresses |

---

### Issues Found

**1. Unique Ground Truth, fail-level: the Rules in force tab has two answers for promotion and demotion (fork S).**
- **Where:** card #80 rule 5 (SQL line 58, mirrored at line 66): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today." and "where a write-up and the build disagree, go by the build."
- **The disagreement:**
  - The deck (line 37) says "win rate of 80% or more over the last 10 attempts" and "4 losses in a row". ZOM-42 says "UP TO THE MOST RECENT 10 attempts" and that a 4-loss streak "can still trigger at any time".
  - The build counts the oldest games since the last tier change. In `WinHistory.cs`, results are appended at the end (line 160), the history is cleared on each tier change (line 26), and the loop counts from index 0 (line 46). `TierManager.cs` line 121 uses that history for every rule.
  - The same file documents the method as "Get win rate over last n games." (line 58).
  - Blake's reply flags only the cpm > 90 check "for the rules tab".
- **Effect:** one Agent writes "80% over the latest 10 / 4 losses in a row" and another writes "80% over the first 10 games on the tier / losing the first 4 games on the tier". Both cite the card, and no record picks between them, so a rubric row on promotion or demotion cannot be graded fairly.
- **Minimum fix (SQL; the prompt can stay as it is):** settle the window in a record the card already points to. Options, simplest first:
  1. Add one sentence to Blake's reply (the card's source on what the build does) saying which games the promotion and demotion checks count. Change every copy of the reply identically: the body at lines 99, 101, 103, 105 and 107, and the snippets at lines 79–95 if the sentence falls inside the snippet. If you state the build's real behaviour, it is "the first 10 games (first 4 for the loss rule) since the last tier change, not the latest". Check that against `WinHistory.cs` before you write it.
  2. Or narrow the card so the tab doesn't depend on the window. Limit rule 5's "go by the build" clause to the starting tier, and have promotion and demotion copied from one named write-up (ZOM-42, which has both demotion rules; the deck lists only the 4-loss rule). The "as they work in the store builds today" wording would then need to change for promotion and demotion as well.
- Whichever you pick, the OEs and rubric must state the same window, or stay off the window entirely.

### Recommended Improvements (not scored)

1. **After fixing Issue 1, update the OEs and rubric to revision 20 (the revision-17 ones no longer match the answer).**
   - **Scope:** 30 tickets. ZOM-281 "Win streak not lost when replaying without main menu" is in (Blake's "tiers:" note) with status Live. ZOM-30, 49, 50, 161, 262 and 275 stay off; ZOM-378 stays on.
   - **Counts:** Live 17, Editor only 9, Replaced 1, Not shipped 3.
   - **Comments:** unchanged, 14 in total: ZOM-199 (the build checks cpm > 90); ZOM-254 (replaced by ZOM-282); the 9 Editor only tickets (ZOM-162, 163, 173, 200, 201, 250, 277, 312, 315) and the 3 Not shipped tickets (ZOM-202, 280, 293): the change isn't in the store builds. ZOM-42 and ZOM-281 get none.
   - **Shares:** unchanged: robert@ and brian.foster@ can edit; leonard.hayes@ and arthur.blake@ can comment.
   - **DM reply:** the total 30, the per-status counts, the Not shipped and Editor only keys, and when a new player gets their starting tier: after their first 10 games (levels played), from the average CPM of those games, above 90 to tier 1 and everyone else tier 0.
2. **Grading the starting-tier answer:** credit "after the first 10 levels" or "after 10 games played". Fail "after 6-7 levels". Don't fail "levels" wording unless the answer says replays or losses don't count. If a row also checks the threshold, it is above 90 (90 exactly stays on tier 0).
3. **Keep the earlier settled forks:**
   - Mailman, Mayor2 and PartyGirl (incl. PartyGirl 50HP) go on the Rules in force tab as not copied yet.
   - ZOM-271 is out.
   - Demotion has two rules (4 losses, or 50% or lower over 10 games). Which games those count depends on how you settle Issue 1. Until then, don't grade "latest 10" or "in a row" wording either way. This replaces the last round's advice to grade "over up to the last 10".
4. **Don't grade ticking the checklist items.** The prompt doesn't ask for it.
5. **Optional wording**, carried from earlier rounds: "then reply to leonard in the dm…" could follow Leonard's own condition and read "once it's in the folder, reply to leonard in the dm with what he asked for." If you change it, put it in your own voice; prompts are screened for AI-written text. A prompt change outdates every pass that reads the prompt.

---

## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5), each a fresh subagent blind to the main review.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 7 sentences, 40 forks | 4 | 1 |
| P2 | 7 sentences | 6 | 1 |
| P3 | 7 sentences | 1 | 0 |
| P4 | 7 sentences | 1 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P1 | "go through his ask and everything it points to and build the register the way he set it up." | Card #80 rule 5 (SQL line 58) "as they work in the store builds today" / "where a write-up and the build disagree, go by the build."; `WinHistory.cs` line 46 `for (int i = 0; i < gamesCount; i++)`, line 160 append, line 26 reset; deck line 37 "over the last 10 attempts" | common_errors §2 | Unique Ground Truth | CONFIRMED | Opened all cited lines. The code counts the first 10 and first 4 games since the last tier change; the write-ups say the latest. Rule 5 supports the build reading, and nothing rules it out. The write-up reading is also supported, by the method's doc comment (line 58 "Get win rate over last n games.") and by Blake's reply flagging only cpm > 90 "for the rules tab". Recorded as fork S, UNRESOLVED_MATERIAL_DIFFERENCE. |
| DR2 | P2 | "build the register the way he set it up." | Same records as DR1; ZOM-42 (`/issues/3485`) "UP TO THE MOST RECENT 10 attempts" | common_errors §2 | Unique Ground Truth | CONFIRMED | Same fork as DR1, found independently. Merged into fork S. |
| DR3 | P1 | "if his rules say something needs to happen on the tickets, go ahead and do that too." | Checklist "Before Monday" items "rule 6 change: …" / "rule 7 change: …" (SQL lines 72, 74), state incomplete; comment "rest of the card stands." 15:41:55Z | common_errors §2 | Unique Ground Truth | REJECTED | Reading B (card as first written) is ruled out by the check items themselves. Leonard, the card's author, labels them "rule 6 change" and "rule 7 change" and added them at 16:20:11Z (addChecklistToCard, line 76), after his "rest of the card stands." comment. A "Before Monday" checklist is unticked because the work isn't done yet. Same as fork L. |
| DR4 | P2 | "if his rules say something needs to happen on the tickets, go ahead and do that too." | Same checklist and comment rows as DR3 | common_errors §2 | Unique Ground Truth | REJECTED | Same as DR3 (rule 6 comment set). |
| DR5 | P2 | "share it with everyone on monday's tuning invite." | Check item "rule 7 change: Brian gets edit as well, he''ll fix rows during the session" (line 74) | common_errors §2 | Unique Ground Truth | REJECTED | Same as DR3 (rule 7 role). |
| DR6 | P1 | "then reply to leonard in the dm with what he asked for." | DM `6f773865…` "reply here when it''s in the folder"; thread reply `33c941fa…` | common_errors §2 | Clarity | REJECTED | A thread reply and a top-level message go to the same DM, the same recipient and carry the same content. Not material; accept either. |
| DR7 | P1 | "build the register the way he set it up." | Linear ZOM-162 (`/issues/3203`) "Dynamic difficulty tracks are linked across tiers in level editor"; note "closing. works on the dev build"; store builds mail (line 85) "A ticket whose changes are only level editor or debug tooling never reached players" | common_errors §2 | Unique Ground Truth | REJECTED | The Live reading is ruled out by the ticket itself: the title and description place the defect in the level editor's tier-track cloning ("in the level objects", "The play button still only plays default tier 0"). No record ties it to runtime code, and rule 3's shipped authority strips editor-only changes. Stays Editor only. |
| DR8 | P2 | "build the register the way he set it up." | `TierManager.cs` line 30 `if (totalGames == 10)`; `WinHistory.cs` line 147 | common_errors §2 | Unique Ground Truth | REJECTED | 10th level vs 10th game played: same as fork K, excluded by rule 5's build clause, the bucketing line and total games = wins + losses. |
| DR9 | P2 | "put it in the zm difficulty folder and share it with everyone on monday's tuning invite." | Folder `d_96489e1e00a56685625939` owner leonard.hayes@ | common_errors §4 | Feasibility | REJECTED | Not fail-level. Whether a file-level commenter role applies to a folder owner is runtime behaviour the export can't show. Kept as an evidence limit; keep OEs and rubric off Leonard's exact role. |
| DR10 | P2 | (SQL) | Schema snapshot: columns not listed for some inserted tables | Eval 0 A1/A2 | Data seeding | REJECTED | The bundled schema is an unverified snapshot. Eval 0 lint shows 0 FAIL and records these as advisories A1–A2; not a demonstrated defect. |
| DR11 | P3 | (SQL) | `linear_comments.sequence`, `slides_pages.notes`, `slides_page_elements.table_json` / `ordinal` | Eval 0 A1/A2 | Data seeding | REJECTED | Same as DR10: an unverified snapshot, recorded as an advisory. |
| DR12 | P4 | "then reply to leonard in the dm with what he asked for." | DM `6f773865…` (line 44) "reply here when it''s in the folder with how many tickets made the list…" | common_errors §6.6 | Command list | REJECTED | §6.6 defines the failure as a "first / then / finally" list, and Eval 1 §1.3.1 asks whether the prompt prescribes a step-by-step procedure. Here there is one lowercase "then", with no first or finally, and the order is Leonard's own condition. The optional rewording is kept under Recommended Improvements. |

Effect on verdict: Unique Ground Truth drops from 5 to 2 on fork S (DR1/DR2), so the overall verdict is FAIL, capped at the UGT score. Every other dimension is unchanged. P1's own derivation of the rest matches the main review: 30 tickets; Live 17 / Editor only 9 / Replaced 1 / Not shipped 3; 14 comments; Robert and Brian edit; starting tier after 10 games played, cpm > 90.

Fork list:
- F1 / S: OPEN | Promotion/demotion over the latest 10 and 4 in a row (deck line 37 "over the last 10 attempts"; ZOM-42 "UP TO THE MOST RECENT 10 attempts"; `WinHistory.cs` line 58 "Get win rate over last n games.") | Over the first 10 and first 4 games since the last tier change (rule 5 "as they work in the store builds today", "go by the build"; `WinHistory.cs` lines 26, 46, 160) | Missing: a persona-visible record, for example Blake's reply that the card names as the source on the build, or a card line, saying which games the promotion and demotion checks count
- F2 / L: settled | Checklist in force: 14 comments, Brian edits | Unchecked items pending: 2 comments, Brian comments | Settled by: check items "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds" and "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; addChecklistToCard 2025-09-30T16:20:11Z, after the "rest of the card stands." comment at 15:41:55Z
- F3 / O: settled | ZOM-281 in | Out (assignee isn't Blake) | Settled by: rule 1 "his closing note on those starts with ''tiers:''"; note by usr_cc3e90160f490686 = arthur.blake@ (Linear `/users/35`) "tiers: closing. checked on the dev build"
- F4 / P: settled | ZOM-281 Live | Not shipped (no PR names it) | Settled by: rule 3 names Blake's store builds mail; mail "everything difficulty related was merged long before that"; ZOM-281 Done 2025-06-27T09:56:19Z
- F5 / Q: settled | Starting tier after 10 games | After 6-7 levels | Settled by: ZOM-42 "to be defined later"; rule 5 "go by the build"; `TierManager.cs` "if (totalGames == 10)"
- F6 / R: settled | cpm > 90 | 90 or more | Settled by: Blake's reply "so 90 exactly stays on tier 0"; `TierManager.cs` "case var cpm when cpm > 90.0f:"
- F7 / K: settled | First 10 games played | First 10 distinct levels | Settled by: rule 5 build clause; `WinHistory.cs` "return GetTotalWins() + GetTotalLosses();"
- F8 / M: settled | ZOM-378 on | Off as a tutorial ticket | Settled by: DM reply "(30, 49, 50, 161, 262 and 275)"; ZOM-378 note "tiers: closing. level 1 is back in the list…"
- F9 / N: settled | Only the six listed tickets off | Editor-tooling tickets off too | Settled by: DM reply "put the keys of the not shipped ones and the editor only ones"
- F10 / J: settled | ZOM-271 out | In | Settled by: Leonard's comment "written out (ATK on its own doesn''t)"
- F11 / H, I: settled | Enrage Live tab as it stands | MonsterBase 0.8/0.8 or PartyGirl 0.6/0.6 | Settled by: rule 5 "Copy its Live tab as it stands"
- F12 / G: settled | ZOM-254 Replaced by ZOM-282 | ZOM-254 Live | Settled by: ZOM-282 note "this replaces the blunder 2.0 boost from ZOM-254"
- F13 / B: settled | ZOM-282 Live | Replaced by match3d#401 | Settled by: rule 4 "PRs that change or split its numbers"
- F14 / F: settled | ZOM-250 Editor only | Replaced by ZOM-277 | Settled by: ZOM-277 note "nothing changes in the game itself"
- F15 / C: settled | No comment on ZOM-42 | Correction comment on ZOM-42 | Settled by: rule 6 "Every other ticket stays as it is, ZOM-42 … included"
- F16 / D: settled | ZOM-23 in | Out under a Pacific start | Settled by: scope "so everything since we started ZM"
- F17 / E: settled | Share with the invite only | Also post in #zombie-design | Settled by: prompt "share it with everyone on monday's tuning invite"
- F18: settled | ZOM-162 Editor only | Live | Settled by: ZOM-162 title "…in level editor"; mail "only level editor or debug tooling never reached players"
- F19: not a fork | DM top-level reply | Thread reply | Same recipient and content
- F20: not a fork | Leave the checklist items unticked | Tick them | Not asked; changes no graded content

Platform defects: none.

### FINAL VERDICT: FAIL

Score: 2

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Clock: Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Next action: Settle which games the promotion and demotion checks count in a record the card points to (Issue 1; for example one sentence in every copy of Blake's reply), then send /injection, /prompt, /hardness, /oe and /rubric in that order. Bring the OEs and rubric to revision 20 with the same window.

Evidence limits: The Evals/Docs PDFs were not re-extracted; Eval 1's restated bands and overrides were applied. Runtime acceptance of the `commenter` share role (including on a folder Leonard owns) is unverified (declared parameters only). Eval 0 checks A–B were reused from the same-hash 0_injection.md, because this portal never writes the gate manifest. Byte-identical SQL rows reuse prior /prompt facts under stage-evidence-v1.

**Lowest Dimension:** Unique Ground Truth (2). The Rules in force tab can state promotion and demotion over the latest games (deck, ZOM-42, the build's doc comment) or over the first games since the last tier change (the code rule 5 says to follow), and no record picks one.

**Summary:** The prompt is unchanged and everything else in revision 20 resolves. ZOM-281 is in and Live (30 tickets: Live 17 / Editor only 9 / Replaced 1 / Not shipped 3), the comments and shares are unchanged, and the starting tier comes after 10 games played at cpm > 90. But rule 5's new "go by the build" clause sends the reader to code that counts a different promotion/demotion window from every write-up, and that fork fails Unique Ground Truth. One clarifying sentence in a source the card already names fixes it.

Eval version: task-quality-v1

Eval release SHA-256: 0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e

Reviewed prompt SHA-256: 22f26066688cedbe94c9c8abfcdd34194db335667d7a195fc499d4d87ede1787

Review context SHA-256: 423ac833b9e83d44cfd519f81fd3cca606d71499d169eea278bee90cd4ee80bb

Prompt record SHA-256: a9ee144c4faaaf8db68e30d6a68b84c3282da8d31bf84dcf42821ac464e717b9
