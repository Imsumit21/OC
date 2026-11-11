## PROMPT EVALUATION REPORT

### Task: Julia hands over Leonard's keep-or-hold audience read on the Zombie Match friend sessions (register, memo, ticket close-out, thread reply, note to Brian)
### Assigned Persona: Julia Lawson - Product Manager
### Assigned Business Function: Product
### Assigned Competency: Marketing and GTM
### Assigned Task Skill: Analysis and synthesis
### Assigned Horizon: long-horizon

Binding hashes are in the verdict block.
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Inputs: prompt `Evals/task_inputs/04_Prompt.txt` (saved rev 7, sha 729d3623…, unchanged), assignment `00_Task_Assigned_Inputs.md`, SQL `01_Universe_Inject.sql` task SQL rev7 (sha 16f9657c…, 714 lines). Rev7 follows the portal /prompt FAIL (ground-truth and clarity scores of 2) and makes three edits: (a) a new Leonard post `676eb4bb7c6fde75e63edf27ad453971` in #zombie-design (2025-09-25T16:42:18Z, lines 698–699) saying "friends" in the feedback note means people you know, with family, neighbours and old classmates counting the same; (b) Leonard's 1943 reply `d7122186…` (L701) now also says 0.3.127 (127), 0.3.38 and 0.3.40 all went through the store; (c) ages moved off the band edges (ZOM-600 25→26; ZOM-582, ZOM-610 / Claire-04 and ZOM-626 45→44). Lines after 697 moved by +2: the 1943 reply is L701, Robert's re-run DM L703, Robert's retention rule L705 and Leonard's ask L707. Friction: none (`03_Error_Async_Config.txt`, all fields empty, so it was not loaded as an input). There are no reference files. `02_Reference_Files/` holds only a README.

---

### Injection Gate
- State: CURRENT (`hg_injection_gate.py`).
- Reviewed SQL sha256: 16f9657c587a0b1e8821585cb0288a64e071594d84eea875e5e6a8d7269df68e. Eval 0 verdict: PASS / COMPLETE (`reports/0_injection.md`, injection-static-v2, report sha `b7ea02825da56db7f8b487a8f2b0777559528f29fba37f3b8b35a86290490bff`, run on the rev7 SQL). Its Check C records `time_order_check.py` Part 1 PASS and all 30 Part 2 pointers dispositioned.
- Eval 0 findings on records this prompt depends on: none open. The `seq`/`sequence`/`notes` column advisories are schema-snapshot items confirmed in the live export and change no graded value. The comment on line 1 is harmless.

### Evidence reuse (stage-evidence-v1)
- REUSED from the rev6 `1_prompt.md` (report sha256 `ddc4e3d37f821eef8b1a5d18982b8a5fdd09d3269ff2b4591dc012e9aeb93a33`): the Phase 1 and 4 findings that do not depend on the edited lines, the requirement ledger and premises PR1–PR12. Dependencies verified unchanged: prompt `729d3623…`, assignment, clock and Eval 1. The SQL changed, so every line-bound citation was rebound to the rev7 lines.
- NEW: the UGT comparison (reading F added and EXCLUDED by S_REL; the old age-edge reading E removed because no session sits on a band edge), the portal reconciliation, a fresh Phase 3 Cross-Service Coherence sweep that covers the new post, the record rebound to the rehashed release `3d51ac28…` and context `76a40fec…`, and four fresh blind deep-recheck passes.

### Portal reconciliation

| # | Portal item | Status | Fix / note |
|---|---|---|---|
| 1 | FAIL finding, Reading K (relation): nothing settled the feedback note's "gamer friends" against the notes-doc relations family / neighbor / classmate. Dropping the 9 counted non-friends leaves 4 casual v 4 RPG, under the 6 minimum, so the call flips to keep (ground-truth and clarity scores of 2). | FIXED by (a) | Leonard's post `676eb4bb…` (L699): "on the feedback note: friends just means people you know. family, neighbours and old classmates count the same, as long as they’re in the 25–45 band and don’t work in games. that goes for sessions already run too". Now reading F, EXCLUDED by S_REL. |
| 2 | Advisory: age endpoints (25 and 45). | FIXED by (c) | ZOM-600 is 26; ZOM-582, ZOM-610 / Claire-04 and ZOM-626 are 44. No session sits on a band edge, so the old reading E is gone. |
| 3 | Advisory: placement of the re-run note (ticket vs Register reason). | Rejected by the portal too | Robert's L703 and Leonard's L707 put it on the ticket (see P1-DR1). Kept as a rubric note. |
| 4 | Note: FD-3785 (2025-09-15 week D14 cells filled early). | PLATFORM, not scored | Robert's "cohorts that have a D14 figure" (L705) settles 9.09. |
| 5 | Earlier portal Coherence 3: the Sep 24 gate doc pointed at PR #476, which opened Sep 30. | Still fixed (rev6) | The dated "Update Sep 30" line and modified_time 2025-09-30T19:21:44Z remain in rev7. |

