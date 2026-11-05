## OE EVALUATION REPORT

### Task: Frederick works through Leonard's vendor and partner backlog (36 companies): Q4 commitments log, written answers, ESG intake emails, signing cards, contacts, January reminders, reply to Leonard
### Persona: Frederick Stone - Co-founder (frederick.stone@harmonygames.co, Executive)

**Scope.** Chat review of attempt 6ae9909f707bc2aa0a7ed6e9, `/oe` (audit), review date 2026-11-04, universe `Universe_SynthCut` (hg4-synth-sep30cut v16, `Evals/references/universes/synthcut/universe_manifest.json`), clock 2025-10-01 00:00 PT. Spec `Evals/2_Oracle_Events_Eval.md`, policy oracle-events-v2.

| Input | Saved path | SHA-256 |
|---|---|---|
| Oracle Events (147 OEs) | Evals/task_inputs/08_Oracle_Events.md | c010b7dfbf6d12dbae59611e2eb63104ab2200605bc6b3109a217ad7eb81426f |
| Prompt | Evals/task_inputs/04_Prompt.txt | 32f7ab0cabd613da0dc4797a9d2f82afcb5b4ed76db1255d507261f98b225dac |
| Task details | Evals/task_inputs/00_Task_Assigned_Inputs.md | 7460cb5f1b4e282b0aa7812786d42e7ee12c342709a2aea0c26d89088e7f0077 |
| Injection SQL (rev 8) | Evals/task_inputs/01_Universe_Inject.sql | 69603ab4b6a4ee6c926c1d8a4ab6ba396ca531f321e877e6c06797d0e2304e6b |
| Task date | Evals/task_inputs/02_Universe_Date.txt | 189e2ac63a6fea6f90c0c9ab3dbfb06e0fc8ed7269f82b0d75af728e3b21da5c |

**Input and authority issues.** None. There are no prompt reference files and no error/async configuration. The SQL was read as a static overlay (parsed, never executed). Evidence: 258 INSERT and 36 UPDATE rows, plus base records (the Balancy thread, Nintendo notices, excluded look-alike threads, Slack thread parents, the Trello board and lists, the Linear user, contacts.json). Every check below is NEW in this review; no fact was reused from an earlier report.

**Checklist.** Every item was done; per-step, per-field results are in the saved record.
- Intake
- Docs and catalog
- Deep exploration of every record and the overlay
- Persona ACL binding
- Critical path derived independently
- Segments
- Five-field check
- Non-action/final-response scan
- Tool, service and parameter verification
- Numeric observability
- Expected-data ledger: 600 values and 17 absence claims, all ledgered
- Dates against the clock
- Act-vs-defer
- Format
- Completeness, dependencies and writes
- Prohibited actions
- Injected errors: none configured
- Path feasibility
- Outcome mapping
- Pre-verdict sweep
- Scoring
- Readability
- Record save
- Deep recheck

### Phase 1: Structure & Alignment
- **Derived critical path (from the prompt, independent of the OEs).**
  1. Find and read Leonard's Sep 30 email.
  2. Read the instruction sources it points to:
     - the runway guardrails doc;
     - Leonard's Monday #executives change;
     - ESG's signing note and Leonard's reply, which gives the founders' board To Do list and the intake checklist;
     - the README in the Q4 commitments folder;
     - Arthur's keep-running card, named in guardrails step 3.
  3. Find the January review date.
  4. Inventory the backlog: the paperwork folder plus engaged companies with no paper, excluding the named and cold look-alikes.
  5. Decide each company by first fit.
  6. Writes:
     - log sheet: create, header, 36 rows, move into the folder;
     - written answers to everyone waiting, including the Paylane cancellation and none for the four already-answered companies or the Nintendo portal;
     - one ESG intake email per agreement ESG must see;
     - one card per Sign company;
     - contacts (no duplicates, none for portals or no-reply senders);
     - one Jan 5, 2026 reminder per company that comes back at the review;
     - reply to Leonard.
- **Segments.** 147 STEP, 0 CONTEXT, 0 RESPONSE_DESCRIPTION, 0 NON_ACTION.

