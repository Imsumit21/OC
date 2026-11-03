# Oracle Events Review (Eval 2)

## OE EVALUATION REPORT

### Task: Fred takes over Leonard's Q4 investor-update send list for the bridge round. He builds the send list as a Sheet in his Q4 2025 investor update folder, does what Leonard's two comments on the Existing Investor Update card ask (group checklists, F/up cards in To Do, a comment on the existing Anel card), and replies on Leonard's thread with the counts per group.
### Persona: Frederick Stone - Co-founder

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Inputs reviewed: OEs (saved `oe`, new version "08_Oracle_Events (2).md", 86 events), prompt, assignment, injection SQL (167,306 bytes, read as a static overlay and never executed). Base data came from Universe_SynthCut: Frederick's Gmail thread files, Slack (#bridge-pitch, #executives, #zombie-match3d, the Fred–Leonard IM), his calendar, Trello, Linear and Contacts, plus the tool catalog and acl.md.

What changed since the last review: OE 6, 7, 8, 21, 28 and 35 were rewritten. Every other OE is byte-identical to the version reviewed before. The prompt, assignment and SQL are unchanged, so the earlier checks on the unchanged OEs still hold. Each rewritten OE was checked again against its records.

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
| OE 1–5 | all | VERIFIED | Unchanged. Leonard's email (SQL L138, sent 21:05Z = 2:05 PM PT); the doc (L23) and Q3 decoy (L21); deck slides (L70, L76); #executives note 18:35Z = 11:35 AM PT (L87); list grid (L31) with 80 named rows and 77 distinct names |
| OE 6 | all | VERIFIED | Every listed investor call is on Fred's calendar at the stated PT time, and the Sep 29 GFR slot is cancelled. The rest of the Sep 3–30 events are DRY RUN, Pitch dry run take 2, Engine Dry Run, POD: PROTOTYPE, SciPlay prep, the SVB catch-up (two copies, one shown as [USERNAME_4501]) and recurring internal series ("All Hands" weekly on Fridays, standups, sprint/art meetings, Executives Biweekly Sync, UA Sync). The added "recurring internal meetings" wording closes the earlier gap |
| OE 7 | expected data | MINOR (deep recheck) | One clause is attached to the wrong firm. "Tue Sep 23: \"I just checked, they didn’t respond\"" comes straight after the bitkraft post, so it reads as BITKRAFT. In #bridge-pitch it is Leonard's 4:55 PM PT answer to Robert's 4:50 PM PT question "So what's the plan on playventure? They didn't respond right?". So it is about Play Ventures. Everything else is VERIFIED. Sep 3 post (/33): "Reached out to" plus every quoted line ("among others" is right). Sep 8 post (/89): "*VCs that we can talk to but not top priority*" holds "Early Bird (Matthew can intro)", "Moon Fire (Matthew can intro)", "Transcend - [PERSON_NAME_2322] (maybe talk to him to get it out of the way lol)" and "Index (it was too early for them and wanted to see KPIs)". Acterra and "Galaxy ([PERSON_NAME_3050] left the company so we lost our contact There)" sit under "*Other VCs may be relevant + Family Funds --> No further update*". The Sony line is IH's read, and the doc says "An advisor's own read on whether a firm invests isn't the firm's answer." |
| OE 8 | all | VERIFIED | Makers thread, Wed 3 Sep 13:57:45 −0700: "are kicking off a $2.5M bridge this week". Raine thread "Intros: PERSON_3068_NAME, …", 14:13:38 −0700: "kicking off a $2.5M bridge this week", and the quoted 2023 signature reads "*The Raine Group*". Each thread has one message, from Leonard. Trap 1: "Leonard Hayes from SEMC onto the next adventure" (14:17:26 −0700) goes to PERSON_0616, signed "Managing Director, General Catalyst" in the quoted thread. Trap 2: "[SOURCE_ORG_0001] bridge round, quick chat?" (15:54:06 −0700) says "Given Supercell’s focus on novel AI x games, would this be interesting for" Supercell. Superplay has no outreach mail, and its list note "Reached out - no response as of 09/11" is the outreach. A search of all 4,656 of Fred's threads finds no bridge mail to the other 48 names |
| OE 9–20 | all | VERIFIED | Unchanged. GRx, Lakestar and 1AM passes with no call; angel post, DMs, the DocuSign Completed notice and the nudge; SciPlay mail and the Slack pass; LVP; Edith Vane and the Hiro contact; Brightwater, Homa, GFR |
| OE 21 | all | VERIFIED | Leonard's Sep 3 mail (13:47 PM PT) pitches "a $2.5M bridge this week", so the paraphrase is accurate. "Will review" came 03:09Z Sep 4 = 8:09 PM PT Sep 3. The speedrun forward is from Sep 30 8:21 PM PT. The doc's program-decision rule applies |
| OE 22–27 | all | VERIFIED | Unchanged. NCsoft, T-accelerate and the Karthic contact, Dentsu, ZOM-567's four comments, and Arthur's 23:20Z note with Leonard's reply |
| OE 28 | all | VERIFIED | The doc rules applied to the records give 1 / 7 / 14 / 3 = 25. The 48 off-list names = 77 − 23 recipients − 6 named offs. The new reasons all match records. Mattel: Sep 26 "since the kickoff that's only been an RFP conversation, we haven't pitched them the bridge", and the doc says "Only outreach about the bridge counts, not RFP or partnership mail." Index has only the earlier-round answer. Transcend Fund, Acterra, Early Bird, Moon Fire, 20VCs and Balderton have plans only. Galaxy is a lost contact. All ten are rows on the list (L31: 13, 71/86, 66, 67, 68, 73, 31, 52, 80) |
| OE 29–34 | all | VERIFIED | Unchanged. Folder and README (L12, L25); create, move and update tools exist; card comments L113 and L115; open To Do cards are Playable Kickoff and the Anel card |
| OE 35 | all | VERIFIED | Fred's calendar has two Oct 1 20:30Z (1:30 PM PT) copies: "1:30pm PT \|\| MEETING \|\| Harmony Games & Dentsu" (/events/2195) and "1:30pm PT \|\| MEETING \|\| [SOURCE_ORG_0001] & Dentsu" (/events/9687). Michael Cheung is on Oct 8, the review on Oct 6 and the board meetings on Oct 14 and Jan 14. All are after the clock |
| OE 36–86 | all | VERIFIED | Unchanged. 18 cards (21 − NCsoft − Dentsu − Makers); every checklist, item, card, comment and the reply maps to a cataloged Trello or Gmail write; counts 0/1, 7/0, 14/0, 3/0 |

