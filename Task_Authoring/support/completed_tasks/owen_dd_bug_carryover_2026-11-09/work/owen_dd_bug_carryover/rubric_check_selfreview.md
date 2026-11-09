## Self-review

**1. Re-read as /rubric** (3_Rubrics_Eval.md Phases 1–5, in order), with the pre-verdict sweep (5.0), on the round-1 rebuild.
- **Sweep.** No item remains on any of the eight sweep checks:
  - **A missing requirement.** The 52 outcomes the round-1 report listed are rows now:
    - the 47 ticked lines;
    - the Why column (@@P:sheet_why:tavern@@, @@P:sheet_why:sides@@);
    - the Fixed and Covered Outcome cells (@@P:sheet_outcome:sides@@, @@P:sheet_outcome:apple@@);
    - no assignee (@@P:assignee:top hud@@) and an empty description (@@P:desc:In chapter selection@@).
  - **A phrasing mismatch with the prompt.** Titles use the prompt's and the notes' own words ('[2231]', 'Bug, Outcome, Ticket and Why', Done / Bugs / Canceled, 'in the thread of his Feb 12 DM').
  - **A non-atomic row.** The bundles are gone:
    - the count rows R6 and R7 are deleted;
    - @@P:new_count@@ is the single volume row that states the template;
    - each template field has its own sample, each child its own build-line row, and each hold one 'stays open' row;
    - @@P:sheet_ticket:sides@@ grades one Ticket cell.
  - **A category mislabel.** One Process row, @@P:reply_after_writes@@, for 'Then reply'. The other 137 rows are Outcome.
  - **An over-specific or hard-coded title.**
    - The state rows accept the issue 'whatever its title'.
    - Lines that end in a mention say so ('it ends with a mention of Arthur Blake / Owen Baker').
    - The hold rows no longer require a reason.
    - Bugs or Broken, and Canceled or Gone, pass on the sheet.
  - **A duplicate or cascade group.**
    - The '[2231]' cascade is gone: the state rows grade the state only.
    - The folder cascade is gone: only @@P:sheet_folder@@ names the folder.
    - The R42/R43 umbrella is gone: R42 is deleted.
  - **A vague exemplar.** None. The lint has no vague_exemplar hit.
  - **A prohibition-only title.** None. An idle Agent fails every row, and 'no assignee' and 'an empty description' sit on a named issue the Agent must file.
- **Calibration.** Checked against the 7-row table in Evals/references/rules/rubric_qc_examples.md:
  - **Do-nothing.** Every row needs a write or the reply.
  - **Valid case and count format.** The counts are bare or state the template, and no row grades a length, line or sentence count. The one format_lock hit is a quoted canvas line ('single character pages').
  - **LITERAL keys.** ENG ids, D05S1S2AB5M, PR #1913 and build 0.3.310 accept any rendering the tools return.
  - **PT/UTC day.** Arthur's DM is Thu Feb 12 2026 3:10 PM PT, which is Feb 12 23:10 UTC, the same day in both.
  - **Reachability.** Every deciding source is PROMPT_LINKED. The rubric-writing gate's v3.rubric_evidence re-checks each path.
  - **Anonymized tokens.** [PERSON_NAME_1711], [USERNAME_20421] and [USERNAME_20422] are the source lines' own strings. They are kept as shown, as in the Fix List.
  - **OE conflict.** The /oe-passed path passes every row. The report's one conflict, OE 71 vs R19, was settled against the row, and @@P:state:I found the issue lives are not decreased after@@ now names the trailing mention.

**1a. Round 1 taken in.** The report was /rubric FAIL 1 on 2ed7a6489798.
- Every Fix List row was copied in its checked text:
  - 90 titles and weights were diffed by script against the report, with 0 missing;
  - the one "needs your own rewrite" row (R40/R41 weights) is set to both 5.
- The current JSON was rebuilt on the reviewed JSON, not on the unreviewed local build cee09a260a85.
- The eight rows the Fix List left alone are byte-identical to the reviewed JSON: R29–R33, R44, R59 and R60.
- Each item is listed under 'Round history and residual risks' with its /rubric type.

**2. Counter-readings.** The table below has one row per criterion, C1…C138:
- false negative: a valid alternative the title might reject;
- false positive: a plausible near miss it might pass.

Each Resolution names the record and pointer. For the round-1 findings, the strongest case that each was a false positive was:
- 'the hold reason is the substance of the line';
- 'a volume row over 68 creations is the sanctioned control';
- 'the sheet's location belongs in every sheet row'.

Each was resolved for the report's ruling:
- Arthur's DM asks only 'saying where it landed';
- the creations carry distinct titles, so each is graded;
- a location condition embedded in 13 rows is a cascade.

**3. Re-verify.** Every value a fix depends on was re-verified through tools/hg.py and the parsed SQL:
- The thread closes behind the new weight-3 rows were read from the hg.py export (plan/oe_base.json): CE156FDFB428/1763606525.993489 (offers), CE156FDFB428/1763074145.483099 (level completed) and CE156FDFB428/1763747143.093969 (saga map).
- Builds #2297 (C05433XK267/1765310444.095399) and #2299 (C05433XK267/1765397569.397939) were read the same way.
- PR #1916 is merged into EconomyChanges (base_ref EconomyChanges, merged true), and PR #1913 is open.
- Slack ids: EMPLOYEE_0025_SLACK_ID is Arthur Blake and EMPLOYEE_0002_SLACK_ID is Marcus Bennett (the dossier's roster).
- The seeded records come from 01_Universe_Inject.sql statements; no SQL was executed:
  - L16: the notes' 'no assignee, nothing in the description';
  - L69: Brian's 'closing this one' with thread_ts 1766415326.501939;
  - L216: Brian's Trello closing rule 'every one gets a note naming the current public build'.
- Arithmetic:
  - 47 + 5 + 1 + 5 = 58 Done; 58 + 7 + 3 = 68;
  - 22 + 5 + 1 = 28 build lines;
  - 61 − 6 deleted + 83 added = 138 rows.

**4. Recount.**
- Findings on the current JSON: 0. The 18 round-1 items are fixed.
- Overlap groups: 0.
- Predicted all-fail: 0.
- Every spot-check group holds five or fewer samples:
  - G1a–G1g: 1 each, all sharing the control @@P:new_count@@;
  - G4 moves: 5;
  - G7 Outcome cells: 5;
  - G8 Ticket cells: 3;
  - G9 Why cells: 2.

**5. Fixes.**
- Each fix rests on the round-1 report's text and a record re-read above.
- The rubric and plan are rebuilt from plan/rubric_rows.py and plan/rubric_titles.py. Locked rows are copied from plan/09_Rubrics.prev_2ed7a6489798.json.
- The current build is sha @@SHA@@.

**6. Stage gate.** The paste follows. The gate recomputes the criteria count, verifies the quoted spans, the issue types and the dimension table, and applies the binary validity gate.

Unresolved: none.
