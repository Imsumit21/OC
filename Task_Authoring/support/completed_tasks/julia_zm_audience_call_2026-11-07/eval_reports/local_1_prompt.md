## PROMPT EVALUATION REPORT

### Task: Julia settles Leonard's "cards earlier" audience call from the friend sessions, then fills the Register tab, writes the memo, closes out the session tickets and posts the call and Brian's go/no-go
### Assigned Persona: Julia Lawson - Product Manager (julia.lawson@harmonygames.co)
### Assigned Business Function: Product
### Assigned Competency: Marketing and GTM
### Assigned Task Skill: Analysis and synthesis
### Assigned Horizon: long-horizon (Difficulty Mode: medium)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Inputs: prompt `Evals/task_inputs/04_Prompt.txt` (saved rev 17, sha256 `c3da944d…`, identical to `Task_Authoring/task_inputs/04_Prompt.txt`); assignment `Evals/task_inputs/00_Task_Assigned_Inputs.md` (all five fields stated); SQL `Evals/task_inputs/01_Universe_Inject.sql` rev9 (sha256 `3a98aa36…`). Friction: none (`03_Error_Async_Config.txt`, all fields empty). Reference files: none; `02_Reference_Files/` holds only a README. Dynamic context: none. No comparison samples were supplied.

Earlier reviews: the archived local PASS (2026-11-08) covered an older prompt (`729d3623…`) on rev7 data with 60 sessions. The /prompt FAIL 2 that led to rev9 is not saved on disk, so no portal or reviewer report exists for these exact inputs. This review is NEW on every phase.

---

### Injection Gate
- State: CURRENT. `hg_injection_gate.py` matched the saved SQL to the reviewed hash.
- Reviewed SQL sha256: `3a98aa36aaddb72cfe833311ca57760c002aef26929d3a82ccba309ed247b52d`. Eval 0 verdict: PASS / COMPLETE (`Evals/task_inputs/reports/0_injection.md`, injection-static-v2, 2026-11-09). Its Check C records `time_order_check.py` Part 1 PASS and Part 2 worked through (35 pointers: 11 OK, 24 N/A, 0 forward).
- Eval 0 findings on records this prompt depends on: two advisories, neither scored here.
  - The L881 Slack id `9c4e7a1d…` doesn't follow sha256(channel|ts). That is Leonard's coaching rule, which the answer does read. But the id never changes a value, set, order, recipient or destination the answer is graded on, so it stays an advisory.
  - The 'Friday at Claire's' calendar event has no invitation mail. The answer does not use it.

---

### Phase 1: Prompt Structure & Persona

**Persona:** PASS (5)
- Julia Lawson is the exact roster entry (`julia_lawson`, Product Manager, Product). She owns the workbook, the log note and the criteria deck, and she relayed Leonard's note to the team (C0880U9751A, 2025-09-22T15:30Z). Leonard's ask is addressed to her. The voice is short, lowercase Slack-style delegation, which fits a PM handing off a read.
- Role plausible: yes. Access plausible: yes (all sources are in her channels, mailbox or Drive shares, or in unscoped services). Responsibility scope: yes (she runs the session log and owes Leonard the call).

**Assigned Competency:** PASS (5)
- Marketing and GTM: the work is an audience-segment read (casual against RPG players) that decides which audience the game is pitched to before a change ships. This is audience and positioning work, a defensible GTM fit. It is not a PRD or roadmap write-up, though it feeds a roadmap card.

**Assigned Task Skill:** PASS (5)
- Analysis and synthesis is clearly present. 82 sessions are spread over notes Docs, observer mails, tickets, contacts and a late form. Each must be filtered by eight rules from five sources, the per-audience means computed and compared against the lead criteria, and the panel and retention context synthesised into a memo.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. PASS (5)
- Ambiguity: the prompt names no rule, number or session set. Every rule lives in records Julia can open.
- Dynamic Change: later records supersede earlier ones.
  - Claire's Sep 26 form says no coaching; her Sep 29 mail says she took the players through the game.
  - ZOM-567 is closed 'Vision Bot run #15 green'; rc_27 says the job runs in the editor with no phone.
  - The KPI sheet's 'D7 mean 8.63' is overridden by Vincent's cutoff note and Robert's install-weighted rule.
  - Owen's late form arrives after the ticket batch.
- Multi-Source: the needed facts sit in Slack, Gmail, Drive/Docs/Sheets/Slides, Linear, Contacts, Snowflake and Trello, and there are visible decoys.
- Data seeding: PASS. The prompt is 6 sentences and 125 words, and every operating rule is seeded in the environment.

**Naturalness:** PASS (5)
- It reads like a real Slack request: first person, lowercase, no headings or bullets, and no polished connectives ('Additionally', 'Please ensure'). The asks are plain and the sentence lengths vary. There are no staged typos or emoji.

**Anti-Patterns:**
| Pattern | Status |
|---------|--------|
| Command List | PASS. The deliverables are listed once in one sentence, with no order or sequencing words (first/then/finally). |
| Bolt-On | PASS. Every sentence serves Leonard's ask: the call drives the Register, the memo, the tickets, the reply and Brian's go/no-go. Removing any sentence loses a needed ask or authorization. |
| Pre-Solving | PASS. No rule, cause, count or outcome is stated, and "keep or hold" repeats Leonard's own option pair. |
| Tool Mention | PASS. There are no tool or parameter names and no "tool" or MCP wording. "register tab", "workbook", "drive folder", "tickets" and "thread" are natural service nouns. |

**Diversity:** goes well beyond "investigate + post one Slack message". Writes: a Sheets tab fill, Log-row appends, a new Doc placed in a folder, Linear state changes, comments and new issues, a Slack thread reply and a channel post.

---

### Phase 2: Depth Assessment

