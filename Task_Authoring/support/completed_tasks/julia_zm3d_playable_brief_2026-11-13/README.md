# Julia Lawson: the PlayableX hand-off brief and the 96-line pack list (submitted 2026-11-13)

| Field | Value |
|---|---|
| Persona | Julia Lawson (Product Manager) |
| Horizon | Long Horizon |
| Assignment | Product / Marketing and GTM / Authoring |
| Difficulty mode | hard (cap: average under 70%) |
| Universe | Oct 1, 2025 (synth-cut, freeze 2025-10-01T00:00:00Z, clock 2025-10-01 00:00 PT = 07:00 UTC) |
| Platform task | 6aea4c201e1fa1ddfdd0a25d (id taken from the report file names) |
| Requester targets | 130 or more counted calls in every run; average under 70%; largest failure pattern at most 50% (exactly 50% passes); the spread (SD) is reported, not binding |

**`task_inputs/`** is the slot folder as submitted (it was `Task_Authoring/task_inputs`), moved here unchanged except that `plateform_reports/` became `eval_reports/` next to it. Notes on what it holds:
- `06_PreCheck_Trajectory/trajectory-run-1.json` is the rev1 pre-check and `trajectory-run-1-2.json` the rev2 pre-check. A stray copy of the round-2 rubric report sits beside them.
- `07_Baseline_Trajectories/` holds the six rev2 runs the verifier graded. `07_Baseline_Trajectories-2/` is the original download of the same six files, byte for byte (`trajectory-run-1 (1).json` there is `trajectory-run-1.json` in the slot).
- The six rev1 baseline runs are in `Working_Files/run_forensics/rev1/exports/`, with the rev1 SQL and design artifacts beside them.
- `task_inputs/eval_reports/` holds the seven reports `report_intake.py` filed, byte-identical to their namesakes in the archive's `eval_reports/`; `Working_Files/platform_task.json` and `task_metrics.json` cite them.
- `plateform_rubrics.json` is the builder export saved on Nov 12 before the verifier ran. It differs from `09_Rubrics.json` (see Final state).
- `Working_Files/` holds the design, budget, dossier, manifest, forecast and preflight, the solver, the OE ledger and check, the rubric plan and check, the rev1 hardening report, run forensics for rev1 and rev2, the verifier binding receipt, and the all-fail, difficulty and human-time generators with their outputs.

**`eval_reports/`** holds every platform report under its download name (prefix `6aea4c201e1fa1ddfdd0a25d`):

| File | What it covers |
|---|---|
| `_0_injection.md`, `_0_injection-1.md` | /injection PASS on rev1, then on rev2 |
| `_1_prompt.md`, `_1_prompt-1.md` | /prompt PASS on rev1 (every dimension 5), then PASS on rev2; same prompt bytes |
| `_1a_hardness.md`, `_1a_hardness-1.md` | /hardness NON-FAIL 4 on the rev1 pre-check (253 calls), then NON-FAIL 4 on the rev2 pre-check (215 calls) |
| `_2_oe.md`, `_2_oe (1).md` | /oe FAIL (Accuracy 2 on one event), then PASS (Completeness 5, Accuracy 5) |
| `_3_rubric.md`, `_3_rubric (1).md` | /rubric FAIL 1 on the 126-row draft, then NON-FAIL 3 on the submitted 153 rows |

**`work/julia_zm3d_playable_brief/`** holds copies of the builders from `task_inputs/Working_Files/`. They hard-code `Task_Authoring/task_inputs`.
- **`plan/`:** the design model and planned record texts (`design_model.py`, `planned_texts.py`), the scenario, surface, budget, SQL, manifest, dossier and review builders, the `patch_d3_*` and `patch_rev2_*` revision patches, and the `run_*.sh` wrappers.
- **`plan/rubric/`:** `build_rows.py`, `build_rubrics.py`, `build_plan.py`, `build_check.py`, and the round-1 repair (`apply_rubric_fix_round1.py` with `fix_round1_map.json`, rehearsed by `rehearse_fix_round1.py`).
- **`oe_gen/`:** the OE fact model, draft, ledger and check assemblers.
- **`hardening_gen/`:** the rev1 forensics report builder and `simulate.py` (the six-run simulation of each rebuild option).
- **`allfail_gen/`, `difficulty_gen/`, `humantime_gen/`:** one generator each for `11_AF_Justification.md`, `12_Difficulty_Stats.txt` and the human-time worksheet with `05_Human_Time.md`.
- **`solver/`:** `solver.py` and `truth.json` (the 96 lines with state, owner, board set and ticket).

