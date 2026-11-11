## PROMPT EVALUATION REPORT

### Task: Julia closes out Leonard's friend-session audience read (60 sessions) and posts the keep/hold call on the cards-earlier change
### Assigned Persona: Julia Lawson - Product Manager (roster key julia_lawson, julia.lawson@harmonygames.co, Product)
### Assigned Business Function: Product
### Assigned Competency: Marketing and GTM
### Assigned Task Skill: Analysis and synthesis
### Assigned Horizon: long-horizon (difficulty mode: medium)


## 1. Scope

- Stage: `/prompt`, chat review, audit mode. Review date: 2026-11-08 (rerun after the SQL revision).
- Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Universe `Universe_SynthCut` (hg4-synth-sep30cut v16), manifest `Evals/references/universes/synthcut/universe_manifest.json`.
- Inputs: `04_Prompt.txt` (724 bytes, SHA-256 `729d3623902ef87c67c5350fa319d715a57d65f45aecc62c03c2b0c2fbb053cc`, attachment to this /prompt message, byte-identical to the previously saved prompt); `00_Task_Assigned_Inputs.md` (platform record, SHA-256 `2bd4116582f3d4c09a83f4bf14d33dd7053f01213242dcb08d84d60fecad1c6d`); `01_Universe_Inject.sql` (258,605 bytes, SHA-256 `49d83af2b21d700d84efa0acecb598ad32ec9ae7ba03d7d160981b7ded9cbb61`). No error/async config, dynamic context or reference files were supplied; none are referenced by the prompt.
- SQL change since the last /prompt review (SQL `5b6e01119505…`): only lines 4 and 134 differ (the "ZM session stability gate" Drive row and Docs row). The Docs body now reads "Arthur Blake owns the Vision Bot job and says what a pass does and doesn't cover." and ends "Update Sep 30: Arthur opened his Vision Bot PR today. What a pass covers gets discussed there."; `modified_time` is 2025-09-30T19:21:44Z on both rows; style run end 992 equals the new body length.
- Calibration samples: none supplied, so Phase 2.9 is N/A.

## 2. Input / authority issues

None. All five assignment fields are on the platform record. The SQL was read as a proposed overlay and never executed. SQL comments and record text were treated as data.

**Evidence reuse (stage-evidence-v1).** Prompt identical; 710 of 712 SQL lines byte-identical; same universe manifest, clock, ACL, catalog and release. Facts from the prior /prompt ledger on unchanged lines are REUSED (prior report SHA-256 recorded in the manifest entry); every source quote in the check record was re-matched against the current SQL lines, and the changed GATE source was re-quoted. Re-verified NEW this run: the gate-doc change and its timing against PR #476 (base GitHub `/pull_requests/2381`, created_at 2025-09-30T18:54:32Z) and Arthur's comment `#476#rc_27` (2025-09-30T20:10:26Z); the ZOM-567 comment author (`usr_65c76e0b87aa7e9b` = vincent.parker, not Arthur); the full 60-session classification recomputed from the SQL (17 counted: casual 9 at 3.833, RPG 8 at 3.375); base Slack has no Arthur statement that a Vision Bot green covers a device (only Jenkins notifications).

### Injection Gate
- State: CURRENT (`hg_injection_gate.py`).
- Reviewed SQL sha256: `49d83af2b21d700d84efa0acecb598ad32ec9ae7ba03d7d160981b7ded9cbb61`. Eval 0 verdict: PASS (injection-static-v2, reviewed 2026-11-08T13:46:23Z).
- Eval 0 findings on records this prompt depends on: none.

### Dataset Similarity
- Library: refreshed 2026-11-08T06:36Z, age 7.2 h, 495 tasks. Gate: PASS. Nearest tier: distinct.
- Nearest neighbours (all below 0.70, no note required): 6adfbc55… (Julia Lawson, friends-session roll-up for the Oct 2 iterate/pivot call, meaning 0.628), 6ad83edd… (0.613), 6abc06a6… (0.608).

## 3. Checklist (STEP 0)

