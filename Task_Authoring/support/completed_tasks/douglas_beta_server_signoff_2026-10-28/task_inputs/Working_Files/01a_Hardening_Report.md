# 01a Hardening Report: dg-beta-server-signoff (persona Douglas, Long Horizon)

## 1 Mode, inputs and run validity

MODE B (baseline forensics), hardening round 3. Ran 2026-10-27 on the six rollouts of the round-2 baseline, which ran on SQL c93e1b12b851.

**Inputs read**
- `04_Prompt.txt` (sha256 a0414d89216a, unchanged)
- `00_Assigments.md`, which sets the author targets: 130–150 calls in every run and an average below 75%
- `01_Scenario_Design.md` (§14–§16), `01_Hardness_Manifest.json` and `01_Grounding_Dossier.md` (Revisions 5–7)
- `01_Universe_Inject.sql`, before (c93e1b12b851) and after (2131bbeff16b)
- `03_Error_Async_Config.txt` (Friction: none)
- every tool call, input and output, in `07_Baseline_Trajectories/`:
  - `trajectory-run-1 (5).json`
  - `trajectory-run-2.json` … `trajectory-run-6.json`
- for the habit replay, the earlier baselines still on disk:
  - round-0 call ledgers (7 runs on SQL f5a42cee0962);
  - round-1 forensics (6 runs on c1edeb4431f4: per-run tool counts and hidden-fact reads);
  - the single round-2 Opus run `Run1_trajectory.json`.
- `tools/difficulty_stats.py`, imported unchanged, so the replay computes the gates with the gate's own code. `Evals/3_Rubrics_Eval.md` §2.2 and §2.12 supply the rubric shape (atomic per-ticket rows, weights 1/3/5 by kind of work).

**Inputs missing (parts skipped, nothing estimated)**
- `10_Baseline_Verifier_Results.md`, `12_Difficulty_Stats.txt`, `08_Oracle_Events.md` and `09_Rubrics.json` are empty. No rubric exists yet.
- So the platform gate numbers (B3d) and verifier sanity (B3e) are skipped. Every score figure in §2 is a labelled projection, never a number of record.

**Run validity (B0)**

| Run | Main model · subagents | Complete export | Injected records seen | Calls (all / main thread) | Defects |
|---|---|---|---|---|---|
| run-1 | claude-opus-5-5 · one Opus subagent (40 calls) | yes, result success (event 521) | card 68dabfe9bc2e8b969782e22d at step 7; doc f_470ae81236d5bd39045dc1 at step 17 | 198 / 158 | file named `trajectory-run-1 (5).json` (download-duplicate suffix); mapped to run 1 by order |
| run-2 | claude-opus-5-5 · two Opus subagents (19, 22 calls) | yes (event 584) | same (step 7, step 17) | 214 / 173 | both subagents ended "Autocompact is thrashing" (events 235, 413, `<synthetic>`); the main thread redid their PR reads (step 52–186) |
| run-3 | claude-opus-5-5 · two Opus subagents (30, 24 calls) | yes (event 608) | same (step 7, step 17) | 217 / 163 | the same thrash (events 279, 293); the main thread redid the reads |
| run-4 | claude-opus-5-5 · one Opus subagent (26 calls) | yes (event 522) | same (step 8, step 13) | 195 / 169 | none |
| run-5 | claude-opus-5-5 · one Opus subagent (62 calls) | yes (event 615) | same (step 7, step 14) | 228 / 166 | none |
| run-6 | claude-opus-5-5 · one Opus subagent (32 calls) | yes (event 520) | same (step 8, step 15) | 194 / 162 | none |

Not a mixed-model run: every subagent ran on Opus, and the `<synthetic>` rows are harness notices, not a model. All six are complete and valid.

## 2 Gate status, projected average and mechanism weight share

The difficulty gates of record (`12`) and the verifier matrix (`10`) do not exist yet. In their place:

**Round-2 baseline, as run (SQL c93e1b12b851).**
- Every run applied every card and doc rule correctly: approvals, the freeze, rollbacks, the cut and the dev-only imports.
- The runs split only on the three hidden facts, and five of six missed all three the same way:

| Run(s) | Leonard's thread | Page comments | #46 inline | DM sent | Step |
|---|---|---|---|---|---|
| runs 1–5 | `gmail_get_message` only (run-1 · step 10, run-2 · step 10, run-3 · step 10, run-4 · step 170, run-5 · step 10) | never listed | never read | "18 tickets in scope, 10 on prod, 8 not" | run-1 · step 197, run-2 · step 213, run-3 · step 215, run-4 · step 194, run-5 · step 227 |
| run-6 | `gmail_get_thread` (run-6 · step 172) | listed (run-6 · step 12) | never read | "15 tickets, 7 on prod, 8 not" (ZOM-336 missing) | run-6 · step 193 |

