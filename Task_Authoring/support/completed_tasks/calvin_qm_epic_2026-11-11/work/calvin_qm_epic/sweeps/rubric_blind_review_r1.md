# Blind rubric review r1 (as the platform /rubric would read it)

Inputs read: `04_Prompt.txt`, `08_Oracle_Events.md` (104 events), `09_Rubrics.json` (121 rows: 120 Outcome, 1 Process, weight sum 471), `01_Universe_Inject.sql` (static), `Evals/3_Rubrics_Eval.md`, and under `Evals/references/rules/`: `coherent_record.md`, `rubric_sampling.md`, `common_errors.md` §7, `qc_rubric_v10.md`, `long_horizon.md` (sampling part), `deep_recheck.md` R1–R7, `rubric_qc_examples.md`. Base data only through `hg.py search`.

Row numbers are 1-based positions in the JSON. Severities follow the Eval 3 taxonomy (`hg-strict-overrides-v1`). Where I am predicting how a strict reviewer would read a borderline row, I say "risk" and give my confidence.

## Verdict in one paragraph

Every expected value is right: I recomputed all 39 statuses, the 22 ticket states, the 17 sub-issue states, the ten open counts, the 7 review rows and the totals 10 / 9 / 20 / 0 / 7 from the SQL and the Oracle Events and found no factual error. The set still fails Overall Rubric Quality, because of three missing outcomes, two clearly bundled volume rows, one over-specific Why row, and one large cascade group (the 22 "once it sits under a child issue" state rows). Weights are close (2 to 3 rows one level off). No negative row, no all-fail row, no category error.

## Facts checked (item 6)

| Check | Result |
|---|---|
| 39 statuses (OE 21) recomputed from the sheet grid, the legend, Arthur's rule, the ticket notes, the PR comments and the Slack sightings in the SQL | All match. Passed = rows 3, 5, 7, 22, 23, 26, 27, 31, 33, 35 (10). Waiting on QA = 1, 2, 6, 13, 14, 18, 25, 37, 38 (9). Waiting on a fix = the other 20. |
| Expected state on the 22 existing tickets (R8–R41) | All match. Eight change (ZOM-568, 572, 573, 584 to In Validation; ZOM-571, 574, 581, 585 to Todo); fourteen stay as found. Base states: ZOM-556 Todo, ZOM-560 Todo (read from `linear/data.json` `/issues/3632`, `/issues/3637`); the 20 injected tickets as in the SQL. |
| Expected state on the 17 new sub-issues (R5–R43) | All match. |
| Note status on the 22 tickets (R44–R65) | All match. |
| Counts 17 new / 22 moved / 39 reports / 10 areas | Match (18 blank Ticket cells, minus rows 11 and 20, plus Marcus = 17; 20 keys plus ZOM-556 and ZOM-560 = 22). |
| Open counts per area (R95–R104) | Match: 3, 3, 3, 5, 4, 3, 1, 1, 4, 2. Every area Open, 0 Clear. |
| Review list (R86–R89, R116) | Match: rows 6, 8, 36 (Level-end rewards) and 15, 17, 18, 19 (Collect & Win) = 7. |
| Share recipients (R105–R109) | Match the attendee list on Calvin's event `evt_342a813cb7765d4a6fce8d` minus Calvin. |
| Parent areas (R67, R68, R72–R74) | Match the sheet's Area column; Marcus's report is Season Pass. |
| ZOM-543 | Base: title "Queue Manager", team_ZOM, In Progress, no parent. |
| #builds branches | Spot-checked #1718 (feature branch), #1745 and #1757 (main); the rest taken from OE 8. |

Not re-verified from base (taken from the Oracle Events): PR merge times for #465/#472/#473/#475, the eight unlisted merged PRs, Calvin's DM with Vincent, the thread parents in #zombie-bugs, and 12 of the 15 build posts. The base search is slow; these are an evidence limit, not a finding.

One thing to know: base #builds also has "DD Android Submission - #135 - develop" and "DD Android - #2006 - develop". The ZM tickets and channels make the Match3D builds the right reading, and no row depends on the DD ones.

## Findings

### A. Missing coverage (Major, one issue each, numerator only)

