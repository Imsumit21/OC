## PROMPT EVALUATION REPORT

### Task: Julia closes out Leonard's friend-session audience read (60 sessions) and posts the keep/hold call on the cards-earlier change
### Assigned Persona: Julia Lawson - Product Manager (roster key julia_lawson, julia.lawson@harmonygames.co, Product)
### Assigned Business Function: Product
### Assigned Competency: Marketing and GTM
### Assigned Task Skill: Analysis and synthesis
### Assigned Horizon: long-horizon (difficulty mode: medium)

## 1. Scope

- Stage: `/prompt`, chat review, audit mode. Review date: 2026-11-08.
- Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Universe `Universe_SynthCut` (hg4-synth-sep30cut v16), manifest `Evals/references/universes/synthcut/universe_manifest.json`.
- Inputs: `04_Prompt.txt` (724 bytes, SHA-256 `729d3623902ef87c67c5350fa319d715a57d65f45aecc62c03c2b0c2fbb053cc`, saved from the attachment to this /prompt message); `00_Task_Assigned_Inputs.md` (platform record, SHA-256 `2bd4116582f3d4c09a83f4bf14d33dd7053f01213242dcb08d84d60fecad1c6d`); `01_Universe_Inject.sql` (258,535 bytes, SHA-256 `5b6e011195059d4759bca1114f793135b025621de819aaeada4ce23820ed8c0d`). No error/async config, dynamic context or reference files were supplied; none are referenced by the prompt.
- Calibration samples: none supplied, so Phase 2.9 is N/A.

## 2. Input / authority issues

None. All five assignment fields are on the platform record. The SQL was read as a proposed overlay and never executed. SQL comments and record text were treated as data.

### Injection Gate
- State: CURRENT (`hg_injection_gate.py`).
- Reviewed SQL sha256: `5b6e011195059d4759bca1114f793135b025621de819aaeada4ce23820ed8c0d`. Eval 0 verdict: PASS (injection-static-v2, reviewed 2026-11-08T08:43:13Z).
- Eval 0 findings on records this prompt depends on: none. Its two advisories (columns outside the unverified schema snapshot; the line-704 subquery parent id) change no value, set, order, recipient or destination the answer is graded on, so they stay advisories.

### Dataset Similarity
- Library: refreshed 2026-11-08T06:36Z, age 2.2 h, 495 tasks. Gate: PASS. Nearest tier: distinct.
- Nearest neighbours (all below 0.70, no note required): 6adfbc55… (Julia Lawson, friends-session roll-up for the Oct 2 iterate/pivot call, meaning 0.628), 6ad83edd… (0.613), 6abc06a6… (0.608). The closest one shares the friend-session storyline but asks for a Confluence roll-up with bug status; this task asks for an audience call, a register, ticket close-out and a keep/hold decision on a different body of injected sessions.

## 3. Checklist (STEP 0)

