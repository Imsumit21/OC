## OE EVALUATION REPORT

### Task: Samuel works through Leonard's Sep 30 DM: a Go/Hold/Drop call on every PNs Beta row and every filed phone-message ask, a calls sheet and one-page note in his Drive folder, ticket comments and moves, new tickets, a Go checklist on the push notifications card, emails to the askers, and the counts back in the DM
### Persona: Samuel Turner - Game Designer

Inputs reviewed: OEs `08_Oracle_Events (2).md` (135 events, saved rev 11), prompt rev 9, assignment (Design / Marketing and GTM / Retrieval / long-horizon / medium), injection SQL rev 8 (read as a proposed overlay, never executed). Universe: Oct 1, 2025 synth-cut. No prompt reference files.

### Phase 1: Structure & Alignment
- Derived critical path (from the prompt, the DM it incorporates, the rule doc the DM names and the roadmap card the rule doc defers to): read the DM → read the rule doc → read all 14 PNs Beta rows → list the 31 DES-314 children and their comments → find asks filed elsewhere (DES-313 for Win & Collect; comment asks on ZOM-542, ZOM-556, ZOM-563, ZOM-483; sweeps of Linear and Trello) → gather test evidence (roadmap lists, live-ops page, ZOM-487/116/363/301, Axe Arena post, NotificationManager.cs, PR #248 comment, QA note, checks sheet, Vincent's Sep 29 and Sep 30 withdrawals, Robert's permission-ask call and Arthur's reply, the cancelled ladder review, the art-thread line and the later calendar line) → apply the six tests in order (36 messages: Go 2, Hold 28, Drop 6) → writes: string ticket, four new tickets with their calls, calls sheet in the folder, one-page note in the folder, checklist with the two Go items, 32 comments, 30 moves (Hold → Backlog unassigned per card 79, Drop → Canceled, Go untouched), 8 emails, counts in the DM last.
- Segments: 135 STEP / 0 CONTEXT / 0 RESPONSE_DESCRIPTION / 0 NON_ACTION.

### Phase 2: Accuracy

Every existing step was checked against the records. All six fields are VERIFIED on every tool step; reasoning steps 29 and 40–47 have tool and parameters NOT_APPLICABLE by design. The ledger covers all 459 values and 14 absence words on the Expected lines (none unledgered).

| Step | Field | Result | Evidence |
|---|---|---|---|
| OE 1 | Expected | VERIFIED | DM in D06L58XCVKK (Samuel is a member), ts 1759264851 = Tue Sep 30 1:40 PM PT; all ten quoted sentences match SQL line 25 |
| OE 2 | Expected | VERIFIED | Doc f_dc45e0e5a8b8635c1b82b2 modified 2025-09-26T17:10:54Z = Fri Sep 26 10:10 AM PT; tests 1–6, Go/Drop/Hold, BETA definition, move rule match the gdocs row word for word |
| OE 3 | Expected | VERIFIED | PN sheet modified 2025-06-23T07:02:43Z = Mon Jun 23 12:02 AM PT; 14 rows, six "Ready" (rows 3, 4, 5, 6, 9, 14); row 6 segmentation "Level 20 not completed and it's been 12 hours since first session" |
| OE 4–5 | Expected | VERIFIED | DES-315…345 (31): titles, creators (Linear users), states (315–320 Done, rest In Review), descriptions ("Built in match3d #248.", "Quests are already in production.", …) and all 62 comment quotes match the SQL; Vincent's comments dated Sep 24 |
| OE 6 | Expected | VERIFIED | Confluence "Live-Ops Event Calendar & Planning": Plague Race "Live; algo bug Aug 2025", Zombie Lane Live, Endless "Live; also one of the three permanent board modes", Weekly Leaderboards "Domino Delights / Zombie Match 3D" Live; Treasure Hunt, Axe Arena, Streak Fever on Domino Delights; Collect & Win "not yet live … under a different name" |
| OE 7–8 | Expected | VERIFIED | DES-313 by Calvin (usr_49b9…), created 2025-09-17T15:20:37Z = 8:20 AM PT, In Review, no parent; comments match |
| OE 9 | Expected | VERIFIED | Base issues updated ≥ 2025-09-23: 17 ZOM tickets; SQL moves ZOM-542/556/483 into the window → exactly the 20 listed, all team Zombie Match 3D |
| OE 10–13 | Expected | VERIFIED | ZOM-542 (Brian, 6:27 AM), ZOM-556 (Julia, 7:08 AM), ZOM-563 (Douglas, Sep 30 11:22 AM), ZOM-483 (Calvin, 9:41 AM): ticket titles and comment text exact |
| OE 14 | Expected | VERIFIED | Base Linear `comments` array is empty; the SQL adds comments only to ZOM-483/542/556/563 among ZOM tickets |
| OE 15 | Expected | VERIFIED | "notification" hits match the scan (ZOM-314/320/366/385/387, DES-9 Backlog 2023, DES-283, older ENG/ART); ENG-2311 and DES-9 are GoD-beta items, outside the Zombie Match beta the rule doc defines |
| OE 16–19 | Expected | VERIFIED | ZM ROADMAP lists "BETA: Oct 10" (SQL rename), "Oct 21", "Backlog" and the named cards; ZOM-487/116/363/301 Done; card "Fix TECH ISSUES" text and last activity Mon Sep 29 1:15 PM PT |
| OE 20–22 | Expected | VERIFIED | 12 base + 1 injected commentCard actions = 13; trello search "notification" = 7 cards (1 ZM, 6 on DD Product Roadmap / Harmony Games, last active ≤ 2025-05-27), "reminder" = 0; card 6851a769c65dc0017a227bb7 on "Jun 30th", Leonard's comment Wed Sep 24 9:00 AM PT |
| OE 23–24 | Expected | VERIFIED | NotificationManager.cs: six scheduling calls; `AddDays(1)` and `AddDays(i * 7)` for i = 1..4 → days 1, 7, 14, 21, 28; titles exact; Arthur's PR #248 comment (Thu Jun 26 1:58 PM PT) on the leaderboard `fireTime` line, also in Samuel's Gmail |
| OE 25–29 | Expected | VERIFIED | QA note (Mon Sep 15 6:05 AM PT) text exact; checks sheet six rows Sep 24; Vincent EMPLOYEE_0012_SLACK_ID; Sep 30 8:12 AM Full Ammo withdrawal in #zombie-match3d; Sep 29 12:40 PM Plague Race iOS withdrawal in DM D06UFE81RF0 (Samuel is a member) |
| OE 30–35 | Expected | VERIFIED | Robert Mon Sep 29 10:40 AM and Arthur 11:21 AM in #zombie-match3d; Leonard 11:05 AM in #zombie-art; calendar "Lapsed copy check" created Sep 29 3:14 PM, updated Sep 30 10:02 AM; cancel note Thu Sep 25 8:00 AM; Brian's Axe Arena post Mon Sep 22 9:22 AM in #company-internal |
| OE 36–37 | Expected | VERIFIED | USER_COHORT_RETENTION: d1_ret "% returning on Day 1", d7_ret "NULL until the 7-day window closes"; 2025-09-15 zombie_match_3d ios 237 / 31.65 / 9.28, android 103 / 37.86 / 10.68 (D1/D7 windows are closed for this cohort; the immature D14 cell is not used) |
| OE 38–39 | Expected | VERIFIED | Folder d_caafeec2804b3a67ce46aa owned by Samuel; eight contact emails exact |
| OE 40–47 | Expected | VERIFIED | Test-by-test counts reproduce: 36 → 5 Drop (test 1) → 6 Hold (test 2) → 6 scheduled, 1 Drop covered (Lapsed 14 days), 18 Hold (test 3) → 1 Hold (test 4) → 1 Hold (test 5) → 2 Hold (test 6) → Go 2 / Hold 28 / Drop 6; headlines "The Horde Is Growing…" (no change) and "Your Squad Is Waiting" (change; the Sep 30 calendar line replaces the Sep 29 art-thread line) |
| OE 48–135 | All | VERIFIED | Each write targets the right record with the right call; Hold moves follow card 79 ("Held tickets sit in Backlog, unassigned"), which postdates and overrides the rule doc's Todo; eight email recipients and their asks match the creators/commenters; counts posted last |

Numeric observability (2.3A): the Snowflake values come straight from the two cohort rows (2-decimal columns, as stored); the day list comes from the code loop; every count is a direct tally of listed records. No unstated calculation or unobservable precision.

Act-vs-defer (2.6): no write rests on a proposed resolution. The Hold moves follow the newer roadmap card rather than the rule doc's Todo clause, which the rule doc itself allows ("unless the roadmap says otherwise").

Decision forks (2.8): `hg_decision_forks` found no hedge wording. Each boundary item has a record that speaks to it: Lapsed 14 days (Leonard's cancel note "day 14 is already covered" plus the rule doc's "covers it under another message" Drop); Comeback gift (Leonard's "version 2 idea, it isn't in the beta"); the Win & Collect row (Confluence's "same feature … under a different name" ties it to DES-313); the four comment asks (each says it is separate from the related ticket, or, for teammate lives, asks for a different message); ENG-2311 and DES-9 (GoD - Beta items, outside the rule doc's Zombie Match beta).

### Format & Standardization
No shape defects. Every OE is numbered, does one action, names its service, and has an Expected: line.

### Phase 3: Completeness
| Requirement | Covered by | Result |
|---|---|---|
| Read the DM and the rule doc | OE 1, 2 | COVERED |
| Every PNs Beta row | OE 3 | COVERED |
| Every ask under DES-314, with audience | OE 4, 5 | COVERED |
| Asks filed on other tickets or cards | OE 7–15, 20, 21 | COVERED |
| No duplicate ticket (Win & Collect = DES-313) | OE 6–8, 58, 65 | COVERED |
| Evidence for tests 1–6 | OE 6, 16–18, 23–35, 40–45 | COVERED |
| Final headline / String change | OE 23, 32, 33, 46 | COVERED |
| Sheet in Samuel's folder | OE 38, 57–59 | COVERED |
| One-page note in the folder | OE 23, 36, 37, 60, 61 | COVERED |
| Call as a comment on each ticket | OE 50, 52, 54, 56, 65–96 | COVERED |
| Move each ticket to match | OE 19, 97–126 | COVERED |
| A ticket for each ask with none; string ticket | OE 48, 49, 51, 53, 55 | COVERED |
| Checklist of every Go | OE 22, 62–64 | COVERED |
| Email each asker except Leonard | OE 39, 127–134 | COVERED |
| Counts in the same DM, last | OE 47, 135 | COVERED |

- Path feasibility: SUPPORTED. Task solvability: SUPPORTED_BY_OE.
- Outcome-first mapping: every write (OE 48–135) and the call logic (OE 40–47) map to Outcome rows on the sheet, the note, the tickets, the checklist, the emails and the DM. Reads map to no rubric of their own. No Process row is needed.

### Issues Found
| # | Step | Issue | Component | Effect |
|---|---|---|---|---|
| — | — | None | — | — |

### Recommended Fixes
None required.

### Readability (advice only, no score impact)
- The set already reads well: goals first, values written out, traps named (Full Ammo and Plague Race withdrawals, the art-thread line replaced by the calendar line, card 79 overriding Todo, day 14 already covered).
- OE 9 and OE 15 lean on query notation. Optional: in OE 15, say plainly that ENG-2311 and DES-9 come up but sit in the GoD - Beta project, so they are another game's beta and not in scope. That makes the exclusion easy to turn into a rubric row.

## Deep Recheck

Passes: O1, O2, O3, Opus 5.5 (claude-opus-5-5), session effort, each blind to the main review (O3 without the OE file).

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| O1 | 135 events | 0 | 0 |
| O2 | 135 events | 1 | 0 |
| O3 | 89 items (6 groups) | 0 mismatches | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | O2 | DM: "Next to it a one-page note for the team" (OE 59, OE 61 only move the files to the folder) | gdrive d_caafeec2804b3a67ce46aa: "shared_with_emails":[], "visibility":"private" | Writes: target and audience | Completeness | REJECTED | The prompt fixes the destination: "The new sheet and the one-page note go in my Drive folder and the checklist goes on our push notifications card." The DM's only notification ask is "When it's done tell me here how many Go, Hold and Drop." "For the team" describes who the note is written for, not a share or send action. No sentence or record asks for sharing or a link, so a set without sharing is complete. Not a fork: no record or sentence supports a share write |

Effect on verdict: unchanged.

- G1: Make a call on every PNs Beta row and every filed ask, using the rule doc | PNs Beta tab, DES-313…345, comments on ZOM-483/542/556/563 | 36 items (M1–M36) | Covered by: OE 40–47 (calls), OE 58 (sheet rows), OE 46 (headlines)
- G2: Leave the call as a comment and move the ticket to match | DES-313, DES-315…345 | 32 items (M37–M68) | Covered by: OE 65–96 (comments), OE 97–126 (moves; Go DES-316/317 left unchanged)
- G3: A ticket for anything with none; string ticket for a changed line | four comment asks, Lapsed 7 days | 5 items (M69–M73) | Covered by: OE 48, 49–56
- G4: Every Go on the checklist | card 6851a769c65dc0017a227bb7 | 2 items (M74–M75) | Covered by: OE 62–64
- G5: Email each asker except Leonard | Calvin, Brian, Robert, Oliver, Julia, Owen, Martin, Douglas | 8 items (M76–M83) | Covered by: OE 39, 127–134
- G6: Counts in the DM; note's lapsed days and client-scheduled Holds | DM D06L58XCVKK; one-page note | 6 items (M84–M89) | Covered by: OE 135, OE 60
Scope: G1 (36 items) and G2 (32 items) each exceed 15 items, but every item is named and covered by an OE. The DM names the sources the scope reaches (the PNs Beta tab, the tickets and cards), so no prompt change is suggested.

Fix text check: no fix OEs are proposed. The readability suggestion about ENG-2311 and DES-9 was checked: both are in Linear project "GoD - Beta".

Platform defects: none. The USER_COHORT_RETENTION D14 cells for the Sep 15 cohort are immature (FD-3785). The set does not use them; it uses only D1 and D7, whose windows have closed.

### FINAL VERDICT: PASS
Score: 5
Execution status: COMPLETE
Completeness score: 5
Accuracy score: 5
Path feasibility: SUPPORTED
Task solvability: SUPPORTED_BY_OE
Prompt follow-up: NONE
Review policy: oracle-events-v2
Reviewed OE SHA-256: 4924949d7fd386c99cddccb3b90c6a9cbaa2a6661b255a5b757370278fc5f6b1
Review context SHA-256: dc92d5c67907310ea93b66c9de810b9abd6ab3fbcb40406d0542f8171f2acbaf
OE record SHA-256: 8dd1ee97d25fc393e7942f1ae36ff9e5a4cdb4482d7a2ea11f5e4b41b308bbd1
Eval version: task-quality-v1
Eval release SHA-256: 81446b85bb68b971bfce06d9d3cf07ad43d923b5702670f206122d1f6d34d53c
Evaluator model: Opus 5.5 (claude-opus-5-5), session effort
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Next action: Proceed to /rubric
Evidence limits: Static universe, SQL and catalog evidence; no live writes executed. The PN sheet and Snowflake values were checked through evaluator extracts of the large exports (source SHA-256 recorded in each extract).
