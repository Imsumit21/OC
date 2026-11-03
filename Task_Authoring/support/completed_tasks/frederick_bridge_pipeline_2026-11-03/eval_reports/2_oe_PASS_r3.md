# Oracle Events Review (Eval 2)

## OE EVALUATION REPORT

### Task: Fred takes over Leonard's Q4 investor-update send list for the bridge round. He builds the send list as a Sheet in his Q4 2025 investor update folder, does what Leonard's two comments on the Existing Investor Update card ask (group checklists, F/up cards in To Do, a comment on the existing Anel card), and replies on Leonard's thread with the counts per group.
### Persona: Frederick Stone - Co-founder

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Inputs reviewed: OEs (saved `oe`, new version "08_Oracle_Events (3).md", 86 events), prompt, assignment, injection SQL (167,306 bytes, read as a static overlay and never executed). Base data came from Universe_SynthCut: Frederick's Gmail thread files, Slack (#bridge-pitch, #executives, #zombie-match3d, the Fred–Leonard IM), his calendar, Trello, Linear and Contacts, plus the tool catalog and acl.md.

What changed since the last review: OE 5, OE 7 and OE 20 were edited. The other 83 OEs are byte-identical to the version reviewed before, and the prompt, assignment and SQL haven't changed, so the earlier checks on those OEs still hold. All three edited OEs were checked again against their records, and the blind recheck passes re-read the whole set.

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
| OE 1–4 | all | VERIFIED | Unchanged. Leonard's email (SQL L138, sent 21:05Z = 2:05 PM PT); the doc (L23) and Q3 decoy (L21); deck slides (L70, L76); #executives note 18:35Z = 11:35 AM PT (L87) |
| OE 5 | all | VERIFIED | Edited. The new clause, Mattel: "I need to follow up with them to see if there is interest from investment stand point", is the Latest Status cell (column 13) of the Mattel row (No. 80) in the injected grid (SQL L31), character for character. "(also a plan)" is a fair reading. The new absence claim "Every other row's Latest Status is blank" holds: the whole grid was decoded and the column read for all 80 named rows. Exactly 23 rows have a note, and OE 5 names all 23. The second Acterra row (No. 71) is blank. Still 80 named rows and 77 distinct names |
| OE 6 | all | VERIFIED | Unchanged. Every listed investor call is on Fred's calendar at the stated PT time; the Sep 29 GFR slot is cancelled; the remaining events are dry runs, POD, SciPlay prep, the SVB catch-up and recurring internal series |
| OE 7 | all | VERIFIED | Edited. The Sep 23 clause now reads "Tue Sep 23 4:55 PM PT, Leonard answering Robert's \"So what's the plan on playventure? They didn't respond right?\": \"I just checked, they didn’t respond\" (this is Play Ventures, not BITKRAFT …)". #bridge-pitch /322 is Robert's question (ts 1758671427 = 4:50 PM PDT) and /323 is Leonard's answer (ts 1758671737 = 4:55 PM PDT). The Sep 25 correction says "it's still their no for this round". The wrong-firm reading flagged last time is fixed. Every other quoted line is unchanged and still verified |
| OE 8–19 | all | VERIFIED | Unchanged. Makers and Raine threads plus the General Catalyst and Supercell traps; GRx, Lakestar and 1AM passes with no call; angel post, DMs, the DocuSign Completed notice and the nudge; SciPlay mail and the Slack pass; LVP; Edith Vane and the Hiro contact; Brightwater; Homa |
| OE 20 | all | VERIFIED | Edited. "after the Sep 12 outreach by [PERSON_NAME_0205] on our behalf (OE 7)": #bridge-pitch /159, Fri Sep 12 3:43 PM PT, "[PERSON_NAME_0205] reached out to GFR, Play, Dentsu, …", and Leonard's earlier /153 "I’m sending this to [PERSON_NAME_0205] for distribution along the pitch deck" shows it was on our behalf. The reschedule (Thu Sep 18 11:13 −0700), the Sep 30 10:30 AM PT call and the 6:41 PM PT follow-up are unchanged |
| OE 21–27 | all | VERIFIED | Unchanged. a16z threads and the program-decision rule; NCsoft, T-accelerate and the Karthic contact, Dentsu, ZOM-567's four comments, and Arthur's 23:20Z note with Leonard's reply |
| OE 28 | all | VERIFIED | Unchanged. The doc rules applied to the records give 1 / 7 / 14 / 3 = 25; the 48 off-list names = 77 − 23 recipients − 6 named offs; Mattel's only contact since the kickoff is the RFP, which the doc excludes, and the OE 5 note is a plan, not outreach |
| OE 29–86 | all | VERIFIED | Unchanged. Folder and README; create, move and update tools exist; card comments; open To Do cards; Oct 1+ calendar; 18 cards; every checklist, item, card, comment and the reply maps to a cataloged Trello or Gmail write; counts 0/1, 7/0, 14/0, 3/0 |

