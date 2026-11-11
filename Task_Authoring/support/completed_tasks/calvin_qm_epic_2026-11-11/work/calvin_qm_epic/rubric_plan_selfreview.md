## Self-review

**1. Re-read as /rubric** (3_Rubrics_Eval.md 1.4 and 3.1, in order, against this plan).
- Every prompt requirement has a row on its own artifact (the /rubric round-1 Fix List applied row for row):
  - the children in Linear: ten create rows, two template spot checks under @@P:child_template@@, ten end-state rows;
  - the report lines in Linear: 17 create rows (title and parent) and 17 state rows for the new sub-issues with the template row @@P:sub_template@@; 22 move rows, 8 state rows for the tickets whose state changes, 22 note-status rows and 22 note-reason rows;
  - the stock-take sheet in the folder: @@P:sheet_folder@@–@@P:area_open_count:Card packs@@, with the Status, Ticket, Review list, Why and Area cells sampled and one open-count row per area naming its reports;
  - the shares: @@P:share:arthur.blake@@–@@P:share:vincent.parker@@;
  - the slide: @@P:slide_new@@ and its five numbers;
  - the DM message: @@P:dm_place@@ and its five numbers;
  - the order ("Once that's done"): @@P:dm_after_writes@@.
- Every write OE maps to a direct row or a population control (§B). Only template-identical writes and repeated cells are sampled, each under a volume row.
- The five told facts each have a DM row.
- No exclusion row. "No priority" and "no assignee" are graded on a named sub-issue the Agent must create, so an idle Agent fails them. The review-list sample on report 10 grades a cell the Agent must write.
- Friction: none.
- Weights follow the kind of work: 5 where the value joins records across services (a pass with the build's branch and Arthur's rule; a Fix cell with a review comment; a later sighting), 3 where the note's rule is applied to one sheet row or a count is calculated, 1 for a value copied from one record.
- Global duplicates: every status is graded at most twice (state plus note for a ticket whose state changes; state plus sheet sample for five reports without a ticket). Each of the five counts is graded twice (DM and slide); the sheet's marked rows are that column's own volume control, as the Fix List writes it.

**2. Baseline evidence taken in** (six Opus 5.5 runs on this SQL, graded by hand; Working_Files/run_forensics/rev3/baseline/calls.json). No row is written to fail a run. The rows that failed in all six runs are the states and notes decided by Arthur's review comments (harmonygames-Games/match3d#472#rc_1, harmonygames-Games/match3d#475#rc_1) and Oliver's comment (harmonygames-Games/match3d#473#c_2), plus the two counts they move; each cites its deciding record, which the persona can read. No row is predicted all-fail on the four Evals bases: every value is reachable.

**Re-verified.** Every expected value was re-read in this run, not taken from the ledger: seeded values from 01_Universe_Inject.sql (the SQL L-numbers in the ledger's Source pointer column), base values through tools/hg.py (plan/oe_reads.py → plan/oe_base.json: the 15 build posts, the chat lines, ZOM-543, ZOM-556, ZOM-560 and the four pull requests), and all 39 statuses, the area counts and the five numbers from solver/truth.json, which the platform /prompt and /oe reviews on this SQL both re-derived (10, 9, 20, 0, 7).

**3. Counter-readings, one per row.**

@@TABLE@@

Unresolved: none. Open points for check mode: /rubric may re-band the passed-report state rows (5 here, as a join of the sheet, #builds and Arthur's rule) and the note rows (same band as the state they repeat).