#### Requirement ledger

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| One audience call: casual, RPG or no clear lead → keep/hold | Leonard's ask (L889); feedback note (base C090N54TG79 /537); Leonard's updates (L873 gate post, L877 industry, L879 friends, L881 coaching, L883 build 1943); gate doc (L174); criteria deck (L360); 80 notes Docs; ZOM-568..647 and their device comments; 17 form mails plus Owen's late form (L434); Claire's mail (L508); Brian's DM (L871); contacts jobs; QA matrix (L901) | Slack #zombie-design history and DMs → gate doc → Drive search for the notes Docs and deck → Gmail forms → Linear tickets → Contacts search → #zombie-bugs QA thread | `slack_*` reads, `gdocs`/`gdrive` reads, `gslides` reads, `gsheets_values_get`, `gmail` reads, `linear` reads, `contacts_search_contacts` | Member of C090N54TG79, C08R27X0EAH, D076RBM29JS, D05GU6L0XFH; owner or share on every Doc/Sheet/Slides; own mailbox; Linear/Contacts/Trello unscoped | Casual 3.833 (n 27) vs RPG 3.500 (n 18), gap 0.333 → casual lead → HOLD |
| Fill the Register tab | Register tab header 'one row per session' (L342) | Julia's workbook | `gsheets_values_update` / `gsheets_values_append` | Owner | 82 rows: ticket, audience, stars, verdict, reason |
| New tickets and Log rows for the late form | Julia's log note (L176): "Any form that comes in after this batch gets a ticket and a log row when I see it." | Gmail → log note | `linear_create_issue`, `gsheets_values_append` | Own note and own workbook; Linear unscoped | 2 new ZOM tickets (Ayşe Polat, Daniel Hughes), 2 Log rows |
| Memo in Julia's folder | Leonard (L889) "put it in a memo, what goes in it is on the roadmap card"; card L858 "the audience call and the numbers behind it, with the panel and retention as context" and "memo goes in Julia's folder with her log note" | Trello search → card | `gdocs_create_document` + `gdrive_move_file` to `d_8140f09bf9f1b94cb8ee2d` | Owner of the folder; Trello unscoped | Memo: hold, counts and means; panel 3.33 (9 players, void removed per L875); retention 10.47% install-weighted D7 (16 cohort rows, 2,607 installs, cohort weeks from 2025-07-28 that have a D14 figure) |
| Close out the session tickets | Log note: "counted goes to Done, not counted goes to Canceled"; Robert's DM (L885): "put a re-run note on it so the observer runs it again" | Drive → log note; DM | `linear_update_issue` (state), `linear_create_comment` | Unscoped; own note; DM member | 45 Done, 37 Canceled; re-run notes on the 13 build-1943 drops |
| Reply in Leonard's thread | L889 "reply here with keep or hold" | #zombie-design | `slack_send_message` with `thread_ts` 1759266627.418203 | Member | "hold" |
| Tell Brian in #zombie-design | L889 "tell @Brian in this channel whether the tutorial and level order work goes on"; Robert's Monday post (base /731) | #zombie-design | `slack_send_message` to C090N54TG79 | Member, and Brian is a member | The tutorial and level order work does not go on (the change is held) |

Incorporation (prompt-incorporation-v1):
- The prompt incorporates Leonard's message ("his message says what he needs") and his feedback note ("the ones that came out of his feedback note").
- Leonard's later posts are his own updates to that note: each opens "on the feedback note" or "One more for the feedback note", or is his reply about watching people play. They incorporate through it, as does the gate doc his L873 update points to.
- The roadmap card is incorporated by Leonard's message, and it points to Julia's log note.
- Robert's re-run rule is a DM instruction to Julia about the same session close-out the prompt delegates. It is the least explicit link in the chain (see Recommended Improvements 2).

#### 2.1 Unique Ground Truth: PASS (5)

### Unique Ground Truth comparison

Unique Ground Truth: PASS 5

Basis: Every call-flipping fork is settled by a persona-visible record: the feedback note and Leonard's updates to it (game industry, friends, coaching, gate doc, build 1943), Julia's log note on late forms, the QA matrix pass, Claire's mail, Brian's DM and the contact job fields. Only reading A survives; it gives a casual lead and HOLD.

