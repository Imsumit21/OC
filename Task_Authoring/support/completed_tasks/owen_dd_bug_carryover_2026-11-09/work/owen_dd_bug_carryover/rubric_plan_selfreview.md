## Self-review

**0. /rubric round 1 taken in.** The platform's /rubric (FAIL 1 on the reviewed JSON 2ed7a6489798; report kept as run_forensics/rev9/3_rubric_FAIL1_r1.md) returned a checked Fix List. This plan applies it row for row:
- R1 became the template volume row @@P:new_count@@; R2–R7 were deleted, and seven per-field samples were added (@@P:prefix:In profile@@–@@P:desc:In chapter selection@@).
- The state rows R8–R28 name each issue by its line or post (@@P:state:offers has no visuals@@–@@P:state:android bottom bar invisible@@). R8, R12, R21, R26, R27 and R28 were reweighted, and R19, R23 and R28 were rewritten.
- The 47 ticked lines whose tick stands each have a row (@@P:state:When I start the game on ios I got@@–@@P:state:and activate pop up has the wrong price tage@@).
- The move sample ENG-2425 was swapped for ENG-2433, and R35 and R36 went to weight 3.
- The hold rows grade "the ticket stays open" at weight 5 (@@P:hold:ENG-2434@@–@@P:hold:ENG-2437@@). R40 and R41 needed my own rewrite; both are at 5, as the Fix List recommends.
- R42 became one build-line row per child (@@P:line:ENG-2434@@–@@P:line:ENG-2435@@, plus @@P:line:ENG-2409@@ at 3).
- The sheet rows name "the DD carry-over sheet" (only @@P:sheet_folder@@ names the folder). R46 and the Outcome and Ticket rows are at 5, R49 was deleted, and four cells were added (@@P:sheet_outcome:sides@@, @@P:sheet_outcome:apple@@, @@P:sheet_why:tavern@@, @@P:sheet_why:sides@@).
- Rows changed: @@P:reply_thread@@ is thread-only, and @@P:reply_broken@@ is a bare 9. @@P:reply_after_writes@@ is at weight 1.

Rows the Fix List leaves alone are byte-identical to the reviewed JSON (R29–R33, R44, R59, R60), so the DELTA locks hold. My local-round changes on cee09a260a85 that the Fix List did not ask for were reverted to the reviewed form; that drafted file is kept as plan/09_Rubrics.prev_cee09a260a85.json.

**1. Re-read as /rubric** (3_Rubrics_Eval.md 1.4 and 3.1, in order, against this plan).
- Every prompt requirement has a row on its own artifact:
  - the Linear tickets: the template volume row @@P:new_count@@, one sample per template field (@@P:prefix:In profile@@–@@P:desc:In chapter selection@@), one state row for each of the 68 new issues, and the two Covered notes @@P:covered:apple@@ and @@P:covered:signin@@;
  - the UI tree: the move count @@P:moves_count@@, five move samples, and the five holds as "stays open" lines;
  - a line on every child: one build-line row per child (28);
  - the sheet in the folder: @@P:sheet_folder@@–@@P:sheet_why:sides@@, with the Outcome, Ticket and Why cells sampled under the row count @@P:sheet_rows@@;
  - the shares: @@P:share:arthur.blake@harmonygames.co@@–@@P:share:oliver.brooks@harmonygames.co@@;
  - the reply in the DM thread @@P:reply_thread@@ and its three numbers @@P:reply_broken@@–@@P:reply_done@@;
  - the order ("Then reply"): @@P:reply_after_writes@@.
- Every write OE maps to a direct row or a population control (§B). Only template-identical writes are sampled: the template fields of the creations, the moves and the sheet cells. Each is under a volume row that states the template.
- The told facts (how many still broken, how many new tickets, how many of the 28 children Done) each have a reply row.
- No exclusion row.
  - The holds are graded as the line the Agent must write on each held child and as the exact move count.
  - The Covered lines are graded as the note on the covering ticket and as the sheet's Ticket and Outcome cells.
  - "No assignee" and "an empty description" are graded on a named issue the Agent must file (@@P:assignee:top hud@@, @@P:desc:In chapter selection@@), so an idle Agent fails them.
- Friction: none.

**2. Counter-readings per row.**
- (a) Can a valid answer fail a title naming exactly these values?
- (b) Can a wrong answer pass?
- Each is resolved with a record, a rule § or a risk number.

@@TABLE@@

**3. Re-verify.**
- Every value in §A was re-verified in this run through tools/hg.py:
  - plan/oe_reads.py re-read the canvas channel's month file (272 records) and the bug channel's Nov, Dec and Feb files whole;
  - it also read the single posts by lookup + get-many, 40 Linear issues field by field, PRs #1905, #1908, #1913 and #1916, the merge commit, the three contacts and the economy doc;
  - this is the read behind the /oe-passed OEs (sha a9bbea55e7c3).
- The thread closes the Fix List's weight-3 rows rest on were re-read from that hg.py read: CE156FDFB428/1763606525.993489 (offers, 'This should be fixed now'), CE156FDFB428/1763074145.483099 (level completed, 'it looks good') and CE156FDFB428/1763747143.093969 (saga map, 'OK I pushed the fix').
- Seeded values were read from 01_Universe_Inject.sql statements (L3, L16, L55, L58, L60, L62, L64, L66, L68, L69, L70, L72, L74, L76, L78, L80, L115, L203, L206, L208, L215, L216, L281, L309, L311, L314, L316, L325–L335). No SQL was executed.
- Recomputed:
  - 63 lines + 7 posts = 70, and 70 − 2 Covered = 68;
  - 52 tick-stands lines + 1 tooltips line + 5 posts = 58 Done, of which 5 + 47 are lines whose tick stands;
  - 7 Bugs and 3 Canceled; 7 + 2 = 9 still broken;
  - 19 open − 5 held = 14 moves, and 9 + 14 = 23 of 28;
  - 22 + 5 + 1 = 28 build lines.

**4. Predicted all-fail re-check.**
- Every row's values are reachable by Owen through cataloged tools. The visibility proof above re-runs persona_view on every scoped id behind every cited F-id.
- No row needs a record outside his view, a filter a tool lacks, or a retry.
- Predicted all-fail rows: 0.
- Over-specific risks are kept open:
  - the state rows accept the issue "whatever its title";
  - any share role passes;
  - Bugs or Broken, and Canceled or Gone, pass on the sheet;
  - any wording of a "stays open" line or a Why passes.

**5. Baseline cross-read (advisory, not used to pick rows).** In the two rev9 baseline batches (12 runs, hand-graded in run_forensics/rev9/baseline/summary.md):
- every run misses the Apple and Tavern items;
- the runs split on the popups and the shop icons.

No row was added, dropped or re-weighted for that. Every row change comes from the /rubric Fix List.

**6. Record.** 138 rows (137 Outcome, 1 Process), weighted by the kind of work. Prompt spans are exact, every F-id is in the ledger, and predicted all-fail is 0. Unresolved: none.
