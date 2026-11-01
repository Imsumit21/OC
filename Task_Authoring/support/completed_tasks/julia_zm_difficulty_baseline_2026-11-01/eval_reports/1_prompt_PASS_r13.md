## PROMPT EVALUATION REPORT

### Task: Julia delegates Leonard's ZM difficulty baseline. The Agent builds the register (Tickets + Rules in force) from the Trello card rules, Leonard's card comment, his "notes for monday" doc, the "Before Monday" checklist, his Tuesday DMs (both thread replies) and Robert's three extra columns from the group chat the card names, using Blake's store builds mail and his reply to it. It then files the register in ZM Difficulty, shares it with the Monday invite, comments on tickets per rule 6 as changed (with the two store builds on the Editor only and Not shipped comments), and replies to Leonard in the DM.
### Assigned Persona: Julia Lawson - Product Manager (roster `julia_lawson`, julia.lawson@harmonygames.co)
### Assigned Business Function: Product
### Assigned Competency: Engineering Ops
### Assigned Task Skill: Retrieval
### Assigned Horizon: long-horizon (Task Type field; Difficulty Mode "medium" recorded as context)

Review: `/prompt`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode. Actual review date 2026-10-31. Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Universe `Universe_SynthCut` (hg4-synth-sep30cut v16). Eval release task-quality-v1 (manifest SHA-256 `0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e`, verified with `hg_eval_release.py snapshot prompt`).

Binding:
- Reviewed prompt SHA-256: `22f26066688cedbe94c9c8abfcdd34194db335667d7a195fc499d4d87ede1787`
- Review context SHA-256: `d9724d9c4730ae72a803045c4d4d4d17b8672fe52d70eb848ef470468207dde1`
- Prompt record SHA-256: `7a83628e0a121ecad615e411177b42c0180e9f1d397a339961c8615c1ab7ef22` (policy prompt-source-checks-v2, format 2)

Inputs:
- `04_Prompt.txt`: revision 46 (attached as `04_Prompt (13).txt`), 525 bytes, sha256 `22f26066…1787`. Byte-identical to the prompt graded last round (revision 43).
- `00_Task_Assigned_Inputs.md`: all five fields stated, so intake is clear.
- `01_Universe_Inject.sql`: revision 45, 98,831 bytes, 397 lines, sha256 `f6afeda7b08647d790a5d96b5bd7ccb2cb6291d83fadf4bd9f2ae2a79f5362f8`. Changed since the revision graded last round (revision 42, `7966b149…20c5b8`):
  1. **Lines 47–50 (new):** two messages in group DM `CAFC495E4006` (`mpdm-robert--leonard.hayes--julia.lawson-1`).
     - Leonard, 2025-09-30T10:01:01Z: "robert anything you want on julia's difficulty list for monday? she's putting it together from the card".
     - Robert's thread reply, 10:51:53Z: "yeah three things after status please. who it's assigned to in linear, the day it got marked done (leave it blank if it never got done), and its linear priority. i want to sort by them in the session".
  2. **Card rule 2 (line 73, and its updateCard action at line 81)** now ends: "Layout as in the session agenda, plus the three things Robert asked for when I asked him in our group chat."
  3. **Header comment** now says 179 INSERT. Every line from 48 on shifted +4. All 123 SQL anchors in the check record were re-found by content at their new lines (0 misses).
- No error/async config, dynamic context or reference files were supplied, and the prompt references none. A saved Agent trajectory, OEs and rubric exist in the workspace; under stage ownership none were opened.
- Evidence contract `stage-evidence-v1`.
  - **Reused:** facts from the prior `1_prompt.md` that rest on byte-identical SQL rows or unchanged base records. That covers the whole revision-42 answer: 24 tickets, statuses, 9 comments with builds, shares, the Rules in force tab and the DM reply.
  - **NEW:** the two group-DM messages and card rule 2's new sentence; group DM membership (`channels.json`); a check of every group chat that includes Leonard, Robert and Julia for a competing ask; Linear assignee, `completed_at`, `canceled_at`, state and priority for all 24 tickets (and the 4 removed ones); the Linear user records behind the assignees; the requirement ledger row; new forks AF–AI; the deep recheck.

**What this round changes.** The answer stays 24 tickets and 9 comments with the same shares and DM reply. The Tickets tab gains three columns after Status: Linear assignee, the day the ticket was marked done (blank if never done) and Linear priority. Card rule 2 points to them ("the three things Robert asked for when I asked him in our group chat"), and Robert's reply sits in a group DM Julia belongs to. It's the only exchange of its kind in any of Julia's group chats with Leonard and Robert.

---

### Injection Gate
- **State:** NEVER_REVIEWED. The gate reads `reports/input_manifest.json`, which this portal's report writer never creates.
- **Eval 0 handling:** `0_injection.md` (injection-static-v2, review date 2026-10-31) reviews the identical SQL hash `f6afeda7…62f8` (revision 45): **FINAL VERDICT: PASS**, COMPLETE. Re-ran `hg_injection_lint.py --summary` on the saved SQL here: 0 FAIL / 0 CHECK / 0 INFO. Its static checks A–C are REUSED. The task-relevant Check C items for the new rows were redone here (Phase 3).
- **Reviewed SQL sha256:** `f6afeda7b08647d790a5d96b5bd7ccb2cb6291d83fadf4bd9f2ae2a79f5362f8`. Eval 0 verdict: PASS.
- **Eval 0 findings on records this prompt depends on:**
  - C-6: Robert's columns are only in the group DM. Checked here: discoverable and visible to Julia; the notes doc's different "three things" list is fork AH, settled.
  - C-7: the new messages are at 03:01 and 03:51 PT. Odd hours, but before the 14:04:31Z card update that cites them; not a defect.
  - G1: off-snapshot GitHub columns, carried.
  - None of these changes a graded value.

---

### Phase 0: Sources read

Docs and references:
- Eval 1, read in full this run: Local Overrides, §1.3 anti-patterns, §2.1 UGT, Phase 3.2, common mistakes.
- `prompt_rubric_reliability.md` (release binding verified); `deep_recheck.md`, including the known platform defects and the edge-value rule; `common_errors.md`.
- `ENVIRONMENT.md` "Clock and outputs" ("If the Pacific date and the UTC date are different, accept either.").
- `acl.md` and `roster.json`; `known_base_issues.md`; the Linear section of `catalog.json`.
- The `Evals/Docs` PDFs were not re-extracted; Eval 1's inline bands and Local Overrides were applied (evidence limit, unchanged from earlier rounds).

Universe exploration, NEW this round:
- **Group DM membership.** `channels.json` `CAFC495E4006`: is_mpim true, members EMPLOYEE_0005 (Julia), EMPLOYEE_0016 (Robert), EMPLOYEE_0038 (Leonard), PERSON_6089. Both new authors are members.
- **Other group chats.** Besides `CAFC495E4006`, Julia shares five other group DMs with Leonard and Robert (`C50582A0294E`, `C563003C8E31`, `C63EBB96E93C`, `CD3556EC8108`, `CEF62B24B47E`). None has a September 2025 base message file (latest 2025-06), and the SQL adds Slack rows only to `CAFC495E4006`, `D05HB64NMQU`, `C090N54TG79` and `C093LEZGF6J`. So Robert's reply is the only answer to "when I asked him in our group chat".
- **Linear fields for the 24 tickets** (`linear/data.json` `/issues`; no SQL row touches a Linear issue, only comments):

| Status | Ticket: assignee, priority, completed_at (UTC) |
|---|---|
| Live | ZOM-23 Robert, 1, 2025-05-16 · ZOM-42 arthur.blake@, 1, 05-30 · ZOM-45 arthur.blake@, 2, 06-23 · ZOM-199 arthur.blake@, 1, 06-23 · ZOM-221 arthur.blake@, 1, 06-23 · ZOM-246 EMPLOYEE_0032_NAME, 1, 06-16 · ZOM-263 EMPLOYEE_0032_NAME, 2, 06-16 · ZOM-274 EMPLOYEE_0032_NAME, 1, 06-21T01:17:25Z · ZOM-281 EMPLOYEE_0032_NAME, 1, 06-27 · ZOM-282 arthur.blake@, 1, 06-21T01:17:19Z · ZOM-288 Robert, 1, 07-08 · ZOM-295 owen.baker@, 1, 07-04 · ZOM-300 arthur.blake@, 1, 06-25 · ZOM-303 arthur.blake@, 2, 07-08 · ZOM-305 arthur.blake@, 1, 06-26 · ZOM-378 arthur.blake@, 1, 07-14 |
| Editor only | ZOM-173 arthur.blake@, 2, 07-08 · ZOM-200 arthur.blake@, 1, 06-13T01:17:38Z · ZOM-277 arthur.blake@, 1, 06-20 · ZOM-315 arthur.blake@, 3, 07-02 |
| Replaced | ZOM-254 EMPLOYEE_0032_NAME, 1, 06-23 |
| Not shipped | ZOM-202 arthur.blake@, 3, none (In Progress) · ZOM-280 EMPLOYEE_0032_NAME, 2, none (Canceled 2025-06-20T23:38:27Z) · ZOM-293 Robert, 4, none (Todo) |

- **Assignee names** come from Linear `/users`: `usr_Robert` "Robert"; `usr_cc3e90160f490686` and `usr_4e13bd40cc73d0fc` carry the email as their name; `usr_EMPLOYEE_0032` (`/users/21`) has name "EMPLOYEE_0032_NAME" and email "EMPLOYEE_0032_EMAIL", an anonymized token. No persona-visible record maps it to a real name (Slack `EMPLOYEE_0032_SLACK_ID` is also a token).
- **Pacific vs UTC day:** three completed_at instants fall between 00:00 and 07:00 UTC, so their Pacific day is one earlier: ZOM-200 (06-12 PT), ZOM-274 and ZOM-282 (06-20 PT). Under ENVIRONMENT.md and deep_recheck's edge-value rule, either day is accepted for a single instant; not a fork.
- **Priority:** stored as integers 1–4 (no label field in the export). Linear's labels map 1 Urgent, 2 High, 3 Medium, 4 Low. The number and the label are the same value.

Status derivation under the leading reading (shows solvability; not a golden answer):
- **Live 16:** ZOM-23, 42, 45, 199, 221, 246, 263, 274, 281, 282, 288, 295, 300, 303, 305, 378.
- **Editor only 4:** ZOM-173, 200, 277, 315.
- **Replaced 1:** ZOM-254, replaced by ZOM-282.
- **Not shipped 3:** ZOM-202, 280, 293.
- **Total 24.**
- **Tickets tab columns:** ticket, title, Linear state, status, then Robert's assignee / done day / priority, and the replacing ticket for Replaced (the three columns may also follow the replaced-by column; see fork AG). Done day is blank for ZOM-202, 280, 293.
- **Comments (9):**
  - ZOM-199: the build checks cpm > 90, so 90 exactly stays on tier 0.
  - ZOM-254: replaced by ZOM-282.
  - ZOM-173, 200, 277, 315, 202, 280 and 293: the change isn't in the store builds, iOS 0.3.49 and Android 0.3.133.
  - None on ZOM-162, 163, 201 or 250.
- **Shares:** robert@ edit; brian.foster@ and leonard.hayes@ comment; arthur.blake@ view.
- **DM reply:** the total, per-status counts, the Not shipped and Editor only keys, that ZOM-282 replaced ZOM-254, and that a new player gets their starting tier when their 10th game ends (wins and losses counted).

---

### Requirement ledger

authority_contract: prompt-incorporation-v1

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Find Leonard's Tuesday DM ask, including both thread replies | SQL 52 (request, 19:48:26Z), 58 (reply 20:07:18Z), 62 (reply 21:16:42Z under Julia's line-60 message) | Slack DM history; threads via reply_count | `slack_conversations_history`, `slack_conversations_replies` / `slack_read_thread`, search | Julia (EMPLOYEE_0005) is a DM member | The register; ten tickets off; build numbers in seven comments; reply contents |
| "everything it points to": card rules | Card #80 (line 73), updateCard (81), commentCard (83), checklist and items (84–91) | DM names "the difficulty baseline card on the zm roadmap board" | `trello_get_cards_on_board`, `trello_get_card`, `trello_get_card_actions`, checklist reads | Trello unscoped | Rules 1–7, the attack-power addendum, the rule 6 change (the rule 7 change later withdrawn) |
| **"everything it points to": Robert's three columns (NEW)** | Card rule 2 (line 73) "plus the three things Robert asked for when I asked him in our group chat"; group DM `CAFC495E4006` lines 48 and 50 | Slack search for Robert's messages or "difficulty list"; Julia's group DMs (`slack_conversations_list` / history) | Slack history / replies / search | Julia is a member of `CAFC495E4006` | Assignee, done day (blank if never done) and priority columns after Status |
| Assignee, done day, priority per ticket (NEW) | Linear `/issues` `assignee_id`, `completed_at`, `priority`; `/users` names | `linear_get_issue` / `linear_list_issues`; `linear_list_users` | Linear reads | Linear unscoped | 24 × 3 cells; done day blank for ZOM-202, 280, 293 |
| "everything it points to": notes on the card | Trello attachment (93) → Google Doc (21), Drive file (12) | Card attachment; Drive search | `trello_get_attachments`, `gdrive_search`, `gdocs_get_document_text` | Doc shared with Julia as reader | ZOM-258 off; Arthur view; reply says which ticket replaced which |
| Ticket scope | Linear ZOM issues; "tiers:" notes; PR #265 review comment; Trello comment; both DM replies; notes | Linear search/list; comments; PR lookup | Linear reads; GitHub PR reviews/comments | Linear, GitHub unscoped | 24 tickets |
| Status per ticket (rules 3–4) | Blake's store builds mail (Julia's copy line 100) and his reply (line 138, own thread); Linear states and closing notes | Gmail search; Linear | Gmail search/read; Linear reads | Julia's mailbox (both mails INBOX); Linear unscoped | Live 16 / Editor only 4 / Replaced 1 / Not shipped 3 |
| Rules in force tab (rule 5) | Deck, ZOM-42, Blake's reply, enrage sheet Live tab, `TierManager.cs`, `WinRateRule.cs`, `WinHistory.cs`, `GameLoader.cs` | GSlides, Linear, Gmail, GSheets, GitHub | `gslides_get_presentation_text`, Linear get, `gsheets_values_batch_get`, `github_get_file_contents` | Deck shared; sheet owned by Julia; GitHub, Linear unscoped | Unchanged from last round |
| Build the register: one sheet, tabs Tickets + Rules in force | Agenda doc (line 19); card rule 2 | GDocs | `gsheets_create_spreadsheet`, `gsheets_batch_update`, `gsheets_values_update` | Write (ACL-free) | New spreadsheet |
| Put it in the ZM Difficulty folder | Prompt; card rule 7 | Drive folder d_96489e1e00a56685625939 | `gdrive_move_file` (or create with parent) | Julia is writer | File in folder |
| Share with everyone on Monday's invite | Prompt; card rule 7; notes (Arthur); line 62 (Brian) | GCal event on Julia's calendar (line 159) | `gdrive_share_file` (role param) | Julia's own calendar | robert@ writer; brian.foster@ and leonard.hayes@ commenter; arthur.blake@ reader |
| Ticket comments (rule 6 as changed) | Card rule 6; checklist item; Blake's reply; rule 4; line 58 (builds); line 62 ("no comments on them either") | Linear | `linear_create_comment` | Write | 9 comments; the seven Editor only / Not shipped ones name iOS 0.3.49 and Android 0.3.133 |
| Reply to Leonard in the DM | DM, both thread replies, notes | Slack | `slack_send_message` | Write | Total, per-status counts, Not shipped and Editor only keys, ZOM-282 replaced ZOM-254, starting-tier timing |