Alternative selection: Each of B to G is a single-rule change that flips hold to keep, so each is a non-trivial alternative backed by a visible record or decoy (the logged rows, the contacts left unread, ZOM-567 and Vision Bot, Claire's form, the friends clarification, the build number). Memo figures and ticket handling were also checked: panel 3.33 is settled by Leonard's void rule, ticket states and re-run notes by the log note and Robert's re-run rule. H is the one open figure: retention 10.47% (warehouse) or 10.59% (KPI sheet), both allowed by Vincent's note, recorded as BOTH\_FAIR\_FIGURE; it does not change the call or any write.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Apply the feedback note and Leonard's updates to it, the gate doc and the facts in the records: Owen's two late sessions are friend sessions and get tickets and Log rows; Alper Koçak (ZOM-598) and Arda Keskin (ZOM-622) work in games; the QA matrix's real-device SM-A546E pass covers the Samsung sessions; Claire's 13 coached, Brian's 9 Kadıköy and 13 build-1943 sessions do not count. | Casual lead (casual mean 3.833 over 27 vs RPG 3.500 over 18; gap 0.333 &gt;= 0.25; both &gt;= 6) so HOLD the cards earlier change | Create two ZOM tickets and two Log rows for Owen's late form; fill the Register (82 rows); create the memo Doc in Julia's folder; set every session ticket Done or Canceled with re-run notes on the build drops; post a thread reply to Leonard; post to Brian in \#zombie-design | Register tab of ZM audience sessions; Log tab of the same workbook; Julia's Drive folder d\_8140f09bf9f1b94cb8ee2d; ZOM-568..ZOM-647 plus two new ZOM tickets; thread under Leonard's post b07f1e10 in \#zombie-design; \#zombie-design post to Brian | Register: 45 counted / 37 not counted (11 game industry, 13 coached, 13 build) with reasons; 45 Done, 37 Canceled, re-run notes on the 13 build drops; memo with the casual call, counts and means, panel 3.33 and retention 10.47% as context; reply 'hold'; Brian told the tutorial and level order work does not go on | S\_ASK (Evals/task\_inputs/01\_Universe\_Inject.sql lines 889-889): "I want to settle the cards earlier change from Monday on what players told us, not on our gut. give me one audience call from the friend sessions: casual, RPG or no clear lead. casual lead means we hold the change. RPG lead means we keep it. no clear lead, we keep it"; S\_CRIT (Evals/task\_inputs/01\_Universe\_Inject.sql lines 360-360): "The lead is the higher mean star rating over counted sessions.\\nAt least 6 counted sessions per audience.\\nA gap under 0.25 is no clear lead." |
| B | Read only the 80 sessions already ticketed and logged; Owen's late form stays out of this read. | No clear lead (casual 3.788 over 26 vs RPG 3.618 over 17; gap 0.170) so KEEP | Fill the Register (80 rows); create the memo Doc; set the 80 tickets Done/Canceled with re-run notes; thread reply; Brian post | Register tab; Julia's Drive folder; ZOM-568..ZOM-647; Leonard's thread; \#zombie-design | Register: 80 rows; no new tickets; memo with no clear lead; reply 'keep'; Brian told the work goes on | S\_LOGNOTE\_TIX (Evals/task\_inputs/01\_Universe\_Inject.sql lines 176-176): "So each session gets a ZOM ticket, and the workbook log has a row per ticket." |
| C | Do not use the players' jobs in Julia's contacts; only Brian's Kadıköy group is game industry. | No clear lead (casual 3.768 over 28 vs RPG 3.579 over 19; gap 0.189) so KEEP | Create two ZOM tickets and two Log rows for Owen's late form; fill the Register (82 rows); create the memo Doc in Julia's folder; set every session ticket Done or Canceled with re-run notes on the build drops; post a thread reply to Leonard; post to Brian in \#zombie-design | Register tab of ZM audience sessions; Log tab of the same workbook; Julia's Drive folder d\_8140f09bf9f1b94cb8ee2d; ZOM-568..ZOM-647 plus two new ZOM tickets; thread under Leonard's post b07f1e10 in \#zombie-design; \#zombie-design post to Brian | Register: ZOM-598 and ZOM-622 counted; 47 Done / 35 Canceled; memo with no clear lead; reply 'keep'; Brian told the work goes on | S\_BRIANDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 871-871): "Kadıköy ekibi komple oyun sektöründen, hepsi mobil oyun şirketlerinde çalışıyor" |
| D | Treat the Samsung sessions as uncovered: Vision Bot is editor-only, so no pass ran on a Samsung phone; drop the 13 Samsung sessions with re-run notes. | No clear lead (casual 3.667 over 18 vs RPG 3.607 over 14; gap 0.060) so KEEP | Create two ZOM tickets and two Log rows for Owen's late form; fill the Register (82 rows); create the memo Doc in Julia's folder; set every session ticket Done or Canceled with re-run notes on the build drops; post a thread reply to Leonard; post to Brian in \#zombie-design | Register tab of ZM audience sessions; Log tab of the same workbook; Julia's Drive folder d\_8140f09bf9f1b94cb8ee2d; ZOM-568..ZOM-647 plus two new ZOM tickets; thread under Leonard's post b07f1e10 in \#zombie-design; \#zombie-design post to Brian | Register: 13 Samsung sessions not counted (device); 32 Done / 50 Canceled with 26 re-run notes; reply 'keep'; Brian told the work goes on | S\_GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 174-174): "A Samsung session counts once we have a clean pass covering that device." |
| E | Take the observers' forms at face value: Claire's form says no coaching, so her 13 sessions count. | No clear lead (casual 3.833 over 27 vs RPG 3.984 over 31; gap -0.151) so KEEP | Create two ZOM tickets and two Log rows for Owen's late form; fill the Register (82 rows); create the memo Doc in Julia's folder; set every session ticket Done or Canceled with re-run notes on the build drops; post a thread reply to Leonard; post to Brian in \#zombie-design | Register tab of ZM audience sessions; Log tab of the same workbook; Julia's Drive folder d\_8140f09bf9f1b94cb8ee2d; ZOM-568..ZOM-647 plus two new ZOM tickets; thread under Leonard's post b07f1e10 in \#zombie-design; \#zombie-design post to Brian | Register: Claire's 13 counted; 58 Done / 24 Canceled; reply 'keep'; Brian told the work goes on | S\_NOTE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C090N54TG79/2025-09.json pointer /537/text): "No coaching, just observe and collect honest reactions." |
| F | Count Brian's Kadıköy group, whose notes doc gives 'Kadıköy ekibi' as the relation, as people he knows. | No clear lead (casual 3.833 over 27 vs RPG 3.926 over 27; gap -0.093) so KEEP | Create two ZOM tickets and two Log rows for Owen's late form; fill the Register (82 rows); create the memo Doc in Julia's folder; set every session ticket Done or Canceled with re-run notes on the build drops; post a thread reply to Leonard; post to Brian in \#zombie-design | Register tab of ZM audience sessions; Log tab of the same workbook; Julia's Drive folder d\_8140f09bf9f1b94cb8ee2d; ZOM-568..ZOM-647 plus two new ZOM tickets; thread under Leonard's post b07f1e10 in \#zombie-design; \#zombie-design post to Brian | Register: Brian's 9 counted; 54 Done / 28 Canceled; reply 'keep'; Brian told the work goes on | S\_REL (Evals/task\_inputs/01\_Universe\_Inject.sql lines 879-879): "friends just means people you know" |
| G | Count the build-1943 sessions, since 0.3.127 is the store version number. | No clear lead (casual 3.375 over 40 vs RPG 3.500 over 18; gap -0.125) so KEEP | Create two ZOM tickets and two Log rows for Owen's late form; fill the Register (82 rows); create the memo Doc in Julia's folder; set every session ticket Done or Canceled with re-run notes on the build drops; post a thread reply to Leonard; post to Brian in \#zombie-design | Register tab of ZM audience sessions; Log tab of the same workbook; Julia's Drive folder d\_8140f09bf9f1b94cb8ee2d; ZOM-568..ZOM-647 plus two new ZOM tickets; thread under Leonard's post b07f1e10 in \#zombie-design; \#zombie-design post to Brian | Register: the 13 build-1943 sessions counted, no re-run notes; reply 'keep'; Brian told the work goes on | S\_QA (Evals/task\_inputs/01\_Universe\_Inject.sql lines 901-901): ""0.3.127 (127)"" |
| H | Same counting and call as A; quote memo retention off Vincent's KPI sheet (cohort weeks from 2025-07-28 to 2025-09-08, install-weighted, both platforms pooled), as his note allows. | Casual lead (casual mean 3.833 over 27 vs RPG 3.500 over 18; gap 0.333 &gt;= 0.25; both &gt;= 6) so HOLD the cards earlier change | Create two ZOM tickets and two Log rows for Owen's late form; fill the Register (82 rows); create the memo Doc in Julia's folder; set every session ticket Done or Canceled with re-run notes on the build drops; post a thread reply to Leonard; post to Brian in \#zombie-design | Register tab of ZM audience sessions; Log tab of the same workbook; Julia's Drive folder d\_8140f09bf9f1b94cb8ee2d; ZOM-568..ZOM-647 plus two new ZOM tickets; thread under Leonard's post b07f1e10 in \#zombie-design; \#zombie-design post to Brian | Register: 45 counted / 37 not counted (11 game industry, 13 coached, 13 build) with reasons; 45 Done, 37 Canceled, re-run notes on the 13 build drops; memo with the casual call, counts and means, panel 3.33 and retention 10.59% as context; reply 'hold'; Brian told the tutorial and level order work does not go on | S\_KPINOTE2 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 346-346): "Whenever ZM retention is quoted, off the warehouse or off this sheet, use only cohort weeks starting on or after 2025-07-24." |

Explicit option inventory: The prompt names one explicit option pair for the reply: keep or hold.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "reply to him in his thread with keep or hold"

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| hold | RETAINED | A | The counted sessions give a casual lead, which Leonard maps to hold. Evidence: P (Evals/task\_inputs/04\_Prompt.txt): "keep or hold" |
| keep | EXCLUDED | B, C, D, E, F, G | Keep arises only under readings B to G, each excluded by a persona-visible record. Evidence: P (Evals/task\_inputs/04\_Prompt.txt): "keep or hold" |

Compared alternative: B
Resolution: EXCLUDED. The prompt defines the sessions as the friend sessions that came out of Leonard's feedback note, not as the logged rows, and Leonard asks for the call from the friend sessions. Owen's late form in Julia's mailbox reports two more such sessions. Julia's own log note says a form that comes in after the batch gets a ticket and a log row when she sees it, so the late sessions join the read.
Resolution evidence: S\_LOGNOTE\_LATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 176-176): "Any form that comes in after this batch gets a ticket and a log row when I see it."; S\_OWEN (Evals/task\_inputs/01\_Universe\_Inject.sql lines 430-430): "Two more, sorry these are late. Host: Owen Baker. Day: Sun Sep 28. 2 sessions, no coaching."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Keep versus hold. |
| writes | DIFFERENT | B creates no tickets or Log rows for Owen's late form. |
| destinations | DIFFERENT | B writes no new tickets. |
| contents | DIFFERENT | Register rows, counts, call and replies differ. |