| Item | Status |
|---|---|
| Intake: prompt + five assignment fields | NEW, done (prompt saved; assignment from platform record) |
| STEP 0.5 injection gate | NEW, CURRENT on the revised SQL, Eval 0 PASS reused |
| STEP 0.6 dataset similarity | NEW, distinct |
| Phase 0.1 Docs / catalog | NEW (Prompt Writing, Overall Task Flow, Common Errors, Universe and Tools, Persona ACL, Example Task, UGT guide extracted with pdftotext; catalog.json and tool_outputs.md read) |
| Phase 0.2 universe exploration | REUSED + NEW recompute (all 357 SQL row effects parsed; 60 sessions tabulated; base #zombie-design Sep 2025, #zombie-match3d, #builds, PR #476, ZOM-559, Trello, Snowflake USER_COHORT_RETENTION read) |
| Phase 0.3 calibration | NEW (Example Task: short prompt, rules in the environment) |
| Phases 1.1–1.5, 2.1–2.9, 3.1–3.2, 4 | REUSED for unchanged facts (prior ledger), NEW for the changed gate doc, UGT and Clarity (deep-recheck fork K), coherence and scoring |
| Phase 5 deep recheck | NEW, four fresh blind passes, below |

## 4. Requirement ledger

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Find Leonard's request and its rules | SQL L705 Leonard 2025-09-30 21:10 UTC in #zombie-design | `slack_conversations_search_messages` / `slack_read_channel` C090N54TG79 | slack read tools | Julia is a member of C090N54TG79 (channels.json /132) | Rules list: post-note rules, audience read criteria, log note, Robert's handling, roadmap card, panel, retention |
| Apply the session rules to all 60 sessions | Workbook Log (SQL L260), 60 notes docs (build, age, relation), 60 ticket comments (phone), 15 form mails + Claire's Sep 29 mail, Brian DM, gate doc, Arthur's PR #476 comment, Leonard's age/game-industry/1943 posts | Sheets read, Drive/Docs search by title, Linear `linear_get_issue`/`linear_list_comments`, Gmail search, Slack DMs, GitHub `github_get_pull_request_comments` | gsheets_values_get, gdocs_get_document, linear_list_comments, gmail_search_messages, slack_read_thread, github_get_pull_request_comments | Notes docs all shared with Julia; mails in her inbox; DMs D076RBM29JS and D05GU6L0XFH include her; Linear/GitHub unscoped | 17 counted, 43 not counted (9 game industry, 10 dev build 1943, 13 coached, 11 Samsung without a device pass) |
| Fill the Register tab | Register tab header "Register: one row per session" / ticket, audience, stars, verdict, reason (SQL L262) | Same workbook | gsheets_values_update / gsheets_values_append | Julia owns the workbook | 60 rows with verdict and reason |
| Write the memo and put it in Julia's folder | Trello card "Cards earlier: waiting on the audience read" (SQL L679): "the audience call and the numbers behind it, with the panel and retention as context", "memo goes in Julia's folder with her log note"; log note in d_8140f09bf9f1b94cb8ee2d | trello_get_card / board search; gdrive_get_file_metadata on the log note | gdrive_create_file (parentId) or gdocs_create_document + gdrive_move_file | Trello unscoped; folder owned by Julia | Doc with the casual call, 9 vs 8 counted sessions, means 3.83 vs 3.375, gap 0.46, panel 3.33, retention 9.09% |
| Panel figure | Leonard's forward (SQL L288) and his thread reply (SQL L695): one number per player, void out of sum and count | Gmail, Slack thread c53936d6 | gmail_get_message, slack_read_thread | Julia's mailbox; channel member | (3.5+3+3.5+4+3+3+3.5+3+3.5)/9 = 3.33 |
| Retention figure | Robert's rule (SQL L703); Snowflake ANALYTICS.GAME_EVENTS.USER_COHORT_RETENTION | snowflake_execute_query | snowflake_execute_query | Snowflake unscoped | 47 zombie_match_3d rows with d14_ret, 6,040 installs, Σ(installs×d7)/Σinstalls = 9.09% |
| Close out the 60 session tickets | Log note (SQL L136): "counted goes to Done, not counted goes to Canceled"; Robert DM (SQL L701) re-run note rule | Linear | linear_update_issue (state), linear_create_comment | Linear unscoped; workflow state Canceled exists in team data | 17 Done, 43 Canceled, re-run comments on 21 technical drops |
| Reply to Leonard in his thread | SQL L705 "reply here with keep or hold" | Same message | slack_send_message with thread_ts 1759266627.418203 | Member | "hold" |
| Tell Brian whether the tutorial and level order work goes on | Robert 2025-09-29 18:52 UTC (base /731) and Julia to Brian (base /777, /780) | #zombie-design history | slack_send_message to C090N54TG79 | Brian and Julia are members | The work does not go on (change on hold) |

Counting arithmetic (from the SQL rows): casual counted = ZOM-595 4, 600 4, 602 4, 605 3.5, 621 3.5, 622 3.5, 625 4, 626 4, 627 4 → 34.5/9 = 3.833; RPG counted = ZOM-589 3, 592 3.5, 597 3, 598 3.5, 599 3.5, 604 3.5, 623 3.5, 624 3.5 → 27/8 = 3.375; gap 0.458 ≥ 0.25, both audiences ≥ 6 sessions → casual lead → hold. Each trap flips the call if missed: counting the Samsung sessions gives casual 3.03 vs RPG 3.375 (keep); counting Claire's gives RPG 4.17 (keep); counting Brian's gives RPG 4.15 (keep); counting Robert's gives casual 3.11 vs 3.375 (keep).

## Phase 1: Prompt Structure & Persona

**Persona:** PASS (5)
- Leonard asks Julia directly (SQL L705 @-mentions her); the workbook, criteria deck and log note are hers. A Product Manager closing out player research and posting a keep/hold call fits role, remit and access. Lowercase, quick request voice fits a PM delegating work.

| Check | Finding |
|---|---|
| Role plausibility | Yes: she owns the session log and the criteria deck |
| Voice | Yes: short, informal delegation |
| Access plausibility | Yes: every source is hers, shared with her, in her mailbox/DMs/channels, or unscoped |
| Responsibility scope | Yes: prepares the call and closes the tickets; Leonard decides on her call |

**Assigned Competency:** PASS (5)
- The core output is an audience call: which player segment (casual vs RPG) responds to the game, read from friend sessions with a playtest panel and retention as context. Who the game is for is target-audience/market work, and the base thread frames the same question as "marketing audience affinity" and a casual vs hardcore funnel (#zombie-design Sep 22). The keep/hold product consequence does not move the work out of GTM; it is a defensible, non-obvious match in the Example Task's sense. Risk noted: a reviewer could read it as Product Management, which is at most an ambiguity, not a clear mismatch.

**Assigned Task Skill:** PASS (5)
- Analysis and synthesis is the heart of the task: merge 60 sessions across Sheets, Docs, Linear comments, Gmail, Slack and GitHub under five rules, compute per-audience means, apply the lead threshold, and synthesise a memo with panel and retention context. Retrieval and Actions are stacked on top.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y — PASS
- Ambiguity: the rules are planted in Leonard's posts, the gate doc, the criteria deck, the log note, Robert's DM and the roadmap card; the prompt names none of them.
- Dynamic change: Claire's Sep 29 mail reverses her Sep 26 "No coaching" form; Arthur's Sep 30 PR comment undercuts ZOM-567's Done "covers the device gate" claim; Leonard's Sep 25 reply marks build 1943 as a dev build; the Sep 24 KPI snapshot is replaced by the Snowflake rule.
- Multi-source: Sheets, Docs, Slides, Linear, Gmail, Slack, GitHub, Trello, Snowflake, with distractors (ZOM-567, the snapshot's 8.63 simple mean, Marcus's resent form mail).
- Data seeding: PASS. 140 words; every operating detail lives in seeded records.

**Naturalness:** PASS
- First person, informal, lowercase, one run-on list of deliverables. No headings, bullets, polished connectives, enumerated contents, preservation rules or staged typos.

| Red flag | Found? | Quote |
|---|---|---|
| Document formatting | No | – |
| Polished connectives | No | – |
| Enumerated deliverable specs / preservation rules | No | the memo's contents are left to the roadmap card |
| Even, symmetric sentences | No | – |
| Staged errors | No | clean lowercase typing |

**Requirements incorporated from the environment:** the prompt incorporates Leonard's message ("his message lays out what he needs and where the rules are. can you do all of it for me?"); that message incorporates, by unique pointer, the post-note rule posts (age, gate doc, game industry, 1943 reply), the audience read criteria deck, the log note, Robert's DM, the roadmap card, the panel forward and thread, and Robert's retention post. Each is persona-visible and states its rule. The feedback note is incorporated by "the ones that came out of his feedback note".

**Anti-Patterns:**
| Pattern | Status |
|---|---|
| Command List | PASS (a list of deliverables, no first/then/finally ordering) |
| Bolt-On | PASS (each ask is one of Leonard's or the register in the same workbook; none can be removed without losing part of the close-out) |
| Pre-Solving | PASS (no rule, exclusion or answer is stated) |
| Tool Mention | PASS (no tool, parameter, MCP or "tool" wording) |

**Diversity:** goes well beyond "investigate + post one Slack message": sheet writes, 60 ticket state changes, conditional comments, a Drive doc and two Slack writes over a source-defined batch.

## Phase 2: Depth Assessment

**Unique Ground Truth:** FAIL (2) — see the generated comparison below. Readings B–J stay excluded by quoted records, but the deep recheck found one unsettled fork (Reading K): whether a session whose notes doc lists the player as family, neighbor or classmate meets the feedback note's "gamer friends" condition. Nothing settles it, and it flips the call.

### Unique Ground Truth comparison

Unique Ground Truth: FAIL 2

Basis: One decision fork is unsettled: whether sessions whose notes doc lists the player as family, neighbor or classmate meet the feedback note's 'gamer friends' condition. No persona-visible record speaks to relation; dropping those 9 counted sessions leaves 4 casual and 4 RPG, under the 6-per-audience minimum, so the call flips from hold to keep and 9 tickets change state. Every other alternative (B to J) stays excluded by a quoted record.

Alternative selection: Each trap in the data was turned into the strongest reading that a careful agent could defend: the Done ZOM-567 ticket, Claire's no-coaching form, the session timing before the game-industry rule, the 0.3.127 version string, the re-run/close-out handling, the per-run panel figures, the snapshot retention mean and the age-band endpoints. The deep recheck added Reading K: the note's 'gamer friends' wording applied to the relation field.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Apply every rule Leonard points to: drop game-industry players, dev-build 1943 sessions, coached sessions and Samsung sessions without an on-device pass; read the lead over the 17 counted sessions. | Casual lead: 9 counted casual sessions (mean 3.83) vs 8 counted RPG sessions (mean 3.375), gap 0.46 &gt;= 0.25, so HOLD the cards earlier change; the tutorial and level order work does not go on. | Register tab filled with 60 rows; 17 session tickets set to Done and 43 to Canceled; re-run note comments on the 21 technical drops (10 Robert dev-build, 11 Samsung); one memo Doc created; one Slack thread reply; one Slack channel post to Brian. | ZM audience sessions workbook Register tab; Linear ZOM-568 to ZOM-627; Julia's Drive root folder with the log note; thread under Leonard's 2025-09-30 \#zombie-design message; \#zombie-design addressed to Brian. | Reply says hold; Brian is told the tutorial and level order work does not go on; memo gives the casual call, the per-audience counts, means and gap, panel 3.33 stars over 9 ratings with player 8 left out, and install-weighted D7 9.09% over mature cohorts. | L (Evals/task\_inputs/01\_Universe\_Inject.sql lines 705-705): "casual lead means we hold the change"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; LGAME (Evals/task\_inputs/01\_Universe\_Inject.sql lines 697-697): "game-industry people don’t count"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "it never went through a store"; NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "No coaching, just observe and collect honest reactions."; CRIT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 280-280): "The lead is the higher mean star rating over counted sessions." |
| B | Treat ZOM-567 (Done; "Vision Bot run \#15 is green ... covers the device gate") as the Samsung pass, so the 11 Samsung sessions count: casual 20 sessions mean 3.03 vs RPG 3.375. | RPG lead, so KEEP the cards earlier change; the tutorial and level order work goes on. | Register filled; 28 tickets Done and 32 Canceled; re-run notes only on the 10 dev-build drops; memo; thread reply; channel post. | ZM audience sessions workbook Register tab; Linear ZOM-568 to ZOM-627; Julia's Drive root folder with the log note; thread under Leonard's 2025-09-30 \#zombie-design message; \#zombie-design addressed to Brian. | Reply says keep; Brian is told the tutorial and level order work goes on; memo gives an RPG call. | Z567C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 552-552): "Vision Bot run \#15 is green too, so that run covers the device gate for the Samsung group." |
| C | Count Claire's 13 Friday sessions because her form mail and the tickets say no coaching and none of Leonard's later posts names coaching: RPG 21 sessions mean 4.17 vs casual 3.83. | RPG lead, so KEEP the cards earlier change; the tutorial and level order work goes on. | Register filled; 30 tickets Done and 30 Canceled; re-run notes on the 21 technical drops; memo; thread reply; channel post. | ZM audience sessions workbook Register tab; Linear ZOM-568 to ZOM-627; Julia's Drive root folder with the log note; thread under Leonard's 2025-09-30 \#zombie-design message; \#zombie-design addressed to Brian. | Reply says keep; Brian is told the tutorial and level order work goes on; memo gives an RPG call. | CLAIREFORM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 368-368): "No coaching, we just watc" |
| D | Count Brian's 9 Monday sessions because they ran before Leonard's Sep 24 game-industry post: RPG 17 sessions mean 4.15 vs casual 3.83. | RPG lead, so KEEP the cards earlier change; the tutorial and level order work goes on. | Register filled; 26 tickets Done and 34 Canceled; re-run notes on the 21 technical drops; memo; thread reply; channel post. | ZM audience sessions workbook Register tab; Linear ZOM-568 to ZOM-627; Julia's Drive root folder with the log note; thread under Leonard's 2025-09-30 \#zombie-design message; \#zombie-design addressed to Brian. | Reply says keep; Brian is told the tutorial and level order work goes on; memo gives an RPG call. | DOC\_ZOM-568 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "Relation: Kadıköy ekibi" |
| E | Count Robert's 10 sessions because 0.3.127 is the published Android version: casual 19 sessions mean 3.11 vs RPG 3.375. | RPG lead, so KEEP the cards earlier change; the tutorial and level order work goes on. | Register filled; 27 tickets Done and 33 Canceled; re-run notes only on the 11 Samsung drops; memo; thread reply; channel post. | ZM audience sessions workbook Register tab; Linear ZOM-568 to ZOM-627; Julia's Drive root folder with the log note; thread under Leonard's 2025-09-30 \#zombie-design message; \#zombie-design addressed to Brian. | Reply says keep; Brian is told the tutorial and level order work goes on; memo gives an RPG call. | REQV2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "Android: 0.3.127" |
| F | Same call, but the technical drops are closed with no re-run note, or the Samsung sessions are left open until a pass exists instead of Canceled. | Casual lead: 9 counted casual sessions (mean 3.83) vs 8 counted RPG sessions (mean 3.375), gap 0.46 &gt;= 0.25, so HOLD the cards earlier change; the tutorial and level order work does not go on. | Register filled; 17 Done; Samsung tickets left Todo or all drops Canceled without re-run comments; memo; thread reply; channel post. | ZM audience sessions workbook Register tab; Linear ZOM-568 to ZOM-627; Julia's Drive root folder with the log note; thread under Leonard's 2025-09-30 \#zombie-design message; \#zombie-design addressed to Brian. | Reply says hold; Brian is told the tutorial and level order work does not go on; memo gives the casual call, the per-audience counts, means and gap, panel 3.33 stars over 9 ratings with player 8 left out, and install-weighted D7 9.09% over mature cohorts. | LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "not counted goes to Canceled." |
| G | Report the panel per run (iOS 3.4, Android 3.25) or keep player 8 in the average (3.1). | Casual lead: 9 counted casual sessions (mean 3.83) vs 8 counted RPG sessions (mean 3.375), gap 0.46 &gt;= 0.25, so HOLD the cards earlier change; the tutorial and level order work does not go on. | Register tab filled with 60 rows; 17 session tickets set to Done and 43 to Canceled; re-run note comments on the 21 technical drops (10 Robert dev-build, 11 Samsung); one memo Doc created; one Slack thread reply; one Slack channel post to Brian. | ZM audience sessions workbook Register tab; Linear ZOM-568 to ZOM-627; Julia's Drive root folder with the log note; thread under Leonard's 2025-09-30 \#zombie-design message; \#zombie-design addressed to Brian. | Reply says hold; Brian is told the work does not go on; memo gives the casual call and numbers, panel as iOS 3.4 and Android 3.25 (or 3.1 with player 8), and retention 9.09%. | PANELMAIL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 288-288): "Android run: player 6 3, player 7 3.5, player 8 1, player 9 3, player 10 3.5" |
| H | Quote retention from Vincent's KPI snapshot (simple D7 mean 8.63) instead of recomputing. | Casual lead: 9 counted casual sessions (mean 3.83) vs 8 counted RPG sessions (mean 3.375), gap 0.46 &gt;= 0.25, so HOLD the cards earlier change; the tutorial and level order work does not go on. | Register tab filled with 60 rows; 17 session tickets set to Done and 43 to Canceled; re-run note comments on the 21 technical drops (10 Robert dev-build, 11 Samsung); one memo Doc created; one Slack thread reply; one Slack channel post to Brian. | ZM audience sessions workbook Register tab; Linear ZOM-568 to ZOM-627; Julia's Drive root folder with the log note; thread under Leonard's 2025-09-30 \#zombie-design message; \#zombie-design addressed to Brian. | Reply says hold; Brian is told the work does not go on; memo gives the casual call and numbers, panel 3.33, and retention as the snapshot simple mean 8.63%. | RRET (Evals/task\_inputs/01\_Universe\_Inject.sql lines 703-703): "USER\_COHORT\_RETENTION has what you need" |
| I | Treat 25 and 45 as outside the "25–45" band, dropping ZOM-600 (age 25) and ZOM-626 (age 45): casual 7 sessions mean 3.79, still a casual lead. | Casual lead: 9 counted casual sessions (mean 3.83) vs 8 counted RPG sessions (mean 3.375), gap 0.46 &gt;= 0.25, so HOLD the cards earlier change; the tutorial and level order work does not go on. | Register filled; 15 Done and 45 Canceled; re-run notes on the 21 technical drops; memo; thread reply; channel post. | ZM audience sessions workbook Register tab; Linear ZOM-568 to ZOM-627; Julia's Drive root folder with the log note; thread under Leonard's 2025-09-30 \#zombie-design message; \#zombie-design addressed to Brian. | Reply says hold; Brian is told the work does not go on; memo gives the casual call over 7 casual sessions (mean 3.79) and 8 RPG sessions, panel 3.33 and retention 9.09%. | DOC\_ZOM-600 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 202-202): "Age: 25"; DOC\_ZOM-626 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 254-254): "Age: 45" |
| J | Leave the 2025-09-15 cohort out of the retention figure because its D14 window had not closed for every install day by the clock: 45 rows, 9.05%. | Casual lead: 9 counted casual sessions (mean 3.83) vs 8 counted RPG sessions (mean 3.375), gap 0.46 &gt;= 0.25, so HOLD the cards earlier change; the tutorial and level order work does not go on. | Register tab filled with 60 rows; 17 session tickets set to Done and 43 to Canceled; re-run note comments on the 21 technical drops (10 Robert dev-build, 11 Samsung); one memo Doc created; one Slack thread reply; one Slack channel post to Brian. | ZM audience sessions workbook Register tab; Linear ZOM-568 to ZOM-627; Julia's Drive root folder with the log note; thread under Leonard's 2025-09-30 \#zombie-design message; \#zombie-design addressed to Brian. | Reply says hold; Brian is told the work does not go on; memo gives the casual call and numbers, panel 3.33, and retention 9.05% over 45 cohort rows. | RRET (Evals/task\_inputs/01\_Universe\_Inject.sql lines 703-703): "Mature cohorts only, meaning cohorts that have a D14 figure" |
| K | Apply the feedback note's own wording that the sessions are with 'gamer friends' the same way Reading A applies its 'No coaching' and age band: a session whose notes doc gives a relation other than friend (family, neighbor, classmate) is not counted. That drops 9 sessions Reading A counts (ZOM-589, 597, 599, 600, 605, 623, 625, 626, 627), leaving 4 casual (mean 3.75) and 4 RPG (mean 3.5) counted sessions, under the deck's minimum of 6 per audience. | No clear lead (4 counted casual, 4 counted RPG, both under the minimum of 6), so KEEP the cards earlier change; the tutorial and level order work goes on. | Register filled with 60 rows; 8 session tickets set to Done and 52 to Canceled; re-run note comments on the 21 technical drops only; memo; thread reply; channel post. | ZM audience sessions workbook Register tab; Linear ZOM-568 to ZOM-627; Julia's Drive root folder with the log note; thread under Leonard's 2025-09-30 \#zombie-design message; \#zombie-design addressed to Brian. | Reply says keep; Brian is told the tutorial and level order work goes on; memo gives no clear lead over 4 casual and 4 RPG counted sessions. | NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "get real-life feedback from 25–45 casual and/or RPG gamer friends (not kids)"; DOC\_ZOM-589 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 180-180): "Relation: family"; DOC\_ZOM-597 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 196-196): "Relation: neighbor"; DOC\_ZOM-605 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 212-212): "Relation: classmate"; CRIT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 280-280): "At least 6 counted sessions per audience."; L (Evals/task\_inputs/01\_Universe\_Inject.sql lines 705-705): "no clear lead, we keep it" |

Explicit option inventory: The prompt offers keep or hold and Leonard's message offers casual, RPG or no clear lead; every option is mapped.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "with keep or hold"; L (Evals/task\_inputs/01\_Universe\_Inject.sql lines 705-705): "casual, RPG or no clear lead"

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| hold | RETAINED | A | Leading reading: casual lead means hold; not settled against Reading K. Evidence: P (Evals/task\_inputs/04\_Prompt.txt): "keep or hold" |
| keep | RETAINED | B, C, D, E, K | Readings B to E are excluded by quoted rules, but Reading K (non-friend relations not counted) reaches keep and no record excludes it. Evidence: P (Evals/task\_inputs/04\_Prompt.txt): "keep or hold" |
| casual lead | RETAINED | A | 9 casual vs 8 RPG counted sessions, gap 0.46. Evidence: L (Evals/task\_inputs/01\_Universe\_Inject.sql lines 705-705): "casual, RPG or no clear lead" |
| RPG lead | EXCLUDED | B, C, D, E | Only reached by counting sessions the rules drop. Evidence: L (Evals/task\_inputs/01\_Universe\_Inject.sql lines 705-705): "casual, RPG or no clear lead" |
| no clear lead | RETAINED | E, K | Reading E is excluded, but Reading K leaves 4 and 4 counted sessions, under the 6-per-audience minimum, and no record excludes it. Evidence: L (Evals/task\_inputs/01\_Universe\_Inject.sql lines 705-705): "casual, RPG or no clear lead" |

Compared alternative: B
Resolution: EXCLUDED. The gate doc defines a pass as one that ran on the device and says a closed ticket is not a pass; Arthur, who owns the job, states on the PR the gate doc points to that a green comes from editor play mode with no phone. ZOM-567 claims the editor green as the device pass, which the gate rules out, so no Samsung session counts.
Resolution evidence: GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "the pass comes from Unity editor play mode on the Jenkins machine, no phone in the loop"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Hold vs keep. |
| writes | DIFFERENT | 17 vs 28 Done; Samsung re-run notes present vs absent. |
| destinations | SAME | Same workbook tab, tickets, folder, thread and channel. |
| contents | DIFFERENT | Reply hold vs keep; Brian told stop vs go on. |

Authority chain: P → L → LPOST → GATE → ARTH

Resolution relevance challenge: The gate doc is the rule Leonard incorporates for devices; Arthur speaks to exactly the Vision Bot green that ZOM-567 relies on.
Delegation challenge: NOT_CLAIMED. No alternative final call is accepted; the cited rule fixes the outcome.
Challenge evidence: Z567C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 552-552): "that run covers the device gate for the Samsung group"; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "nothing about how the game behaves on a given handset"

Compared alternative: C
Resolution: EXCLUDED. Leonard's feedback note, which the prompt names as the origin of the sessions, requires no coaching; Claire's own Sep 29 mail to Julia says she sat the Friday group down and took them through how ZM plays, so those 13 sessions fail the note's condition.
Resolution evidence: NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "No coaching, just observe and collect honest reactions."; CLAIRE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 424-424): "Before anyone touched their phone I sat them all down and took them through how ZM plays"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Hold vs keep. |
| writes | DIFFERENT | 17 vs 30 Done. |
| destinations | SAME | Same workbook tab, tickets, folder, thread and channel. |
| contents | DIFFERENT | Reply hold vs keep. |

Authority chain: P → NOTE

Resolution relevance challenge: The note sets the session condition; Claire's mail is about the same 13 sessions and corrects her form's no-coaching line.
Delegation challenge: NOT_CLAIMED. No alternative final call is accepted; the cited rule fixes the outcome.
Challenge evidence: CLAIRE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 424-424): "Before anyone touched their phone I sat them all down and took them through how ZM plays"; CLAIREFORM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 368-368): "No coaching, we just watc"