Output capability: creating the spreadsheet and its tabs, moving it into the folder, sharing, the Linear comments and the Slack reply are SUPPORTED by declared catalog tools. The `commenter` and `reader` roles are free strings for `gdrive_share_file` `role`; their runtime acceptance is UNVERIFIED (an evidence limit, not a failure). `catalog.json` lists no return schemas, so how `linear_get_issue` renders assignee, `completed_at` and priority is an evidence limit. The raw fields exist for every ticket.

Dimensional feasibility (T10): "who it's assigned to" → `assignee_id` + `/users` name; "the day it got marked done" → `completed_at`; "its linear priority" → `priority`. All three fields exist on all 24 issues. Feasible.

---

### Phase 1: Prompt Structure & Persona (prompt byte-identical; re-judged against revision-45 sources)

**Persona:** PASS (5). Exact roster entry; a CEO delegating to a PM fits the role. The card says "Julia owns this one", and Leonard tells Robert "she's putting it together from the card".

**Assigned Competency:** PASS (5). Engineering Ops: reconciling tickets with what shipped in store builds, PR review marks and the build code; a batch of ticket comments that cite the builds checked; a register that carries ticket ops fields (assignee, done day, priority).

**Assigned Task Skill:** PASS (5). Retrieval is the core work:
- every in-scope ticket across title rules, closing notes and a PR review;
- each ticket's state, shipped status, assignee, done day and priority;
- six late instruction layers: card comment, notes, checklist, two DM thread replies, and Robert's group-DM columns.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. PASS. Data seeding: PASS.
- **Dynamic Change:** the 21:16Z reply withdraws the checklist's Brian edit and removes four tickets; the 20:07Z reply adds build numbers to the rule 6 comments.
- **Friction, new:** the three extra columns live in a group DM the card only points at ("our group chat"), while the notes doc attached to the same card carries a different "three things for the register" list.
- **Friction, carried:** Blake's reply in its own thread; ZOM-312 removed by a PR review comment; ZOM-258 by the notes; Arthur's role from the notes; ZOM-173, 277 and 315 kept as Editor only.

**Naturalness:** PASS. First person, lowercase and casual; no document formatting, polished connectives or enumerated specs.

**Anti-Patterns:**

| Pattern | Status |
|---------|--------|
| Command List | PASS. No "first"/"finally" steps or numbered procedure. The one lowercase "then" orders the final reply after the filing, which Leonard's own ask requires ("reply here when it''s in the folder") |
| Bolt-On | PASS. Every sentence serves the baseline |
| Pre-Solving | PASS. No counts, tickets, statuses, exclusions, builds, columns, timings or causes named |
| Tool Mention | PASS. "dm", "folder", "invite" and "tickets" are natural nouns |

**Diversity:** a two-tab sheet with source-defined columns, folder placement, role-based sharing with three roles, a batch of Linear comments with source-defined content, and a DM reply over a source-defined cohort with a rules answer.

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** PASS (5). Every fork is settled by a prompt sentence or a persona-visible record. New this round:
- **AH (strongest): "the three things Robert asked for" read as the notes doc's "three things for the register". EXCLUDED** by source identity.
  - The card names Robert and "our group chat". The notes doc is Leonard's own Google Doc to Julia.
  - The only such exchange is Leonard's "robert anything you want on julia''s difficulty list for monday?" and Robert's "yeah three things after status please. …" in `CAFC495E4006`, which Julia belongs to. Both lists apply.
- **AF: leave the three columns out. EXCLUDED** by card rule 2 ("plus the three things Robert asked for when I asked him in our group chat") and Robert's reply naming them.
- **AI: fill the cancel day for ZOM-280. EXCLUDED** by "(leave it blank if it never got done)"; Linear shows `canceled_at` 2025-06-20T23:38:27Z, `completed_at` null.
- **AG: the three columns after the replaced-by column instead of straight after Status. SAME MATERIAL RESULT.** Both are "after status" with the same cells; Robert's purpose is sorting; the agenda fixes no column positions. The rubric should accept either placement after Status.
- **AJ (raised by the deep recheck): ZOM-199 Not shipped because its ">= 90" text never reached the build. EXCLUDED.**
  - Card rule 1 defines Not shipped by lifecycle ("open, cancelled and never-merged ones are in, as Not shipped"). ZOM-199 is Done, and Blake says "everything difficulty related was merged long before that."
  - Rule 6 handles a ticket whose text Blake says is wrong with a separate comment, "what the build does", which only fits a ticket whose change is in the build.
- **Not forks:**
  - Pacific vs UTC done day for ZOM-200, 274, 282: either day is accepted for one instant (ENVIRONMENT.md; deep_recheck edge-value rule).
  - The `EMPLOYEE_0032_NAME` assignee token on six tickets: correct as shown; deep_recheck known platform defects, anonymized tokens.
  - Priority as a number or a label: the same value.
- **Earlier forks B–AE:** excluded on rows byte-identical to revision 42, re-anchored by content.

**Feasibility:** PASS (5). All asks map to cataloged tools; all data exists, including the three new column fields on every ticket (ledger above).

**Persona ACL Reachability:** PASS (5). Every scoped read is visible to Julia: the group DM `CAFC495E4006` (member), both DM threads (IM member), her mailbox (both Blake mails, INBOX), her calendar (invite), Drive files shared with or owned by her. Trello, Linear and GitHub are unscoped.

**Truthfulness:** PASS (5). Five premises verified (record PR1–PR5): the Tuesday DM (2025-09-30T19:48:26Z, a Tuesday in PT and UTC), Monday's tuning session and invite (2025-10-06, line 159), the ZM Difficulty folder, and Leonard's rules on the card. Nothing the prompt treats as done is after the clock.

**Tool Use & Cross-service:** PASS (5). Each service changes a graded fact:
- Slack: the ask, exclusions, builds in comments, Brian's role, Robert's columns.
- Trello: the rules.
- Linear: scope, states, assignee, done day, priority, comments.
- Gmail: shipped status, the Editor only rule, cpm > 90 and timing.
- GitHub: the ZOM-312 removal, build rules.
- Drive/Docs/Sheets/Slides: notes, enrage numbers, deck, register.
- Calendar: the share list.

**Investigation + Action:** PASS (5). The investigation feeds the sheet, the shares, the comments and the reply.

**Clarity & Specificity:** PASS (5). Every reading posts the same 9 comments on the same tickets and builds the same columns; the column set, build numbers and ZOM-199 content are source-defined. No "I'll" statements.

**Contrived / Unnatural:** PASS (5). No opaque ids, timestamps, trap hints, hidden destinations, audit-form wording or if-chains in the prompt. Robert's columns sit in the group DM, not the prompt.

**Alignment with Today's Date:** PASS (5). "tuesday" = Sep 30, 2025; "monday's tuning session" = Oct 6, 2025 (the invite); every relied-on record is before the clock.

**Originality / Sample Similarity:** N/A (no samples supplied).

**Coherence (Bolt-on):** PASS (5).


### Unique Ground Truth comparison

Unique Ground Truth: PASS 5

Basis: Every fork is settled by a prompt sentence or a persona-visible record. SQL revision 45 adds Robert's three columns: card rule 2 now ends 'plus the three things Robert asked for when I asked him in our group chat', and in group DM CAFC495E4006 (Julia is a member) Robert asks for, after status, the Linear assignee, the day it got marked done (blank if never done) and the Linear priority. AF (columns left out) and AH (the notes doc's 'three things for the register' taken as Robert's) are excluded by card rule 2 and source identity; AI (cancel day for ZOM-280) by 'leave it blank if it never got done'; AG (column position) is the same material result. The Pacific/UTC day of the three completed\_at instants after 00:00 UTC (ZOM-200, 274, 282) is accepted either way under ENVIRONMENT.md and is not a fork; the EMPLOYEE\_0032\_NAME assignee token is correct as shown (deep\_recheck known platform defects). AJ (ZOM-199 Not shipped because its &gt;= 90 text never shipped, raised by the deep recheck) is excluded by card rule 1, rule 6's wrong-text comment and Blake's 'everything difficulty related was merged'. Earlier forks B-AE stay excluded on byte-identical rows re-anchored by content. 24 tickets, 9 comments.