Authority chain: P → S\_ASK → S\_ASK\_MEMO → S\_CARD → S\_LOGNOTE\_LATE

Resolution relevance challenge: B rests on the read being only the ticketed rows; the log note's late-form rule is the exact instruction for forms that arrive after the batch.
Delegation challenge: NOT_CLAIMED. No alternative call is accepted; the cited records exclude it.
Challenge evidence: S\_LOGNOTE\_LATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 176-176): "Any form that comes in after this batch gets a ticket and a log row when I see it."

Compared alternative: C
Resolution: EXCLUDED. Leonard's update to the feedback note excludes anyone who works in games. Julia's contacts give Alper Koçak's job as 'QA tester, console games publisher' and Arda Keskin's as 'Live ops producer, mobile games studio'.
Resolution evidence: S\_IND (Evals/task\_inputs/01\_Universe\_Inject.sql lines 877-877): "One more for the feedback note: game-industry people don’t count, and that goes for sessions already run too. Anyone who works in games plays it like we do"; S\_C\_ALPER\_JOB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 967-967): "'QA tester, console games publisher'"; S\_C\_ARDA\_JOB (Evals/task\_inputs/01\_Universe\_Inject.sql lines 1015-1015): "'Live ops producer, mobile games studio'"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Keep versus hold. |
| writes | SAME | Same kinds of write actions. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Register verdicts, ticket states, memo call, reply and Brian post differ. |

Authority chain: P → S\_IND

Resolution relevance challenge: The rule's condition is working in games; the contact job fields state that attribute for these two players.
Delegation challenge: NOT_CLAIMED. No alternative call is accepted; the cited records exclude it.
Challenge evidence: S\_IND (Evals/task\_inputs/01\_Universe\_Inject.sql lines 877-877): "One more for the feedback note: game-industry people don’t count, and that goes for sessions already run too. Anyone who works in games plays it like we do"

Compared alternative: D
Resolution: EXCLUDED. The gate doc defines a pass as a clean test run of the build players get and says a pass covers a device only if it ran on that device, then covers all Samsung sessions. Vincent's QA matrix has a real-device SM-A546E (Galaxy A) row on store build 0.3.127 (127) marked PASS, so the Samsung sessions count. Vision Bot being editor-only does not matter once this pass exists.
Resolution evidence: S\_GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 174-174): "A Samsung session counts once we have a clean pass covering that device. A pass covers a device only if it ran on that device. Once there is a pass, it covers all the Samsung sessions in the read."; S\_GATE\_PASS (Evals/task\_inputs/01\_Universe\_Inject.sql lines 174-174): "A pass is a clean test run of the build players get."; S\_QA (Evals/task\_inputs/01\_Universe\_Inject.sql lines 901-901): "\["Android current-gen", "SM-A546E", "yes", "0.3.127 (127)", "PASS", "2025-09-29", "Vincent Parker"\]"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Keep versus hold. |
| writes | SAME | Same kinds of write actions. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Register verdicts, ticket states, memo call, reply and Brian post differ. |

Authority chain: P → S\_GATEPOST → S\_GATE

Resolution relevance challenge: The gate's pass rule decides the Samsung sessions; the QA row is a run on a Samsung device of a store build.
Delegation challenge: NOT_CLAIMED. No alternative call is accepted; the cited records exclude it.
Challenge evidence: S\_GATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 174-174): "A Samsung session counts once we have a clean pass covering that device. A pass covers a device only if it ran on that device. Once there is a pass, it covers all the Samsung sessions in the read."

Compared alternative: E
Resolution: EXCLUDED. Leonard's update to the no-coaching part of the feedback note says a coached session doesn't count, whoever ran it, including sessions already run. Claire's later mail to Julia says she took the players through how ZM plays before they touched their phones.
Resolution evidence: S\_COACH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 881-881): "a coached session doesn''t count, whoever ran it. if the players were told how it plays before or while they played, it''s our explanation we''re watching, not their honest reaction. that goes for sessions already run too"; S\_CLAIRE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 508-508): "Before anyone touched their phone I sat them all down and took them through how ZM plays"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Keep versus hold. |
| writes | SAME | Same kinds of write actions. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Register verdicts, ticket states, memo call, reply and Brian post differ. |

Authority chain: P → S\_COACH

Resolution relevance challenge: The rule's condition is being told how it plays before play; Claire's mail states exactly that for her Friday sessions.
Delegation challenge: NOT_CLAIMED. No alternative call is accepted; the cited records exclude it.
Challenge evidence: S\_COACH (Evals/task\_inputs/01\_Universe\_Inject.sql lines 881-881): "a coached session doesn''t count, whoever ran it. if the players were told how it plays before or while they played, it''s our explanation we''re watching, not their honest reaction. that goes for sessions already run too"

Compared alternative: F
Resolution: EXCLUDED. Leonard's update excludes game-industry people, and Brian told Julia the whole Kadıköy group works in mobile game companies. The friends clarification itself repeats the condition: 'don’t work in games'.
Resolution evidence: S\_IND (Evals/task\_inputs/01\_Universe\_Inject.sql lines 877-877): "One more for the feedback note: game-industry people don’t count, and that goes for sessions already run too. Anyone who works in games plays it like we do"; S\_BRIANDM (Evals/task\_inputs/01\_Universe\_Inject.sql lines 871-871): "Kadıköy ekibi komple oyun sektöründen, hepsi mobil oyun şirketlerinde çalışıyor"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Keep versus hold. |
| writes | SAME | Same kinds of write actions. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Register verdicts, ticket states, memo call, reply and Brian post differ. |

Authority chain: P → S\_IND