| Item | Status |
|---|---|
| Intake: prompt + five assignment fields | NEW, done (prompt saved; assignment from platform record) |
| STEP 0.5 injection gate | NEW, CURRENT, Eval 0 PASS reused |
| STEP 0.6 dataset similarity | NEW, distinct |
| Phase 0.1 Docs / catalog | NEW (Prompt Writing, Overall Task Flow, Common Errors, Universe and Tools, Persona ACL, Example Task, UGT guide extracted with pdftotext; catalog.json and tool_outputs.md read) |
| Phase 0.2 universe exploration | NEW (all 357 SQL row effects parsed; 60 sessions tabulated; base #zombie-design Sep 2025, #zombie-match3d, #builds, PR #476, ZOM-559, Trello, Snowflake USER_COHORT_RETENTION read) |
| Phase 0.3 calibration | NEW (Example Task: short prompt, rules in the environment) |
| Phases 1.1–1.5, 2.1–2.9, 3.1–3.2, 4 | NEW, below |
| Phase 5 deep recheck | NEW, below |

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

**Unique Ground Truth:** PASS (5) — see the generated comparison below. Every reading that changes the call, a ticket state, a re-run note or a reported figure is excluded by a dated, persona-visible record that names the item or its kind of case.

### Unique Ground Truth comparison

Unique Ground Truth: PASS 5

Basis: Every alternative that changes the keep/hold call, a ticket state, a re-run note or a reported figure is ruled out by a dated, persona-visible rule record that names the item or its kind of case; all 60 sessions have a record-settled outcome.

Alternative selection: Each trap in the data was turned into the strongest reading that a careful agent could defend: the Done ZOM-567 ticket, Claire's no-coaching form, the session timing before the game-industry rule, the 0.3.127 version string, the re-run/close-out handling, the per-run panel figures, the snapshot retention mean and the age-band endpoints.

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

Explicit option inventory: The prompt offers keep or hold and Leonard's message offers casual, RPG or no clear lead; every option is mapped.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "with keep or hold"; L (Evals/task\_inputs/01\_Universe\_Inject.sql lines 705-705): "casual, RPG or no clear lead"

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| hold | RETAINED | A | Leading reading: casual lead means hold. Evidence: P (Evals/task\_inputs/04\_Prompt.txt): "keep or hold" |
| keep | EXCLUDED | B, C, D, E | Keep follows only from readings B to E, each excluded by a quoted rule. Evidence: P (Evals/task\_inputs/04\_Prompt.txt): "keep or hold" |
| casual lead | RETAINED | A | 9 casual vs 8 RPG counted sessions, gap 0.46. Evidence: L (Evals/task\_inputs/01\_Universe\_Inject.sql lines 705-705): "casual, RPG or no clear lead" |
| RPG lead | EXCLUDED | B, C, D, E | Only reached by counting sessions the rules drop. Evidence: L (Evals/task\_inputs/01\_Universe\_Inject.sql lines 705-705): "casual, RPG or no clear lead" |
| no clear lead | EXCLUDED | E | The closest gap to 0.25 is reading E (0.27, still an RPG lead); the leading gap is 0.46. Evidence: L (Evals/task\_inputs/01\_Universe\_Inject.sql lines 705-705): "casual, RPG or no clear lead" |

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
| ZOM-589 | ZOM-589: counted (RPG, 3 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-589 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 180-180): "Build: 0.3.127 (127)"; DOC\_ZOM-589 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 180-180): "Relation: family"; CMT\_ZOM-589 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 596-596): "device for this one: Pixel 7a"; REQV2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "Android: 0.3.127"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-590 | ZOM-590: not counted, Samsung phone (played on an SM-S921B) with no on-device pass -&gt; Canceled with a re-run note | RECORD | CMT\_ZOM-590 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 598-598): "played on an SM-S921B"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "no phone in the loop"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-591 | ZOM-591: not counted, Samsung phone (Galaxy S23 FE) with no on-device pass -&gt; Canceled with a re-run note | RECORD | CMT\_ZOM-591 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 600-600): "Galaxy S23 FE"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "no phone in the loop"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-592 | ZOM-592: counted (RPG, 3.5 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-592 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 186-186): "Build: 0.3.40 (40)"; DOC\_ZOM-592 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 186-186): "Relation: friend"; CMT\_ZOM-592 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 602-602): "on an iPhone 12"; REQV3 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "iOS: 0.3.40"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-593 | ZOM-593: not counted, Samsung phone (phone was a Galaxy A54) with no on-device pass -&gt; Canceled with a re-run note | RECORD | CMT\_ZOM-593 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 604-604): "phone was a Galaxy A54"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "no phone in the loop"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-594 | ZOM-594: not counted, Samsung phone (phone: Galaxy S22) with no on-device pass -&gt; Canceled with a re-run note | RECORD | CMT\_ZOM-594 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 606-606): "phone: Galaxy S22"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "no phone in the loop"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-595 | ZOM-595: counted (casual, 4 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-595 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 192-192): "Build: 0.3.127 (127)"; DOC\_ZOM-595 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 192-192): "Relation: friend"; CMT\_ZOM-595 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 608-608): "device for this one: OnePlus 11"; REQV2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "Android: 0.3.127"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-596 | ZOM-596: not counted, Samsung phone (played on a Galaxy A15) with no on-device pass -&gt; Canceled with a re-run note | RECORD | CMT\_ZOM-596 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 610-610): "played on a Galaxy A15"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "no phone in the loop"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-597 | ZOM-597: counted (RPG, 3 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-597 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 196-196): "Build: 0.3.127 (127)"; DOC\_ZOM-597 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 196-196): "Relation: neighbor"; CMT\_ZOM-597 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 612-612): "Pixel 8"; REQV2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "Android: 0.3.127"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-598 | ZOM-598: counted (RPG, 3.5 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-598 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 198-198): "Build: 0.3.127 (127)"; DOC\_ZOM-598 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 198-198): "Relation: friend"; CMT\_ZOM-598 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 614-614): "on a Pixel 8"; REQV2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "Android: 0.3.127"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-599 | ZOM-599: counted (RPG, 3.5 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-599 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 200-200): "Build: 0.3.40 (40)"; DOC\_ZOM-599 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 200-200): "Relation: family"; CMT\_ZOM-599 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 616-616): "phone was an iPhone 14"; REQV3 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "iOS: 0.3.40"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-600 | ZOM-600: counted (casual, 4 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-600 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 202-202): "Build: 0.3.40 (40)"; DOC\_ZOM-600 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 202-202): "Relation: family"; CMT\_ZOM-600 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 618-618): "phone: iPhone 13"; REQV3 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "iOS: 0.3.40"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-601 | ZOM-601: not counted, Samsung phone (device for this one: Galaxy A35) with no on-device pass -&gt; Canceled with a re-run note | RECORD | CMT\_ZOM-601 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 620-620): "device for this one: Galaxy A35"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "no phone in the loop"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-602 | ZOM-602: counted (casual, 4 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-602 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 206-206): "Build: 0.3.40 (40)"; DOC\_ZOM-602 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 206-206): "Relation: friend"; CMT\_ZOM-602 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 622-622): "played on an iPhone 14"; REQV3 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "iOS: 0.3.40"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-603 | ZOM-603: not counted, Samsung phone (SM-A346E) with no on-device pass -&gt; Canceled with a re-run note | RECORD | CMT\_ZOM-603 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 624-624): "SM-A346E"; GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 134-134): "A pass covers a device only if it ran on that device."; ARTH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 676-676): "no phone in the loop"; RDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 701-701): "If one gets dropped for a technical reason, device or build, put a re-run note on it" |
| ZOM-604 | ZOM-604: counted (RPG, 3.5 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-604 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 210-210): "Build: 0.3.40 (40)"; DOC\_ZOM-604 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 210-210): "Relation: friend"; CMT\_ZOM-604 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 626-626): "on an iPhone 15"; REQV3 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "iOS: 0.3.40"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-605 | ZOM-605: counted (casual, 3.5 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-605 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 212-212): "Build: 0.3.40 (40)"; DOC\_ZOM-605 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 212-212): "Relation: classmate"; CMT\_ZOM-605 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 628-628): "phone was an iPhone 14"; REQV3 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "iOS: 0.3.40"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
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
| ZOM-623 | ZOM-623: counted (RPG, 3.5 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-623 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 248-248): "Build: 0.3.127 (127)"; DOC\_ZOM-623 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 248-248): "Relation: family"; CMT\_ZOM-623 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 664-664): "phone was a Redmi Note 13"; REQV2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "Android: 0.3.127"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-624 | ZOM-624: counted (RPG, 3.5 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-624 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 250-250): "Build: 0.3.40 (40)"; DOC\_ZOM-624 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 250-250): "Relation: friend"; CMT\_ZOM-624 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 666-666): "phone: iPhone 15"; REQV3 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "iOS: 0.3.40"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-625 | ZOM-625: counted (casual, 4 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-625 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 252-252): "Build: 0.3.127 (127)"; DOC\_ZOM-625 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 252-252): "Relation: classmate"; CMT\_ZOM-625 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 668-668): "device for this one: Pixel 7"; REQV2 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "Android: 0.3.127"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-626 | ZOM-626: counted (casual, 4 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-626 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 254-254): "Build: 0.3.40 (40)"; DOC\_ZOM-626 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 254-254): "Relation: classmate"; CMT\_ZOM-626 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 670-670): "played on an iPhone 13"; REQV3 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "iOS: 0.3.40"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |
| ZOM-627 | ZOM-627: counted (casual, 4 stars) -&gt; Done, no re-run note | RECORD | DOC\_ZOM-627 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 256-256): "Build: 0.3.40 (40)"; DOC\_ZOM-627 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 256-256): "Relation: classmate"; CMT\_ZOM-627 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 672-672): "iPhone 15"; REQV3 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C0880U9751A/2025-09.json pointer /407/text): "iOS: 0.3.40"; LOG (Evals/task\_inputs/01\_Universe\_Inject.sql lines 136-136): "counted goes to Done" |