Alternative selection: Revision 45 adds Robert's group-DM ask and the card rule 2 pointer to it. AH is the strongest new alternative (a second 'three things for the register' list sits in the notes doc attached to the same card); AF tests leaving the columns out, AG their position, AI the blank rule for the cancelled ticket. B-AE are every earlier fork, retested against rows re-anchored by content (all byte-identical apart from the +4 line shift).

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Follow the card as Leonard left it, his card comment, his 'notes for monday' doc attached to the card, his checklist and his Tuesday DMs (the request thread and his later reply in the thread under Julia's Monday question): scope is every difficulty ticket created up to Aug 31 by title word plus every ticket with Blake's 'tiers:' closing note (ZOM-221, 281, 300, 305, 378), minus a title match Blake marked 'not tiers' in his review on its PR (ZOM-312, PR match3d\#265), attack power counting only when written out (ZOM-271 out), minus the six analytics and tutorial tickets his DM reply lists, ZOM-258 from his notes and the four tickets his later DM reply takes off by key (ZOM-162, 163, 201, 250; 'just those four'), which also get no comments; status against Blake's store builds mail and his reply to it (the 13:26Z 'editor stuff and ZOM-199, before Monday' mail, which says editor and debug tooling never reached players); Replaced only where another ticket's closing note says so (ZOM-282 on ZOM-254); comments on ZOM-199, on Replaced ZOM-254 and, per the checklist's rule 6 change, on every Editor only and Not shipped ticket still on the list, each naming the two store builds (iOS 0.3.49 and Android 0.3.133) per Leonard's first DM reply; the ZOM-199 comment says what the build does (cpm &gt; 90, checked when the 10th game ends); share with the invite attendees, Robert as editor, Brian as commenter per Leonard's later DM reply, Leonard as commenter and Arthur as viewer per the notes; the Rules in force tab as before; the DM reply gives the total, per-status counts, the Not shipped and Editor only keys, which ticket replaced which, and when a new player gets their starting tier. Card rule 2 also adds 'the three things Robert asked for when I asked him in our group chat': in the group DM with Julia, Robert asks for, after status, who each ticket is assigned to in Linear, the day it was marked done (blank if never done) and its Linear priority. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and the four tickets Leonard's later DM reply takes off, ZOM-162, 163, 201 and 250, off ('just those four'); ZOM-312 off as Blake's 'not tiers'; ZOM-378 and ZOM-281 on); ZOM-173, 200, 277 and 315 stay on as Editor only; ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-271 out; checklist rule 6 change in force for the tickets still listed: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds iOS 0.3.49 and Android 0.3.133); no comments on ZOM-162, 163, 201 or 250; reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280, 293; Leonard DM D05HB64NMQU. | 24 rows: the 35 rule-1 tickets (31 title matches without Duplicates ZOM-203 and ZOM-276 and without ZOM-312, which Blake marked 'not tiers' in his review on PR match3d\#265, plus tiers: tickets ZOM-221, 281, 300, 305, 378) minus the eleven Leonard leaves off (ZOM-30, 49, 50, 161, 262, 275 in his first DM reply, ZOM-258 in his notes for monday, and ZOM-162, 163, 201, 250 in his later DM reply); Live 16, Editor only 4, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force as the build runs them: starting tier set after the first 10 games played (wins and losses), average CPM above 90 to tier 1, everyone else tier 0 (90 exactly stays on tier 0); promotion and demotion in ZOM-42's wording: 80% or more over up to the most recent 10 attempts (the last 10 games played) promotes, one win on tier -2 promotes; demotion on a losing streak of 4 games in a row at any time or a win rate of 50% or lower over up to the last 10 games; the record resets after every promotion or demotion; after a demotion the level being played is replayed lower (below the new tier) until a win; enrage from the sheet Live tab copied as it stands: nine monster rows and MonsterBase 0.8/0.8 with their numbers, and Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP) as not copied yet; DM gives the total 24, the per-status counts, the keys of the Not shipped (ZOM-202, 280, 293) and Editor only (ZOM-173, 200, 277, 315) tickets, that ZOM-282 replaced ZOM-254, and that a new player gets their starting tier after their first 10 games (levels played), from the average CPM of those games. Tickets tab columns after Status: Linear assignee, the day each ticket was marked done (Linear completed\_at; blank for ZOM-202 In Progress, ZOM-280 Canceled and ZOM-293 Todo), and Linear priority; ZOM-200, 274 and 282 have completed\_at after 00:00 UTC, so their Pacific day is one earlier (either day accepted per ENVIRONMENT.md); six tickets show the anonymized assignee token EMPLOYEE\_0032\_NAME, which is correct as shown. | CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 280-280): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."; SHEET\_LIVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 26-26): "\["MonsterBase (base prefab)", "0.8", "0.8", "0"\], \["Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP)", "not copied yet", "not copied yet", "0"\]"; TCOMMENT\_W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "written out (ATK on its own doesn''t)"; CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 87-87): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 89-89): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; CARD\_R1B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "any ticket Blake counts as tier work even if the title doesn''t say so: his closing note on those starts with ''tiers:''"; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 278-278): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 100-100): "Both were cut from main on Sep 26, and everything difficulty related was merged long before that."; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; TM\_CPM (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 93-93): "case var cpm when cpm &gt; 90.0f:"; DMT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 52-52): "tell me when a new player gets their starting tier"; DECK\_PROMO (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Promotion: win rate of 80% or more over the last 10 attempts moves you up one tier."; Z42MR (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we evaluate UP TO THE MOST RECENT 10 attempts of the player"; CARD\_R5PD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "For which games promotion and demotion look at, write it the way ZOM-42 words it."; Z42LAST (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we constantly look at the last 10 games played"; Z42STREAK (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "A losing streak of 4 games in a row can still trigger at any time"; Z42DEM (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we demote someone when their win rate for up to the last 10 games is 50% or lower"; Z42RESET (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "every time a promotion/demotion happens, the record is reset and we start at 0 games played"; WR\_DEM50 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/WinRateRule.cs lines 31-31): "new WinRateRule(-1, 100, 10, 0.5f, RuleComparisonType.LessThanOrEqualTo, -1),"; GL\_RETRY (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Match3D/Game/Levels/GameLoader.cs lines 101-101): "// Make sure we go down a tier for this level"; REPLY\_TAB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "For the rules tab: the starting tier check in the code is cpm &gt; 90, not &gt;= 90"; NOTES\_258 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "leave ZOM-258 off the list. it''s only the icon players see over a monster, it doesn''t change how hard a level plays."; NOTES\_ART (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "arthur is only listening in on monday, view access is enough for him."; NOTES\_REPL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "when you reply to me, also tell me which ticket replaced which."; CARD\_R1NT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "It works the other way too: a title match Blake marked ''not tiers'' in his review on its PR stays off."; GH265RC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work"; DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 62-62): "take 162, 163, 201 and 250 off the list too. just those four, on top of the ones i already left off."; DMR2\_BR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 62-62): "comment access is enough for brian"; DMR1\_BLD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "put the two builds in the comment (ios 0.3.49 and android 0.3.133)"; CARD\_R3B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Blake''s store builds mail and his reply to it."; CARD\_R2R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "plus the three things Robert asked for when I asked him in our group chat."; GDM\_R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "who it''s assigned to in linear, the day it got marked done (leave it blank if it never got done), and its linear priority." |
| B | match3d\#401 changed how enrage works (speed and damage split per monster, hp method dropped), so ZOM-282 is Replaced by match3d\#401 and gets a Replaced comment. | ZOM-282 Replaced by match3d\#401. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a Replaced comment on ZOM-282 naming match3d\#401. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus ZOM-282. | Register shows ZOM-282 Replaced; DM counts Live 15, Replaced 2. | GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 66-66): "this gives enrage speed and damage their own values, they shared one since ZOM-282." |
| C | Comment on every listed ticket whose text the store builds contradict, including ZOM-42 (6-7 levels vs 10). | Correction comment also on ZOM-42. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a comment on ZOM-42. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus ZOM-42. | Extra correction comment; register unchanged. | Z42A (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "gets assigned after the first 6-7 levels based on CPM" |
| D | Read the scope window in Pacific days with an Apr 21 start, dropping ZOM-23 (2025-04-21T04:51:38Z, Apr 20 PT); ZOM-30 is already off under Leonard's DM reply. | 23 tickets; ZOM-23 out. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Register 23 rows; DM total 23 and Live 15. | Z23 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3277): "2025-04-21T04:51:38Z" |
| E | Also post the register in \#zombie-design because Vincent asked Julia to drop it there. | Share with the invite and also post in \#zombie-design. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a Slack post in \#zombie-design. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus C090N54TG79. | Same register; extra channel post. | VINCENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 56-56): "julia when you have the difficulty list can you drop it in here too" |
| G | ZOM-254 was closed (2025-06-23) after ZOM-282 (2025-06-21) and its own QA note says blunder enrages the monsters, so ZOM-282 is not the 'later' ticket and ZOM-254 stays Live with no Replaced comment. | ZOM-254 Live; no Replaced ticket. | Same as A without the ZOM-254 comment. | Same as A without Linear ZOM-254. | Register shows ZOM-254 Live; DM counts Live 17, Replaced 0, and no replacement to report. | Z254C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 256-256): "checked on the dev build, blunder enrages the monsters on the board now" |
| H | Rule 5 asks for enrage as it works in the store builds today, so the three monsters the sheet has not copied are given what they actually run on in main: no own override, so MonsterBase's 0.8 speed / 0.8 damage. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same 24 rows and counts as A; Rules in force from deck, ZOM-42, Blake's reply and the enrage sheet Live tab, with Mailman, Mayor2 and PartyGirl given 0.8 speed / 0.8 damage (MonsterBase) instead of not copied yet; DM as A. | CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; MB\_ENRAGE (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Prefabs/Monsters/MonsterBase.prefab lines 342-343): "enrageSpeedPercentage: 0.8" |
| I | Fill the gap from the VarC prefabs the History tab says the Live tab was copied from: VarC-PartyGirl carries enragePercentage 0.6, so PartyGirl is 0.6 speed / 0.6 damage; Mailman and Mayor2 show no enrage value in their prefab text. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same 24 rows and counts as A; Rules in force from deck, ZOM-42, Blake's reply and the enrage sheet Live tab, with PartyGirl at 0.6 / 0.6 and Mailman and Mayor2 without numbers; DM as A. | SHEET\_HIST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 30-30): "\["2025-09-08", "Live tab copied from the VarC prefabs in main", "Julia"\]"; PG\_PREFAB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Prefabs/Monsters/VarC-PartyGirl.prefab lines 215-216): "propertyPath: enragePercentage" |
| J | Leonard's comment adds attack power in the title; ZOM-271's title says 'ATK POWER' / 'ATK Power', and 'ATK on its own' is read as ATK without 'power', so ZOM-271 (Done, June 16, card-profile stat display) is in scope as Live. | 25 tickets; ZOM-271 Live; otherwise as A. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 25 rows (adds ZOM-271); Live 17, Editor only 4, Replaced 1, Not shipped 3; DM total 25 and Live 17. | TCOMMENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "attack power in the title counts too"; Z271 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3323): "Comprehensive Item Stat Display Rules also ATK POWER BUG. Also Change Damage sort to ATK Power sort" |
| K | Take the starting-tier window from the written rules (deck, ZOM-42, ZOM-199): average CPM over the player's first 10 levels read as ten distinct levels, so replays of a lost level don't count; &gt; 90 to tier 1, the rest tier 0. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register and counts as A; Rules in force and the DM answer give the starting tier as after the first 10 distinct levels (replays not counted), instead of after the first 10 games played (wins and losses) as the build counts them. | Z42S (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "1st 10 level avg CPM &gt; 90 (top 20%) moves to tier 1, rest stays in tier 0)"; DECK\_ST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0." |
| L | The 'Before Monday' checklist items are unchecked, so they are Leonard's pending notes, not rules in force; card rule 6 as written stands: comments only on ZOM-199 and ZOM-254, with the Not shipped and Editor only tickets left as they are. | Checklist not applied: two comments. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, leonard.hayes@ and brian.foster@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 and ZOM-254 only; reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; invite attendees' Drive shares; Linear ZOM-199 and ZOM-254; Leonard DM D05HB64NMQU. | Same 24 rows and counts; no comments on the seven Editor only and Not shipped tickets; brian.foster@ as commenter as in A. | CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CL\_NAME (Evals/task\_inputs/01\_Universe\_Inject.sql lines 85-85): "'Before Monday', '68daca5871dba40417a00383'" |
| M | ZOM-378 'Level 1 is removed and creates tutorial order problems' is a tutorial ticket, so it goes off the list with the other analytics and tutorial tickets Leonard named. | 23 tickets; ZOM-378 off. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 23 rows; Live 15; DM total 23 and Live 15. | DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; Z378 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3440): "It creates other important issues like wrong tutorials at the wrong spot." |
| N | Leonard's reason 'they don't change how hard a level plays' (repeated in his notes for ZOM-258) and Blake's 'players never see it' on ZOM-312 are the test, so every ticket that only touches editor or debug tooling is left off too (ZOM-162, 163, 173, 200, 201, 202, 250, 277, 315), with no comments on them. | Editor-tooling tickets off the list; no comments on them. | As A without the comments on the editor-tooling tickets. | As A without those Linear tickets. | 19 rows (ZOM-173, 200, 202, 277 and 315 off on top of ZOM-162, 163, 201, 250); no Editor only rows; DM without Editor only keys. | DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not."; NOTES\_258 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "leave ZOM-258 off the list. it''s only the icon players see over a monster, it doesn''t change how hard a level plays."; GH265RC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work" |
| O | ZOM-281 is assigned to someone else (usr\_EMPLOYEE\_0032), so it isn't one of Blake's tickets and its 'tiers:' note doesn't bring it in; its title has none of rule 1's words, so it stays off the list. | 23 tickets; ZOM-281 out. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 23 rows; Live 15; DM total 23 and Live 15. | Z281 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "Win streak not lost when replaying without main menu" |
| P | No PR or commit in match3d names ZOM-281, so it counts as never merged and goes on the list as Not shipped, with the checklist's not-in-the-store-builds comment. | 24 tickets; ZOM-281 Not shipped; extra comment on ZOM-281. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a not-in-the-store-builds comment on ZOM-281. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus ZOM-281. | Register shows ZOM-281 Not shipped; DM counts Live 15, Not shipped 4, and ZOM-281 among the Not shipped keys. | CARD\_R1NS (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "open, cancelled and never-merged ones are in, as Not shipped" |
| Q | Answer Leonard's starting-tier question from ZOM-42's line that players get assigned after the first 6-7 levels, and put that on the Rules in force tab. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 6-7 levels, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register and counts as A; Rules in force and the DM answer say a new player gets their starting tier after the first 6-7 levels. | Z42A (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "gets assigned after the first 6-7 levels based on CPM" |
| R | Use the written threshold from the deck and ZOM-199: average CPM of 90 or more starts a player on tier 1. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM of 90 or more to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register and counts as A; Rules in force (and any threshold in the DM answer) give 90 or more to tier 1, so 90 exactly goes to tier 1. | DECK\_ST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0." |
| S | Card rule 5 asks for promotion and demotion 'as they work in the store builds today'. The build's tier history is appended at the end and cleared on every tier change, and the win-rate check counts from index 0, so promotion and demotion are judged on the first 10 (and first 4) games since the last tier change, not the most recent ones. The Rules in force tab says that. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 24 rows: the 35 rule-1 tickets (31 title matches without Duplicates ZOM-203 and ZOM-276 and without ZOM-312, which Blake marked 'not tiers' in his review on PR match3d\#265, plus tiers: tickets ZOM-221, 281, 300, 305, 378) minus the eleven Leonard leaves off (ZOM-30, 49, 50, 161, 262, 275 in his first DM reply, ZOM-258 in his notes for monday, and ZOM-162, 163, 201, 250 in his later DM reply); Live 16, Editor only 4, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force as the build runs them: starting tier set after the first 10 games played (wins and losses), average CPM above 90 to tier 1, everyone else tier 0 (90 exactly stays on tier 0); promotion and demotion judged on the first games played since the last tier change, not the latest: 80% or more over the first 10 games on the tier promotes, on tier -2 only if the first game there is a win; 50% or lower over the first 10, or losing the first 4 games on the tier, demotes; a player who does neither in those games stays on the tier; enrage from the sheet Live tab copied as it stands: nine monster rows and MonsterBase 0.8/0.8 with their numbers, and Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP) as not copied yet; DM gives the total 24, the per-status counts, the keys of the Not shipped (ZOM-202, 280, 293) and Editor only (ZOM-173, 200, 277, 315) tickets, that ZOM-282 replaced ZOM-254, and that a new player gets their starting tier after their first 10 games (levels played), from the average CPM of those games. | CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; WH\_LOOP (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 46-46): "for (int i = 0; i &lt; gamesCount; i++)"; WH\_APPEND (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 160-160): "tierWinHistory += win ? "W" : "L";"; WH\_RESET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 26-26): "PlayerPrefs.SetString(TierWinHistoryKey, "");"; TM\_RULE (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 121-121): "WinHistory.GetWorstTierWinRatePossible(rule.NumGames) : WinHistory.GetBestTierWinRatePossible(rule.NumGames)" |
| T | Rule 5's go-by-the-build sentence now covers only the starting tier, so for demotion follow Robert's deck, the first write-up rule 5 names: demotion is 4 losses in a row only, with no 50%-or-lower rule; the window wording still follows ZOM-42. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 24 rows: the 35 rule-1 tickets (31 title matches without Duplicates ZOM-203 and ZOM-276 and without ZOM-312, which Blake marked 'not tiers' in his review on PR match3d\#265, plus tiers: tickets ZOM-221, 281, 300, 305, 378) minus the eleven Leonard leaves off (ZOM-30, 49, 50, 161, 262, 275 in his first DM reply, ZOM-258 in his notes for monday, and ZOM-162, 163, 201, 250 in his later DM reply); Live 16, Editor only 4, Replaced 1 (ZOM-254 by ZOM-282), Not shipped 3; Rules in force as the build runs them: starting tier set after the first 10 games played (wins and losses), average CPM above 90 to tier 1, everyone else tier 0 (90 exactly stays on tier 0); promotion and demotion in ZOM-42's wording: 80% or more over up to the most recent 10 attempts (the last 10 games played) promotes, one win on tier -2 promotes; demotion only on a losing streak of 4 games in a row (no 50%-or-lower rule); the record resets after every promotion or demotion; after a demotion the level being played is replayed lower (below the new tier) until a win; enrage from the sheet Live tab copied as it stands: nine monster rows and MonsterBase 0.8/0.8 with their numbers, and Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP) as not copied yet; DM gives the total 24, the per-status counts, the keys of the Not shipped (ZOM-202, 280, 293) and Editor only (ZOM-173, 200, 277, 315) tickets, that ZOM-282 replaced ZOM-254, and that a new player gets their starting tier after their first 10 games (levels played), from the average CPM of those games. | CARD\_R5WU (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "The tier rules are written up in Robert''s dynamic difficulty deck and in ZOM-42 itself."; DECK\_DEM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Demotion: 4 losses in a row moves you down one tier." |
| U | Card rule 7 says everyone on the invite other than Robert comments, and the later checklist changes rule 7 only for Brian; Leonard's note that view access is 'enough' for Arthur sets a floor, not a cap, so Arthur still gets comment access. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian, Leonard and Arthur comment; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor and brian.foster@, leonard.hayes@ and arthur.blake@ as commenters; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register, comments and DM; arthur.blake@ shared as commenter, not viewer. | CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 89-89): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; NOTES\_ART (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "arthur is only listening in on monday, view access is enough for him." |
| V | ZOM-258 'Icon for Enraged monster' is a rule-1 title match, and Leonard's later DM reply lists the tickets to leave off (30, 49, 50, 161, 262 and 275) without ZOM-258, so the DM list is his final exclusion list and ZOM-258 stays on as Live. | 25 tickets; ZOM-258 Live. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | 25 rows; Live 17; DM total 25 and Live 17. | CARD\_R1W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "as a whole word in the title"; Z258 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3308): "Icon for Enraged monster"; DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays" |
| W | ZOM-312 'Delete Difficulty Tier and Reassign' is a title match. PR match3d\#265 is Blake's own PR, so his 'not tiers' line is a comment on his own code, not 'his review on its PR'; ZOM-312 stays on as Editor only and gets the checklist's not-in-the-store-builds comment. | 25 tickets; ZOM-312 Editor only with a comment. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. Plus a not-in-the-store-builds comment on ZOM-312. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. Plus ZOM-312. | 25 rows; Editor only 5 with ZOM-312 among the Editor only keys; DM total 25. | CARD\_R1W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "as a whole word in the title"; Z312 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3368): "Delete Difficulty Tier and Reassign"; PR265 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /pull\_requests/2147): ""title": "ZOM-312"" |
| X | The prompt says to reply with what Leonard asked for in the DM; the DM and its thread reply ask for the counts, the Not shipped and Editor only keys and the starting-tier timing, so the reply leaves out which ticket replaced which. | 24 tickets (the six analytics/tutorial tickets, ZOM-258 and ZOM-162, 163, 201, 250 off, ZOM-312 off as Blake's 'not tiers', ZOM-378 and ZOM-281 on); ZOM-281 Live; ZOM-282 Live; ZOM-254 Replaced by ZOM-282; ZOM-173, 200, 277, 315 Editor only; ZOM-271 out; checklist changes in force: comments on ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Robert edits, Brian and Leonard comment, Arthur views; starting tier after the first 10 games played, average CPM above 90 to tier 1. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the seven Editor only and Not shipped tickets ZOM-173, 200, 277, 315, 202, 280 and 293 (the change isn't in the store builds); reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets; Leonard DM D05HB64NMQU. | Same register, comments and shares; the DM gives the total, counts, keys and starting-tier timing without saying that ZOM-282 replaced ZOM-254. | DMC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 52-52): "reply here when it''s in the folder with how many tickets made the list and how many of each status"; DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"; DMT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 52-52): "tell me when a new player gets their starting tier" |
| Y | All four keys Leonard's later DM reply takes off (ZOM-162, 163, 201, 250) are level editor tickets by their titles, so his intent is the level editor category: Blake's store builds mail defines level editor work (Assets/Scripts/LevelEditor and the LevelDesigner panels), and ZOM-173 (Linear label 'Level Editor', 'Item Set Count in editor', level objects panel), ZOM-277 and ZOM-315 (the editor's stats panel, which ZOM-250 created) are level editor tickets on the same footing. So those three go off too, with no comments; only ZOM-200 (debug menu) is left as Editor only. | 21 tickets: ZOM-173, 277 and 315 also off as level editor tickets, with no comments; ZOM-200 the only Editor only ticket; otherwise as A. | Create the register spreadsheet with Tickets and Rules in force tabs; place it in the ZM Difficulty folder; share it with robert@ as editor, brian.foster@ and leonard.hayes@ as commenters and arthur.blake@ as viewer; post Linear comments on ZOM-199 (the build checks cpm &gt; 90), ZOM-254 (replaced by ZOM-282) and the four Editor only and Not shipped tickets ZOM-200, 202, 280 and 293 (the change isn't in the store builds); no comments on ZOM-162, 163, 173, 201, 250, 277 or 315; reply in the Leonard DM D05HB64NMQU. | ZM Difficulty folder; Drive shares to the four other invite attendees; Linear ZOM-199, ZOM-254, ZOM-200, 202, 280, 293; Leonard DM D05HB64NMQU. | 21 rows (24 minus ZOM-173, 277, 315); Live 16, Editor only 1 (ZOM-200), Replaced 1, Not shipped 3; DM total 21, Editor only key ZOM-200 only; rules tab as A. | DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 62-62): "take 162, 163, 201 and 250 off the list too."; Z201T (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3246): "Also turn it into an overlay in editor while not obstructing game board."; Z250T (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3300): "Create faux level timer and add attack power stats in level editor"; MAIL\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "The level editor (Assets/Scripts/LevelEditor and the LevelDesigner panels), anything in an Editor folder and the debug menu (Assets/Scripts/Debug) are stripped before we ship to players on iOS and Android."; Z173L (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3215/labels): "Level Editor"; Z173T (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3215): "Item Set Count in editor not updating with difficulty tier changes"; Z173C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 224-224): "this one is the set count in the level objects panel"; Z277C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 270-270): "this is the average in the editor''s stats panel, nothing changes in the game itself"; Z315C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 318-318): "this is the total attack power in the editor''s stats panel, items without cardData now count with their base damage. nothing changes in the game itself" |
| Z | The 'Before Monday' checklist's rule 7 change ('Brian gets edit as well') is on the card the DM points to, so Brian keeps edit access. | Robert and Brian edit, Leonard comments, Arthur views; otherwise as A. | Same as A except brian.foster@ is shared as editor. | Same as A. | Same register, comments and DM as A. | CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 89-89): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session" |
| AA | Leonard's later message sits in the thread under Julia's own Monday question, not in his Tuesday request thread, so it is not part of 'his ask'; the register keeps ZOM-162, 163, 201 and 250 (Editor only, commented) and Brian keeps edit. | 28 tickets (Live 16, Editor only 8, Replaced 1, Not shipped 3); 13 comments; Robert and Brian edit, Leonard comments, Arthur views. | Same kinds of writes as A, plus comments on ZOM-162, 163, 201 and 250, and brian.foster@ shared as editor. | As A plus Linear ZOM-162, 163, 201, 250. | 28 rows; DM total 28 with Editor only keys ZOM-162, 163, 173, 200, 201, 250, 277, 315. | DMP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 60-60): "leonard, anything you need from me before monday''s tuning session?"; DM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 52-52): "julia before monday''s tuning session i want a baseline of the difficulty system from you" |
| AB | The seven Editor only and Not shipped comments only say the change isn't in the store builds, as the checklist words it; the build numbers are not needed. | As A. | As A, but the seven comments omit the build numbers. | As A. | Seven comments without iOS 0.3.49 / Android 0.3.133. | CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 87-87): "saying the change isn''t in the store builds" |
| AC | Blake's 13:26Z mail sits in its own thread under a new subject, so it is not 'his reply to it'; status and comments go by the 09:12Z store builds mail alone, which says nothing about editor tooling or ZOM-199. | No Editor only basis: ZOM-173, 200, 277, 315 count as Live (Done, merged before Sep 26); no wrong-text comment on ZOM-199. | Four fewer comments (no Editor only comments) and no ZOM-199 comment. | Linear ZOM-199, 173, 200, 277, 315 untouched. | Live 20, Editor only 0; DM Editor only keys empty. | MAIL2\_SUBJ (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "'editor stuff and ZOM-199, before Monday'"; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 100-100): "Both were cut from main on Sep 26, and everything difficulty related was merged long before that." |
| AD | Put the two build numbers in every ticket comment, including ZOM-199 and ZOM-254. | As A. | As A; the ZOM-199 and ZOM-254 comments also mention the builds. | As A. | Two comments carry an extra build reference. | DMR1\_BLD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "when you comment on the editor only and not shipped ones" |
| AE | The ZOM-199 comment only needs the threshold (cpm &gt; 90, 90 exactly stays on tier 0), not when the check runs. | As A. | As A. | As A. | ZOM-199 comment states the &gt; 90 threshold without the 10th-game timing. | REPLY\_TAB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "For the rules tab: the starting tier check in the code is cpm &gt; 90, not &gt;= 90" |
| AF | Build the Tickets tab with only the card's own columns and the agenda layout; leave out Robert's three extra columns because they sit in a separate group chat the Agent doesn't open. | As A. | As A. | As A. | Tickets tab without the assignee, done-date and priority columns. | CARD\_R2R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Layout as in the session agenda" |
| AG | Put Robert's three columns at the end of the Tickets tab, after the 'replaced by' column, instead of straight after Status. | As A. | As A. | As A. | Same cells in every row; the three columns sit after the 'replaced by' column. | GDM\_R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "yeah three things after status please." |
| AH | Read 'the three things Robert asked for' as the 'three things for the register' in Leonard's notes for monday doc (ZOM-258 off, Arthur view, which ticket replaced which), so no extra columns are added. | As A. | As A. | As A. | No assignee, done-date or priority columns; the notes' three items applied (as in A). | NOTES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "julia, three things for the register:" |
| AI | Treat a cancelled ticket as 'marked done' and fill the cancel day for ZOM-280. | As A. | As A. | As A. | ZOM-280 done-date cell shows 2025-06-20 instead of blank. | Z280 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3333): ""canceled\_at": "2025-06-20T23:38:27Z"" |
| AJ | ZOM-199 is Not shipped, not Live: its '&gt;= 90 after the first 10 levels' change never reached the build (Blake: 'the code never changed from the original spec'), so it gets the 'not in the store builds' comment with the two builds and moves into the Not shipped counts and keys. | ZOM-199 Not shipped instead of Live. | As A, but the ZOM-199 comment says the change isn't in the store builds (iOS 0.3.49, Android 0.3.133) instead of what the build does. | As A. | Live 15 / Not shipped 4 (ZOM-199, 202, 280, 293); DM keys and counts change. | REPLY90 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "so 90 exactly stays on tier 0"; CARD\_R1NS (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "open, cancelled and never-merged ones are in, as Not shipped" |