Resolution relevance challenge: Brian's DM states the Kadıköy group's industry, which is the condition the rule tests.
Delegation challenge: NOT_CLAIMED. No alternative call is accepted; the cited records exclude it.
Challenge evidence: S\_IND (Evals/task\_inputs/01\_Universe\_Inject.sql lines 877-877): "One more for the feedback note: game-industry people don’t count, and that goes for sessions already run too. Anyone who works in games plays it like we do"

Compared alternative: G
Resolution: EXCLUDED. The gate doc says dev builds do not count and a dev build is anything that never went through a store; Leonard says android 1943 never went through a store.
Resolution evidence: S\_GATE\_BUILD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 174-174): "Sessions on dev builds do not count. A dev build is anything that never went through a store."; S\_1943 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 883-883): "careful with android 1943, the one that’s been passed around. it never went through a store"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Keep versus hold. |
| writes | SAME | Same kinds of write actions. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Register verdicts, ticket states, memo call, reply and Brian post differ. |

Authority chain: P → S\_GATEPOST → S\_GATE\_BUILD

Resolution relevance challenge: Leonard names build 1943 as never having gone through a store, which is the gate's dev-build test.
Delegation challenge: NOT_CLAIMED. No alternative call is accepted; the cited records exclude it.
Challenge evidence: S\_GATE\_BUILD (Evals/task\_inputs/01\_Universe\_Inject.sql lines 174-174): "Sessions on dev builds do not count. A dev build is anything that never went through a store."

Compared alternative: H
Resolution: BOTH_FAIR_FIGURE. Only the memo's retention context figure differs. Robert's method applied to the warehouse gives 10.47% (16 rows, 2,607 installs, including the 2025-09-15 cohorts that carry a D14 figure); applied to Vincent's KPI sheet, which stops at 2025-09-08, it gives 10.59% (14 rows, 2,267 installs). Vincent's newer note authorizes quoting off either source.
Resolution evidence: S\_RET (Evals/task\_inputs/01\_Universe\_Inject.sql lines 887-887): "when we quote ZM retention let''s use install-weighted D7, not a simple mean of the cohorts. Mature cohorts only, meaning cohorts that have a D14 figure, both platforms pooled. USER\_COHORT\_RETENTION has what you need"; S\_KPINOTE2 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 346-346): "Whenever ZM retention is quoted, off the warehouse or off this sheet, use only cohort weeks starting on or after 2025-07-24."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Both HOLD. |
| writes | SAME | Identical write set. |
| destinations | SAME | Identical destinations. |
| contents | DIFFERENT | Memo retention figure 10.47% versus 10.59%. |

Both-fair figure: RATE, Memo retention (install-weighted D7, mature cohorts from 2025-07-24)
Value for A: 10.47%. Evidence: S\_RET (Evals/task\_inputs/01\_Universe\_Inject.sql lines 887-887): "when we quote ZM retention let''s use install-weighted D7, not a simple mean of the cohorts. Mature cohorts only, meaning cohorts that have a D14 figure, both platforms pooled. USER\_COHORT\_RETENTION has what you need". Derivation: USER\_COHORT\_RETENTION zombie\_match\_3d, cohort\_week 2025-07-28..2025-09-15 with d14\_ret not null, both platforms: sum(installs\*d7\_ret)/sum(installs) = 272.98/2607 = 10.47
Value for H: 10.59%. Evidence: S\_KPINOTE2 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 346-346): "Whenever ZM retention is quoted, off the warehouse or off this sheet, use only cohort weeks starting on or after 2025-07-24.". Derivation: KPI tab of f\_4e21b203a62910bdae0353, cohort weeks 2025-07-28..2025-09-08, both platforms: sum(installs\*d7)/sum(installs) = 239.98/2267 = 10.59
Newer source check does not settle it: Vincent's Sep 30 note is newer than Robert's Sep 29 rule and allows either source.
Authority check does not settle it: Robert sets the method and Vincent the cutoff; neither ranks warehouse over sheet.
Source identity check does not settle it: Robert points to USER\_COHORT\_RETENTION, but Vincent's later note expressly adds 'off this sheet'.
Scope check does not settle it: Both figures are ZM install-weighted D7 over mature cohorts from the cutoff; they differ only in the sheet's snapshot end.
Same material result check does not settle it: The memo figure differs while the call and writes do not.
Every explicit ask: Both readings complete every ask: Register, tickets, memo, reply and Brian post.
Next step unchanged: Retention is context only ('Sessions decide. Panel and other numbers are context.'); the call stays HOLD.
Rubric must accept: 10.47% or 10.59%

Resolution relevance challenge: Vincent's note names both the warehouse and the sheet as quotable sources, so no record ranks the two figures.
Delegation challenge: NOT_CLAIMED. No delegation claimed; the fork is a both-fair figure.
Challenge evidence: S\_KPINOTE2 (Evals/task\_inputs/01\_Universe\_Inject.sql lines 346-346): "Whenever ZM retention is quoted, off the warehouse or off this sheet, use only cohort weeks starting on or after 2025-07-24."

Strongest-alternative challenge (B): B is the most natural reading for an agent that works from the workbook: the 80 logged rows look like the full set, and Owen's late mail is a reply in an older thread. It flips the call, so it is not a strawman.
Challenge evidence: S\_LOGNOTE\_LATE (Evals/task\_inputs/01\_Universe\_Inject.sql lines 176-176): "Any form that comes in after this batch gets a ticket and a log row when I see it."

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

#### 2.2 Feasibility: PASS (5)
- Tool feasibility: every write has a cataloged tool, listed in the ledger.
  - The memo is a native Google Doc, so there's no export-format question.
  - `gdocs_create_document` takes title and bodyText, and `gdrive_move_file` places it under `d_8140f09bf9f1b94cb8ee2d`.
  - The ZOM team's Done and Canceled states are in use in base Linear (Done 427, Canceled 20).
  - Slack replies take `thread_ts`.
- Data feasibility: every fact the answer needs exists.
  - 80 notes Docs carry age, relation, build, audience, stars and coaching; ZOM device comments carry the phone.
  - Owen's late form carries all fields for its two sessions.
  - Contacts carry jobs (Alper Koçak 'QA tester, console games publisher'; Arda Keskin 'Live ops producer, mobile games studio').
  - The QA matrix carries a real-device SM-A546E PASS on 0.3.127 (127).
  - The panel stars are in Leonard's forward. USER_COHORT_RETENTION carries installs, d7_ret and d14_ret by cohort week and platform.