Compared alternative: D
Resolution: EXCLUDED. Leonard's rule post says game-industry people do not count and that this goes for sessions already run; Brian's DM says the whole Kadıköy group works at mobile game companies.
Resolution evidence: LGAME (Evals/task\_inputs/01\_Universe\_Inject.sql lines 697-697): "game-industry people don’t count, and that goes for sessions already run too"; BDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 691-691): "Kadıköy ekibi komple oyun sektöründen"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Hold vs keep. |
| writes | DIFFERENT | 17 vs 26 Done. |
| destinations | SAME | Same workbook tab, tickets, folder, thread and channel. |
| contents | DIFFERENT | Reply hold vs keep. |

Authority chain: P → L → LGAME

Resolution relevance challenge: The post names the timing case directly ("sessions already run"), and the DM identifies the players.
Delegation challenge: NOT_CLAIMED. No alternative final call is accepted; the cited rule fixes the outcome.
Challenge evidence: LGAME (Evals/task\_inputs/01\_Universe\_Inject.sql lines 697-697): "that goes for sessions already run too"

Compared alternative: E
Resolution: EXCLUDED. Leonard's rule reply names android 1943 as a build that never went through a store, and the gate doc says sessions on dev builds do not count; Robert's notes docs record Build 0.3.127 (1943).
Resolution evidence: LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "careful with android 1943"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "it never went through a store"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "Sessions on dev builds do not count."; DOC\_ZOM-577 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 156-156): "Build: 0.3.127 (1943)"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Hold vs keep. |
| writes | DIFFERENT | 17 vs 27 Done; dev-build re-run notes present vs absent. |
| destinations | SAME | Same workbook tab, tickets, folder, thread and channel. |
| contents | DIFFERENT | Reply hold vs keep. |