Explicit option inventory: The prompt lists no options; the status values sit in the incorporated card.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "build the register the way he set it up"

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: B
Resolution: EXCLUDED. Card rule 4 now makes a ticket Replaced only when another ticket's closing note says so and says PRs that change or split its numbers don't. match3d\#401 is a PR, and its comment describes a split of the shared value, not a replacement.
Resolution evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 66-66): "this gives enrage speed and damage their own values, they shared one since ZOM-282."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Live vs Replaced for ZOM-282. |
| writes | DIFFERENT | B adds a ZOM-282 comment. |
| destinations | DIFFERENT | B adds ZOM-282. |
| contents | DIFFERENT | Status cell and DM counts differ (Live 15 / Replaced 2). |

Authority chain: P → DMR → CARD\_R4

Resolution relevance challenge: The quoted sentences exclude PRs and value splits by name; \#401's comment says it gives speed and damage their own values.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; CARD\_R4X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don''t, and a ticket players never had stays Editor only or Not shipped."; GH401C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 66-66): "this gives enrage speed and damage their own values, they shared one since ZOM-282."

Compared alternative: C
Resolution: EXCLUDED. Card rule 6 limits Blake-sourced comments to tickets his mail or reply calls wrong (only ZOM-199 in the reply), and says ZOM-42 stays as it is even if its wording is a bit off; the checklist's rule 6 change adds only Editor only and Not shipped tickets, and ZOM-42 is Live.
Resolution evidence: CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "ZOM-199 says &gt;= 90 after the first 10 levels, but the code never changed from the original spec"; CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 87-87): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | C decides ZOM-42 needs a comment. |
| writes | DIFFERENT | C adds one comment. |
| destinations | DIFFERENT | C adds ZOM-42. |
| contents | DIFFERENT | Extra comment text. |

Authority chain: P → DMR → CARD\_R6X

Resolution relevance challenge: The quoted sentences name ZOM-42 as staying as it is; the checklist change covers Editor only and Not shipped tickets, which ZOM-42 (Live) is not; the reply names only ZOM-199.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Ticket comments, only two kinds: where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them."; REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "ZOM-199 says &gt;= 90 after the first 10 levels, but the code never changed from the original spec"

Compared alternative: D
Resolution: EXCLUDED. The scope has no start date (everything since ZM started), so ZOM-23 is in under any timezone; the next title match after Aug 31 is ZOM-517 on 2025-09-03.
Resolution evidence: CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; Z517 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3591): "2025-09-03T22:22:22Z"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | D drops ZOM-23. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rows and counts differ by one. |

Authority chain: P → DMR → CARD\_SCOPE

Resolution relevance challenge: The quoted scope removes the start-date edge; Z517 shows no ticket near the Aug 31 end.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty"; Z517 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3591): "2025-09-03T22:22:22Z"

Compared alternative: E
Resolution: EXCLUDED. The prompt and card both define the audience as the invite list; Vincent is not an attendee and his channel request is not part of Leonard's ask.
Resolution evidence: CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; P (Evals/task\_inputs/04\_Prompt.txt): "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system before monday's tuning session. can you take it off my plate? go through his ask and everything it points to and build the register the way he set it up. put it in the zm difficulty folder and share it with everyone on monday's tuning invite. if his rules say something needs to happen on the tickets, go ahead and do that too. then reply to leonard in the dm with what he asked for. go with your read on the details, no need to check with me first"; CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 159-159): "VALUES ('evt\_91674a9c23d012a9ac34da', 'julia.lawson@harmonygames.co', 'ZM difficulty tuning'"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | E adds a channel post. |
| writes | DIFFERENT | E adds a Slack post. |
| destinations | DIFFERENT | E adds \#zombie-design. |
| contents | DIFFERENT | Extra post. |

Authority chain: P → DMR → CARD\_R7

Resolution relevance challenge: The prompt names the audience as the invite; the invite on Julia's calendar does not include Vincent.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; P (Evals/task\_inputs/04\_Prompt.txt): "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system before monday's tuning session. can you take it off my plate? go through his ask and everything it points to and build the register the way he set it up. put it in the zm difficulty folder and share it with everyone on monday's tuning invite. if his rules say something needs to happen on the tickets, go ahead and do that too. then reply to leonard in the dm with what he asked for. go with your read on the details, no need to check with me first"; CAL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 159-159): "VALUES ('evt\_91674a9c23d012a9ac34da', 'julia.lawson@harmonygames.co', 'ZM difficulty tuning'"

Compared alternative: G
Resolution: EXCLUDED. Rule 4 now keys on another ticket's closing note, with no ordering condition. ZOM-282's closing note says it replaces the blunder 2.0 boost from ZOM-254; ZOM-254's QA note describes the dev build and is not a closing note on another ticket that replaces it. Close order no longer matters.
Resolution evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 280-280): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; Z254D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3304): "2025-06-12T21:59:58Z"; Z282D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3335): "2025-06-19T05:23:06Z"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Replaced vs Live for ZOM-254. |
| writes | DIFFERENT | G drops the ZOM-254 comment. |
| destinations | DIFFERENT | G drops Linear ZOM-254. |
| contents | DIFFERENT | Status and DM counts differ (Live 17 / Replaced 0), and the DM has no replacement to report. |