- Dimensional feasibility: the per-audience split uses the observer label (Audience field in every notes Doc, ticket and Log row). Per-session device, build, relation, age and job fields exist.
- Numeric observability: the means are averages of half-star values. The panel is 30/9 = 3.333, from integer and half-star inputs in a mail body. Retention: `snowflake_execute_query` over USER_COHORT_RETENTION returns installs and d7_ret to 2 decimals, which is enough for an install-weighted mean to 2 decimals (10.47). Rendering is inferred from catalog parameters (evidence limit).
- Persona-scoped reads (acl.md matrix: Gmail, Slack, GCal, GDrive, GDocs, GSheets and GSlides are scoped):
  - Slack sources sit in C090N54TG79 (Julia a member), C08R27X0EAH (member), D076RBM29JS (Julia–Brian DM) and D05GU6L0XFH (Julia–Robert DM).
  - The Gmail forms are Julia's mailbox copies.
  - Every Doc, Sheet and Slides file is owned by or shared with Julia: the gate doc, the KPI sheet and the QA matrix are shared, and all 80 notes Docs list her.
  - Arthur's rc_27 is mirrored only in #zombie-prs (Julia not a member), but GitHub is unscoped, and the answer does not need it once the QA pass is found.
- Ask-level ACL: no ask directs a read outside Julia's view.

#### 2.3 Truthfulness: PASS (5)
Premises PR1–PR11 are verified in the record. None is contradicted or unresolved.

| Prompt claim | Record | Verdict |
|---|---|---|
| "leonard asked me in #zombie-design for the audience call on the friend sessions" | L889, C090N54TG79 = zombie-design (channels.json /132/name), 2025-09-30T21:10:27Z, tags Julia: "give me one audience call from the friend sessions" | Verified |
| "the ones that came out of his feedback note" | base /537: "get real-life feedback from 25–45 casual and/or RPG gamer friends"; Leonard's later posts say "on the feedback note" | Verified |
| "settle the cards earlier change on what players told us" | L889: "settle the cards earlier change from Monday on what players told us"; Robert's Mon Sep 29 post /731 "move up card introduction earlier" | Verified |
| "his message says what he needs" | L889 gives options, mapping, memo/card, reply and Brian post | Verified |
| "the register tab in my audience sessions workbook" | 'ZM audience sessions', owner julia.lawson; tab 'Register' (L342) | Verified |
| "the memo he asked for" | L889 "put it in a memo" | Verified |
| "my drive folder" | Julia's root folder `d_8140f09bf9f1b94cb8ee2d` holds the log note; the card says "memo goes in Julia's folder with her log note" | Verified |
| "the session tickets" | ZOM-568..ZOM-647 'Friend session: …', Todo, assignee Julia | Verified |
| "his thread" | Leonard's top-level post; "reply here with keep or hold" | Verified |
| "brian in #zombie-design" | EMPLOYEE_0026 (Brian Foster) in C090N54TG79 members | Verified |
| "the tutorial and level order work" | /731 "Brian will make the changes in the tutorial … shuffle the levels"; L889 names it | Verified |

Phantom tight-identifier search: one tight identifier, #zombie-design, exists exactly. There are no ticket ids, amounts, dates or fiscal periods in the prompt. State premises: nothing is treated as done after the clock, and every named person is active in September 2025.

#### 2.4 Cross-Service Requirement: PASS (5)
Each required service changes a graded fact:
- Slack: Leonard's ask, his rule updates, the 1943 build rule, the re-run rule and Brian's industry statement; writes the reply and the Brian post.
- Gmail: Claire's coaching admission and Owen's two late sessions, each of which flips the call.
- Drive/Docs/Sheets/Slides: the notes fields, the gate doc, the lead criteria, the QA pass that admits the Samsung sessions, the Register and the memo.
- Linear: the device per session and the close-out writes.
- Contacts: two game-industry jobs, which flip the call.
- Snowflake: the retention figure in the memo.
- Trello: the memo's contents and folder.

There is information friction and there are several writes.

#### 2.5 Investigation + Action: PASS (5)
Investigation over about 100 records feeds the call and every write: Register verdicts, ticket states, re-run notes, memo, reply and Brian post. The call cannot be made without the reads.

#### 2.6 Clarity & Specificity: PASS (5)
- Intent is clear: one call, five named deliverables with named destinations.
- Delegation scan: no "I'll …" self-action; "you don't need my ok on any of it, post and update everything under my name" delegates all writes.
- Write-action divergence: B to G in the UGT table only change contents (B also adds or omits two tickets), and each is excluded by a record. "no clear lead" maps to keep, so "not a maybe" never forces a third reply.

#### 2.7 Contrived vs Natural Difficulty: PASS (5)
- No exact timestamps, opaque ids, filenames, format rules or prescribed reply format beyond Leonard's own keep/hold.
- No trap hints or riddles: "he has to act on this, so give him one call, not a maybe" restates Leonard's need and hints at no trap.
- No hidden destination: workbook, folder, thread and channel are all named the way Julia would name them.
- No audit-form wording or if-chains.
- Spec-sheet triggers: 0 of 4. The deliverables are named, not their contents.
- Difficulty comes from records: cohort filtering by rules in several places, a late form, contacts jobs, a superseding mail, an editor-only "green" decoy and a real-device pass.
- Long Horizon anti-inflation: the per-session reads answer distinct questions over a source-defined cohort of 82 sessions. No bulk result replaces them: the device is only in ticket comments, the job only in contacts, and coaching only in mail.

#### 2.8 Alignment with Today's Date: PASS (5)
The prompt uses no dates. "from Monday" in Leonard's ask resolves to Mon 2025-09-29 (Robert's 18:52Z post). Every relied-on record is dated at or before 2025-09-30T21:10:27Z, before the clock.

#### 2.9 Sample Similarity / Originality: N/A
No comparison samples were supplied.

---

### Phase 3: Universe Feasibility

**Data Existence:** PASS (5)
- Entities verified: 11 of 11 premises, plus every source in the ledger.
- All retrievable via MCP: yes. Slack, Gmail, Drive-family, Linear, Contacts, Snowflake and Trello reads are all cataloged.

**Cross-Service Coherence:** PASS (5). Scored fresh.
- Inconsistencies in task-touched data: none introduced. Static integrity is REUSED from Eval 0 (`0_injection.md`, Checks A–C PASS on `3a98aa36…`).
  - Checked fresh here: 80/80 Log rows match the notes Docs and tickets on date, observer, audience and stars.
  - Form session counts match the notes Docs.
  - Every injected Slack author is a member of the channel, and every SQL apostrophe is doubled (Eval 0).
- Pointer time-order: Eval 0 Part 1 PASS, Part 2 35/35 dispositioned, 0 forward. Rechecked here:
  - The gate doc (Sep 24 15:12Z) names "the Vision Bot job" and Arthur as its owner. The job posts in #ci from 2025-09-23T23:10Z and was built in DMs from Aug 27, so it already existed.
  - The roadmap card (Sep 30 16:52Z) points to the log note (16:24Z) and is pointed to by Leonard's ask (21:10Z).
  - Robert's "Vincent's retention post above" (Sep 29 17:30Z) points to base /730 (17:03Z).