## Final state
- **Injection SQL:** rev2, sha256 7d1f2aaeb29c, 136,372 bytes (the platform hashes it without the four header comment lines: c037dd89736e). Friction: none. No reference files. rev1 was 78465cd474f8 (platform 3a76797fbde1); rev2 edits six statements of it in place and adds none.
- **Prompt:** sha256 33c721d60945, 46 words, unchanged from rev1 to rev2. It asks for everything in Frederick's playable message from the day before, with the files in Julia's Drive and the links in the PlayableX channel. Frederick's DM points at his hand-off notes, which carry the brief's contents, the three state tests, the ticket rule and the recipients.
- **/prompt:** PASS on both revisions.
- **/hardness:** NON-FAIL 4 twice, three independent causes each time.
  - rev1 (253 calls): Marcus's post, Brian's folder log and Robert's board-swap reply were missed.
  - rev2 (215 calls): Marcus's post, Robert's bathroom note and Brian's folder log were missed; 35 of 96 lines wrong.
- **Oracle Events:** 130 events, 39,556 bytes, sha256 53b494931204.
  - **Round 1, FAIL:** OE 20 accepted "a more hardcore friendly playable" as a second purpose for the brief. Robert takes that back three minutes later in the same thread.
  - **Round 2, PASS** on the one-purpose version.
- **Rubric:** 153 rows (151 Outcome, 2 Process), weight 371 (5 ×50, 3 ×9, 1 ×94), sha256 ea8009a35949.
  - **Round 1, FAIL 1** on the 126-row draft (weight 338): 42 Major rows, one missing outcome and a Moderate overlap group. The facts were right; the structure was not. 34 comment rows bundled two parts, several rows rejected correct answers, the State samples went over five per group, 56 titles began "The Agent's ...", two rows accepted by absence, and the weights were uneven. The Fix List was applied by script.
  - **Round 2, NON-FAIL 3:** no Major or Moderate; 11 Minor rows of 153 (7.2%), on the eight instrument comment rows and the brief's sound rows R21 to R23. Left as they are.
- **Builder paste:** `plateform_rubrics.json` differs from `09_Rubrics.json` in content on 18 rows. R87 and R100 carry weight 1 (local 5), R152 and R153 are "outcome" (local Process), and the evidence text differs on 15 rows (R29, R34, R38, R56, R58, R60 and the even rows R92 to R108). Whether the builder was corrected before the verifier ran is not recorded. Pass and fail results do not depend on weights; with the platform's two weights the average reads 41.0%, not 40.5%.
- **Baselines** (rev2, verifier on ea8009a35949, 6 of 6 completed, all `claude-opus-5-5`):

  | | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Run 6 |
  |---|---|---|---|---|---|---|
  | Rows passed (of 153) | 73 | 73 | 73 | 98 | 93 | 99 |
  | Weighted pass | 31.0% | 31.0% | 31.0% | 50.7% | 48.2% | 50.9% |
  | Counted calls | 221 | 196 | 200 | 237 | 225 | 244 |

  - Average 40.5%, under the hard cap of 70%. No full passes; 0 errored. Average 220 counted calls, lowest 196.
  - Four failure patterns: {1, 2, 3}, {4}, {5}, {6}. The largest is 3 of 6, exactly 50%, which passes with no margin.
  - Population SD 0.095 against the band of 0.1 to 0.3 (sample SD 0.104). This is the one gate that fails. The task was submitted with it open, under the owner's rule of 2026-11-10 that a spread miss alone does not force a revision.
- **rev1 baseline (superseded, graded on the gradable surface, no verifier):** 53.3, 100.0, 92.3, 72.8, 72.3 and 100.0, average 81.8% with two full passes. That is why rev2 exists.
- **All-fail:** R55 (exactly 49 tickets moved to Todo), R147 (Owed count 49 in the DM) and R148 (Ready count 39 in the DM), all VALID. Each needs all three deciding records, and no run opened more than one. Justifications in `11_Baseline_AllFail_Justifications.md`.
- **Human time:** 19.00 h (1,140 min: reading 515, dead ends 200, re-reading 80, writing 345). Worksheet in `Working_Files/05_Human_Time_Worksheet.md`; the typed paragraph is `05_Human_Time.md`.
- **Local gates:** human time PASS. The all-fail and difficulty gates pass every check on their own files and fail only on `chain.rubric-check` and `readiness.evidence`:
  - the local rubric check was never certified (37 rows, mostly ticket comments, carry weight 5, above the band the gradable surface gave that kind of work);
  - the hardening report is for rev1, and no rev2 hardening, baseline design review, builder export or platform hand-off receipt exists.