Authority chain: P → DMR → CARD\_R4

Resolution relevance challenge: The rule no longer says 'later', so close dates cannot reverse it; ZOM-282's note names ZOM-254 explicitly, which is what the rule asks for.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R4 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Replaced: only when another ticket''s closing note says it replaces this one. Name that ticket."; Z282C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 280-280): "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th."; Z254D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3304): "2025-06-12T21:59:58Z"; Z282D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3335): "2025-06-19T05:23:06Z"

Compared alternative: H
Resolution: EXCLUDED. Rule 5 now says how to fill the enrage section: copy the sheet's Live tab as it stands, put a monster the sheet has not copied on the tab as not copied yet, and do not work numbers out from anywhere else. Deriving 0.8/0.8 for Mailman, Mayor2 and PartyGirl from MonsterBase inheritance in the repo is working numbers out from somewhere else. The later, more specific sentence in the same rule governs the store-builds clause for these rows; the copied numeric rows equal main (Eval 0 Check C), so the two clauses no longer pull apart.
Resolution evidence: CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."; SHEET\_LIVE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 26-26): "\["MonsterBase (base prefab)", "0.8", "0.8", "0"\], \["Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP)", "not copied yet", "not copied yet", "0"\]"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and share list. |
| writes | SAME | Same spreadsheet, shares, Linear comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | Rules in force tab: three monsters as not copied yet (A) vs 0.8/0.8 (H). |

Authority chain: P → DMR → CARD\_R5C

Resolution relevance challenge: Not a strawman: H was the leading reading last round, and 'as they work in the store builds today' still sits in rule 5. The new sentence speaks to exactly this case, a monster the sheet hasn't copied, and names the required entry ('not copied yet') and forbids the derivation H needs.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."

Compared alternative: I
Resolution: EXCLUDED. Rule 5 says to copy the Live tab as it stands and not to work numbers out from anywhere else, so reading PartyGirl's old enragePercentage 0.6 out of its prefab is excluded; the code also no longer reads that field (Monster.cs declares only enrageSpeedPercentage and enrageDamagePercentage).
Resolution evidence: CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."; MONSTER\_CS (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Monster/Monster.cs lines 87-88): "\[SerializeField\] private float enrageSpeedPercentage = 0.25f;"; PG\_PREFAB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Prefabs/Monsters/VarC-PartyGirl.prefab lines 215-216): "propertyPath: enragePercentage"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and share list. |
| writes | SAME | Same spreadsheet, shares, Linear comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | PartyGirl 0.6/0.6 vs not copied yet. |

Authority chain: P → DMR → CARD\_R5C

Resolution relevance challenge: The new rule 5 sentence forbids taking numbers from anywhere but the Live tab, which covers prefab text; the dead field is a second, independent reason.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted.
Challenge evidence: CARD\_R5C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Copy its Live tab as it stands: a monster it hasn''t copied yet goes on the tab as not copied yet, don''t work numbers out from anywhere else."; MONSTER\_CS (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Monster/Monster.cs lines 87-88): "\[SerializeField\] private float enrageSpeedPercentage = 0.25f;"

Compared alternative: J
Resolution: EXCLUDED. Leonard's card comment now says attack power counts only when written out in the title and that ATK on its own doesn't. ZOM-271's title never spells out 'attack power'; it uses the abbreviation 'ATK POWER' / 'ATK Power'. 'Written out' sets the test (the words spelled in full), and the parenthetical names the abbreviation as what fails it, so ZOM-271 stays out. Every other ZOM title created up to Aug 31 with ATK or attack was checked: ZOM-246, 250, 263, 277 and 315 spell out 'attack power'; ZOM-21 ('Monster Attack Speed') has no 'attack power'.
Resolution evidence: TCOMMENT\_W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "written out (ATK on its own doesn''t)"; Z271 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3323): "Comprehensive Item Stat Display Rules also ATK POWER BUG. Also Change Damage sort to ATK Power sort"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-271 out vs in (Live). |
| writes | SAME | Same spreadsheet, comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | One more register row; DM total 25 vs 24 and Live 17 vs 16. |

Authority chain: P → DMR → TCOMMENT\_W

Resolution relevance challenge: Not a strawman: ATK is the game's short form and ZOM-271 also says ATK POWER, so a reader could take 'ATK on its own' as 'ATK without power'. But 'written out' is the governing test and 'ATK POWER' is not attack power written out; the parenthetical illustrates the abbreviation failing that test rather than creating a second, looser one.
Delegation challenge: NOT_CLAIMED. No alternative scope is authorized.
Challenge evidence: TCOMMENT\_W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "written out (ATK on its own doesn''t)"

Compared alternative: K
Resolution: EXCLUDED. Rule 5 asks for the tier rules as they work in the store builds today and says that for when a new player gets their starting tier, where a write-up and the build disagree, go by the build. The build buckets a player when total games reach 10, and total games are wins plus losses, so the window is the first 10 games played. Leonard's DM asks for the tier numbers 'as they are today', so the DM answer follows the same build fact. 'First 10 levels' read as level plays is the same answer; only 'ten distinct levels' differs, and the build clause excludes it.
Resolution evidence: CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; WH\_GAMES (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 147-147): "return GetTotalWins() + GetTotalLosses();"; DMNUM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 52-52): "plus the tier and enrage numbers as they are today"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and share list. |
| writes | SAME | Same spreadsheet, shares, Linear comments and DM reply. |
| destinations | SAME | Same folder, shares, tickets and DM. |
| contents | DIFFERENT | Starting-tier window on the Rules in force tab and in the DM answer: first 10 games played (A) vs first 10 distinct levels (K). |

Authority chain: P → DMR → CARD\_R5W

Resolution relevance challenge: Not a strawman: three records (deck, ZOM-42, ZOM-199) say 'first 10 level(s)'. The card's own criterion is how the rules work in the store builds, and the build code fixes the unit as games, wins and losses.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied.
Challenge evidence: CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; WH\_GAMES (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/Player/WinHistory.cs lines 147-147): "return GetTotalWins() + GetTotalLosses();"

Compared alternative: L
Resolution: EXCLUDED. The checklist is Leonard's later change to the same two rules on the same card: its items are labelled 'rule 6 change' and 'rule 7 change', stated as decisions with a reason ('he''ll fix rows during the session'), and were added at 16:20, after his 14:04 description update and his 15:41 'rest of the card stands' comment. Under Eval 1 §2.1 check 1 a later applicable update by the same author for the same issue and scope resolves the earlier sentence without announcing replacement. Leonard's 19:48 DM points to the card (which carries the checklist) and his 20:07 reply asks for the Not shipped and Editor only keys. An unchecked item is a to-do for the card owner ('Julia owns this one'), not a hedge; no record says the changes are pending or tentative.
Resolution evidence: CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 87-87): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 89-89): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; CL\_ACT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 91-91): "'addChecklistToCard', '2025-09-30T16:20:11Z'"; UPD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 81-81): "'updateCard', '2025-09-30T14:04:31Z'"; DMR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 52-52): "the rules for the register are on the difficulty baseline card on the zm roadmap board"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Whether the checklist changes apply. |
| writes | DIFFERENT | L posts 2 Linear comments instead of 9. |
| destinations | DIFFERENT | L drops the seven Editor only and Not shipped tickets. |
| contents | DIFFERENT | Same register; the seven comments are missing. |

Authority chain: P → DMR → CL\_R6

Resolution relevance challenge: Not a strawman: the card description still literally says the Not shipped and Editor only tickets stay as they are and that everyone but Robert comments, and the items are unchecked. The quoted items name the exact rules they change and say what now happens; they post-date both the description and Leonard's 'rest of the card stands' comment, and come from the same author on the same card.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the later card change is applied.
Challenge evidence: CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 87-87): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; TCOMMENT\_S (Evals/task\_inputs/01\_Universe\_Inject.sql lines 83-83): "rest of the card stands."; CL\_ACT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 91-91): "'addChecklistToCard', '2025-09-30T16:20:11Z'"

Compared alternative: M
Resolution: EXCLUDED. Leonard's exclusion names its tickets in parentheses (30, 49, 50, 161, 262 and 275) and ZOM-378 is not among them. ZOM-378 is in scope as one of Blake's tier tickets, and his closing note says the fix lines the first levels up with their tier versions, which changes how hard those levels play, so Leonard's reason does not reach it either.
Resolution evidence: DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; Z378T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 348-348): "tiers: closing. level 1 is back in the list so the first levels line up with their tier versions again"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-378 on vs off. |
| writes | SAME | ZOM-378 is Live and gets no comment either way. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | One row fewer; DM total 23 and Live 15. |

Authority chain: P → DMX

Resolution relevance challenge: Not a strawman: ZOM-378's title says 'tutorial order problems' and its description is about tutorials. But the DM gives an explicit list, and the tiers: note quoted ties ZOM-378 to tier level versions, which is difficulty.
Delegation challenge: NOT_CLAIMED. No alternative scope is authorized.
Challenge evidence: DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; Z378T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 348-348): "tiers: closing. level 1 is back in the list so the first levels line up with their tier versions again"

Compared alternative: N
Resolution: EXCLUDED. Leonard's later DM reply takes off only four tickets by key and closes the list ('just those four, on top of the ones i already left off'), so no other editor or debug tooling ticket comes off. Blake's mail names the debug menu separately from the level editor, so ZOM-200 (debug menu) is not reached; ZOM-202 is open and goes on as Not shipped under rule 1. Leonard's first reply still asks for 'the editor only ones', which N leaves empty. The narrower level-editor fork is tested separately as Y. The exclusion is scoped to 'the analytics and tutorial tickets' with their keys listed, and in the same message Leonard asks for the keys of the editor only ones, which only makes sense if they stay on the list; the checklist's rule 6 change also has Editor only tickets commented, and card rule 3 lists Editor only as a status. The newer 'doesn't change how hard a level plays' (ZOM-258 note) and 'players never see it' (ZOM-312 review) lines each name one ticket by key or PR; card rule 3 keeps an Editor only status and the checklist comments on Editor only tickets, so the list still holds them.
Resolution evidence: DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 62-62): "just those four, on top of the ones i already left off."; DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"; CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 87-87): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"; CARD\_R3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Status is one of Live, Editor only, Replaced, Not shipped, judged against the store builds players have today."; MAIL\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "The level editor (Assets/Scripts/LevelEditor and the LevelDesigner panels), anything in an Editor folder and the debug menu (Assets/Scripts/Debug) are stripped before we ship to players on iOS and Android."; DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Editor-tooling tickets off vs on. |
| writes | DIFFERENT | N drops their comments. |
| destinations | DIFFERENT | N drops those Linear tickets. |
| contents | DIFFERENT | Rows, counts and DM keys differ. |

Authority chain: P → DMK

Resolution relevance challenge: The reason clause explains the listed tickets; the same message asks for editor only keys, which rules out dropping them.
Delegation challenge: NOT_CLAIMED. No alternative scope is authorized.
Challenge evidence: DMK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "in your reply put the keys of the not shipped ones and the editor only ones so i know who to chase"

Compared alternative: O
Resolution: EXCLUDED. Rule 1 now brings in 'any ticket Blake counts as tier work even if the title doesn't say so', marked by his closing note starting 'tiers:'; it does not require Blake to be the assignee. The ZOM-281 note is by usr\_cc3e90160f490686, which Linear /users/35 maps to arthur.blake@, and it starts 'tiers: closing.', 22 minutes before ZOM-281 was completed.
Resolution evidence: CARD\_R1B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "any ticket Blake counts as tier work even if the title doesn''t say so: his closing note on those starts with ''tiers:''"; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 278-278): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; LUSR\_AB (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /users/35): "arthur.blake@harmonygames.co"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | O drops ZOM-281. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rows and counts differ by one (23 / Live 15). |

Authority chain: P → DMR → CARD\_R1B

Resolution relevance challenge: Not a strawman: ZOM-281's assignee is another person and the old rule 1 wording tied scope to Blake's own tickets. The current rule 1 keys on the note, and the note's author id is Blake's.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R1B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "any ticket Blake counts as tier work even if the title doesn''t say so: his closing note on those starts with ''tiers:''"; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 278-278): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; LUSR\_AB (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /users/35): "arthur.blake@harmonygames.co"

Compared alternative: P
Resolution: EXCLUDED. Card rule 3 makes Blake's store builds mail the authority for what is in the store builds and what counts as shipped. The mail says both store builds were cut from main on Sep 26 and everything difficulty related was merged long before that; it strips only level editor and debug code, and ZOM-281 (win streak on replay) is a gameplay fix. ZOM-281 is Done, completed 2025-06-27, and Blake's closing note says it was checked on the dev build. Rule 1's 'never-merged' covers work that never landed, not a Done ticket the shipped-authority calls merged.
Resolution evidence: CARD\_R3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Status is one of Live, Editor only, Replaced, Not shipped, judged against the store builds players have today."; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 100-100): "Both were cut from main on Sep 26, and everything difficulty related was merged long before that."; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not."; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 278-278): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; Z281D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "2025-06-27T09:56:19Z"; Z281 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "Win streak not lost when replaying without main menu"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Live vs Not shipped for ZOM-281. |
| writes | DIFFERENT | P adds a ZOM-281 comment. |
| destinations | DIFFERENT | P adds ZOM-281. |
| contents | DIFFERENT | Status cell, DM counts and Not shipped keys differ. |

Authority chain: P → DMR → CARD\_R3B → MAIL\_MERGED

Resolution relevance challenge: Not a strawman: a complete GitHub scan finds no 'ZOM-281' string, so an Agent looking for a merged PR finds none. The card names the mail as the shipped authority and the mail answers the question for difficulty work as a class.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: CARD\_R3 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Status is one of Live, Editor only, Replaced, Not shipped, judged against the store builds players have today."; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 100-100): "Both were cut from main on Sep 26, and everything difficulty related was merged long before that."; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not."; Z281T (Evals/task\_inputs/01\_Universe\_Inject.sql lines 278-278): "VALUES ('cmt\_df69e4a92767cbff0000', 'ZOM-281', 'usr\_cc3e90160f490686', NULL, 'tiers: closing. checked on the dev build'"; Z281D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "2025-06-27T09:56:19Z"; Z281 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3334): "Win streak not lost when replaying without main menu"