- Designed stale records, consistent and later superseded:
  - ZOM-567 closed Done on 'Vision Bot run #15 green' (Sep 30 17:10Z); rc_27 (20:10Z) says no phone was in the loop.
  - Claire's form (Sep 26) is corrected by her Sep 29 mail.
  - KPI 'D7 mean 8.63' is narrowed by Vincent's Sep 30 note.
- Injection SQL considered: yes.
- Prompt-specific sources, access and configuration: supported. Friction none.
- PLATFORM:FD-3785: USER_COHORT_RETENTION has a D14 figure on the 2025-09-15 cohorts before their window closes. Robert's "cohorts that have a D14 figure" includes them (10.47%); excluding them gives 10.59%. The call does not depend on it (sessions decide), and this is not scored.

---

### Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|-----------|--------------|-------------|---------------|
| Prompt | Unique Ground Truth | 5 | Eight-reading comparison: B–G each excluded by a persona-visible record; H is a both-fair retention figure (10.47% or 10.59%) |
| Prompt | Feasibility | 5 | All writes cataloged; all data present; numeric values observable |
| Prompt | Persona ACL Reachability | 5 | Every scoped read is in Julia's channels, mailbox or Drive shares |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 5 | One call, named deliverables and destinations, no write divergence |
| Prompt | Contrived / Unnatural | 5 | Natural delegation; 0 register triggers; no hints, ids or hidden destinations |
| Prompt | Alignment with Today's Date | 5 | "from Monday" = Sep 29; all sources before the clock |
| Prompt | Originality / Sample Similarity | N/A | No samples supplied |
| Prompt | Truthfulness | 5 | 11/11 premises verified |
| Prompt | Tool Use & Cross-service | 5 | Seven services each change a graded fact; several writes |
| Prompt | Investigation + Action | 5 | Reads feed every write |
| Prompt | Coherence (Bolt-on) | 5 | No bolt-on |
| Prompt | Persona | 5 | Exact roster identity; natural PM request |
| Prompt | Business Function | 5 | Product, matching Julia's department |
| Prompt | Assigned Competency | 5 | Audience-segment GTM read |
| Prompt | Assigned Task Skill | 5 | Multi-rule cohort synthesis |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three load-bearing; short trigger |
| Universe | Data Exists | 5 | All entities retrievable |
| Universe | Cross-Service Coherence | 5 | No task-touched inconsistency; FD-3785 is platform |

---

### Issues Found

| # | Issue | Severity | Dimension |
|---|-------|----------|-----------|
| 1 | Memo retention context figure has two fair values (10.47% warehouse, 10.59% KPI sheet); recorded as BOTH_FAIR_FIGURE, so the rubric must accept either | Minor (no score change) | Unique Ground Truth |
| 2 | Leonard's coaching-rule Slack id (SQL L881) does not follow sha256(channel, ts); Eval 0 advisory, unscored here | Minor (advisory) | Injection Gate |
| 3 | PLATFORM:FD-3785 premature D14 cells in USER_COHORT_RETENTION | Platform | Not scored |

### Recommended Improvements

1. (Injection, advisory) Change Leonard's coaching-rule Slack id at L881 from `9c4e7a1d03b85f26e1a4d70c5b2f9e38` to `a4721db4ba861c926965546ca48efbd9` (= sha256('C090N54TG79|1758819012.336518')[:32]), so `base_check.py` passes. Re-run /injection afterwards; the prompt is unaffected.
2. (For /rubric) Two writes rest on the least explicit incorporation links:
   - the re-run notes on the 13 build-1943 drops (Robert's DM D05GU6L0XFH 2025-09-26);
   - the two new tickets and Log rows for Owen's late form (Julia's log note).

   Both are settled by records Julia can open, so the prompt passes. A criterion that grades them should cite those records in its own text.
3. (Portal risk, not scored) The gate doc's "Arthur Blake owns the Vision Bot job and says what its passes do and don't cover" (Sep 24) can read as a pointer to Arthur's Sep 30 PR comment, the only Arthur statement Julia can see. It is true at its edit time (Arthur's 2025-09-16 DM), but a portal reviewer may score it as a date slip. Optional SQL change: end that sentence after "owns the Vision Bot job", so it names the owner without implying a statement already on record.

---

## Deep Recheck

Passes: P1, P2, P3 and P4. Each ran as a fresh Opus 5.5 (claude-opus-5-5) subagent at session effort, all launched in parallel after the record was saved. Each got only the saved inputs under `Evals/task_inputs/` (not `reports/`), `Evals/SEARCH.md`, the persona folder, `common_errors.md` and `deep_recheck.md`. None saw the main review, the record, earlier reports or `Task_Authoring/`. P1 ran the same-sentence clause sweep over every session attribute, and P2 ran the pointer time-order sweep.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 6 prompt sentences plus 8 sentences of Leonard's ask. Clause sweep over 82 sessions; 19 forks; end state recomputed: HOLD, casual 3.833 (n 27) vs RPG 3.500 (n 18), 45 Done / 37 Canceled, 13 re-run notes | 1 | 1 (as BOTH_FAIR_FIGURE) |
| P2 | 6 sentences; seven services mapped to graded facts; pointer sweep; Snowflake derived columns | 2 | 1 (platform) |
| P3 | 22 premises; SQL ids, columns, authors, apostrophes | 1 | 0 |
| P4 | 6 sentences; every wording check | none | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| P1-DR1 | P1 | "write the memo he asked for and put it in my drive folder" | USER_COHORT_RETENTION zombie_match_3d, weeks 2025-07-28..2025-09-15 with d14_ret → 10.47%; KPI sheet f_4e21b203… rows to 2025-09-08 → 10.59%; Vincent's note: "Whenever ZM retention is quoted, off the warehouse or off this sheet, use only cohort weeks starting on or after 2025-07-24." | §2 which number | Unique Ground Truth | CONFIRMED (BOTH_FAIR_FIGURE) | Only the memo's retention context figure differs, and both values sit on records Julia can open. Vincent's later note allows either source, so none of the five checks ranks them. The decision, writes and destinations are identical. Recorded as reading H; the rubric must accept 10.47% or 10.59%. |
| P2-DR1 | P2 | "leonard asked me in #zombie-design for the audience call on the friend sessions, the ones that came out of his feedback note." | Gate doc f_748d26e7… (last edit 2025-09-24T15:30:02Z): "Arthur Blake owns the Vision Bot job and says what its passes do and don't cover."; rc_27 created 2025-09-30T20:10:26Z | Pointer time-order | Cross-Service Coherence | REJECTED | The sentence names Arthur's role. It does not point at a record, and the role statement was already true before the doc: Arthur in DM D06KV30TPL4, 2025-09-16T19:13Z: "1. Run Unity editor from command line 2. It runs the first instruction a. It puts editor in play mode". The job ran in #ci from 2025-09-23T23:10Z. Julia reaches Arthur's coverage statement through rc_27, which exists before the task clock (GitHub is unscoped), and the Samsung decision rests on the QA matrix row, not on Arthur. Kept as a portal-risk note under Recommended Improvements. |
| P2-DR2 | P2 | "fill in the register tab … write the memo he asked for …" | snowflake.json /tables/10 USER_COHORT_RETENTION, 2025-09-15 d14_ret 5.83 / 7.17 filled before the window closes | Derived columns | PLATFORM:FD-3785 | REJECTED (platform) | A known platform rollup defect, not scored. Its only effect on the answer is the memo retention figure, already recorded as BOTH_FAIR_FIGURE (P1-DR1). |
| P3-DR1 | P3 | "leonard asked me in #zombie-design for the audience call on the friend sessions, the ones that came out of his feedback note." | SQL L855–856 `github.github_review_comments` column `seq` | SQL columns | Data integrity | REJECTED | The 2026-10-04 live schema (`Task_Authoring/references/universe_schema_live.json`) lists `github_review_comments.seq` as NOT NULL with no default, so keeping it is required. Eval 0 resolved the same lint CHECK. |