### Phase 2: Accuracy
| Step(s) | Field | Result | Evidence |
|---|---|---|---|
| 1 | all | VERIFIED | SQL Gmail row `…CAlIXcq3…` (Frederick's inbox): subject "Vendor and partner stuff while I'm in LA", 2025-09-30T23:20:00Z = Tue 4:20 PM PDT, to Frederick only; every quote matches |
| 2-6 | all | VERIFIED | Guardrails doc f_b98287… (created 16:00Z = 9:00 AM PDT, shared with Frederick); Slack C07C2866011 (#executives, Frederick a member) 17:15Z = 10:15 AM PDT; ESG note 20:05Z = 1:05 PM PDT, to Leonard, cc Frederick, Robert, Arthur; Leonard's reply 16:30Z = 9:30 AM PDT; checklist six items; contact "ESG Law intake" PERSON_2599_EMAIL |
| 7-12 | all | VERIFIED | Folder d_80a8… (created 20:00Z = Mon 1:00 PM PDT, owner Frederick, shared with Leonard); README and template header; Harmony Games board open lists To Do/Doing/Done/Backlog (Recruiting closed); keep-running card with 4 items; review event 2026-01-05T17:00Z = 9:00 AM PST |
| 13 | all | VERIFIED | 33 drive_files rows with parent d_ffa3…, names match the list |
| 14 | parameters | **MINOR** | "Jun 1 to Sep 30 2025" has no source (see Issue 1) |
| 14 | expected_data | **MINOR** | Rayking: "Frederick's reply went to Leonard only", but the record is an unsent draft (Issue 2). Every other value matches: Hootline Aug 5/12; Balancy subject; Nintendo notices Thu Sep 4, "NDA Effective: 09/04/2025", "This is an automatically generated email. Please do not reply."; Playable Factory Sep 11/24; Gamesforum Sep 10 single message; InterCo 3 mails Aug 27–Sep 18; Singular subject; NCsoft Sep 25 and Dentsu Sep 23 quotes; Nova Rewards "I'm withdrawing this offer for now"; 36 total |
| 15-54 | all | VERIFIED | Every sender, token address, PT time and paper term matches its SQL row word for word. Balancy (base): 7 messages; 1:54 PM PDT; Leonard 5:21 PM PDT (Sep 12 00:21Z); "Absolutely, thank you for the update." Slack replies: Lanternfly 19:31Z = 12:31 PM PDT under "we have no localization though" (Wed Sep 17); Spotlight 18:41Z = 11:41 AM PDT; Framewell 21:02Z = 2:02 PM PDT under "Playtestcloud results are in" (Sun Sep 21 8:53 PM PDT). ZOM-567 comment by usr_cc3e90160f490686 = arthur.blake@ |
| 55-147 | all | VERIFIED | Writes:<br>- sheet: gsheets_create_spreadsheet, values_update, gdrive_move_file;<br>- 31 replies plus the Paylane cancellation, each addressed to the thread's sender token;<br>- 3 ESG intake emails to PERSON_2599_EMAIL;<br>- 7 cards on To Do list 640643a3fd8f3ca308d93195;<br>- 32 contact adds (3 already exist, the other 32 are absent from base contacts.json and the SQL; complete scan);<br>- 14 events on Mon Jan 5, 2026;<br>- reply to leonard.hayes@harmonygames.co |

Numeric observability: every figure is a literal in a record (amounts, dates) or a UTC-to-Pacific rendering recorded in the ledger. No hidden calculation. Act-vs-defer: Robert's "honestly we should just cancel every marketing tool" is an opinion, not a decision, and no record defers any write. The July "under $500" rule is superseded by Leonard's Sep 25 "This replaces what I said in July", as OE 4 notes. Every timestamp is before the 2025-10-01 07:00Z clock, and the Jan 5 review is a future event.

### Format & Standardization
No shape defects. Every OE is numbered, has one action, names its service and has an Expected: line. OEs that read a thread and its paper pair two reads, not a read with a write.

### Phase 3: Completeness
| Requirement | Covered by | Result |
|---|---|---|
| Read Leonard's email | OE 1 | COVERED |
| Guardrails, Monday change, ESG note and reply, checklist, keep-running list | OE 2-6, 11 (applied in 31-41) | COVERED |
| Inventory the whole backlog, excluding look-alikes | OE 13-14 | COVERED (matches the blind O3 inventory of 36) |
| Decide each of the 36 companies | OE 15-54 | COVERED |
| Log sheet in the Q4 commitments folder per README | OE 7-9, 55-57 | COVERED |
| Written answers, including the Paylane cancellation; none for Answered/portal | OE 58-89 | COVERED |
| ESG intake emails (Kinetic Arcade, Lumencloud, Bundlehouse) | OE 5-6, 90-92 | COVERED |
| Signing cards on the Harmony Games board To Do list (7) | OE 10, 93-99 | COVERED |
| Contacts (32 new, 3 existing, none for Nintendo/Paylane) | OE 100-132 | COVERED |
| January reminders (12 Park + Balancy + Lanternfly) | OE 12, 133-146 | COVERED |
| Reply to Leonard (Keep 3, Sign 7) | OE 147 | COVERED |

- **Path feasibility:** SUPPORTED. Task solvability: SUPPORTED_BY_OE. Prompt follow-up: NONE.
  - Every read is in Frederick's mailbox or calendar, a Drive file he owns or that is shared with him, a Slack channel or DM he belongs to, or unscoped Trello, Linear or Contacts.
  - Every write has a cataloged completing tool.
- **Outcome-first mapping:** every step maps to OUTCOME, either through the end-state artifact (mail, sheet, card, contact, event) or through the log row or answer a read decides. No Process criterion is needed.

### Issues Found
| # | Step | Issue | Component | Effect |
|---|---|---|---|---|
| 1 | OE 14 | **Unsourced search window.** "Go through Frederick's Gmail inbox from Jun 1 to Sep 30 2025": neither the prompt nor Leonard's email sets a start date. The window silently skips an engaged pre-June offer, Appodeal's publishing program (base thread `frederick@…_1830012626042968381`). Frederick replied Apr 29 and May 14, and Appodeal's last mail (Tue May 20, 10:33 PM PDT) says "Just checking in to see if you’ve had a chance to consider our proposal". The offer is ad-monetization/UA ("ROAS-focused testing *with ad monetization", "parallel UA"), so Leonard's "the ad networks ... stay off it" keeps it off the log. | Accuracy (Minor) | NON-FAIL 3: the outcome is unchanged, but the step leaves out an engaged company without a reason |
| 2 | OE 14 | **Wrong qualifier.** "Rayking Game (…; Frederick's reply went to Leonard only)": Frederick's Sep 4 message in that thread is an unsent draft (`X-Gmail-Labels: Opened,Drafts`, no SENT label, base `frederick@…_1842348778705877030`). It never went to anyone. Rayking stays off either way ("Cold pitches nobody answered, including ones we only forwarded around internally"). | Accuracy (Minor) | NON-FAIL 3: the outcome is unchanged |

### Recommended Fixes
1. **OE 14, first line.** Replace it with: "Find every other outside company in Frederick's Gmail with an offer, a trial, a quote, terms or an ask that one of us engaged with (scope from OE 1). Search the whole inbox up to Sep 30, 2025, and read the threads that look like one."
   Then add this sentence to its Expected line, after the Rayking item: "Appodeal's publishing program also stays off: Frederick replied on Apr 29 and May 14 and their last mail asks him to 'consider our proposal', but it is ad-monetization/UA ('ROAS-focused testing with ad monetization'), so it falls under the ad networks that stay on the UA budget call."
   (Values checked: base thread `…1830012626042968381`, messages of Apr 29 and May 14, 2025 from Frederick; May 20 nudge; OE 1's ad-network exclusion.)
2. **OE 14, Rayking clause.** Replace "Frederick's reply went to Leonard only" with: "Frederick's reply is an unsent draft addressed to Leonard (Gmail labels 'Opened,Drafts'), so nobody ever answered Rayking". Keep the rest of the Expected line as it is.

Neither fix changes any other OE. After editing, send `/oe` again. `/rubric` also reads the OEs, so rerun it after `/oe`.

### Readability (advice only, no score impact)
- The set already reads well. Each per-company OE states the goal, quotes the deciding words and names the trap: Paylane overriding the pilot's Jan 15, Pingwise as the "night pager", Leonard's Framewell hold, Robert's Spotlight answer, Lanternfly's phone answer.
- OE 56 mentions only Kinetic Arcade's "with our lawyers first", although Lumencloud and Bundlehouse rows say the same. Naming all three would make the row check easier.
- The templated write OEs (59-146) are fine as they are; one line each is enough.

## Deep Recheck

Passes: O1, O2, O3, Opus 5.5 (claude-opus-5-5), each blind to the main review. O3 was not given the OE file. The passes started while the record was being assembled. They never saw it, and their confirmed findings are in the saved record.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| O1 | 147 OEs | 2 | 1 |
| O2 | 147 OEs | 2 | 1 |
| O3 | 7 open instructions, 37 items | 0 mismatches | n/a |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | O1 | "Frederick's reply went to Leonard only" (OE 14) | gmail threads/frederick@harmonygames.co_1842348778705877030.json /messages/0/headers/1/value "Opened,Drafts" | Accuracy: stay-off list | Minor OE inaccuracy | CONFIRMED | Header and labels (no SENT) show an unsent draft; harmless because Rayking stays off either way. Recorded as OE14 expected_data MINOR and a MINOR ledger entry |
| DR2 | O1 | "two no-reply Nintendo Developer Portal notices to Frederick" (OE 14) | …_1842359398719557772.json body "user Email: frederick.stone@harmonygames.co" | Accuracy: recipient | Minor OE inaccuracy | REJECTED | The To header is blank, but the notices sit in Frederick's inbox and name him as the account user, so "to Frederick" is accurate |
| DR3 | O2 | "Go through Frederick's Gmail inbox from Jun 1 to Sep 30 2025" (OE 14) | …_1830012626042968381.json /messages/0/body "Just checking in to see if you’ve had a chance to consider our proposal" | Completeness: discovery | Minor OE inaccuracy | CONFIRMED | The window has no source and drops this engaged offer without a reason; Appodeal is ad-monetization/UA, so it stays off under Leonard's ad-network exclusion and the outcome is unchanged. Recorded as OE14 parameters MINOR, not a missing step |
| DR4 | O2 | "Stay off the log: Rayking Game … Nova Rewards" (OE 14) | …_1833464394449700499.json "adjoe is covering your travel expenses"; Frederick Jun 21 "I won't be able to make it"; event "August 6–8, 2025" | Completeness: discovery | Missing step | REJECTED | AppCamp is an adjoe (ad network, UA spend doc "Adjoe for now") event that is already past and that Frederick already declined; it is out of scope, and the exclusion list need not name every look-alike |

Effect on verdict: Accuracy goes from 5 to 3 (two MINOR items in OE 14); Completeness stays 5. Overall NON-FAIL 3.

O3 inventory (built without the OEs). Every group matches the OE set:
- G1: Decide every company in Leonard's scope | Leonard's email, guardrails, Monday change, ESG note, keep-running card | 36 items (M1–M36: End 10, Keep 3, Sign 7, Park 12, Answered 4) | Covered by: OE 13–54
- G2: Log it all in a sheet | README, template "Log" tab | 36 rows (M1–M36) | Covered by: OE 7–9, 55–57
- G3: Written answer to everyone waiting | guardrails "Answers" | 31 answers plus the Paylane cancellation (M1–M19, M21–M32) | Covered by: OE 58–89
- G4: One ESG intake email per agreement | ESG note, checklist | 3 items (M14–M16) | Covered by: OE 90–92
- G5: Cards for anything that needs signing | Leonard's Sep 25 reply, prompt | 7 items (M14–M20) | Covered by: OE 93–99
- G6: Each company's contact into Contacts | README contacts rule | 32 new (M1–M36 less Noor, Aiden, Leah, Nintendo) | Covered by: OE 100–132
- G7: A reminder for each company that comes back at the January review | guardrails steps 1 and 5, review event | 14 items (M21–M33, M36) | Covered by: OE 133–146
- G8: Reply to Leonard | Leonard's email | 1 item (M37) | Covered by: OE 147

Scope: none. The 36-company instruction is fully named by Leonard's email and the paperwork folder; O3 flagged the Pixel Harbor "I'll come back to you" reading as a possible fork. That is settled for `/prompt` (a holding reply, not an answer), and OE 23 already says so.

Platform defects: none.

### FINAL VERDICT: NON-FAIL
Score: 3
Execution status: COMPLETE
Completeness score: 5
Accuracy score: 3
Path feasibility: SUPPORTED
Task solvability: SUPPORTED_BY_OE
Prompt follow-up: NONE
Review policy: oracle-events-v2
Reviewed OE SHA-256: c010b7dfbf6d12dbae59611e2eb63104ab2200605bc6b3109a217ad7eb81426f
Review context SHA-256: 6e48778ea4881c5abc8d3c277d5773ccb6fe3065263b6cfd70ec211d2effe7d3
OE record SHA-256: 47883fcc2acb26c6e109990056aade01533de2583a30505babc65945e5fe201c
Eval version: task-quality-v1
Eval release SHA-256: a6d0d5849af43fa85dc1c2d9bf598b27771ddcb6c23e39cc14c4eba835fe3225
Evaluator model: Opus 5.5 (claude-opus-5-5)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Next action: Fix the two OE 14 items (the unsourced Jun 1 window, with Appodeal named as an ad-network exclusion, and the Rayking draft wording), then send /oe again; /oe needs a PASS. Rerun /rubric afterwards because it reads the OEs.
Evidence limits: Static universe, SQL overlay and catalog evidence; no live writes executed. Absence receipts for contacts, vendor names and folder IDs are saved under Evals/.cache/oe_receipts/.