## Key answers
- **Population:** 96 pack lines, one ticket each (DES-314 to DES-409 under Brian's pack ticket DES-313).
- **States:** Delivered 8, Ready 39, Owed 49. Owed by holder: Brian 27, Claire 18, Calvin 3, Martin 1.
- **What decides the hard lines.** Brian's ticket notes say Ready on all of these until a later record is read:
  - Marcus's post in #zombie-match3d (Sep 26): Brian's 12 Thursday exports out of Unity are ASCII FBX, and PlayableX takes binary only. Owed, Brian.
  - Robert's DM to Julia (Sep 29): the 12 bathroom files Claire gave Brian on Friday are the old version. Owed, Claire.
  - Brian's log of the outgoing folder (a Drive doc): the zip with the 8 instruments was cut off on upload. Owed, Brian. The same log says Claire re-sent the three recoloured models (Cactus Plant, Chainsaw, Cone), so they are Ready, against Robert's earlier post.
  - Calvin's sound sources sheet: the Rocket and Explosion sounds come from a library and a bought pack, and the background music is not made. Owed, Calvin.
  - Robert's later reply in a #zombie-art thread: the Bow replaces the Dynamite in the board's eight.
- **The brief:** Scenario 1 and its one purpose, the eight board items with the Bow, four zombies, the 7-slot tray, loss at zero health (a full tray is not a loss), music after the first tap, the Nov 3 start and the vendor's formats.
- **Writes:** a Doc and a 96-row, 7-column Sheet in Julia's Drive; 8 view-only shares (Frederick, Brian, Robert and the PlayableX intake address, on both files); 49 tickets moved to Todo with 49 comments; the count for each state to Frederick; both links in the PlayableX channel.
- **How Opus failed on rev2:** three records (Marcus's post, Robert's note, Brian's log) decide 32 of the 49 Owed lines. Runs 1 to 3 opened none of them and reported 20 Owed. Runs 4, 5 and 6 each opened exactly one (Marcus's post, Brian's log, Robert's note) and reported 32, 25 and 32. Runs 4 and 6 also missed the Bow swap. All six read Calvin's sheet.

## Lessons carried forward
- **Moving the deciding records off Opus's routine paths halved the score.** rev1 averaged 81.8% with two full passes; rev2 averaged 40.5% with the same prompt, the same 96 lines and six edited statements. What moved:
  - a correction in the author's own DM, found by a search for that author in 6 of 7 runs, became another person's DM to the persona (found by 1 of 6);
  - the folder log lost the one word ("sound") that another unit's Drive search returned (5 of 7, then 1 of 6);
  - the correcting post lost the wording of the note it corrects (4 of 7, then 1 of 6);
  - a hub-channel post every run read was reversed by a completion note in the log.
- **It overshot, and the spread paid for it.** Three records at 1 of 6 each, never two in one run, put the scores in two tight groups (31.0% and 48 to 51%): SD 0.095 and a largest pattern at exactly 50%. The rev1 forensics simulation had this as its "finds less" case. A relocated record's central find rate was too hopeful.
- **Spread needs a mid-rate record that carries weight.** The only record found by about half the runs (the Bow swap, 4 of 6) decided 15 of 371 weight. Give one unit a find rate near one half and a fifth or more of the weight.
- **Exact-count rows all-fail when several low-rate records feed them.** R55, R147 and R148 need all three records. They are fair, so write their justifications early.
- **The forecast was right for the wrong reason.** It expected an average of 78 to 93% and a failed gate; the average was 40.5% and the gate that failed was spread. A yes/no score on "a gate fails" (Brier 0.0005) hid that.
- **Certify the local rubric check before the platform /rubric.** The all-fail and difficulty gates chain on it. Here it was skipped, and afterwards it could not be certified: 37 rows, mostly ticket comments, sit at weight 5, above the band the gradable surface gave that kind of work.
- **/rubric round 1 failed on shape, not facts:** "moved and commented" in one row, "The Agent's ..." titles, accept-by-absence rows, more than five State samples per group. Applying the Fix List text unchanged by script cleared it in one round.
- **An Expected line that accepts a second wording needs the thread read to its end.** One event cost /oe a round.
- **Diff the builder export against the local rubric before the verifier.** Two weights and two categories differed after the paste. The average moves with weights even though pass and fail do not.
- **Two baseline batches were in the folder.** Binding every export to its SQL revision by content, keeping only the graded batch in the slot and filing the older one under `run_forensics/rev1/exports/` kept the numbers honest.
- **Human time after the baseline:** measure windows in Pacific days, count a check no Oracle Event needs (22 pull requests, opened by 5 of 6 runs) as a dead end, and write the field text as one paragraph.
