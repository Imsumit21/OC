# Prompt Brief — frederick_dd_publishing · prep
> Built 2026-11-06 from 00_Assigments.md, Working_Files/00_Task_Context.json, 01_Grounding_Dossier.md, 01_Universe_Inject.sql (rev2; rev1 passed /injection and failed /prompt on one fork), 01_Scenario_Design.md, 01_Hardness_Manifest.json, solver/truth.json, 03_Error_Async_Config.txt and three blind passes (plan/sweep/) · Persona view verified: all · Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human.

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
|---|---|---|
| Business function | Executive | Maps to `task_categories.md` 'Founders / Exec / Strategy' (strategic decisions, priorities and executive coordination): the founders choose which publisher, if any, gets Domino Delights (hub frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com>; Leonard's Aug 25 post C07C2866011/1756140953.197759) |
| Persona | Frederick Stone, frederick.stone@harmonygames.co, Co-founder (roster frederick_stone; department Executive) | Voice: a co-founder handing his assistant a job Leonard gave him; plain, brief. Remit: he ran the Appodeal talks (frederick.stone@harmonygames.co/1830012626042968381), was handed the Rayking mail (frederick.stone@harmonygames.co/1842348778705877030) and opened publisher outreach on Sep 24 (D05S58U4SAK/1758736827.548589). Reads: his mailbox, calendar and Drive shares; #executives C07C2866011, #bridge-pitch C096HFA5Z8W, #analytics C069FF9Q57S, DM D05S58U4SAK |
| Competency | Finance | Taxonomy screen 9: 'Budget, forecast, cap table, fundraising'; outputs 'Models, spreadsheets, decks'. Here: a forecast model of publisher offers for a founders' decision, in a Google Sheet (rule doc f_5e355d03f6eb6a4e866ead 'Layout') |
| Task skill | Analysis and synthesis (stacked: Retrieval, Actions) | Screen 10 'Combine information from multiple sources and compute, model, reconcile, or diagnose to reach findings': reconcile each publisher's latest terms across term sheets, a calendar note, a card comment and Slack, then compute value and Q4 cash (f_5e355d03f6eb6a4e866ead) |
| Task type | long-horizon (Long Horizon → extreme profile; requester-confirmed volume and cohort exceptions in the manifest) | 10 services carry weight: Gmail (24 publisher threads, ESG thread), Drive and Docs (8 term sheets, rule doc), Sheets (outreach, model), Slides (one-pager), Slack (4 containers), Trello (UA/BD board), Calendar (3 calls), Linear (ENG-2362), Contacts, plus Snowflake (ANALYTICS.MONETIZATION.REVENUE_DAILY). hardness_gate PASS in the dossier. 26 publishers, 86 write objects |

## 2 · Situation

| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |
|---|---|---|---|
| The founders meet on Monday Oct 6 to decide on Domino Delights publishing; Leonard has asked Frederick for a model of what each publisher would bring in, with follow-up on the board and in Contacts | Frederick (To, INBOX) | hub frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com>; event evt_881d3e07c598b2205a7ff3; card 68dab660c900179df4f5f92d | Leonard's mailbox copies; P&L workbooks (not needed, dossier 'Known data issues') |

## 3 · Investigation → action

Questions the run must resolve (answers only in §5 and the records, never in the prompt):
1. Who is in: the outreach sheet plus any publisher that came to one of the four founders about DD since Apr 1, 2025, however it reached them, less passed-along names and co-dev, engine or investment talks (f_5e355d03f6eb6a4e866ead).
2. Each publisher's status, first that fits, from its thread, its terms and anything said about it elsewhere (f_5e355d03f6eb6a4e866ead).
3. The latest terms for each offer, wherever they are (f_5e355d03f6eb6a4e866ead).
4. Whether an offer's terms take something the founders keep (C07C2866011/1756140953.197759).
5. Each Live offer's 12-month value and Q4 cash, given the signing date (frederick.stone@harmonygames.co/<CA9raR_pqldShsvOhd5Uwxoj8zJh2-tzH0UJ5JLd@mail.gmail.com>).
6. What publisher money is actually in the SVB account (f_5e355d03f6eb6a4e866ead).
7. The game's keep value from the named warehouse table (f_5e355d03f6eb6a4e866ead).
8. Which offer goes first (f_5e355d03f6eb6a4e866ead).
9. Who is already in Contacts, who has a card already, and what was each publisher sent (f_fd467bd2ae0c6d4f3bd2bc).
10. Which notes Leonard asked for on what goes out to publishers, and who gets one (f_5e355d03f6eb6a4e866ead).

Writes those answers feed (each depends on a publisher's status or terms):
- the model sheet in d_6fc54be60d1377e340a5b5;
- checklists and items on 68dab660c900179df4f5f92d;
- follow-up cards on list 670015c2ecd45b634d5eec81, and comments on 68d5913004a98be3b4c45408 and 68d598387dea3e7fe85e3a0a;
- Gmail drafts: nudges and notes;
- Contacts entries;
- calendar reminders;
- one reply on the hub thread frederick.stone@harmonygames.co/1844732284109533347;

## 4 · Pinned final state (UGT anchor)

| Deliverable | Required contents | Destination | Recipients | Catalog write | Fed by |
|---|---|---|---|---|---|
| D1 model sheet | a native Google Sheet called DD publishing model; tab Publishers with Publisher, Status, Advance, Monthly installs, 12-month value, Q4 cash, one row per publisher (26), figures only on Live rows; tab Summary with Keep value, First pick, Banked so far | folder d_6fc54be60d1377e340a5b5 (A3) | — | gsheets_create_spreadsheet, gsheets_values_update, gdrive_move_file | f_5e355d03f6eb6a4e866ead 'Layout' |
| D2 checklists | one checklist per status (6), one item per publisher (26) | card 68dab660c900179df4f5f92d (A2) | — | trello_create_checklist, trello_create_check_item | 68dab660c900179df4f5f92d desc |
| D3 follow-ups | a card named F/up with plus the publisher's name for each Live, Waiting on us and No reply publisher without one (15); a comment with the status on an existing card (2: 68d5913004a98be3b4c45408, 68d598387dea3e7fe85e3a0a) | list 670015c2ecd45b634d5eec81 on board 66da196af476ab78deaa0cef | — | trello_create_card, trello_add_comment | 68dab660c900179df4f5f92d desc |
| D4 nudges | a one-line draft to each No reply publisher (7), not sent | Frederick's Gmail drafts (frederick.stone@harmonygames.co) | partnerships@orchardlanegames.com, partnerships@summitmobile.io, partnerships@silverlakemobile.com, partnerships@cedarbrookplay.com, partnerships@foxglovegames.com, partnerships@riverstoneinteractive.com, partnerships@bellwetherarcade.com | gmail_create_draft | 68dab660c900179df4f5f92d desc |
| D5 organic notes | a short draft with the organic figure, $0.50 D30 ARPI, to each publisher that got the May one-pager and still has an offer in (3), not sent | Frederick's Gmail drafts (frederick.stone@harmonygames.co) | diego@harborlanegames.com, paola@tallwatergames.com, sofia@wavecrestplay.com | gmail_create_draft | C096HFA5Z8W/1758915000.867092 |
| D6 contacts | a contact for everyone at a publisher who gave terms or said no, with the company in the job title, skipping anyone already there (14) | Contacts (skip 5373edb55ca853d6052ecce5, 1d6fd505d2fea08fa0f26c6e) | — | contacts_add_new_contact | frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> |
| D7 reminders | one event per Live offer on its response date, named for the publisher (7) | Frederick's calendar (frederick.stone@harmonygames.co) | — | gcal_create_event | f_5e355d03f6eb6a4e866ead 'Reminders' |
| D8 reply | which offer goes first, its 12-month value, its Q4 cash, publisher money banked so far | reply on the hub thread frederick.stone@harmonygames.co/1844732284109533347 | leonard.hayes@harmonygames.co | gmail_reply_to_message | frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> |

Alternatives a careful run could defend, and how each is settled:
- D1 destination: created in the folder or created elsewhere and moved there; both end in d_6fc54be60d1377e340a5b5.
- D1 rows: the 26 keys; Homa, NCsoft, Tilting Point, Tamatem and the Sep 24 lead stay out (f_5e355d03f6eb6a4e866ead, frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com>).
- D1 Advance for Oakline: the total, $30,000 (f_27cac0eed300cc33eeb4fd; the rule doc says 'the total advance').
- D1 Q4 cash for Oakline: $30,000, the resent $10,000 and the $20,000 on Dec 14 (C07C2866011/1759251900.005166: it'll land in October).
- D3 card names: the publisher's name after 'F/up with' (the card's wording, 68dab660c900179df4f5f92d); existing cards named for people keep their names and get a comment.
- D4 Summit: to partnerships@summitmobile.io, the address Frederick wrote to, not the noreply@ sender (frederick.stone@harmonygames.co/1842077918822746195).
- D4, D5 thread: a draft reply on the publisher's thread or a new draft to the same person are both the draft asked for; neither 68dab660c900179df4f5f92d nor C096HFA5Z8W/1758915000.867092 says which.
- D5 Moonrail: no note, its offer is off (e44da6a468e7795a1b5853cfb0763aaf); Oakline, Sunfold, Copperleaf and Redwood: no note, they didn't get the one-pager (f_fd467bd2ae0c6d4f3bd2bc).
- D6 job field: the company must be in it; any role words are representational (frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com>). Copperleaf's and Redwood's people come from 495d71a7e14dfaa68cac26fc4a6c4e03 and lc_674982ffdca63f854ec6f591.
- D7 time of day, duration and all-day form are representational; the date and one event per offer are not (f_5e355d03f6eb6a4e866ead).
- D8 reply or reply-all on frederick.stone@harmonygames.co/1844732284109533347: both reach Leonard; extra lines are allowed. The Q4 figure is the first pick's, never a total across offers ('what it brings in during Q4', frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com>).
- Who sends: every write is the agent's on Frederick's behalf; drafts stay drafts (f55bd27436eb285a15d833648b922e9b, 68dab660c900179df4f5f92d).

### 4b · Canonical outcome (all fair outcomes)

| Deliverable | Field | Fixed value (or closed accepted set, with sources) | Delegated by | Allowed equivalence class | Material / representational |
|---|---|---|---|---|---|
| D1 | Name and home | a native Sheet named DD publishing model whose final parent is d_6fc54be60d1377e340a5b5 | — | created there or moved there | material |
| D1 | Tabs | Publishers and Summary, with the columns in f_5e355d03f6eb6a4e866ead | — | case | material |
| D1 | Rows | Oakline Games, Tallwater Games, Sunfold Mobile, Harbor Lane Games, Wavecrest Play, Copperleaf Games, Redwood Arcade, Moonrail Studios, Northglow Publishing, Pinegrove Games, Fernhollow Media, Quietbay Games, Slatewood Mobile, Ironbridge Interactive, Tidewell Studios, Marlin Play, Appodeal, Rayking Game, Kitebridge Games, Orchard Lane Games, Summit Mobile, Silverlake Mobile, Cedarbrook Play, Foxglove Games, Riverstone Interactive, Bellwether Arcade (f_5e355d03f6eb6a4e866ead, f_fd467bd2ae0c6d4f3bd2bc) | — | record spelling or an obvious short form | material |
| D1 | Copperleaf Games | Live; Advance 32,000; Monthly installs 40,000; 12-month value 67,200; Q4 cash 32,000 (solver/truth.json; 495d71a7e14dfaa68cac26fc4a6c4e03) | — | currency symbols, commas | material |
| D1 | Redwood Arcade | Live; Advance 25,000; Monthly installs 40,000; 12-month value 57,600; Q4 cash 25,000 (solver/truth.json; ENG-2362) | — | currency symbols, commas | material |
| D1 | Sunfold Mobile | Live; Advance 20,000; Monthly installs 30,000; 12-month value 54,000; Q4 cash 20,000 (solver/truth.json; f_8ddfb9901891eb8e9dcab8) | — | currency symbols, commas | material |
| D1 | Tallwater Games | Live; Advance 40,000; Monthly installs 30,000; 12-month value 45,000; Q4 cash 40,000 (solver/truth.json; f_e8cb875d5b7c8d9972d259) | — | currency symbols, commas | material |
| D1 | Oakline Games | Live; Advance 30,000; Monthly installs 20,000; 12-month value 36,000; Q4 cash 30,000 (solver/truth.json; f_27cac0eed300cc33eeb4fd) | — | currency symbols, commas | material |
| D1 | Harbor Lane Games | Live; Advance 25,000; Monthly installs 25,000; 12-month value 30,000; Q4 cash 0 (solver/truth.json; f_d72e8b34e7496f0de668bc) | — | currency symbols, commas | material |
| D1 | Wavecrest Play | Live; Advance 15,000; Monthly installs 15,000; 12-month value 19,800; Q4 cash 0 (solver/truth.json; f_a6a5647f977d4638b2b8b1) | — | currency symbols, commas | material |
| D1 | Withdrawn | Moonrail Studios; figures blank (f_5e355d03f6eb6a4e866ead) | — | a dash or blank in figure cells | material |
| D1 | Out on rights | Northglow Publishing, Pinegrove Games; figures blank (f_5e355d03f6eb6a4e866ead) | — | a dash or blank in figure cells | material |
| D1 | Passed | Fernhollow Media, Quietbay Games, Slatewood Mobile, Ironbridge Interactive, Tidewell Studios, Marlin Play; figures blank (f_5e355d03f6eb6a4e866ead) | — | a dash or blank in figure cells | material |
| D1 | Waiting on us | Appodeal, Rayking Game, Kitebridge Games; figures blank (f_5e355d03f6eb6a4e866ead) | — | a dash or blank in figure cells | material |
| D1 | No reply | Orchard Lane Games, Summit Mobile, Silverlake Mobile, Cedarbrook Play, Foxglove Games, Riverstone Interactive, Bellwether Arcade; figures blank (f_5e355d03f6eb6a4e866ead) | — | a dash or blank in figure cells | material |
| D1 | Summary | Keep value 12,723.96; First pick Copperleaf Games; Banked so far 0 (f_5e355d03f6eb6a4e866ead, 0230b2df24ec829928fe1c55ad6185bf) | — | keep value to the dollar ($12,724); 'none' or 'nothing' for banked | material |
| D2 | Checklists | Live, Withdrawn, Out on rights, Passed, Waiting on us, No reply on 68dab660c900179df4f5f92d, each holding the publishers of that status | — | item wording carrying the publisher's name | material |
| D3 | New cards | F/up with: Appodeal, Bellwether Arcade, Cedarbrook Play, Copperleaf Games, Foxglove Games, Harbor Lane Games, Kitebridge Games, Orchard Lane Games, Rayking Game, Redwood Arcade, Riverstone Interactive, Silverlake Mobile, Summit Mobile, Tallwater Games, Wavecrest Play, on list 670015c2ecd45b634d5eec81 | — | short forms of the publisher's name | material |
| D3 | Comments | Live on 68d5913004a98be3b4c45408 and 68d598387dea3e7fe85e3a0a | — | extra words beside the status | material |
| D4 | Nudges | Orchard Lane Games, Summit Mobile, Silverlake Mobile, Cedarbrook Play, Foxglove Games, Riverstone Interactive, Bellwether Arcade: one each, unsent (68dab660c900179df4f5f92d) | 'Leave a one-line nudge' (68dab660c900179df4f5f92d) | wording is the run's; new draft or draft reply | wording representational |
| D5 | Notes | Harbor Lane Games, Tallwater Games, Wavecrest Play: one each, unsent, carrying $0.50 D30 ARPI (C096HFA5Z8W/1758915000.867092) | 'one short note each' (C096HFA5Z8W/1758915000.867092) | wording is the run's; new draft or draft reply | figure material, wording representational |
| D6 | Contacts | Copperleaf Games, Fernhollow Media, Harbor Lane Games, Ironbridge Interactive, Marlin Play, Northglow Publishing, Oakline Games, Pinegrove Games, Quietbay Games, Redwood Arcade, Slatewood Mobile, Tallwater Games, Tidewell Studios, Wavecrest Play: person, address, company in job (frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com>) | — | role words | material |
| D7 | Reminders | Copperleaf Games 2025-10-17; Redwood Arcade 2025-10-31; Sunfold Mobile 2025-10-31; Tallwater Games 2025-10-17; Oakline Games 2025-10-24; Harbor Lane Games 2025-10-24; Wavecrest Play 2025-10-31 on frederick.stone@harmonygames.co's calendar | — | time of day, all-day form | date material |
| D8 | Reply | Copperleaf Games; $67,200; $32,000; $0 banked, on frederick.stone@harmonygames.co/1844732284109533347 | — | reply or reply-all; 'nothing banked yet'; added explanation | material |

## 5 · Discovery map

Root causes and corrections appear only here and are never in the prompt.

| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |
|---|---|---|---|---|---|---|
| F1 hub ask | the model, the card, Contacts, the reply; leave the Sep 24 lead out | frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> | YES | first link (A1) | — | Yes (A1, the job's source) |
| F2 ground rules doc | who's in, status order, value, Q4 cash, keep value, first pick, reminders, layout | f_5e355d03f6eb6a4e866ead | YES | named by the hub; met second | first-framing latch on F3 | No |
| F3 co-dev doc (decoy) | co-dev terms, not DD | f_21203dbcdf780cc07c76cb | YES | competing hit on a 'what we'd take' or 'terms' search | decoy | No |
| F4 DD publishing card | checklists, follow-up cards, nudges | 68dab660c900179df4f5f92d | YES | named by the hub | — | Yes (A2, on the hub) |
| F5 DD publishing folder | term sheets and the outreach sheet; the model's home | d_6fc54be60d1377e340a5b5 | YES | named by the hub | — | Yes (A3, the destination) |
| F6 outreach sheet | 24 publishers, what each got | f_fd467bd2ae0c6d4f3bd2bc | YES | named by the rule doc | stops here for the population | No |
| F7 May one-pager | paid-traffic numbers only | f_4b3ef3dcf76258a6fda5cd | YES | named by the standing line | — | No |
| F8 organic figure | $0.50 D30 ARPI | D05S58U4SAK/1758736747.409459 | YES | named by the rule doc; overturns the paid numbers in F27 | — | No |
| F9 rights position | retain code, IP and non-mobile distribution rights | C07C2866011/1756140953.197759 | YES | named by the rule doc as the August sync position | value-first reading of Northglow | No |
| F10 August sync doc | same sentence on the agenda | f_26e1f9a86761e35049192a | YES | named by the rule doc | — | No |
| F11 Copperleaf's offer | 28 %, $32,000 net 30, 40,000 installs, respond by Oct 17 | C07C2866011/1758909900.662794 | YES | off the sheet and off the inbox; a reply under the Sep 24 root | rarely opens a thread under an unrelated post | No |
| F12 #analytics pointer | a tech lead at a publisher, notes on ENG-2362 | C069FF9Q57S/1758912000.686342 | YES | leads to F13 | no publisher name in the line | No |
| F13 Redwood's offer on ENG-2362 | 24 %, $25,000 net 45, 40,000 installs, respond by Oct 31 | ENG-2362 comment lc_674982ffdca63f854ec6f591 | YES | behind F12 | prefers mail and Drive over Linear comments | No |
| F14 Kestrel post | frozen every outside signing; anything on the table is off | C07C2866011/1759176900.065118 | YES | overturns Moonrail's term sheet | says Kestrel only | No |
| F15 Anika's contact | Partnerships, Kestrel Group | 5373edb55ca853d6052ecce5 | YES | joins Kestrel to Moonrail | — | No |
| F16 Arthur's SVB reply | the first-look never hit the account; resent next week, lands in October | C07C2866011/1759251900.005166 | YES | overturns F25 and F26 | stops at 'went out today' | No |
| F17 banker root | Sep 8 post the reply sits under | C07C2866011/1757345405.134829 | YES | container of F16 | — | No |
| F18 70 % D1 root | Sep 24 post the relay sits under | C07C2866011/1758736960.824899 | YES | container of F11 | — | No |
| F19 Matthew root | Sep 17 post the standing line sits under | C096HFA5Z8W/1758147530.732569 | YES | container of F20 | — | No |
| F20 standing line | anyone who got the one-pager and still has an offer in hears $0.50 D30 ARPI; notes in Gmail drafts | C096HFA5Z8W/1758915000.867092 | YES | carried by the rule doc's last line | reply under an unrelated root | No |
| F21 Tallwater note | the advance is $40,000 now | evt_43fda04cd11b9d58a05161 | YES | overturns Tallwater's term sheet | description past the first lines | No |
| F22 F/up with Lena card | comment: 30,000 installs, not 50,000 | 68d598387dea3e7fe85e3a0a | YES | overturns Sunfold's term sheet; comment 68dbfe80ef9c41b4f4fa8fe9 | card named for a person | No |
| F23 F/up with Marek card | comment: the $10K went out | 68d5913004a98be3b4c45408 | YES | claim met first (T1); comment 68dabd6800e271eb0608d2d6 | card named for a person | No |
| F24 ESG thread | earliest signature Nov 14; Leonard confirms | frederick.stone@harmonygames.co/1844620296192667598 | YES | overturns the rule doc's Oct 31, as the doc allows | names no publisher | No |
| F25 Oakline's paid mail | $10,000 sent by wire Sep 29, ref OAK-2291 | frederick.stone@harmonygames.co/<CAybuYiHDdC_1wq0wp32aITdzH-XuQAf6p028lBn@mail.gmail.com> | YES | claim met first (T1) | stops here | No |
| F26 Appodeal thread | no terms; last message theirs | frederick.stone@harmonygames.co/1830012626042968381 | YES | base cohort member | — | No |
| F27 board note | paid-traffic numbers, Apr 30 | frederick.stone@harmonygames.co/1830890312657338682 | YES | claim met first (T13) | — | No |
| F28 Rayking thread | Frederick's Sep 4 message is an unsent draft | frederick.stone@harmonygames.co/1842348778705877030 | YES | base cohort member | reads the draft as a reply | No |
| F29 Rayking DM | we still owe them an answer | D05S58U4SAK/1757090400.829462 | YES | settles F28 | — | No |
| F30 Homa talk | co-dev path, out of scope | C096HFA5Z8W/1758210489.170809 | YES | named out by the rule doc | — | No |
| F31 NCsoft talk | engine talks, out of scope | C07C2866011/1757516293.887729 | YES | named out by the rule doc | — | No |
| F32 Tilting Point ack | UA funding form, out of scope | frederick.stone@harmonygames.co/1842443183462721250 | YES | named out by the rule doc | — | No |
| F33 Publishing Partners doc | candidate list, not the population | f_10dfa1b4236a7c35dcb632 | YES | decoy for the population | — | No |
| F34 Biz Dev Notes | April candidate list with a template | f_0d17fc08eddaf231cf7f28 | YES | decoy for the population | — | No |
| F35 Monday event | Oct 6 17:00Z, the four execs | evt_881d3e07c598b2205a7ff3 | YES | context | — | No |
| F36 Lena's contact | already in Contacts | 1d6fd505d2fea08fa0f26c6e | YES | skip | — | No |
| F37 revenue table | ANALYTICS.MONETIZATION.REVENUE_DAILY total_revenue_usd: Jul 2,078.33, Aug 721.55, Sep 381.11 | snowflake.wh_analytics__monetization__revenue_daily | YES | named by the rule doc | the agent's system prompt doesn't advertise Snowflake; the doc names it | No |
| F38 the Sep 24 lead | left out by the hub | D05S58U4SAK/1758736842.534589 | YES | named out by the hub | — | No |
| F39 Tamatem mention | a name passed along, not in scope | C48D58CD7FBD/1748974617.722599 | YES | named out by the rule doc's passed-along sentence | — | No |
| F40 Apple Arcade post | a dominoes lead nobody took | C07C2866011/1756261199.570279 | YES | not on the sheet, nobody came to us | — | No |
| C:Oakline Games Oakline Games thread | Live | frederick.stone@harmonygames.co/1842077918822838564 | YES | cohort member | per-record read | No |
| C:Tallwater Games Tallwater Games thread | Live | frederick.stone@harmonygames.co/1842077918823428620 | YES | cohort member | per-record read | No |
| C:Sunfold Mobile Sunfold Mobile thread | Live | frederick.stone@harmonygames.co/1842077918823258769 | YES | cohort member | per-record read | No |
| C:Harbor Lane Games Harbor Lane Games thread | Live | frederick.stone@harmonygames.co/1842077918823445589 | YES | cohort member | per-record read | No |
| C:Wavecrest Play Wavecrest Play thread | Live | frederick.stone@harmonygames.co/1842077918823344908 | YES | cohort member | per-record read | No |
| C:Moonrail Studios Moonrail Studios thread | Withdrawn | frederick.stone@harmonygames.co/1842077918822811962 | YES | cohort member | per-record read | No |
| C:Northglow Publishing Northglow Publishing thread | Out on rights | frederick.stone@harmonygames.co/1842077918822429064 | YES | cohort member | per-record read | No |
| C:Pinegrove Games Pinegrove Games thread | Out on rights | frederick.stone@harmonygames.co/1842077918823323729 | YES | cohort member | per-record read | No |
| C:Fernhollow Media Fernhollow Media thread | Passed | frederick.stone@harmonygames.co/1842077918822912178 | YES | cohort member | per-record read | No |
| C:Quietbay Games Quietbay Games thread | Passed | frederick.stone@harmonygames.co/1842077918822894896 | YES | cohort member | per-record read | No |
| C:Slatewood Mobile Slatewood Mobile thread | Passed | frederick.stone@harmonygames.co/1842077918823167383 | YES | cohort member | per-record read | No |
| C:Ironbridge Interactive Ironbridge Interactive thread | Passed | frederick.stone@harmonygames.co/1842077918822812534 | YES | cohort member | per-record read | No |
| C:Tidewell Studios Tidewell Studios thread | Passed | frederick.stone@harmonygames.co/1842077918822727407 | YES | cohort member | per-record read | No |
| C:Marlin Play Marlin Play thread | Passed | frederick.stone@harmonygames.co/1842077918823060205 | YES | cohort member | per-record read | No |
| C:Kitebridge Games Kitebridge Games thread | Waiting on us | frederick.stone@harmonygames.co/1842077918823167536 | YES | cohort member | per-record read | No |
| C:Orchard Lane Games Orchard Lane Games thread | No reply | frederick.stone@harmonygames.co/1842077918822627795 | YES | cohort member | per-record read | No |
| C:Summit Mobile Summit Mobile thread | No reply | frederick.stone@harmonygames.co/1842077918822746195 | YES | cohort member | per-record read | No |
| C:Silverlake Mobile Silverlake Mobile thread | No reply | frederick.stone@harmonygames.co/1842077918822773098 | YES | cohort member | per-record read | No |
| C:Cedarbrook Play Cedarbrook Play thread | No reply | frederick.stone@harmonygames.co/1842077918822506013 | YES | cohort member | per-record read | No |
| C:Foxglove Games Foxglove Games thread | No reply | frederick.stone@harmonygames.co/1842077918822804025 | YES | cohort member | per-record read | No |
| C:Riverstone Interactive Riverstone Interactive thread | No reply | frederick.stone@harmonygames.co/1842077918823170401 | YES | cohort member | per-record read | No |
| C:Bellwether Arcade Bellwether Arcade thread | No reply | frederick.stone@harmonygames.co/1842077918822759281 | YES | cohort member | per-record read | No |
| T:Oakline Games Oakline Games term sheet | 30% of net to Harmony Games, $30,000 advance ($10,000 first- | f_27cac0eed300cc33eeb4fd | YES | named by the folder | stale value on three sheets | No |
| T:Tallwater Games Tallwater Games term sheet | 25% of net to Harmony Games, $60,000 advance net 30 from sig | f_e8cb875d5b7c8d9972d259 | YES | named by the folder | stale value on three sheets | No |
| T:Sunfold Mobile Sunfold Mobile term sheet | 30% of net to Harmony Games, $20,000 advance net 45 from sig | f_8ddfb9901891eb8e9dcab8 | YES | named by the folder | stale value on three sheets | No |
| T:Harbor Lane Games Harbor Lane Games term sheet | 20% of net to Harmony Games, $25,000 advance net 60 from sig | f_d72e8b34e7496f0de668bc | YES | named by the folder | per-record read | No |
| T:Wavecrest Play Wavecrest Play term sheet | 22% of net to Harmony Games, $15,000 advance net 60 from sig | f_a6a5647f977d4638b2b8b1 | YES | named by the folder | per-record read | No |
| T:Moonrail Studios Moonrail Studios term sheet | 26% of net to Harmony Games, $30,000 advance net 30 from sig | f_464839da025a0a01f53979 | YES | named by the folder | per-record read | No |
| T:Northglow Publishing Northglow Publishing term sheet | 35% of net to Harmony Games, $50,000 advance net 30 from sig | f_3eccf6e0bb63955dc51e27 | YES | named by the folder | per-record read | No |
| T:Pinegrove Games Pinegrove Games term sheet | 30% of net to Harmony Games, $40,000 advance net 30 from sig | f_5f3ef4a4760d18e696a41a | YES | named by the folder | per-record read | No |

## 5a · Search-as-persona proof

`persona_view.py search` reads the base only; seeded hits are counted from the SQL rows Frederick can see (the same rows check-sql proves visible). One row per §5 fact.

| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |
|---|---|---|---|---|---|---|
| F1 hub ask | gmail | "DD publishing" | base 0; seeded 2 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1844732284109533347 | YES (seeded; check-sql YES) |
| F2 ground rules doc | gdocs | "ground rules" | base 0; seeded 1 | 1 | f_5e355d03f6eb6a4e866ead | YES (seeded; check-sql YES) |
| F3 co-dev doc (decoy) | gdocs | "Co-dev" | base 2; seeded 2 | 2 | f_21203dbcdf780cc07c76cb | YES (seeded; check-sql YES) |
| F4 DD publishing card | trello | "DD publishing" | base 0; seeded 1 | 0 | 68dab660c900179df4f5f92d | YES (seeded; unscoped) |
| F5 DD publishing folder | gdrive | "DD publishing" | base 0; seeded 2 | 0 | d_6fc54be60d1377e340a5b5 | YES (seeded; check-sql YES) |
| F6 outreach sheet | gsheets | "outreach" | base 0; seeded 1 | 6 | f_fd467bd2ae0c6d4f3bd2bc | YES (seeded; check-sql YES) |
| F7 May one-pager | gslides | "one-pager" | base 0; seeded 1 | 0 | f_4b3ef3dcf76258a6fda5cd | YES (seeded; check-sql YES) |
| F8 organic figure | slack | "D30 ARPI" | base 1; seeded 1 | n/a (--no-hidden) | D05S58U4SAK/1758736747.409459 | YES (base, hit 1 of 1) |
| F9 rights position | slack | "non-mobile" | base 3; seeded 0 | n/a (--no-hidden) | C07C2866011/1756140953.197759 | YES (base, hit 2 of 3) |
| F10 August sync doc | gdocs | "Executives Biweekly Sync" | base 1; seeded 0 | 0 | f_26e1f9a86761e35049192a | YES (base, hit 1 of 1) |
| F11 Copperleaf's offer | slack | "advance" | base 184; seeded 1 | n/a (--no-hidden) | C07C2866011/1758909900.662794 | YES (seeded; check-sql YES) |
| F12 #analytics pointer | slack | "deep links" | base 1; seeded 1 | n/a (--no-hidden) | C069FF9Q57S/1758912000.686342 | YES (seeded; check-sql YES) |
| F13 Redwood's offer on ENG-2362 | linear | "ENG-2362" | base 3; seeded 0 | 0 | ENG-2362 | YES (base, in the visible hits) |
| F14 Kestrel post | slack | "Kestrel" | base 0; seeded 1 | n/a (--no-hidden) | C07C2866011/1759176900.065118 | YES (seeded; check-sql YES) |
| F15 Anika's contact | contacts | "Anika" | base 0; seeded 1 | 0 | 5373edb55ca853d6052ecce5 | YES (seeded; unscoped) |
| F16 Arthur's SVB reply | slack | "first-look" | base 0; seeded 1 | n/a (--no-hidden) | C07C2866011/1759251900.005166 | YES (seeded; check-sql YES) |
| F17 banker root | slack | "banker" | base 9; seeded 0 | n/a (--no-hidden) | C07C2866011/1757345405.134829 | YES (base, hit 4 of 9) |
| F18 70 % D1 root | slack | "70% D1" | base 6; seeded 0 | n/a (--no-hidden) | C07C2866011/1758736960.824899 | YES (base, hit 2 of 6) |
| F19 Matthew root | slack | "talked to Matthew" | base 8; seeded 0 | n/a (--no-hidden) | C096HFA5Z8W/1758147530.732569 | YES (base, hit 8 of 8) |
| F20 standing line | slack | "one-pager" | base 1; seeded 1 | n/a (--no-hidden) | C096HFA5Z8W/1758915000.867092 | YES (seeded; check-sql YES) |
| F21 Tallwater note | gcal | "Tallwater" | base 0; seeded 1 | 0 | evt_43fda04cd11b9d58a05161 | YES (seeded; check-sql YES) |
| F22 F/up with Lena card | trello | "F/up with Lena" | base 0; seeded 1 | 0 | 68d598387dea3e7fe85e3a0a | YES (seeded; unscoped) |
| F23 F/up with Marek card | trello | "F/up with Marek" | base 0; seeded 1 | 0 | 68d5913004a98be3b4c45408 | YES (seeded; unscoped) |
| F24 ESG thread | gmail | "License paper timing" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1844620296192667598 | YES (seeded; check-sql YES) |
| F25 Oakline's paid mail | gmail | "first-look" | base 1; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918822838564 | YES (seeded; check-sql YES) |
| F26 Appodeal thread | gmail | "Appodeal publishing Program" | base 2; seeded 0 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1830012626042968381 | YES (base, hit 2 of 2) |
| F27 board note | gmail | "Board Follow-Up" | base 1; seeded 0 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1830890312657338682 | YES (base, hit 1 of 1) |
| F28 Rayking thread | gmail | "Rayking" | base 1; seeded 0 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842348778705877030 | YES (base, hit 1 of 1) |
| F29 Rayking DM | slack | "Rayking" | base 0; seeded 1 | n/a (--no-hidden) | D05S58U4SAK/1757090400.829462 | YES (seeded; check-sql YES) |
| F30 Homa talk | slack | "focus Homa" | base 1; seeded 0 | n/a (--no-hidden) | C096HFA5Z8W/1758210489.170809 | YES (base, hit 1 of 1) |
| F31 NCsoft talk | slack | "NCsoft" | base 20; seeded 0 | n/a (--no-hidden) | C07C2866011/1757516293.887729 | YES (base, hit 2 of 10) |
| F32 Tilting Point ack | gmail | "Tilting Point" | base 3; seeded 0 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842443183462721250 | YES (base, hit 3 of 3) |
| F33 Publishing Partners doc | gdocs | "Publishing Partners" | base 1; seeded 0 | 1 | f_10dfa1b4236a7c35dcb632 | YES (base, hit 1 of 1) |
| F34 Biz Dev Notes | gdocs | "Biz Dev Notes" | base 1; seeded 0 | 0 | f_0d17fc08eddaf231cf7f28 | YES (base, hit 1 of 1) |
| F35 Monday event | gcal | "DD publishing" | base 0; seeded 1 | 0 | evt_881d3e07c598b2205a7ff3 | YES (seeded; check-sql YES) |
| F36 Lena's contact | contacts | "Lena" | base 0; seeded 1 | 0 | 1d6fd505d2fea08fa0f26c6e | YES (seeded; unscoped) |
| F37 revenue table | snowflake | "REVENUE_DAILY" | base 10; seeded 0 | 0 | REVENUE_DAILY | YES (base, in the visible hits) |
| F38 the Sep 24 lead | slack | "looking for games" | base 1; seeded 0 | n/a (--no-hidden) | D05S58U4SAK/1758736842.534589 | YES (base, hit 1 of 1) |
| F39 Tamatem mention | slack | "Tamatem" | base 2; seeded 0 | n/a (--no-hidden) | C48D58CD7FBD/1748974617.722599 | YES (base, hit 2 of 2) |
| F40 Apple Arcade post | slack | "signed someone for dominoes" | base 1; seeded 0 | n/a (--no-hidden) | C07C2866011/1756261199.570279 | YES (base, hit 1 of 1) |
| C:Oakline Games Oakline Games thread | gmail | "Oakline" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918822838564 | YES (seeded; check-sql YES) |
| C:Tallwater Games Tallwater Games thread | gmail | "Tallwater" | base 0; seeded 2 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918823428620 | YES (seeded; check-sql YES) |
| C:Sunfold Mobile Sunfold Mobile thread | gmail | "Sunfold" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918823258769 | YES (seeded; check-sql YES) |
| C:Harbor Lane Games Harbor Lane Games thread | gmail | "Harbor" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918823445589 | YES (seeded; check-sql YES) |
| C:Wavecrest Play Wavecrest Play thread | gmail | "Wavecrest" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918823344908 | YES (seeded; check-sql YES) |
| C:Moonrail Studios Moonrail Studios thread | gmail | "Moonrail" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918822811962 | YES (seeded; check-sql YES) |
| C:Northglow Publishing Northglow Publishing thread | gmail | "Northglow" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918822429064 | YES (seeded; check-sql YES) |
| C:Pinegrove Games Pinegrove Games thread | gmail | "Pinegrove" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918823323729 | YES (seeded; check-sql YES) |
| C:Fernhollow Media Fernhollow Media thread | gmail | "Fernhollow" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918822912178 | YES (seeded; check-sql YES) |
| C:Quietbay Games Quietbay Games thread | gmail | "Quietbay" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918822894896 | YES (seeded; check-sql YES) |
| C:Slatewood Mobile Slatewood Mobile thread | gmail | "Slatewood" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918823167383 | YES (seeded; check-sql YES) |
| C:Ironbridge Interactive Ironbridge Interactive thread | gmail | "Ironbridge" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918822812534 | YES (seeded; check-sql YES) |
| C:Tidewell Studios Tidewell Studios thread | gmail | "Tidewell" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918822727407 | YES (seeded; check-sql YES) |
| C:Marlin Play Marlin Play thread | gmail | "Marlin" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918823060205 | YES (seeded; check-sql YES) |
| C:Kitebridge Games Kitebridge Games thread | gmail | "Kitebridge" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918823167536 | YES (seeded; check-sql YES) |
| C:Orchard Lane Games Orchard Lane Games thread | gmail | "Orchard" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918822627795 | YES (seeded; check-sql YES) |
| C:Summit Mobile Summit Mobile thread | gmail | "Summit" | base 3; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918822746195 | YES (seeded; check-sql YES) |
| C:Silverlake Mobile Silverlake Mobile thread | gmail | "Silverlake" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918822773098 | YES (seeded; check-sql YES) |
| C:Cedarbrook Play Cedarbrook Play thread | gmail | "Cedarbrook" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918822506013 | YES (seeded; check-sql YES) |
| C:Foxglove Games Foxglove Games thread | gmail | "Foxglove" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918822804025 | YES (seeded; check-sql YES) |
| C:Riverstone Interactive Riverstone Interactive thread | gmail | "Riverstone" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918823170401 | YES (seeded; check-sql YES) |
| C:Bellwether Arcade Bellwether Arcade thread | gmail | "Bellwether" | base 0; seeded 1 | n/a (--no-hidden) | frederick.stone@harmonygames.co/1842077918822759281 | YES (seeded; check-sql YES) |
| T:Oakline Games Oakline Games term sheet | gdocs | "Oakline Games - term sheet" | base 0; seeded 1 | 0 | f_27cac0eed300cc33eeb4fd | YES (seeded; check-sql YES) |
| T:Tallwater Games Tallwater Games term sheet | gdocs | "Tallwater Games - term sheet" | base 0; seeded 1 | 0 | f_e8cb875d5b7c8d9972d259 | YES (seeded; check-sql YES) |
| T:Sunfold Mobile Sunfold Mobile term sheet | gdocs | "Sunfold Mobile - term sheet" | base 0; seeded 1 | 0 | f_8ddfb9901891eb8e9dcab8 | YES (seeded; check-sql YES) |
| T:Harbor Lane Games Harbor Lane Games term sheet | gdocs | "Harbor Lane Games - term sheet" | base 0; seeded 1 | 0 | f_d72e8b34e7496f0de668bc | YES (seeded; check-sql YES) |
| T:Wavecrest Play Wavecrest Play term sheet | gdocs | "Wavecrest Play - term sheet" | base 0; seeded 1 | 0 | f_a6a5647f977d4638b2b8b1 | YES (seeded; check-sql YES) |
| T:Moonrail Studios Moonrail Studios term sheet | gdocs | "Moonrail Studios - term sheet" | base 0; seeded 1 | 0 | f_464839da025a0a01f53979 | YES (seeded; check-sql YES) |
| T:Northglow Publishing Northglow Publishing term sheet | gdocs | "Northglow Publishing - term sheet" | base 0; seeded 1 | 0 | f_3eccf6e0bb63955dc51e27 | YES (seeded; check-sql YES) |
| T:Pinegrove Games Pinegrove Games term sheet | gdocs | "Pinegrove Games - term sheet" | base 0; seeded 1 | 0 | f_5f3ef4a4760d18e696a41a | YES (seeded; check-sql YES) |

Search outputs, verbatim:

```
SEARCH gmail 'DD publishing' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gdocs 'ground rules' as frederick_stone  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=1 in 1 containers  UNVERIFIED=0 in 0 containers

SEARCH gdocs 'Co-dev' as frederick_stone  scope: GDocs title + body_text
visible hits=2 (showing 2)  hidden by ACL=2 in 2 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_a17bda426285acec3020e2", "name": "[PERSON_NAME_0038] Offer Letter.docx", "mime": "application/vnd.google-apps.document", "why": "file is shared with the persona (shared_with_emails)", "snippet": "ligible to receive a Contingent Profit Share Bonus for each co-development project you introdu
  {"id": "f_f83ccbdaaef1cd6e66309a", "name": "Executive Offsite - Sep 24.docx", "mime": "application/vnd.google-apps.document", "why": "file is shared with the persona (shared_with_emails)", "snippet": "side for backup plans (see below). Ryan: Continue exploring co-development opportunities and potent

SEARCH trello 'DD publishing' as frederick_stone  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gdrive 'DD publishing' as frederick_stone  scope: Drive file/folder names (on-disk file content is not searched)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gsheets 'outreach' as frederick_stone  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=0 (showing 0)  hidden by ACL=6 in 6 containers  UNVERIFIED=1 in 1 containers

SEARCH gslides 'one-pager' as frederick_stone  scope: GSlides title + page element text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH slack 'D30 ARPI' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "D05S58U4SAK/1758736747.409459", "channel": "D05S58U4SAK", "kind": "im", "date": "2025-09-24", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "[PERSON_NAME_16377] pure organics, $0.50 D30 ARPI"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'non-mobile' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=3 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=1 in 1 containers
  {"id": "C05M9QYMZUN/1723061674.491209", "channel": "industry-news", "kind": "public", "date": "2024-08-07", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "I think if it's non-mobile, it's pretty cool"}
  {"id": "C07C2866011/1756140953.197759", "channel": "executives", "kind": "private", "date": "2025-08-25", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "D> <@EMPLOYEE_0025_SLACK_ID>. I want to retain code, IP and non-mobile distribution rights but anything else is up for grabs. 2- We 
  {"id": "C07C2866011/1756251167.453019", "channel": "executives", "kind": "private", "date": "2025-08-26", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "D> <@EMPLOYEE_0025_SLACK_ID>. I want to retain code, IP and non-mobile distribution rights but anything else is up for grabs. 2- We 
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gdocs 'Executives Biweekly Sync' as frederick_stone  scope: GDocs title + body_text
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_26e1f9a86761e35049192a", "name": "Executives Biweekly Sync.docx", "mime": "application/vnd.google-apps.document", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Executives Biweekly Sync"}

SEARCH slack 'advance' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=184 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=65 in 7 containers
  {"id": "C04RYU8TJ8K/1698948669.857269", "channel": "random", "kind": "public", "date": "2023-11-02", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "ummoning\" towers and place them statically on the board and advance by just placing more and more tower to leap frog until you destroy t
  {"id": "C04RYU8TJ8K/1701391761.119039", "channel": "random", "kind": "public", "date": "2023-12-01", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "r further progression. Speaking of progression, you have to advance at least 6 characters in this game, or you'll never keep up the gold g
  {"id": "C04RYU8TJ8K/1729730910.252789", "channel": "random", "kind": "public", "date": "2024-10-24", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "als, surfacing, and lighting. Everything works with all our advanced features, such as style references, character references, and person
  {"id": "C04RYU8TJ8K/1737063316.714239", "channel": "random", "kind": "public", "date": "2025-01-16", "user": "PERSON_6065_SLACK_ID", "reply": false, "snippet": "SpaceX designs, manufactures and launches advanced rockets and spacecraft."}
  {"id": "C04S28HSD0U/1678249985.265079", "channel": "product", "kind": "private", "date": "2023-03-08", "user": "PERSON_6046_SLACK_ID", "reply": true, "snippet": "what they do is not really advanced but we can always say we’ll do segmentation for single player events"}
  {"id": "C04S28HSD0U/1679676847.959599", "channel": "product", "kind": "private", "date": "2023-03-24", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "Either way it's advanced af"}
  {"id": "C04S28HSD0U/1680067668.683759", "channel": "product", "kind": "private", "date": "2023-03-29", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "Try playing it, it's freaking impossible to advance 10 levels without running out of lives"}
  {"id": "C04S28HSD0U/1680205974.017369", "channel": "product", "kind": "private", "date": "2023-03-30", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "Yeah basic animations, because if we want advanced stuff we'll have to hire"}
  {"id": "C04S28HSD0U/1680387851.467019", "channel": "product", "kind": "private", "date": "2023-04-01", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "If we have 10K levels, I'm OK to let people advance 3 levels per life on average"}
  {"id": "C04S28HSD0U/1682392460.426649", "channel": "product", "kind": "private", "date": "2023-04-25", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "the stars from finishing but you don't have to spend any to advance the story. You can also keep playing the levels, it doesn't stop yo
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'deep links' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C06M373FT63/1709843878.195429", "channel": "[SOURCE_ORG_0001]-gpt", "kind": "public", "date": "2024-03-07", "user": "SLACK_BOT_0013_SLACK_ID", "reply": false, "snippet": "enting logic for progressFraction calculation, and managing deep links for directing players to relevant game parts. [Cit
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH linear 'ENG-2362' as frederick_stone  scope: hg.py search (unscoped: no ACL filter)
visible hits=3 (showing 3)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/2304/relations/0/target", "parent_pointer": "/issues/2304/relations/0", "encoding": "json", "text": "ENG-2362", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/2305/id", "parent_pointer": "/issues/2305", "encoding": "json", "text": "ENG-2362", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/2305/identifier", "parent_pointer": "/issues/2305", "encoding": "json", "text": "ENG-2362", "truncated": false}

SEARCH slack 'Kestrel' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH contacts 'Anika' as frederick_stone  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH slack 'first-look' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'banker' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=9 (showing 9)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04S28HSD0U/1680068224.180609", "channel": "product", "kind": "private", "date": "2023-03-29", "user": "EMPLOYEE_0038_SLACK_ID", "reply": true, "snippet": "e management is crucial. They could be a frugal merchant or banker who always seeks to save money on their purchases. Their ability to e
  {"id": "C04UM32UWKD/1682100767.326789", "channel": "investors", "kind": "private", "date": "2023-04-21", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "he calls [PERSON_NAME_0080] a banker type"}
  {"id": "C04UM32UWKD/1682100796.741269", "channel": "investors", "kind": "private", "date": "2023-04-21", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I guess you could be a banker and play star craft :[USERNAME_3620]:"}
  {"id": "C07C2866011/1757345405.134829", "channel": "executives", "kind": "private", "date": "2025-09-08", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "rove in the next 2-3 weeks, I think it may be time to get a banker involved"}
  {"id": "C07C2866011/1758739303.608839", "channel": "executives", "kind": "private", "date": "2025-09-24", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "alked to [PERSON_NAME_6423] from SEMC and he has heard from bankers that NCsoft talks to everyone but they are extremely slow at mov
  {"id": "C07C2866011/1758739382.896799", "channel": "executives", "kind": "private", "date": "2025-09-24", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "s after end of next week it’s probably time to reach out to bankers"}
  {"id": "C07C2866011/1759290197.446099", "channel": "executives", "kind": "private", "date": "2025-10-01", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": " out in the next 7-10 days it is likely time to talk to the bankers"}
  {"id": "D05S58U4SAK/1756250547.405729", "channel": "D05S58U4SAK", "kind": "im", "date": "2025-08-26", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "2 people asked me do you have a banker, are you doing corpdev track"}
  {"id": "D05S58U4SAK/1756250583.504089", "channel": "D05S58U4SAK", "kind": "im", "date": "2025-08-26", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": "Did you say chatgpt is our banker? :[USERNAME_42656]:"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack '70% D1' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=6 (showing 6)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C07C2866011/1758378846.430339", "channel": "executives", "kind": "private", "date": "2025-09-20", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "N_NAME_59047] , [PERSON_NAME_59043] - The Standout Success: 70% D1 retention, 30% D14 retention (iOS-US) - metrics we haven't seen i
  {"id": "C07C2866011/1758736960.824899", "channel": "executives", "kind": "private", "date": "2025-09-24", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "how the fuck can you have 70% D1"}
  {"id": "D05S58U4SAK/1758737024.956899", "channel": "D05S58U4SAK", "kind": "im", "date": "2025-09-24", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": "70% D1? Almost hard to believe, even with the highest intent incent traffic."}
  {"id": "D05S58U4SAK/1758737132.730789", "channel": "D05S58U4SAK", "kind": "im", "date": "2025-09-24", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "it’s a not a game that will have 70% D1"}
  {"id": "D05S58U4SAK/1758737179.060429", "channel": "D05S58U4SAK", "kind": "im", "date": "2025-09-24", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": "What game will have 70% D1r?"}
  {"id": "D05S58U4SAK/1758737212.050999", "channel": "D05S58U4SAK", "kind": "im", "date": "2025-09-24", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": "Even that I'm not sure if you'll get 70% D1r."}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'talked to Matthew' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=8 (showing 8)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UM32UWKD/1682115625.283139", "channel": "investors", "kind": "private", "date": "2023-04-21", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "talked to Matthew:  his list to go after  *tier 1* makers, [PERSON_NAME_2000], play, index, [PERS"}
  {"id": "C04UM32UWKD/1685630956.995569", "channel": "investors", "kind": "private", "date": "2023-06-01", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Yo, talked to Matthew on the [PERSON_NAME_2000] term sheet. Apparently they are expecting us to say y"}
  {"id": "C04UM32UWKD/1697663899.891509", "channel": "investors", "kind": "private", "date": "2023-10-18", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "talked to Matthew, he is not supportive of chasing Apple Arcade/Netflix etc. in general because i"}
  {"id": "C07C2866011/1736551646.682939", "channel": "executives", "kind": "private", "date": "2025-01-10", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "good news - I talked to Matthew and he is on board with the plan"}
  {"id": "C07C2866011/1746053163.773989", "channel": "executives", "kind": "private", "date": "2025-04-30", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "talked to Matthew"}
  {"id": "C07C2866011/1746058658.875709", "channel": "executives", "kind": "private", "date": "2025-05-01", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "but talked to Matthew on that too as I mentioned earlier"}
  {"id": "C07C2866011/1748987610.562589", "channel": "executives", "kind": "private", "date": "2025-06-03", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Talked to Matthew"}
  {"id": "C096HFA5Z8W/1758147530.732569", "channel": "bridge-pitch", "kind": "private", "date": "2025-09-17", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "talked to Matthew - he says it’s almost impossible to raise based on the content/metrics for Harm"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'one-pager' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C05H8KVNU67/1731482756.388939", "channel": "game-design", "kind": "private", "date": "2024-11-13", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "this with clear instructions on how to create a comic style one-pager is what I wanted to show"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gcal 'Tallwater' as frederick_stone  scope: GCal event summary (base events carry no description/location)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
note: counted per meeting instance (ical_uid + start), visible if any copy is visible

SEARCH trello 'F/up with Lena' as frederick_stone  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH trello 'F/up with Marek' as frederick_stone  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gmail 'License paper timing' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'first-look' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "frederick.stone@harmonygames.co/1821892717497372991", "last": "2025-01-21T20:44:51Z", "subject": "Config 2025: Why you can't miss it", "snippet": "ut what to expect at Config 2025  [https://Figma.com/blog/a-first-look-at-config-2025/]    Figma is a design platform for teams who build product
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Appodeal publishing Program' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=2 (showing 2)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "frederick.stone@harmonygames.co/1829689338387596598", "last": "2025-04-17T22:08:32Z", "subject": "We received your application - Next steps", "snippet": "36]  We’re thrilled that you’ve taken the step to apply for Appodeal publishing Program. Game developers like you are the heart of what we
  {"id": "frederick.stone@harmonygames.co/1830012626042968381", "last": "2025-05-21T05:33:45Z", "subject": "Re: Appodeal publishing Program", "snippet": "Re: Appodeal publishing Program"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Board Follow-Up' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "frederick.stone@harmonygames.co/1830890312657338682", "last": "2025-05-01T04:19:37Z", "subject": "Re: Board Follow-Up [SOURCE_ORG_0001]: Domino Delights Metrics, Runway Discipline, and 4X Proposal", "snippet": "Re: Board Follow-Up [SOURCE_ORG_0001]: Domino Delights Metrics, Runway Discipline
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Rayking' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "frederick.stone@harmonygames.co/1842348778705877030", "last": "2025-09-04T17:41:50Z", "subject": "Re: Chinese Local Game publishing", "snippet": "ERSON_NAME_49709], and I am the   > manager of marketing at Rayking Game, a leading game publishing company   > based in China. Please pardon the 
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'Rayking' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'focus Homa' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C096HFA5Z8W/1758210489.170809", "channel": "bridge-pitch", "kind": "private", "date": "2025-09-18", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": "I think we should focus Homa on the co-dev investment path."}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'NCsoft' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=20 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C07C2866011/1747282330.535609", "channel": "executives", "kind": "private", "date": "2025-05-15", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Talked to NCsoft. They are super interested in talking to us more. Very impressed with our Harmo"}
  {"id": "C07C2866011/1757516293.887729", "channel": "executives", "kind": "private", "date": "2025-09-10", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "So is NCsoft publishing?  investing? Or we don't really know?"}
  {"id": "C07C2866011/1757523685.461369", "channel": "executives", "kind": "private", "date": "2025-09-10", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "We all gonna work for NCSoft? hah"}
  {"id": "C07C2866011/1757523715.053849", "channel": "executives", "kind": "private", "date": "2025-09-10", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "I'm surprised NCsoft is so late into the mobile casual games"}
  {"id": "C07C2866011/1758134424.689839", "channel": "executives", "kind": "private", "date": "2025-09-17", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "RSON_NAME_0854] is tomorrow as well, Friday second round of NCSOFT, Monday [USERNAME_1161] and t-accelerate, tuesday [USERNAME_5817]
  {"id": "C07C2866011/1758135942.903089", "channel": "executives", "kind": "private", "date": "2025-09-17", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": "These 8am meetings ([PERSON_NAME_0854] and NCSOFT) are tough for me. I'll try my best but may need to jump on late or take part o"}
  {"id": "C07C2866011/1758135956.716939", "channel": "executives", "kind": "private", "date": "2025-09-17", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "NCsoft you can skip if you want"}
  {"id": "C07C2866011/1758291198.457989", "channel": "executives", "kind": "private", "date": "2025-09-19", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": "Confirming I'll skip the NCSoft demo."}
  {"id": "C07C2866011/1758739303.608839", "channel": "executives", "kind": "private", "date": "2025-09-24", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "SON_NAME_6423] from SEMC and he has heard from bankers that NCsoft talks to everyone but they are extremely slow at moving forward s
  {"id": "C07C2866011/1758739449.333829", "channel": "executives", "kind": "private", "date": "2025-09-24", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "Because it's NCsoft"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Tilting Point' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=3 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "frederick.stone@harmonygames.co/1822685416297870441", "last": "2025-01-30T14:44:26Z", "subject": "Predicting the future of mobile game monetization 🔮", "snippet": "m-campaign-Jan25/c5wg4/982361898/h/y2Lj[USERNAME_1752]  How Tilting Point is unlocking the value of D2C webstores  [PERSON_NAME_
  {"id": "frederick.stone@harmonygames.co/1834169618424444784", "last": "2025-06-06T09:00:50Z", "subject": "3 steps to Shift 10% off Major App Stores, May's Top Mobile Games & Big News from Turborilla", "snippet": "+ how Tilting Point’s $150M UA fund is reshaping growth and creative strategy    View i
  {"id": "frederick.stone@harmonygames.co/1842443183462721250", "last": "2025-09-05T16:45:42Z", "subject": "'UA Funding request", "snippet": " with us and will be in touch if we    can move forward.    Tilting Point"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gdocs 'Publishing Partners' as frederick_stone  scope: GDocs title + body_text
visible hits=1 (showing 1)  hidden by ACL=1 in 1 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_10dfa1b4236a7c35dcb632", "name": "Publishing Partners.docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "Publishing Partners"}

SEARCH gdocs 'Biz Dev Notes' as frederick_stone  scope: GDocs title + body_text
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_0d17fc08eddaf231cf7f28", "name": "Biz Dev Notes.docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "Biz Dev Notes"}

SEARCH gcal 'DD publishing' as frederick_stone  scope: GCal event summary (base events carry no description/location)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
note: counted per meeting instance (ical_uid + start), visible if any copy is visible

SEARCH contacts 'Lena' as frederick_stone  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH snowflake 'REVENUE_DAILY' as frederick_stone  scope: hg.py search (unscoped: no ACL filter)
visible hits=10 (showing 10)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/12/name", "parent_pointer": "/tables/12", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/12/id", "parent_pointer": "/tables/12", "encoding": "json", "text": "ANALYTICS.MONETIZATION.REVENUE_DAILY", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/name", "parent_pointer": "/tables/13", "encoding": "json", "text": "REVENUE_DAILY_V2", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/id", "parent_pointer": "/tables/13", "encoding": "json", "text": "ANALYTICS.MONETIZATION.REVENUE_DAILY_V2", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/rows/0/source_table", "parent_pointer": "/tables/13/rows/0", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/rows/1/source_table", "parent_pointer": "/tables/13/rows/1", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/rows/2/source_table", "parent_pointer": "/tables/13/rows/2", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/rows/3/source_table", "parent_pointer": "/tables/13/rows/3", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/rows/4/source_table", "parent_pointer": "/tables/13/rows/4", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/rows/5/source_table", "parent_pointer": "/tables/13/rows/5", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}

SEARCH slack 'looking for games' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "D05S58U4SAK/1758736842.534589", "channel": "D05S58U4SAK", "kind": "im", "date": "2025-09-24", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "There was a dude from [USERNAME_34104] looking for games"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'Tamatem' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=2 (showing 2)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C48D58CD7FBD/1748974194.583999", "channel": "mpdm-leonard.hayes--julia.lawson--frederick.stone-1", "kind": "mpim", "date": "2025-06-03", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "<https://tamateminc.Helpshift.com/hc/en/3-tamatem-inc/>"}
  {"id": "C48D58CD7FBD/1748974617.722599", "channel": "mpdm-leonard.hayes--julia.lawson--frederick.stone-1", "kind": "mpim", "date": "2025-06-03", "user": "EMPLOYEE_0005_SLACK_ID", "reply": false, "snippet": "[PERSON_NAME_0036], hey. Tamatem is a very good publisher who specializes in scaling games in
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'signed someone for dominoes' as frederick_stone  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C07C2866011/1756261199.570279", "channel": "executives", "kind": "private", "date": "2025-08-27", "user": "EMPLOYEE_0038_SLACK_ID", "reply": true, "snippet": "[PERSON_NAME_9160] thought and then we learned they already signed someone for dominoes"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Oakline' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Tallwater' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Sunfold' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Harbor' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Wavecrest' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Moonrail' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Northglow' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Pinegrove' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Fernhollow' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Quietbay' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Slatewood' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Ironbridge' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Tidewell' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Marlin' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Kitebridge' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Orchard' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Summit' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=3 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "frederick.stone@harmonygames.co/1811348022795472184", "last": "2024-09-27T11:21:27Z", "subject": "Gamesforum Focus: Gamesforum London recap, hybrid strategies, latest podcast and more...", "snippet": "t off the heels of [ORGANIZATION_NAME_8593] Ad Monetization Summit. Leaders from companies 
  {"id": "frederick.stone@harmonygames.co/1830295795657785249", "last": "2025-04-24T14:48:09Z", "subject": "LevelUp Newsletter April: This month’s news, insights, and events", "snippet": "0uMzN2cAXLciaSpuuukaqq7Ed4Hp-tQTaIihIvzQ     Dubai GameExpo Summit: Unity Happy Hour      Join Unity for an evenin
  {"id": "frederick.stone@harmonygames.co/1830364442392364276", "last": "2025-04-25T08:59:17Z", "subject": "How to get investment for your game in 2025, Midcore's massive comeback & more", "snippet": "Ydb8BN5WRW3746vb6HvbDGdGGfXz04 )    Join the Dubai GameExpo Summit, powered by PG Connects, on May 7-
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Silverlake' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Cedarbrook' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Foxglove' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Riverstone' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Bellwether' as frederick_stone  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gdocs 'Oakline Games - term sheet' as frederick_stone  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gdocs 'Tallwater Games - term sheet' as frederick_stone  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gdocs 'Sunfold Mobile - term sheet' as frederick_stone  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gdocs 'Harbor Lane Games - term sheet' as frederick_stone  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gdocs 'Wavecrest Play - term sheet' as frederick_stone  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gdocs 'Moonrail Studios - term sheet' as frederick_stone  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gdocs 'Northglow Publishing - term sheet' as frederick_stone  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gdocs 'Pinegrove Games - term sheet' as frederick_stone  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

Search-behaviour risks (design notes only, never in the prompt): runs latch onto the outreach sheet as the population; they stop at Marek's 'sent' mail; they rarely open replies under old roots; they read the first lines of a calendar description; they treat cards named for people as unrelated; Snowflake isn't advertised, but the rule doc names the table.

## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · persona-readable · unique · instructions-not-answer) | Inferable |
|---|---|---|---|---|
| R1 population | f_5e355d03f6eb6a4e866ead | deliverable (the model) | frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> → f_5e355d03f6eb6a4e866ead · YES · one doc · states who counts, not who they are | yes |
| R2 status | f_5e355d03f6eb6a4e866ead | deliverable | f_5e355d03f6eb6a4e866ead · YES · one doc · states the order, not the answers | yes |
| R3 latest terms | f_5e355d03f6eb6a4e866ead | deliverable | f_5e355d03f6eb6a4e866ead 'latest terms' · YES · one sentence · no values | yes |
| R4 12-month value | f_5e355d03f6eb6a4e866ead | deliverable | f_5e355d03f6eb6a4e866ead · YES · a formula, no results | yes |
| R5 Q4 cash and banked | f_5e355d03f6eb6a4e866ead | deliverable | f_5e355d03f6eb6a4e866ead and frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> · YES · a definition, no results | yes |
| R6 rights | C07C2866011/1756140953.197759 | constraint, via the doc | f_5e355d03f6eb6a4e866ead → C07C2866011/1756140953.197759, f_26e1f9a86761e35049192a · YES · 'the August sync' · a position, not a verdict | yes |
| R7 first pick | f_5e355d03f6eb6a4e866ead | deliverable | f_5e355d03f6eb6a4e866ead · YES · a definition | yes |
| R8 keep value | f_5e355d03f6eb6a4e866ead | deliverable | f_5e355d03f6eb6a4e866ead · YES · names the table, gives no number | yes |
| R9 board writes | 68dab660c900179df4f5f92d | deliverable (the card) | frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> → 68dab660c900179df4f5f92d · YES · one card · instructions | yes |
| R10 contacts | frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> | deliverable, via the hub | frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> · YES · one sentence · no names | yes |
| R11 reminders | f_5e355d03f6eb6a4e866ead | deliverable, via the doc | f_5e355d03f6eb6a4e866ead · YES · no dates | yes |
| R12 organic notes | C096HFA5Z8W/1758915000.867092 | deliverable, via the doc's last line | f_5e355d03f6eb6a4e866ead (says the notes are owed) → C096HFA5Z8W/1758915000.867092 · YES · one reply · an instruction, no recipient list | yes |
| R13 reply | frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> | deliverable and recipient | frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> · YES · lists the asks, gives no values | yes |

| Anchor | May be named |
|---|---|
| A1 | Leonard's email from yesterday; Leonard's email yesterday; his email |
| A2 | the DD publishing card |
| A3 | my DD publishing folder; the DD publishing folder |

## 7 · Dates and constraints

| Item | Absolute date or value | Source | Past fact or deadline |
|---|---|---|---|
| Today | Wed Oct 1, 2025 (Pacific) | 00_Task_Context.json universe.persona_today; the day after frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> | clock |
| Leonard's email ('yesterday') | Tue Sep 30, 2025 4:10 PM PT = 2025-09-30T23:10:00Z | frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> | past fact |
| Founders' meeting | Mon Oct 6, 2025 10:00 AM PT = 2025-10-06T17:00:00Z | evt_881d3e07c598b2205a7ff3 | deadline (plan field) |
| Scope start | Apr 1, 2025 | f_5e355d03f6eb6a4e866ead | past fact |
| Signing, as first assumed | Oct 31, 2025 | f_5e355d03f6eb6a4e866ead | superseded |
| Signing | Nov 14, 2025 | frederick.stone@harmonygames.co/<CA9raR_pqldShsvOhd5Uwxoj8zJh2-tzH0UJ5JLd@mail.gmail.com> | deadline |
| Q4 window | Oct 1 to Dec 31, 2025 | f_5e355d03f6eb6a4e866ead | deadline |
| Net 30 / 45 / 60 from Nov 14 | Dec 14, 2025 / Dec 29, 2025 / Jan 13, 2026 | f_5e355d03f6eb6a4e866ead | computed |
| Response dates | Oct 17 (Tallwater, Copperleaf), Oct 24 (Oakline, Harbor Lane), Oct 31 (Sunfold, Wavecrest, Redwood) | f_e8cb875d5b7c8d9972d259, 495d71a7e14dfaa68cac26fc4a6c4e03 | deadlines |
| Keep-value months | Jul, Aug, Sep 2025 | snowflake.wh_analytics__monetization__revenue_daily | past fact |
| Oakline's wire | sent Sep 29, 2025; returned; resent the week of Oct 6 | frederick.stone@harmonygames.co/<CAybuYiHDdC_1wq0wp32aITdzH-XuQAf6p028lBn@mail.gmail.com>, 0230b2df24ec829928fe1c55ad6185bf | past fact |

## 8 · Difficulty levers

| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |
|---|---|---|---|---|
| Ambiguity | yes | yes | where each offer and correction lives; the prompt names the job and the known destinations only (A1, A2, A3) | vague about where answers live, never about what's asked |
| Dynamic change | yes | yes | term sheets, Marek's 'sent' and the rule doc's Oct 31 are met first (T1, T2, T7, T9) | the prompt names neither the summary nor the correction |
| Multi-source | yes | yes | 10 services plus Snowflake | no source named as an exact artifact beyond the anchors |
| Async | no | — | — | no wait configured (03_Error_Async_Config.txt: Friction: none) |
| Error recovery | no | — | — | no forced error |
| Access control | no | — | — | every deciding record is Frederick-visible (§5a) |

## 9 · Must not appear in the prompt

- Tool and server names (`Evals/references/tools/catalog.json`): gmail_search_messages, gmail_get_thread, gmail_reply_to_message, gmail_create_draft, gdrive_search, gdrive_move_file, gdocs_get_document, gsheets_create_spreadsheet, gsheets_values_update, gslides_get_presentation, slack_read_thread, trello_create_card, trello_add_comment, trello_create_checklist, trello_create_check_item, contacts_add_new_contact, contacts_search_contacts, gcal_create_event, snowflake_execute_query, and any MCP server name.
- Ids and opaque names: any f_/d_/evt_ id, thread or message id, Slack channel id or ts, ENG-2362, card or list ids, PERSON_ tokens, the warehouse table name.
- Root causes and findings (from §5): the returned wire, the Tallwater note, the Sunfold comment, Kestrel, the rights position, Copperleaf, Redwood, the Nov 14 date, the organic figure and Leonard's standing line.
- The rules themselves: status order, who's in, the value formula, the Q4 definition, reminders, layout.
- Any publisher name, status, amount, date or count (26 publishers, 7 Live, 15 cards, 14 contacts, 10 drafts, 7 reminders).
- Wording close to a fundraising hand-off, investor list or bridge round (dataset-duplicate risk).
- Markdown, numbered steps, per-deliverable content lists or format rules (they belong in the records).

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

LOOKALIKE_HANDLES_AND_ALIASES (15)
  - Gmail thread files of arthur.blake@harmonygames.co are named 'blake@harmonygames.co_*'
  - Gmail thread files of brian.foster@harmonygames.co are named 'brian@harmonygames.co_*'
  - Gmail thread files of calvin.price@harmonygames.co are named 'calvin@harmonygames.co_*'
  - Gmail thread files of claire.morgan@harmonygames.co are named 'claire@harmonygames.co_*'
  - Gmail thread files of frederick.stone@harmonygames.co are named 'frederick@harmonygames.co_*'
  - Gmail thread files of julia.lawson@harmonygames.co are named 'jlawson@harmonygames.co_*'
  - Gmail thread files of leonard.hayes@harmonygames.co are named 'leonard@harmonygames.co_*'
  - Gmail thread files of oliver.brooks@harmonygames.co are named 'oliver@harmonygames.co_*'
  - Gmail thread files of owen.baker@harmonygames.co are named 'owen@harmonygames.co_*'
  - Gmail thread files of samuel.turner@harmonygames.co are named 'samuel@harmonygames.co_*'
  - Gmail thread files of simon.walker@harmonygames.co are named 'simon@harmonygames.co_*'
  - Gmail thread files of vincent.parker@harmonygames.co are named 'vincent@harmonygames.co_*'
  - Gmail thread files of felix.young@harmonygames.co are named 'felixyoung@harmonygames.co_*'
  - Gmail thread files of oscar.bennett@harmonygames.co are named 'oscar@harmonygames.co_*'
  - Slack handle 'thomas' (U05F0A0D12F) belongs to Thomas Baker <thomas.baker@harmonygames.co> but equals the mailbox local part of Thomas <thomas@harmonygames.co> [persona thomas]

LOOKALIKE_EMAIL_LOCAL_PARTS (1)
  - 'thomas@' vs 'thomas.baker@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['Thomas Baker <thomas.baker@harmonygames.co>']

TOKENS_MAPPING_TO_SEVERAL_ENTITIES (9)
  EMPLOYEE_0024: {'entities': ['scott <employee_0024@harmonygames.co>', '? <slack:EMPLOYEE_0024_SLACK_ID>', '? <trello:3d36d70154e6a715614e0d75>'], 'records': ['gcal.calendar_id=employee_0024@harmonygames.co', 'gcal.owner_email=employee_0024@harmonygames.co', 'linear.id=usr_EMPLOYEE_0024', 'linear.email=employee_0024@harmonygames.co', 'contacts.email=employee_0024@harmonygames.co', 'email.email=employee_0024@harmonygames.co', 'slack.id=EMPLOYEE_0024_SLACK_ID', 'trello.username=employee_0024']}
  EMPLOYEE_0032: {'entities': ['? <EMPLOYEE_0032_EMAIL>', 'Josh Dempsey <josh.dempsey@harmonygames.co>', '? <github:EMPLOYEE_0032_GITHUB_USERNAME>', '? <slack:EMPLOYEE_0032_SLACK_ID>'], 'records': ['confluence.id=user_EMPLOYEE_0032', 'gmail.mailbox=EMPLOYEE_0032_EMAIL', 'gdrive.email=EMPLOYEE_0032_EMAIL', 'linear.id=usr_EMPLOYEE_0032', 'linear.email=EMPLOYEE_0032_EMAIL', 'contacts.email=EMPLOYEE_0032_EMAIL', 'email.email=EMPLOYEE_0032_EMAIL', 'github.login=EMPLOYEE_0032_GITHUB_USERNAME', 'slack.id=EMPLOYEE_0032_SLACK_ID']}
  PERSON_2218: {'entities': ['? <PERSON_2218_EMAIL>', '? <github:PERSON_2218_GITHUB_USERNAME>'], 'records': ['linear.id=usr_PERSON_2218', 'linear.email=PERSON_2218_EMAIL', 'contacts.email=PERSON_2218_EMAIL', 'email.email=PERSON_2218_EMAIL', 'github.login=PERSON_2218_GITHUB_USERNAME']}
  PERSON_2360: {'entities': ['? <PERSON_2360_EMAIL>', 'Claire <github:PERSON_2360_GITHUB_USERNAME>'], 'records': ['github.login=PERSON_2360_GITHUB_USERNAME', 'email.email=PERSON_2360_EMAIL']}
  PERSON_3233: {'entities': ['? <PERSON_3233_EMAIL>', '? <github:PERSON_3233_GITHUB_USERNAME>', '? <slack:PERSON_3233_SLACK_ID>'], 'records': ['linear.id=usr_PERSON_3233', 'linear.email=PERSON_3233_EMAIL', 'contacts.email=PERSON_3233_EMAIL', 'email.email=PERSON_3233_EMAIL', 'github.login=PERSON_3233_GITHUB_USERNAME', 'slack.id=PERSON_3233_SLACK_ID']}
  PERSON_3335: {'entities': ['? <PERSON_3335_EMAIL>', '? <slack:PERSON_3335_SLACK_ID>'], 'records': ['contacts.email=PERSON_3335_EMAIL', 'email.email=PERSON_3335_EMAIL', 'slack.id=PERSON_3335_SLACK_ID']}
  PERSON_3935: {'entities': ['? <PERSON_3935_EMAIL>', '? <slack:PERSON_3935_SLACK_ID>'], 'records': ['email.email=PERSON_3935_EMAIL', 'slack.id=PERSON_3935_SLACK_ID']}
  PERSON_5275: {'entities': ['? <PERSON_5275_EMAIL>', '? <slack:PERSON_5275_SLACK_ID>'], 'records': ['contacts.email=PERSON_5275_EMAIL', 'email.email=PERSON_5275_EMAIL', 'slack.id=PERSON_5275_SLACK_ID']}
  PERSON_5360: {'entities': ['? <PERSON_5360_EMAIL>', '? <slack:PERSON_5360_SLACK_ID>'], 'records': ['email.email=PERSON_5360_EMAIL', 'slack.id=PERSON_5360_SLACK_ID']}

SEVERAL_IDS_IN_ONE_SERVICE (1)
  - Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]: 2 github identities ['PERSON_0003_GITHUB_USERNAME', 'PERSON_2137_GITHUB_USERNAME'] (joins: ['exact_email', 'exact_name'])

PERSONA_ROLE_VS_CONTACTS_JOB (5)
  - Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]: roster role 'Game Engineer (Unity VFX)' vs Contacts job 'Game Engineer (Unity/VFX)'
  - Frederick Stone <frederick.stone@harmonygames.co> [persona frederick_stone]: roster role 'Co-founder' vs Contacts job 'Commercial Lead, Marketing & Business Development'
  - Leonard Hayes <leonard.hayes@harmonygames.co> [persona leonard_hayes]: roster role 'Co-founder & Creative Director' vs Contacts job 'Co-founder & CEO'
  - Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]: roster role 'Artist' vs Contacts job 'Artist (VFX & Animation)'
  - Robert <robert@harmonygames.co> [persona robert]: roster role 'Co-Founder & Creative Director' vs Contacts job 'Co-founder & Chief Product Officer'

SHARED_CONTACT_JOB_TITLES (5)
  Game Designer: ['Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]', 'Samuel Turner <samuel.turner@harmonygames.co> [persona samuel_turner]']
  Game Developer: ['Thomas <thomas@harmonygames.co> [persona thomas]', 'Lucas <lucas@harmonygames.co>']
  Game Engineer: ['Brian Foster <brian.foster@harmonygames.co> [persona brian_foster]', 'Victor Barnes <victor.barnes@harmonygames.co> [persona victor_barnes]']
  General Counsel: ['Michelle Carter <michelle.carter@harmonygames.co>', 'Thomas Baker <thomas.baker@harmonygames.co>']
  User Acquisition Manager: ['George Miller <george.miller@harmonygames.co>', 'Megan Wilson <megan.wilson@harmonygames.co>', 'Victoria Lane <victoria.lane@harmonygames.co>']

UNRESOLVED (11)
  [ambiguous_name] github: mononym 'Claire' is an exact name of [] and the first name of ['email:claire.morgan@harmonygames.co'] -> candidates ['email:claire.morgan@harmonygames.co']
  [ambiguous_name] trello: mononym 'Marcus' is an exact name of [] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co'] -> candidates ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']
  [token_link] EMPLOYEE_0024: same token number across services but no shared exact email/name: not joined -> candidates ['email:employee_0024@harmonygames.co', 'slack:EMPLOYEE_0024_SLACK_ID', 'trello:3d36d70154e6a715614e0d75']
  [token_link] EMPLOYEE_0032: same token number across services but no shared exact email/name: not joined -> candidates ['email:EMPLOYEE_0032_EMAIL', 'email:josh.dempsey@harmonygames.co', 'github:EMPLOYEE_0032_GITHUB_USERNAME', 'slack:EMPLOYEE_0032_SLACK_ID']
  [token_link] PERSON_2218: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_2218_EMAIL', 'github:PERSON_2218_GITHUB_USERNAME']
  [token_link] PERSON_2360: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_2360_EMAIL', 'github:PERSON_2360_GITHUB_USERNAME']
  [token_link] PERSON_3233: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3233_EMAIL', 'github:PERSON_3233_GITHUB_USERNAME', 'slack:PERSON_3233_SLACK_ID']
  [token_link] PERSON_3335: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3335_EMAIL', 'slack:PERSON_3335_SLACK_ID']
  [token_link] PERSON_3935: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3935_EMAIL', 'slack:PERSON_3935_SLACK_ID']
  [token_link] PERSON_5275: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_5275_EMAIL', 'slack:PERSON_5275_SLACK_ID']
  [token_link] PERSON_5360: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_5360_EMAIL', 'slack:PERSON_5360_SLACK_ID']

INTEGRITY FLAGS (2)
  {'type': 'id_with_space', 'service': 'linear', 'id': 'usr_Victor Barnes'}
  {'type': 'name_mismatch_on_email_join', 'service': 'github', 'id': 'PERSON_2314_GITHUB_USERNAME', 'detail': "GitHub PERSON_2314_GITHUB_USERNAME joined by email but shows name 'Ryan' (entity is Frederick Stone)"}
ENTITY email:frederick.stone@harmonygames.co  name=Frederick Stone  kind=person  emails=['frederick.stone@harmonygames.co']
  persona: frederick_stone - Co-founder / Executive
  slack      id=EMPLOYEE_0008_SLACK_ID, name=Frederick Stone, real_name=Frederick Stone, email=frederick.stone@harmonygames.co, is_bot=False, deleted=False, messages=4780, first_post=2023-09-15, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=frederick.stone@harmonygames.co, threads=4656, messages=5474, first=2024-06-25, last=2025-10-01, thread_filename_alias=['frederick@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=frederick.stone@harmonygames.co, owner_email=frederick.stone@harmonygames.co, summary=Frederick Stone — primary, events=316, last_event_before_clock=2025-09-30   [join: exact_email]
  gdrive     id=user_175c0d7bc72e, email=frederick.stone@harmonygames.co, display_name=frederick.stone@harmonygames.co, root_folders=['d_175c0d7bc72ed244b944cb'], owned_items=46, last_modified=2025-09-24, files_shared_with=213   [join: exact_email]
  linear     id=usr_175c0d7bc72ed244, email=frederick.stone@harmonygames.co, name=frederick.stone@harmonygames.co, is_active=True, last_activity=2025-08-26   [join: exact_email]
  github     login=PERSON_2314_GITHUB_USERNAME, name=Ryan, email=frederick.stone@harmonygames.co, type=User, last_activity=2025-03-25   [join: exact_email]
  trello     id=4b4a68fc0fec0b254e4f9d8e, username=frederick.stone, fullName=Frederick Stone   [join: exact_name]
  confluence id=user_EMPLOYEE_0008, account_id=acct_EMPLOYEE_0008, email=frederick.stone@harmonygames.co, display_name=Frederick Stone, is_active=True, last_activity=2025-09-01   [join: exact_email]
  contacts   contact_id=175c0d7bc72ed244b944cb90, name=Frederick Stone, email=frederick.stone@harmonygames.co, job=Commercial Lead, Marketing & Business Development, is_user=False   [join: exact_email]
  last activity: {'slack': '2025-09-30', 'gmail': '2025-10-01', 'gcal': '2025-09-30', 'gdrive': '2025-09-24', 'linear': '2025-08-26', 'github': '2025-03-25', 'confluence': '2025-09-01'}
  FLAG: GitHub PERSON_2314_GITHUB_USERNAME joined by email but shows name 'Ryan' (entity is Frederick Stone)
ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
  persona: leonard_hayes - Co-founder & Creative Director / Executive
  slack      id=EMPLOYEE_0038_SLACK_ID, name=Leonard Hayes, real_name=Leonard Hayes, email=leonard.hayes@harmonygames.co, is_bot=False, deleted=False, messages=129898, first_post=2023-03-15, last_post=2025-10-01   [join: exact_email]
  gmail      mailbox=leonard.hayes@harmonygames.co, threads=15339, messages=19668, first=2023-03-15, last=2025-10-01, thread_filename_alias=['leonard@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=leonard.hayes@harmonygames.co, owner_email=leonard.hayes@harmonygames.co, summary=Leonard Hayes — primary, events=1382, last_event_before_clock=2025-09-30   [join: exact_email]
  gdrive     id=user_63fffeb4fab5, email=leonard.hayes@harmonygames.co, display_name=leonard.hayes@harmonygames.co, root_folders=['d_63fffeb4fab5233ed5bb73'], owned_items=752, last_modified=2025-09-30, files_shared_with=365   [join: exact_email]
  linear     id=usr_63fffeb4fab5233e, email=leonard.hayes@harmonygames.co, name=leonard.hayes@harmonygames.co, is_active=True, last_activity=2025-09-22   [join: exact_email]
  trello     id=PERSON_6094_TRELLO_USER_ID, username=leonard.hayes, fullName=Leonard Hayes, last_activity=2025-09-30   [join: exact_name]
  confluence id=user_EMPLOYEE_0038, account_id=acct_EMPLOYEE_0038, email=leonard.hayes@harmonygames.co, display_name=Leonard Hayes, is_active=True, last_activity=2025-09-29   [join: exact_email]
  contacts   contact_id=63fffeb4fab5233ed5bb73bf, name=Leonard Hayes, email=leonard.hayes@harmonygames.co, job=Co-founder & CEO, is_user=False   [join: exact_email]
  absent from: github
  last activity: {'slack': '2025-10-01', 'gmail': '2025-10-01', 'gcal': '2025-09-30', 'gdrive': '2025-09-30', 'linear': '2025-09-22', 'trello': '2025-09-30', 'confluence': '2025-09-29'}
ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
  persona: arthur_blake - Co-founder & CTO / Executive
  slack      id=EMPLOYEE_0025_SLACK_ID, name=Arthur Blake, real_name=Arthur Blake, email=arthur.blake@harmonygames.co, is_bot=False, deleted=False, messages=35266, first_post=2023-03-20, last_post=2025-10-01   [join: exact_email]
  gmail      mailbox=arthur.blake@harmonygames.co, threads=3320, messages=5134, first=2023-03-23, last=2025-10-01, thread_filename_alias=['blake@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=arthur.blake@harmonygames.co, owner_email=arthur.blake@harmonygames.co, summary=Arthur Blake — primary, events=756, last_event_before_clock=2025-09-30   [join: exact_email]
  gdrive     id=user_cc3e90160f49, email=arthur.blake@harmonygames.co, display_name=arthur.blake@harmonygames.co, root_folders=['d_cc3e90160f490686039986'], owned_items=246, last_modified=2025-09-19, files_shared_with=403   [join: exact_email]
  linear     id=usr_cc3e90160f490686, email=arthur.blake@harmonygames.co, name=arthur.blake@harmonygames.co, is_active=True, last_activity=2025-09-15   [join: exact_email]
  github     login=EMPLOYEE_0025_GITHUB_USERNAME, name=Arthur Blake, email=arthur.blake@harmonygames.co, type=User, last_activity=2025-09-30   [join: exact_email]
  trello     id=2162c1ba310341bf318f48b7, username=arthur.blake, fullName=Arthur Blake   [join: exact_name]
  confluence id=user_EMPLOYEE_0025, account_id=acct_EMPLOYEE_0025, email=arthur.blake@harmonygames.co, display_name=Arthur Blake, is_active=True, last_activity=2025-09-12   [join: exact_email]
  contacts   contact_id=cc3e90160f49068603998654, name=Arthur Blake, email=arthur.blake@harmonygames.co, job=Co-founder & CTO, is_user=False   [join: exact_email]
  last activity: {'slack': '2025-10-01', 'gmail': '2025-10-01', 'gcal': '2025-09-30', 'gdrive': '2025-09-19', 'linear': '2025-09-15', 'github': '2025-09-30', 'confluence': '2025-09-12'}
ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
  persona: robert - Co-Founder & Creative Director / Executive
  slack      id=EMPLOYEE_0016_SLACK_ID, name=Robert, real_name=Robert, email=robert@harmonygames.co, is_bot=False, deleted=False, messages=110334, first_post=2023-03-15, last_post=2025-10-01   [join: exact_email]
  gmail      mailbox=robert@harmonygames.co, threads=14813, messages=17363, first=2023-03-15, last=2025-10-01   [join: exact_email]
  gcal       calendar_id=robert@harmonygames.co, owner_email=robert@harmonygames.co, summary=Robert — primary, events=1133, last_event_before_clock=2025-09-30   [join: exact_email]
  gdrive     id=user_9f7ba94f7526, email=robert@harmonygames.co, display_name=Robert, root_folders=['d_9f7ba94f7526d54d8482ba'], owned_items=190, last_modified=2025-09-25, files_shared_with=412   [join: exact_email]
  linear     id=usr_Robert, email=robert@harmonygames.co, name=Robert, is_active=True, last_activity=2025-09-30   [join: exact_email]
  github     login=EMPLOYEE_0016_GITHUB_USERNAME, name=Robert, email=robert@harmonygames.co, type=User, last_activity=2025-09-29   [join: exact_email]
  trello     id=3d06b73654d0c8940792514c, username=robert, fullName=Robert   [join: exact_name]
  confluence id=user_EMPLOYEE_0016, account_id=acct_EMPLOYEE_0016, email=robert@harmonygames.co, display_name=Robert, is_active=True, last_activity=2025-09-30   [join: exact_email]
  contacts   contact_id=5f647df33ba6e92fbd56b05b, name=Robert, email=robert@harmonygames.co, job=Co-founder & Chief Product Officer, is_user=True   [join: exact_email]
  last activity: {'slack': '2025-10-01', 'gmail': '2025-10-01', 'gcal': '2025-09-30', 'gdrive': '2025-09-25', 'linear': '2025-09-30', 'github': '2025-09-29', 'confluence': '2025-09-30'}
no exact match for 'Lena'
no exact match for 'Marek'
no exact match for 'Paola'
no exact match for 'Diego'
no exact match for 'Sofia'
no exact match for 'Anika'
no exact match for 'Jonas'
no exact match for 'Mei'
```

| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |
|---|---|---|---|
| Leonard Hayes | file alias leonard@ | one person | leonard.hayes@harmonygames.co |
| Arthur Blake | file alias blake@ | one person | arthur.blake@harmonygames.co |
| Robert | no surname in any service | one person | robert@harmonygames.co |
| Frederick Stone | GitHub display name 'Ryan' (S04); file alias frederick@ | GitHub not used | frederick.stone@harmonygames.co |
| UA/BD board | the other boards, each with its own lists | the card's board | 66da196af476ab78deaa0cef (list 670015c2ecd45b634d5eec81) |
| the ground rules doc | the co-dev doc | scope: DD publishing vs co-dev | f_5e355d03f6eb6a4e866ead vs f_21203dbcdf780cc07c76cb |
| Moonrail Studios | Kestrel Group (its parent) | one offer, one row | frederick.stone@harmonygames.co/1842077918822811962, 5373edb55ca853d6052ecce5 |
| Sunfold Mobile | the card 'F/up with Lena' | one publisher, named for its contact | f_8ddfb9901891eb8e9dcab8, 68d598387dea3e7fe85e3a0a |
| Oakline Games | the card 'F/up with Marek' | one publisher, named for its contact | f_27cac0eed300cc33eeb4fd, 68d5913004a98be3b4c45408 |
| Summit Mobile | its noreply@ sender | the partnerships@ address is the contact | frederick.stone@harmonygames.co/1842077918822746195 |

## 11 · Pre-submit checklist

- [ ] Persona voice: an ordinary request from Frederick to his assistant; clean spelling; no spec-sheet layout
- [ ] Names Leonard's email from yesterday (A1) as the source of the job, not its rules
- [ ] Names my DD publishing folder (A3) for the model and asks for the reply to Leonard on his email (R13)
- [ ] No publisher name, status, count, date, amount, rule, id or tool name (§9)
- [ ] No hint, riddle, hedge, if-chain or audit-form wording; no fundraising or investor framing
- [ ] Every deliverable in §4 is reachable from the prompt or Leonard's email
- [ ] hardness_v2_check RULE_IN_PROMPT clean; word count 20–4,000

## 12 · Blockers and routed defects

- No blocker. Blind sweeps ran before this stage; every fork and coherence finding they raised was settled in records (dossier 'Blind sweeps'; plan/sweep/).
- Rev1 passed /injection and failed /prompt on one fork (`run_forensics/rev1/platform_prompt_review.md`): whether the organic-figure notes were part of this job. Rev2 settles it in the rule doc's last line (f_5e355d03f6eb6a4e866ead), so /injection, /prompt and /hardness must run again.
- For the pre-check to prove: the calendar description route on evt_43fda04cd11b9d58a05161, and card and checklist writes on the UA/BD board.
- Unverified: none load-bearing.

## 13 · Self-review

Re-read as Eval 1 Phases 1–3 against this brief (brief mode). Load-bearing values were re-read from the rev1 SQL or through `tools/hg.py` in this run (§5a outputs, dossier check-sql). Three blind passes matched the solver on every value; the last found 0 forks.

| Area | Counter-reading (strongest argument it fails) | Evidence that resolves it | Verdict |
|---|---|---|---|
| Fair readings | Oakline's Q4 cash could be $20,000, because a resend is only a promise | C07C2866011/1759251900.005166: 'so it'll land in October'; the rule doc counts money that lands Oct 1 to Dec 31 | settled in a record |
| Fair readings | phone changes aren't 'in writing', so Tallwater and Sunfold keep their term-sheet terms, which flips the pick to Sunfold | 'in writing' tests Live; f_5e355d03f6eb6a4e866ead says 'Use the latest terms we have from them, wherever they are, calls included' | settled in a record |
| Fair readings | the Sep 24 lead could be a sheet publisher such as Kitebridge | frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com>: 'never made it onto your sheet' | settled in a record |
| Clarity | reminders could be one per date; notes could live in a Doc | f_5e355d03f6eb6a4e866ead: 'One for each Live offer'; C096HFA5Z8W/1758915000.867092: 'left in your Gmail drafts' | settled in a record |
| Clarity | 'reply here' could read as a new mail or a send of the drafts | frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> says reply here; 68dab660c900179df4f5f92d and C096HFA5Z8W/1758915000.867092 keep the drafts unsent | settled in a record |
| Incorporation | the organic note is graded, but no prompt word asks for it, and a line saying it 'still applies' could be a limit on content (rev1 /prompt fork) | f_5e355d03f6eb6a4e866ead's last line now says the notes aren't done and to do them as part of this; the hub points at that doc; C096HFA5Z8W/1758915000.867092 states who and what | incorporated |
| Incorporation | the hub could be read as handing over an answer | frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com>, f_5e355d03f6eb6a4e866ead and 68dab660c900179df4f5f92d state rules and asks, no publisher or value | instructions, not answers |
| Truthfulness | a prompt premise like 'Leonard emailed yesterday' could be off | frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> is Tue Sep 30 23:10Z = 4:10 PM PT, the day before Wed Oct 1 (§7) | holds |
| Feasibility / ACL | a deciding record could sit outside Frederick's view | check-sql PASS (dossier 1.E); §5a finds every fact as frederick_stone; Linear, Trello, Contacts and Snowflake are unscoped | holds |
| Feasibility / ACL | a sheet with two tabs, drafts and checklists may not be writable | catalog has gsheets_create_spreadsheet, gsheets_values_update, gmail_create_draft, trello_create_checklist and trello_create_check_item; the UA/BD board write is for the pre-check to prove | holds; pre-check |
| Contrived register | naming the folder and the card could read as a spec sheet or a hint | both are destinations the persona knows from his own folder and Leonard's mail; no rule, publisher or trap is named | ordinary request |

Unresolved: thread form of the drafts and the reminders' time of day stay open by design (accepted both ways in §4b). No independent red team ran (REDTEAM_* unset).

```
STAGE GATE prompt-writing: PASS — Task_Authoring/task_inputs · 04_Prompt_Writing_Brief.md#09c020e06d02 · 00_Assigments.md#b715c1dcdbe1 · 01_Grounding_Dossier.md#9c0a597a75ac · 01_Universe_Inject.sql#f6eb3512dffa · 03_Error_Async_Config.txt#250fd0e10e4f · __context__#ec895c36b5f1 · __assignment__#a95625679300 · __policy__#dc4ab5df3cdd · __gate_policy__#f8638415ca2c · __review__#e2ef4af6e1cb · blocking 0 · warnings 0 · checks 24
[PASS] assignment.v3_context: Frederick Stone / Co-founder; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Writing_Brief.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql, 03_Error_Async_Config.txt)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#f6eb3512dffa, 01_Hardness_Manifest.json#550c4fbf3aad, 01_Grounding_Dossier.md#9c0a597a75ac, solver/solver.py#92f94f353626, 01c_Dispositions.json#c3c88b75e591, 01c_Preflight_Report.json#85aeea3b5432, 00_Assigments.md#b715c1dcdbe1, 01_Scenario_Design.md#e6f4b48f11e9, 01_Hardness_Manifest.draft.json#70c5ac3229a5, 01_Gradable_Surface.json#7e68f34657e8, __context__#ec895c36b5f1, __assignment__#a95625679300, __policy__#dc4ab5df3cdd, __gate_policy__#f8638415ca2c, __review__#938b3fc22f77)
[PASS] chain.error-async: upstream 'error-async' PASS pasted and current (03_Error_Async_Config.txt#250fd0e10e4f, 00_Assigments.md#b715c1dcdbe1, 01_Grounding_Dossier.md#9c0a597a75ac, 01_Universe_Inject.sql#f6eb3512dffa, __context__#ec895c36b5f1, __assignment__#a95625679300, __policy__#dc4ab5df3cdd, __gate_policy__#f8638415ca2c, __review__#938b3fc22f77)
[PASS] structure.sections: 14 required sections present and non-empty (04_Prompt_Writing_Brief.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Writing_Brief.md
[PASS] evidence.situation: 1/1 items carry a source pointer (min 100%)
[PASS] evidence.final_state: 44/44 items carry a source pointer (min 100%)
[PASS] evidence.discovery_map: 70/70 items carry a source pointer (min 100%)
[PASS] evidence.dates: 11/11 items carry a source pointer (min 100%)
[PASS] evidence.entity_traps: 10/10 items carry a source pointer (min 100%)
[PASS] tool.search_as_persona: 70 facts proven findable by persona_view search as frederick_stone
[PASS] reach.brief: 64 scoped load-bearing ids YES for frederick_stone
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] structure.accepted_outcomes: V3 accepts multiple fair outcomes; see v3.fair_outcomes_review
[PASS] boundary.anchor_naming: 3 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 9 evidenced counter-readings (of 11 found; need ≥ 6) in 04_Prompt_Writing_Brief.md
[PASS] review.coverage: self-review addresses all 6 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.fair_outcomes_review: current accepted outcomes and considered alternatives recorded; multiple fair outcomes are allowed
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