Numeric observability: Anton's 25,000 comes from "he can only do 25 this time, not the 40" (the $40K pledge), so 25 means 25,000. The 25 recipients, 23 Latest Status notes, 48 off-list names and 18 cards were recounted from the records.

Date/time: every event the OEs treat as done is dated before 2025-10-01 07:00 UTC. The Oct 1, Oct 6, Oct 8, Oct 14 and Jan 14 events are presented as future.

Act-vs-defer: none of the writes depends on a proposed resolution. The decoys (Robert's "send it to everyone" mail and Arthur's "just use who Leonard emailed" post) are overridden by Leonard's "Let's not, only the people the doc says."

Expected-values ledger: 278 values and 19 absence claims on the Expected lines, all ledgered against records; none unledgered.

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
None. The one issue from the last review (OE 7's Sep 23 line read as BITKRAFT) is fixed, and the edits to OE 5 and OE 20 are accurate.

### Recommended Fixes
None required.

### Readability (advice only, no score impact)
- The set reads goal-first, with the values written out and traps called out (OE 7, 8, 10, 26, 33). OE 37–83 are deliberately one write each, and that's fine.
- Optional: OE 6 or OE 28 could also name two more decoys as traps. Neither is a missing step:
  - Arthur's Sep 29 #executives post "I'd just use who Leonard emailed this month".
  - Leonard's Sep 29 "waiting for the Turkish VC to show up". That meeting is only on Leonard's calendar, so it doesn't count as a call.

## Deep Recheck

Passes: O1, O2, O3, run on Opus 5.5 (claude-opus-5-5) at session effort, each blind to the main review. O3 did not see the OEs.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| O1 | 86 events | 0 | 0 |
| O2 | 51 requirements across 86 events | 0 | 0 |
| O3 | 126 inventory items | 0 mismatches | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|

None

Effect on verdict: unchanged. Completeness 5, Accuracy 5.

O3 inventory, by group (each item matched to the OEs; every group, count, card and exemption agrees with OE 28, 32, 36 and 85):
- G1: Build the send list (groups, amounts, build access) | Q4 send-list doc / 2025 investor list / calls since Sep 3 / folder README | 80 items (M1–M80: 77 list names, 2 off-list firms with calls, the excluded SVB call, and the Sheet with 25 rows) | Covered by: OE 2–32
- G2: One checklist per group, one item per firm or angel | Existing Investor Update card comments | 25 items (M81–M105: 3 / 1 / 7 / 14) | Covered by: OE 33, OE 37–65
- G3: F/up cards, a comment where a card exists, none for a call after Sep 30 | Card comment of Sep 29 | 20 items (M106–M125: 18 cards, the NCsoft comment on the Anel card, the Dentsu and Makers exemptions) | Covered by: OE 34–36, OE 66–84
- G4: Reply with counts per group | Leonard's Sep 30 email | 1 item (M126: 1 / 7 / 14 / 3) | Covered by: OE 85, OE 86
Scope: the group instruction covers 79 entities (M1–M79). The doc names the population explicitly ("Every name on the 2025 game investor list, angels included", plus off-list firms pitched on a call since Sep 3), and an OE covers every item. This note doesn't change the OE score.

Platform defects: anonymized token. Homa appears in mail and calendar only as [PERSON_NAME_0854], and Frederick's own #bridge-pitch post names it "Homa", so OE 19's "Homa" and the token are both correct. It is not scored.

### FINAL VERDICT: PASS
Score: 5
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Execution status: COMPLETE
Completeness score: 5
Accuracy score: 5
Path feasibility: SUPPORTED
Task solvability: SUPPORTED_BY_OE
Prompt follow-up: NONE
Review policy: oracle-events-v2
Reviewed OE SHA-256: bea7b71ffac79aa4dd5090ece808273b117c54f0b8dcb4d4e2aef6b0b75c47a9
Review context SHA-256: c13c54e24d50c6ca5e4b75aba4549681cfe6068857c86a7f7a5d0b04d1f78183
OE record SHA-256: b7f71076017e29e4209bcbeddd9444cfcb8d7031f3903f19f4715dbd4e416f23
Eval version: task-quality-v1
Eval release SHA-256: a6d0d5849af43fa85dc1c2d9bf598b27771ddcb6c23e39cc14c4eba835fe3225
Evaluator model: Opus 5.5 (claude-opus-5-5), session effort
Next action: Review complete. Run /rubric.
Evidence limits: Static universe, SQL overlay and tool catalog only; no live reads or writes executed. Two absence checks rely on evaluator search receipts in Evals/.cache/queries. The Evals/Docs PDFs were applied through Eval 2 and its references and were not re-extracted.
