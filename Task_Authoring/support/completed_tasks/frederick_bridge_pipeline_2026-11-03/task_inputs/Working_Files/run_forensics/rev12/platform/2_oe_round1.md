# Oracle Events Review (Eval 2)

## OE EVALUATION REPORT

### Task: Fred takes over Leonard's Q4 investor-update send list for the bridge round. He builds the send list as a Sheet in his Q4 2025 investor update folder, does what Leonard's two comments on the Existing Investor Update card ask (group checklists, F/up cards in To Do, a comment on the existing Anel card), and replies on Leonard's thread with the counts per group.
### Persona: Frederick Stone - Co-founder

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Inputs reviewed: OEs (saved `oe`, 86 events), prompt, assignment, injection SQL (167,306 bytes, read as a static overlay and never executed). Base data came from Universe_SynthCut: Frederick's Gmail thread files, Slack (#bridge-pitch, #executives, #zombie-match3d, IM D05S58U4SAK), his calendar, Trello, Linear and Contacts, plus the tool catalog and acl.md.

### Phase 1: Structure & Alignment
- Derived critical path (built from the prompt and the instructions it pulls in, before reading the OEs):
  1. Read Leonard's Sep 30 email.
  2. Read the Q4 send-list doc rules, the draft deck and the #executives "signed" note.
  3. Read the 2025 investor list (80 named rows, 77 names) with its Latest Status notes.
  4. Read Fred's calendar from Sep 3 to Sep 30.
  5. Read bridge outreach in #bridge-pitch and Gmail.
  6. Read the passes (direct, relayed to Griffin, program decision), the angels (pledge, reduction, DocuSign, back-out), and the off-list firms with calls (Brightwater, Homa).
  7. Settle build access from ZOM-567, overridden by Arthur's Sep 30 Slack note.
  8. Decide the groups.
  9. Find the README rule; create "Q4 update - send list" as a Sheet, move it into the folder and write its rows.
  10. Read both card comments; create four checklists with 25 items.
  11. Check To Do and Fred's calendar after Sep 30; create 18 F/up cards and comment on the existing Anel card.
  12. Reply on Leonard's thread with firm and angel counts.
- Segments: 86 STEP, 0 CONTEXT, 0 RESPONSE_DESCRIPTION, 0 NON_ACTION.
- Persona ACL: every read is in Frederick's mailbox or calendar, a Slack channel or IM he belongs to, a Drive file shared with him, or an unscoped service (Trello, Linear, Contacts).