Authority chain: P → L → LTHREAD

Resolution relevance challenge: The reply names the exact build number on Robert's notes docs.
Delegation challenge: NOT_CLAIMED. No alternative final call is accepted; the cited rule fixes the outcome.
Challenge evidence: LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "careful with android 1943"

Compared alternative: F
Resolution: EXCLUDED. Robert's rule, which Leonard incorporates, says a session dropped for a device or build reason gets a re-run note so the observer runs it again; the log note says not-counted sessions go to Canceled. Samsung (device) and 1943 (build) drops therefore get both.
Resolution evidence: RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it so the observer runs it again"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "not counted goes to Canceled."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Hold in both. |
| writes | DIFFERENT | 21 re-run comments and 43 Canceled vs none or Samsung left Todo. |
| destinations | SAME | Same workbook tab, tickets, folder, thread and channel. |
| contents | SAME | Same reply, post and memo. |

Authority chain: P → L → RDM

Resolution relevance challenge: Both cited rules speak to how not-counted sessions are closed and which ones get a re-run note.
Delegation challenge: NOT_CLAIMED. No alternative final call is accepted; the cited rule fixes the outcome.
Challenge evidence: RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed"

Compared alternative: G
Resolution: EXCLUDED. Leonard set the panel read in the thread where Robert asked who the players were: one number per player, a void rating comes out of both the sum and the count, and the rest is averaged. His forward marks player 8 void. That gives one average, 30/9 = 3.33.
Resolution evidence: LPANEL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 695-695): "for the panel it’s stars per player, one number each. if a rating is void it comes out of both the sum and the count, so you average what’s left"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Hold in both. |
| writes | SAME | Same writes. |
| destinations | SAME | Same workbook tab, tickets, folder, thread and channel. |
| contents | DIFFERENT | Panel 3.33 vs 3.4/3.25 or 3.1. |

Authority chain: P → L → LPANEL

Resolution relevance challenge: The rule asks for one average over what is left after removing the void rating.
Delegation challenge: NOT_CLAIMED. No alternative final call is accepted; the cited rule fixes the outcome.
Challenge evidence: LPANEL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 695-695): "so you average what’s left"

Compared alternative: H
Resolution: EXCLUDED. Robert's retention rule, incorporated by Leonard, asks for install-weighted D7 over cohorts that have a D14 figure, both platforms pooled, from USER\_COHORT\_RETENTION, and rejects a simple mean of cohorts, which is what the snapshot's 8.63 is.
Resolution evidence: RRET (Evals/task\_inputs/01\_Universe\_Inject.sql lines 703-703): "use install-weighted D7, not a simple mean of the cohorts. Mature cohorts only, meaning cohorts that have a D14 figure, both platforms pooled."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Hold in both. |
| writes | SAME | Same writes. |
| destinations | SAME | Same workbook tab, tickets, folder, thread and channel. |
| contents | DIFFERENT | Retention 9.09% vs 8.63%. |

Authority chain: P → L → RRET

Resolution relevance challenge: The rule names both the method and the source table.
Delegation challenge: NOT_CLAIMED. No alternative final call is accepted; the cited rule fixes the outcome.
Challenge evidence: RRET (Evals/task\_inputs/01\_Universe\_Inject.sql lines 703-703): "not a simple mean of the cohorts"

Compared alternative: I
Resolution: EXCLUDED. Leonard's clarification gives the band as 25–45 years old, which in ordinary use includes both ends; no record narrows it. ZOM-600 (25) and ZOM-626 (45) are in the band.
Resolution evidence: LAGE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 685-685): "age. 25–45 years old, not a headcount"; NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "25–45 casual and/or RPG gamer friends (not kids)"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Casual lead and hold in both. |
| writes | DIFFERENT | 17 vs 15 Done. |
| destinations | SAME | Same workbook tab, tickets, folder, thread and channel. |
| contents | DIFFERENT | Counts 9 vs 7 casual sessions. |

Authority chain: P → L → LAGE

Resolution relevance challenge: The band is stated as an inclusive range of ages; the only purpose stated is excluding kids.
Delegation challenge: NOT_CLAIMED. No alternative final call is accepted; the cited rule fixes the outcome.
Challenge evidence: LAGE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 685-685): "25–45 years old"

Compared alternative: J
Resolution: EXCLUDED. Robert's rule defines a mature cohort operationally as one that has a D14 figure; the 2025-09-15 rows carry d14\_ret values in USER\_COHORT\_RETENTION, so they are in by the rule's own test.
Resolution evidence: RRET (Evals/task\_inputs/01\_Universe\_Inject.sql lines 703-703): "Mature cohorts only, meaning cohorts that have a D14 figure, both platforms pooled."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Hold in both. |
| writes | SAME | Same writes. |
| destinations | SAME | Same workbook tab, tickets, folder, thread and channel. |
| contents | DIFFERENT | Retention 9.09% vs 9.05%. |

Authority chain: P → L → RRET

Resolution relevance challenge: The rule names its maturity test (a D14 figure present), which the 2025-09-15 cohort meets.
Delegation challenge: NOT_CLAIMED. No alternative final call is accepted; the cited rule fixes the outcome.
Challenge evidence: RRET (Evals/task\_inputs/01\_Universe\_Inject.sql lines 703-703): "cohorts that have a D14 figure"

Compared alternative: K
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. No persona-visible record says whether a session with a family member, neighbor or classmate meets the feedback note's 'gamer friends' condition. The notes docs record relation as a separate field with friend, family, neighbor and classmate as distinct values, and Reading A already applies the same note sentence's 'No coaching' to drop Claire's 13 sessions. Leonard's later posts exclude game-industry players, dev builds and Samsung without a device pass, but none speaks to relation; the criteria deck and the log note are silent on it. Dropping the 9 non-friend counted sessions leaves 4 and 4, under the deck's 6-per-audience minimum, which flips the call to keep.
Resolution evidence: NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "casual and/or RPG gamer friends (not kids)"; DOC\_ZOM-600 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 202-202): "Relation: family"; CRIT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 280-280): "At least 6 counted sessions per audience."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Hold vs keep. |
| writes | DIFFERENT | 17 vs 8 Done; 9 tickets change state. |
| destinations | SAME | Same workbook tab, tickets, folder, thread and channel. |
| contents | DIFFERENT | Reply hold vs keep; Brian told stop vs go on. |

Resolution relevance challenge: Leonard's Sep 30 'the friend sessions are in your workbook now' names where the sessions are, not which of them count; the counted/not-counted split already presumes some workbook sessions are dropped, so it does not settle relation.
Delegation challenge: NOT_CLAIMED. No record delegates the relation question or accepts both calls.
Challenge evidence: L (Evals/task\_inputs/01\_Universe\_Inject.sql lines 705-705): "the friend sessions are in your workbook now"

Decision sweep: The prompt and Leonard's message apply the counting rules to each friend session (counted or not, Done or Canceled, re-run note or not).
Decision rule: LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done, not counted goes to Canceled."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it so the observer runs it again"; CRIT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 280-280): "The lead is the higher mean star rating over counted sessions."