| # | Missing outcome | Why it is owed | Suggested row |
|---|---|---|---|
| A1 | The review-list number on the slide | Brian's note: "Slide: the five numbers I asked you for"; OE 103 lists 7 on the review list. R117–R120 grade 10, 9, 20 and 0 only. | "The Agent gives 7 as the number of reports on the review list on the slide it adds to Calvin's ZM queue manager presentation" (weight 5) |
| A2 | The "why" in the Linear notes | Brian's note: "leave a note with the status and why"; OE 71–92 each expect a why. R44–R65 grade the status only; no row grades any why on a ticket. R90–R91 grade the sheet's Why cell, a different artifact. | Sample the hard ones, five or fewer: "The Agent gives, in its note on ZOM-585, the reason that the bug was seen again on Android Submission 135 after its pass"; same shape for ZOM-586 (Submission 135), ZOM-571 (Arthur Blake's review says the fix is not in pull request #472), ZOM-568 (merged pull request #472 holds the fix), ZOM-582 (still happens on iOS Internal #1757, built after #475 merged) |
| A3 | The Area column of the Reports tab | Area is one of the six requested columns and no row grades any Area value (`coherent_record.md` C1: "Omitting the whole requested column … is a gap"). | "The Agent gives Marcus Bennett's report that the season pass icon glow stays on after everything is claimed the Area Season Pass in the Reports tab of the stock-take sheet"; plus one wording trap: "…the report "Season pass popup comes up on top of the daily gift when both are due" the Area Daily Gift…" |

Smaller gaps, worth a row each but arguable:

- **Ticket cell of a report with a new sub-issue.** OE 94 fills it with the new key; R84–R85 sample only existing tickets. Suggested: "The Agent puts the key of the sub-issue it creates for the report "Quest tutorial arrow points at the wrong tab after the last panel closes" in that report's Ticket cell in the Reports tab of the stock-take sheet".
- **Parent of a new sub-issue whose wording points at another area.** R67–R68 sample an ordinary row and Marcus. Rows 9 (Daily Gift, wording says "season pass") and 25 (Boss Arena, wording says "tutorial") are the edge cases (`rubric_sampling.md`: "Include … meaningful hard/edge cases").
- **Wrong-target sharing.** No row fails a run that shares with extra people. Optional: "The Agent shares the stock-take sheet with exactly 5 people".

### B. Not atomic (Major)

| Row | Span | Why | Corrected title(s) |
|---|---|---|---|
| R1 | "creates exactly 10 child issues … each titled with a different one of the ten areas … in team ZOM with no assignee" | Count plus name set is allowed as one cohort control (`long_horizon.md`: "Exact cohort multisets … rejects missing, duplicate, and extra keys in one independently verifiable claim"). Team and no assignee are two further properties that fail apart from the count (Eval 3 §2.2: "Quantifier, disjunctive or compound phrasing over independently gradable items … → independent"). Weight 1 on five assertions. | (a) "The Agent creates exactly 10 child issues under the Linear ticket ZOM-543 (Queue Manager), one titled for each of Tutorials, Level-end rewards, Daily Gift, Season Pass, Collect & Win, Win Streak, Zombie Lane, Boss Arena, Endless Mode and Card packs (extra words around the area name are fine)"; (b) "The Agent creates the Tutorials child issue under ZOM-543 with no assignee"; (c) drop team, or "…in team ZOM" as its own sample |
| R66 | "exactly 17 new sub-issues …, each for one report that no existing ticket holds, with the report as its title, no priority and no assignee" | Five assertions. R69 and R70 already sample priority and assignee, so one assignee slip fails R66 (5) and R70. "No existing ticket holds" cannot be checked from the title. | "The Agent creates exactly 17 new sub-issues under the area child issues it creates under ZOM-543" |
| R8, R10, R12, R14–R25, R28, R32, R34, R36, R38, R40, R41 (22 rows) | "has ZOM-567 … in the state Todo once it sits under a child issue of ZOM-543" | A move plus a state. Brian's note asks for each on its own ("move that ticket under the child"; "If its state does not match the status, put …"). A run that sets ZOM-568 to In Validation but leaves it unparented fails the state row for the move. Risk, about 70%: a reviewer may accept it as two fields of one update. See C1 for the cascade, which stands either way. | See C1 |
| R76, R77 | "a tab named Reports whose header has the columns Report, Area, Status, Ticket, Review list and Why" | Tab name plus six (three) column names. Defensible as fields of one header write (§2.2 "Different fields of one write action"). Risk, about 40%. | Split the name from the header: "The Agent names a tab of the stock-take spreadsheet it creates Reports"; "The Agent gives the Reports tab … a header with the columns Report, Area, Status, Ticket, Review list and Why (any order)" |

Volume rows, one by one (item 2):

| Row | Template | Allowed? |
|---|---|---|
| R71 "exactly 22 existing ZOM tickets" | Pure count on a required write | Yes. `rubric_sampling.md`: "add one criterion checking the volume of the output (its exact count or total)"; `common_errors.md` §7.8 GOOD: "closes exactly three of the leftover reviews". |
| R86 "exactly 7 report rows" | Pure count | Yes, same rule. See D2 for what it cannot catch. |
| R92 "exactly 10 areas … one row each" | Pure count | Yes. Naming the ten would stop ten wrong names passing. |
| R78 "exactly 39 reports … (the 38 rows of Vincent's flow pass sheet and Marcus Bennett's pass icon glow report)" | Count plus a membership gloss | Allowed as a cohort control; the gloss cannot be checked from the title. Minor. |
| R1 | Count, names, team, assignee | Must split (above). |
| R66 | Count, eligibility, title, priority, assignee | Must split (above). |

### C. Cascades and duplicates (Moderate, one group each)

**C1. The 22 existing-ticket state rows share "once it sits under a child issue of ZOM-543".** One error (tickets left without a parent, or placed straight under ZOM-543) fails all 22 (88 of 471 points) plus R71–R74 (16 points): 22% of the rubric on one condition. This is the pattern in Eval 3 §3.3 ("each embeds the same acceptance condition"). For the fourteen tickets whose state does not change, the row has no Agent action of its own: it passes on the move alone.

Suggested repair:
- Eight tickets that change: "The Agent sets ZOM-568 (the report "Level-end coins fly while the pre-level panel is already open") to the state In Validation". Same for ZOM-572, 573, 584 (In Validation) and ZOM-571, 574, 581, 585 (Todo). An idle run fails each.
- Fourteen that do not change: drop the state row. The note rows R44–R65 already reject the wrong status for each, including the three traps (ZOM-576, 582, 586). Add one count on the write: "The Agent changes the state of exactly 8 of the existing ZOM tickets it moves under the child issues of ZOM-543".
- Grade the move itself for more than three tickets, in R74's form.

**C2. Rows that name "the Reports tab" / "the Areas tab"** (R78–R91, R92–R104). A tab named "Report" or left as "Sheet1" could fail up to 28 rows with R76/R77. A grader will probably find the tab by content. Minor; no change needed if R76/R77 are the only rows that test the name.

Not a group, but a concentration to know about: one misread report costs many rows across artifacts. Missing Owen's note on ZOM-586 fails R28, R59, R2, R93, R101, R112, R114, R115, R117, R119, R120 (55 points, 11.7%). These are separate prompt-named artifacts, so §3.3 does not count them ("Rows that merely share a likely model root cause are not a group").

### D. Overly specific and overly broad (Major where confirmed)

| # | Row | Span | Issue | Why | Corrected title |
|---|---|---|---|---|---|
| D1 | R91 | "the reason that it has no fix and no QA pass" | overly_specific; evidence also wider than the title | "No fix in main yet" is a complete why for Waiting on a fix and fails the row. The evidence rejects only "an empty Why cell", which accepts more than the title (§2.7 pattern 5). | "…the reason that no fix for it is in main (any wording with that meaning: no fix yet, no pull request)" |
| D2 | R86, R116 | "exactly 7" | overly_broad by coincidence | The old agenda (Collect & Win, Daily Gift) also gives 7: four Collect & Win plus three Daily Gift. A run that used Brian's Sep 29 DM or the Oct 3 invitation passes R86 and R116. Only R88 and R89 catch it, and §2.7 says a sibling is no defence. The DM number cannot be repaired in the rubric. | Add "The Agent marks exactly 3 reports of the area Level-end rewards as on the review list in the Reports tab of the stock-take sheet" |
| D3 | R44–R65 | "adds a comment on ZOM-567" | overly_specific, risk about 35% | Brian says "leave a note". Text added to the description is a note. Eval 3's own valid example accepts "in a comment or in the ticket's description". | "The Agent leaves a note on ZOM-567 (a comment, or text added to its description) that gives …" |
| D4 | R86–R89 | "(Yes, a tick or x)" | overly_specific, risk about 30% | TRUE, Y or a ticked checkbox are not in the list. | "(any affirmative mark: Yes, Y, TRUE, a tick or x)" |
| D5 | R90 | "seen again on Android Submission 135 (135 or Submission #135)" | harmless_specificity (Minor); evidence wider than the title | "Vincent saw it again on Sep 30 after the nr on #1745" is a valid why without the build number. The evidence rejects only "a reason that leaves out the later sighting". | "…the reason that it was seen again after its pass (Vincent Parker's Sep 30 sighting, on Android Submission 135)" |
| D6 | R1 | "(a prefix before the area name is fine)" | harmless_specificity (Minor) | "Tutorials flow" has a suffix. | "(extra words around the area name are fine)" |

Rows I tested and found sound on these two tests: the 17 sub-issue state rows (a wrong status writes a different state and fails), the status aliases in R44–R65 and R79–R83 (each wrong status is one of the other two names and is rejected), R75 ("created there or moved in"), R76/R77 ("any order"), R95–R104 (number or list), R105–R109 ("any role"), R111 (new message or thread reply), R115/R120 ("0, zero, none or no areas"), R43/R68/R82 (Marcus's report described by meaning, no fixed title).

### E. Not self-contained (Major by taxonomy; risk)

| Rows | Phrase | Identifiable from the title and the run? | Fix |
|---|---|---|---|
| R76–R109 (34 rows) | "the stock-take sheet" | Usually yes: the run creates one new spreadsheet. Not from the title alone: only R75 says it is a new spreadsheet in Calvin's folder, and nothing fixes its name. Fails if the run makes two sheets or edits Vincent's. Risk about 35%. | "the stock-take spreadsheet it creates" in each title |
| R71 | "one of the ten area children" | Partly: the ten are named only in R1. | "one of the area child issues the Agent creates under ZOM-543" |
| R66 | "each for one report that no existing ticket holds" | No. | Removed by the split in B |
| R92 | "exactly 10 areas" | The count yes, the names no. | Name the ten, or leave as a pure count |
| R78 | "the 38 rows of Vincent's flow pass sheet" | The count yes, the membership no. | Leave as a count; keep the gloss in the evidence |

Self-contained as written: R2–R4, the 17 sub-issue rows, R67–R70, R72–R75, R105–R121.

### F. Negative rows and the idle-agent test

No row passes for an agent that writes nothing and answers nothing. The fourteen unchanged-state rows fail an idle agent only through the move (see C1).

Lexical hits to resolve in the lint, all benign:
- Inside quoted report names: "never" (R6, R24, R57), "keeps" (R15, R36, R48, R62, R84), "does not" (R29, R37), "do not" (R40, R64, R89).
- Conditions on a required write: "no assignee" (R1, R66, R70), "no priority" (R66, R69), "none after it" (R121), "not Passed" (R95–R104).

### G. Weights

Label check: every justification's label (Lookup / Interpretation or Calculation / Multi-source) matches its weight on all 121 rows.

| Rows | Weight | Verdict |
|---|---|---|
| R1 | 1 | Right for the lookup; the row is a bundle (B). |
| R2, R3 | 5 | Right: each area is Open only through one traced report (ZOM-586 note; the chat ok on a feature build). |
| R4 | 3 | Right: row 4 is plainly open. |
| R5–R7, R9, R11, R13, R26, R27, R29–R31, R33, R35, R37, R39, R42 | 5 | Right: sheet cell, legend, Arthur's rule and the #builds branch, plus a chat, PR comment or later sighting. |
| R43 | 5 | Right, given the DM must be found. Makes R68 inconsistent. |
| R8, R12, R14, R15, R20, R23–R25, R32, R34, R40 | 3 | Right: one row with no fix and no pass. |
| R10, R16–R19, R21, R22, R28, R36, R38, R41 | 5 | Right. |
| R44–R65 | 3 or 5 | Right; each mirrors its state row. |
| R66, R71, R78, R86 | 5 | Right: joins across sources. |
| R67, R69, R70, R74, R75–R77, R85, R91, R92 | 1 | Right. |
| **R68** | 3 | **Re-band to 5.** It cannot pass without finding Marcus's DM under the note's scope sentence; R43 and R82 are 5 for the same discovery. |
| R72, R73, R84 | 5 | Right: a blank Ticket cell against Vincent's note on an older ticket. |
| R79–R83, R87 | 5 | Right. |
| **R88 / R89** | 5 / 3 | **Inconsistent.** Both are open Level-end rewards rows; neither depends on its own status (row 6 is not Passed either way). Both hinge on the changed agenda (Sep 29 DM and invitation against the updated invitation and the card). Make both 5. |
| R90 | 3 | Acceptable; 5 is arguable, since the reason sits in a Slack thread reply. |
| R93, R94 | 5 | Right. |
| R95, R97–R99, R101–R103 | 5 | Right: each count moves with one traced status. |
| R96, R100, R104 | 3 | Right: the count is the same whichever way the hard rows fall. |
| R105–R111 | 1 | Right. |
| R112–R116 | 5 | Right. |
| R117–R120 | 5 | Defensible. A reviewer may call the slide a copy of the DM numbers (weight 1). Risk; keep 5 and be consistent with the new slide row (A1). |
| R121 | 1 | Right. |

One to two rows one level off (R68, R89): under 10%, none two levels off.

### H. Category, phrasing, sampling

- **Category.** 120 Outcome, 1 Process. R121 passes the three-condition test: the prompt says "Once that's done, message him", and no Outcome row can see order. No write is labelled Process.
- **Title pattern.** All 121 start "The Agent". No "The Agent's …" possessive, no ranking word, no "such as / e.g. / for example" in any field, no tool name (Linear, Slack and Drive are service names).
- **Off-pattern, risk.** "The Agent has ZOM-… in the state …" on 22 rows (18%) is a state of the ticket, not an action. If a reviewer calls it nonstandard, 18% is over the 10% band. The C1 repair removes it.
- **Sampling.** Each sampled group has five or fewer samples and a volume row:

| Sampled property | Samples | Volume row | Selection |
|---|---|---|---|
| Child states | R2–R4 | R1 | Good: two hard, one ordinary |
| Sub-issue parent | R67, R68 | R66 | Missing the wording traps (rows 9, 25) |
| Sub-issue priority / assignee | R69 / R70 | R66 | Fine |
| Moves | R72–R74 | R71 | Good: both found tickets and one ordinary |
| Sheet Status | R79–R83 | R78 | Good |
| Sheet Ticket | R84, R85 | R78 | Missing a new sub-issue key |
| Sheet Review list | R87–R89 | R86 | Good; see D2 |
| Sheet Why | R90, R91 | R78 | Fine |
| Areas Status | R93, R94 | R92 | Good: the two hard ones |
| Sheet Area | none | R78 | Missing (A3) |
| Note why | none | none | Missing (A2) |

- **Exhaustive families.** Sub-issue states (17), ticket states (22), note statuses (22) and open counts (10) are complete, not sampled. The rule allows it (`rubric_sampling.md`: "no … requirement to shrink an otherwise valid exhaustive rubric"; Eval 3 §1.4: "Per-ticket statuses are separate outcomes"). A reviewer who reads them as samples would raise "rows beyond five in one group" as one Moderate group each.

## Predicted dimension scores

| Dimension | Prediction | Reason |
|---|---|---|
| Overall Rubric Quality | FAIL (1–2) | Majors: A1, A2, A3, R1, R66, R91; likely the 22 move-plus-state rows; Moderate: cascade C1 |
| Criteria Weights | NON-FAIL 4 | R68 and R89 one level off; 5 if fixed |
| Rubric Category Balance | 5 | 120 Outcome rows |
| Process Rubrics | 5 | R121 valid; no ordering check missing |
| Agent-Centric Phrasing | 5, with a risk of 1–2 | The 22 "The Agent has ZOM-…" rows |
| Negative Criteria | 5 | No idle-pass row |
| Predicted All-Fail gate | PASS | No row depends on absent data or a missing tool |

## The three changes that matter most

1. Add the missing rows: the review-list 7 on the slide, sampled "why" rows on the Linear notes, and Area-column samples in the Reports tab.
2. Rebuild the 22 existing-ticket state rows: eight plain "sets ZOM-n to <state>" rows, drop the fourteen that do not change, add "changes the state of exactly 8", and grade more moves on their own. This clears the cascade, the move-plus-state bundle and the "The Agent has …" phrasing together.
3. Split R1 and R66 down to their counts, fix R91 (and R90) so a valid why passes, and add the Level-end rewards count so the old agenda's coincidental 7 no longer passes the review-list control.
