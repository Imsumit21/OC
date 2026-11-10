# All-fail rows R25 and R58: fairness, readability and grader accuracy (rev7, batch 2)

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal). Universe manifest: `Evals/references/universes/normal/universe_manifest.json`.

R25: the sheet shows 959,342.64 as the Domino Delights build cost. R58: the #winddown reply gives 959,342.64 (or a
rounding to $1K or finer) as the Domino Delights build cost. Both are weight 5 and both failed all six runs.

## What each run wrote

| Run | Sheet total (event) | Reply (event) | Short of or over truth by | Cause |
|---|---|---|---|---|
| run-1 | 963,374.64 (formula at 575, read back at 581) | $963,374.64 (650) | +4,032.00 | MotMot wire to 8605 kept in |
| run-2 | 955,849.64 (413, 416) | $955,849.64 (481) | +4,032.00 − 7,525.00 | MotMot kept in, Lucas transfers left out |
| run-3 | 951,817.64 (363) | $951,818 (426) | −7,525.00 | Lucas transfers left out |
| run-4 | 951,817.64 (393) | $951,817.64 (454) | −7,525.00 | Lucas transfers left out |
| run-5 | 951,817.64 (377) | $951,818 (438) | −7,525.00 | Lucas transfers left out |
| run-6 | 951,817.64 (678, 687) | $951,817.64 (747) | −7,525.00 | Lucas transfers left out |

Every gap is exactly one or both of the two designed adjustments. No run made an arithmetic slip, and the full
22-payee diff (`register_diff.txt`) shows no other difference from the truth register in any run. The ZM and Combo
Fighter totals (R26, R27, R59, R60) are right in all six.

## Grader accuracy

The judge's text for R25 and R58 in each run names the figure the run wrote and matches the payload above. No judge
concedes the true figure and fails the row. R58's title lists the wrong figures it rejects ($952K, $963K and others);
each run's figure is on that list or outside the $1K rounding of 959,342.64. Verdict: graded correctly, six of six.

## Fairness

- **The total is asked for.** The prompt asks for "what each bet cost us to build" on the sheet and in the reply.
- **Both adjustments are incorporated.** The prompt delegates the counting to Leonard's doc ("He laid out how he wants
  it counted"). The doc says a notice counts unless one of the founders has said the money came back, and that a
  contractor paid some other way counts if a receipt reached Robert's mail, at the amount sent.
- **One value fits the records.** MotMot: one wire of 4,032.00 to account 8605 on Apr 2 2024 came back and was
  re-sent to 3341 (Leonard's message, SQL line 52). Lucas: five Western Union transfers, 1,075.00 three times and
  2,150.00 twice, 7,525.00 sent (run-1 read all five receipts at event 500 and the verifier passed its 13,975.00).
- **No fair alternative is rejected.** The rows accept any label naming the build cost and any rounding to $1K or
  finer. 963,374.64 and 951,817.64 are not alternative readings; each leaves one incorporated adjustment out.
- **Not one run's quirk.** Five runs missed Lucas and two missed MotMot; no run found both, so the rows fail on two
  different root causes. Across the 13 runs on rev7 (see `rates_and_gates.md`) one run, batch 1 r5, had both
  adjustments right, so the rows are passable.

Verdict: valid all-fail rows. They are a cascade: each is the sum of decisions that already have their own rows
(R7, R8), so a single miss costs the cell row, the comment row, the order row and these two.

## Readability (could the persona's tools return the deciding records?)

- **MotMot.** Robert is a member of the founders' channel `C04UEQVDVB7`. Four runs got Leonard's message from one
  Slack search: run-3 event 259 (query "wire came back"), run-4 event 344 ("wires"), run-5 event 267 ("wires"),
  run-6 event 458 ("came back"). The two runs that missed it never searched Slack for a return (run-1: only a Gmail
  search at event 205; run-2: none).
- **Lucas.** The five receipts are in Robert's own mailbox (base Gmail threads `robert@harmonygames.co/1800906573953663690`,
  `…/1802093473277810505`, `…/1803224093176618488`, `…/1805405814137504108`, `…/1808201960854294221`, re-read through
  `hg.py`). Run-1 read them through ordinary Gmail calls (events 440 to 500). In the five runs that missed them the
  searches that could have reached them returned a first page of 50 or 100 bare ids, newest first, with a next-page
  token that was not followed, and none of those ids was opened (run-2 events 169, 171, 338; run-3 153, 171, 276;
  run-4 163, 304; run-6 157, 189, 351, 388). Run-5 made no search aimed at Lucas. The tool returned what it promises.
  A search on the payee's name alone, or on "Western Union", was open to every run and none of the five made it.
- **Pointers seen and passed by.** Runs 4 and 5 received Robert's own DM line "Western Union? Or wire?" (Oct 22 2024,
  the day before a Lucas notice) inside a Slack search result (events 344 and 267) and did not follow it.
- **A caution on evidence.** The wide Gmail search `"Payment Processed"` matched 434 messages in every run, and the
  five receipt ids are in that result. The result spilled to a file; the model saw a stub or printed only the first
  entries. The export keeps the full spilled result, so a text match on that event does not show the model read it.

Verdict: both deciding records were readable by ordinary calls. The misses are retrieval failures by the run.

## Unconfigured tool behaviour that touches these rows

`=SUMIF(...)` evaluates to `#NAME?` in the Sheets service (run-3 event 354). Run-3 read the cells back, saw it and
replaced the formulas with `=SUM(...)` (events 358, 360), so no row was lost. A run that leaves `SUMIF` in its total
cells without reading them back would fail R25, R26 and R27 for a tool reason; that would be a confounded failure,
not a difficulty. It did not happen in this batch.
