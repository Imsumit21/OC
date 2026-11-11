# Prompt Brief — julia_zm_audience_read · prep (rev7)
> Built 2026-11-09 from 00_Assigments.md, 00_Task_Context.json, 01_Universe_Inject.sql (rev7, sha256 3acbfad93f4a), 01_Grounding_Dossier.md (rev7 delta, clause sweep and injection gate current), 01_Scenario_Design.md, 01_Hardness_Manifest.json (rev7), 01_Gradable_Surface.json, Working_Files/solver/truth.json (rev7), 01a_Hardening_Report.md §9–§11 (prompt defect P1), 03_Error_Async_Config.txt (Friction: none, error-async gate re-run on rev7), 04_Prompt_Check.md (rev7 re-check) · Persona view verified: all (check-sql PASS on rev7, 0 load-bearing rows not visible)
> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human. The rev7 prompt (132 words, sha256 c3da944d7da5) was finalized before this re-bind; this brief re-binds the facts to rev7 and leaves the prompt unchanged.
> **Clock:** `Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)`. Julia's today is Wednesday 1 October 2025 (universe.persona_today). Seed bound 2025-10-01T00:00:00Z. The latest seeded event the prompt leans on is Leonard's ask C090N54TG79/1759266627.418203 (2025-09-30T21:10:27Z, Tue Sep 30 2:10 PM PT).

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
|---|---|---|
| Business function | Product → Product & Design (`Evals/references/rules/task_categories.md`) | a product decision on Zombie Match 3D: keep or hold the Sep 29 "cards earlier" change (C090N54TG79/1759172166.547199, "17 -> level 5") from player evidence |
| Persona / role | Julia Lawson, julia.lawson@harmonygames.co, Product Manager, Product (roster `julia_lawson`) | Voice: short, plain, lowercase is fine, no spec layout. Remit: she owns the workbook f_43bc35baf77fd59f4e57b8, the log note f_c691d577b8f837eb4f9eaa and the criteria deck f_a087f049d271e9aa9f567f, typed the session tickets ZOM-568 to ZOM-647, holds the players in her contacts for gift codes, and is the one Leonard asks (C090N54TG79/1759266627.418203 mentions EMPLOYEE_0005_SLACK_ID). Read scope: member of #zombie-design C090N54TG79 and #zombie-bugs C08R27X0EAH, her DMs with Brian D076RBM29JS and Robert D05GU6L0XFH, her own mailbox and calendar, Docs/Sheets/Slides she owns or that are shared with her |
| Competency | Marketing and GTM | an audience-fit read: which player audience (casual vs RPG) the game resonates with, from friend sessions, with the Playtestcloud panel and retention as context, feeding a go-to-market content decision. Before the freeze Julia already argues audience fit (C090N54TG79/1758569491.223089; role review in 00_V3_Authoring_Evidence.json) |
| Task skill | Analysis and synthesis | 82 sessions joined across ticket comments, notes Docs, form mails, a late mail, Contacts, DMs, a PR comment, a QA matrix and Snowflake into one audience call with the numbers behind it (R1–R14, 01_Hardness_Manifest.json); stacked: Actions (register, memo, 2 new tickets, 82 state writes, 13 re-run notes, two Slack messages) |
| Task type / tier | long-horizon (Long Horizon, 100–500+) | 12 services carry weight (Slack, Gmail, Docs, Slides, Sheets, Drive, Calendar, Trello, Linear, GitHub, Snowflake, Contacts) plus a supporting Confluence read; manifest call_budget 438 planned, 358 firm (80 conditional per-ticket reads count 0) (01_Hardness_Manifest.json; dossier L1207); `HARDNESS GATE (extreme): PASS` in 01_Grounding_Dossier.md L1294; volume exception recorded (`volume_exception`, floor 340, requester confirmed 2026-11-07, rev7 volume asked 2026-11-08) |
| Difficulty mode / date | medium (cap .85, never changed); October 1, 2025 07:00 → synth-cut | nothing first appearing after 2025-09-30 23:59:59 PT may be described as done; beta not shipped, interim read, Victor gone (SC-5, SC-36; rev7 replaced him as observer with Douglas, dossier rev7 delta) |

Known-data-issue cards the asks touch (`references/known_data_issues/synthcut.md`, via 01_Scenario_Design.md §1a): SC-5/36 (Victor: not named), SC-6 (Brian has no Gmail: the Brian message goes to Slack C090N54TG79), SC-7 (membership not graded), SC-8/16/30/32 (ZOM-559 state not proof), SC-19 (build names as Slack writes them, C05433XK267/1758803475.436309). No ask grades a value a card forbids.

### 1b · Asks that drive the call volume (brief only, never in the prompt)

| Prompt ask | What it forces per record | Calls (01_Hardness_Manifest.json call_budget) |
|---|---|---|
| "fill in the register tab in my audience sessions workbook" | a verdict for each of 82 sessions: one Linear comment list per ticket (device only there, e.g. cmt_2fbcaf2d990d8b4e9c0d), one notes Doc per ticketed session (build, age, relation only there, e.g. f_524278b67bfa30dde78699), Contacts for jobs (038b5eb5a30326895cb54756), and Owen's late mail for the two unticketed sessions | 80 + 80 + 4 + 4 Gmail batch reads |
| "close out the session tickets" | 2 new tickets for the late sessions per the log note f_c691d577b8f837eb4f9eaa, one state write per ticket (82), one re-run note per build drop per Robert's reply D05GU6L0XFH/1758913471.205816 (13) | 2 + 80 + 13 (+2 writes phase) |
| "the audience call" / "one call" | rules and reconciliation reads across #zombie-design, #zombie-bugs, the deck f_a087f049d271e9aa9f567f, the gate Doc f_748d26e760e54651eaa0d8, PR harmonygames-Games/match3d#476, the QA matrix f_cadae9f611d82d56ac02c3 | about 60 |
| "write the memo he asked for" | Trello card 68dc0acf1815df76ed9b887d, panel forward, retention rule, KPI tab note, Snowflake | about 25 incl. writes |
| per-ticket header read (conditional) | linear get per ticket if the bulk list truncates descriptions | 0 or 80 |

Firm 358, 438 with the conditional row. No ask was added to reach volume (padding is a failing error, Prompt Writing §2.4); the 20 extra sessions ZOM-628 to ZOM-647 are cohort volume in the universe, not prompt asks. The prompt states no count, step or service list.

### 1c · Style taken from the completed tasks (traits only; no content, phrase or structure copied)

| Trait | Taken from | How it shows here |
|---|---|---|
| Opens with who asked, where and when, in one clause | `support/completed_tasks/frederick_card_spend_q3_*/task_inputs/04_Prompt.txt`, `robert_winddown_closeout_2026-10-30/task_inputs/04_Prompt.txt` | "leonard asked me in #zombie-design" |
| One short paragraph, roughly 70–160 words, no lists | all five completed prompts (69–104 words) | one paragraph, 132 words |
| Lowercase, conversational register | `julia_zm_difficulty_baseline_2026-11-01`, `robert_winddown_closeout_2026-10-30` | lowercase throughout, clean spelling, no planted typos (learnings §4) |
| Destinations named plainly as the persona knows them | `douglas_beta_server_signoff_2026-10-28`, `frederick_account_handover_2026-10-26` | "the register tab in my audience sessions workbook", "my drive folder", "in his thread", "in #zombie-design" |
| Points at the requester's message rather than restating it | `douglas_beta_server_signoff_2026-10-28`, `frederick_card_spend_q3_*` | "his message says what he needs" (rev7: no longer says where the rules are, 01a §11 P1) |
| Closes with a delegation line so the agent acts | all five | "you don't need my ok on any of it, post and update everything under my name" |

