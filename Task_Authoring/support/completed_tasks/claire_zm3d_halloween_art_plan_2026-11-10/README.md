# Claire: ZM3D Halloween art plan (submitted 2026-11-10)

Persona Claire Morgan (Art Lead) · Long Horizon · Design / Marketing and GTM / Authoring · difficulty mode medium in `00_Assigments.md` (cap under 85%), easy on the second platform attempt (cap under 90%; never reconciled, the baseline clears both) · universe Oct 1, 2025 (synth-cut, clock 2025-10-01 00:00 PT) · platform attempts 6aea4c1eea32a6fa98b9b1d9 (first, Nov 5 to 7) and 6aeed825ea17fab7311d0896 (second, submitted).

Prompt (3 sentences, 669 bytes, sha256 63d7c0713c3b, unchanged through both attempts): take Leonard's #zombie_marketing message and do it all: work out the Halloween call for everything live (store pages and every running ad) and who makes what by when, put it in a plan doc and a tracker in Claire's Drive shared with everyone on Thursday's review, comment each ad's call and due date on its ART ticket, assign the ones needing new work, open ART tickets for new store art, and reply in Leonard's thread with both links.

This folder replaces the 2026-11-07 archive of the same task. That archive was the rev3 state after attempt 1. The author reused it on 2026-11-07 as working copy `task_inputsKum`, the second attempt failed /prompt on it, and the task was finished and submitted from that copy. Every file of the old archive is kept here (see Layout).

## Iterations