Local process failure: on 2026-11-08 17:12 the local P1 pass raised the relation fork, and the main session rejected it by citing collective labels (Leonard's "the friend sessions are in your workbook now" and the "Friend session: …" ticket titles), which do not settle what the note's "gamer friends" condition admits. The portal then failed the prompt on that fork. The rule that a collective label does not settle a per-session condition is now in the /prompt skill and in learnings §61.

### Phase 1: Prompt Structure & Persona

**Persona:** PASS (5). Julia (roster `julia_lawson`, PM, Product) hands over a request Leonard addressed to her (`<@EMPLOYEE_0005_SLACK_ID>`, SQL L707). She owns the workbook, the criteria deck, the log note and the tickets. Her voice is a short informal Slack-style handoff.

**Assigned Competency:** PASS (5). The task is an audience read: which player segment, casual or RPG, the evidence favours. It draws on friend sessions, a Playtestcloud panel and D7 retention, and the call decides whether the funnel change stays. Choosing the target audience is defensible market and GTM work. Risk note: a reviewer could read the keep-or-hold and tutorial-order decision as Product Management. The competency rests on the audience-segment analysis being the core of the work.

**Assigned Task Skill:** PASS (5). The work is Analysis and synthesis: it applies 6 rules from 5 sources to 60 sessions, then computes per-audience means, the gap and the minimum count.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. PASS.
- Data seeding: PASS. The prompt is 7 sentences and the rules live in Slack, Docs, Slides, Gmail, Linear, GitHub, Trello and Snowflake.
- Dynamic change: Vincent's ZOM-567 "covers the device gate" is followed by Arthur's rc_27 "no phone in the loop". The observer forms' "no coaching" is followed by Claire's mail. Brian's form label is followed by the Kadıköy DM. The note's "gamer friends" is followed by Leonard's Sep 25 relation post. The KPI-tab mean is replaced by Robert's retention rule.

**Naturalness:** PASS. Rev 7 removed the earlier `then` search hit. The prompt has no headings, bullets or polished connectives. The lowercase typing reads natural, not planted.

**Anti-Patterns:**
| Pattern | Status |
|---|---|
| Command List | PASS: deliverables are a comma list with no first/then/finally (rev 7) |
| Bolt-On | PASS: every sentence feeds one ask |
| Pre-Solving | PASS: no exclusion, cause, count or call is named |
| Tool Mention | PASS: none |

Diversity: 5 write types across Sheets, Docs/Drive, Linear (state plus comment), Slack thread and Slack channel. This is not the "investigate + post one Slack message" pattern.

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** PASS (5)

Portal Reading K and its fix: the portal's FAIL rested on the relation fork (Reading K). Rev7 adds Leonard's post `676eb4bb…` (L699), which says family, neighbours and old classmates count the same as friends, including sessions already run. That reading is now F below and is EXCLUDED by S_REL, so the call stays hold. The age-edge reading is gone because rev7 moves every age off the 25/45 bounds.

### Unique Ground Truth comparison

Unique Ground Truth: PASS 5

Basis: The deciding rules are all persona-visible and incorporated through Leonard's message; the three call-flipping alternatives (Samsung pass, coached sessions, dropping family/neighbor/classmate sessions as not 'gamer friends') are excluded by quoted records, and the retention edge is settled by Robert's explicit definition.

Alternative selection: B, C and F are the single-rule changes that flip the call (B and C are each backed by a visible decoy: the Done ticket and Vincent's comment; the clean coaching line on the forms and the label rule; F reads the note's 'gamer friends' against the notes-doc relation field and is settled by Leonard's Sep 25 post). D is the only open edge in a memo figure. The age-boundary edge no longer exists (counted ages run 26 to 44, strictly inside 25–45), and the build-1943 and industry edges were computed and do not change any write or the call.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Apply the note's conditions, Leonard's posted rules, the gate doc and Arthur's PR note: 43 sessions not counted (9 game-industry, 13 coached, 10 dev build 1943, 11 Samsung without an on-device pass); 17 counted. | Casual lead (counted casual mean 3.833 over 9 vs RPG 3.375 over 8; gap 0.458 &gt;= 0.25, both &gt;= 6) so HOLD the cards earlier change | Fill the Register tab (60 rows); create the memo Doc; set 60 tickets Done/Canceled with re-run notes on the technical drops; post a thread reply to Leonard; post to Brian in \#zombie-design | Register tab of ZM audience sessions; Julia's Drive folder d\_8140f09bf9f1b94cb8ee2d; ZOM-568..ZOM-627; Leonard's thread in \#zombie-design; \#zombie-design to Brian | Register: 17 counted / 43 not counted with reasons; 17 Done, 43 Canceled, re-run notes on 21 technical drops; memo with the casual call, counts and means, panel 3.33 and retention 9.09 as context; reply 'hold'; Brian told the tutorial and level order work does not go on | S\_GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device. A closed ticket isn''t a pass."; S\_CRIT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 280-280): "The lead is the higher mean star rating over counted sessions." |
| B | Treat ZOM-567 (Done) and Vincent's comment that Vision Bot run \#15 covers the device gate as the Samsung pass, so the 11 Samsung casual sessions count. | RPG lead (casual mean 3.025 over 20 vs RPG 3.375 over 8) so KEEP the change | Fill the Register tab (60 rows); create the memo Doc; set 60 tickets Done/Canceled with re-run notes on the technical drops; post a thread reply to Leonard; post to Brian in \#zombie-design | Register tab of ZM audience sessions; Julia's Drive folder d\_8140f09bf9f1b94cb8ee2d; ZOM-568..ZOM-627; Leonard's thread in \#zombie-design; \#zombie-design to Brian | Register: 28 counted / 32 not counted; 28 Done, 32 Canceled; memo with RPG call; reply 'keep'; Brian told the work goes on | S\_VINCENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 552-552): "Vision Bot run \#15 is green too, so that run covers the device gate for the Samsung group" |
| C | Count Claire's 13 coached RPG sessions because their forms say no coaching and the criteria deck says the observer's label stands. | RPG lead (RPG mean 4.167 over 21 vs casual 3.833 over 9) so KEEP the change | Fill the Register tab (60 rows); create the memo Doc; set 60 tickets Done/Canceled with re-run notes on the technical drops; post a thread reply to Leonard; post to Brian in \#zombie-design | Register tab of ZM audience sessions; Julia's Drive folder d\_8140f09bf9f1b94cb8ee2d; ZOM-568..ZOM-627; Leonard's thread in \#zombie-design; \#zombie-design to Brian | Register: 30 counted / 30 not counted; memo with RPG call; reply 'keep'; Brian told the work goes on | S\_LABEL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 276-276): "The observer''s label stands, nothing gets re-derived." |
| D | Quote retention only over cohorts whose 14-day window had fully closed by the clock, dropping the 2025-09-15 week: install-weighted D7 9.05 instead of 9.09. | Casual lead (counted casual mean 3.833 over 9 vs RPG 3.375 over 8; gap 0.458 &gt;= 0.25, both &gt;= 6) so HOLD the cards earlier change | Fill the Register tab (60 rows); create the memo Doc; set 60 tickets Done/Canceled with re-run notes on the technical drops; post a thread reply to Leonard; post to Brian in \#zombie-design | Register tab of ZM audience sessions; Julia's Drive folder d\_8140f09bf9f1b94cb8ee2d; ZOM-568..ZOM-627; Leonard's thread in \#zombie-design; \#zombie-design to Brian | Same as A except the memo's retention context reads 9.05 (45 mature rows) instead of 9.09 (47 rows) | S\_ASK5 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 707-707): "plus retention the way Robert set it in the channel after Vincent''s post" |
| F | Apply the note's 'gamer friends' to the relation field: family, neighbor and classmate sessions are not counted. Drops ZOM-589, 597, 599, 600, 605, 623, 625, 626, 627, leaving 4 casual / 4 RPG, under the 6 minimum, so no clear lead → KEEP; 8 Done, 52 Canceled. | No clear lead (4 casual / 4 RPG counted, under the 6-per-audience minimum) so KEEP the change | Fill the Register tab (60 rows); create the memo Doc; set 60 tickets Done/Canceled with re-run notes on the technical drops; post a thread reply to Leonard; post to Brian in \#zombie-design | Register tab of ZM audience sessions; Julia's Drive folder d\_8140f09bf9f1b94cb8ee2d; ZOM-568..ZOM-627; Leonard's thread in \#zombie-design; \#zombie-design to Brian | Register: 8 counted / 52 not counted; 8 Done, 52 Canceled; the 9 family/neighbor/classmate sessions not counted and closed without a re-run note; memo with no-clear-lead call; reply 'keep'; Brian told the work goes on | S\_NOTE\_AGE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "get real-life feedback from 25–45 casual and/or RPG gamer friends (not kids)" |

Explicit option inventory: The prompt names one explicit option pair for the reply: keep or hold.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "reply to him in his thread with keep or hold"

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| hold | RETAINED | A, D | The counted sessions give a casual lead, which Leonard maps to hold. Evidence: P (Evals/task\_inputs/04\_Prompt.txt): "keep or hold" |
| keep | EXCLUDED | B, C, F | Keep arises only by counting the Samsung or coached sessions, or by dropping the family/neighbor/classmate sessions; all three are excluded by persona-visible records. Evidence: P (Evals/task\_inputs/04\_Prompt.txt): "keep or hold" |

Compared alternative: B
Resolution: EXCLUDED. The gate doc Leonard posted after his note says a pass covers a device only if it ran on that device and a closed ticket is not a pass, and defers pass scope to Arthur's PR; Arthur's later inline note says the job runs in editor play mode with no phone. Vincent's own comment says no Samsung phone was used. No on-device pass exists, so the Samsung sessions do not count.
Resolution evidence: S\_GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device. A closed ticket isn''t a pass."; S\_RC27 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "the pass comes from Unity editor play mode on the Jenkins machine, no phone in the loop"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Keep versus hold. |
| writes | SAME | Same set of write actions. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Register verdicts, ticket states, memo call and reply differ. |

Authority chain: P → S\_ASK → S\_ASK2 → S\_GATEPOST → S\_GATE

Resolution relevance challenge: The gate doc's rule decides whether a green run is a pass for the Samsung group, which is exactly the difference between A and B.
Delegation challenge: NOT_CLAIMED. No alternative call is accepted; the rule excludes B.
Challenge evidence: S\_GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A Samsung session counts once we have a clean pass covering that device."

Compared alternative: C
Resolution: EXCLUDED. The sessions are defined by Leonard's note, which asks for no coaching and honest reactions; Leonard treats the note's conditions as counting rules ('One more for the feedback note: game-industry people don't count'), and Claire's mail to Julia says she coached the group before they played and that this is not what Leonard asked for. The deck's label rule governs the audience label, not whether a session counts.
Resolution evidence: S\_NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "No coaching, just observe and collect honest reactions."; S\_CLAIRE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 424-424): "Before anyone touched their phone I sat them all down and took them through how ZM plays"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Keep versus hold. |
| writes | SAME | Same set of write actions. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Register verdicts, ticket states, memo call and reply differ. |

Authority chain: P → S\_NOTE

Resolution relevance challenge: The note's no-coaching condition and Claire's admission decide whether the 13 coached sessions are part of the read, which is the A/C difference.
Delegation challenge: NOT_CLAIMED. No alternative call is accepted.
Challenge evidence: S\_IND (Evals/task\_inputs/01\_Universe\_Inject.sql lines 697-697): "One more for the feedback note: game-industry people don’t count, and that goes for sessions already run too"; S\_CLAIRE2 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 424-424): "I know that''s not what Leonard asked for"

Compared alternative: D
Resolution: EXCLUDED. Robert defines mature cohorts explicitly as the cohorts that have a D14 figure, which includes the 2025-09-15 week rows; the incorporated rule picks 47 rows and 9.09.
Resolution evidence: S\_RET (Evals/task\_inputs/01\_Universe\_Inject.sql lines 705-705): "Mature cohorts only, meaning cohorts that have a D14 figure, both platforms pooled."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Both hold. |
| writes | SAME | Same writes. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Memo retention figure 9.09 versus 9.05. |

Authority chain: P → S\_ASK5 → S\_RET

Resolution relevance challenge: Robert's own definition of 'mature' decides which cohort rows enter the weighted D7, which is the only A/D difference.
Delegation challenge: NOT_CLAIMED. No alternative figure is accepted; the definition settles it.
Challenge evidence: S\_RET (Evals/task\_inputs/01\_Universe\_Inject.sql lines 705-705): "Mature cohorts only, meaning cohorts that have a D14 figure, both platforms pooled."

Compared alternative: F
Resolution: EXCLUDED. Leonard settles what 'friends' in his note means: people you know, with family, neighbours and old classmates counting the same as long as they are in the 25–45 band and do not work in games, including sessions already run. The relation field therefore does not drop any session, and the 9 family/neighbor/classmate sessions stay counted as in A.
Resolution evidence: S\_REL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "family, neighbours and old classmates count the same"; S\_NOTE\_AGE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "get real-life feedback from 25–45 casual and/or RPG gamer friends (not kids)"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Keep versus hold. |
| writes | SAME | Same set of write actions. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Nine register verdicts and ticket states, the memo call and the reply differ. |

Authority chain: P → S\_ASK → S\_ASK2 → S\_REL

Resolution relevance challenge: Leonard's clarification of the note's 'friends' decides whether the relation field removes sessions, which is the whole A/F difference.
Delegation challenge: NOT_CLAIMED. No alternative call is accepted; Leonard's post excludes F.
Challenge evidence: S\_REL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "family, neighbours and old classmates count the same"

Strongest-alternative challenge (B): B rests on the newest visible claim in the ticket system (ZOM-567 closed Done with an explicit statement that run \#15 covers the Samsung group) and flips the call; it is not a strawman.
Challenge evidence: S\_VINCENT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 552-552): "Vision Bot run \#15 is green too, so that run covers the device gate for the Samsung group"

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

**Computed end state (Reading A, independently reproduced by P1):**
- Not counted, 43 sessions:
  - 9 game-industry: Brian's, Kadıköy (L691, L697).
  - 13 coached: Claire's (L424 and the note).
  - 10 on dev build 1943: Robert's (L701, gate doc).
  - 11 Samsung with no on-device pass (gate doc, rc_27).
- The 9 family, neighbor and classmate sessions stay in scope (L699). Builds 0.3.127 (127), 0.3.38 and 0.3.40 are store builds (L701). No counted age sits on a band edge.
- Counted, 17 sessions: casual 9, mean 3.833; RPG 8, mean 3.375. The gap is 0.458, so this is a casual lead (deck slide 3) and the call is **hold** (L707).
- Tickets: 17 go to Done and 43 to Canceled (log note). Re-run notes go on the 21 build and device drops (Robert's DM L703).
- Memo context: panel 3.33 (9 rated players, 1 void, L695) and D7 9.09% (47 rows, Robert's rule L705). The memo goes in Julia's folder `d_8140f09bf9f1b94cb8ee2d` (card L679).
- Brian is told the tutorial and level order work does not go on.

**Feasibility:** PASS (5). Each write maps to a catalog tool:
- `gsheets_values_update` for the Register tab.
- `gdocs_create_document` (`driveFileId`) or `gdrive_move_file` for the memo in the folder.
- `linear_update_issue` (state) and `linear_create_comment` for the tickets. Team ZOM has Done and Canceled states, and all 60 tickets are in Todo.
- `slack_send_message` with `thread_ts` for the reply to Leonard, and without it for Brian.

There is no per-X breakdown beyond audience, which the field carries. Means are computed from integer and half-star values. Retention is computed from tool-visible `installs` and `d7_ret`.

**Persona ACL Reachability:** PASS (5). The scoped services are Gmail, Slack, GCal and the Drive family (acl.md matrix). Julia can reach every deciding record:
- She is a member of C090N54TG79 #zombie-design (including the new L699 post), DM D05GU6L0XFH (Robert), DM D076RBM29JS (Brian) and C08R27X0EAH (channels.json).
- Every injected Doc, Sheet and Slides file is owned by her or shared with her.
- Claire's mail and the panel forward are in her mailbox.
- GitHub, Linear, Trello and Snowflake are unscoped.
- No ask directs her to read anything outside her view. The only record she can't see is #executives, and nothing needs it.

**Explicit Tool Mention:** PASS (5).

**Clarity & Specificity:** PASS (5). The destinations are named: the register tab, my drive folder, his thread, and #zombie-design to Brian. "In his thread" and "in #zombie-design" are written as two separate places. Delegation is explicit ("you don't need my ok on any of it"). The portal's Clarity 2 came from the relation fork, which L699 now settles.

**Contrived / Unnatural:** PASS (5). Rev 7 removed the only step-list hit. A case-insensitive search for `First`/`Then`/`Finally`/`tool`/`MCP`/tool-name prefixes returns nothing (fresh P4 pass). There are no opaque ids, timestamps, riddles, hidden destinations, audit wording or if-chains.

**Alignment with Today's Date:** PASS (5). The prompt uses no dates. Nothing it treats as done is after 2025-09-30 23:59:59 PT. The latest seed is L707, at 2025-09-30T21:10:27Z.

**Originality:** N/A. No samples were supplied.

**Truthfulness:** PASS (5). All 12 premises (PR1–PR12) are verified in the record. The fresh P3 pass checked 14 premises and found none false.

**Tool Use & Cross-service:** PASS (5). Each of these changes a graded fact:
- Slack: the rules, the relation post, the industry DM, the 1943 build and store builds, Robert's re-run rule and the retention rule.
- Gmail: Claire's coaching mail and the panel.
- GitHub: rc_27 settles the Samsung group.
- Drive/Slides/Docs: the lead rule, the gate and the close-out mapping.
- Linear, Sheets and Snowflake: the tickets, the register and retention.

**Investigation + Action:** PASS (5). All five writes depend on the computed read.

**Coherence (Bolt-on):** PASS (5).

**Business Function:** PASS (5). The work is Product: a decision on the Zombie Match 3D funnel change.

---

### Phase 3: Universe Feasibility

**Data Existence:**
- Entities verified: 12 of 12 premises, plus the 60 session rows. The Log tab matches all 60 tickets and notes docs on audience, stars and date.
- All retrievable via the catalog tools: yes.

**Cross-Service Coherence:** PASS (5).
- Pointer time-order sweep (fresh, main session; all times UTC). Every pointer lands on a target that already existed, all OK:
  - The gate doc's last edit (2025-09-30T19:21:44Z) points to PR #476 "Vision bot", created 18:54:32Z.
  - The gate doc's creation (Sep 24 15:12:40Z) comes before Leonard's share at L693 (15:40:11Z).
  - The log note (created 16:24:03Z, edited 16:35:20Z) points to the workbook, created 16:21:47Z, and to the observer notes docs from Sep 23–29.
  - Vincent's ZOM-567 comment (Sep 30 16:50:22Z) points to Jenkins "Match 3D Vision Bot - #15", which succeeded Sep 25 12:31:15Z.
  - The Trello card (created 16:52:31Z) points to the log note.
  - L683/L687 (Sep 22 15:00Z/15:30Z) point to Leonard's note /537 (Sep 22 05:01:26Z).
  - The L695 panel rule (Sep 24 16:05Z) answers Robert's "what's the audience you requested" (Sep 24 05:23:17Z).
  - Leonard's new relation post at L699 (Sep 25 16:42:18Z) points to the feedback note /537 (2025-09-22T05:01:26Z) and to the game-industry rule at L697 (Sep 24 17:00Z), both earlier.
  - Robert's retention rule at L705 (Sep 29 17:30:08Z) follows Vincent's post /730 (Sep 29 17:03:34Z).
  - Leonard's ask at L707 (Sep 30 21:10:27Z) points to "cards earlier change from Monday" (Robert /731, Mon Sep 29 18:52:37Z), the deck (Sep 24 17:02Z), Robert's DM rule (Sep 26 19:04Z), the panel forward (Sep 22 09:14Z) and the roadmap card.
  - Every build exists before its sessions: #1943 succeeded Sep 22 21:12:37Z (sessions from Sep 23); 0.3.127 was published Sep 22 21:04Z (sessions from Sep 23); 0.3.40 was a required version from Sep 23 16:02Z (sessions from Sep 24); 0.3.38 was in use from Sep 17 (sessions Sep 22).
  - The rest are not pointers: in-game "card/deck/board" wording, and generic "the ticket"/"the form".
- Blind P2 sweep: 359 pointers checked, 359 OK, 0 FORWARD, 67 not-a-pointer.
- Inconsistencies in task-touched data: none scored. The retention table has two rows for the 2025-09-15 week with a D14 value before that window closes. This is PLATFORM:FD-3785, recorded and not scored, and Robert's explicit "cohorts that have a D14 figure" (L705) settles which rows count.
- Injection SQL considered: yes.
- Static integrity evidence: REUSED from `0_injection.md` (injection-static-v2 PASS / COMPLETE on sha 16f9657c…), Checks A–C.
- Prompt-specific sources, access and configuration: supported. Friction is none.

---

### Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score | Justification |
|---|---|---|---|
| Prompt | Unique Ground Truth | 5 | Generated comparison above. B, C, D and F are excluded by quoted persona-visible records; the portal's relation fork is settled by L699. |
| Prompt | Feasibility | 5 | All writes are cataloged and all data exists. |
| Prompt | Persona ACL Reachability | 5 | Julia can open every deciding record. |
| Prompt | Explicit Tool Mention | 5 | None. |
| Prompt | Clarity & Specificity | 5 | Destinations are named and delegation is explicit; the relation fork is settled. |
| Prompt | Contrived / Unnatural | 5 | No step-list or tool wording after the rev 7 fix. |
| Prompt | Alignment with Today's Date | 5 | No temporal conflict. |
| Prompt | Originality / Sample Similarity | N/A | No samples. |
| Prompt | Truthfulness | 5 | 12 of 12 premises verified; P3 found none of 14 false. |
| Prompt | Tool Use & Cross-service | 5 | At least 7 services change graded facts. |
| Prompt | Investigation + Action | 5 | The read feeds all five writes. |
| Prompt | Coherence (Bolt-on) | 5 | No bolt-on. |
| Prompt | Persona | 5 | Fits a PM handover. |
| Prompt | Business Function | 5 | Product. |
| Prompt | Assigned Competency | 5 | Audience-segment GTM read (see the risk note). |
| Prompt | Assigned Task Skill | 5 | Analysis and synthesis. |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three dimensions, and a short trigger. |
| Universe | Data Exists | 5 | Verified. |
| Universe | Cross-Service Coherence | 5 | The gate-doc fix (rev6) holds and the time-order sweep, including the new L699 post, is clean. FD-3785 is platform. |

### Issues Found

| # | Issue | Severity | Dimension |
|---|---|---|---|
| 1 | (Fixed in rev6) The Sep 24 gate doc pointed at PR #476, which opened Sep 30. | Was Minor (Coherence 3, portal); now resolved | Cross-Service Coherence |
| 2 | (Fixed in rev7) Nothing settled the note's "gamer friends" against the notes-doc relations family / neighbor / classmate; dropping the 9 gives 4 v 4 and flips the call to keep. Leonard's post `676eb4bb…` (L699) now settles it. | Was FAIL (ground-truth and clarity scores of 2, portal Reading K); now resolved | Unique Ground Truth, Clarity & Specificity |
| 3 | (Fixed in rev7) Sessions at ages 25 and 45 sat on the band edges. Ages are now 26 and 44. | Was Advisory (portal); now resolved | Unique Ground Truth |
| 4 | The competency fit depends on reading the audience call as GTM work rather than a roadmap decision. | Advisory (not scored) | Assigned Competency |

### Recommended Improvements

None required. For later stages:
- Rubric notes:
  - Grade the re-run notes on the 21 dropped tickets (L703, log note, L707), not only a Register reason.
  - Accept retention 9.09 (or 9.1). The 8.63 KPI simple mean is the decoy, and 9.05 is the FD-3785 variant.
  - Do not grade the Trello card: "update everything" does not require editing it.
  - Grade Brian's message by recipient and channel C090N54TG79, whether or not it is in the thread.
- Next action: /hardness, then /oe and /rubric on rev7. Earlier runs on rev6 are stale.

---

## Deep Recheck

Passes: P1, P2, P3, P4 on the rev 7 prompt with the rev7 SQL (sha 16f9657c…). Each was a fresh Opus 5.5 (claude-opus-5-5) subagent at session effort, launched in parallel after the record save. Each got only the saved inputs under `Evals/task_inputs/` (not `reports/`), the persona folder, `common_errors.md`, `deep_recheck.md` and `SEARCH.md`, and none saw the main review, the record, earlier reports, the portal output or `Task_Authoring/`. P1 ran a clause sweep of every session attribute against every session. P2 was told to check every record-to-target pointer in time order.

| Pass | Scope | Result |
|---|---|---|
| P1 | 8 sentences, clause sweep of 7 attributes × 60 sessions, 13 forks, end state reproduced (hold; casual 3.833/9 vs RPG 3.375/8; 17 Done, 43 Canceled, 21 re-run notes) | 1 finding, 0 confirmed |
| P2 | 11 sentences, pointer sweep | 1 finding, platform |
| P3 | 14 premises, SQL integrity | 1 CHECK, 0 confirmed |
| P4 | 7 sentences | 1 advisory, 0 confirmed |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| P1-DR1 | P1 | "close out the tickets" | Robert, L703: "put a re-run note on it so the observer runs it again. Dropped for anything else, no re-run, it just gets closed"; log note: "counted goes to Done, not counted goes to Canceled"; Leonard, L707: "close the tickets the way your log note says. Robert already told you how not-counted sessions get handled" | §2 destination (re-run note) | Clarity & Specificity | REJECTED | What "just gets closed" is the ticket, as the log note's Done/Canceled mapping shows, so the re-run note goes on the ticket. L707 sends the close-out to the log note and to Robert's handling of not-counted sessions. The portal rejected the same point. Kept as a rubric note. |
| P2-DR1 | P2 | "write the memo he asked for and put it in my drive folder" | USER_COHORT_RETENTION zombie_match_3d 2025-09-15 D14 cells filled before the window closes; Robert, L705: "Mature cohorts only, meaning cohorts that have a D14 figure, both platforms pooled." | §3 derived columns | PLATFORM:FD-3785 | REJECTED (platform) | Retention is 9.09 with the rows and 9.05 without them, and the call does not change either way. Robert's "cohorts that have a D14 figure" settles 9.09 (reading D stays EXCLUDED). Not scored. |
| P3-DR1 | P3 | — | `github_review_comments.seq` column in the INSERT column list | SQL integrity | Data integrity (CHECK) | REJECTED | Eval 0 resolved the column as present in the live export, and the portal accepted the same SQL. |
| P4-DR1 | P4 | "reply to him in his thread with keep or hold" | Leonard, L707: "no clear lead, we keep it" | §1 option set ("not a maybe") | Clarity & Specificity (advisory) | REJECTED | "No clear lead" still maps to keep, so the reply is one of the two named calls either way. |

Effect on verdict: none. Every dimension stays at 5.

Fork list:
- F1: settled | 11 Samsung sessions not counted, with a re-run note | count them per ZOM-567 (keep) | Settled by: gate "A pass covers a device only if it ran on that device. A closed ticket isn't a pass." and rc_27 "no phone in the loop".
- F2: settled | Robert's 10 sessions on 1943 not counted, with a re-run note; 0.3.127 (127), 0.3.38 and 0.3.40 are store builds | count 1943 (keep), or treat the other builds as dev builds | Settled by: `d7122186…` L701 "it never went through a store" and "0.3.127 (127) on android and 0.3.38 / 0.3.40 on ios all went through the store, those are fine".
- F3: settled | Claire's 13 coached sessions not counted | count them (keep) | Settled by: note /537 "No coaching, just observe and collect honest reactions." and L424 "I know that's not what Leonard asked for".
- F4: settled | Brian's 9 Kadıköy sessions not counted | count them (keep) | Settled by: L697 "game-industry people don't count, and that goes for sessions already run too" and L691 "Kadıköy ekibi komple oyun sektöründen".
- F5: settled | family, neighbor and classmate guests count | only "Relation: friend" counts (4 v 4, keep) | Settled by: `676eb4bb…` L699 "friends just means people you know. family, neighbours and old classmates count the same".
- F6: settled | no session sits on an age edge | — | Settled by: L685 "age. 25–45 years old, not a headcount"; the edge ages are now 26 (ZOM-600) and 44 (ZOM-582, ZOM-610, ZOM-626).
- F7: settled | the observer's label is used as-is | re-derive it | Settled by: slide L276 "The observer's label stands, nothing gets re-derived."
- F8: settled | technical drops go to Canceled with the other not-counted sessions | leave them open | Settled by: log note L136 "counted goes to Done, not counted goes to Canceled" and L703 "Dropped for anything else, no re-run, it just gets closed".
- F9: settled | re-run note on the ticket | only in the Register reason | Settled by: L703 "put a re-run note on it so the observer runs it again", referring to a dropped session's ticket, and L707.
- F10: settled | panel 3.33 (void removed) | 3.10 | Settled by: L695 "if a rating is void it comes out of both the sum and the count".
- F11: settled (PLATFORM:FD-3785) | retention 9.09 | 9.05 / 8.63 | Settled by: L705 "Mature cohorts only, meaning cohorts that have a D14 figure" and "not a simple mean of the cohorts".
- F12: settled | session set = the 60 Log rows | add Marcus's duplicate or double-count it | Settled by: L707 "the friend sessions are in your workbook now". Marcus: "Same sessions as before".
- F13: settled | memo in Julia's root folder | the Zombie Art subfolder | Settled by: L679 "memo goes in Julia's folder with her log note".
- F14: settled | Brian gets a channel post | a thread tag | Settled by: L707 "tell <@EMPLOYEE_0026_SLACK_ID> in this channel". Same recipient and write either way.
- F15: settled (rubric note) | "update everything" does not require editing the Trello card | edit the Trello card | Settled by: the five named writes in the prompt and L707; no record asks for a card change.

Platform defects: PLATFORM:FD-3785 (USER_COHORT_RETENTION 2025-09-15 D14, 2025-09-22 D7 and 2025-09-29 D1 cells filled before their windows close; P2-DR1).

### FINAL VERDICT: PASS

Score: 5

Execution status: COMPLETE

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Eval version: task-quality-v1
Eval release SHA-256: 3d51ac2867d2ce85946d4723cd9ad17c6a16d285f36ae548758157568b052b06
Reviewed prompt SHA-256: 729d3623902ef87c67c5350fa319d715a57d65f45aecc62c03c2b0c2fbb053cc
Review context SHA-256: 76a40fec24e51de20657998fc2f967b71aec30cc162bef448d299bf8874cff34
Prompt record SHA-256: a688717fefc9be1710a430ba7c85d13434c77085e0f55a45fe0da953d8c1a734

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: /hardness, then /oe and /rubric on rev7 (SQL sha 16f9657c…). Earlier runs and verifier results on rev6 are stale.

Evidence limits: Static review. The SQL was never executed, and tool rendering is inferred from catalog parameters. The release manifest was rehashed (3d51ac28…) only to record local skill additions (learnings §60 and §61); Eval 1 itself is unchanged. The portal release (b9281224…) still differs, so portal reviewers may apply checks this release lacks. The UGT comparison, portal reconciliation, Phase 3 coherence sweep and the four blind passes are NEW. FD-3785 is recorded as platform and not scored.

**Lowest Dimension:** None. All scored dimensions are 5.

**Summary:** Rev7 fixes the portal's FAIL: Leonard's Sep 25 post settles that family, neighbours and old classmates count as friends, so the relation reading (F) is excluded and the call stays hold. The age edges are gone and the store builds are stated outright. Four fresh blind passes reach the same end state (hold; casual 3.833 over 9 vs RPG 3.375 over 8; 17 Done, 43 Canceled, 21 re-run notes) and confirm no finding, and the pointer sweep, including the new post, finds no forward reference.
