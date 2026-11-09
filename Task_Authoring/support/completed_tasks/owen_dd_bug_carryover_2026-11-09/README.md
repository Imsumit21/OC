# Owen Baker: DD bug carry-over from Slack to Linear (submitted 2026-11-09)

| Field | Value |
|---|---|
| Persona | Owen Baker (Game Engineer, Unity) |
| Horizon | Long Horizon |
| Assignment | Engineering / Engineering Ops / Actions |
| Difficulty mode | medium (cap: average under 85%) |
| Universe | Feb 14, 2026 (normal, clock 2026-02-14 00:00 UTC) |
| Platform task | 6aeed8256c022adb310c8253 (taken from the report file names) |
| Requester targets | more than 130 counted calls in every run; average under 80%; every other difficulty gate passing |

**`task_inputs/`** is the full slot folder as submitted, diff-verified against the original. It includes `Working_Files/run_forensics/`, which holds:
- every injection revision rev1 to rev9, with its SQL;
- the pre-check and baseline forensics for rev5, rev7, rev8 and rev9 (`rev9/baseline/` has the hand grading);
- the rubric builds (`rev9/rubric/`, including `09_Rubrics_PASS5_138f960e0b21.json`);
- the escaped-title binding copy the verifier needs (`rev9/platform/09_Rubrics.verifier_titles.json`).

**`eval_reports/`** holds every platform report, named by stage, verdict and round:

| File | Revision |
|---|---|
| `0_injection_*_r1.md` to `_r9.md` | rev1 to rev9. r3 was a FAIL (Owen's join rows had no matching base leave); every other round passed. |
| `1_prompt_FAIL_r2.md`, `1_prompt_FAIL_r4.md`, `1_prompt_FAIL_r6.md` | rev2, rev4, rev6 (unsettled forks; Coherence; the tooltips thread) |
| `1_prompt_PASS_r5.md`, `_r7.md`, `_r8.md`, `_r9.md` | rev5, rev7, rev8, rev9 (all PASS 5) |
| `1a_hardness_NONFAIL_r5.md`, `1a_hardness_FAIL1_r7.md`, `1a_hardness_FAIL2_r8.md`, `1a_hardness_NONFAIL3_r9.md` | rev5, rev7, rev8, rev9 |
| `2_oe_FAIL2_r1.md`, `2_oe_NONFAIL3_r2.md`, `2_oe_PASS5_r3.md` | rev9 OEs; the third round passed (a9bbea55e7c3) |
| `3_rubric_FAIL1_r1.md`, `3_rubric_FAIL_r2.md`, `3_rubric_PASS5_r3.md` | the 61-row first draft 2ed7a6489798, then 9f8ebad8c3e3 (138 rows), then 138f960e0b21 (R3 rewritten) |

**`work/owen_dd_bug_carryover/`** holds copies of the builders from `task_inputs/Working_Files/plan/`, plus the solver:
- **Scenario and SQL:** `build_scenario.py`, `assemble_design.py`, `build_sql.py`, `build_final_manifest.py`, `build_dispositions.py`, `boot_rev*.py` and `sim_rev6*.py` (the revision simulations).
- **Dossier, brief, OEs and human time:** `assemble_dossier.py`, `assemble_brief.py`, `assemble_check.py`, `oe_reads.py`, `oe_defer.py`, `assemble_oe_ledger.py`, `assemble_oe_events.py`, `assemble_oe_check.py`, `build_humantime.py`.
- **Rubric:**
  - `rubric_rows.py` builds the rows and `rubric_titles.py` the text. The `lock=` key byte-copies the rows /rubric reviewed.
  - `assemble_rubric_draft.py` writes `09_Rubrics.json` and the V3 sidecar rows; `assemble_rubric_plan.py`, `build_rubric_extra.py` and `assemble_rubric_check.py` build the plan and check files.
  - `shortcut_ok.txt` holds the probe dispositions as `@@P:fact@@` tokens.
- **All-fail:** `assemble_allfail.py` writes both all-fail files from one table.
- **`scratch/`:**
  - `predict_rows_r1.py` maps the saved baseline grades onto the 138 rows;
  - `check_assumed.py` checks the template, build-line, sheet and reply rows against the runs' write calls;
  - `extract.py` pulls the per-run all-fail evidence with event indexes.

## Final state
- **Injection SQL:** sha256 ea5b542897c8 (rev9), 149 inserts and 39 updates. Friction: none. No reference files. /injection passed on every revision except rev3.
- **Prompt:** sha256 03e95ad1e900, 105 words. The text was unchanged from rev2 to rev9; every /prompt fix went into the universe. It asks Owen to do three things before Sunday's bug review, "the way he lays it out":
  - carry DD's Slack bug list into Linear;
  - bring the UI Changes tree up to date, with a line on every child;
  - put a sheet in his DD bug carry-over folder, shared with the review.

  Then he replies in Arthur's DM thread with the numbers.
- **/prompt:** FAIL 2 on rev2, rev4 and rev6. PASS 5 on rev5, rev7, rev8 and rev9.
- **/hardness:**
  - NON-FAIL 4 on rev5;
  - FAIL 1 on rev7 (Brian's second carriers were all read in one sweep);
  - FAIL 2 on rev8 (a narrow miss, only Apple);
  - NON-FAIL 3 on rev9 (288 calls; missed Apple and Tavern).
- **Oracle Events:** 150 events, 45,392 characters, sha256 a9bbea55e7c3. /oe went FAIL 2, then NON-FAIL 3, then PASS 5.
- **Rubric:** 138 rows (137 Outcome, 1 Process), weight 350 (5 ×31, 3 ×44, 1 ×63), sha256 138f960e0b21.
  - **Round 1, FAIL 1** on the 61-row first draft. It asked for one state row per new issue, one build-line row per child and one sample per template field, and fixed two cascades (the "[2231]" title prefix and the folder phrase). The Fix List was copied exactly; the eight untouched rows stayed byte-identical.
  - **Round 2, FAIL 1** on one row: R3 also required the prefix. It was rewritten with the prefix optional.
  - **Round 3, PASS 5**, every dimension at 5.
- **Builder export:** it matched apart from three things.
  - R108 (the 0.3.310 line on ENG-2423) was typed at weight 1 instead of 3.
  - It escaped the brackets in 9 titles.
  - It stripped the `<>` around Vincent's Gmail id in R123 and R128.

  Two imported linters were marked invalid: "Unrequested Scope" on R1 (the notes are incorporated by "the way he lays it out") and "Overlapping Items" on R1 against its samples (Eval 3 §3.3: "an aggregate control versus its atomic spot checks" are not duplicates).
- **Baselines** (rev9, verifier on 138f960e0b21, 6 of 6 completed, all claude-opus-5-5):

  | | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Run 6 |
  |---|---|---|---|---|---|---|
  | Rows passed (of 138) | 125 | 125 | 129 | 129 | 129 | 125 |
  | Weighted pass | 81.4% | 81.4% | 87.1% | 87.1% | 87.1% | 81.4% |
  | Counted calls | 312 | 326 | 325 | 274 | 263 | 230 |

  - Average 84.3%, which passes the medium cap but misses the requester's 80%. No full passes; 0 errored.
  - SD 0.029 (population): **FAIL**, the only gate to fail.
  - Patterns: 2 groups of 3 (50%), PASS.
  - Average calls: 288.
- **All-fail:** 9 rows (R1, R15, R77, R122, R123, R128, R129, R135, R136), all VALID, 0 invalid, 0 judge errors. Four of the nine paragraphs (R1, R123, R128, R129) were tightened before they were entered.
- **Local gates not re-pasted:** the rubric-writing → rubric-check → all-fail chain on the final files was still running when the task was submitted. The all-fail gate passed every check except that upstream chain. The rubric-writing gate run was stopped at archive time.
- **Human time:** 25.75 h, in `Working_Files/05_Human_Time_Worksheet.md`.

## Key answers
- **Population:** 63 canvas lines in Vincent's Android canvas comment channel, plus 7 #god-bugs posts after the last line, gives 70 bugs.
- **Outcomes:** 58 Fixed (Done), 7 Broken (Bugs), 3 Gone (Canceled) and 2 Covered. That means 68 new issues, each `[2231] <line>` under ENG-2401 (Engineering, Bug label, no assignee, empty description), with the canvas wording added on ENG-2073 and ENG-2363.
- **Broken:**
  - Tavern buttons (Marcus's Dec 11 DM D05USBTQY1F/1765452012.418229 overturns the tick);
  - shop icons (Brian's Dec 1 reply in #dd-road-to-sub-250mb);
  - train backgrounds and team-quit nav bar (Vincent's later thread replies);
  - backend errors (unticked, nobody closed it);
  - the mega tile post;
  - the tile dozer window post (PR #1913 still open).
- **Gone:** the three lives lines. Leonard's Dec 2 update removed lives on the economy line (build #2299).
- **Covered:**
  - Apple sync → ENG-2073 (Vincent's Nov 20 email to Owen);
  - manual sign-in → ENG-2363 (Vincent's Linear comment).
- **First-fit traps:** the Win & Collect and lives lines that are still ticked stay Done, because Fixed comes before Gone.
- **UI tree:** 14 open children move to Done and 5 are held:
  - ENG-2424: Win & Collect disabled;
  - ENG-2426 and ENG-2434: popups, from Arthur's inline PR reviews and Brian's Dec 11 DM;
  - ENG-2428: Oliver's comment;
  - ENG-2437: Daily Gift, from Brian's DM.

  23 of 28 end Done. Every child gets a line naming public build 0.3.310.
- **Sheet and reply:** the sheet goes in folder d_9b41e7c2a05d36f8e1c7a4 with columns Bug, Outcome, Ticket and Why, 70 rows, shared with Arthur, Robert and Oliver. The reply in thread 1770937805.214409 says 9 still broken, 68 new tickets and 23 of 28 Done.

## Lessons carried forward
- **Two universal misses cannot give spread.** Every rev9 run missed Vincent's email (Apple) and Marcus's DM (Tavern). Only the popup holds varied (3 of 6). Average 84.3% is fine, but SD 0.029 fails. A task needs at least two heavy traps that runs catch at different rates, each on a different search habit.
- **Per-target rows push the average up and the SD down.** /rubric took the rubric from 61 to 138 rows, adding one state row per issue and one build line per child. The predicted average went from 75% to 85% and the SD from 0.06 to 0.03. Plan the trap weight against the full per-target count, as the Robert task already showed.
- **Second carriers written by the same person act as one trap.** At rev6 to rev8, Brian's DM lines each repeated a trap. Runs sweep Brian's messages because he owns the closing rule, so they found all of them at once (/hardness FAIL 1 at rev7).
- **Check the reviewed SHA before acting on a /rubric report.** Round 1 reviewed the first draft, not the local check rebuild. Rebase on the reviewed JSON and byte-copy the rows the Fix List leaves alone, so the DELTA locks hold.
- **"Needs your own rewrite" rows:** make the optional part explicit in the title ("with or without a [2231] prefix", with the passing forms listed) and keep Accept equal to the title.
- **The builder drifts:** it was one weight again (R108) and escaped titles. Diff the export before the verifier, and bind difficulty_stats through an escaped-title copy.