| Item | Outcome | Basis | Settled by / gap |
|---|---|---|---|
| ZOM-568 | ZOM-568: not counted, player works in games (Kadıköy ekibi) -&gt; Canceled, no re-run note | RECORD | DOC\_ZOM-568 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 138-138): "Relation: Kadıköy ekibi"; BDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 691-691): "Kadıköy ekibi komple oyun sektöründen"; LGAME (Evals/task\_inputs/01\_Universe\_Inject.sql lines 697-697): "game-industry people don’t count, and that goes for sessions already run too"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-569 | ZOM-569: not counted, player works in games (Kadıköy ekibi) -&gt; Canceled, no re-run note | RECORD | DOC\_ZOM-569 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 140-140): "Relation: Kadıköy ekibi"; BDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 691-691): "Kadıköy ekibi komple oyun sektöründen"; LGAME (Evals/task\_inputs/01\_Universe\_Inject.sql lines 697-697): "game-industry people don’t count, and that goes for sessions already run too"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-570 | ZOM-570: not counted, player works in games (Kadıköy ekibi) -&gt; Canceled, no re-run note | RECORD | DOC\_ZOM-570 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 142-142): "Relation: Kadıköy ekibi"; BDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 691-691): "Kadıköy ekibi komple oyun sektöründen"; LGAME (Evals/task\_inputs/01\_Universe\_Inject.sql lines 697-697): "game-industry people don’t count, and that goes for sessions already run too"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-571 | ZOM-571: not counted, player works in games (Kadıköy ekibi) -&gt; Canceled, no re-run note | RECORD | DOC\_ZOM-571 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 144-144): "Relation: Kadıköy ekibi"; BDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 691-691): "Kadıköy ekibi komple oyun sektöründen"; LGAME (Evals/task\_inputs/01\_Universe\_Inject.sql lines 697-697): "game-industry people don’t count, and that goes for sessions already run too"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-572 | ZOM-572: not counted, player works in games (Kadıköy ekibi) -&gt; Canceled, no re-run note | RECORD | DOC\_ZOM-572 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 146-146): "Relation: Kadıköy ekibi"; BDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 691-691): "Kadıköy ekibi komple oyun sektöründen"; LGAME (Evals/task\_inputs/01\_Universe\_Inject.sql lines 697-697): "game-industry people don’t count, and that goes for sessions already run too"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-573 | ZOM-573: not counted, player works in games (Kadıköy ekibi) -&gt; Canceled, no re-run note | RECORD | DOC\_ZOM-573 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 148-148): "Relation: Kadıköy ekibi"; BDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 691-691): "Kadıköy ekibi komple oyun sektöründen"; LGAME (Evals/task\_inputs/01\_Universe\_Inject.sql lines 697-697): "game-industry people don’t count, and that goes for sessions already run too"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-574 | ZOM-574: not counted, player works in games (Kadıköy ekibi) -&gt; Canceled, no re-run note | RECORD | DOC\_ZOM-574 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 150-150): "Relation: Kadıköy ekibi"; BDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 691-691): "Kadıköy ekibi komple oyun sektöründen"; LGAME (Evals/task\_inputs/01\_Universe\_Inject.sql lines 697-697): "game-industry people don’t count, and that goes for sessions already run too"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-575 | ZOM-575: not counted, player works in games (Kadıköy ekibi) -&gt; Canceled, no re-run note | RECORD | DOC\_ZOM-575 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 152-152): "Relation: Kadıköy ekibi"; BDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 691-691): "Kadıköy ekibi komple oyun sektöründen"; LGAME (Evals/task\_inputs/01\_Universe\_Inject.sql lines 697-697): "game-industry people don’t count, and that goes for sessions already run too"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-576 | ZOM-576: not counted, player works in games (Kadıköy ekibi) -&gt; Canceled, no re-run note | RECORD | DOC\_ZOM-576 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 154-154): "Relation: Kadıköy ekibi"; BDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 691-691): "Kadıköy ekibi komple oyun sektöründen"; LGAME (Evals/task\_inputs/01\_Universe\_Inject.sql lines 697-697): "game-industry people don’t count, and that goes for sessions already run too"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-577 | ZOM-577: not counted, dev build 0.3.127 (1943) -&gt; Canceled with a re-run note | RECORD | DOC\_ZOM-577 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 156-156): "Build: 0.3.127 (1943)"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "careful with android 1943"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "it never went through a store"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "Sessions on dev builds do not count."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-578 | ZOM-578: not counted, dev build 0.3.127 (1943) -&gt; Canceled with a re-run note | RECORD | DOC\_ZOM-578 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 158-158): "Build: 0.3.127 (1943)"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "careful with android 1943"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "it never went through a store"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "Sessions on dev builds do not count."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-579 | ZOM-579: not counted, dev build 0.3.127 (1943) -&gt; Canceled with a re-run note | RECORD | DOC\_ZOM-579 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 160-160): "Build: 0.3.127 (1943)"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "careful with android 1943"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "it never went through a store"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "Sessions on dev builds do not count."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-580 | ZOM-580: not counted, dev build 0.3.127 (1943) -&gt; Canceled with a re-run note | RECORD | DOC\_ZOM-580 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 162-162): "Build: 0.3.127 (1943)"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "careful with android 1943"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "it never went through a store"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "Sessions on dev builds do not count."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-581 | ZOM-581: not counted, dev build 0.3.127 (1943) -&gt; Canceled with a re-run note | RECORD | DOC\_ZOM-581 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 164-164): "Build: 0.3.127 (1943)"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "careful with android 1943"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "it never went through a store"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "Sessions on dev builds do not count."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-582 | ZOM-582: not counted, dev build 0.3.127 (1943) -&gt; Canceled with a re-run note | RECORD | DOC\_ZOM-582 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 166-166): "Build: 0.3.127 (1943)"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "careful with android 1943"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "it never went through a store"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "Sessions on dev builds do not count."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-583 | ZOM-583: not counted, dev build 0.3.127 (1943) -&gt; Canceled with a re-run note | RECORD | DOC\_ZOM-583 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 168-168): "Build: 0.3.127 (1943)"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "careful with android 1943"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "it never went through a store"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "Sessions on dev builds do not count."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-584 | ZOM-584: not counted, dev build 0.3.127 (1943) -&gt; Canceled with a re-run note | RECORD | DOC\_ZOM-584 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 170-170): "Build: 0.3.127 (1943)"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "careful with android 1943"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "it never went through a store"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "Sessions on dev builds do not count."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-585 | ZOM-585: not counted, dev build 0.3.127 (1943) -&gt; Canceled with a re-run note | RECORD | DOC\_ZOM-585 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 172-172): "Build: 0.3.127 (1943)"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "careful with android 1943"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "it never went through a store"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "Sessions on dev builds do not count."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-586 | ZOM-586: not counted, dev build 0.3.127 (1943) -&gt; Canceled with a re-run note | RECORD | DOC\_ZOM-586 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 174-174): "Build: 0.3.127 (1943)"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "careful with android 1943"; LTHREAD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 699-699): "it never went through a store"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "Sessions on dev builds do not count."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-587 | ZOM-587: not counted, Samsung phone (phone was a Galaxy S24) with no on-device pass -&gt; Canceled with a re-run note | RECORD | CMT\_ZOM-587 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 592-592): "phone was a Galaxy S24"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "no phone in the loop"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-588 | ZOM-588: not counted, Samsung phone (phone: SM-A546E) with no on-device pass -&gt; Canceled with a re-run note | RECORD | CMT\_ZOM-588 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 594-594): "phone: SM-A546E"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "no phone in the loop"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-589 | ZOM-589: counted under Reading A (RPG, 3 stars) -&gt; Done under A; relation 'family' is outside 'gamer friends' under K -&gt; Canceled | BOUNDARY | Edge: Relation 'family' sits at the edge of the feedback note's 'gamer friends' condition; no record says whether non-friend relations count.. Not settled; tested as A vs K |
| ZOM-590 | ZOM-590: not counted, Samsung phone (played on an SM-S921B) with no on-device pass -&gt; Canceled with a re-run note | RECORD | CMT\_ZOM-590 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 598-598): "played on an SM-S921B"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "no phone in the loop"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-591 | ZOM-591: not counted, Samsung phone (Galaxy S23 FE) with no on-device pass -&gt; Canceled with a re-run note | RECORD | CMT\_ZOM-591 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 600-600): "Galaxy S23 FE"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "no phone in the loop"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-592 | ZOM-592: counted (RPG, 3.5 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-592 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 186-186): "Build: 0.3.40 (40)"; DOC\_ZOM-592 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 186-186): "Relation: friend"; CMT\_ZOM-592 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 602-602): "on an iPhone 12"; REQV3 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "iOS: 0.3.40"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-593 | ZOM-593: not counted, Samsung phone (phone was a Galaxy A54) with no on-device pass -&gt; Canceled with a re-run note | RECORD | CMT\_ZOM-593 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 604-604): "phone was a Galaxy A54"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "no phone in the loop"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-594 | ZOM-594: not counted, Samsung phone (phone: Galaxy S22) with no on-device pass -&gt; Canceled with a re-run note | RECORD | CMT\_ZOM-594 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 606-606): "phone: Galaxy S22"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "no phone in the loop"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-595 | ZOM-595: counted (casual, 4 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-595 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 192-192): "Build: 0.3.127 (127)"; DOC\_ZOM-595 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 192-192): "Relation: friend"; CMT\_ZOM-595 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 608-608): "device for this one: OnePlus 11"; REQV2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "Android: 0.3.127"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-596 | ZOM-596: not counted, Samsung phone (played on a Galaxy A15) with no on-device pass -&gt; Canceled with a re-run note | RECORD | CMT\_ZOM-596 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 610-610): "played on a Galaxy A15"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "no phone in the loop"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-597 | ZOM-597: counted under Reading A (RPG, 3 stars) -&gt; Done under A; relation 'neighbor' is outside 'gamer friends' under K -&gt; Canceled | BOUNDARY | Edge: Relation 'neighbor' sits at the edge of the feedback note's 'gamer friends' condition; no record says whether non-friend relations count.. Not settled; tested as A vs K |
| ZOM-598 | ZOM-598: counted (RPG, 3.5 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-598 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 198-198): "Build: 0.3.127 (127)"; DOC\_ZOM-598 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 198-198): "Relation: friend"; CMT\_ZOM-598 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 614-614): "on a Pixel 8"; REQV2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "Android: 0.3.127"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-599 | ZOM-599: counted under Reading A (RPG, 3.5 stars) -&gt; Done under A; relation 'family' is outside 'gamer friends' under K -&gt; Canceled | BOUNDARY | Edge: Relation 'family' sits at the edge of the feedback note's 'gamer friends' condition; no record says whether non-friend relations count.. Not settled; tested as A vs K |
| ZOM-600 | ZOM-600: counted under Reading A (casual, 4 stars) -&gt; Done under A; relation 'family' is outside 'gamer friends' under K -&gt; Canceled | BOUNDARY | Edge: Relation 'family' sits at the edge of the feedback note's 'gamer friends' condition; no record says whether non-friend relations count.. Not settled; tested as A vs K |
| ZOM-601 | ZOM-601: not counted, Samsung phone (device for this one: Galaxy A35) with no on-device pass -&gt; Canceled with a re-run note | RECORD | CMT\_ZOM-601 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 620-620): "device for this one: Galaxy A35"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "no phone in the loop"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-602 | ZOM-602: counted (casual, 4 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-602 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 206-206): "Build: 0.3.40 (40)"; DOC\_ZOM-602 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 206-206): "Relation: friend"; CMT\_ZOM-602 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 622-622): "played on an iPhone 14"; REQV3 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "iOS: 0.3.40"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-603 | ZOM-603: not counted, Samsung phone (SM-A346E) with no on-device pass -&gt; Canceled with a re-run note | RECORD | CMT\_ZOM-603 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 624-624): "SM-A346E"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "no phone in the loop"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-604 | ZOM-604: counted (RPG, 3.5 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-604 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 210-210): "Build: 0.3.40 (40)"; DOC\_ZOM-604 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 210-210): "Relation: friend"; CMT\_ZOM-604 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 626-626): "on an iPhone 15"; REQV3 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "iOS: 0.3.40"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-605 | ZOM-605: counted under Reading A (casual, 3.5 stars) -&gt; Done under A; relation 'classmate' is outside 'gamer friends' under K -&gt; Canceled | BOUNDARY | Edge: Relation 'classmate' sits at the edge of the feedback note's 'gamer friends' condition; no record says whether non-friend relations count.. Not settled; tested as A vs K |
| ZOM-606 | ZOM-606: not counted, Samsung phone (phone: SM-S911B) with no on-device pass -&gt; Canceled with a re-run note | RECORD | CMT\_ZOM-606 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 630-630): "phone: SM-S911B"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "no phone in the loop"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-607 | ZOM-607: not counted, Claire coached the Friday group -&gt; Canceled, no re-run note | RECORD | CLAIRE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 424-424): "Before anyone touched their phone I sat them all down and took them through how ZM plays"; CLAIREFORM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 368-368): "Host: Claire Morgan. Day: Fri Sep 26, at my place. 13 sessions"; NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "No coaching, just observe and collect honest reactions."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-608 | ZOM-608: not counted, Claire coached the Friday group -&gt; Canceled, no re-run note | RECORD | CLAIRE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 424-424): "Before anyone touched their phone I sat them all down and took them through how ZM plays"; CLAIREFORM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 368-368): "Host: Claire Morgan. Day: Fri Sep 26, at my place. 13 sessions"; NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "No coaching, just observe and collect honest reactions."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-609 | ZOM-609: not counted, Claire coached the Friday group -&gt; Canceled, no re-run note | RECORD | CLAIRE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 424-424): "Before anyone touched their phone I sat them all down and took them through how ZM plays"; CLAIREFORM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 368-368): "Host: Claire Morgan. Day: Fri Sep 26, at my place. 13 sessions"; NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "No coaching, just observe and collect honest reactions."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-610 | ZOM-610: not counted, Claire coached the Friday group -&gt; Canceled, no re-run note | RECORD | CLAIRE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 424-424): "Before anyone touched their phone I sat them all down and took them through how ZM plays"; CLAIREFORM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 368-368): "Host: Claire Morgan. Day: Fri Sep 26, at my place. 13 sessions"; NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "No coaching, just observe and collect honest reactions."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-611 | ZOM-611: not counted, Claire coached the Friday group -&gt; Canceled, no re-run note | RECORD | CLAIRE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 424-424): "Before anyone touched their phone I sat them all down and took them through how ZM plays"; CLAIREFORM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 368-368): "Host: Claire Morgan. Day: Fri Sep 26, at my place. 13 sessions"; NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "No coaching, just observe and collect honest reactions."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-612 | ZOM-612: not counted, Claire coached the Friday group -&gt; Canceled, no re-run note | RECORD | CLAIRE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 424-424): "Before anyone touched their phone I sat them all down and took them through how ZM plays"; CLAIREFORM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 368-368): "Host: Claire Morgan. Day: Fri Sep 26, at my place. 13 sessions"; NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "No coaching, just observe and collect honest reactions."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-613 | ZOM-613: not counted, Claire coached the Friday group -&gt; Canceled, no re-run note | RECORD | CLAIRE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 424-424): "Before anyone touched their phone I sat them all down and took them through how ZM plays"; CLAIREFORM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 368-368): "Host: Claire Morgan. Day: Fri Sep 26, at my place. 13 sessions"; NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "No coaching, just observe and collect honest reactions."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-614 | ZOM-614: not counted, Claire coached the Friday group -&gt; Canceled, no re-run note | RECORD | CLAIRE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 424-424): "Before anyone touched their phone I sat them all down and took them through how ZM plays"; CLAIREFORM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 368-368): "Host: Claire Morgan. Day: Fri Sep 26, at my place. 13 sessions"; NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "No coaching, just observe and collect honest reactions."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-615 | ZOM-615: not counted, Claire coached the Friday group -&gt; Canceled, no re-run note | RECORD | CLAIRE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 424-424): "Before anyone touched their phone I sat them all down and took them through how ZM plays"; CLAIREFORM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 368-368): "Host: Claire Morgan. Day: Fri Sep 26, at my place. 13 sessions"; NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "No coaching, just observe and collect honest reactions."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-616 | ZOM-616: not counted, Claire coached the Friday group -&gt; Canceled, no re-run note | RECORD | CLAIRE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 424-424): "Before anyone touched their phone I sat them all down and took them through how ZM plays"; CLAIREFORM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 368-368): "Host: Claire Morgan. Day: Fri Sep 26, at my place. 13 sessions"; NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "No coaching, just observe and collect honest reactions."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-617 | ZOM-617: not counted, Claire coached the Friday group -&gt; Canceled, no re-run note | RECORD | CLAIRE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 424-424): "Before anyone touched their phone I sat them all down and took them through how ZM plays"; CLAIREFORM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 368-368): "Host: Claire Morgan. Day: Fri Sep 26, at my place. 13 sessions"; NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "No coaching, just observe and collect honest reactions."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-618 | ZOM-618: not counted, Claire coached the Friday group -&gt; Canceled, no re-run note | RECORD | CLAIRE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 424-424): "Before anyone touched their phone I sat them all down and took them through how ZM plays"; CLAIREFORM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 368-368): "Host: Claire Morgan. Day: Fri Sep 26, at my place. 13 sessions"; NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "No coaching, just observe and collect honest reactions."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-619 | ZOM-619: not counted, Claire coached the Friday group -&gt; Canceled, no re-run note | RECORD | CLAIRE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 424-424): "Before anyone touched their phone I sat them all down and took them through how ZM plays"; CLAIREFORM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 368-368): "Host: Claire Morgan. Day: Fri Sep 26, at my place. 13 sessions"; NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "No coaching, just observe and collect honest reactions."; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "Dropped for anything else, no re-run, it just gets closed" |
| ZOM-620 | ZOM-620: not counted, Samsung phone (played on an SM-A155F) with no on-device pass -&gt; Canceled with a re-run note | RECORD | CMT\_ZOM-620 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 658-658): "played on an SM-A155F"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "no phone in the loop"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-621 | ZOM-621: counted (casual, 3.5 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-621 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 244-244): "Build: 0.3.40 (40)"; DOC\_ZOM-621 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 244-244): "Relation: friend"; CMT\_ZOM-621 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 660-660): "iPhone 13"; REQV3 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "iOS: 0.3.40"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-622 | ZOM-622: counted (casual, 3.5 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-622 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 246-246): "Build: 0.3.40 (40)"; DOC\_ZOM-622 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 246-246): "Relation: friend"; CMT\_ZOM-622 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 662-662): "on an iPhone 12"; REQV3 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "iOS: 0.3.40"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-623 | ZOM-623: counted under Reading A (RPG, 3.5 stars) -&gt; Done under A; relation 'family' is outside 'gamer friends' under K -&gt; Canceled | BOUNDARY | Edge: Relation 'family' sits at the edge of the feedback note's 'gamer friends' condition; no record says whether non-friend relations count.. Not settled; tested as A vs K |
| ZOM-624 | ZOM-624: counted (RPG, 3.5 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-624 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 250-250): "Build: 0.3.40 (40)"; DOC\_ZOM-624 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 250-250): "Relation: friend"; CMT\_ZOM-624 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 666-666): "phone: iPhone 15"; REQV3 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "iOS: 0.3.40"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-625 | ZOM-625: counted under Reading A (casual, 4 stars) -&gt; Done under A; relation 'classmate' is outside 'gamer friends' under K -&gt; Canceled | BOUNDARY | Edge: Relation 'classmate' sits at the edge of the feedback note's 'gamer friends' condition; no record says whether non-friend relations count.. Not settled; tested as A vs K |
| ZOM-626 | ZOM-626: counted under Reading A (casual, 4 stars) -&gt; Done under A; relation 'classmate' is outside 'gamer friends' under K -&gt; Canceled | BOUNDARY | Edge: Relation 'classmate' sits at the edge of the feedback note's 'gamer friends' condition; no record says whether non-friend relations count.. Not settled; tested as A vs K |
| ZOM-627 | ZOM-627: counted under Reading A (casual, 4 stars) -&gt; Done under A; relation 'classmate' is outside 'gamer friends' under K -&gt; Canceled | BOUNDARY | Edge: Relation 'classmate' sits at the edge of the feedback note's 'gamer friends' condition; no record says whether non-friend relations count.. Not settled; tested as A vs K |

