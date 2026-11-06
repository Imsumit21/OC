## Self-review

**1. Re-read as /rubric** (3_Rubrics_Eval.md Phases 1–5, in order), with the pre-verdict sweep (5.0).
- **Sweep.** No item remains on any of the eight sweep checks:
  - a missing requirement (Coverage table: all covered);
  - a phrasing mismatch with the prompt;
  - a non-atomic row (P35's header row is one tool output);
  - a category mislabel (one Process row, for "Then reply");
  - an over-specific or hard-coded title (labels, dates and folders accept every fair form);
  - a duplicate or cascade group (the thread is graded once in P71);
  - a vague exemplar (lint 0);
  - a prohibition-only title (an idle Agent fails every row).
- **Calibration.** Checked against the 7-row table in Evals/references/rules/rubric_qc_examples.md:
  - do-nothing: every row needs a write;
  - valid case and count format: the counts P5, P27, P36 and P68 are bare;
  - LITERAL keys: ENG ids, thread_ts 1770961200.890407;
  - PT/UTC day: no row grades a record's day, and the semantic dates Feb 28, Mar 1 and Mar 3 are date-only;
  - reachability: every deciding source is PROMPT_LINKED;
  - anonymized tokens: none graded;
  - OE conflict: the OE path (OE 100: top level of Robert's Drive) passes P34.

**1a. /rubric round 1 applied.**
- Every Fix List row was copied byte-exactly; the script check found 82 of 82 titles and weights.
- The 43 reviewed rows it did not name are byte-identical to the reviewed JSON (run_forensics/rev4/rubric_r1/09_Rubrics_reviewed_8296aaf8dc71.json).
- Its non-failing wording repairs are made: the work-kind labels, R1's Accept note, R35's '/oe note 1', and R16's unrelated citation.
- New-row evidence names deciding records that Robert can reach: seeded mails, Slack replies and the ground rules; base #winddown and #prototype posts; and the issue's own comment.
- One wording change from the reviewer's candidate: three quotes of the #winddown action items replace 'such as' with '...'. The candidate's evidence text was not shared with us, and the lint's vague_exemplar check matches 'such as' even inside a quote.

**2. Counter-readings.** The table below has one row per criterion C1…C73:
- false negative: a valid alternative the title might reject;
- false positive: a plausible near miss it might pass.
Each row's Resolution names the records and pointers. For the round-1 findings (section 'Round history and residual risks'), the strongest case each was a false positive:
- the HG labels: "HG" is the draft's own word;
- the owner rows: Owner duplicates the Linear assignee;
- the core comments: the calls are graded on the sheet.
Each was resolved for coverage, not against it. rubric_sampling ("distinct requested property/column", "never spot-check a core requirement") and the Q4/Samuel /rubric rounds (a row per surface) settle these.

**3. Re-verify.** Every value a clearance depends on was re-verified in this run through tools/hg.py and the parsed SQL:
- the rubric-writing gate's v3.rubric_evidence re-read each cited field: base Slack posts and Contacts through hg.py get-many; seeded Slack, Gmail, Docs and Drive rows from 01_Universe_Inject.sql;
- plan/oe_reads.py re-read the 25 Slack posts, the 194 REVENUE_DAILY rows, the Drive root, two contacts and three Linear users;
- the blind reviewer independently re-read the 37 issues and comments, the four mails, #winddown /51–/204, the #prototype roots, and REVENUE_DAILY and REVENUE_DAILY_V2. It found every literal correct;
- arithmetic: 140 + 62 + 3,000 + 100 + 100 + 48 = 3,450; 3,450 / 3 = 1,150; 1,150 − 248 = 902.

**4. Recount.**
- Findings on the current JSON: 0. The 16 round-1 items are fixed.
- Overlap groups: 0.
- Predicted all-fail: 0.
- Every spot-check group holds five or fewer samples: the sheet's Decision cells (D3, 4), By cells (D4, 2), Owner cells (D5, 2), and Paid by / Game cells (D6, 4). Linear comments and states are graded one row per issue.

**5. Fixes.**
- Each round-1 fix rests on a record re-read in this run:
  - SQL L45, L51, L68, L92, L100;
  - C09UHHN6PFZ/1770844309.583109;
  - #prototype /389–/391;
  - the draft's grid, SQL L23;
  - the ground rules, SQL L15.
- The rubric and plan are rebuilt from plan/rubric_rows.py and plan/rubric_titles.py.
- Dated copies of every build are in run_forensics/rev4/rubric/. The current one is sha @@SHA@@.

**6. Stage gate.** The paste follows. The gate recomputes the criteria count, verifies the quoted spans, the issue types and the dimension table, and applies the binary validity gate.

Unresolved: none.
