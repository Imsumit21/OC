# Learnings from the eleven completed tasks, and how they bind this design

Written 2026-11-10, before `/create-scenario`. Sources: each folder's `README.md` under `Task_Authoring/support/completed_tasks/` (eleven folders), the earlier cross-task file in Owen's archive (`00_Completed_Task_Learnings.md`, eight tasks, measured from stored difficulty inputs), the root `learnings` file §1–62 and the session memory notes. Every number is measured on real Opus runs unless marked UNCALIBRATED. This file holds no prompt, Oracle Event or criterion text.

## Your targets for this task

Your words: "i want over 130 tool calls in each runs", "difficulty pass rate under 60%", "failuure pattern under 50%", "follow all other difficulty guidelines", "you can choose from your self which option is best fit".

| Target | Yours | Assignment gate | Design target |
|---|---|---|---|
| Counted tool calls | Over 130 in every run | Long Horizon ≥ 100 | Weakest of six runs about 150 or more |
| Corrected average | Strictly under 60 % | Hard: under 70 % | E[avg] ≤ 52 % |
| Largest failure pattern | Under 50 % of failing runs | At most 50 % | At most 2 of 6 runs alike |
| Everything else | All other guidelines | SD 0.10–0.30, fewer than 5 full passes, ≥ 2 patterns, ≤ 2 errored, six Opus 5.5 slots | All together |

## What the eleven tasks measured

| Task | Mode | Rows | Average | SD | Full passes | Counted calls | Under 60 %? | SD in band? | Every run over 130? |
|---|---|---|---|---|---|---|---|---|---|
| **Douglas beta sign-off** | medium | 76 | **56.3 %** | **0.117** | 0 | 163–238 | yes | yes | yes |
| Samuel ZM messages | medium | 153 | 70.4 % (local grade) | 0.065 | 0 | 177–197 | no | no | yes |
| Q4 commitments | easy | 102 | 71.0 % | 0.016 | 0 | 151–212 | no | no | yes |
| Bridge pipeline | medium | 40 | 77.7 % | 0.106 | 1 | 109–150 | no | yes | no |
| Card spend | medium | 63 | 78.3 % | 0.054 | 0 | 554–573 | no | no | yes |
| Vincent ZM QA gate | easy | 67 | 78.3 % | 0.049 | 0 | not stored | no | no | not stored |
| Account handover (Normal) | medium | 37 | 80.8 % | 0.161 | 1 | 68–100 | no | yes | no |
| Robert LLC | easy | 130 | 83.6 % | 0.103 | 1 | 149–162 | no | yes | yes |
| Julia ZM baseline | medium | 81 | 83.8 % | 0.099 | 1 | 357–1,209 | no | no | yes |
| Owen DD carry-over | medium | 138 | 84.3 % | 0.029 | 0 | 230–326 | no | no | yes |
| Robert close-out | easy | 136 | 85.7 % | 0.034 | 0 | 116–143 | no | no | no |

**Only one task of eleven has ever averaged under 60 %, and it is also the only one that met all three of your targets at once.** Douglas's weight split was 44.6 % always passed, 29.0 % mixed, 26.4 % always failed (17 all-fail rows, all valid). That split is the model for this task.

## What landed and what leaked, by carrier

| Carrier | Measured | Task |
|---|---|---|
| Inline PR review comment | 0 reads in 12 runs; landed in all 6 baselines | Owen, Douglas |
| Mail no search returns | 0 of 8 runs; missed 5 of 6; most runs missed the vendor mail | Owen, handover, Vincent |
| 1:1 chat the run was not pointed at | 0 of 12 | Owen (Marcus's chat) |
| Chat in another language | Most runs missed it | Vincent (Turkish) |
| Reply under an unrelated post | 2 of 8, 3 of 6, 1 of 6 caught | Bridge, Owen |
| Later post in another channel | 0 of 7, then 3 of 6 caught | Bridge |
| Confluence page comment | Missed | Douglas |
| The rule owner's own chat | Read by 6 of 7 runs, swept by date with no keyword | Owen |
| Linear comments on listed tickets | Read on every ticket | Owen, Robert |
| Rule in a doc every run reads; a rule doc that names sources | Leaked every time | Handover, Robert, Samuel |
| Same-thread correction, visible caveat | Leaked | every task |
| Judgement after retrieval | 0 landings in 28+ runs | Julia |
| A done claim against a stated rule | Caught | Bridge |

## Rules this design takes from them

1. **The average needs an always-fail floor.** Under 60 % took 26 % always-fail weight on Douglas. This design plans four near-certain channels on four carriers, so the floor alone sits near 57 %.
2. **The spread needs heavy rows that about half the runs miss.** Universal misses add none (Owen 0.029, Q4 0.016). The largest spread a design can show is about half the gap between its best and worst plausible run.
3. **Runs behave alike.** Most carriers are read by every run or by none. The ones that varied inside a batch were records a keyword search returns for some words and not others, and records past a paging boundary. Lottery channels are placed that way on purpose.
4. **Carriers by one author act as one trap.** Runs sweep the rule owner by date. No two channels here share an author, and the requester writes no correction.
5. **The weakest run is set by writes.** Reads fell to 54–81 on list tasks. Tasks with 80 or more per-item writes cleared 130 in every run; Bridge's 53–55 left a 109 run. This design plans about 88 writes that happen whichever traps land.
6. **Rubric growth is the biggest threat to both targets.** /rubric gives a row to every write whose content differs by target (Owen 61 → 138 rows, LLC 73 → 130), and each always-pass row lifts the average and flattens the spread. High-count writes must be template-identical so they are sampled. The reply carries counts, never a member list.
7. **Score every placement on both gates together**: one pre-check run for /hardness, six runs for the baseline gates. Owen's rev6 fixed one and broke the other.
8. **A pre-check needs two independent causes, or a loss at least as large as the mode's.** One narrow miss scores 2.
9. **Unique Ground Truth is won before the SQL.** Vincent needed six /prompt rounds for lack of a rule-by-item sweep. Run it at revision 1, with a base contradiction scan on every seed that names a build, a version or a deploy.
10. **A touched known-data card fails coherence on presence.** Repair or stay off; never "accept".
11. **Keep the task's own keyword out of hidden corrections**, and never word a correction with a pointer's words.
12. **Persona owns every write target.** A share made the persona a reader at run time (Robert).
13. **At /rubric, apply the Fix List word for word**; check count-plus-identity, two artifacts in a title, cross-service order rows and names only in the evidence before the first run. Diff the builder export field by field (two mistyped weights moved Bridge's SD from 0.106 to 0.098).
14. **At /oe, no value seen only in run output**, no Gmail attachment read.
15. **A failed batch is not always a rebuild.** Bridge failed patterns on one batch and passed every gate on the next with the same SQL. A spread ceiling, though, cannot be re-run away (Owen).

## Originality

No cohort, rule vocabulary, record set or wording is copied from these tasks. Three of them use Zombie Match engineering records (Vincent, Douglas, Julia); this design's population (main-menu flows and the reports against them) and its output (an epic) are different. The platform's duplicate score cannot be measured locally.