Effect on verdict: unchanged. Every dimension stays at 5. The UGT record gains reading H (BOTH_FAIR_FIGURE).

Fork list:
- F1: settled | Owen's two late sessions (Ayşe Polat casual 5, Daniel Hughes RPG 1.5) are in the read with new tickets and Log rows | read only the 80 logged sessions (KEEP) | Settled by: log note "Any form that comes in after this batch gets a ticket and a log row when I see it." and Owen's mail "Two more, sorry these are late. Host: Owen Baker. Day: Sun Sep 28. 2 sessions, no coaching."
- F2: settled | 13 Samsung sessions count | dropped as uncovered (KEEP) | Settled by: gate "A pass covers a device only if it ran on that device. Once there is a pass, it covers all the Samsung sessions in the read." and QA matrix "SM-A546E, yes, 0.3.127 (127), PASS, 2025-09-29".
- F3: settled | Claire's 13 sessions not counted (coached) | counted per her form (KEEP) | Settled by: Claire's mail "Before anyone touched their phone I sat them all down and took them through how ZM plays" and Leonard "a coached session doesn't count, whoever ran it … that goes for sessions already run too".
- F4: settled | Brian's 9 Kadıköy sessions, ZOM-598 (Alper Koçak) and ZOM-622 (Arda Keskin) not counted | counted (KEEP) | Settled by: Brian's DM "Kadıköy ekibi komple oyun sektöründen", contacts jobs "QA tester, console games publisher" and "Live ops producer, mobile games studio", and Leonard "game-industry people don't count".
- F5: settled | 13 build-1943 sessions not counted, with re-run notes | counted (KEEP) | Settled by: gate "Sessions on dev builds do not count." and Leonard "android 1943 … never went through a store".
- F6: settled | age, friends, not kids and audience labels change no session | re-derive the labels or exclude relations | Settled by: Leonard "25–45 years old, not a headcount", "family, neighbours and old classmates count the same", and the deck "The observer's label stands, nothing gets re-derived." (all ages 26–44).
- F7: settled | panel 3.33 (9 players) | 3.10 (void kept) | Settled by: Leonard "if a rating is void it comes out of both the sum and the count" and the forward "Player 8's rating is void".
- F8: both fair | memo retention | 10.47% (warehouse) | 10.59% (KPI sheet) | Both fair: 10.47% or 10.59%, BOTH_FAIR_FIGURE; the rubric must accept either.
- F9: settled | memo in Julia's root folder `d_8140f09bf9f1b94cb8ee2d` | the Zombie Art subfolder | Settled by: card "memo goes in Julia's folder with her log note".
- F10: settled | counted → Done, not counted → Canceled, re-run notes only on technical drops | close all as Done, or leave the build drops open | Settled by: log note "counted goes to Done, not counted goes to Canceled" and Robert "If one gets dropped for a technical reason, device or build, put a re-run note on it … Dropped for anything else, no re-run, it just gets closed".
- F11: settled | the late sessions are not double-counted; Marcus's resend adds nothing | count Marcus's resend | Settled by: Marcus "Same sessions as before".
- F12: settled | Brian told that the tutorial and level order work does not go on | it goes on | Settled by: Leonard "casual lead means we hold the change" and Robert's Monday post tying Brian's tutorial and level shuffle to the cards-earlier change.

Platform defects: PLATFORM:FD-3785 (USER_COHORT_RETENTION 2025-09-15 D14 and 2025-09-22 D7 cells filled before their windows close; P2-DR2; its only effect is the both-fair retention figure F8).

### FINAL VERDICT: PASS

Score: 5

Execution status: COMPLETE

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Eval version: task-quality-v1
Eval release SHA-256: 3d51ac2867d2ce85946d4723cd9ad17c6a16d285f36ae548758157568b052b06
Reviewed prompt SHA-256: c3da944d7da5a32891a9c1e06664e6111bb3bccd1a1efe31bb0c713f7b795088
Review context SHA-256: fbd953016d9d04258a9256bcc520d7bf5207831f294dea581058f771b95f84aa
Prompt record SHA-256: 5f3b6edac271ca86bd5e49b8259e1feb88b8ebeb08d8ed0cd7cbbb5d7765e319

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /hardness on this prompt with rev9 SQL (sha 3a98aa36…). Before submitting, apply the advisory Slack-id fix at SQL L881 and re-run /injection. /rubric must accept retention 10.47% or 10.59%.

Evidence limits: static review only (the SQL was never executed; tool rendering is inferred from catalog parameters); the /prompt FAIL 2 that led to rev9 is not saved on disk, so its forks (coaching, Samsung, friends, ages, builds) were re-derived fresh rather than reconciled finding by finding; PLATFORM:FD-3785 is recorded and not scored.

**Lowest Dimension:** None. All scored dimensions are 5; Originality is N/A (no samples).

**Summary:** Leonard's ask, his feedback note and his updates to it, the gate doc and Julia's own records settle one end state. 82 sessions (80 logged plus Owen's 2 late ones): 45 counted, 37 not counted (11 game industry, 13 coached, 13 build). Casual 3.833 vs RPG 3.500, so HOLD. Six call-flipping alternatives were each excluded by a persona-visible record, and four blind passes reached the same end state. The only open item is the memo's retention context figure, a both-fair 10.47% or 10.59%.
