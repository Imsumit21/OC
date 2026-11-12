# 09 Rubric draft notes — Julia Lawson · ZM3D playable hand-off

Drafted 2026-11-12 · Clock 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) · Plan `Working_Files/09_Rubric_Writing_Plan.md` (gate PASS, OE status PROVISIONAL) · Output `09_Rubrics.json` sha256 1c44f4afdac1…

## What was written

- 126 criteria in the Criteria Builder shape (`title`, `category`, `weight`, `justification`, `evidence`), one per plan row in plan order: **R<n> = P<n>**. Generator: `Working_Files/plan/rubric/build_rubrics.py` (reads `plan/rubric/rows.json`).
- All Outcome (126); weights 5 ×26 · 3 ×54 · 1 ×46, total 338 (kind of work, from the plan's A2). Longest title 32 words.
- Evidence per row: the expected value, the record(s) holding it with the quoted span, what is accepted, what is rejected (the idle run first, then the distractor), and the OE steps that reach it. Internal ids (F-n, ledger T-n, probe forms) stay in the plan.
- Brian's per-line notes are quoted whole and attributed to the ticket they sit on ("Brian's note on DES-367 ('…')"); the plan quotes them shortened.

## Titles changed from the plan's draft titles

| Row | Plan draft title | Export title | Why |
|---|---|---|---|
| R21, R22 | The Agent's brief says PlayableX cannot use the Rocket / Explosion sound yet | The Agent's brief gives PlayableX a list of usable sounds that excludes the Rocket / Explosion sound | The ask is "what they can use for sound". A brief that lists only Matching, Success and Failure answers it, and "says … cannot use" would reject that valid answer (overly_specific). Grading the usable list accepts both fair forms and still rejects the decoy (a list naming the library sound as usable). |
| R30 | … has 96 data rows, one for each line of Brian's pack list | … has 96 data rows, one for each row of Brian's pack list | `hg.py rubric-lint` reads "each line" as a text-length format (format_lock). |
| R64 | … moves exactly 49 of the pack's tickets (DES-314 to DES-409) to Todo, one for each Owed line … | … moves exactly 49 of the tickets under Brian's pack ticket DES-313 to Todo, one for each row its hand-off list marks Owed | A count joined to a range of targets is the platform lint's `bundled_writes`; "each line" is format_lock. The row stays the one volume row of the move template and states the template. |
| R122–R124 | … tells Frederick in their DM that 49 / 39 / 8 lines are Owed / Ready / Delivered | … that the Owed / Ready / Delivered count is 49 / 39 / 8 | "<n> lines" is format_lock. |

## Checks run on the export

- `python3 -B Task_Authoring/tools/hg.py rubric-lint Task_Authoring/task_inputs/09_Rubrics.json` → `{"findings": [], "count": 0}` (5 format_lock hits on the first draft, cleared by the retitles above).
- `python3 -B Task_Authoring/tools/platform_delta_lint.py rubric --task-dir Task_Authoring/task_inputs` → `PLATFORM DELTA LINT (rubric): PASS` (R64 read as the move group's one volume row; R125/R126 claim links to files the Agent creates).
- Draft grounding (`plan/rubric/ground_draft.py` → `plan/rubric/draft_grounding.txt`): 138 quoted spans tied to a record id, 0 misses — seeded records against the parsed SQL rows, base records re-read through `hg.py search search-many` plus `hg.py search get` of the matched record's `ts` / `id`. A second sweep found all 49 distinct quoted spans of the Source parts in the SQL or in a re-read base record.
  - Fixed in the plan generator (`build_rows.py`) and re-gated: PlayableX's rule C08H78VJG80/1758022459.227279 is quoted as written ('please make sure it’s exported in *Binary format*, not ASCII'); Brian's log f_faf4d7c167d14a1127dcc3 is quoted with its capital and full sentence ('The zip with Friday's music instruments got cut off on upload … I'll put them back when we pick this up again.'); the READY source no longer carries a paraphrase in quote marks. `stage_gate.py rubric-writing --paste` → PASS on the regenerated plan (`09_Rubric_Writing_Plan.md#dedd75fc5a1b`).
  - Not changed: `08_OE_Writing_Ledger.md` quotes the same rule as 'Binary format, not ASCII' (Slack's rendered bold); the OE file does not quote it. Editing the ledger would stale the OE and plan gates for no grading gain.
- Budget on the final rows (`budget.rubric`, warn mode): `rubric_rows` added to `Working_Files/01_Difficulty_Budget.json` (A1 Brian's log 19 rows · A2 Robert's note 21 · C1 Marcus's post 20 · C2 Calvin's sheet 11 · C3 Robert's reply 3; the Owed and Ready count rows sit under every unit whose miss moves a line). `rubric_skeleton.py drift` → **WARN**: anchors 40.5% of the final weight (skeleton 40.0%; the Hard loss is 30%), C2 share −6.6 points, always-pass 26.9%. `difficulty_budget.py check` on the rubric basis → FAIL on the design-time find-rate priors (A1/A2 above 0.20, no variance unit inside 0.35–0.65, P(average < 70%) 0.824 at the high find rates). These are rev1 priors in a warn-mode check, and the measured rev2 runs below supersede them. Flagged for `/create-difficulty`, not tuned here (playbook: never add or tighten rows to move the average).

## Rehearsal on the rev2 baseline (advisory; the platform verifier grades)

`plan/rubric/rehearse_rows.py` grades the six rev2 runs (`07_Baseline_Trajectories-2`, decoded in `run_forensics/rev2/baseline/`) against these 126 rows. Rows with a gradable-surface slot take `surface_grader`'s result; the rest are graded from the decoded writes with keyword proxies. It then runs `difficulty_stats.compute` (V3, hard):

| Run | Score | Rows failed | Calls |
|---|---|---|---|
| run-1 | 139/338 = 41.1% | 55 | 221 |
| run-2 | 142/338 = 42.0% | 54 | 196 |
| run-3 | 139/338 = 41.1% | 55 | 200 |
| run-4 | 183/338 = 54.1% | 41 | 237 |
| run-5 | 204/338 = 60.4% | 38 | 225 |
| run-6 | 188/338 = 55.6% | 40 | 244 |

Gates: average **49.1%** (cap < 70%) PASS · full passes **0/6** PASS · failure patterns **4, largest 50%** PASS (at the limit) · horizon **220** PASS · provenance PASS · SD 0.079 (report-only). Rows every run passes: 68 (weight 124). Rows every run fails: R64 (exactly 49 moves), R122 (Owed 49), R123 (Ready 39); each value is reachable and each run missed it through a deciding record it never opened, so `/create-allfail` will justify them as valid.

## Self-review

| Check | Verdict | Strongest counter-reading | Resolution (evidence) | Unresolved |
|---|---|---|---|---|
| Comment rows R65–R113 grade "what is owed" and "who has it" in one row | keep | `multi_part_write`: two parts of one write are separate rows | The platform rule splits parts that come **from different sources**. Here both come from one deciding record per group (Marcus's post C0880U9751A/1758906517.912099, Robert's note D05GU6L0XFH/1759178332.042459, Brian's log f_faf4d7c167d14a1127dcc3, Calvin's sheet f_b2387e31d46d3a7b3fa2a9, or the line's own note), and the notes define the comment as one sentence ("a comment saying what is owed and who has it"). `platform_delta_lint` multi_part_write: no finding. | Reviewer judgement remains possible |
| R11 Bow "in place of the Dynamite" | keep | non_atomic (Bow in, Dynamite out) | One fact: Robert's reply C08R8CHB0QL/1758922879.243189 swaps the last item. A list of eight with the Bow and no Dynamite passes; a list of nine (both) fails, which is the decoy the row exists for. | — |
| R19 "lost only when … HP to zero" | keep | "only" could reject a brief that states the one condition without the word | A brief giving HP-to-zero as its one loss condition reads as "only"; the word rejects the decoy (a full 7-slot tray as a loss, the design page says "not a fail state"). | — |
| R21, R22 retitled | changed | The original wording rejected a usable-list-only brief | See the retitle table. All six rev2 briefs still pass. | — |
| R30, R64 volume rows | keep | count-bundle-v1 | R64 is the move template's one volume row and states the template; R30 counts table rows (table rule). `platform_delta_lint` count_bundle reads R64 as the volume row. | — |
| R122–R124 DM counts | keep | three rows from one audit = cascade group | Each count is its own reported fact, and a run can get one right and another wrong (rev2: Delivered 8 right in every run, Owed and Ready wrong). | — |
| Share rows R114–R121 | keep | one row per share target (one-row-per-write) | Eight separate writes, eight rows; each names the address and the file. | — |
| Draft grounding | PASS | a quoted span altered or paraphrased | 138 spans re-read in this run, 0 misses; three plan quotes corrected (above). | — |
| Every criterion maps to a plan row | PASS | a criterion with no plan row | R<n> = P<n> by construction; 126 = 126. | — |
| Fact duplication (gate 6) | PASS | a fact in three rows across deliverables | Unchanged from the plan (gate PASS: no fact in ≥ 3 rows); retitles changed wording only. | — |

Unresolved: the plan is PROVISIONAL until `/oe` passes (OE 10, 20 and 130 to update on the platform). The largest failure signature sits exactly at the 50% limit on the rev2 runs; that belongs to the design, not the rubric.

## Repair after /rubric round 1 (2026-11-12)

Report: `eval_reports/6aea4c201e1fa1ddfdd0a25d_3_rubric.md` — FAIL, score 1, reviewed sha256 1c44f4afdac1… (taken in: `/rubric` round 1, task_metrics event 6). Repaired export: `09_Rubrics.json` sha256 ea8009a35949… · 153 criteria (151 Outcome, 2 Process) · weight 371 (5 ×50 · 3 ×9 · 1 ×94). The reviewed export is kept at `plan/rubric/09_Rubrics.rubric_round1_reviewed.json`.

How: `plan/rubric/apply_rubric_fix_round1.py` applies the report's Fix List to the reviewed export and writes `plan/rubric/fix_round1_map.json` (new row → reviewed row, plan tag, part, change). It asserts that every new or changed title is in the Fix List word for word, that the 30 rows the report does not list keep their bytes, and that the set has the report's 153 rows.

| Change | Reviewed rows | Result |
|---|---|---|
| Possessive titles reworded | R2–R20, R23–R27, R29–R31, R33, R37, R42, R44–R58 | titles pasted from the Fix List |
| Deleted | R21, R22 (accept by absence) · R32, R34–R36, R38–R41, R43 (State samples over the cap of five) | 11 rows out |
| Split into owed (5) + holder (1) | R65–R67, R73–R84, R86–R94, R97–R104, R108, R109 | 34 rows → 68 |
| Added | Plushie Chick State Delivered (3) · Cannon's empty Board set (1) · two Process ordering rows (1 each) | 4 rows in |
| Weight moved | to 1: R2, R18, R26, R30, R48–R52, R55, R56 · to 5: R59–R61, R122, R123 | kind-of-work label follows the band |
| Evidence, as the report states | R3, R11, R19, R29, R30, R44, R46, R47, R64 and the split rows | binary lock, "the zip won't unpack", library Reject and the R64 sheet join removed |

Edits beyond the Fix List text, each forced by a fix: the Reject line of R2 and R4–R10 quoted the replaced title and now names the row; the owed rows of the binary group quote PlayableX's format line whole ('.fbx, .glb, or .blend …', re-read in C08H78VJG80) because the title now accepts .glb and .blend; the holder rows and the four added rows have new justification and evidence, written from the notes, the pack list, the deciding records and the prompt.

Not applied / open: the R23–R25 open problem stays as the report leaves it (a brief that also lists the Rocket or Explosion sound passes those rows); the held-back sounds are graded by their sheet and comment rows. No fix contradicted a record (Plushie Chick DES-334 Delivered, Cannon DES-398 Kind Weapon with an empty Board set, counts 8 / 39 / 49 all equal `oe_gen/model.py`).

Checks on the repaired export:
- `hg.py rubric-lint` → `{"findings": [], "count": 0}` (a first pass hit `vague_exemplar` on 35 rows of new evidence; the phrase is gone and the script now asserts it).
- `platform_delta_lint.py rubric` → PASS (R55 read as the move group's one volume row; R150–R153 claim links to files the Agent creates).
- `budget_rubric_rows_round1.py` re-mapped `rubric_rows` to the new numbers; `rubric_skeleton.py drift` → WARN: anchors 45.3% of the weight (Hard loss 30%), always-pass 22.1% (was 26.9%), C2 −11.6 points.
- Rehearsal on the rev2 runs (`plan/rubric/rehearse_fix_round1.py`, advisory): 31.0 / 31.0 / 31.0 / 50.7 / 48.2 / 50.9%, average **40.5%** (was 49.1%), 0/6 full passes, 4 failure patterns with the largest at 50%, SD 0.095 (report-only). Rows every run passes: 70 (weight 100). Rows every run fails: R55, R147, R148 (the same three as before: the 49 moves and the Owed and Ready counts).

Still to do: `/rubric` round 2 on this export. The plan (`09_Rubric_Writing_Plan.md`, `plan/rubric/rows.json`) still describes the 126-row set and still reads OE PROVISIONAL (`/oe` round 2 PASS was taken in today); it needs a refresh to the 153 rows before `/create-rubric-writing check`, whose PASS the all-fail gate requires.

## /rubric round 2 (2026-11-12)

`eval_reports/6aea4c201e1fa1ddfdd0a25d_3_rubric (1).md`: FINAL VERDICT **NON-FAIL**, Score 3, on `09_Rubrics.json` sha256 ea8009a35949… (the file on disk; intake `bind.hashes` PASS, metrics event 8). Overall Rubric Quality 3 (Minor on 11 of 153 rows, 7.2%); Weights, Category Balance, Process, Agent-Centric and Negative Criteria all 5; predicted all-fail PASS; no Major or Moderate issue. Every round 1 finding is reported fixed.

Scored Minor findings: R112–R126 even (the eight instrument comment rows: the evidence accepts "send the eight again", which the title does not) and R21–R23 (the sound decoy, carried from round 1).

Optional fix not applied: R36 and R112–R126 even, new titles and Accept clauses, marked "revised after check" with an open problem (a terse "Cello FBX" entry could still be failed). On the rev2 runs it changes no grade: runs 1–4 and 6 wrote no comment on DES-379–386 and fail these rows either way; run 5 wrote "the Cello FBX put back in the outgoing folder", which passes both wordings. Applying it needs another `/rubric` round, and after the verifier has run it would also need the verifier again.

Still to do: refresh the plan and `rows.json` to the 153 rows, then `/create-rubric-writing check` (the all-fail gate needs its PASS); the verifier results for `10_Baseline_Verifier_Results.md`.