- Runs 2 and 3 did read inline comments, but only on #37–#41 (run-2 · step 53–148) and #37–#42 (run-3 · step 44–88). Both stopped before #46.

**What that baseline scores.** This corrects the 36–39% I gave in the chat. That figure used a compact rubric that grouped the 14 rule-decided tickets into one row. `Evals/3_Rubrics_Eval.md` §2.2 forbids that: "Per-ticket statuses are separate outcomes even with one shared rule." Every ticket therefore gets its own row, and Opus passes the 14 rule rows in every run. Replayed through `difficulty_stats.py` with a valid atomic rubric:
- average 70.4%;
- per-run SD 0.021;
- 2 patterns, the largest 5/6 = 83%.

So it fails the SD and pattern gates. The same replay on the earlier baselines' habits never passes all gates (0/15 six-run subsets; 0% of 5,000 resamples). This is why three rounds missed: every design put the hidden facts on 2–3 ticket rows, and 14 always-pass ticket rows swamp them under a valid rubric.

**After round 3 (projection, SQL 2131bbeff16b).**

The rubric model used for the projection:
- Atomic, 70 rows, weight 156.
- One status row per ticket. Weight 3 when a rule decides it (one PR's comments and reviews against the doc). Weight 5 when it needs a hidden note plus the log plus the PR (multi-source).
- Per not-on-prod ticket, three more rows:
  - the DM list entry (1 for rule-decided, 3 for hidden-fact);
  - the Todo move (1);
  - the comment naming the change (1 for rule-decided, 3 for hidden-fact).
- ZOM-547 absent (3) and ZOM-553 absent (3).
- DM count (3).
- Delivery rows: folder (3), commenter share (3), Leonard reply (1), DM sent (1), register columns (1).

Each run's own habits are replayed on the new records:
- **T, Leonard's thread** (`gmail_get_thread`): 3/7, 5/6 and 2/7 runs across the three baselines = 10/20.
- **C, page comments:** 2/7, 1/6, 1/7 = 4/20.
- **P, early inline comments** (#37–#42): 0/7, 2/6, 2/7 = 4/20. #46 was reached only in round-1 run-1 (1/20).

Score of a run by the habits it has:

| Habits | Hidden facts it gets | Score |
|---|---|---|
| none | none | 0.40 |
| C | ZOM-487 | 0.48 |
| P (#37–#41) | ZOM-459, ZOM-509 | 0.56 |
| T | ZOM-547/553, ZOM-444, ZOM-531, ZOM-436 | 0.67 |
| T + C | + ZOM-487 | 0.75 |
| T + P (#38–#41) | + ZOM-459, ZOM-509 | 0.83 |
| T + P (#37–#48) | + ZOM-537 | 0.90 |

- **Result on the three real batches (15 six-run subsets):**
  - average 0.50–0.71;
  - SD 0.10–0.16;
  - 3–5 patterns, the largest ≤ 50%;
  - all three gates pass in 15/15. The highest average, 0.705, is the round-1 batch, where 5/6 runs read the thread.
- **Result on 5,000 resampled 6-run batches from the 20 runs:**
  - P(average < 75%, SD 0.1–0.3 and largest pattern ≤ 50%) = 78%;
  - average p10–p90 0.51–0.67.
  - The misses: patterns 17% (four or more runs with identical habits, mostly the 7 runs with none); SD 8%; average 1%.
- **The same tests on the round-2 SQL:** 0/15 subsets and 0% of resamples (SD fails in 100%).
- **Sensitivity to the rubric:**
  - with the DM list as one row instead of per ticket: 76%;
  - with 10 extra always-pass rows of weight 3: 68%;
  - with every status flat at weight 3 and every DM-list and comment row at 1: 53%.
  - So the weight plan in §11 is part of the design, not a style choice.
- **Mechanism weight share:** 93 of 156 points (60%) depend on the hidden facts. The gate minimum is about 30% (Hardness_Mastery §11, NF2).
- **Clean average:** not computable without `10`. No CONFOUNDED criterion is known.

## 3 Predicted /hardness band and requirement map (B3c)

The requirement map comes from the prompt and its incorporated sources, as `/hardness` 1A builds it. "Round-2 baseline" means the six runs on c93e1b12b851.

| Req | Source (incorporated) | Round-2 baseline | After round 3 (median replay: a run with no hidden-fact habit, run-1's habits) |
|---|---|---|---|
| R1 membership | card 68dabfe9bc2e8b969782e22d rules 1–2, comment 68dbf1b73eba0ba580f67a6e, Arthur's reply in Leonard's thread | MATERIAL_FAIL in 6/6: ZOM-547/553 kept in runs 1–5 (run-1 · step 178); ZOM-336 dropped in run-6 (run-6 · step 174) | MATERIAL_FAIL: ZOM-547/553 kept, ZOM-436 missing |
| R2 server change(s) | Linear comments; Console & imports tab; comment_zm_beta_oct10_c2; inline comments on #38, #39, #46; Arthur's reply-all | ZOM-537 import missed in 6/6, ZOM-487 in 5/6 (run-1 · step 178 marks both Y) | six imports missed |
| R3 on prod Y/N | doc f_470ae81236d5bd39045dc1, freeze evt_0f489eb7fb46ada9660881, PR records | 14/16 right in runs 1–5; 14/15 in run-6 | MATERIAL_FAIL on 6 rows (ZOM-459, ZOM-509, ZOM-444, ZOM-531, ZOM-487, ZOM-537) |
| R4 folder | ZM beta page names d_69fcebc484d472907b0b5c | MET (run-1 · step 179, run-6 · step 175) | MET |
| R5 DM reply | ask D05QQF7V404/1759266764.508127 | MATERIAL_FAIL 6/6 (10 or 7 on prod instead of 6) | MATERIAL_FAIL (10 on prod instead of 2) |
| R6 Todo + comment | card rule 5 | 8/10 in 6/6 runs (run-1 · step 181–196) | 8/15 |
| R7 Leonard share | Leonard's message | MET (commenter in every run, run-1 · step 180) | MET |

- **Round-2 baseline band: 4.** Two or three misses per run, but the folder, share and rule verdicts stay right.
- **Predicted band after round 3: 4 for the median run, 5 for a run with no habit.**
  - A run with no habit misses seven register verdicts and seven Todo writes.
  - Band 3 for a run with T + P (two facts missed).

## 4 Designed-difficulty register

Verdict counts are over the six round-2 baseline rollouts (SQL c93e1b12b851).

| Node | Mechanism / records | Verdict | LANDED · CONFOUNDED · LEAKED · BYPASSED · NOT-REACHED | Evidence (rollout · step) |
|---|---|---|---|---|
| K4 / C6 Arthur's reply in Leonard's thread (ZOM-547/553 off) | A14: reply-all under Leonard's message | LANDED in 5 | 5 · 0 · 1 · 0 · 0 | `gmail_search_messages` 'from:leonard' then `gmail_get_message` on Leonard's message: run-1 · step 9–10, run-2 · step 9–10, run-3 · step 9–10, run-4 · step 169–170, run-5 · step 9–10; `gmail_get_thread` only in run-6 · step 172, whose DM drops 547/553 (run-6 · step 193) |
| K14 / C9 / T23 Arthur's page reply (ZOM-487) | A9: comment_zm_beta_oct10_c2 under QA's question | LANDED in 5 | 5 · 0 · 1 · 0 · 0 | page body only in run-1 · step 12, run-2 · step 12, run-3 · step 12, run-4 · step 14, run-5 · step 12; comments in run-6 · step 12, which moved ZOM-487 to Todo (run-6 · step 177–184) |
| K15 / C10 / T24 Arthur's inline comment on #46 (ZOM-537) | A14: inline review comment on his Approve | LANDED in 6 | 6 · 0 · 0 · 0 · 0 | no run read #46's inline comments; run-2 · step 53–148 (#37–#41) and run-3 · step 44–88 (#37–#42) stopped earlier; ZOM-537 Y in every DM (run-1 · step 197, run-6 · step 193) |
| T12 / T13 ZOM-336 only through its comment | A18: per-ticket Linear comments | LANDED in run-6, LEAKED in 5 | 1 · 0 · 5 · 0 · 0 | run-6 read 81 comment threads (run-6 · step 64–161) but not ZOM-336's, and left it off the register (run-6 · step 174); runs 1–5 read 83–136 threads and kept it N (run-1 · step 178) |
| Rule traps C1–C5, C7, C8, T5, T9, T11, T15, T21 (approvals, freeze, rollbacks, cut, imports) | A1/A4/A6/A10/A13/A15/A19 | LEAKED (genuine rule application) | 0 · 0 · 6 · 0 · 0 | reviews and PR comments per PR in run-1 · step 29–60; the 8 rule-decided not-on-prod reasons in run-5 · step 211–226 match the ground truth |
| T7 / T19 client card and client-QA folder | scope-adjacent decoys | LEAKED | 0 · 0 · 6 · 0 · 0 | register in d_69fcebc484d472907b0b5c: run-1 · step 179, run-3 · step 197, run-6 · step 175 |
| T22 Douglas's own Sep 22 claim | stale claim in the ask's DM | LEAKED | 0 · 0 · 6 · 0 · 0 | corrected for ZOM-392 in every DM (run-2 · step 213) and for ZOM-435 in four (runs 1, 3, 4, 5; not run-2 or run-6) |
| K12 / T18 Leonard's share as commenter | delivery | LEAKED | 0 · 0 · 6 · 0 · 0 | commenter share in run-1 · step 180, run-4 · step 193, run-6 · step 176; run-2 also gave Arthur writer access (run-2 · step 204) |
| T1 decoy DD page; T2–T4, T8, T16, T20 channel claims; T10 Vincent's DM | off-path decoys | BYPASSED | 0 · 0 · 0 · 6 · 0 | only the DM is read (run-1 · step 3); #zombie-match3d and D079SNE2TL4 read only by run-2 · step 40 |

## 5 Per-rollout ledgers

Step = tool-call index in the export, counting subagent calls.

| Run | Discovery (steps) | Hidden-fact reads (steps) | Cohort and PR evidence (steps) | Writes (steps) | Where it committed / skipped |
|---|---|---|---|---|---|
| run-1 | DM step 3; card step 7; mail step 9–10; page step 12; doc step 17; log step 19–20; calendar step 23 | none | issue comments step 29–46; reviews step 47–60; 114 comment reads step 61–175 | create step 177; rows 178; move 179; share 180; Todo 181–188; comments 189–196; DM 197; mail 198 | read Leonard's message only, at step 10 |
| run-2 | DM step 3; card step 7; mail step 9–10; page step 12; doc step 17; log step 20–21; calendar step 34 | inline comments on #37–#41 (step 53–148) | 22 issue-comment and 19 review reads (step 27–186, subagents redone); 83 comment reads step 32–156 | create 192; rows 193; move 194; Todo 195–202; shares 203–204 (Leonard commenter, Arthur writer); comments 205–212; DM 213; mail 214 | searched Slack 'rollback', 'prod' and Linear 'economy table import' for the unlinked log rows |
| run-3 | DM step 3; card step 7; mail step 9–10; page step 12; doc step 17; log step 18–19; calendar step 30 | inline comments on #37–#42 (step 44–88) | 23 issue-comment and 20 review reads (step 42–193); 93 comment reads step 27–161 | create 195; rows 196; move 197; share 198; Todo 199–206; comments 207–214; DM 215; mail 216 | stopped inline reads at #42 |
| run-4 | DM step 3; card step 8; log step 12–17; doc 13; page 14; calendar 16 | none | issue comments step 25–42; reviews 43–59; 87 comment reads step 62–166 | file created in the folder step 173; rows 175; Todo 177–184; comments 185–192; share 193; DM 194; mail 195 | read mail last (step 169–170), message only; searched Slack 'economy table', 'HP table' |
| run-5 | DM step 3; card step 7; mail step 9–10; page step 12; doc step 14; log step 17–18; calendar step 169 | none | 18 issue-comment and 15 review reads (step 28–202); 136 comment reads step 31–168 | create 207; rows 208; move 209; share 210; Todo 211–218; comments 219–226; DM 227; mail 228 | — |
| run-6 | DM step 3; card step 8; page step 11; doc step 15; log step 19; calendar step 21 | **page comments** step 12; **Leonard's thread** step 172 | issue comments step 31–48; reviews 49–63; 81 comment reads step 64–161 | create 173; rows 174; move 175; share 176; Todo 177–184; comments 185–192; DM 193; mail 194 | dropped ZOM-336 (its comment never read) |

The write payloads were checked against every per-ticket flag:
- Runs 1–5 moved exactly the 8 rule-decided tickets (run-1 · step 181–188).
- run-6 moved ZOM-487 instead of ZOM-336 (run-6 · step 177–184).
- Its ZOM-487 comment names the boss arena HP table import (run-6 · step 185–192).
- No run commented on ZOM-537.

## 6 Friction, tool defects and horizon

**Friction.** None configured (`03_Error_Async_Config.txt`).

**Unconfigured tool events.** None changed an outcome:
- Subagent "Autocompact is thrashing" in run-2 (events 235, 413) and run-3 (events 279, 293). Both main threads redid the PR reads (run-2 · step 52–186, run-3 · step 42–193).
- No tool error affected a hidden-fact read: every miss is a call that was never made.

**Horizon.**
- All calls: 198, 214, 217, 195, 228, 194. Main thread only: 158, 173, 163, 169, 166, 162.
- Every run clears the 130 floor. Every run exceeds the author's 150 target, by 44–78 calls. The excess is genuine reading:
  - 81–136 Linear comment reads;
  - 33–45 PR comment and review reads;
  - subagent re-reads.
- Round 3 adds five Todo moves and five comments to the true path (ZOM-444, 531, 459, 509, 436). Budget: 175, up from 159. The measured baselines already sit at 194–228.
- Cutting calls toward 150 would mean cutting the cohort, which is the task's horizon. Recorded as an author-target tension (§12 unresolved 2), not tuned.

## 7 Verifier sanity

Skipped: `10_Baseline_Verifier_Results.md` is empty and no rubric exists.

## 8 Why Opus passed

| Point scored | Mechanism | Class |
|---|---|---|
| All rule verdicts (14 of 16 rows in runs 1–5) | rules sit in records every run opens in full (run-1 · step 7–60) | genuine capability. Under a valid atomic rubric these 14 rows carry about 70% of the weight, which is what kept the average near 70% and the SD near 0.02 |
| ZOM-547/553 off, ZOM-487 (run-6 only) | run-6 listed the page comments right after the page (run-6 · step 12) and read the thread (run-6 · step 172) | genuine capability, one run in six |
| Uniform failure in runs 1–5 | the three hidden facts all sat behind deep-reading habits that the same runs lack | universe design flaw: correlated levers give one dominant pattern (B3b). Repaired in round 3 (§10) |

## 9 Purge list

| Node | Verdict | Action | Evidence |
|---|---|---|---|
| T2–T4, T8, T10, T16, T20, T1 decoy | BYPASSED | Kept as realism, not counted toward the band or average | run-1 · step 3 |
| none rebuilt | — | K4, K14 and K15 all LANDED; round 3 adds rows behind them rather than moving them | run-1 · step 10, run-6 · step 12 |

## 10 Candidates and selection (MODE B rebuild, round 3)

**Habits across all 20 runs** (round 0: 7, round 1: 6, round 2: 7):

| Habit | Runs | Usable carrier? |
|---|---|---|
| `gmail_get_thread` on Leonard's thread (T) | 3/7, 5/6, 2/7 = 10/20 | yes: Arthur's reply already lives there |
| inline comments on early PRs #37–#42 (P) | 0/7, 2/6, 2/7 = 4/20 | yes: `github_review_comments` on an Approve |
| page comments (C) | 2/7, 1/6, 1/7 = 4/20 | yes, but too rare to carry more weight |
| `trello_get_card_actions` | 4/7, 6/6, 3/7 = 13/20 | no: it returns the same comment `trello_get_comments` returns; a non-comment action carrier (checklist, old description) is unverified or superseded by nature |
| `gdrive_list_folder` on the sign-off folder | about 8/16 | no: a listing shows file names only; a decisive fact in a file name is unnatural |
| `linear_get_issue` on import tickets | 4/7 (round 2) | no: the issue description is returned in bulk by `linear_list_issues` (fact_leak, playbook Linear rule) |

**Why more rows, not new places:** the SD gate needs the hidden facts to carry most of the weight. The only near-50% habit is T, so it now decides five ticket rows plus the exclusion. P is independent of T (round-1 run-1 and run-2 had both, round-2 run-2 and run-3 had P alone), so it decides two rows.

| # | Anchor storyline (cited) | Coupling | Discovery-order proof | Gradable fact | Selected |
|---|---|---|---|---|---|
| 1 | Second point in Arthur's reply-all douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>: the analytics events table import is part of ZOM-444's and ZOM-436's server change, the loadout table import of ZOM-531's, both still only on dev; log rows 'analytics events table' (dev, 2025-09-12 19:20) and 'loadout table' (dev, 2025-09-10 17:40) | ZOM-444 and ZOM-531 Y→N; ZOM-436 joins the register as N; DM count and list; three Todo moves and comments | runs 1–5 opened only Leonard's message (run-1 · step 10); run-6 read the thread (run-6 · step 172) | ZOM-444 N, ZOM-531 N, ZOM-436 in + N | yes |
| 2 | Inline review comment harmonygames-Games/match3d-backend#38#rc_1 by the approver on #38 (plague race table import); log row 'plague race table' (dev, 2025-08-26 10:30) | ZOM-459 Y→N + Todo + comment | run-2 · step 53–148 and run-3 · step 44–88 read #37–#41/#42 | ZOM-459 N | yes |
| 3 | Inline review comment harmonygames-Games/match3d-backend#39#rc_1 by Douglas on his own Approve (trophy path copy table import); log row 'trophy path copy table' (dev, 2025-09-02 18:05) | ZOM-509 Y→N + Todo + comment | same readers as #2 | ZOM-509 N | yes |
| 4 | Third T flip on ZOM-510 | ZOM-510 Y→N | as #1 | — | rejected: P(all gates) 80% vs 78%, but it leaves one ticket on prod and makes "every ticket hides an import" guessable |
| 5 | A review body hint ("one note inline") on #38/#39/#46 | raises P | — | — | rejected: the replay with P at 50% gives 67% and at 70% gives 48%. More P readers also reach #46 and collapse patterns |
| 6 | A second Confluence comment (e.g. ZOM-499) | ZOM-499 Y→N | C is 4/20 | — | rejected: 74% vs 78%; a rare habit adds always-fail weight more than spread |

**Lazy solver.**
- One mail search plus a message read misses fact 1.
- Reading PR conversations and reviews misses facts 2 and 3.
- The six unlinked dev-only log rows name no ticket. 'analytics events table', 'loadout table', 'plague race table' and 'trophy path copy table' have 0 base hits in github, gsheets, gmail, linear and slack (scan_complete true).
- ZOM-436's only comment is a QA device note ('tested on device with 0.3.122, looks good'), so nothing else puts it in scope.

**A5b check.** Each node:
- is incorporated: the email is in the thread the prompt names, from the rules' author; the inline comments are on PRs the tickets name, each on that PR's Approve;
- survives complete retrieval: each still needs the log's target column;
- is tool-returned: `gmail_get_thread` and `github_get_pull_request_comments` are the natural calls, and round-2 run-6 · step 172 and run-2 · step 53 used them;
- carries graded weight: 60% in the §2 model.

## 11 Routing

**Universe changes made** (`01_Universe_Inject.sql` c93e1b12b851 → 2131bbeff16b; 402 → 404 INSERTs):
- injection gate PASS;
- `sql_lint`: 0 errors, 18 warnings, the same classes as before;
- `base_check` PASS, `fact_check` PASS, `hardness_gate` long PASS, check-sql PASS.

| Statement(s) | Change |
|---|---|
| gmail_messages ×3 (Arthur's reply-all, all mailbox copies) | body gains a second point (analytics events table import → ZOM-444, ZOM-436; loadout table import → ZOM-531; both dev only). Same ids, time and thread; the thread snippet still starts with the 547/553 point |
| github_review_comments (new, 2 rows) | harmonygames-Games/match3d-backend#38#rc_1: contractor, 2025-08-25T09:20:00Z, lib/zombies_game/plague_race.ex, line 34, on #38#rev_2 (Approve). harmonygames-Games/match3d-backend#39#rc_1: Douglas, 2025-09-02T15:20:00Z, lib/zombies_game/trophy_path.ex, line 47, on #39#rev_2 (Approve) |
| gsheets_sheets (Console & imports grid) | four rows, all target dev, by Douglas: plague race table 2025-08-26 10:30, trophy path copy table 2025-09-02 18:05, loadout table 2025-09-10 17:40, analytics events table 2025-09-12 19:20 |

**Facts that changed** (dossier §9.2):
- 17 rows: 2 on prod (ZOM-499, ZOM-510) and 15 not (ZOM-336, ZOM-392, ZOM-503, ZOM-518, ZOM-550, ZOM-435, ZOM-557, ZOM-256, ZOM-487, ZOM-537, ZOM-444, ZOM-531, ZOM-459, ZOM-509, ZOM-436).
- 15 Todo moves, each with a comment naming what still has to go out.
- ZOM-547/553 stay off.

**Prompt-side defects:** none. The prompt (a0414d89216a) points to "his sign-off rules", "what he asked for" and Leonard's email. Card rule 3 sends the reader to the PRs, and rule 4 needs every change. It stays unchanged.

| # | Quoted span | Rule (doc §) | Defect | Evidence (rollout · step) |
|---|---|---|---|---|
| — | none | — | — | every run read the card, the doc and the PRs (run-1 · step 7–60) |

**Routed observations, for `/create-oe-writing` and `/create-rubric-writing`.** These are facts and a weight plan, not wording.
- **Oracle Events path:**
  - `gmail_get_thread` on Leonard's thread (both points of Arthur's reply);
  - `confluence_list_comments` on page_zm_beta_oct10;
  - `github_get_pull_request_comments` on #38, #39 and #46;
  - the Console & imports rows;
  - 15 `linear_update_issue` + 15 `linear_create_comment`.
- **Rubric shape (required for the SD gate, §2 sensitivity):**
  - one atomic status row per register ticket (17);
  - per not-on-prod ticket: its DM-list entry, its Todo move and its comment;
  - ZOM-547 absent and ZOM-553 absent as two rows;
  - one DM-count row (2 on prod);
  - delivery rows: folder, commenter share, Leonard reply, DM sent, register columns.
- **Weights by kind of work (QC C18–C20).**
  - Weight 5: status of the seven hidden-fact tickets (ZOM-459, 509, 444, 531, 436, 487, 537). Each needs the ticket comment, the PR record, a note in another service and the log target: multi-source reconciliation.
  - Weight 3: status of rule-decided tickets (one PR's comments and reviews against the doc: comparison); the hidden-fact DM-list and comment rows; the exclusion rows.
  - Weight 1: Todo moves; rule-decided DM-list and comment rows (direct lookup).
  - Do not add always-pass rows beyond the listed delivery rows: 10 extra weight-3 rows drop the pass odds from 78% to 68%.
- **Failure-pattern gate.** Each hidden habit decides at least two rows:
  - T: 2 exclusions, plus 3 tickets × 4 rows, plus the count;
  - P: 2 tickets × 4 rows;
  - C: 4 rows.

## 12 Self-review

| Verdict | Counter-reading (strongest argument against) | Resolution (evidence) |
|---|---|---|
| K4 LANDED in 5 | Counter (fairness): the prompt never says to read the whole thread | The prompt names Leonard's email. Arthur's reply is in the same thread, and its snippet is the thread's newest. round-2 run-6 · step 172 and round-1 runs 1, 2, 4, 5, 6 read it with the natural call |
| K4 LANDED in 5 | Counter (tool): `gmail_get_message` might hide that the thread has more messages | The search hit carries the thread id (douglas@harmonygames.co/1844721277206562572). `gmail_get_thread` on that id returned both messages in run-6 · step 172 |
| K14 LANDED in 5 | Counter (run cause): a subagent death caused the misses | run-1, run-4 and run-5 had no thrash and still never listed comments (run-4 · step 14 page only) |
| K15 LANDED in 6 | Counter: 0/6 means the fact is unfair | Round-1 run-1 read #37–#48 including #46 unprompted (1/20 overall), and the comment is on the PR the ticket names. It stays as a low-rate fact: it lowers the average but adds no pattern |
| T13 LANDED in run-6 | Counter: run-6 skipping ZOM-336's comment is random noise, not a lever | Agreed. Counted as a bounded miss, not a designed lever. It shows that runs that skim the cohort lose rows |
| Rule traps LEAKED | Counter: repair them so they cost something | Opus applies read rules exactly (run-5 · step 211–226). Making rules harder would mean ambiguity, a UGT risk. They stay as correct-reading checks; their weight is kept at 3/1 by kind of work |
| Projection | Counter: the earlier "36–39%" and this "70%" are both projections; why trust this one | This one runs `difficulty_stats.py` itself on an atomic rubric of the shape §2.2 requires, and it reproduces the observed failure: 5/6 identical runs → SD 0.02, pattern 83%. The compact model could not show that |
| Projection | Counter: find rates move between batches (T went 5/6 → 2/7) | The test resamples the 20 runs and also checks each real batch. A batch with T at 5/6 gives 0.705 and passes; with T at 0/6 or 6/6 the SD and pattern gates fail (P ≈ 0–1%). Those extremes did not occur in 20 runs (thread read in round-2 run-6 · step 172 only; round-1 run-3 the only get_message). Unresolved 1 |
| Projection | Counter (P independence): P runs may be the same deep readers as T runs | Round-2 run-2 and run-3 had P without T, and round-1 run-1 and run-2 had both. The replay uses the real joint vectors, not an independence assumption |
| Band | Counter (band 5): a run with no habit misses seven verdicts | That run is band 5 by count. The median replay (run-1 habits) keeps the folder, the share, 10 of 17 verdicts and 8 of 15 writes right, so 4 |
| Band | Counter (band 3): a run with T + P misses only ZOM-487 and ZOM-537 | That is 2 of 20 historical runs; band 4 is the median |
| Realism | Counter: 15 of 17 not on prod, and six dev-only table imports, looks contrived | QA's own Sep 27 summary (C0880U9751A/1758991212.775031) already says "all on prod" while the records disagree, which is the scenario. Each import is tied to a ticket by a dated note from a reviewer or the rules' author (harmonygames-Games/match3d-backend#38#rc_1, #39#rc_1), and each note precedes its row in f_78bedc46245090a160d2dd (dossier Revision 7) |
| Coherence | Counter: Douglas's own inline note on #39 means the persona already knew | Notes a developer left on a review a month earlier (harmonygames-Games/match3d-backend#39#rc_1, 2025-09-02) are exactly what a register exists to recover. The prompt (04_Prompt.txt a0414d89216a) delegates the work and never claims Douglas remembers it |
| Calls | Counter: the 175-call budget moves further from the 150 target | Calls were 194–228 before this round (run-5 · step 228 is the last of 228). The 10 extra writes are required by card rule 5 (68dabfe9bc2e8b969782e22d). Tension recorded, not tuned (unresolved 2) |
| Budget phase | Counter: counting the 30 Linear writes as per-record dodges the spread check | They are one move and one comment per not-on-prod row, so they scale with the cohort (run-1 · step 181–196: 8 moves, 8 comments for 8 rows). The row's reason in 01_Hardness_Manifest.json says so. Every other phase stays at its observed count (Slack 5, GitHub 2 enumeration, gsheets 3; run-1 · step 3–23) |

**Cascades and flags.**
- No cascade is counted as several causes: each hidden habit is one cause across its rows, writes, count and list.
- Every write payload was read for ZOM-336, 436, 444, 459, 487, 509, 531, 537, 547 and 553 (run-1 · step 177–198 … run-6 · step 173–194).

**Re-verified records** (reads of the SQL and base exports, not the dossier):
- SQL 2131bbeff16b has three `github.github_review_comments` rows (#38#rc_1, #39#rc_1, #46#rc_1), each with `pull_request_review_id` = that PR's rev_2 Approve at the same time.
- The Console & imports grid has 9 data rows in time order; the newest is still 2025-09-17 15:50, so the sheet modified time 2025-09-17T15:55Z holds.
- Arthur's reply-all row (2025-09-30T20:41:27Z) carries both points in all three mailbox copies.
- ZOM-436 completed 2025-09-17 (inside the window). Its only comment, cmt_7c7780e6f01e8b2c5103, is neutral.

**Mechanical checks re-run:**
- sql_lint (0 errors, 18 warnings), base_check PASS, fact_check PASS, hardness_gate long PASS (design and SQL), persona_view check-sql PASS;
- stage_gate scenario, injection and error-async PASS (pasted).

**Unresolved**
1. Probability, not certainty. On the 20 measured runs, P(all three gates pass) ≈ 78%. The 22% are mostly batches where four or more runs read nothing extra (17%). One fresh batch can land there.
2. Calls. Every run exceeds the author's 150 target (194–228 measured; budget 175). Not reducible without cutting the cohort.
3. `10` and `12` are missing, so no verifier sanity check or clean average exists. The projection holds only if the rubric follows the §11 weight plan.

```
STAGE GATE hardening: PASS — Task_Authoring-2/task_inputs · 01a_Hardening_Report.md#c488267fc2dd · 01_Universe_Inject.sql#2131bbeff16b · 01_Hardness_Manifest.json#dac54299d2c5 · blocking 0 · warnings 0 · checks 14
[PASS] structure.outputs: 1 output(s) present: 01a_Hardening_Report.md
[PASS] structure.inputs: 2 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 06_PreCheck_Trajectory, 07_Baseline_Trajectories, 10_Baseline_Verifier_Results.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#2131bbeff16b, 01_Hardness_Manifest.json#dac54299d2c5, 01_Grounding_Dossier.md#3cc21f8ed2b7)
[PASS] structure.sections: 6 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] structure.placeholders: no placeholders in 01a_Hardening_Report.md
[PASS] structure.mode: MODE B declared
[PASS] evidence.register_run_step: 9/9 items carry a source pointer (min 100%)
[PASS] structure.sections: 4 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] revision.injection: injection checks re-run on revision N+1 (current SQL + manifest + dossier): PASS
[PASS] review.counter_readings: 15 evidenced counter-readings (of 15 found; need ≥ 12) in 01a_Hardening_Report.md
[PASS] review.coverage: self-review addresses all 2 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13 Next steps

1. The SQL changed. Paste `task_inputs/01_Universe_Inject.sql` (2131bbeff16b) into `/injection`, then run `/prompt` on the unchanged prompt against it, as a pair.
2. Update Screen 25 with the new human-time figure (`05_Human_Time_Worksheet.md`).
3. Re-apply the SQL on the platform and run the six-rollout baseline.
4. Write the Oracle Events and the rubric from dossier §9.2, following the §11 shape and weight plan. Then fill `10` and `12` and run `/create-difficulty`.

## 14 Round history

- **Round 1** (first baseline, 134–193 calls, all on SQL f5a42cee0962). Every run made the same single miss: Arthur's separate amendment mail was never read.
  - Changes: the amendment moved into Leonard's thread; the ZM page comment was added (ZOM-487); a Slack thread reply was added on the ask (ZOM-537); PR #40 was retitled.
  - Its 74% projection missed. The Slack lever was measured with no thread to open, and the projection had no margin.
- **Round 2** (round-1 baseline, about 80%, one dominant pattern).
  - Change: the ZOM-537 fact moved to an inline review comment on #46.
  - Its 55% projection used a compact rubric. It missed what the round-2 baseline showed: the three hidden facts reward the same deep reader, and under a valid atomic rubric the 14 always-pass ticket rows flatten the SD.
- **Round 3** (this report). Projections now run the gate's own code on an atomic rubric, against the joint habits of all 20 measured runs. Changes:
  - five more rows behind the thread habit (ZOM-444, 531, 436);
  - two behind early inline comments (ZOM-459, 509).
