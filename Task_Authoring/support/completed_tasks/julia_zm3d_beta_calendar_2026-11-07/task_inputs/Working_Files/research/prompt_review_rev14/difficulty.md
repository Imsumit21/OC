# Difficulty update: final SQL (revision 14)

SQL sha256 `edae63f3…8e13` (checked). Prompt `2a23afd8…` unchanged. Base for comparison: revision 8.

**Bottom line.** I now expect about **76% on the real verifier** (71% on the 30 slots), down from about 79%. Calls barely move. No run exists on this task, so this is still a forecast.

## What is measured and what is judgement

**Measured in this pass**
- No run exists: `06_PreCheck_Trajectory` and `07_Baseline_Trajectories` hold only READMEs. No new baseline exists elsewhere either (N2's verifier file is empty).
- 30 slots, weight 102. Budget 154 of 164 planned, or 136 if only Aug-Sep PRs count (dossier: 9 of the 39 merged before Aug 1).
- Record diff against rev 8: 15 statements added, none removed.
- The change-request sentence is verbatim.
- "Halloween" appears once in the SQL, in the approval. The withdrawal carries neither "Halloween" nor "one-off".
- "vial" and "premium strip" appear only in the two inline notes and their #zombie-prs mirrors, which Julia cannot read. No seeded text states the lock.
- **No PNs Beta row names "Zombie Match 3D"** (14 rows checked).

**Judgement**
- Every per-slot probability, the rubric dilution and the call model.
- The carrier read habits come from the same measured sources as before. None is measured on this task.
- The simulation only combines these (`/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review_rev14/mc14.py`).
- The stated odds include an assumed 3-point error for rubric and judge effects. I applied the same 3 points to rev 8 so the two compare fairly.

Nothing was tuned to a target. Each input moved only for a reason listed in section 3.

## 1. Weight lost and pass rate

| Cause | Rev 8 | Final |
|---|---|---|
| Inline notes (S08, S09) | 7.7 | 7.5 |
| Thread reply (V01, V02, P04, P05) | 3.4 | 4.9 |
| Lock chain (S10, W06, W07) | 4.7 | 4.5 |
| Halloween (S02, W03) | 2.4 | 4.1 |
| C&W window (S01, W02) | 1.2 | 2.5 |
| Leagues (S03, W05) | 2.3 | 2.2 |
| Icon (S11) | 2.1 | 1.7 |
| Other | 2.2 | 2.0 |
| **Total of 102** | **25.9** | **29.4** |

Slots that moved: S01 .87 to .69, S02 .92 to .81, S07 .75 to .85, S08 .25 to .28, S09 .21 to .23, S11 .59 to .65, V01 .64 to .53, P04 and P05 .85 to .65, W02 .81 to .68, W03 .61 to .36, W06 .49 to .51, W07 .45 to .48. The rest moved by .02 or less.

| | Mean | Under 85 | Under 80 | Under 70 |
|---|---|---|---|---|
| Rev 8, same method | 78.6% | 93% | 61% | 3% |
| **Final** | **76.3%** | **96%** | **78%** | **10%** |

I would state that as: **about 76%, plausible range 70 to 83; about 95% under 85, about 75% under 80, about 10% under 70.**

Pinning more cells in the brief adds rows but barely changes this (76.5% with about 15 more weight of mostly easy rows, some tied to S01).

**Spread.** SD median .075, up from .066, with about a 15% chance of reaching 0.1. It most likely still misses the floor.

**Largest unknown.** The inline read rate: .15 gives 75.3%, .45 gives 77.6%.

## 2. Tool calls

- **Per run:** median about 130, range about 92 to 210. This is down about 4 from rev 8 because the brief now settles cells a run would otherwise explore (a judgement, not a measurement).
- **Six-run average:** about 140. At or above 100: about 99%. At or above 130: about 70%.
- **Every run at 130+:** about 2 to 3%. Under 5% is the honest statement.

Nothing changed the main driver: about 10 writes, and the only per-PR mandate is the change-request sentence.

## 3. What moved the estimate most

Verifier points, applied in this order.

| Change | Effect |
|---|---|
| Withdrawal de-named | **−1.6** |
| Cadence moved and "pre-empts" deleted | **−1.2** |
| "only" removed from Push copy | **−0.7** |
| `cmt_zom563_1` (new) | +0.3 |
| Closed still-to-do rule | +0.3 |
| Vial and icon notes state they must land | +0.2 |
| Settling records and cell rules | +0.2 |
| "you tell its owner", "any time before it" | +0.1 |
| **Net** | **−2.4** |

My earlier review forecast about 74.6% for these three levers. It lands higher, for three reasons:

- **I overstated lever 1 on S02.** Robert's approval names no week or slot, and the brief lets one-offs overlap, so a run that keeps the one-off need not take a week from Plague Race. S02 is .81, not .65. Part of the loss moves to V01, because a live one-off invites an extra row. The design's "week 4" wrong reading is weaker than the manifest says.
- **Lever 2 is weaker than I assumed.** Since no row names the game, a strict reading holds all ten rows. That may read as a cue, so I used 25% sending without the reply, not 15%.
- **`cmt_zom563_1` gives back part of lever 3.** It says outright that the C&W server windows wait for Oct 8. ZOM-563 is now Done, so an open-issue list skips it. I put reach at about 18%.

The closed rule's "flagged since this brief" works in both directions. It keeps noise out of the cells and also nudges runs to look for later flags. It contains no word pointing at reviews, so I moved inline reads only .25 to .27.

## 4. Remaining lever

**No SQL change is worth reopening review.** Take the pre-check first: it measures the thread and inline read rates, which matter more than any further edit. At `/rubric`, keep owner rows and the C&W prod-deploy item (Douglas) as their own atomic rows where the rules already require it, then re-run the SD check after any row change.
