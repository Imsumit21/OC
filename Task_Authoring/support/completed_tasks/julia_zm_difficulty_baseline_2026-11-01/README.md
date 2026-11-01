# Julia: ZM difficulty baseline register (submitted 2026-11-01)

Persona Julia Lawson (Product Manager) · Long Horizon · Product / Engineering Ops / Retrieval · difficulty mode medium · env hg4-with-gsuite-bundle-1174 · universe hg4-2026-08-31 · universe date Oct 1, 2025 07:00 · platform task 6adfee3ef9092601a61245bb (id taken from the eval reports; 00_Assigments.md left taskId blank).

`task_inputs/` is the full slot folder as submitted (including `Run1_trajectory.json` and `02_Chnagelog.json`). `eval_reports/` holds every platform eval report, renamed by stage, verdict and round (`0_injection_*`, `1_prompt_*`, `1a_hardness_*`, `2_oe_*`, `3_rubric_*`). `work/jl_difficulty/` holds the builders (moved from `support/task_work/`): design/SQL/manifest/dossier builders v1 to v13pre, hardening rounds `harden_r5..r7.py` with matching `manifest_`, `dossier_`, `report_` scripts, and `r7/` (round-7 truth, OE, OE check, rubric and rubric-check builders: `sqlrows.py`, `truth7.py`, `build_oe_r7.py`, `build_rubrics_r7.py`, `build_rubrics_r7b.py`, `build_rubrics_r7c.py`).

## Final state
- Injection SQL `01_Universe_Inject.sql` sha256 b64bc2f2c6dc (187 INSERT/UPDATE). Friction: none. No reference files.
- Prompt sha256 22f26066688c (Julia's voice): take Leonard's DM ask, build the register his way in the ZM Difficulty folder, share with everyone on Monday's tuning invite, do what his rules say on the tickets, reply to Leonard in the DM.
- Oracle Events: 45 events, sha 1a7525103716; /oe PASS 5 (`2_oe_PASS_r3.md`).
- Rubric: 81 rows, weight 173, sha 784ad0b6eef8; /rubric went FAIL r4 (bundled rows), FAIL r5 (wording edges), fixed by copying the checked Fix List text verbatim.
- Evaluator path: /injection 13 rounds (final PASS r13), /prompt 14 rounds (final PASS 5 r14), /hardness 7 rounds (final NON-FAIL 3 PROCEED r7), 7 hardening rounds in total.
- Baselines (6/6 completed, verifier 66/73/81/75/77/76 of 81): weighted 68.2 / 76.9 / 100 / 82.7 / 88.4 / 86.7, average 83.8% (passes QC < 90% and the medium-mode 85% cap, misses the Evals < 75%), pass@1 1/6, population SD 0.099 (sample 0.108), 4 failure patterns, largest 40%, golden run-3 862 counted calls (range 357 to 1209). No all-fail rows. Report: `task_inputs/Working_Files/12_Difficulty_Stats.txt`.
- Platform rubric atomicity linter flagged criterion d8f33906 (ZOM-254 Replaced + replaced by ZOM-282); answered with an invalidation note (rule 4 defines Replaced by naming the replacer). The splitting alternative was not applied.

## Key answers
- Register: 23 ticket rows: 15 Live, 4 Editor only (ZOM-173, 200, 277, 315), 3 Not shipped (ZOM-202, 280, 293), 1 Replaced (ZOM-254 replaced by ZOM-282). Off the list: ZOM-162/163/201/250 (Leonard's DM thread reply), ZOM-30/49/50/161/262/275 (Leonard's thread), ZOM-258 (notes doc), ZOM-312 (Blake 'not tiers' on PR #265), ZOM-295 (Blake 'not tiers' inline review on PR #271).
- Tickets tab columns: ticket, title, Linear state, status, replaced-by, plus Robert's three from the group-chat thread: Linear assignee, day marked done in Pacific time (blank if never), Linear priority.
- Rules in force tab: starting tier after the first 10 games (wins and losses) when average CPM is strictly above 90; promotion/demotion windows as ZOM-42 words them; enrage hp boost 0.
- 9 Linear comments: ZOM-199 (build check is > 90, 10th game), ZOM-254 (replaced by ZOM-282), and the 7 Editor only / Not shipped tickets naming iOS 0.3.49 and Android 0.3.133.
- Shares: Robert writer, Brian and Leonard commenter, Arthur reader.
- DM reply to Leonard: 23 tickets, 15 Live, 4 Editor only with keys, 3 Not shipped with keys, 1 Replaced (ZOM-254 to ZOM-282).

## Lessons carried forward
- Judgement traps (status calls, title-match scope rules) never landed across 28+ runs; only hard-to-reach carriers discriminated: Slack DM thread replies (slack_read_thread with a user id returns channel_not_found), PR inline review comments (GitHub 'in:comments' search misses them), and the ZOM-281 'tiers:' note on a non-Blake assignee.
- Levers whose values sit in a mail every run reads, or that a card names explicitly (findable by sender search), get met by default; Pacific-time conversion landed 0/6.
- Even with 7 hardening rounds the average sat at about 84% with SD on the 0.1 edge: one dominant scope choke point. Design 3 to 4 independent partial-source traps, each with at least 2 unique graded rows, before the first baseline.
- /rubric: never bundle status + citation or N-key exact-set rows; 'leaves X off' rows fail Negative Criteria; copy checked Fix List text verbatim.
- Platform verifier export HTML-escapes '>' as &gt; and bolds some titles; unescape a scratch copy before `difficulty_stats.py --build`.
- Local gate diversity.authority_share fails structurally when one Trello card governs most rows (same as Robert, Douglas, Frederick); it does not affect the platform.