Not copied: "take it off my plate", "go with your read on the details", "no need to check with me first", "everything it points to", "the way he laid it out", "as me", any register/folder/ticket wording specific to those tasks.

## 2 · Situation

| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |
|---|---|---|---|
| Leonard wants one audience call (casual, RPG or no clear lead) from the friend sessions to settle the cards earlier change, a memo per the roadmap card, keep or hold in his thread and a word to Brian | Julia, #zombie-design | C090N54TG79/1759266627.418203 (Tue Sep 30 2:10 PM PT; SQL L887) | none needed; the #zombie-prs mirror of the PR note is a non-member read and never load-bearing (GitHub harmonygames-Games/match3d#476#rc_27 is unscoped) |
| The sessions Julia logged tie out 80 for 80 against the tickets and lean RPG, as Robert and Leonard already believe | Julia, her workbook and the tickets | f_43bc35baf77fd59f4e57b8 Log tab (SQL L340, 80 rows); ZOM-568 to ZOM-647; base lean C090N54TG79/1759178344.878219 | — |
| The friend sessions come from Leonard's feedback note | Julia, #zombie-design | C090N54TG79/1758517286.431379 (Sun Sep 21 10:01 PM PT) | — |

No cause belongs here. Which sessions drop and why (coaching at Claire's, build 1943, Brian's group and two players' games jobs), why the Samsung sessions now count (Vincent's on-device QA matrix), and that two sessions sit only in Owen's late mail are discovery-only (§5, never in the prompt).

## 3 · Investigation → action

Questions to resolve (no answers here):
1. Which sessions exist in total, including any form that came in after the ticket batch?
2. Which of them count under the rules the team posted after the note and in the docs those rules point to, and for those that don't, why?
3. What audience label each session carries and how the lead is read?
4. Does the result give casual, RPG or no clear lead, and so keep or hold?
5. How each ticket closes, which new tickets are needed, and which dropped sessions get a re-run note?
6. What the memo holds, the panel read and the retention figure?

Writes they feed: W1 register rows (1–3) → W2 memo (1–4, 6) → W3a new tickets (1) → W3 82 ticket states + W4 re-run notes (2, 5) → W5 reply keep/hold (4) → W6 message to Brian (4). Every write depends on the session verdicts; none is a bolt-on, each is named in the ask C090N54TG79/1759266627.418203 or Julia's own log note f_c691d577b8f837eb4f9eaa.

## 4 · Pinned final state (UGT anchor)

The pinned state is Working_Files/solver/truth.json (rev7, regenerated on SQL 3acbfad93f4a; run_forensics/rev7/solver_check.txt OVERALL PASS).

| Deliverable | Required contents (requirements) | Destination (exact) | Recipient(s) (exact) | Catalog write (reference only; never in the prompt) | Fed by |
|---|---|---|---|---|---|
| W1 register | one row per session for all 82: ZOM-568 to ZOM-647 plus the two late sessions in julia.lawson@harmonygames.co/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com> (Ayşe Polat, Daniel Hughes; keyed by their new tickets); audience, stars, verdict, reason; 45 counted, 37 not counted (coached 13 ZOM-607–619; build 13 ZOM-577–586, ZOM-632, ZOM-637, ZOM-645; game industry 11 ZOM-568–576, ZOM-598, ZOM-622) | Register tab of f_43bc35baf77fd59f4e57b8 (SQL L342) | — | gsheets_values_update | F3, F5–F8, F12–F19, F22 |
| W2 memo | one audience call: casual leads 3.83 (27) vs RPG 3.50 (18), gap 0.33 past the 0.25 band in f_a087f049d271e9aa9f567f, over counted sessions; panel context 3.33 over 9 per Leonard's void rule in thread C090N54TG79/1758729919.603185 on julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>; retention context 10.47 % install-weighted mature D7 (16 cohort rows, 2,607 installs) for cohort weeks starting on or after 2025-07-24 per Vincent's KPI-tab note f_4e21b203a62910bdae0353 over Robert's rule C090N54TG79/1759167008.881274 | new Doc in Julia's folder d_8140f09bf9f1b94cb8ee2d (card 68dc0acf1815df76ed9b887d, SQL L859) | — | gdocs_create_document | F9–F11, F20, F21 |
| W3a late tickets | 2 new ZOM tickets for Owen's Sun Sep 28 sessions per the log note f_c691d577b8f837eb4f9eaa ("gets a ticket and a log row when I see it") | Linear team ZOM | — | linear_create_issue | F4, F19 |
| W3 ticket states | counted → Done (45), not counted → Canceled (37) per f_c691d577b8f837eb4f9eaa | ZOM-568 to ZOM-647 and the 2 new tickets | — | linear_update_issue | W1, W3a |
| W4 re-run notes | technical drops only: the 13 build-1943 sessions (ZOM-577 to ZOM-586, ZOM-632, ZOM-637, ZOM-645) per D05GU6L0XFH/1758913471.205816; no device drops in rev7 (the 13 Samsung sessions count) | comments on those 13 tickets | — | linear_create_comment | W1 |
| W5 reply | hold (casual lead means hold, C090N54TG79/1759266627.418203) | thread of C090N54TG79/1759266627.418203 | leonard.hayes@harmonygames.co (EMPLOYEE_0038_SLACK_ID) | slack_send_message (thread_ts) | W1, W2 |
| W6 Brian message | hold: the tutorial and level order work does not go on | #zombie-design C090N54TG79 (thread or top level) | brian.foster@harmonygames.co (EMPLOYEE_0026_SLACK_ID) | slack_send_message | W5 |