| # | When | Platform | What changed |
|---|---|---|---|
| 1 | Nov 5 | Attempt 1: /injection PASS r1; /prompt FAIL 2 ("new store art" could mean 2 or 4 tickets, lifecycle slips in injected records) | rev1 SQL |
| 2 | Nov 5 | /injection PASS r2; /prompt PASS 5; /hardness FAIL 2 (the run got 58 of 58 ad calls right) | rev2 moved the deciding facts off the swept path |
| 3 | Nov 6 | /injection PASS r3; /prompt PASS 5; /hardness NON-FAIL 4 PROCEED; /oe PASS 5 first time | rev3 (sha 0a08dedecd60) |
| 4 | Nov 6 to 7 | /rubric FAIL 2 on 221 rows (5801aea6371a); its Fix List applied; round 2 passed per the author (no report on disk) | 217 rows, 3d4bb51e8a92; rev3 baseline run but no verifier results; archived 2026-11-07 |
| 5 | Nov 7 to 8 | Attempt 2 on the same rev3 body (2175e44f = rev3 minus 7 header comment lines): /injection PASS; /prompt FAIL 2 (Unique Ground Truth 2, Clarity 2) | Fork: did Marcus's Sep 25 re-records (#1935, #1896, #1966) replace the running cuts on ART-795, 797, 805 and 823? Earlier rounds passed the same bytes |
| 6 | Nov 8 | rev4 (sha 6c143945fe3e): /injection PASS; /prompt PASS 5 (Eval release 81446b85 → adefd7cb, every dimension rescored); /hardness NON-FAIL 4 (215 calls, five independent misses); /oe PASS 5 | One thread reply by Marcus under his post: "use these from now on, they replace the april captures on ART-795, ART-805 and ART-797. the couch 16:9 on ART-823 wasnt redone, thats still the apr 7 capture". Answer key byte-identical. Note in `Working_Files/run_forensics/rev4/CHANGE.md` |
| 7 | Nov 8 | /rubric FAIL 1 on 217 rows (6e8624c28ac6): 55 Major (53 rows + 2 missing outcomes, 25.3%) | Count and exact-list bundles (R6 to R8 totals, R9's 30-ad list) and the undefined labels "Refresh first" and "Reuse" in 36 comment rows and R4/R5. Checked fixes verbatim, six rows deleted, own rewrites for R6 to R9: 213 rows, weight 727 (`Working_Files/rubric_gen/platform_r3fix/`) |
| 8 | Nov 8 | /rubric FAIL 1 on e70e93c35e19 | The own rewrites failed: R6 to R8 totals were overly specific ("the prompt never asks for a total"); evidence Accept lines widened R25, R34, R85, R99, R210 (not self-contained); R15/R16 bare Oct 22. All fixes were checked and applied verbatim: one named ad per call (ART-809, ART-808, ART-811); OE 38 updated to match. 213 rows, weight 731 (`platform_r4fix/`) |
| 9 | Nov 9 to 10 | /rubric passed per the author (no report on disk) | Builder paste diffed against `09_Rubrics.json`: 4 content errors reported before submission (below) |
| 10 | Nov 10 | Baseline on rev4, verifier, /create-allfail | 64.1% average, 37 valid all-fails; submitted |

## Final state

| Slot | State |
|---|---|
| `01_Universe_Inject.sql` | rev4, sha256 6c143945fe3e, 173,249 bytes. /injection PASS on every round of both attempts. Friction: none. No reference files |
| `04_Prompt.txt` | sha256 63d7c0713c3b, never edited |
| `08_Oracle_Events.md` | 161 events, 46,193 bytes, sha256 072d1e999ce9 (OE 22 quotes the rev4 reply; OE 38 names the ART-808/816 redo, the ART-809 re-cut and the ART-811/813 Skip). /oe PASS 5 on both attempts; no /oe report after the OE 38 edit is on disk |
| `09_Rubrics.json` | 213 rows, all Outcome, weight 731 (5 ×70, 3 ×119, 1 ×24), sha256 363f27b46cae |
| `plateform_rubrics.json` | The builder paste (not valid JSON). Content errors against `09_Rubrics.json`: R31 and R66 justifications replaced by the row title, R64 evidence replaced by its justification, R43 weight 4 for 3. The platform also strips `<>` from 70 Gmail message IDs in 66 rows (not an error) |
| `05_Human_Time.md` | 24.75 h (worksheet `Working_Files/05_Human_Time_Worksheet.md`, humantime gate PASS) |
| `07_Baseline_Trajectories/` | 6 rollouts on rev4, all claude-opus-5-5, counted calls 221, 231, 237, 211, 216, 226 (mean 224) |
| `10_Baseline_Verifier_Results.md` | 169, 160, 154, 158, 156, 162 of 213 criteria; weighted pass 70.7, 63.7, 60.5, 63.2, 61.6, 65.1; average 64.1%; 0 full passes; 6 distinct failure patterns; population SD 0.033, below the 0.1 to 0.3 band (Spread Too Low) |
| `11_AF_Justification.md` | 37 all-fail rows, all VALID, weight 185 of 731 (25.3%). Screen text in `11_Baseline_AllFail_Justifications.md` |
| Verifier binding | `Working_Files/verifier_binding.json`: each Run #N cites a plan-doc Drive file id found in exactly one export, plus each export's init session id; `Working_Files/12_difficulty_input.json` built from it |
| Local gates | allfail: every content check passes; the gate fails only on `chain.rubric-check` and `readiness.evidence`, because `09_Rubric_Check.md` predates the platform rubric fixes (it still says 217 criteria). `12_Difficulty_Stats.txt` was not produced |

## Key answers

- **Scope:** 62 surfaces: 4 store surfaces, 56 Unity rows, plus two ads off the sheet, ART-826 (Frederick's Trello comment) and ART-831 (its own ticket). ART-836 to ART-839 are paused, on the Archive tab.
- **Calls (58 ads):** Refresh first 36, Halloween version 12, Skip 10. **Store:** the app icon and the iPad 12.9" set are Halloween versions still to be made; the iPhone 6.5" and Google Play phone sets are Reuse. Tracker totals 14 / 36 / 2 / 10.
- **Skip:** ART-806, 811, 813, 820, 821, 822, 824, 842, 844, 849, the ads that run only on Android US tablet. ART-811 and ART-813 get there through Frederick's Sep 29 mail.
- **Halloween version:** ART-795, 797, 805 (Marcus's re-records, settled by his rev4 reply; ART-823 keeps its Apr 7 capture), 808, 816 (test turned down, redo from the Sep 16 capture), 817, 818, 819, 851, 852, 853, 854.
- **Refresh first exceptions:** ART-809 (music baked in, Aug 13 thread), ART-833, 834, 835, 848 (old zombies on the packs, Frederick's Trello comment), ART-831 (Android #1450, two builds short), ART-840 (Jul 28 capture, the Sep 11 opening is an edit).
- **Due dates:** Fri Oct 10 for the 30 working ads on Android US phone (Frederick's Sep 30 4:42 PM PT reply in #zombie-match3d overrides his 4:10 PM mail), Wed Oct 15 for the other 18. Icon and iPad set by the Thu Oct 16 12:00 PT merge cut, in the Oct 17 build, not a swap around the 24th.
- **Makers:** Julia Lawson 6 (ART-825 to ART-830, Martin's vacation hand-off), Marcus Bennett 42, Martin Walsh the icon and store art.
- **Writes:** plan doc, tracker, 12 shares to the six other review attendees, 58 comments, 48 assignments, 2 new ART tickets, one reply under C06DJBJL798/1759269913.882683.
- **What the rev4 baseline missed:** no run read Frederick's Oct 10 reply (33 all-fail rows: R9, R36, R37 and 30 comment rows; every run dated all ads Wed Oct 15, runs 2 and 4 wrote Oct 10 only as a refresh checkpoint) or his end card 001 Trello comment (R129, R131, R133, R149; every run called the four cuts Halloween version). The spread came from three traps some runs did find: the cheer fastcouch ruling (ART-808/816 rows passed by 4 of 6 runs), Martin's hand-off to Julia (1 of 6) and the re-record calls on ART-795, 797 and 805 (1 of 6).

## Lessons carried forward

### From attempt 2 (Nov 7 to 10)

- **A /prompt PASS does not survive a new attempt.** The rev3 body passed /prompt twice in attempt 1, then failed Unique Ground Truth 2 in attempt 2 on a fork the earlier rounds never raised. Settle it in data with one record off the runs' path (0 of 7 rev3 runs would have read it) and keep the answer key byte-identical. Attack the draft text first: "in unity now", "same slots" and "only those 3" each opened a new fork or contradicted the base. One revision fixed it.
- **/rubric rules move between attempts.** Titles using "Refresh first" and "Reuse" passed in attempt 1 and were Major not_self_contained in attempt 2. Define every call label inside every title ("Refresh first, meaning re-captured, re-rendered or re-cut before its Halloween pass"). Do not grade totals or exact lists the prompt never asks for; one named item per call passed.
- **Own rewrites cost another round, again.** Every round-1 "needs your own rewrite" row (R6 to R8 totals) and every widened evidence Accept line was a round-2 finding. Round 2's list was all `(checked)` and passed after a verbatim copy.
- **A rubric fix can change an Oracle Event.** The round 2 report asked for OE 38 to name the same items as the new rows and for /oe to be re-sent. Check the OEs after every rubric change.
- **Diff the builder paste.** Four of 213 rows came back wrong (two justifications replaced by the row title, one evidence replaced by its justification, one weight 3 typed as 4). Lost `<>` around Gmail IDs is the platform, not the paste.
- **The local regex grader read the spread right.** rev3's local projection (60.6%, SD 0.025) was close to the rev4 verifier (64.1%, SD 0.033). Trust it as an early warning, and fix the spread before the baseline, not after.
- **Deciding records nobody reads make the score deterministic.** 0 of 7 rev3 runs and 0 of 6 rev4 runs read Frederick's Oct 10 reply or the end card 001 comment. Those two records carry 25.3% of the weight as 37 all-fail rows, so SD stayed at 0.033. /hardness's "Grouped failures" table (C1 to C5) named both families before the baseline. When one cause holds more than about 20% of the weight and the pre-check missed it, expect Spread Too Low. The fix is a route some runs take (a link from a record they already read), not more rows.
- **Binding the verifier.** The verifier copy has no session IDs. Each run's first row cites the plan doc's Drive file id, which is unique per run, and each export's init event has a session id. That makes a reviewed receipt `difficulty_stats.py --build` accepts with `--task-dir`, `--revision` and `--binding-receipt`. Newer gates also need `Working_Files/00_Readiness_Config.json`.
- **Platform rubric fixes leave the local chain stale.** After the platform-driven edits, `09_Rubric_Check.md` no longer matched, and the allfail gate failed only on that chain. Re-run `/create-rubric-writing check` on the final file if a clean local chain matters.
- **Record the platform's difficulty mode at intake.** Attempt 2's platform record said easy while `00_Assigments.md` said medium; it was never reconciled.

### From attempt 1 (Nov 5 to 7)

- **Local /rubric did not predict the platform, in either direction.** The same file got local PASS 5 and platform FAIL 2; the fixed file got a local read-only FAIL 2 and then passed. Seven local runs were too many: sync Evals, run one local pass, then use the platform.
- **Check a local Fix List against platform reports before copying it.** Run 1 wanted 184 rows cut to 90 by sampling comments, which is what failed frederick_q4 with 48 missing outcomes; that one was caught. Run 4's exclusion-only rows were copied and cost a platform round.
- **Guard rows, as the platform ruled:** one bare count on existing records ("exactly 48 existing ART tickets"), with no range and no list; no "only on tickets other than ..." rows (an idle Agent passes them); no guard without a real decoy ("exactly 6 people" failed as overly specific); never "exactly" plus named members.
- **Rubric size:** 217 rows was the largest in this folder (213 submitted). 154 are per-ticket rows. The 48 assignment rows were an author's choice to escape named sets; template writes can be sampled with a volume row, as frederick_q4 did. Every row has to be typed into the builder, which is where the paste errors came from.
- **`revised after check` rows draw the next finding.** Six local rounds in a row found a defect in the previous fix text. Only `checked` fixes lock.
- **Weights the platform set:** a ticket that says "Made by Marcus" is still 3, because assigning it needs the needs-new-work check. A rule joining Gmail, Slack and Linear is 5 even when the value is literal in one reply.
- **Accepted forms go in the title,** including first names: "Julia Lawson (or Julia)". Keep "final" on due-date rows, because the runs write a refresh date plus an Oct 15 hand-off; both attempts' baselines did.
- **Corrections nobody finds add no spread.** rev3 moved the deciding facts off the swept path to clear /hardness; the four records it moved were read by 0 of 7 rev3 runs. Only mid-findability traps separated runs. Plan at least two traps at that level. Trimming rows does not fix it: a simulated 96-row set still gave SD 0.055.
- **What made /oe pass first time (twice):** `oe_gen/model.py` re-derives every call, date and maker from the rows and asserts against `solver/truth.json`; `build_events.py` quote-checks every Expected span; a blind reviewer re-derived all 62 surfaces before /oe.
- **Tooling:** `hg_rubric_ledger.py plan` writes files; `search` and `get` reject `--no-cache`, so use `--no-index`; zsh does not split `$PY` when it holds a path and a flag. Keep multi-step pipelines in a bash script (`rubric_gen/run_pipeline.sh`).

## Layout

- `task_inputs/` is the slot as submitted, moved here from `Task_Authoring/task_inputsKum` with these changes: the platform reports moved to `eval_reports/`, the builder paste `rubrics.json` became `plateform_rubrics.json`, and the builders moved to `work/`.
- `task_inputs/Working_Files/`:
  - `oe_gen/`: the OE builders.
  - `rubric_gen/`: the rubric builders and the local grader, the local rounds `review1/` to `review8/`, and the two platform fixes `platform_r3fix/` and `platform_r4fix/`, each with its reviewed file and a CHANGE.md.
  - `run_forensics/`: every SQL revision, rev1 to rev4.
  - `research/prompt_review_rev4/`: the local cold review of rev4.
- `task_inputs/Working_Files/archive/` holds the 2026-11-07 archive:
  - `README_2026-11-07.md`: the old README.
  - `rev3_slot/`: the 18 files whose rev3 content was replaced later, including the rev3 SQL, OEs and 217-row rubric, the attempt-1 pre-check and the rev3 baseline trajectories (no verifier results exist for them).
- `eval_reports/attempt1_6aea4c1eea32a6fa98b9b1d9/` holds attempt 1's reports, renamed by stage, verdict and round.
- `eval_reports/attempt2_6aeed825ea17fab7311d0896/` holds attempt 2's reports under their download names:

  | File | What it covers |
  |---|---|
  | `_0_injection.md`, `_1_prompt (1).md` | rev3 body: /injection PASS, /prompt FAIL 2 |
  | `_0_injection (4).md`, `_1_prompt (4).md`, `_1a_hardness.md` | rev4: /injection PASS, /prompt PASS 5, /hardness NON-FAIL 4 |
  | `_2_oe.md` | /oe PASS 5 |
  | `_3_rubric.md`, `_3_rubric (1).md` | /rubric rounds 1 and 2, both FAIL 1 |

  The round 3 /rubric report was not saved.
- `work/claire_zm3d_halloween/` holds copies of the builders (`scenario_gen`, `injection_gen`, `prompt_gen`, `oe_gen`, `rubric_gen`) and the solver. They name the old folders `task_inputsN2` and `task_inputsKum`, so repoint them before re-running. `injection_gen/gen_sql.py` does not hold the rev4 reply, so a rebuild drops it.