Strongest-alternative challenge (K): The note's 'gamer friends' wording is part of the same sentence whose 'No coaching' Reading A applies, and the notes docs mark family, neighbor and classmate as relations distinct from friend; dropping those 9 counted sessions flips the call to keep, and no record speaks to relation.
Challenge evidence: NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "gamer friends (not kids). No coaching"

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

**Feasibility:** PASS (5)

| Ask | Required capability | Tool(s) | Feasible? |
|---|---|---|---|
| Read sessions, rules, mails, tickets, PR | read tools | gsheets_values_get, gdocs_get_document, gslides_get_presentation_text, gmail_search_messages, linear_list_comments, slack_read_thread, github_get_pull_request_comments, trello_get_card | Yes |
| Retention | SQL over a Snowflake table | snowflake_execute_query | Yes |
| Register rows | sheet write | gsheets_values_update / values_append | Yes |
| Memo in Julia's folder | create a Doc with a parent | gdrive_create_file (parentId) or gdocs_create_document + gdrive_move_file | Yes |
| Ticket close-out and re-run notes | state change, comment | linear_update_issue (state), linear_create_comment | Yes |
| Thread reply / channel post | Slack write | slack_send_message (thread_ts) | Yes |

- A1 service availability: Snowflake is live and unscoped; the retention read uses a cataloged query tool.
- B data: every needed fact exists (60 Log rows, 60 notes docs, 60 device comments, 18 mails, the rule records, USER_COHORT_RETENTION rows).
- C dimensional: per-audience split uses the observer label on each session (Log "audience" column, notes doc "Audience:"); per-platform pooling uses USER_COHORT_RETENTION.platform. Fields exist.
- D numeric observability: stars are half-point values in Sheets/Docs; retention uses `installs`, `d7_ret`, `d14_ret` columns, all returned by the query tool. The rendering of query results is an evidence limit of the catalog (no return schemas), not a defect; the inputs survive at the needed precision.
- E persona ACL: every scoped read is Julia's own file/mail/channel or shared with her (all 60 notes docs list julia.lawson in `shared_with_emails_json`; gate doc shared as reader; Claire's mail in her INBOX; DMs D076RBM29JS and D05GU6L0XFH include her). Lens 2: no ask points at a record outside her view. No link, attachment or reply-all ask (tool_outputs.md risks do not apply).

