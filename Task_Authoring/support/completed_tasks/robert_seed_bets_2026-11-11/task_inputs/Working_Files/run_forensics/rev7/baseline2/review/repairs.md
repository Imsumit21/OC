# Repair proposals for the pattern gate (rev7 baseline, batch 2): proposals only, S0r and the owning stages decide

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal). Universe manifest: `Evals/references/universes/normal/universe_manifest.json`.

## What has to change

The platform's failure-pattern rule fails when more than half of the failing runs lose the same rows. On rev7 the
Lucas miss (OFF) happens in about three runs of four and nothing else splits those runs:
- RET is missed in about one run of four and shares the two total rows with OFF;
- CORR owns the most weight (16) and is missed one run in thirteen;
- ALIAS is missed about one run in three and owns a single row, so a run that adds it stays in the OFF pattern;
- ORPH, CLASS, CURR and Oleg were never missed.

Making OFF easier is the wrong lever: the average is 85.7% against a cap of 90%, and at a 50% miss rate for OFF the
average clears the cap in only about half of simulated batches (`rates_and_gates.md` section 5). What helps is a
second decision that fails often enough on rows of its own.

No proposal adds a payee, an issue, a step, a write or a prompt rule.

## P-NODE (rubric stage): grade where the Node Media dollars sit

- **Now.** R12 grades the Bucket cell of the `PERSON_4419_NAME LLC` line. Nothing grades the line's dollars.
- **Observed wrong outcome.** Run-5 wrote bucket Company and put 16,428.57 in the Company column (event 377). The three
  batch-1 runs that missed the alias did the same (`rates_and_gates.md` section 4). The five runs that resolved the
  alias put 16,428.57 under Domino Delights.
- **Proposal.** One Outcome row for the dollars cell of that line: 16,428.57 in the Domino Delights column, with the
  Company and ZM columns failing. The fact is its own: the single notice is dated Jan 2 2025, six days inside the
  Domino Delights window, and the method lists Marketing under its bet.
- **Why it is coverage and not a split of R12.** The rubric already grades two cells for the other payees a rule
  singles out: JPMorgan (R9 dollars, R10 bucket), Brooks (R13 bucket, R20 dollars), Martin (R14 bucket, R15 amount),
  and for Adjoe (R19 dollars, R22 bucket). Node Media is the one such payee with only its bucket graded.
- **Effect on this batch.** Run-5 would fail two rows that runs 3, 4 and 6 pass, so it becomes its own pattern:
  {3, 4, 6}, {5}, {1}, {2}. The largest is 3 of 6, which is exactly 50% and passes. The other five runs pass the new
  row on their current sheets. No new baseline is needed for a rubric change, only the verifier re-run.
- **Effect on a fresh batch (advisory).** 65% to clear the pattern, average and full-pass gates, against 32% today.

Attack and answer:
1. *It is tuned to the baseline.* True in timing: the gap was noticed because of the gate, and its effect on the
   gate is known in advance. The playbook forbids deleting, softening or re-weighting rows to move numbers, and the
   Mode B routing table warns against cosmetic splits. The row stands only if the rubric stage accepts it as coverage
   on its merits. That decision belongs to the user and `/create-rubric-writing check`, not to this report.
2. *One decision, two rows.* A run that mislabels the bucket will usually misplace the dollars, so the rows move
   together. That is also true of R9 with R10 and R13 with R20, and it is within the rule that one fact may not sit in
   three or more rows.
3. *Sample cap.* The dollar-figure group already holds its five spot checks (R16 to R20). The new row has to enter as
   an exception row for a payee the method singles out, like R6 to R11, not as a sixth sample.
4. *A new row is a new finding surface.* Each /rubric round so far has raised a finding on a row changed in the
   round before. The
   last stored report is round 3 (FAIL 2 on ba1f9ca2ee1c, R33 only); no report for the current 923f89f3ac9c is in
   `plateform_reports/`, so a /rubric run is owed in any case.
5. *It does not fix the spread.* Correct. Spread stays near 0.03.

**Outcome (2026-11-10).** The user chose P-NODE. Answer 3 above was wrong: platform /rubric round 10
(`plateform_reports/6aeed82596dcfe103f9f74d9_3_rubric-10.md`, FAIL 2, one Moderate) counted the row as a sixth
ordinary sample, because its figure equals its notice, and found nothing else on it. Its stated alternative was to
keep the row and drop the 500.00 sample (old R17, the 4X helper); round 2 had already suggested swapping Node Media
into the amount group. That swap is applied: `09_Rubrics.json` is 73 rows, weight 167, sha256 b182d5186aac, equal to
the reviewed file with old R17 cut out. Old R18 to R74 are now R17 to R73, so the all-fail rows are R24 and R57.
Projection on the six runs is unchanged in shape: {3, 4, 6}, {5}, {1}, {2}, largest exactly 50%, average 85.5%.