Numeric observability: Anton's 25,000 comes from "he can only do 25 this time, not the 40" (the $40K pledge), so 25 means 25,000. The 25 recipients, 48 off-list names and 18 cards were recounted from the records.

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
| 1 | OE 7 | "Mon Sep 22 10:57 AM PT: \"reached out to bitkraft\". Tue Sep 23: \"I just checked, they didn’t respond\"." The Sep 23 line reads as BITKRAFT not responding. In #bridge-pitch it is Leonard's Tue Sep 23 4:55 PM PT answer to Robert's 4:50 PM PT question "So what's the plan on playventure? They didn't respond right?". So it is about Play Ventures, and it has no time. Found by deep recheck O1. | Accuracy | MINOR: BITKRAFT stays Awaiting reply (outreach Sep 22, no call, no no). Play Ventures stays off (its pasted no counts, per the Sep 25 correction "it's still their no for this round"). No group, count, card or write changes, but a rubric row built on this line would credit the wrong firm. |

All five issues from the previous report (OE 6, 7, 8 and 28) are fixed in this version.

### Recommended Fixes
1. OE 7, replace the clause `Tue Sep 23: "I just checked, they didn’t respond".` with:
   `Tue Sep 23 4:55 PM PT, Leonard answering Robert's "So what's the plan on playventure? They didn't respond right?": "I just checked, they didn’t respond" (this is Play Ventures, not BITKRAFT; the Sep 25 correction below still makes it their no).`
   Or drop the clause. BITKRAFT's group needs only the Sep 22 outreach and the absence of a call or a no.

### Readability (advice only, no score impact)
- The set reads goal-first, with the values written out and traps called out (OE 8, 10, 26, 33). OE 37–83 are deliberately one write each, and that's fine.
- You could name three decoys as traps in OE 6 or OE 28, though none of them is a missing step:
  - Arthur's Sep 29 #executives post "I'd just use who Leonard emailed this month".
  - Leonard's Sep 29 "waiting for the Turkish VC to show up" / "this is gonna be a no". That meeting is only on Leonard's calendar, so it isn't a call, and the "no" is a guess, not the firm's answer.
  - The "Comments (Ibrahim)" note on Sony Mobile, "IH says they don't invest in gaming". It is an advisor's read in a column the doc says doesn't count.
- OE 20 says "IH's outreach (OE 7)", but the Sep 12 post shows the name as "[PERSON_NAME_0205]". If you add a short pointer, the label is easier to check. The list's "IH to reach out" comments on GFR, Triptyq, Turkven and Harlem tie the two together.

## Deep Recheck