**Truthfulness:** PASS (5). Every premise is in the premise table below; none is contradicted and none sits after the clock.

| Entity/Fact from prompt | Record | Found / accurate |
|---|---|---|
| "leonard asked me in #zombie-design for the audience call" | SQL L705, C090N54TG79, 2025-09-30 21:10 UTC (14:10 PT) | Yes / yes |
| "his feedback note" | base #zombie-design /537, 2025-09-22 05:01 UTC; Leonard calls it "the feedback note" (SQL L693, L697) | Yes / yes |
| "the cards earlier change" | SQL L705 "the cards earlier change from Monday"; base /731 Robert 2025-09-29 "move up card introduction earlier" | Yes / yes |
| "my audience sessions workbook" | Drive f_43bc35baf77fd59f4e57b8 "ZM audience sessions", owner Julia | Yes / yes |
| "the register tab there" | sheet index 1 "Register" | Yes / yes |
| "the memo he asked for" | SQL L705 "what the memo holds is on the roadmap card"; Trello card idShort 80 | Yes / yes |
| "my drive folder" | d_8140f09bf9f1b94cb8ee2d (Julia's root, holds the log note); card "memo goes in Julia's folder with her log note" | Yes / yes |
| "the session tickets" | ZOM-568…ZOM-627, Todo, assignee Julia | Yes / yes |
| "his thread" | Leonard's top-level message, "reply here" | Yes / yes |
| "brian in #zombie-design" | channels.json /132 members include EMPLOYEE_0026 | Yes / yes |
| "the tutorial and level order work" | base /731 (Brian "will make the changes in the tutorial", "shuffle the levels"), /777, /780 | Yes / yes |

Tight identifiers: one channel (#zombie-design), verified exactly. No ticket IDs, amounts or dates stated. State premises: nothing is treated as done after 2025-09-30 23:59:59 PT; no departed person acts.

**Tool Use & Cross-service:** PASS (5). Linear changes graded facts (device comments decide the 11 Samsung exclusions; ticket states are written); Gmail changes one (Claire's Sep 29 mail removes 13 sessions); Docs change one (build 1943 and "Kadıköy ekibi" relations); GitHub changes one (Arthur's comment kills the ZOM-567 pass); Snowflake changes the retention figure; Slack holds the rules and takes two writes; Sheets takes the register. Dropping any of Linear, Gmail, Docs or GitHub flips the keep/hold call.

**Investigation + Action:** PASS (5). The writes (register verdicts, Done/Canceled, re-run notes, memo, keep/hold, Brian's go/stop) all depend on the investigation.

**Clarity & Specificity:** FAIL (2), Action Decision Ambiguity. Destinations are named, there is no "I'll" self-action and writes are authorized, but the §2.1 Reading K fork changes writes: under A, 17 tickets go to Done and the reply is hold; under K, 8 go to Done, 52 to Canceled, the reply is keep and Brian is told the work goes on. No record settles which is right.

**Contrived / Unnatural:** PASS (5). No exact timestamps, opaque IDs, format rules, trap hints, hidden destinations, audit-form wording or if-chains. "he has to act on this, so give him one call, not a maybe" restates Leonard's "give me one audience call", and "no clear lead" still maps to a call (keep), so it does not hint at the trap. Long-horizon anti-inflation: each call answers a distinct question about a source-defined set of 60 sessions; no bulk result replaces the per-session reads and writes.

**Alignment with Today's Date:** PASS (5). "Monday" in Leonard's message resolves to Sep 29 (Robert's post). All sessions, mails, tickets and posts sit on or before 2025-09-30 21:10 UTC.

**Originality / Sample Similarity:** N/A (no comparison samples supplied). Dataset library check is distinct (STEP 0.6).

**Coherence (Bolt-on):** PASS (5). **Business Function:** PASS (5): a product decision on a game change maps to Product & Design.

## Phase 3: Universe Feasibility

**Data Existence:** entities verified 12 of 12 premises plus every rule record; all retrievable with cataloged tools (Drive/Docs/Sheets/Slides, Gmail, Slack, Linear, GitHub, Trello, Snowflake).

**Cross-Service Coherence:** PASS (5)
- Inconsistencies in task-touched data: none. The earlier minor Temporal Field Inconsistency is fixed. The gate doc (`f_748d26e760e54651eaa0d8`, SQL lines 4 and 134) no longer sends a Sep 24 reader to a PR that didn't exist yet. It now says Arthur "says what a pass does and doesn't cover", and its dated "Update Sep 30: Arthur opened his Vision Bot PR today" carries `modified_time` 2025-09-30T19:21:44Z (Drive and Docs rows agree). That is after PR #476 opened (2025-09-30T18:54:32Z, 11:54 PT, so "today" holds in PT) and before Arthur's coverage comment (2025-09-30T20:10:26Z). The PR's `updated_at` is moved to 20:10:26Z by SQL line 677. Body length 992 matches the style run.
- Base records checked against the overlay (REUSED, unchanged lines): 0.3.127 published on Android and required versions Android 0.3.127 / iOS 0.3.40 set 2025-09-23 (store builds); Jenkins "Match3D Android - #1943" (non-store build); Jenkins "Match 3D Vision Bot - #15 … Success" 2025-09-25; no base record shows an on-device Samsung pass; ZOM-559 open as the gate doc says. The bot post in #zombie-prs (SQL line 707) is by SLACK_BOT_0004, which authors 662 base messages in that channel.
- Snowflake USER_COHORT_RETENTION (the task depends on it): consistent with the KPI snapshot; the 2025-09-15 D14 / 2025-09-22 D7 cells are PLATFORM:FD-3785 (not scored). Robert's "cohorts that have a D14 figure" still picks one cohort set (9.09%).
- Known base-data issues (not scored): no listed synth-cut conflict is touched; keep the rubric and OEs off RAW_EVENTS app versions and time_in_status_minutes.
- Injection SQL considered: Yes. Static integrity evidence: REUSED from `0_injection.md` (injection-static-v2 PASS/COMPLETE on this SQL hash). Prompt-specific sources, access and configuration: supported.

## Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score | Justification |
|---|---|---|---|
| Prompt | Unique Ground Truth | 2 | Reading K (family, neighbor and classmate sessions under "gamer friends") is unsettled and flips hold to keep; B–J excluded |
| Prompt | Feasibility | 5 | Every ask maps to a cataloged write/read with existing data |
| Prompt | Persona ACL Reachability | 5 | All scoped reads are Julia's or shared with her |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 2 | Action Decision Ambiguity on the same fork: 9 ticket states, the reply and Brian's message change |
| Prompt | Contrived / Unnatural | 5 | Natural request; no hints, IDs, format rules or if-chains |
| Prompt | Alignment with Today's Date | 5 | All references before the clock |
| Prompt | Originality / Sample Similarity | N/A | No samples supplied; library check distinct |
| Prompt | Truthfulness | 5 | 12 premises verified (P3 recheck: none contradicted) |
| Prompt | Tool Use & Cross-service | 5 | Linear, Gmail, Docs, GitHub, Snowflake each change a graded fact |
| Prompt | Investigation + Action | 5 | Investigation feeds every write |
| Prompt | Coherence (Bolt-on) | 5 | No removable ask |
| Prompt | Persona | 5 | Julia owns the read |
| Prompt | Business Function | 5 | Product & Design |
| Prompt | Assigned Competency | 5 | Audience targeting is GTM work |
| Prompt | Assigned Task Skill | 5 | Analysis and synthesis is central |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three dimensions load-bearing; short trigger |
| Universe | Data Exists | 5 | All facts retrievable |
| Universe | Cross-Service Coherence | 5 | The gate-doc date slip is fixed; no inconsistency in task-touched data |

### Issues Found

| # | Issue | Severity | Dimension |
|---|-------|----------|-----------|
| 1 | Leonard's feedback note (base #zombie-design `/537`, 2025-09-22) asks for feedback from "25–45 casual and/or RPG gamer friends (not kids). No coaching". The 60 notes docs record relation as friend (28), family (10), neighbor (7), classmate (6) or "Kadıköy ekibi" (9). No persona-visible record says whether family, neighbor or classmate sessions count. Nine counted sessions are affected (family: ZOM-589, 599, 600, 623; neighbor: ZOM-597; classmate: ZOM-605, 625, 626, 627). Dropping them leaves 4 casual (3.75) and 4 RPG (3.5) counted sessions, under the deck's "At least 6 counted sessions per audience", which gives no clear lead and so keep. Reading A already applies the same sentence's "No coaching" to drop Claire's group, so the stricter reading is a fair one. | Major (FAIL) | Unique Ground Truth; Clarity (Action Decision Ambiguity) |

### Recommended Improvements

1. **Fix issue 1 in the data (required).** Add one dated, persona-visible record that says how the relation field is treated. Name each relation value the notes docs use (family, neighbor and classmate), and keep the game-industry exclusion intact for the "Kadıköy ekibi" sessions. The natural place is a short Leonard reply or post in #zombie-design (C090N54TG79; Leonard EMPLOYEE_0038 and Julia are members). Date it after the note (2025-09-22 05:01 UTC) and before his 2025-09-30 21:10 UTC request, and have it say it holds for sessions already run, the way his game-industry post does. If he says those relations count, the leading answer (hold, 17 Done) stands. The other way to fix it is to change the nine notes docs' relation to friend, but that removes variety without adding a rule. Don't fix it with a prompt line.
2. **Optional hardening (not scored).** ZOM-600 (age 25) and ZOM-626 (age 45) sit exactly on the ends of "25–45 years old". This review settles them as in, because the record names both ends as the band's limits. Moving those two ages inside the band in their notes docs would close off the endpoint argument.
3. **For the OE/rubric stages, after the fix:** grade the panel as one average, 3.33 over 9 ratings (Leonard: "average what's left"), and retention as 9.09% (Robert: "cohorts that have a D14 figure"). The snapshot's 8.63 and the per-run panel figures are decoys. Put the re-run notes on the tickets (Leonard: "close the tickets the way your log note says. Robert already told you how not-counted sessions get handled").
4. After changing the SQL, rerun /injection, /prompt, /hardness, /oe and /rubric, in that order.

## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5) subagents at this session's effort, each blind to the main review.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 7 sentences, 60 sessions, 17 forks | 3 | 1 |
| P2 | 7 sentences, all services, access, injected-record timing, Snowflake derived columns | 1 (platform) | 0 (1 platform note) |
| P3 | 7 sentences, all premises, injection integrity | 0 | 0 |
| P4 | 7 sentences | 0 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P1 | "the friend sessions, the ones that came out of his feedback note" | base #zombie-design `/537` "get real-life feedback from 25–45 casual and/or RPG gamer friends (not kids). No coaching"; notes docs ZOM-589/599/600/623 "Relation: family", ZOM-597 "Relation: neighbor", ZOM-605/625/626/627 "Relation: classmate"; criteria deck "At least 6 counted sessions per audience." | §2 boundary items | Unique Ground Truth | CONFIRMED | No persona-visible record speaks to relation. Leonard's "the friend sessions are in your workbook now" says where the sessions are, not which ones count, and his later rule posts, the deck and the log note are silent on it. Recorded as Reading K, UNRESOLVED_MATERIAL_DIFFERENCE, plus 9 BOUNDARY sweep items. Clarity fails on the same fork. |
| DR2 | P1 | "the friend sessions, the ones that came out of his feedback note" | Slack 12b40a5b… "age. 25–45 years old, not a headcount"; ZOM-600 "Age: 25"; ZOM-626 "Age: 45" | §2 edge values | Unique Ground Truth | REJECTED | The record names 25 and 45 as the band's own limits ("25–45 years old"), so both ends are members. Hardening suggested anyway (Recommended Improvements 2). |
| DR3 | P1 | "close out the session tickets" | Robert DM 167dc58a… "put a re-run note on it so the observer runs it again" | §2 writes | Clarity | REJECTED | Leonard ties Robert's handling to the ticket close-out: "close the tickets the way your log note says. Robert already told you how not-counted sessions get handled" (SQL line 705), and the log note says "each session gets a ZOM ticket". The note goes on the ticket. |
| DR4 | P2 | "write the memo he asked for and put it in my drive folder" | USER_COHORT_RETENTION 2025-09-15 d14_ret 5.83 / 7.17 | §3 derived columns | PLATFORM:FD-3785 | REJECTED | Known platform defect, not scored. Robert's maturity test ("cohorts that have a D14 figure") picks one set, giving 9.09%. |

Effect on verdict: UGT 5 → 2 and Clarity 5 → 2 (DR1). Cross-Service Coherence 3 → 5, because the gate-doc date slip is fixed (main review). Every other dimension is unchanged.

- F1: Relation under "gamer friends" (ZOM-589, 597, 599, 600, 605, 623, 625, 626, 627) | counted, Done, hold | not counted, Canceled, 4 v 4 under the minimum of 6, keep | Missing: a dated, persona-visible record (for example from Leonard in #zombie-design) saying whether family, neighbor and classmate sessions count
- F2: Samsung sessions (ZOM-587, 588, 590, 591, 593, 594, 596, 601, 603, 606, 620) | not counted, Canceled, re-run note | counted via ZOM-567 | Settled by: gate doc "A pass covers a device only if it ran on that device." and Arthur on #476 "no phone in the loop"
- F3: Claire's 13 sessions (ZOM-607–619) | not counted, Canceled, no re-run | counted per her form | Settled by: Claire 2025-09-29 "Before anyone touched their phone I sat them all down and took them through how ZM plays" and the note "No coaching, just observe and collect honest reactions."
- F4: Brian's 9 sessions (ZOM-568–576) | not counted, Canceled, no re-run | counted (ran before the rule) | Settled by: Leonard "that goes for sessions already run too" and Brian's DM "Kadıköy ekibi komple oyun sektöründen"
- F5: Robert's 10 sessions (ZOM-577–586) | not counted, Canceled, re-run note | counted (0.3.127) | Settled by: Leonard "careful with android 1943 … it never went through a store" and gate doc "Sessions on dev builds do not count."
- F6: Builds 0.3.127 (127), 0.3.40 (40), 0.3.38 (38) | store builds | dev builds | Settled by: #zombie-match3d `/407` "Android: 0.3.127" / "iOS: 0.3.40"; only 1943 is named as never going through a store
- F7: Re-run scope and where the note goes | technical drops Canceled with a re-run comment on the ticket | no notes, or the note in the register | Settled by: Robert "If one gets dropped for a technical reason, device or build, put a re-run note on it" and Leonard "close the tickets the way your log note says. Robert already told you how not-counted sessions get handled"
- F8: Age-band ends (ZOM-600, ZOM-626) | counted, Done | not counted | Settled by: Leonard "age. 25–45 years old"
- F9: Panel figure | 3.33 | 3.40 / 3.25 per run, or 3.1 with player 8 | Settled by: Leonard "if a rating is void it comes out of both the sum and the count, so you average what's left"
- F10: Retention figure | 9.09% | 8.63% snapshot, or 9.05% without 2025-09-15 | Settled by: Robert "install-weighted D7, not a simple mean of the cohorts. Mature cohorts only, meaning cohorts that have a D14 figure"
- F11: Memo destination | Julia's root folder with the log note | another folder | Settled by: card "memo goes in Julia's folder with her log note"
- F12: Brian message content | follows the call | — | Settled by: Leonard's keep/hold mapping plus Robert 2025-09-29 "will make the changes in the tutorial … shuffle the levels"
- F13: Marcus's resent form | 3 sessions | 6 | Settled by: Marcus "Same sessions as before"
- F14: ZOM-567 in the session set | not a session ticket | a session | Settled by: Log tab rows ZOM-568 to ZOM-627 only

Platform defects: PLATFORM:FD-3785 (USER_COHORT_RETENTION 2025-09-15 D14 and 2025-09-22 D7 cells filled before a window closes; the task's figure follows Robert's presence-of-D14 rule, so it does not create a fork).

### FINAL VERDICT: FAIL

Score: 2

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Eval version: task-quality-v1

Eval release SHA-256: b9281224e0e101faab431b7e10f928a29b8c6f02ebd52037b8aaa26ca5f9fc8c

Reviewed prompt SHA-256: 729d3623902ef87c67c5350fa319d715a57d65f45aecc62c03c2b0c2fbb053cc

Review context SHA-256: bb4c49776110dfb286b8a9303962f5af9b9be640ccb0a120bcd3e09473ced4f4

Prompt record SHA-256: 4a9364527d8244136dcfa9bfd67280b23f8d787e6f9108492017822fee9d8136

Next action: In the injection SQL, add a dated record from Leonard in #zombie-design saying whether family, neighbor and classmate sessions count (Recommended Improvements 1). Then rerun /injection, /prompt, /hardness, /oe and /rubric.

Evidence limits: Tool result rendering is not in the catalog (no return schemas); raw values and derivations were verified instead. Schema snapshot unverified (Eval 0 advisory).

**Lowest Dimension:** Prompt – Unique Ground Truth – 2 – nothing says whether family, neighbor and classmate sessions meet the note's "gamer friends" condition, and the answer flips from hold to keep.

**Summary:** The gate-doc date slip from the last round is fixed, and every other trap is still settled by a dated, persona-visible record. But the feedback note's "gamer friends" wording, set against the relation field (family, neighbor, classmate), leaves 9 counted sessions unsettled. Dropping them takes both audiences below 6 counted sessions and turns hold into keep, so UGT and Clarity fail until a record settles it.