| Decision-ambiguity risk | Alternative a careful run could take | What pins it |
|---|---|---|
| reply place | top-level post in #zombie-design | prompt "reply to him in his thread"; ask "reply here" C090N54TG79/1759266627.418203 (learnings §5) |
| Brian message place | Brian's DM D076RBM29JS | ask says "tell <@EMPLOYEE_0026_SLACK_ID> in this channel" C090N54TG79/1759266627.418203; prompt "in #zombie-design" |
| register place | a new sheet or the Log tab | prompt "the register tab in my audience sessions workbook"; tab exists, SQL L342 f_43bc35baf77fd59f4e57b8 |
| memo place | Drive root by default / another folder | card "memo goes in Julia's folder with her log note" 68dc0acf1815df76ed9b887d; the log note's parent is d_8140f09bf9f1b94cb8ee2d (SQL L6) |
| session scope | only the 80 logged sessions | Julia's log note f_c691d577b8f837eb4f9eaa: a form after the batch gets a ticket and a log row; Owen's mail julia.lawson@harmonygames.co/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com> (20:40Z) follows the last batch edit (workbook 20:26:45Z, SQL L10) |
| Samsung sessions | drop them (Vision Bot run #15 is editor-only; or the matrix names one phone) | gate Doc f_748d26e760e54651eaa0d8 "Once there is a pass, it covers all the Samsung sessions"; real-device row SM-A546E in f_cadae9f611d82d56ac02c3 posted at C08R27X0EAH/1759158757.418562 |
| keep vs hold | keep, from the leaders' lean C090N54TG79/1759178344.878219 | ask mapping casual → hold; gap 0.33 past the 0.25 band in f_a087f049d271e9aa9f567f |
| hedge | "with and without" view, no clear call | prompt "give him one call, not a maybe"; ask "give me one audience call" C090N54TG79/1759266627.418203 |
| act vs wait | stage the writes for Julia | prompt "you don't need my ok on any of it"; the ask asks for the writes directly C090N54TG79/1759266627.418203 |
| re-run scope | notes on all 37 drops | Robert's reply D05GU6L0XFH/1758913471.205816 limits notes to technical drops (device or build) |
| note order | note before or after the state write | no record orders them (D05GU6L0XFH/1758913471.205816 states no order); both accepted |

### 4b · Canonical outcome (all fair outcomes)

| Deliverable | Field | Fixed value (or closed accepted set, with sources) | Delegated by (quoted span, or —) | Allowed equivalence class | Material / representational |
|---|---|---|---|---|---|
| W1 | rows | exactly the 82 sessions: ZOM-568 to ZOM-647 (f_43bc35baf77fd59f4e57b8 Log tab) plus the two in julia.lawson@harmonygames.co/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com> | — | any row order; late rows keyed by their new ticket key or by player name | material |
| W1 | verdict | counted 45 / not counted 37 as in §4 (rules C090N54TG79/1758517286.431379, C090N54TG79/1758733233.117446, C090N54TG79/1758818538.552913, f_748d26e760e54651eaa0d8, f_a087f049d271e9aa9f567f) | — | counted/not counted, Done/Canceled-equivalent labels | material |
| W1 | reason wording | names the deciding fact (coached, non-store build, game industry) per the Register header f_43bc35baf77fd59f4e57b8 | — | any wording naming the fact | representational |
| W2 | call | casual leads → hold (mapping in C090N54TG79/1759266627.418203; band in f_a087f049d271e9aa9f567f) | — | "casual" / "casual lead" | material |
| W2 | means | casual 3.83 over 27, RPG 3.50 over 18 (3.8333 / 3.5 accepted), counted sessions only (truth.json; deck f_a087f049d271e9aa9f567f "over counted sessions") | — | rounding to 2 dp or exact | material |
| W2 | panel | 3.33 over 9 after the void (julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>, rule C090N54TG79/1758729919.603185) | — | 3.3 or 3.33 | material |
| W2 | retention | 10.47 % install-weighted mature D7 over cohort weeks starting on or after 2025-07-24 (snowflake.USER_COHORT_RETENTION; f_4e21b203a62910bdae0353; C090N54TG79/1759167008.881274) | — | 10.47, 10.5 | material |
| W2 | layout and prose | — (contents per card 68dc0acf1815df76ed9b887d) | "write the memo he asked for" | any Doc layout | representational |
| W3a | late tickets | 2 new tickets, one per late session (f_c691d577b8f837eb4f9eaa) | — | any title or description naming the session | material count, representational text |
| W3a | late Log rows | a Log-tab row per late ticket per the same log note f_c691d577b8f837eb4f9eaa | — | present or absent; not a manifest requirement (R7 and R14 grade tickets and register rows); rubric weight decided at 09 | representational |
| W3 | states | Done 45 / Canceled 37 (f_c691d577b8f837eb4f9eaa) | — | — | material |
| W4 | notes | on the 13 build drops only (D05GU6L0XFH/1758913471.205816) | — | any wording; before or after the state write | material set, representational text |
| W5 | place and word | thread reply under C090N54TG79/1759266627.418203 saying hold | — | "hold" with or without the reason | material |
| W6 | place and word | C090N54TG79, tutorial and level order work does not go on | — | thread or top level | material word, representational place |

## 5 · Discovery map

| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |
|---|---|---|---|---|---|---|
| F1 the ask | one audience call; mapping casual → hold, RPG/no clear lead → keep; memo per roadmap card; reply here; tell Brian; current game only. No rule pointers (rev7) | C090N54TG79/1759266627.418203 (SQL L887) | YES member | met first | low | Yes, as "his message" / "his thread": anchor A2 Julia knows |
| F2 Leonard's feedback note | No coaching, 25–45 friends, honest reactions | C090N54TG79/1758517286.431379 (base /537) | YES member | met first | low | Yes, anchor A1 "his feedback note" |
| F3 workbook | Log 80 rows ZOM-568 to ZOM-647, Register header "one row per session" | f_43bc35baf77fd59f4e57b8 (SQL L10, L340, L342) | YES owner | met first; ties out 80/80 (trap) | low | Yes, anchor A3 "my audience sessions workbook" |
| F4 log note | counted → Done, not counted → Canceled; late form gets a ticket and a log row; players in contacts; device in comments | f_c691d577b8f837eb4f9eaa (SQL L176) | YES owner | Julia's own doc, found by her Drive | medium | No |
| F5 audience read criteria | label stands, higher mean, ≥ 6, gap < 0.25 no clear lead, sessions decide | f_a087f049d271e9aa9f567f (SQL L348–L360) | YES owner | GDD decoy first | medium | No |
| F6 stability gate | Samsung only; a pass covers all Samsung sessions once it ran on a Samsung; Arthur says what Vision Bot covers; dev builds do not count | f_748d26e760e54651eaa0d8 (SQL L174) via C090N54TG79/1758728411.540327 | YES shared / member | via the posts after the note | medium | No |
| F7 game-industry rule | game-industry people don't count, sessions already run too | C090N54TG79/1758733233.117446 (SQL L877) | YES member | via the posts after the note | medium | No |
| F8 relation rule | family, neighbours, old classmates count; 25–45; not in games | C090N54TG79/1758818538.552913 (SQL L879) | YES member | via the posts after the note | medium | No |
| F9 re-run handling | technical drops (device or build) get a re-run note; others just closed | D05GU6L0XFH/1758913471.205816 (SQL L883) | YES DM member | under an off-topic root | high | No |
| F10 memo spec | the call and numbers, panel and retention as context; memo in Julia's folder | 68dc0acf1815df76ed9b887d (SQL L859) | YES unscoped | via "roadmap card" in the ask | low | No |
| F11 retention rule | install-weighted D7, mature cohorts (D14), both platforms | C090N54TG79/1759167008.881274 (SQL L885) | YES member | KPI tab mean met first | medium | No |
| F12 coaching | form says none; Claire's later mail says she took them through the game | julia.lawson@harmonygames.co/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com> (SQL L452) then julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com> (SQL L508); evt_da65644831bc088267263d | YES own mailbox / calendar | form first, mail overturns | high (no shared vocabulary) | No — root cause |
| F13 Brian's group | Kadıköy ekibi works at mobile game companies | D076RBM29JS/1758659012.418207 (SQL L871) over f_524278b67bfa30dde78699 | YES DM member / shared | clean Doc first, DM overturns | high | No — root cause |
| F14 build 1943 | never went through a store; 0.3.127 (127), 0.3.38, 0.3.40 did | C090N54TG79/1758819934.612483 (SQL L881); C05433XK267/1758575557.575349 | YES member | form first, reply overturns | high (thread reply) | No — root cause |
| F15 Vision Bot limit | editor play mode, no phone in the loop | harmonygames-Games/match3d#476#rc_27 (SQL L856) | YES unscoped | after Vincent's line | high (inline comment read) | No |
| F16 Vincent's ZOM-567 line | editor repro and green run #15, no device claim | cmt_38b3cc50dceda37f40f5 on ZOM-567 (SQL L692) | YES unscoped | met first; decoy | — | No |
| F17 on-device pass | 0.3.127 (127) matrix all green; Android row SM-A546E real device PASS 2025-09-29 | C08R27X0EAH/1759158757.418562 (SQL L901), reply C08R27X0EAH/1759158843.902317; f_cadae9f611d82d56ac02c3 (SQL L899) | YES member / shared | met after the Vision Bot dead end; overturns "no pass" | high (other channel, model code only) | No — root cause |
| F18 players' jobs | Alper Koçak QA tester, console games publisher (ZOM-598); Arda Keskin live ops producer, mobile games studio (ZOM-622) | 038b5eb5a30326895cb54756 (SQL L965), 0810fb8287e489c125fe2cd9 (SQL L1013) | YES unscoped (Contacts) | via log note "players are in my contacts" | high | No — root cause |
| F19 late sessions | two Sun Sep 28 sessions, no ticket, Log row or notes Doc: Ayşe Polat casual 5 iPhone 15 0.3.40 (40); Daniel Hughes RPG 1.5 Pixel 8 0.3.127 (127) | julia.lawson@harmonygames.co/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com> (SQL L434) | YES own mailbox | workbook 80/80 tie-out first; mail adds two | high (outside every list) | No — root cause |
| F20 panel | ten ratings, player 8 void; void leaves sum and count → 3.33 over 9 | julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com> (SQL L368); C090N54TG79/1758729919.603185 (SQL L875) | YES own mailbox / member | note's 3–3.5 first | medium | No |
| F21 retention cut-off and data | Vincent: cohort weeks starting on or after 2025-07-24 only; 16 rows, 2,607 installs, D7 10.47 % (9.09 without the cut-off; 8.63 tab mean) | f_4e21b203a62910bdae0353 KPI row 1 (SQL L346); snowflake.USER_COHORT_RETENTION | YES shared / unscoped | 9.09 from the rule alone met first | high | No |
| F22 per-session facts | device in comments, build/age/relation in notes Docs | ZOM-568 to ZOM-647; cmt_2fbcaf2d990d8b4e9c0d; f_524278b67bfa30dde78699 and siblings | YES unscoped / shared | via F3 and F4 | volume | No |

## 5a · Search-as-persona proof

`persona_view.py search` reads only the base export, so seeded rows return 0 there; seeded reach is `persona_view.py check-sql julia_lawson 01_Universe_Inject.sql --load-bearing` (run this session on rev7, 19 load-bearing ids, verdict PASS, 0 load-bearing rows not visible). Visible hits below are base counts.

| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |
|---|---|---|---|---|---|---|
| F1 | slack | keep or hold | base 0; seeded 1 | 0 | C090N54TG79/1759266627.418203 | YES (seeded; check-sql YES LB L886) |
| F2 | slack | honest reactions | 1 | 1 | C090N54TG79/1758517286.431379 | YES |
| F3 | gsheets | ZM audience sessions | base 0; seeded 1 | 0 | f_43bc35baf77fd59f4e57b8 | YES (seeded; owner, check-sql YES LB L337) |
| F4 | gdocs | log note | base 0; seeded 1 | 0 | f_c691d577b8f837eb4f9eaa | YES (seeded; owner, check-sql YES LB L175) |
| F5 | gslides | audience read criteria | base 0; seeded 1 | 0 | f_a087f049d271e9aa9f567f | YES (seeded; owner, check-sql YES LB L347) |
| F6 | gdocs | stability gate | base 0; seeded 1 | 0 | f_748d26e760e54651eaa0d8 | YES (seeded; shared, check-sql YES LB L173) |
| F7 | slack | game industry | 8 base (off-topic) + seeded 1 | 14 | C090N54TG79/1758733233.117446 | YES (seeded; check-sql YES LB L876) |
| F8 | slack | old classmates | base 0; seeded 1 | 0 | C090N54TG79/1758818538.552913 | YES (seeded; check-sql YES LB L878) |
| F9 | slack | re-run note | base 0; seeded 1 | 0 | D05GU6L0XFH/1758913471.205816 | YES (seeded; check-sql YES LB L882) |
| F10 | trello | audience read | base 0; seeded 1 | 0 | 68dc0acf1815df76ed9b887d | YES (seeded; unscoped) |
| F11 | slack | install-weighted | base 0; seeded 1 | 0 | C090N54TG79/1759167008.881274 | YES (seeded; check-sql YES LB L884) |
| F12 | gmail | a small thing from Friday | base 0; seeded 1 | not scanned (--no-hidden) | julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com> | YES (seeded; own mailbox, check-sql YES LB L507) |
| F13 | slack | Kadıköy | 5 base (2024 meetup) + seeded 1 | 9 | D076RBM29JS/1758659012.418207 | YES (seeded; check-sql YES LB L870) |
| F14 | slack | 1943 | 31 base | 6 | C090N54TG79/1758819934.612483 | YES (seeded reply, check-sql YES LB L880; base C05433XK267/1758575557.575349 second path) |
| F15 | github | Vision bot | 3 base | 0 | harmonygames-Games/match3d#476#rc_27 | YES (unscoped; seeded inline comment SQL L856) |
| F16 | linear | ZOM-567 | base 0; seeded 1 | 0 | cmt_38b3cc50dceda37f40f5 | YES (seeded; unscoped) |
| F17 | slack / gsheets | regression matrix / QA matrix | base 0; seeded 1 each | 0 | C08R27X0EAH/1759158757.418562; f_cadae9f611d82d56ac02c3 | YES (seeded; check-sql YES LB L900, L896) |
| F18 | contacts | games studio | base 0; seeded 1 | 0 | 0810fb8287e489c125fe2cd9 | YES (seeded; unscoped) |
| F19 | gmail | sorry these are late | base 0; seeded 1 | not scanned (--no-hidden) | julia.lawson@harmonygames.co/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com> | YES (seeded; own mailbox, check-sql YES LB L433) |
| F20 | gmail | Playtest results | base 0; seeded 1 | not scanned (--no-hidden) | julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com> | YES (seeded; own mailbox, check-sql YES LB L367; rule C090N54TG79/1758729919.603185 YES LB L874) |
| F21 | gsheets / snowflake | KPI snapshot / USER_COHORT_RETENTION | base 0 + seeded 1 / 3 | 0 | f_4e21b203a62910bdae0353; ANALYTICS.GAME_EVENTS.USER_COHORT_RETENTION | YES (seeded; shared, check-sql YES LB L343; Snowflake unscoped) |
| F22 | linear | session | 3 base + 80 seeded "Friend session:" titles | 0 | ZOM-568 | YES (seeded; unscoped) |

```
SEARCH slack 'keep or hold' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH slack 'honest reactions' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=1 in 1 containers  UNVERIFIED=0 in 0 containers
  {"id": "C090N54TG79/1758517286.431379", "channel": "zombie-design", "kind": "private", "date": "2025-09-22", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "r friends (not kids). No coaching, just observe and collect honest reactions. • Once we have clean data from a tech-stable beta i
SEARCH gsheets 'ZM audience sessions' as julia_lawson  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gdocs 'log note' as julia_lawson  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gslides 'audience read criteria' as julia_lawson  scope: GSlides title + page element text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gdocs 'stability gate' as julia_lawson  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH slack 'game industry' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=8 (showing 3)  hidden by ACL=14 in 10 containers  UNVERIFIED=0 in 0 containers
SEARCH slack 'old classmates' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH slack 're-run note' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH trello 'audience read' as julia_lawson  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH slack 'install-weighted' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gsheets 'KPI snapshot' as julia_lawson  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gmail 'Playtest results' as julia_lawson  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gmail 'a small thing from Friday' as julia_lawson  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH slack 'Kadıköy' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=5 (showing 3)  hidden by ACL=9 in 2 containers  UNVERIFIED=0 in 0 containers
SEARCH slack '1943' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=31 (showing 3)  hidden by ACL=6 in 6 containers  UNVERIFIED=5 in 1 containers
SEARCH github 'Vision bot' as julia_lawson  scope: hg.py search (unscoped: no ACL filter)
visible hits=3 (showing 3)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH linear 'ZOM-567' as julia_lawson  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH slack 'regression matrix' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gsheets 'QA matrix' as julia_lawson  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH contacts 'games studio' as julia_lawson  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gmail 'sorry these are late' as julia_lawson  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH snowflake 'USER_COHORT_RETENTION' as julia_lawson  scope: hg.py search (unscoped: no ACL filter)
visible hits=3 (showing 3)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH linear 'session' as julia_lawson  scope: hg.py search (unscoped: no ACL filter)
visible hits=3 (showing 3)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

check-sql julia_lawson 01_Universe_Inject.sql --load-bearing (19 ids, rev7 3acbfad93f4a), load-bearing rows (excerpt):
[YES LB] L886 slack.slack_messages insert b07f1e10112b7661e1d8eaf3b127227f, C090N54TG79/1759266627.418203 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] L876 slack.slack_messages insert e72083b249987542a134098010edd305, C090N54TG79/1758733233.117446 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] L878 slack.slack_messages insert ba19de7863a540175f2aeadc12916fa6, C090N54TG79/1758818538.552913 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] L882 slack.slack_messages insert 167dc58affb9902420038f71d0f5af28, D05GU6L0XFH/1758913471.205816 - persona EMPLOYEE_0005_SLACK_ID is in members of im D05GU6L0XFH
[YES LB] L884 slack.slack_messages insert 2ca968ace3e14d1a34c535f8a5c0cd6e, C090N54TG79/1759167008.881274 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] L874 slack.slack_messages insert 7b38bd6429ce0f189456ac72af02f210, C090N54TG79/1758729919.603185 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] L870 slack.slack_messages insert 246d6f4a90620e5dafbb06068f450e46, D076RBM29JS/1758659012.418207 - persona EMPLOYEE_0005_SLACK_ID is in members of im D076RBM29JS
[YES LB] L880 slack.slack_messages insert d7122186e361aa99778c65cb1502759d, C090N54TG79/1758819934.612483 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] L900 slack.slack_messages insert 3dd0b6d6c52c21cd5bbfcd6d6f5345cd, C08R27X0EAH/1759158757.418562 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-bugs
[YES LB] L902 slack.slack_messages insert 3d8e451a198d5d59b39e60064b590305, C08R27X0EAH/1759158843.902317 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-bugs
[YES LB] L896 gsheets.sheets_spreadsheets insert f_cadae9f611d82d56ac02c3 - file is shared with the persona (shared_with_emails)
[YES LB] L343 gsheets.sheets_spreadsheets insert f_4e21b203a62910bdae0353 - file is shared with the persona (shared_with_emails)
[YES LB] L173 gdocs.docs_documents insert f_748d26e760e54651eaa0d8 - file is shared with the persona (shared_with_emails)
[YES LB] L175 gdocs.docs_documents insert f_c691d577b8f837eb4f9eaa - persona owns the file
[YES LB] L347 gslides.slides_presentations insert f_a087f049d271e9aa9f567f - persona owns the file
[YES LB] L337 gsheets.sheets_spreadsheets insert f_43bc35baf77fd59f4e57b8 - persona owns the file
[YES LB] L433 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L367 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L507 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
summary: {'YES': 242, 'NO': 41, 'UNVERIFIED': 3}  unscoped rows (always visible): 249
verdict: PASS (0 load-bearing rows not visible)
```

check-sql line numbers are 0-based statement indexes (L886 = SQL file line 887). The 41 NO rows are other mailbox copies of seeded mail threads (Owen's SENT copy among them), none load-bearing; the 3 UNVERIFIED are #zombie-prs mirror rows (non-member reads), never load-bearing.

Search-behaviour risks (design notes only): the log and tickets tie out 80/80 and agents stop at a clean tie-out; Owen's late mail sits outside every list (F19); F9, F14 sit as thread replies under roots the ask does not name; F15 needs an inline-comment read and F17 sits in another channel naming a model code only; F18 needs a Contacts read the log note mentions in passing; F12 shares no vocabulary with the form mails; agents take the 9.09 rule result and miss Vincent's cut-off on the KPI tab (F21).

## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · readable · unique · instructions-not-answer) | Inferable |
|---|---|---|---|---|
| R1–R4 session exclusions (coaching, device clearance, store builds, game industry) | C090N54TG79/1758517286.431379, f_748d26e760e54651eaa0d8, C090N54TG79/1758733233.117446, C090N54TG79/1758818538.552913 | deliverable: "the audience call" + "fill in the register tab" | Leonard's feedback note C090N54TG79/1758517286.431379 (named as "his feedback note") and his rule posts after it in the same channel · YES member · the posts reply "on the feedback note" · state rules, not verdicts | yes: a PM counting sessions applies the requester's posted session rules (rev7 ask no longer points at them, 01a §11 P1) |
| R5, R10–R13 memo contents and place | 68dc0acf1815df76ed9b887d | deliverable: "write the memo he asked for and put it in my drive folder" | ask "put it in a memo, what goes in it is on the roadmap card" · YES · one card on ZM ROADMAP · states contents, not values | no — needs the ask |
| R6 reply keep/hold | C090N54TG79/1759266627.418203 | deliverable + destination: "reply to him in his thread with keep or hold" | the ask itself · YES | no |
| R7 ticket states and late tickets | f_c691d577b8f837eb4f9eaa | deliverable: "close out the session tickets" | Julia's own log note · YES owner · unique · states the mapping and the late-form procedure, not which tickets (04_Prompt_Check.md #3, Advisory) | yes: the persona's own standing procedure |
| R8 re-run notes | D05GU6L0XFH/1758913471.205816 | scope via the close-out ask | Robert's reply to Julia on the friend sessions · YES DM member · one reply · states handling, not tickets | yes: a direct instruction to Julia about closing these sessions |
| R9 Brian message | C090N54TG79/1759266627.418203 | deliverable + recipient: "tell brian in #zombie-design whether the tutorial and level order work goes on" | the ask · YES | no |
| R14 register format | f_43bc35baf77fd59f4e57b8 Register tab | destination: "the register tab in my audience sessions workbook" | tab header "Register: one row per session" (SQL L342) · YES owner | no |
| commitment (no hedge) | C090N54TG79/1759266627.418203 "give me one audience call" | constraint: "he has to act on this, so give him one call, not a maybe" | the ask | yes (implicit) |

| Anchor | May be named |
|---|---|
| A1 | Leonard's feedback note; his feedback note |
| A2 | Leonard's keep-or-hold message; his message; his thread |
| A3 | audience sessions workbook; the register tab |

### 6b · Every prompt reference and the record it matches

| Prompt span | Record (SQL line or base pointer) | Match |
|---|---|---|
| "leonard asked me in #zombie-design" | SQL L887 user EMPLOYEE_0038_SLACK_ID = leonard.hayes@harmonygames.co (entity.py resolve), channel C090N54TG79 | author and place of the ask |
| "for the audience call on the friend sessions" | SQL L887 "give me one audience call from the friend sessions" | wording of the ask |
| "the ones that came out of his feedback note" | base messages/C090N54TG79/2025-09.json /537, ts 1758517286.431379; SQL L879 "on the feedback note" | true; no date named |
| "he wants to settle the cards earlier change on what players told us" | SQL L887 "I want to settle the cards earlier change from Monday on what players told us, not on our gut"; base C090N54TG79/1759172166.547199 | Leonard's words; no shipped claim |
| "his message says what he needs" | SQL L887 lists the call, the memo, the reply and the Brian message | true; no rule location (01a §11 P1 closed) |
| "fill in the register tab in my audience sessions workbook" | SQL L10 'ZM audience sessions', owner julia.lawson@harmonygames.co; SQL L342 sheet 'Register' | anchor A3; no completeness claim (Owen's mail SQL L434 is later than the workbook's last edit) |
| "write the memo he asked for" | SQL L887 "put it in a memo, what goes in it is on the roadmap card"; L859 card 68dc0acf1815df76ed9b887d | true |
| "put it in my drive folder" | SQL L859 "memo goes in Julia's folder with her log note"; d_8140f09bf9f1b94cb8ee2d owner julia.lawson@harmonygames.co; log note parent SQL L6 | true |
| "close out the session tickets" | log note SQL L176 close-out mapping; tickets ZOM-568 to ZOM-647 | true |
| "reply to him in his thread with keep or hold" | SQL L887 "reply here with keep or hold" | true |
| "tell brian in #zombie-design whether the tutorial and level order work goes on" | SQL L887 "tell <@EMPLOYEE_0026_SLACK_ID> in this channel whether the tutorial and level order work goes on"; EMPLOYEE_0026 = brian.foster@harmonygames.co | verbatim |
| "he has to act on this, so give him one call, not a maybe" | SQL L887 "give me one audience call" | true |
| "can you do all of it for me?" | SQL L887 addressed to EMPLOYEE_0005_SLACK_ID (Julia) | true |
| "post and update everything under my name" | catalog writes post as the persona; SQL L887 asks Julia herself to reply and tell Brian | true |

No deck title, Doc title, card title, ticket key, PR, mail, contact, matrix or DM is named. The prompt names no hidden authority and no rule location.

## 7 · Dates and constraints

| Item | Absolute date or value | Source | Past fact or deadline |
|---|---|---|---|
| Leonard's feedback note | 2025-09-22T05:01:26Z (Sun Sep 21 10:01 PM PT; UTC day Sep 22) | C090N54TG79/1758517286.431379 | past |
| Cards earlier proposal | 2025-09-29 (Mon) | C090N54TG79/1759172166.547199 | past; unshipped |
| Sessions | 2025-09-22 to 2025-09-29 (Owen's late pair Sun Sep 28) | f_43bc35baf77fd59f4e57b8 Log tab; ZOM-568 to ZOM-647; julia.lawson@harmonygames.co/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com> | past |
| QA matrix posted | 2025-09-29T15:12:37Z (Mon 8:12 AM PT) | C08R27X0EAH/1759158757.418562 | past |
| Vincent's KPI-tab cut-off note | sheet modified 2025-09-30T10:22:41Z; cut-off cohort weeks starting on or after 2025-07-24 | f_4e21b203a62910bdae0353 | past |
| Arthur's PR note | 2025-09-30T20:10:26Z | harmonygames-Games/match3d#476#rc_27 | past |
| Owen's late mail | 2025-09-30T20:40:00Z (Tue 1:40 PM PT), after the workbook's last edit 20:26:45Z | julia.lawson@harmonygames.co/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com>; SQL L10 | past |
| Leonard's ask (latest seeded deciding record) | 2025-09-30T21:10:27Z (Tue Sep 30 2:10 PM PT) | C090N54TG79/1759266627.418203 | past (the prompt names no date) |
| Iterate or pivot | later call, no date | C090N54TG79/1759266627.418203 "iterate or pivot is a later call" | future; prompt does not mention it |
| Clock / today | 2025-10-01 00:00 PT (07:00Z), Wednesday | 00_Task_Context.json universe.clock_line; seed bound 2025-10-01T00:00:00Z; latest seed before it C090N54TG79/1759266627.418203 | now |

No deadline is stated in the prompt; none exists in a seed (01_Grounding_Dossier.md §Constraints).

## 8 · Difficulty levers

| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |
|---|---|---|---|---|
| Ambiguity | yes | yes | which sessions exist and count lives in the rule posts after the note, the gate Doc f_748d26e760e54651eaa0d8, the deck f_a087f049d271e9aa9f567f, the log note f_c691d577b8f837eb4f9eaa | prompt points at "his message" only and no longer at where the rules are; destinations all named |
| Dynamic change | yes | yes | form → Claire's mail; Vincent's ZOM-567 line → rc_27 → QA matrix; Brian's Doc → DM; form → 1943 reply; workbook 80/80 → Owen's late mail; Robert's rule → Vincent's cut-off | prompt names none of the first or second records |
| Multi-source | yes | yes | 12 services | no source named as an exact artifact beyond the three anchors |
| Async | no | — | — | — |
| Error recovery | no | — | Friction: none (03_Error_Async_Config.txt, re-run on rev7) | — |
| Access control | no | no | #zombie-prs mirror unverified; GitHub carries the fact | not mentioned |

hardness_v2_check (this run): RULE_IN_PROMPT CLEAN; DECISION_FLIP flags R_F, R_D, R_E (weight-3 slots only), dispositioned upstream in the manifest; no prompt change needed.

## 9 · Must not appear in the prompt

- Tool / server names (Evals/references/tools/catalog.json): slack_*, gsheets_*, gdocs_*, gdrive_*, gslides_*, linear_*, trello_*, gmail_*, gcal_*, github_*, snowflake_*, contacts_*, confluence_*, any MCP server name, "the X tool".
- Ids: C090N54TG79, C08R27X0EAH, D076RBM29JS, D05GU6L0XFH, any ts, f_43bc35baf77fd59f4e57b8, f_c691d577b8f837eb4f9eaa, f_a087f049d271e9aa9f567f, f_748d26e760e54651eaa0d8, f_cadae9f611d82d56ac02c3, f_4e21b203a62910bdae0353, d_8140f09bf9f1b94cb8ee2d, 68dc0acf1815df76ed9b887d, evt_da65644831bc088267263d, contact ids, any ZOM key, PR #476, run #15, build 1943 (dossier §Constraints).
- Hidden authorities and rule locations, by title or by place: "ZM session stability gate", "ZM audience read criteria", "ZM sessions log note", the roadmap card title, "the rules he posted after his note", "where the rules are", Robert's DM, the panel forward, Leonard's void-rating thread, the retention post, Vincent's KPI-tab note, the QA matrix, #zombie-bugs, Julia's contacts.
- Trap hints: that a form came in late or sits outside the workbook, Owen, "two more", any claim that the workbook is or is not complete, "check every session", "some sessions may not count", jobs or industry of players, editor vs device, "a newer number", cut-off or Calm Play.
- Findings and causes: coaching at Claire's, Samsung, editor play mode, on-device matrix, non-store build, Kadıköy ekibi / game industry, Alper Koçak, Arda Keskin, Ayşe Polat, Daniel Hughes, the counts 82/45/37/13/11, the means 3.83/3.50, casual lead, hold, 10.47, 9.09, 3.33, 2025-07-24.
- Audit wording: valid, audit, check carefully, make sure, reconcile, classify, exclude, which sessions count.
- Form: markdown, numbered steps, column lists, format rules, call or step counts.
- False premises: beta shipped, the read is final, Victor acting, anything dated after 2025-09-30 23:59:59 PT.

## 10 · Entity traps

```
SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <trello:c48a210d5c5a4b59231c6873>']
  martin: ['Martin Lewis <PERSON_0394_EMAIL>', 'Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]']
  thomas: ['Thomas Baker <thomas.baker@harmonygames.co>', 'Thomas <thomas@harmonygames.co> [persona thomas]']

SHARED_LAST_NAMES (5)
  baker: ['Owen Baker <owen.baker@harmonygames.co> [persona owen_baker]', 'Thomas Baker <thomas.baker@harmonygames.co>']
  bennett: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Oscar Bennett <oscar.bennett@harmonygames.co>']
  brooks: ['Lauren Brooks <lauren@harmonygames.co>', 'Oliver Brooks <oliver.brooks@harmonygames.co> [persona oliver_brooks]']
  lawson: ['Julia Lawson <julia.lawson@harmonygames.co> [persona julia_lawson]', 'Peter Lawson <peter.lawson@harmonygames.co>']
  price: ['Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]', 'Nathan Price <nathan@harmonygames.co>']

ENTITY email:brian.foster@harmonygames.co  name=Brian Foster  kind=person  emails=['brian.foster@harmonygames.co']
  persona: brian_foster - Game Engineer / Engineering
  slack      id=EMPLOYEE_0026_SLACK_ID, name=Brian Foster, real_name=Brian Foster, email=brian.foster@harmonygames.co, is_bot=False, deleted=False, messages=28951, first_post=2024-06-06, last_post=2025-09-30   [join: exact_email]
ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
  persona: leonard_hayes - Co-founder & Creative Director / Executive
  slack      id=EMPLOYEE_0038_SLACK_ID, name=Leonard Hayes, real_name=Leonard Hayes, email=leonard.hayes@harmonygames.co, is_bot=False, deleted=False, messages=129898, first_post=2023-03-15, last_post=2025-10-01   [join: exact_email]
ENTITY email:julia.lawson@harmonygames.co  name=Julia Lawson  kind=person  emails=['julia.lawson@harmonygames.co']
  persona: julia_lawson - Product Manager / Product
  slack      id=EMPLOYEE_0005_SLACK_ID, name=Julia Lawson, real_name=Julia Lawson, email=julia.lawson@harmonygames.co, is_bot=False, deleted=False, messages=31848, first_post=2023-07-16, last_post=2025-09-30   [join: exact_email]
no exact match for 'Brian'
  candidate: email:brian.foster@harmonygames.co  Brian Foster  ['brian.foster@harmonygames.co']
no exact match for 'Leonard'
  candidate: email:leonard.hayes@harmonygames.co  Leonard Hayes  ['leonard.hayes@harmonygames.co']
no exact match for 'Julia'
  candidate: email:julia.lawson@harmonygames.co  Julia Lawson  ['julia.lawson@harmonygames.co']
```

| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |
|---|---|---|---|
| Leonard Hayes leonard.hayes@harmonygames.co | mailbox files `leonard@…` | alias only | leonard.hayes@harmonygames.co |
| Brian Foster brian.foster@harmonygames.co | mailbox files `brian@…`; no Gmail use (SC-6) | alias only | brian.foster@harmonygames.co |
| Julia Lawson julia.lawson@harmonygames.co | Peter Lawson peter.lawson@harmonygames.co | different person | julia.lawson@harmonygames.co |
| Owen Baker owen.baker@harmonygames.co (late mail sender) | Thomas Baker thomas.baker@harmonygames.co | different person | julia.lawson@harmonygames.co/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com> |
| #zombie-design C090N54TG79 | zombie-match3d, zombie-bugs C08R27X0EAH (holds the QA matrix post), zombie-prs, zombie-art, zombie-ops, zombie-social, zombie_marketing | different channels; only C090N54TG79 takes the writes | C090N54TG79 |
| ZOM-568 to ZOM-647 friend-session tickets | ZOM-567 (Samsung recheck, Done), ZOM-559 (Todo) | not sessions; outside the 80 | ZOM-567, ZOM-559 |
| ZM audience sessions f_43bc35baf77fd59f4e57b8 | KPI snapshot f_4e21b203a62910bdae0353; QA matrix f_cadae9f611d82d56ac02c3 | different workbooks; neither is the register | f_4e21b203a62910bdae0353 |

## 11 · Pre-submit checklist

- [ ] Julia's voice: short, plain, lowercase, one paragraph, no markdown
- [ ] names Leonard's feedback note, his message/thread and the audience sessions workbook as plain anchors; nothing else by exact title or id
- [ ] asks the agent (no "I'll") for the register tab, the memo in her drive folder, the ticket close-out, the reply in Leonard's thread, the message to Brian in #zombie-design
- [ ] asks for one call
- [ ] says nothing about where the rules are (01a §11 P1) and makes no claim the workbook holds every session
- [ ] no relative or absolute date in the prompt
- [ ] nothing from §9; no "valid", "audit", "check carefully", "make sure"
- [ ] no tool or server name; no numbered steps; no count
- [ ] hardness_v2_check RULE_IN_PROMPT CLEAN

## 12 · Blockers and routed defects

None blocking for this stage. Prompt unchanged (sha256 c3da944d7da5, 132 words): the rev7 check (04_Prompt_Check.md) found 0 Fail; this re-bind found no new defect. Carried open items: C8 Advisory on the late tickets resting on Julia's own log note f_c691d577b8f837eb4f9eaa (rubric weight ≤ 3 or confirm at /rubric); the late-session Log rows are expected by the log note but not a manifest requirement (§4b, decide at 09). Platform follow-ups from 01_Grounding_Dossier.md: injected Linear comments render (cmt_2fbcaf2d990d8b4e9c0d), the #476 comment read spill (harmonygames-Games/match3d#476), a new Doc landing in d_8140f09bf9f1b94cb8ee2d, Slides element text (f_a087f049d271e9aa9f567f), Snowflake figures after regeneration (snowflake.USER_COHORT_RETENTION, 10.47 over 16 rows). Volume: firm 358, 438 with the conditional per-ticket reads; the 400+ ask needs a run that also reads routine context (dossier rev7 Unresolved). No independent review of the rev7 SQL exists.

## 13 · Self-review

Walked `Evals/1_Prompt_Eval.md` Phases 1–3 against this brief and 04_Prompt.txt (§1.1 persona, §1.2 voice, §1.3 pre-solved/tool mention/command list, §1.5 complexity and seeding, §2.1 fair outcomes, §2.2 feasibility and ACL, §2.3 truthfulness, §2.6 clarity, §2.7 contrived register, §2.8 today's date, §2.9 originality, §3.2 friction and coherence).

| Area | Counter-reading | Resolution (evidence) |
|---|---|---|
| Fair readings | a run could keep, following the leaders' lean C090N54TG79/1759178344.878219 | the ask's mapping and the 0.25 band in f_a087f049d271e9aa9f567f settle it on the counted sessions: casual 27 at 3.8333 vs RPG 18 at 3.5000 (truth.json); one fair outcome |
| Fair readings | a run could drop the 13 Samsung sessions because Vision Bot run #15 is editor-only (harmonygames-Games/match3d#476#rc_27) | the gate Doc f_748d26e760e54651eaa0d8 needs one on-device pass and says it then covers all Samsung sessions; the matrix f_cadae9f611d82d56ac02c3 has a real-device SM-A546E PASS, posted at C08R27X0EAH/1759158757.418562 before the clock |
| Fair readings | a run could close only the 80 logged sessions and skip Owen's two | log note f_c691d577b8f837eb4f9eaa sends a later form to a new ticket and a log row; the mail julia.lawson@harmonygames.co/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com> is 20:40Z, after the workbook's last edit (SQL L10) |
| Fair readings | retention 9.09 (Robert's rule alone) or 10.44 (keeping week 2025-07-21) | Vincent's note on f_4e21b203a62910bdae0353 limits to cohort weeks starting on or after 2025-07-24, Robert's method unchanged → 10.47 (10.5 accepted); week 2025-07-21 starts before the cut-off |
| Fair readings | Brian's message in a thread vs top level, re-run note order | both accepted in §4b; same decision, recipient and content (C090N54TG79/1759266627.418203) |
| Clarity | "close out the session tickets" could mean comment only, or Done for all, or only the 80 that exist | the log note f_c691d577b8f837eb4f9eaa gives the mapping and the late-ticket step; one concrete write per ticket (04_Prompt_Check.md #3 Advisory) |
| Clarity | "my drive folder" could be another folder | the card 68dc0acf1815df76ed9b887d says Julia's folder with her log note; the log note sits in d_8140f09bf9f1b94cb8ee2d (SQL L6) |
| Incorporation | with "where the rules are" gone, the exclusion rules may be unauthorized | the rules are Leonard's own posts replying "on the feedback note" (C090N54TG79/1758818538.552913, C090N54TG79/1758733233.117446) in the channel of his ask, and the prompt names that note; a PM applies the requester's posted rules (C8 (a)–(d) hold: readable, unique, rules not verdicts) |
| Incorporation | the re-run notes might be unauthorized | Robert's reply D05GU6L0XFH/1758913471.205816 is addressed to Julia about the friend sessions; it states handling, not tickets |
| Truthfulness | "fill in the register tab in my audience sessions workbook" could imply the workbook holds every session | it names only the destination; the rev6 completeness premise was removed (04_Prompt_Check.md #2); the Register tab exists (SQL L342) |
| Truthfulness | "his message says what he needs" could overclaim | SQL L887 lists the call, memo, reply and Brian message, which is all the prompt attributes to it |
| Feasibility / ACL | Julia might not reach the QA matrix or Vincent's post | f_cadae9f611d82d56ac02c3 is shared with her as reader and she is a member of C08R27X0EAH (check-sql YES LB L896, L900); Contacts and GitHub are unscoped |
| Feasibility / ACL | a Doc create may not land in the folder | d_8140f09bf9f1b94cb8ee2d is Julia's root, so a parentless create lands there; gdrive_move_file exists in Evals/references/tools/catalog.json (dossier Platform follow-ups) |
| Contrived register | "he has to act on this, so give him one call, not a maybe" could read as a hint | it names commitment, not a trap; control-symptom (prompt_qc_cases.json) passes symptom wording |
| Contrived register | listing five destinations could read as a spec sheet | each is one plain clause the persona knows; no columns, labels or rules (control-plain-request; K42/K47 show naming destinations is required) |

Calibration self-test against `Evals/references/rules/prompt_qc_cases.json` (15 cases): K11-staged-errors not matched (clean spelling); K11-control-spelled-correctly matched; K31-trap-hint not matched (no rule location, no completeness or lateness hint); control-symptom matched; K42, K47, K44 hidden-destination not matched; control-named-destination matched; K1-audit-form and K43-audit-form not matched; K44-if-chain not matched; control-plain-request matched; K43-departed-person-premise not matched (no Victor); K50-both-fair-figure and K49-newer-source not applicable (no figure in the prompt, no "most recent" line). Playbook checks C1 (132 words), C14 (no tool names), C15 (deliverable order only) and C9 (no cause or count) hold.

Re-verified this run: the ask text (SQL L887), the log note (SQL L176), the gate Doc (SQL L174), the Register tab (SQL L342), the KPI note (SQL L346), the matrix row (SQL L899) and post (SQL L901), the Contacts jobs (SQL L965, L1013), Owen's mail (SQL L434), the card (SQL L859), base visibility of C090N54TG79/1759172166.547199, C090N54TG79/1759178344.878219, C05433XK267/1758575557.575349 and d_8140f09bf9f1b94cb8ee2d (persona_view can-see YES), the truth counts and means (truth.json: 45 counted, casual 27 at 3.8333, RPG 18 at 3.5000; re-run set ZOM-577–586, ZOM-632, ZOM-637, ZOM-645), entity.py collisions and resolve. The 04_Prompt.txt hash (c3da944d7da5) is unchanged by this run.

Rev7 re-bind (2026-11-09): replaces the rev5 facts (60 sessions, 17 counted, 21 re-run notes, retention 9.09). Upstream error-async was re-run on rev7 so the chain is current.

Unresolved: none for this stage. Open items (rubric / pre-check, not prompt): §12.

```
STAGE GATE prompt-writing: PASS — Task_Authoring\task_inputs · 04_Prompt_Writing_Brief.md#5c85145c29b3 · 00_Assigments.md#638de5aac707 · 01_Grounding_Dossier.md#854cbb11bc06 · 01_Universe_Inject.sql#3acbfad93f4a · 03_Error_Async_Config.txt#7174fb324883 · 01a_Hardening_Report.md#cbb68eeabfe4 · __context__#50e89bdae5e1 · __assignment__#7709f2a35b0e · __policy__#dc4ab5df3cdd · __gate_policy__#6bbf415e008b · __review__#7343be0506e2 · blocking 0 · warnings 0 · checks 25
[PASS] assignment.v3_context: Julia Lawson / Product Manager; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Writing_Brief.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql, 03_Error_Async_Config.txt, 01a_Hardening_Report.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#3acbfad93f4a, 01_Hardness_Manifest.json#ccaf326dbd28, 01_Grounding_Dossier.md#854cbb11bc06, solver/solver.py#c5cb9c1fd1f2, 01c_Dispositions.json#a93e896d5a19, 01c_Preflight_Report.json#eb3e617a6933, 00_Assigments.md#638de5aac707, 01_Scenario_Design.md#e8967f83db15, 01_Hardness_Manifest.draft.json#814b8577398a, 01_Gradable_Surface.json#d1ce8485d03c, __context__#50e89bdae5e1, __assignment__#7709f2a35b0e, __policy__#dc4ab5df3cdd, __gate_policy__#ce51ca16c6f8, __review__#cb4fae31202a)
[PASS] chain.error-async: upstream 'error-async' PASS pasted and current (03_Error_Async_Config.txt#7174fb324883, 00_Assigments.md#638de5aac707, 01_Grounding_Dossier.md#854cbb11bc06, 01_Universe_Inject.sql#3acbfad93f4a, __context__#50e89bdae5e1, __assignment__#7709f2a35b0e, __policy__#dc4ab5df3cdd, __gate_policy__#6bbf415e008b, __review__#cb4fae31202a)
[PASS] structure.sections: 14 required sections present and non-empty (04_Prompt_Writing_Brief.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Writing_Brief.md
[PASS] evidence.situation: 3/3 items carry a source pointer (min 100%)
[PASS] evidence.final_state: 32/32 items carry a source pointer (min 100%)
[PASS] evidence.discovery_map: 22/22 items carry a source pointer (min 100%)
[PASS] evidence.dates: 10/10 items carry a source pointer (min 100%)
[PASS] evidence.entity_traps: 7/7 items carry a source pointer (min 100%)
[PASS] tool.search_as_persona: 22 facts proven findable by persona_view search as julia_lawson
[PASS] reach.brief: 26 scoped load-bearing ids YES for julia_lawson
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] structure.accepted_outcomes: V3 accepts multiple fair outcomes; see v3.fair_outcomes_review
[PASS] boundary.anchor_naming: 3 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 15 evidenced counter-readings (of 15 found; need ≥ 6) in 04_Prompt_Writing_Brief.md
[PASS] review.coverage: self-review addresses all 6 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.fair_outcomes_review: current accepted outcomes and considered alternatives recorded; multiple fair outcomes are allowed
[PASS] readiness.context: explicit task/revision and current upstream evidence verified
[PASS] handoff.pasted: pasted into the Self-review by --paste
```