Strongest-alternative challenge (B): ZOM-567 is a Done Linear ticket from an engineer saying the Vision Bot green covers the Samsung device gate; it is the most authoritative-looking record for counting the 11 Samsung sessions, and counting them flips the call to keep.
Challenge evidence: Z567C (Evals/task\_inputs/01\_Universe\_Inject.sql lines 552-552): "that run covers the device gate for the Samsung group"

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

**Clarity & Specificity:** PASS (5). One request, named destinations, no "I'll" self-action, explicit authorization to write. Every write-diverging reading tested in §2.1 is settled by a record, so there is no Action Decision Ambiguity.

**Contrived / Unnatural:** PASS (5). No exact timestamps, opaque IDs, format rules, trap hints, hidden destinations, audit-form wording or if-chains. "he has to act on this, so give him one call, not a maybe" restates Leonard's "give me one audience call", and "no clear lead" still maps to a call (keep), so it does not hint at the trap. Long-horizon anti-inflation: each call answers a distinct question about a source-defined set of 60 sessions; no bulk result replaces the per-session reads and writes.

**Alignment with Today's Date:** PASS (5). "Monday" in Leonard's message resolves to Sep 29 (Robert's post). All sessions, mails, tickets and posts sit on or before 2025-09-30 21:10 UTC.

**Originality / Sample Similarity:** N/A (no comparison samples supplied). Dataset library check is distinct (STEP 0.6).

**Coherence (Bolt-on):** PASS (5). **Business Function:** PASS (5): a product decision on a game change maps to Product & Design.

## Phase 3: Universe Feasibility

**Data Existence:** entities verified 12 of 12 premises plus every rule record; all retrievable with cataloged tools (Drive/Docs/Sheets/Slides, Gmail, Slack, Linear, GitHub, Trello, Snowflake).

**Cross-Service Coherence:** NON-FAIL (3)
- Inconsistencies in task-touched data: one, Temporal Field Inconsistency (minor, confirmed in the deep recheck, DR P2-1). The injected Google Doc "ZM session stability gate" (`f_748d26e760e54651eaa0d8`, created 2025-09-24T15:12:40Z, modified 2025-09-24T15:30:02Z, SQL lines 4 and 134) says "What a pass does and doesn't cover gets discussed on his Vision Bot PR." The only Vision Bot PR, `harmonygames-Games/match3d#476` (base GitHub `/pull_requests/2381`, head_ref `Blake/visionBot`), was created 2025-09-30T18:54:32Z, so the Sep 24 doc points at a PR opened six days later. The coverage comment the answer needs (injected `#476#rc_27`, 2025-09-30T20:10:26Z) is later than both. It changes no count, order or window the answer uses, so under the date-slip rule it is one minor inconsistency, not a fail.
- Base records checked against the overlay: 0.3.127 published on Android by 2025-09-22 21:04 UTC and required versions Android 0.3.127 / iOS 0.3.40 set 2025-09-23 (store builds); Jenkins "Match3D Android - #1943" built 2025-09-22 21:12 UTC (consistent with a non-store build); Jenkins "Match 3D Vision Bot - #15 … Success" 2025-09-25 (consistent with ZOM-567's "run #15 came back green"); no base record shows an on-device Samsung pass (Linear, GitHub and September Slack searched for Samsung/Galaxy/Vision); ZOM-559 open as the gate doc says.
- Snowflake USER_COHORT_RETENTION (the task depends on it): 242 rows; comment's D1 range 0.0–75.0% and unweighted mean 24.8% match the rows (24.78%); zombie_match_3d NULL pattern is consistent with windows measured from the cohort week (09-15 has D14, 09-22 has D7 but no D14, 09-29 has D1 only). The KPI snapshot's 45 rows equal the table (Eval 0). No contradiction.
- Known base-data issues (not scored): none of the listed synth-cut conflicts (SC-1…SC-73) is touched. SC-19 (telemetry app versions) and SC-22 (time_in_status_minutes) are nearby but unused; keep the rubric and OEs off RAW_EVENTS app versions and off time_in_status_minutes.
- Injection SQL considered: Yes. Static integrity evidence: REUSED from `0_injection.md` (injection-static-v2 PASS/COMPLETE, same SQL hash, checks A–C incl. channel-membership and doubled apostrophes). Prompt-specific sources, access and configuration: supported.

## Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score | Justification |
|---|---|---|---|
| Prompt | Unique Ground Truth | 5 | Generated comparison: readings B–J all EXCLUDED by quoted records; 60-item sweep all RECORD |
| Prompt | Feasibility | 5 | Every ask maps to a cataloged write/read with existing data |
| Prompt | Persona ACL Reachability | 5 | All scoped reads are Julia's or shared with her |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 5 | Named destinations; no write-divergent reading survives |
| Prompt | Contrived / Unnatural | 5 | Natural request; no hints, IDs, format rules or if-chains |
| Prompt | Alignment with Today's Date | 5 | All references before the clock |
| Prompt | Originality / Sample Similarity | N/A | No samples supplied; library check distinct |
| Prompt | Truthfulness | 5 | 12 premises verified |
| Prompt | Tool Use & Cross-service | 5 | Linear, Gmail, Docs, GitHub, Snowflake each change a graded fact |
| Prompt | Investigation + Action | 5 | Investigation feeds every write |
| Prompt | Coherence (Bolt-on) | 5 | No removable ask |
| Prompt | Persona | 5 | Julia owns the read |
| Prompt | Business Function | 5 | Product & Design |
| Prompt | Assigned Competency | 5 | Audience targeting is GTM work |
| Prompt | Assigned Task Skill | 5 | Analysis and synthesis is central |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three dimensions load-bearing; short trigger |
| Universe | Data Exists | 5 | All facts retrievable |
| Universe | Cross-Service Coherence | 3 | One minor temporal inconsistency: the Sep 24 gate doc refers to discussion on PR #476, opened Sep 30 |

### Issues Found

| # | Issue | Severity | Dimension |
|---|-------|----------|-----------|
| 1 | The Sep 24 "ZM session stability gate" doc (SQL lines 4 and 134) sends readers to "his Vision Bot PR", but PR #476 was created 2025-09-30T18:54:32Z. | Minor (NON-FAIL) | Cross-Service Coherence |

### Recommended Improvements

1. **Fix issue 1 (required for a PASS).** Make the doc's PR pointer postdate the PR. One coherent way: keep the Sep 24 body, add a dated update line to the doc's `body_text` saying that since Sep 30, what a pass does and doesn't cover is discussed on Arthur's Vision Bot PR #476, and move `modified_time` on both the `gdrive.drive_files` row (SQL line 4) and the `gdocs.docs_documents` row (SQL line 134) to a time after 2025-09-30T18:54:32Z and before 2025-09-30T20:10:26Z (Arthur's comment), so the update sits before the comment it points to. Another way is to drop the PR sentence and name Arthur Blake as the person who decides what a pass covers, but that removes the doc's pointer to the comment, so the first fix keeps discovery intact.
2. **Optional hardening (not scored):** ZOM-600 (age 25, notes doc `f_e0843c039ea62e1a61179e`) and ZOM-626 (age 45, notes doc `f_69e935f38bc4f701a82307`) sit exactly on the ends of Leonard's "25–45 years old". The record names both ends, so this review settles them as in. Moving those two ages inside the band in the notes docs would remove any argument about endpoints without changing the call.
3. **For the OE/rubric stages:** grade the panel as one average, 3.33 over 9 ratings (Leonard: "average what's left"), and retention as 9.09% (Robert: "cohorts that have a D14 figure"); the snapshot's 8.63 and per-run panel figures are decoys. Don't make the Brian message's placement (channel post vs a mention inside Leonard's thread) a graded point beyond "in #zombie-design".
4. Dataset similarity: no action (distinct).

## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5) subagents at this session's effort, each blind to the main review.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 7 sentences, 60 sessions, 81 fork lines | 4 | 0 |
| P2 | all sentences, services, access, Snowflake derived columns | 2 | 1 (plus 1 platform note) |
| P3 | 8 sentences, 19 claims, SQL checks | 1 | 0 |
| P4 | 7 sentences | 0 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P1 | "close out the session tickets" | Slack 12b40a5b… "age. 25–45 years old, not a headcount"; ZOM-600 notes doc "Age: 25"; ZOM-626 notes doc "Age: 45" | §2 edge values | Unique Ground Truth | REJECTED | The record states the band as "25–45 years old", naming 25 and 45 as its ends, and the note's only other limit is "(not kids)"; a 25- or 45-year-old is inside the stated range. The call is hold either way. Optional hardening in Recommended Improvements 2. |
| DR2 | P1 | "write the memo he asked for" | Gmail fwd "Player 8''s rating is void"; Slack 7b38bd64… | §2 which number | Unique Ground Truth | REJECTED | Leonard's rule is for "the panel": "stars per player, one number each … so you average what's left", one average over the remaining 9 ratings = 3.33; the per-run split is not the panel read he set. |
| DR3 | P1 | "write the memo he asked for" | Slack 2ca968ac… "cohorts that have a D14 figure"; USER_COHORT_RETENTION 2025-09-15 d14_ret 5.83 / 7.17 | §2 edge values | Unique Ground Truth | REJECTED | Robert's maturity test is presence of a D14 figure, which the 2025-09-15 rows meet, so 9.09% (47 rows, 6,040 installs). Recorded as reading J, EXCLUDED. Platform note below. |
| DR4 | P1 | "tell brian in #zombie-design whether the tutorial and level order work goes on." | Slack b07f1e10… "tell <@EMPLOYEE_0026_SLACK_ID> in this channel" | §2 destination | Clarity | REJECTED | The prompt separates "reply to him in his thread" from "tell brian in #zombie-design", which points to a channel post; a thread mention would still reach the same person in the same channel with the same content. |
| DR5 | P2 | "his message lays out what he needs and where the rules are." | Doc f_748d26e760e54651eaa0d8 (2025-09-24) "gets discussed on his Vision Bot PR"; GitHub match3d#476 created_at 2025-09-30T18:54:32Z | §3 date slip | Cross-Service Coherence | CONFIRMED | Opened both records: the PR is the only Vision Bot PR and postdates the doc by six days. No count, order or window changes, so minor (NON-FAIL). |
| DR6 | P2 | (Snowflake, retention) | USER_COHORT_RETENTION 2025-09-15 D14, 2025-09-22 D7 | §3 derived columns | PLATFORM:FD-3785 | REJECTED | Platform defect, not scored; the answer follows Robert's rule to one figure. |
| DR7 | P3 | (SQL column lists) | schema snapshot lacks slides_pages.notes, slides_page_elements.table_json/ordinal, linear_comments.sequence, github_reviews.seq, github_review_comments.seq | §6.8 SQL | Injection advisory | REJECTED | Same advisory as Eval 0; the snapshot is unverified and these columns carry no graded value. Stays in the Injection Gate section. |

Effect on verdict: Cross-Service Coherence 5 → 3 (DR5). UGT, Clarity and every other dimension unchanged.

- F1: Audience call | casual lead, hold | RPG lead, keep | Settled by: criteria deck "The lead is the higher mean star rating over counted sessions." and Leonard "casual lead means we hold the change"
- F2: Samsung sessions (ZOM-587, 588, 590, 591, 593, 594, 596, 601, 603, 606, 620) | not counted, Canceled, re-run note | counted via ZOM-567 | Settled by: gate doc "A pass covers a device only if it ran on that device." and Arthur on #476 "no phone in the loop"
- F3: Claire's 13 sessions (ZOM-607–619) | not counted, Canceled, no re-run | counted per her form | Settled by: Claire 2025-09-29 "Before anyone touched their phone I sat them all down and took them through how ZM plays" and the note "No coaching, just observe and collect honest reactions."
- F4: Brian's 9 sessions (ZOM-568–576) | not counted, Canceled, no re-run | counted (ran before the rule) | Settled by: Leonard "that goes for sessions already run too" and Brian's DM "Kadıköy ekibi komple oyun sektöründen"
- F5: Robert's 10 sessions (ZOM-577–586) | not counted, Canceled, re-run note | counted (0.3.127) | Settled by: Leonard "careful with android 1943 … it never went through a store" and gate doc "Sessions on dev builds do not count."
- F6: Re-run scope and close-out | technical drops Canceled with a re-run note, others Canceled only | no notes / Samsung left open | Settled by: Robert "If one gets dropped for a technical reason, device or build, put a re-run note on it" and log note "not counted goes to Canceled."
- F7: Age-band ends (ZOM-600, ZOM-626) | counted, Done | not counted | Settled by: Leonard "age. 25–45 years old"
- F8: Panel figure | 3.33 | 3.40 / 3.25 per run, or 3.1 with player 8 | Settled by: Leonard "if a rating is void it comes out of both the sum and the count, so you average what's left"
- F9: Retention figure | 9.09% | 8.63% snapshot, or 9.05% without 2025-09-15 | Settled by: Robert "install-weighted D7, not a simple mean of the cohorts. Mature cohorts only, meaning cohorts that have a D14 figure"
- F10: Memo destination | Julia's root folder with the log note | another folder | Settled by: card "memo goes in Julia's folder with her log note"
- F11: Brian message content | the work does not go on | goes on | Settled by: Leonard's hold mapping plus Robert 2025-09-29 "will make the changes in the tutorial … shuffle the levels"
- F12: Marcus's resent form | 3 sessions | 6 | Settled by: Marcus "Same sessions as before"

Platform defects: PLATFORM:FD-3785 (USER_COHORT_RETENTION 2025-09-15 D14 and 2025-09-22 D7 cells filled before a last-install-day window closes; the task's figure follows Robert's presence-of-D14 rule, so it does not create a fork).

### FINAL VERDICT: NON-FAIL

Score: 3

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Eval version: task-quality-v1

Eval release SHA-256: b9281224e0e101faab431b7e10f928a29b8c6f02ebd52037b8aaa26ca5f9fc8c

Reviewed prompt SHA-256: 729d3623902ef87c67c5350fa319d715a57d65f45aecc62c03c2b0c2fbb053cc

Review context SHA-256: ac784d41448b6c85a1a5627b799cffd4e6187a7809d79fc844924971ace59251

Prompt record SHA-256: 0a2b58292619881db8bc723e7c9301643a5fc2609285eb1f2effcb6867c157a3

Next action: Fix the stability-gate doc's PR reference (Recommended Improvements 1) in the injection SQL, then rerun /injection, /prompt, /hardness, /oe and /rubric.

Evidence limits: Tool result rendering is not in the catalog (no return schemas); raw values and derivations were verified instead. Schema snapshot unverified (Eval 0 advisory).

**Lowest Dimension:** Universe – Cross-Service Coherence – 3 – the Sep 24 gate doc refers to discussion on PR #476, opened Sep 30.

**Summary:** A strong, natural long-horizon prompt: 60 sessions, five seeded rules, and every trap flips the keep/hold call and is settled by a dated record Julia can open (17 counted sessions, casual 3.83 vs RPG 3.375, hold). The only defect is one minor date slip in the injected gate doc, which holds the prompt at NON-FAIL 3 until fixed.