Passes: O1, O2, O3, run on Opus 5.5 (claude-opus-5-5) at session effort, each blind to the main review. O3 did not see the OEs.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| O1 | 86 events | 1 | 1 |
| O2 | 52 requirements across 86 events | 5 | 0 |
| O3 | 107 inventory items | 0 mismatches | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | O1 | "Mon Sep 22 10:57 AM PT: \"reached out to bitkraft\". Tue Sep 23: \"I just checked, they didn’t respond\"." (OE 7) | #bridge-pitch 2025-09.json /322 Robert 4:50 PM PT "So what's the plan on playventure? They didn't respond right?"; /323 Leonard 4:55 PM PT "I just checked, they didn’t respond" | Expected data | Qualifier: wrong firm | CONFIRMED | Opened both messages; the line answers Robert's Play Ventures question. Harmless to groups, so MINOR (Issue 1). |
| DR2 | O2 | "Settle each recipient's group and details …" (OE 28) | OE text | Segments | Non-action | REJECTED | A reasoning step over earlier reads is allowed (Eval 2: "A reasoning or calculation step may explain that no tool call is needed"); it is not a "does not…" statement. |
| DR3 | O2 | "Work out the follow-up cards …" (OE 36) | OE text | Segments | Non-action | REJECTED | Same as DR2. |
| DR4 | O2 | "Count the firms and angels in each group …" (OE 85) | OE text | Segments | Non-action | REJECTED | Same as DR2. |
| DR5 | O2 | "after IH's outreach (OE 7)" (OE 20) | #bridge-pitch /159 "[PERSON_NAME_0205] reached out to GFR, Play, Dentsu, General Catalyst, Sciplay …, Triptyq, Turkven, Harlem Capital"; /153 "I’m sending this to [PERSON_NAME_0205] for distribution along the pitch deck" | Coverage | Missing step | REJECTED | OE 7 obtains the post. Whoever the token is, they reached out on our behalf, and the doc counts "anyone who reached out or made an intro on our behalf", so the groups hold. Noted under Readability. |
| DR6 | O2 | "none of these is an investor call." (OE 6) | #executives Sep 29 "waiting for the Turkish VC to show up"; gcal "Leonard Hayes and PERSON_5748_NAME" on Leonard's calendar only | Coverage | Missing step | REJECTED | The doc says "calls that never went on Fred's calendar don't" count, and Fred's calendar has no such event, so no read is needed for a correct path. Noted under Readability. |

Effect on verdict: Accuracy drops from 5 to 3 (one confirmed MINOR in OE 7). Completeness stays 5. The record was re-saved and recomputed.

O3 inventory, by group:
- G1: Build the send list (groups, amounts, build access) | Q4 send-list doc / 2025 investor list / calls since Sep 3 | 81 items (M1–M80, M106: 77 list names, 2 off-list firms with calls, the excluded SVB call and the Sheet with 25 rows) | Covered by: OE 2–32
- G2: One checklist per group, one item per firm or angel | Existing Investor Update card comments | 4 items (M81–M84: 1 / 7 / 14 / 3 = 25 items) | Covered by: OE 33, OE 37–65
- G3: F/up cards, or a comment where a card exists, none for a call after Sep 30 | Card comment of Sep 29 | 21 items (M85–M105: 18 cards, the NCsoft comment, the Dentsu and Makers exemptions) | Covered by: OE 34–36, OE 66–84
- G4: Reply with counts per group | Leonard's Sep 30 email | 1 item (M107: 1 / 7 / 14 / 3) | Covered by: OE 85, OE 86
Scope: none (the instructions cover the 77-name list and the card rules, which the prompt and doc name explicitly; every item matches an OE).

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
Reviewed OE SHA-256: 22fc978ed33b8d7ec33484803f13f42adb9add670cf324da2f7a921f3921cdd8
Review context SHA-256: e27af6ad8eee510d8b4e34f0c6c24d11c13b2f95396f5ba090a9844b46d9d8d3
OE record SHA-256: 85952d03a1eaa69ebbb71da9755721643e0008d258be516df30b3694a9a9e0ef
Eval version: task-quality-v1
Eval release SHA-256: a6d0d5849af43fa85dc1c2d9bf598b27771ddcb6c23e39cc14c4eba835fe3225
Evaluator model: Opus 5.5 (claude-opus-5-5), session effort
Next action: Fix the one OE 7 clause (Recommended Fix 1), save the new OE file and send /oe again. /oe needs a PASS; then run /rubric.
Evidence limits: Static universe, SQL overlay and tool catalog only; no live reads or writes executed. Two absence checks rely on evaluator search receipts in Evals/.cache/queries. The Evals/Docs PDFs were applied through Eval 2 and its references and were not re-extracted.