Compared alternative: Q
Resolution: EXCLUDED. ZOM-42's 6-7 levels line is provisional ('to be defined later') and the same ticket's rule 1 gives the first 10 levels' average CPM; the deck and ZOM-199 also say first 10. Card rule 5 says that for when a new player gets their starting tier, where a write-up and the build disagree, go by the build, and the build buckets a player when total games reach 10. Leonard's DM asks for the tier numbers as they are today.
Resolution evidence: Z42TBD (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "to be defined later"; Z42S (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "1st 10 level avg CPM &gt; 90 (top 20%) moves to tier 1, rest stays in tier 0)"; DECK\_ST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0."; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; DMNUM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 52-52): "plus the tier and enrage numbers as they are today"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Starting-tier timing on the Rules in force tab and in the DM answer: 10 games vs 6-7 levels. |

Authority chain: P → DMR → CARD\_R5W

Resolution relevance challenge: Not a strawman: ZOM-42 is the system ticket rule 4 sends to the rules tab, and its 6-7 sentence is the only text that answers 'when' in so many words. Its own 'to be defined later', its own rule 1, the deck, ZOM-199 and the build all give 10.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: Z42TBD (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "to be defined later"; Z42S (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "1st 10 level avg CPM &gt; 90 (top 20%) moves to tier 1, rest stays in tier 0)"; DECK\_ST (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0."; CARD\_R5W (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build."; TM\_BUCKET (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 30-32): "if (totalGames == 10)"; DMNUM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 52-52): "plus the tier and enrage numbers as they are today"

Compared alternative: R
Resolution: EXCLUDED. Blake's reply is written 'for the rules tab' and says the build checks cpm &gt; 90, not &gt;= 90, so 90 exactly stays on tier 0; card rule 5 asks for the starting tier 'as they work in the store builds today', and rule 6 has the ZOM-199 comment say what the build does; TierManager.cs line 93 is 'cpm &gt; 90.0f'. Rule 5's narrowed build clause covers when the starting tier is given, so the threshold rests on the rules-tab note and the opening clause.
Resolution evidence: REPLY\_TAB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "For the rules tab: the starting tier check in the code is cpm &gt; 90, not &gt;= 90"; REPLY90 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "so 90 exactly stays on tier 0"; CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; TM\_CPM (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 93-93): "case var cpm when cpm &gt; 90.0f:"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set (the ZOM-199 comment is in both). |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Threshold: above 90 vs 90 or more. |

Authority chain: P → DMR → CARD\_R5B

Resolution relevance challenge: Not a strawman: the deck and ZOM-199 both say 90 or more. Blake's reply, addressed to the rules tab, and the build say otherwise, and rule 5 asks for the starting tier as it works in the store builds.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card rule is applied, not delegated.
Challenge evidence: REPLY\_TAB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "For the rules tab: the starting tier check in the code is cpm &gt; 90, not &gt;= 90"; REPLY90 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "so 90 exactly stays on tier 0"; CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; TM\_CPM (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/TierManager.cs lines 93-93): "case var cpm when cpm &gt; 90.0f:"

Compared alternative: S
Resolution: EXCLUDED. Card rule 5 (revision 22) now settles this item directly: 'For which games promotion and demotion look at, write it the way ZOM-42 words it.' ZOM-42 words the window as up to the most recent 10 attempts / the last 10 games played, with the record reset after every promotion or demotion, and says a losing streak of 4 in a row can still trigger at any time. The later, more specific sentence in the same rule governs the opening 'as they work in the store builds today' for this one item, the same way rule 5's enrage sentence governs the enrage rows (fork H). The code's first-10-since-the-last-change window is therefore not what the tab states.
Resolution evidence: CARD\_R5PD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "For which games promotion and demotion look at, write it the way ZOM-42 words it."; Z42MR (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we evaluate UP TO THE MOST RECENT 10 attempts of the player"; Z42LAST (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we constantly look at the last 10 games played"; Z42RESET (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "every time a promotion/demotion happens, the record is reset and we start at 0 games played"; Z42STREAK (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "A losing streak of 4 games in a row can still trigger at any time"; Z42DEM (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we demote someone when their win rate for up to the last 10 games is 50% or lower"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rules in force tab: promotion and demotion over the latest 10 (and 4 in a row at any time) vs over the first 10 and first 4 games since the last tier change. |

Authority chain: P → DMR → CARD\_R5PD

Resolution relevance challenge: Not a strawman: last round's deep recheck passes P1 and P2 raised it and it failed UGT. The new card sentence names exactly this item ('which games promotion and demotion look at') and names ZOM-42 as the wording to use, and ZOM-42 states the window in one consistent way across its promotion, demotion and streak paragraphs.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card names the wording to use.
Challenge evidence: CARD\_R5PD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "For which games promotion and demotion look at, write it the way ZOM-42 words it."; Z42MR (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we evaluate UP TO THE MOST RECENT 10 attempts of the player"; Z42STREAK (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "A losing streak of 4 games in a row can still trigger at any time"

Compared alternative: T
Resolution: EXCLUDED. Rule 5 opens by asking for promotion and demotion 'as they work in the store builds today', and the build has the 50%-or-lower demotion rule (WinRateRule.cs line 31). ZOM-42, the other write-up rule 5 names and the one it sends promotion/demotion wording to, has the same rule. The deck's demotion line omits it; it does not say there is no such rule, so there is no write-up/build disagreement for a tie-break to settle. Both demotion rules go on the tab.
Resolution evidence: CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; WR\_DEM50 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/WinRateRule.cs lines 31-31): "new WinRateRule(-1, 100, 10, 0.5f, RuleComparisonType.LessThanOrEqualTo, -1),"; Z42DEM (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we demote someone when their win rate for up to the last 10 games is 50% or lower"; CARD\_R5PD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "For which games promotion and demotion look at, write it the way ZOM-42 words it."; DECK\_DEM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Demotion: 4 losses in a row moves you down one tier."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same ticket set, statuses, comments and shares. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rules in force demotion: two rules (4 in a row, or 50% or lower over up to the last 10) vs the 4-loss rule only. |

Authority chain: P → DMR → CARD\_R5B

Resolution relevance challenge: Not a strawman: the narrowed build clause no longer covers demotion, and the deck is a named write-up whose demotion line lists only the 4-loss rule. It is excluded because the deck is silent on the 50% rule rather than contrary, while the build and ZOM-42 both have it and rule 5 asks for the rules as they work in the store builds.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; the card names the wording to use.
Challenge evidence: CARD\_R5B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they work in the store builds today."; WR\_DEM50 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d/Assets/Scripts/DynamicDifficulty/WinRateRule.cs lines 31-31): "new WinRateRule(-1, 100, 10, 0.5f, RuleComparisonType.LessThanOrEqualTo, -1),"; Z42DEM (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3485): "we demote someone when their win rate for up to the last 10 games is 50% or lower"; DECK\_DEM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 41-41): "Demotion: 4 losses in a row moves you down one tier."

Compared alternative: U
Resolution: EXCLUDED. Leonard's notes for monday, attached to the card and written after the card text (doc 2025-09-30T15:47-15:51Z; card description updated 14:04:31Z), are 'three things for the register', and one of them is Arthur's access: he is 'only listening in', so 'view access is enough for him'. Rule 7's default for him is comment, so the line has no effect unless it lowers him to view. The later checklist (16:20:11Z) changes rule 7 only for Brian and says nothing about Arthur.
Resolution evidence: NOTES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "julia, three things for the register:"; NOTES\_ART (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "arthur is only listening in on monday, view access is enough for him."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 89-89): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; TATT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 93-93): "'notes for monday', '68daca5871dba40417a00383'"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Arthur viewer vs commenter. |
| writes | DIFFERENT | Different role on the arthur.blake@ share. |
| destinations | SAME | Same four shares. |
| contents | SAME | Same register and DM. |

Authority chain: P → DMR → NOTES → NOTES\_ART

Resolution relevance challenge: Not a strawman: 'enough' can be read as a floor. But the doc lists changes to the register setup, and 'only listening in' gives the reason he does not need to comment; reading it as a floor makes the instruction do nothing.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; Leonard's instruction is applied, not delegated.
Challenge evidence: NOTES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "julia, three things for the register:"; NOTES\_ART (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "arthur is only listening in on monday, view access is enough for him."; CARD\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can edit, everyone else comments."; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 89-89): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"; TATT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 93-93): "'notes for monday', '68daca5871dba40417a00383'"

Compared alternative: V
Resolution: EXCLUDED. The notes name ZOM-258 and say to leave it off; the DM reply opens 'forgot one thing', which adds exclusions rather than replacing earlier ones, and no record puts ZOM-258 back. Both are Leonard's, and they cover different tickets, so both apply (scope check).
Resolution evidence: NOTES\_258 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "leave ZOM-258 off the list. it''s only the icon players see over a monster, it doesn''t change how hard a level plays."; DMF (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "forgot one thing: leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275)"; DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-258 off vs Live. |
| writes | SAME | Same write set. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Rows 24 vs 25; Live 16 vs 17. |

Authority chain: P → DMR → NOTES → NOTES\_258

Resolution relevance challenge: The quoted note names the ticket by key; 'forgot one thing' marks the DM reply as an addition, so it cannot be read as the complete list.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; Leonard's instruction is applied, not delegated.
Challenge evidence: NOTES\_258 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "leave ZOM-258 off the list. it''s only the icon players see over a monster, it doesn''t change how hard a level plays."; DMF (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "forgot one thing: leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275)"; DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"

Compared alternative: W
Resolution: EXCLUDED. Rule 1 asks for a title match Blake marked 'not tiers' in his review on its PR, and does not say the PR has to be someone else's. Blake left review rev\_8 on PR match3d\#265 (title 'ZOM-312'), and its review comment says 'not tiers ... leave it out when we list tier work'. So ZOM-312 stays off and gets no comment.
Resolution evidence: CARD\_R1NT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "It works the other way too: a title match Blake marked ''not tiers'' in his review on its PR stays off."; GH265REV (Evals/task\_inputs/01\_Universe\_Inject.sql lines 173-173): "'harmonygames-Games/match3d\#265\#rev\_8', 'harmonygames-Games/match3d\#265', 'EMPLOYEE\_0025\_GITHUB\_USERNAME', 'COMMENTED'"; GH265RC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work"; PR265 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /pull\_requests/2147): ""title": "ZOM-312""; GHU\_AB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /users/6): ""name": "Arthur Blake""

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-312 off vs Editor only. |
| writes | DIFFERENT | W adds a ZOM-312 comment. |
| destinations | DIFFERENT | W adds Linear ZOM-312. |
| contents | DIFFERENT | Rows 24 vs 25; Editor only 4 vs 5; keys differ. |

Authority chain: P → DMR → CARD\_R1NT

Resolution relevance challenge: Rule 1 asks only for Blake's review on the ticket's PR. Review rev\_8 is authored by EMPLOYEE\_0025 (Arthur Blake) on PR \#265, and the comment is part of that review.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; Leonard's instruction is applied, not delegated.
Challenge evidence: CARD\_R1NT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "It works the other way too: a title match Blake marked ''not tiers'' in his review on its PR stays off."; GH265REV (Evals/task\_inputs/01\_Universe\_Inject.sql lines 173-173): "'harmonygames-Games/match3d\#265\#rev\_8', 'harmonygames-Games/match3d\#265', 'EMPLOYEE\_0025\_GITHUB\_USERNAME', 'COMMENTED'"; GH265RC (Evals/task\_inputs/01\_Universe\_Inject.sql lines 69-69): "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work"; PR265 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /pull\_requests/2147): ""title": "ZOM-312""; GHU\_AB (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /users/6): ""name": "Arthur Blake""

Compared alternative: X
Resolution: EXCLUDED. The prompt says to reply with what Leonard asked for, after going through his ask and everything it points to. His notes, reached through the card the DM points to, ask: 'when you reply to me, also tell me which ticket replaced which.' Both are Leonard's asks to Julia and they cover different content, so both apply.
Resolution evidence: P (Evals/task\_inputs/04\_Prompt.txt): "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system before monday's tuning session. can you take it off my plate? go through his ask and everything it points to and build the register the way he set it up. put it in the zm difficulty folder and share it with everyone on monday's tuning invite. if his rules say something needs to happen on the tickets, go ahead and do that too. then reply to leonard in the dm with what he asked for. go with your read on the details, no need to check with me first"; NOTES\_REPL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "when you reply to me, also tell me which ticket replaced which."; DMR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 52-52): "the rules for the register are on the difficulty baseline card on the zm roadmap board"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same register decisions. |
| writes | SAME | Same DM reply write. |
| destinations | SAME | Same DM. |
| contents | DIFFERENT | The DM includes or leaves out 'ZOM-282 replaced ZOM-254'. |

Authority chain: P → DMR → NOTES → NOTES\_REPL

Resolution relevance challenge: The note addresses the reply directly ('when you reply to me') and is Leonard's own ask; the prompt's 'what he asked for' covers his asks through everything the DM points to.
Delegation challenge: NOT_CLAIMED. No materially different final call is accepted; Leonard's instruction is applied, not delegated.
Challenge evidence: P (Evals/task\_inputs/04\_Prompt.txt): "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system before monday's tuning session. can you take it off my plate? go through his ask and everything it points to and build the register the way he set it up. put it in the zm difficulty folder and share it with everyone on monday's tuning invite. if his rules say something needs to happen on the tickets, go ahead and do that too. then reply to leonard in the dm with what he asked for. go with your read on the details, no need to check with me first"; NOTES\_REPL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "when you reply to me, also tell me which ticket replaced which."; DMR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 52-52): "the rules for the register are on the difficulty baseline card on the zm roadmap board"

Compared alternative: Y
Resolution: EXCLUDED. Leonard's 2025-09-30T21:16:42Z DM reply (revision 30) now names no category and gives no category-wide reason. It takes off four keys and closes the list in so many words: 'just those four, on top of the ones i already left off.' ZOM-173, 277 and 315 are not among the four, and not among the ones he already left off (the six in his first DM reply, ZOM-258 in his notes). So they stay on the list and, as level-editor-only work stripped from store builds (Blake's mail), they are Editor only and get the checklist's rule 6 comment. Same author, latest message, same issue (which tickets come off): the newer, explicit closed list settles it (checks 1-3); the scope check (4) keeps the rest of the card and checklist unchanged.
Resolution evidence: DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 62-62): "just those four, on top of the ones i already left off."; DMX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "leave the analytics and tutorial tickets off the list (30, 49, 50, 161, 262 and 275), they don''t change how hard a level plays"; NOTES\_258 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "leave ZOM-258 off the list. it''s only the icon players see over a monster, it doesn''t change how hard a level plays."; MAIL\_STRIP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "A ticket whose changes are only level editor or debug tooling never reached players, Done or not."; CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 87-87): "rule 6 change: the Editor only and Not shipped tickets get a comment too, saying the change isn''t in the store builds"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | ZOM-173, 277 and 315 on as Editor only (A) vs off (Y). |
| writes | DIFFERENT | Three Linear comments on ZOM-173, 277 and 315 under A, none under Y. |
| destinations | DIFFERENT | Linear ZOM-173, 277, 315 touched under A only. |
| contents | DIFFERENT | 24 vs 21 rows; Editor only 4 vs 1; DM total and Editor only keys differ. |

Authority chain: P → DMR2\_LE

Resolution relevance challenge: Not a strawman: the four keys are all level editor tickets by title, so a reader could look for the theme. But Leonard's own words now close the list ('just those four'), and the message no longer names the category or gives a reason that reaches other tickets. The cited line addresses exactly this difference: whether tickets beyond the four come off.
Delegation challenge: NOT_CLAIMED. Leonard's explicit closed list is applied; no alternative is delegated.
Challenge evidence: DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 62-62): "just those four, on top of the ones i already left off."

Compared alternative: Z
Resolution: EXCLUDED. Leonard's DM reply at 2025-09-30T21:16:42Z, after the checklist (added 16:20:11Z), takes back the checklist's rule 7 change for Brian: 'scratch brian editing, robert will fix rows in the session. comment access is enough for brian'. It is the same author and the same item, later in time, and it names the replacement role.
Resolution evidence: DMR2\_BR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 62-62): "and scratch brian editing, robert will fix rows in the session. comment access is enough for brian"; CL\_R7 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 89-89): "rule 7 change: Brian gets edit as well, he''ll fix rows during the session"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Brian editor vs commenter. |
| writes | DIFFERENT | Different role on the brian.foster@ share. |
| destinations | SAME | Same four shares. |
| contents | SAME | Same register and DM. |

Authority chain: P → DMR2\_BR

Resolution relevance challenge: Not a strawman: the checklist item is still on the card. But 'scratch brian editing' takes that item back by name and gives the reason (Robert fixes rows instead).
Delegation challenge: NOT_CLAIMED. Leonard's later instruction is applied, not delegated.
Challenge evidence: DMR2\_BR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 62-62): "and scratch brian editing, robert will fix rows in the session. comment access is enough for brian"