### Phase 2: Accuracy
| Step | Field | Result | Evidence |
|---|---|---|---|
| OE 1 | all | VERIFIED | SQL L138: sent 2025-09-30T21:05Z (2:05 PM PT), to Frederick, cc Robert and Arthur; every quoted ask matches |
| OE 2 | all | VERIFIED | SQL L23 (doc created 2025-09-26T18:00Z, shared with Fred): every quoted rule matches; the Q3 doc (L21) is the July decoy |
| OE 3 | all | VERIFIED | SQL L70 and L76: both slide texts match |
| OE 4 | all | VERIFIED | SQL L87: #executives, 18:35Z = Fri Sep 26 11:35 AM PT; quote matches |
| OE 5 | all | VERIFIED | SQL L31 grid: 80 named rows, 77 distinct (Progression Fund, BITKRAFT Ventures, Acterra twice); every quoted Latest Status cell matches |
| OE 6 | expected data | MINOR (deep recheck) | The "rest" sentence leaves out the recurring internal series on Fred's calendar ("All Hands", weekly Fridays). Otherwise everything is VERIFIED:  gcal events on Fred's calendar at the stated PT times (LVP Sep 9 9:30, NCsoft Sep 10, SciPlay Sep 15 1:30 PM, Homa Sep 18 8:00, speedrun Sep 18 10:40, NCsoft Sep 19, T-accelerate Sep 22, Dentsu Sep 23 5:30 PM); injected Hiro Sep 23 and Brightwater Sep 25; GFR Sep 29 cancelled, Sep 30 10:30 confirmed |
| OE 7 | expected data | MINOR | #bridge-pitch Sep 8 08:25 post: the "not top priority" section also holds "Index (it was too early for them and wanted to see KPIs)", which is not a plan. Acterra and Galaxy sit under "*Other VCs may be relevant + Family Funds --> No further update*", and Galaxy is a lost contact. Every other quoted post matches. No group changes. |
| OE 8 | expected data | MINOR | Two threads are credited to the wrong firm (see Issues). Makers and BITKRAFT are correct, each thread has only Leonard's message, and the 48-name absence holds (search receipt over all 4,656 of Fred's threads). |
| OE 9 | all | VERIFIED | GRx Sep 8 6:41 AM PT; Lakestar 05:46Z = Sep 3 10:46 PM PT; 1AM forward Sep 8; no call since Sep 3 for any of them (GRx's only call is Feb 11 2025) |
| OE 10–12 | all | VERIFIED | SQL L83 (reply_count 0), L102/104/106 (IM), L158 (only DocuSign notice in Fred's mailbox; base has none), L162 nudge 15:00Z = 8:00 AM PT |
| OE 13–17 | all | VERIFIED | SciPlay thread quotes; Robert's Sep 30 16:06Z reply under the Sep 29 18:38 PT parent; LVP Sep 25 7:13 AM PT; Edith 09:40Z = 2:40 AM PT; contact "Partner, Hiro Capital" with PERSON_9903_EMAIL as a guest on the Sep 23 call |
| OE 18–25 | all | VERIFIED | Brightwater, Homa, GFR (moved to Sep 30, follow-up 6:41 PM PT), a16z ("Will review" 8:09 PM PT; program decision forwarded 8:21 PM PT), NCsoft (Anel's Thu request, Calendly sent, nothing booked), T-accelerate (Karthic; contact "T-Accelerate Capital (PXLite fund)"), Dentsu (6:52 PM PT; Oct 1 1:30 PM) |
| OE 26–27 | all | VERIFIED | ZOM-567 has four Arthur comments on Sep 30 with the quoted text; Arthur's 23:20Z note and Leonard's 23:48Z reply in #zombie-match3d (Fred is a member) |
| OE 28 | expected data | MINOR (deep recheck) | "nothing from us since Sep 3" isn't literally true for Mattel ("told Mattel we're passing on the Barbie RFP", which is RFP-only) or Index (an earlier-round answer); both still stay off and 48 holds. Otherwise everything is VERIFIED:  Doc rules applied to the records give 1 / 7 / 14 / 3 = 25; build access T-accelerate, NCsoft, Brightwater and Dentsu iOS only; GFR, a16z and Homa none |
| OE 29–32 | all | VERIFIED | Folder owned by Fred (L12); README naming and format rule (L25); gsheets_create_spreadsheet, gdrive_move_file and gsheets_values_update exist; rows match the doc's Sheet section |
| OE 33–36 | all | VERIFIED | Comments L113 (Sep 13 9:20 PM PT) and L115 (Sep 29 3:10 PM PT); no checklists on the card; open To Do cards are Playable Kickoff and the Anel card (Sep 16); after Sep 30 the only investor meetings are Dentsu Oct 1 and Michael Cheung (Makers partner) Oct 8; 21 − 3 = 18 cards |
| OE 37–86 | all | VERIFIED | Each checklist, item, card, comment and the reply maps to a cataloged Trello or Gmail write; 25 items, 18 cards, counts 0/1, 7/0, 14/0, 3/0; reply to leonard.hayes@harmonygames.co (reply-all adds Robert and Arthur) |

Numeric observability: Anton's 25,000 comes from "he can only do 25 this time, not the 40" (the $40K pledge), so 25 means 25,000. Every count was recounted from the records.

Date/time: every event the OEs treat as done is dated before 2025-10-01 07:00 UTC. The Oct 1, Oct 6, Oct 8, Oct 14 and Jan 14 events are presented as future.

Act-vs-defer: none of the writes depends on a proposed resolution. The decoys (Robert's "send it to everyone" mail and Arthur's "just use who Leonard emailed" post) are overridden by Leonard's "Let's not, only the people the doc says."

### Format & Standardization
No shape defects. Every OE is numbered and has one action. Each one names its service, or for OEs 28, 36 and 85 the earlier steps it reasons over, and has an Expected: line.

### Phase 3: Completeness
| Requirement | Covered by | Result |
|---|---|---|
| Read Leonard's email | OE 1 | COVERED |
| Doc rules, deck, signed note | OE 2, 3, 4, 12 | COVERED |
| List population and Latest Status | OE 5 | COVERED |
| Calls on Fred's calendar since Sep 3 | OE 6 | COVERED |
| Bridge outreach (Slack and mail) | OE 7, 8 | COVERED |
| Passes, relayed nos, program decision | OE 7, 9, 13–17, 21 | COVERED |
| Angels (pledge, reduction, signed, back-out) | OE 10–12 | COVERED |
| Off-list and on-list firms with calls | OE 18–20, 22–25 | COVERED |
| Build access (log plus later correction) | OE 26, 27 | COVERED |
| Group decision | OE 28 | COVERED |
| README, Sheet, folder, rows | OE 29–32 | COVERED |
| Card instructions | OE 33 | COVERED |
| Keep warm checklist and items | OE 37–40 | COVERED |
| New investor / In talks / Awaiting reply checklists and items | OE 41–65 | COVERED |
| F/up cards with exemptions | OE 34–36, 66–83 | COVERED |
| Comment on the existing card | OE 34, 84 | COVERED |
| Counts and reply on the thread | OE 85, 86 | COVERED |
- Path feasibility: SUPPORTED. Task solvability: SUPPORTED_BY_OE.
- Outcome-first mapping: every write (sheet, folder placement, checklist items, cards, comment, reply) is an Outcome. Reads are verified through the outcomes they feed. No Process row is needed.

### Issues Found
| # | Step | Issue | Component | Effect |
|---|---|---|---|---|
| 1 | OE 8 | "Raine, Sep 3 2:17 PM PT" cites the "Leonard Hayes from SEMC onto the next adventure" thread, but that mail goes to PERSON_0616, whose signature in the thread reads "Managing Director, General Catalyst". Raine's own outreach is the Sep 3 2:13 PM PT thread "Intros: PERSON_3068_NAME, PERSON_0300_NAME, PERSON_2533_NAME ([PERSON_NAME_6608]) <> Leonard + [PERSON_NAME_0054] ([SOURCE_ORG_0001])", signed "*The Raine Group*". | Accuracy | MINOR: Raine is still Awaiting reply (Latest Status "Reached out - no response as of 09/11"), so no group changes. A rubric row built on this line would cite the wrong thread. |
| 2 | OE 8 | "Superplay, Sep 3 3:54 PM PT: the 'bridge round, quick chat?' outreach" — that mail goes to PERSON_2877_EMAIL, which the Sep 8 #bridge-pitch post names as Supercell's lead ("Supercell ([PERSON_NAME_25642] is the lead There - <mailto:PERSON_2877_EMAIL\|PERSON_2877_EMAIL>)"). Fred's mailbox has no outreach to Superplay since Sep 3. | Accuracy | MINOR: Superplay is Awaiting reply from its Latest Status note alone, and Supercell stays off (not on the list, no call). |
| 3 | OE 6 | The "rest are dry runs, POD meetings, 'SciPlay prep' and the SVB catch-up" list leaves out the recurring internal meetings on Fred's calendar. | Accuracy | MINOR: no investor call is missing. |
| 4 | OE 28 | The 48 off-list names are described as having "nothing from us since Sep 3", but Mattel had RFP contact after Sep 3 (#bridge-pitch Sep 26: "told Mattel we're passing on the Barbie RFP. since the kickoff that's only been an RFP conversation, we haven't pitched them the bridge"), and Index's Sep 8 line is an earlier-round answer. | Accuracy | MINOR: both are still off under the doc ("Only outreach about the bridge counts"; answers from earlier rounds don't count). |
| 5 | OE 7 | The Sep 8 description says the "not top priority" part "lists only plans … and Transcend, Moon Fire, 20VCs, Acterra and Galaxy". That section also holds the past answer "Index (it was too early for them and wanted to see KPIs)", and Acterra and Galaxy sit in the next section, Galaxy as a lost contact. | Accuracy | MINOR: every name involved stays off. |

### Recommended Fixes
1. OE 8, replace with:
   "OE 8  Check whether we wrote to the list names that #bridge-pitch doesn't settle. Search Frederick's Gmail from Sep 3 to Sep 30 2025 for outreach to each of them and read the threads found: "Intro: Makers / [SOURCE_ORG_0001]", the Raine thread "Intros: PERSON_3068_NAME, PERSON_0300_NAME, PERSON_2533_NAME ([PERSON_NAME_6608]) <> Leonard + [PERSON_NAME_0054] ([SOURCE_ORG_0001])" and the Sep 22 "[SOURCE_ORG_0001] Intro".
   Expected: Makers, Wed Sep 3 1:57 PM PT: "we are kicking off a $2.5M bridge this week". Raine, Wed Sep 3 2:13 PM PT, signed "*The Raine Group*": "kicking off a $2.5M bridge this week". BITKRAFT, Mon Sep 22 11:07 AM PT: "It was nice meeting you over linkedin." Each thread has only Leonard's message: no reply, no call, no no. Trap: "Leonard Hayes from SEMC onto the next adventure" (Sep 3 2:17 PM PT) goes to General Catalyst's former managing director, not Raine, and "[SOURCE_ORG_0001] bridge round, quick chat?" (Sep 3 3:54 PM PT) goes to Supercell's lead, not Superplay. Superplay has no outreach mail; its Latest Status note "Reached out - no response as of 09/11" is the outreach. For the other 48 list names there is no bridge mail from us since Sep 3."
2. OE 7, replace the Sep 8 clause with: "its 'not top priority' part lists plans such as 'Early Bird (Matthew can intro)', 'Moon Fire (Matthew can intro)' and 'Transcend - [PERSON_NAME_2322] (maybe talk to him to get it out of the way lol)', plus the old answer 'Index (it was too early for them and wanted to see KPIs)'. Acterra and Galaxy sit under 'Other VCs may be relevant + Family Funds', Acterra as a plan and Galaxy as a lost contact ('[PERSON_NAME_3050] left the company so we lost our contact There')."

3. OE 6, replace the last sentence with: "The rest are dry runs, POD meetings, "SciPlay prep", the SVB catch-up (a bank, which the doc excludes) and recurring internal meetings; none of these is an investor call."
4. OE 28, replace the last clause with: "and the 48 list names with no bridge outreach from us since Sep 3 (OE 5, OE 7, OE 8). Mattel's only contact since the kickoff was the RFP ("since the kickoff that's only been an RFP conversation, we haven't pitched them the bridge"). Index Ventures has only an earlier-round answer. Transcend Fund and Acterra have only plans to reach out. The rest have nothing from us at all."

### Readability (advice only, no score impact)
- The set already reads goal-first, with the values written out and traps called out (OE 10, 26, 33). OE 37–83 are deliberately one write each; that's fine.
- Two decoys are worth naming as traps, though neither is a missing step. Arthur's Sep 29 #executives post, "for the Q4 send list I'd just use who Leonard emailed this month, the rest of that list is noise imo", is a scope suggestion the doc overrules. Leonard's Sep 29 #executives "waiting for the Turkish VC to show up" / "so this is gonna be a no" refers to a meeting that was only on Leonard's calendar and a guess, so it is neither a call nor a no.
- One trap worth naming in OE 7 or OE 28: the Sep 8 line "Sony ([PERSON_NAME_25644] - they are not investing in content right now according IH)" is IH's read, which the doc says "isn't the firm's answer". That is why Sony Mobile stays Awaiting reply.

## Deep Recheck

Passes: O1, O2, O3, run on Opus 5.5 (claude-opus-5-5) at session effort, each blind to the main review. O3 did not see the OEs.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| O1 | 86 events | 5 | 5 |
| O2 | about 32 requirements across 86 events | 4 | 0 |
| O3 | 85 inventory items | 1 mismatch | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | O1 | "Superplay, Sep 3 3:54 PM PT: the 'bridge round, quick chat?' outreach" (OE 8) | Fred's thread …1842285179768836773: to PERSON_2877_EMAIL, "would this be interesting for Supercell"; #bridge-pitch Sep 8: "Supercell ([PERSON_NAME_25642] is the lead There - …PERSON_2877_EMAIL…)" | Expected data | Firm attribution | CONFIRMED | Opened both records. Superplay is still Awaiting reply from its Latest Status note, so this is MINOR (Issue 2). |
| DR2 | O1 | "Raine, Sep 3 2:17 PM PT: 'we are kicking off a $2.5M bridge round this week'" (OE 8) | Thread …1842279098258817066 signature "Managing Director, General Catalyst"; Raine's thread …1842278858600251474, 2:13 PM PT, "*The Raine Group*" | Expected data | Firm attribution | CONFIRMED | Matches the main review. MINOR (Issue 1). |
| DR3 | O1 | "its 'not top priority' part lists only plans … Acterra and Galaxy" (OE 7) | #bridge-pitch Sep 8 08:25 post sections | Expected data | Qualifier | CONFIRMED | MINOR (Issue 5). |
| DR4 | O1 | "the 48 list names with nothing from us since Sep 3 (… Mattel, Index Ventures …)" (OE 28) | SQL L97: "told Mattel we're passing on the Barbie RFP …"; Sep 8 Index line | Expected data | Qualifier | CONFIRMED | Contact with Mattel after Sep 3 exists but is RFP-only, so the outcome holds. MINOR (Issue 4). |
| DR5 | O1 | "The rest are dry runs, POD meetings, 'SciPlay prep' and the SVB catch-up" (OE 6) | gcal: recurring "All Hands" (weekly Fridays), other internal series on Fred's calendar | Expected data | Incomplete list | CONFIRMED | MINOR (Issue 3). |
| DR6 | O2 | Sony Mobile Awaiting reply (OE 28) vs Sep 8 "Sony (… not investing in content right now according IH)" | #bridge-pitch Sep 8 08:25 post | Coverage | Missing step | REJECTED | OE 7 reads the whole channel, including this line, and OE 28 applies the doc's advisor-read rule correctly. This is not a missing read; the trap is noted under Readability. |
| DR7 | O2 | OE 6 calendar; Awaiting Turkish firms | #executives Sep 29 "waiting for the Turkish VC to show up" / "so this is gonna be a no"; event only on Leonard's calendar | Coverage | Missing step | REJECTED | OE 6 already establishes Fred's calendar, and the doc says "calls that never went on Fred's calendar don't". A guess is not the firm's no. No read is required for a correct path. |
| DR8 | O2 | "Andreessen Horowitz is In talks." (OE 21) | #executives Sep 30 8:23 PM PT paste of the same speedrun letter | Coverage | Missing step | REJECTED | OE 21 reads the same letter by mail and applies the doc's program-decision rule. The Slack copy adds nothing. |
| DR9 | O2 | OE 1 scope ("only the people the doc says") | SQL L84, Arthur in #executives: "I'd just use who Leonard emailed this month" | Coverage | Missing step | REJECTED | OE 1 (Leonard's instruction) and OE 2 (the doc) settle the scope, and the decoy doesn't change membership. Noted under Readability. |
| DR10 | O3 | M84: Oct 8 "Michael Cheung" call can't be tied to a firm, so 19 cards | SQL L31 list row 34: "Makers Fund", Partner "Michael Cheung" | Inventory | Count mismatch | REJECTED | The list ties Michael Cheung to Makers Fund, so Makers needs no card and 18 cards is correct (OE 35, OE 36). |

Effect on verdict: Accuracy stays 3. Two more harmless imprecisions were added (OE 6, OE 28). Completeness stays 5, since no missing step was confirmed. The record was re-saved and recomputed.

O3 inventory, by group:
- G1: Build the send list (groups, amounts, build access) | Q4 send-list doc / 2025 investor list / calls since Sep 3 | 81 items (M1, M4–M83: 77 list names and 4 off-list firms with calls, which yield 25 rows) | Covered by: OE 5–28, OE 29–32
- G2: One checklist per group, one item per firm or angel | Existing Investor Update card comments | 1 item (M2: 4 checklists, 1/7/14/3 = 25 items) | Covered by: OE 33, OE 37–65
- G3: F/up cards, or a comment where a card exists, none after a call past Sep 30 | Card comment of Sep 29 | 2 items (M71 NCsoft comment, M84 Makers exemption; M84 corrected as in DR10) | Covered by: OE 34–36, OE 66–84
- G4: Reply with counts per group | Leonard's Sep 30 email | 1 item (M3) | Covered by: OE 85, OE 86
- G5: Sep 29 Turkish VC check | #executives / Leonard's calendar | 1 item (M85), no write | Covered by: OE 6 (Fred's calendar has no such call)
Scope: none (the instructions cover the 77-name list, which the prompt and doc name explicitly; every group is covered).

Platform defects: none.

### FINAL VERDICT: NON-FAIL
Score: 3
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Execution status: COMPLETE
Completeness score: 5
Accuracy score: 3
Path feasibility: SUPPORTED
Task solvability: SUPPORTED_BY_OE
Prompt follow-up: NONE
Review policy: oracle-events-v2
Reviewed OE SHA-256: a52557b959967d838b472231c31d0fb853c39e74706cc1474a7dcebb8f6ba725
Review context SHA-256: 22cd6f35537e129e55d2f1777d9e090166616c2c0dc177297192f74e1a6e6136
OE record SHA-256: 34e16839fed19547375561c51831848f5455a50ef6152f772a32a3c3df3fe6db
Eval version: task-quality-v1
Eval release SHA-256: a6d0d5849af43fa85dc1c2d9bf598b27771ddcb6c23e39cc14c4eba835fe3225
Evaluator model: Opus 5.5 (claude-opus-5-5), session effort
Next action: Apply the five MINOR fixes (OE 6, 7, 8 and 28), save the new OE file and send /oe again. /oe needs a PASS; then run /rubric.
Evidence limits: Static universe, SQL overlay and tool catalog only; no live reads or writes executed. Two absence checks rely on evaluator search receipts in Evals/.cache/queries. The Evals/Docs PDFs were applied through Eval 2 and its references and were not re-extracted.