## P-CORR2 (universe, next revision): take the bank tokens out of the Chase records mail

- **Now.** Arthur's mail of Feb 13 2026 names the payee and the account: "the $4,000 to JPMorgan ***3203 on the SVB
  notices in Aug 2024 was me. That was our own Chase account" (SQL lines 65 to 73). The ENG-2450 note says Leonard
  cannot place the payment, which sends every run looking.
- **How the runs settled it.** One Gmail search on a token from the issue, then one read: run-2 event 154 (`3203`),
  run-3 event 297 (`"3203"`), run-4 event 136 (`JPMorgan OR Chase 3203`), run-5 event 224
  (`3203 OR chase OR JPMorgan`). Run-1 (event 239) and run-6 (events 226, 247) met the mail in a sweep of recent mail.
- **Proposal (v2 move: the deciding fact behind an alias).** Arthur's mail says what he did without the notice's
  words: the amount, the month, SVB to "our Chase account", Carta's renewal. It no longer carries "JPMorgan" or
  "3203". The join is then the bank's two names (JPMorgan and Chase), the amount and the month. The subject
  "Chase records", the sender, the date and Leonard's reply stay.
- **Fair discovery path.** The method doc itself names Chase ("Anything paid out of Chase isn't in here") and says a
  transfer between the company's own accounts is not spending. The mail is addressed to Robert, one day old, in his
  inbox. A search on Chase, a look at recent mail, or a search on the amount with the month reaches it.
- **Facts it would change.** The body of one seeded mail (three mailbox copies). Oracle Event 19 quotes that body and
  reaches it by searching "JPMorgan". The evidence text of R9, R10 and R34 may quote it.
- **Effect (advisory, catch rate unmeasured).** Two of six runs searched only the account number. If CORR were missed
  in one run of four, the gates clear in about 58% of simulated batches, and 81% together with P-NODE.

Attack and answer:
1. *Runs that include "Chase" in the query, or sweep recent mail, still find it.* Yes: four of six in this batch
   would. The move aims at a miss rate near one in four, not at a wall. A stronger form, a confident wrong note on
   ENG-2450, risks the opposite failure: most runs take the note at face value, and "Lucas and JPMorgan both missed"
   becomes the new dominant pattern.
2. *Coherence.* Leonard's note (Feb 12, 4:26 PM PT) comes before Arthur's mail (Feb 13, 8:26 AM PT) and his reply
   (9:08 AM PT), and that order stays. The body edit must keep "Aug 2024" and "$4,000", or the mail no longer
   identifies the payment. Whether any other record ties account 3203 to Chase was not censused here; S0r should
   check before adopting.
3. *Cost.* A universe change re-opens /injection, /prompt, the Opus pre-check with /hardness, /oe, /rubric and the
   six-run baseline. Two platform pre-checks are already spent on this scenario (rev6 HOLD, rev7 score 3).
4. *It does not fix the spread.* Correct. With CORR at 40% and P-NODE the simulated spread reaches the band in 9% of
   batches.

## Considered and not proposed

- **Reword Leonard's 8605 message so "came back" and "wire" no longer match.** It would raise the RET miss rate from
  about one in four toward most runs, and "Lucas and MotMot both missed" would then be the dominant pattern.
- **Restore a pointer on ENG-2447 so more runs find the receipts.** It lowers the one loss that keeps the average
  under the cap.
- **Move the Leapblock close-out off Slack.** Never missed in 13 runs, but its wording took three SQL revisions to
  pass /prompt; the risk to a settled record outweighs an unmeasured gain.
- **Re-weight or drop the two total rows, or the order rows R68 and R69.** They are valid rows; changing them to move
  the spread is tuning.
- **More payees, issues or notices.** Volume. Six runs brute-forced 132 notices and tied to Leonard's quick pass to
  the cent.

## Not a repair: re-running rev7 unchanged

The simulated chance that a fresh batch clears the pattern, average and full-pass gates is about one in three. Both
batches so far failed the pattern rule the same way (four of six runs in the Lucas pattern).