Compared alternative: AA
Resolution: EXCLUDED. The prompt points to what Leonard DM'd on Tuesday about the baseline and asks for the reply in the DM. The 21:16:42Z message is Leonard's, in the same DM, on the same Tuesday, and opens 'one more for the baseline', so it adds to his baseline ask. Its place in a thread under Julia's Monday question doesn't change who wrote it or what it is about. Julia is a DM member, the parent shows reply\_count 1, and Slack thread reads are cataloged.
Resolution evidence: DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 62-62): "one more for the baseline: take 162, 163, 201 and 250 off the list too."; P (Evals/task\_inputs/04\_Prompt.txt): "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | 28 vs 24 tickets; Brian's role. |
| writes | DIFFERENT | Four extra comments; different Brian role. |
| destinations | DIFFERENT | Linear ZOM-162, 163, 201, 250 touched vs not. |
| contents | DIFFERENT | 28 vs 24 rows and DM counts and keys. |

Authority chain: P → DMR2\_LE

Resolution relevance challenge: Not a strawman: the message is in a thread under Julia's own message, which a reader of the request thread alone would miss. But source identity (Leonard), timing (Tuesday, after the request) and subject ('for the baseline') tie it to the ask.
Delegation challenge: NOT_CLAIMED. No delegation claimed.
Challenge evidence: DMP (Evals/task\_inputs/01\_Universe\_Inject.sql lines 60-60): "leonard, anything you need from me before monday''s tuning session?"; DMR2\_LE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 62-62): "one more for the baseline"

Compared alternative: AB
Resolution: EXCLUDED. Leonard's 20:07Z reply, in his own request thread and after the 16:20Z checklist, adds to those same comments: 'when you comment on the editor only and not shipped ones, put the two builds in the comment (ios 0.3.49 and android 0.3.133)'. Same author, later, same scope; it adds content and does not replace the checklist's wording, so both apply.
Resolution evidence: DMR1\_BLD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "when you comment on the editor only and not shipped ones, put the two builds in the comment (ios 0.3.49 and android 0.3.133) so people can see what you checked against"; P (Evals/task\_inputs/04\_Prompt.txt): "go through his ask and everything it points to"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same tickets and statuses. |
| writes | SAME | Same seven comments are posted. |
| destinations | SAME | Same Linear tickets. |
| contents | DIFFERENT | Build numbers present vs absent in seven comments. |

Authority chain: P → DMR1\_BLD

Resolution relevance challenge: Not a strawman: the checklist alone words the comment without builds. The later DM reply settles it.
Delegation challenge: NOT_CLAIMED. No delegation claimed.
Challenge evidence: CL\_R6 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 87-87): "saying the change isn''t in the store builds"; DMR1\_BLD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "put the two builds in the comment (ios 0.3.49 and android 0.3.133)"

Compared alternative: AC
Resolution: EXCLUDED. Card rule 3 names 'Blake''s store builds mail and his reply to it', and rule 6 the same pair. The 13:26Z mail is from Blake to the same four people the same day, opens 'Two things I left out of the mail this morning.', and its In-Reply-To header points at the store builds mail. A changed subject does not change what it is. It is in Julia's inbox (her mailbox copy, INBOX label) and Gmail reads and search are cataloged.
Resolution evidence: CARD\_R3B (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "What is in the store builds and what counts as shipped: Blake''s store builds mail and his reply to it."; MAIL2\_HDR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "Two things I left out of the mail this morning."; MAIL2\_IRT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "\{"name": "In-Reply-To", "value": "&lt;CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com&gt;"\}"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Editor only status and the ZOM-199 comment exist vs not. |
| writes | DIFFERENT | Four Editor only comments and the ZOM-199 comment vs none. |
| destinations | DIFFERENT | Linear ZOM-199, 173, 200, 277, 315 touched vs not. |
| contents | DIFFERENT | Live 16/Editor only 4 vs Live 20/Editor only 0. |

Authority chain: P → DMR → CARD\_R3B → MAIL2\_HDR

Resolution relevance challenge: Not a strawman: the mail is in its own Gmail thread with a new subject, so a reader of the first thread alone would miss it. The card's own wording, the opening line and the reply header tie it to the store builds mail.
Delegation challenge: NOT_CLAIMED. No delegation claimed.
Challenge evidence: MAIL2\_SUBJ (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "'editor stuff and ZOM-199, before Monday'"; MAIL2\_HDR (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "Two things I left out of the mail this morning."

Compared alternative: AD
Resolution: EXCLUDED. Leonard scopes the build numbers to 'the editor only and not shipped ones'. Adding them to the ZOM-199 or ZOM-254 comment is extra wording, not a different comment, ticket or decision; it does not contradict any instruction. Not material; the rubric should neither require nor penalize it.
Resolution evidence: DMR1\_BLD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "when you comment on the editor only and not shipped ones"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same register. |
| writes | SAME | Same nine comments on the same tickets. |
| destinations | SAME | Same. |
| contents | SAME | Required content present in both; one adds a harmless reference. |

Authority chain: P → DMR1\_BLD

Resolution relevance challenge: Weak alternative; recorded so the rubric doesn't grade the extra mention.
Delegation challenge: NOT_CLAIMED. No delegation claimed.
Challenge evidence: DMR1\_BLD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 58-58): "when you comment on the editor only and not shipped ones"

Compared alternative: AE
Resolution: EXCLUDED. Rule 6 says to comment 'with what the build does' where Blake's mail or reply says a ticket's text is wrong. Blake says ZOM-199 is wrong on both points: 'ZOM-199 says &gt;= 90 after the first 10 levels' while the code checks cpm &gt; 90 'when a player''s 10th game ends, wins and losses both counted, not after 10 levels cleared'. A comment with only the threshold covers the sharper error; both are the same single comment on the same ticket. The threshold is the required content; the timing is supported and should be accepted, not required.
Resolution evidence: CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does"; REPLY (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "ZOM-199 says &gt;= 90 after the first 10 levels, but the code never changed from the original spec"; MAIL2\_10TH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "it runs when a player''s 10th game ends, wins and losses both counted, not after 10 levels cleared"; Z199D (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3243): "If first 10 level CPM &gt;= 90, then tier 1, otherwise everyone else stays at default tier 0."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same register. |
| writes | SAME | One comment on ZOM-199 either way. |
| destinations | SAME | Linear ZOM-199. |
| contents | SAME | Both state what the build does for the threshold Blake flags; the timing is additive detail from the same mail. |

Authority chain: P → DMR → CARD\_R6N

Resolution relevance challenge: Edge content question, not a different write; carried to the rubric guidance.
Delegation challenge: NOT_CLAIMED. No delegation claimed.
Challenge evidence: REPLY90 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "so 90 exactly stays on tier 0"

Compared alternative: AF
Resolution: EXCLUDED. Card rule 2 adds the three things Robert asked for to the layout, and Robert's reply in the group DM Julia belongs to names them. Leaving them out drops a stated column requirement.
Resolution evidence: CARD\_R2R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "plus the three things Robert asked for when I asked him in our group chat."; GDM\_R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "who it''s assigned to in linear, the day it got marked done (leave it blank if it never got done), and its linear priority."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same as A. |
| writes | SAME | Same as A. |
| destinations | SAME | Same as A. |
| contents | DIFFERENT | A has three more columns. |

Authority chain: P → DMR → CARD\_R2R → GDM\_R

Resolution relevance challenge: The card sentence points to the group chat and the reply names the three columns; Julia is a member of CAFC495E4006.
Delegation challenge: NOT_CLAIMED. No delegation claimed; the record states the requirement.
Challenge evidence: CARD\_R2R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "plus the three things Robert asked for when I asked him in our group chat."; GDM\_R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "who it''s assigned to in linear, the day it got marked done (leave it blank if it never got done), and its linear priority."

Compared alternative: AG
Resolution: SAME_MATERIAL_RESULT. Robert asks for the columns 'after status' so he can sort by them; both placements come after Status and carry the same cells, and nothing in the agenda (which names only the two tabs) fixes column positions. Column position is layout, not content; the rubric should accept either placement after Status.
Resolution evidence: GDM\_R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "yeah three things after status please."; GDM\_R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "i want to sort by them in the session"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same as A. |
| writes | SAME | Same as A. |
| destinations | SAME | Same as A. |
| contents | SAME | Same three columns with the same values per row; only their position relative to the replaced-by column differs. |

Resolution relevance challenge: 'after status' is met by both; the stated purpose (sorting) works with either.
Delegation challenge: NOT_CLAIMED. No delegation claimed; the record states the requirement.
Challenge evidence: GDM\_R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "yeah three things after status please."; GDM\_R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "i want to sort by them in the session"

Compared alternative: AH
Resolution: EXCLUDED. Source identity: the card names 'the three things Robert asked for when I asked him in our group chat'. The notes doc's three things are Leonard's own, written to Julia in a Google Doc, not Robert's answer in a group chat. Robert's reply is the only message where Leonard asks Robert about the list.
Resolution evidence: CARD\_R2R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "the three things Robert asked for when I asked him in our group chat."; GDM\_Q (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "robert anything you want on julia''s difficulty list for monday?"; GDM\_R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "yeah three things after status please."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same as A. |
| writes | SAME | Same as A. |
| destinations | SAME | Same as A. |
| contents | DIFFERENT | AH omits the three columns. |

Authority chain: P → DMR → CARD\_R2R → GDM\_R

Resolution relevance challenge: The card names Robert and the group chat; the notes doc is Leonard's. Both lists apply: the notes' three items and Robert's three columns.
Delegation challenge: NOT_CLAIMED. No delegation claimed; the record states the requirement.
Challenge evidence: CARD\_R2R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "the three things Robert asked for when I asked him in our group chat."; GDM\_Q (Evals/task\_inputs/01\_Universe\_Inject.sql lines 48-48): "robert anything you want on julia''s difficulty list for monday?"; GDM\_R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "yeah three things after status please."

Compared alternative: AI
Resolution: EXCLUDED. Robert says to leave the day blank if the ticket never got done; ZOM-280 was cancelled (canceled\_at set, completed\_at null), so it never got done.
Resolution evidence: GDM\_R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "(leave it blank if it never got done)"; Z280 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3333): ""canceled\_at": "2025-06-20T23:38:27Z", "completed\_at": null"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same as A. |
| writes | SAME | Same as A. |
| destinations | SAME | Same as A. |
| contents | DIFFERENT | One cell differs. |

Authority chain: P → DMR → CARD\_R2R → GDM\_R

Resolution relevance challenge: Robert's parenthesis settles cancelled and open tickets; Linear shows ZOM-280 cancelled with no completed\_at.
Delegation challenge: NOT_CLAIMED. No delegation claimed; the record states the requirement.
Challenge evidence: GDM\_R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "(leave it blank if it never got done)"; Z280 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3333): ""canceled\_at": "2025-06-20T23:38:27Z", "completed\_at": null"

Compared alternative: AJ
Resolution: EXCLUDED. Card rule 1 defines Not shipped by lifecycle (open, cancelled, never-merged); ZOM-199 is Done and Blake's store builds mail says everything difficulty related was merged before the Sep 26 cut. Card rule 6 handles exactly this case, a ticket whose text Blake's mail or reply says is wrong, with a separate comment kind ('what the build does'), which only makes sense for a ticket whose change is in the build; the checklist's 'isn't in the store builds' comment is for the Editor only and Not shipped tickets. The CPM-based starting tier ZOM-199 asks for runs in the build; only its threshold text is off.
Resolution evidence: CARD\_R1NS (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "open, cancelled and never-merged ones are in, as Not shipped"; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does"; CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 100-100): "everything difficulty related was merged long before that."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Live vs Not shipped for ZOM-199. |
| writes | DIFFERENT | Different ZOM-199 comment. |
| destinations | SAME | Same ticket, sheet and DM. |
| contents | DIFFERENT | Counts 16/3 vs 15/4 and keys. |

Authority chain: P → DMR → CARD\_R3B → MAIL\_MERGED

Resolution relevance challenge: Rule 6's wrong-text clause is written for ZOM-199's situation and asks for 'what the build does'; rule 1 plus Blake's merged statement keep a Done, merged gameplay ticket out of Not shipped.
Delegation challenge: NOT_CLAIMED. No delegation; the card rules decide.
Challenge evidence: CARD\_R1NS (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "open, cancelled and never-merged ones are in, as Not shipped"; CARD\_R6N (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does"; CARD\_R6X (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off."; MAIL\_MERGED (Evals/task\_inputs/01\_Universe\_Inject.sql lines 100-100): "everything difficulty related was merged long before that."

Strongest-alternative challenge (AH): AH is the strongest new alternative: Leonard's notes for monday doc, attached to the same card, opens with 'julia, three things for the register:', so an Agent that doesn't search Slack group chats can take those as the three things and add no columns. Card rule 2 names Robert and 'our group chat', and the only such exchange is Leonard's question and Robert's reply in the group DM Julia belongs to.
Challenge evidence: CARD\_R2R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 73-73): "the three things Robert asked for when I asked him in our group chat."; NOTES (Evals/task\_inputs/01\_Universe\_Inject.sql lines 21-21): "julia, three things for the register:"; GDM\_R (Evals/task\_inputs/01\_Universe\_Inject.sql lines 50-50): "yeah three things after status please."

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

---

### Phase 3: Universe Feasibility

**Data Existence:** PASS (5). Every needed entity is verified and retrievable through cataloged reads, including assignee, `completed_at` and priority on all 24 tickets.

**Cross-Service Coherence:** PASS (5). No inconsistency in task-touched data.
- **Lines 48/50 (new group-DM messages):**
  - Both authors (EMPLOYEE_0038 Leonard, EMPLOYEE_0016 Robert) are members of `CAFC495E4006`.
  - Apostrophes are doubled ("julia''s", "she''s", "it''s").
  - ts and created_at agree (1759226461 = 2025-09-30T10:01:01Z; 1759229513 = 10:51:53Z).
  - Parent reply_count 1 / reply_users_count 1 / latest_reply equals the reply ts.
  - Both are before the 14:04:31Z card update that cites them, and before the clock.
  - "she's putting it together from the card" fits the card created 2025-09-29 as "Difficulty baseline (Julia)".
- **Card rule 2 (lines 73/81):** the new sentence is identical in the card desc and its updateCard action. "when I asked him" is past tense, consistent with the 10:01Z question before the 14:04Z update.
- **Robert's columns vs Linear:** every ticket the register lists has an assignee and a priority. "Blank if never done" matches exactly the three Not shipped tickets with `completed_at` null (ZOM-202 In Progress, ZOM-280 Canceled, ZOM-293 Todo). Every Done ticket has a `completed_at`; no Done ticket lacks one, and no open ticket has one.
- **Unchanged rows:** REUSED (byte-identical apart from the +4 shift) from earlier rounds and the same-hash `0_injection.md`.
- **Known base-data issues (not scored):** none touched; the task uses no Snowflake or Confluence data.
- **Platform (not scored):** Linear user `usr_EMPLOYEE_0032` (`/users/21`) carries the anonymized token "EMPLOYEE_0032_NAME" as its name; six tickets (ZOM-246, 263, 274, 281, 254, 280) show it as assignee. Under deep_recheck's known platform defects, the token as shown is correct, and the real name only when a persona-visible record maps it (none found).
- **Not task-touched (not scored), carried:** `Monster.cs` passes a single `enrageDamagePercentage`; the distractor card action's board label "Product Roadmap" follows the base convention.
- **Injection SQL considered:** Yes. Static integrity evidence REUSED from `0_injection.md` (same hash `f6afeda7…62f8`, checks A–C; lint re-run here, 0 flags). The task-relevant Check C items for the new rows were redone above.
- **Prompt-specific sources, access and configuration:** supported. No error/async config or dynamic context applies.

---

### Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|-----------|--------------|-------------|---------------|
| Prompt | Unique Ground Truth | 5 | New forks AF, AH, AI, AJ settled by card rule 2, source identity, Robert's blank rule and card rules 1/6; AG same result; B–AE carried |
| Prompt | Feasibility | 5 | All asks cataloged; the three new column fields exist on every ticket |
| Prompt | Persona ACL Reachability | 5 | Julia is in the group DM; both DM threads, both Blake mails and the invite visible |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 5 | Writes and columns don't diverge |
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
| Universe | Cross-Service Coherence | 5 | New rows consistent with channel membership, the card and Linear |

---

### Issues Found

None.

### Recommended Improvements

1. **Bring the OEs and rubric to this round's SQL before /oe and /rubric.**
   - **Unchanged:** 24 tickets (Live 16; Editor only 4: ZOM-173, 200, 277, 315; Replaced 1: ZOM-254 by ZOM-282; Not shipped 3: ZOM-202, 280, 293); 9 comments, the seven Editor only / Not shipped ones naming iOS 0.3.49 and Android 0.3.133; shares robert@ edit, brian.foster@ and leonard.hayes@ comment, arthur.blake@ view.
   - **New: Robert's three columns.** Add an OE step that reads Robert's reply in the group DM with Leonard, Robert and Julia (2025-09-30 10:51 UTC). Add rubric rows for:
     - Linear assignee per ticket;
     - the day marked done (Linear `completed_at`), blank for ZOM-202, ZOM-280 and ZOM-293;
     - Linear priority.
   - **Rubric acceptance for those columns:**
     - Accept the Pacific or the UTC day where they differ (ZOM-200: 06-13 UTC / 06-12 PT; ZOM-274 and ZOM-282: 06-21 UTC / 06-20 PT).
     - Accept priority as the number (1–4) or Linear's label (Urgent / High / Medium / Low).
     - Accept the assignee as shown in Linear: the token "EMPLOYEE_0032_NAME" for ZOM-246, 263, 274, 281, 254 and 280, and a name or the email for arthur.blake@ and owen.baker@.
     - Accept the three columns straight after Status or after the replaced-by column.
     - Don't fill a date for ZOM-280's cancellation.
   - **Keep the two "three things" lists apart:** the notes doc's three items (ZOM-258 off, Arthur view, which ticket replaced which) still apply on their own.
2. **Carried:**
   - ZOM-199 comment: require cpm > 90 (90 exactly stays on tier 0); accept, don't require, the 10th-game timing.
   - Starting tier: accept "after the 10th game" or "after 10 levels played"; reject "after 10 levels cleared/won".
   - Don't grade ticking the checklist items, a "rage by level" tab, or whether the DM reply is a thread reply or a top-level message.
3. **Optional, cosmetic (carried from /injection C-7):** the two group-DM messages are at 03:01 and 03:51 PT. If you move them, keep both before the 14:04:31Z card update. Not a defect; any SQL change outdates /injection and every later pass.

---

## Deep Recheck

Passes: P1, P2, P3 and P4 on Opus 5.5 (claude-opus-5-5), session effort, each blind to the main review. Each ran as a fresh subagent given only the saved prompt, task details and injection SQL (not `reports/`, OEs, rubric or trajectory), the persona references, `SEARCH.md`, `common_errors.md` and `deep_recheck.md`. Every cited record was reopened in the main session.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 7 sentences; 14 forks | 2 | 1 (as fork AJ, excluded) |
| P2 | 7 sentences; every SQL row | 4 | 0 (1 platform) |
| P3 | 7 sentences; 13 premises; 182 SQL statements | 0 | 0 |
| P4 | 7 sentences | 2 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| P1-DR1 | P1 | "go through his ask and everything it points to and build the register the way he set it up." | Blake's reply (line 138) "ZOM-199 says >= 90 after the first 10 levels, but the code never changed from the original spec"; card rules 1, 4, 6; Linear ZOM-199 Done | §2 set membership | UGT | CONFIRMED as a fork, recorded as AJ and EXCLUDED | Rejection-grade quotes rule out Reading B: card rule 1 "open, cancelled and never-merged ones are in, as Not shipped" (ZOM-199 is Done); Blake's mail "everything difficulty related was merged long before that."; rule 6 "where Blake''s store builds mail or his reply to it says a ticket''s text is wrong, comment on that ticket with what the build does". That comment kind only fits a ticket whose change is in the build, and the build runs the CPM starting tier ZOM-199 asks for. Live 16 / Not shipped 3 stands. UGT stays 5 |
| P1-DR2 | P1 | "build the register the way he set it up." | Group DM `abe096ff…` "yeah three things after status please" | §2 what gets written | Clarity (advisory 3) | REJECTED | Same as fork AG (SAME_MATERIAL_RESULT): both placements are "after status" with the same cells, and the writes don't differ. The prompt's request is clear; the record sets an order both placements meet. Rubric note added (accept either placement after Status) |
| P2-DR1 | P2 | "go through his ask and everything it points to" | SQL columns absent from the unverified schema snapshot (linear_comments `sequence`, github `seq`/`side`/…, slides `notes`/`table_json`/`ordinal`) | §6.8 | Schema compatibility | REJECTED (advisory) | `schema/README.md`: the snapshot is unverified and a missing column is advisory only. Eval 0 G1, carried as an evidence limit |
| P2-DR2 | P2 | (Robert's "who it''s assigned to in linear") | Linear `/users/21` "EMPLOYEE_0032_NAME"; six assignees | §3 | PLATFORM:anonymized-token | Recorded, not scored | deep_recheck known platform defects: the token as shown is correct; no persona-visible record maps it. Rubric note added |
| P2-DR3 | P2 | (card rule 3 "his reply to it") | Blake's reply in its own thread `…/1844695547248825769` with In-Reply-To the store builds mail | §3 | Thread metadata | REJECTED | Fork AC, settled and carried: card rule 3, the opening line "Two things I left out of the mail this morning.", the header; both mails INBOX for Julia. Rows byte-identical to revision 42 |
| P2-DR4 | P2 | (decoy card) | SQL action `683dbef4…` board name "Product Roadmap" vs base "DD Product Roadmap" | §6.8 | Label | REJECTED | Base Trello actions on that board use the same "Product Roadmap" label; decoy card only. Carried ruling |
| P4-DR1 | P4 | "then reply to leonard in the dm with what he asked for." | prompt text | §3 search hits / §6.6 | Command List | REJECTED | §6.6 fails a "first / then / finally" list; this is one lowercase "then" with no list, ordering the reply after filing as Leonard's own "reply here when it''s in the folder" requires. Same ruling as earlier rounds |
| P4-DR2 | P4 | "go with your read on the details, no need to check with me first" | prompt text | §3 search hits | Command List | REJECTED | "first" here means "before acting", not a step marker |

P3 notes outside its topic (Blake's reply thread id, PR #401 `ev_7` with no base `ev_6`, PR #265 `rev_8` earlier than `rev_7`) are on rows byte-identical to revision 42, which `0_injection.md` already reviewed. None changes a graded value.

Effect on verdict: unchanged. The one confirmed fork (AJ) is excluded by quoted persona-visible records, the record was re-saved with it, and every score stays at 5. P1's independent answer matches this review: 24 tickets (16 / 4 / 1 / 3), 9 comments, the same shares and DM reply, and Robert's three columns with blanks on ZOM-202, 280, 293.

Fork list:
- F-AH: settled | Robert's three columns (assignee, done day, priority) | The notes doc's "three things for the register" instead | Settled by: card rule 2 "the three things Robert asked for when I asked him in our group chat"; group DM `cec246a6…` "robert anything you want on julia''s difficulty list for monday?" and `abe096ff…` "yeah three things after status please."
- F-AF: settled | Columns included | Columns left out | Settled by: card rule 2; Robert "who it''s assigned to in linear, the day it got marked done (leave it blank if it never got done), and its linear priority."
- F-AI: settled | ZOM-280 done day blank | Cancel day 2025-06-20 | Settled by: "(leave it blank if it never got done)"; Linear `/issues/3333` `"canceled_at": "2025-06-20T23:38:27Z", "completed_at": null`
- F-AJ: settled | ZOM-199 Live | ZOM-199 Not shipped | Settled by: card rule 1 "open, cancelled and never-merged ones are in, as Not shipped"; Blake "everything difficulty related was merged long before that."; rule 6 "comment on that ticket with what the build does"
- F-AG: not material | Columns straight after Status | After the replaced-by column | Same cells; both "after status"; the rubric must accept either
- F-done-day TZ: not a fork | UTC day (ZOM-200 06-13; ZOM-274, 282 06-21) | Pacific day (06-12; 06-20) | One instant each; ENVIRONMENT.md "If the Pacific date and the UTC date are different, accept either."
- F-priority: not a fork | 1–4 | Urgent/High/Medium/Low | Same value
- F-assignee token: platform | "EMPLOYEE_0032_NAME" on ZOM-246, 254, 263, 274, 280, 281 | A real name | Correct as shown (deep_recheck anonymized tokens)
- F-AC, F-AB, F-AD, F-AE, F-Q/K, F-R, F-Y, F-Z, F-AA, F-N, F-L, F-J, F-U, F-E, F-M, F-V, F-W, F-O/P, F-B/G, F-C, F-S, F-T, F-H/I, F-X, F-DMform: unchanged from last round, settled by the same quoted records on byte-identical rows (see the Unique Ground Truth comparison above). P1 re-derived F1–F14 independently and reached the same settlements.

Platform defects: PLATFORM:anonymized-token (Linear `usr_EMPLOYEE_0032`), not scored.

### FINAL VERDICT: PASS

Score: 5

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Next action: Send /hardness, then /oe and /rubric, in that order (the SQL changed, so those passes are outdated). Bring the OEs and rubric to this round's SQL: Robert's three columns and their acceptance notes (Recommended Improvement 1).

Evidence limits: The Evals/Docs PDFs were not re-extracted; Eval 1's restated bands and overrides were applied. Runtime acceptance of the `commenter` and `reader` share roles and how `linear_get_issue` renders assignee, completed_at and priority are unverified (catalog lists parameters only). Eval 0 checks were reused from the same-hash 0_injection.md, because this portal never writes the gate manifest; lint was re-run here (0 flags). Byte-identical SQL rows reuse prior /prompt facts under stage-evidence-v1. The schema snapshot is unverified (G1).

**Lowest Dimension:** None below 5. Every scored dimension is 5 (Originality N/A, no samples).

**Summary:** The prompt is unchanged, and the new SQL keeps a single answer. That answer is 24 tickets (Live 16, Editor only 4, Replaced 1, Not shipped 3), 9 comments, the same shares and the same DM reply, plus Robert's three columns (assignee, done day, priority) that card rule 2 points to. Julia is in the group DM where Robert asks for them. The notes doc's separate "three things" list is a different source, and the blind recheck's ZOM-199 alternative is excluded by card rules 1 and 6.

Eval version: task-quality-v1

Eval release SHA-256: 0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e

Reviewed prompt SHA-256: 22f26066688cedbe94c9c8abfcdd34194db335667d7a195fc499d4d87ede1787

Review context SHA-256: d9724d9c4730ae72a803045c4d4d4d17b8672fe52d70eb848ef470468207dde1

Prompt record SHA-256: 7a83628e0a121ecad615e411177b42c0180e9f1d397a339961c8615c1ab7ef22
