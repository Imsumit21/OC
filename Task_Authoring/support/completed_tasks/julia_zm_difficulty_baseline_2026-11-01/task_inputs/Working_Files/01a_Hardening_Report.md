# 01a Hardening Report — jl-zm-difficulty-baseline · rounds 1–7

## 1 Mode, inputs and run validity

**Round 7: MODE B (baseline, no verifier yet).** Six Opus 5.5 baseline rollouts on SQL f6afeda7b086 (round 6), after /injection PASS, /prompt PASS 5 and /hardness NON-FAIL 3 PROCEED on the same SQL (task_inputs/Audit-Report/0_injection_PASS_r12.md, 1_prompt_PASS_r13.md, 1a_hardness_NONFAIL_r6.md). No verifier file exists yet; verdicts below come from the write payloads.

Inputs read:
- task_inputs/07_Baseline_Trajectories: trajectory-run-1 (3).json, trajectory-run-2.json … trajectory-run-6.json, every tool call and result
- the round-6 hardness run (task_inputs/Run1_trajectory.json), two round-5 single runs and the round-5 batch's call inventory, for the replay over 15 runs

Run validity: all six completed with a DM reply (run-1 · event 2369, run-2 · event 2076, run-3 · event 3885, run-4 · event 1980, run-5 · event 2116, run-6 · event 2789); none errored.

| Rollout | Calls | Leonard's thread replies | Robert's thread | Register write | Brian | #271 reviews | #271 inline comments |
|---|---|---|---|---|---|---|---|
| run-1 | 900 | not opened | read (run-1 · event 80) | 34 rows (run-1 · event 2326) | writer (run-1 · event 2335) | not read | not read |
| run-2 | 825 | read (run-2 · event 20) | read (run-2 · event 100) | 24 rows, all right (run-2 · event 2041) | commenter (run-2 · event 2052) | run-2 · event 1963 | run-2 · event 1986 |
| run-3 | 1356 | read (run-3 · event 20) | read (run-3 · event 87) | 24 rows, all right (run-3 · event 3844) | commenter (run-3 · event 3858) | run-3 · event 1231 | run-3 · event 3812 |
| run-4 | 716 | read (run-4 · event 20) | read (run-4 · event 94) | 24 rows, all right (run-4 · event 1946) | commenter (run-4 · event 1956) | run-4 · event 1866 | not read |
| run-5 | 825 | read (run-5 · event 21) | read (run-5 · event 74) | 24 rows, all right (run-5 · event 2076) | commenter (run-5 · event 2092) | run-5 · event 1990 | run-5 · event 2051 |
| run-6 | 1061 | read (run-6 · event 10) | read (run-6 · event 75) | 24 rows, all right (run-6 · event 2751) | commenter (run-6 · event 2765) | run-6 · event 2665 | not read |


**Round 6: MODE B (baseline, no verifier yet).** Six Opus 5.5 baseline rollouts on SQL 7966b1496ad9 (round 5), plus the /hardness run on the same SQL (NON-FAIL 4, task_inputs/Audit-Report/1a_hardness_NONFAIL_r5.md). The rubric was not yet brought to round 5, so no verifier file exists; verdicts below come from the write payloads.

Inputs read:
- task_inputs/07_Baseline_Trajectories: trajectory-run-1 (1).json, trajectory-run-2.json … trajectory-run-6.json, every tool call and result
- two earlier baseline batches of the same task (round 4 and round 5 SQL, 12 rollouts, read only) and four hardness runs, for read-habit rates across 22 runs
- 0_injection and 1_prompt PASS reports on 7966b1496ad9 (task_inputs/Audit-Report/*_r5.md)

Run validity: all six completed with a DM reply (run-1 · event 1583, run-2 · event 2330, run-3 · event 2167, run-4 · event 2222, run-5 · event 2365, run-6 · event 2134); none errored.

| Rollout | Calls | Thread replies opened | Card | Notes doc | Blake's reply (own thread) | PR #265 review comments | Register rows | Brian |
|---|---|---|---|---|---|---|---|---|
| run-1 | 639 | none | run-1 · event 20 | run-1 · event 27 | run-1 · event 54 | run-1 · event 1486 | 34 (run-1 · event 1540) | writer |
| run-2 | 851 | tried with the user id, channel_not_found, no retry | run-2 · event 22 | run-2 · event 29 | run-2 · event 57 | not read | 35 incl. ZOM-312 (run-2 · event 2280) | writer |
| run-3 | 872 | both (run-3 · event 19) | run-3 · event 30 | run-3 · event 38 | run-3 · event 58 | run-3 · event 2047 | 24, all right (run-3 · event 2122) | commenter |
| run-4 | 881 | none | run-4 · event 20 | run-4 · event 27 | run-4 · event 65 | run-4 · event 2108 | 34 (run-4 · event 2177) | writer |
| run-5 | 919 | both (run-5 · event 19) | run-5 · event 32 | run-5 · event 40 | run-5 · event 64 | run-5 · event 2273 | 24, all right (run-5 · event 2330) | commenter |
| run-6 | 703 | both (run-6 · event 18) | run-6 · event 27 | run-6 · event 34 | run-6 · event 59 | run-6 · event 2052 | 24, all right (run-6 · event 2099) | commenter |


**Round 5: MODE B (baseline).** Six Opus 5.5 baseline rollouts on SQL dd7536cdea3f, graded by the platform verifier on the 68-row rubric (/rubric PASS 5).

Inputs read:
- task_inputs/07_Baseline_Trajectories: trajectory-run-1 (8).json and trajectory-run-2 … trajectory-run-6.json, every tool call (parsed copies in the scratchpad, base4/run1–6.json)
- task_inputs/10_Baseline_Verifier_Results.md (the export HTML-escapes '>' as '&gt;'; rows R25 and R43 bind after unescaping a scratch copy; the saved input is unchanged)
- 04_Prompt.txt, 08_Oracle_Events.md, 09_Rubrics.json; the platform linter "Largest baseline failure signature must be at most 50%"

Inputs missing: 12_Difficulty_Stats.txt (not yet written by /create-difficulty). The gate values below come from tools/difficulty_stats.py run on file 10, not from estimates.

Run validity (B0): all six completed with a final DM (run-1 · event 3522, run-2 · event 2275, run-3 · event 2307, run-4 · event 2460, run-5 · event 2153, run-6 · event 1993); none errored; main agent and subagents on Opus 5.5; Friction: none. Content matches SQL dd7536cdea3f: every run's DM read (run-1 · event 6 … run-6 · event 6) returns Leonard's ask, and every card read returns the round-4 checklist (run-1 · event 20, run-4 · event 25).

| Rollout | Calls | Thread replies opened | Card (checklist, actions) | Notes doc | Mail thread | PR #265 review comments | Register rows | DM |
|---|---|---|---|---|---|---|---|---|
| run-1 | 1,286 | none | run-1 · event 20 | run-1 · event 27 | run-1 · event 44 | reviews only (run-1 · event 3337), no review comments | 35 (+ZOM-312) (run-1 · event 3479) | 35 / 22 Live / 9 Editor only, keys listed (run-1 · event 3522) |
| run-2 | 810 | none | run-2 · event 21 | run-2 · event 28 | run-2 · event 41 | read (run-2 · event 2167) | 34 (run-2 · event 2212) | 34 / 22 / 8, no keys (run-2 · event 2275) |
| run-3 | 890 | none | run-3 · event 18 | run-3 · event 25 | run-3 · event 48 | read (run-3 · event 2172) | 34 (run-3 · event 2261) | 34 / 22 / 8, no keys (run-3 · event 2307) |
| run-4 | 892 | none | run-4 · event 21, 25 | run-4 · event 30 | run-4 · event 50 | read (run-4 · event 1660) | 34 (run-4 · event 2415) | 34 / 22 / 8, keys listed (run-4 · event 2460) |
| run-5 | 853 | both (run-5 · event 19, 21) | run-5 · event 31 | run-5 · event 38 | run-5 · event 50 | read (run-5 · event 2078) | 24, all right (run-5 · event 2118) | 24 / 16 / 4 / 3 / 1, keys (run-5 · event 2153) |
| run-6 | 765 | none | run-6 · event 19 | run-6 · event 27 | run-6 · event 41 | read (run-6 · event 1887) | 34 (run-6 · event 1951) | 34 / 22 / 8, keys listed (run-6 · event 1993) |

Every run read the code (TierManager.cs: run-1 · event 3409, run-5 · event 553), the enrage sheet and ZOM-42; the Rules in force tab, shares other than Brian, the 9 required comments and the ZOM-254 → ZOM-282 line were right in all six.


**Round 4: MODE B (baseline).** Six Opus 5.5 baseline rollouts on SQL 2ee488e28ab5 and prompt 22f26066688c, in task_inputs/07_Baseline_Trajectories (trajectory-run-1.json … trajectory-run-6.json). All six completed (result success, is_error false), none errored, Friction: none.

| Rollout | Calls | Thread under the ask | Register rows | Shares | Comments | DM reply |
|---|---|---|---|---|---|---|
| run-1 | 889 | read (run-1 · event 13 failed with Leonard's user id; event 17 with D05HB64NMQU) | 28, all statuses right (run-1 · event 2245) | right (run-1 · event 2257–2263) | 13 right (run-1 · event 2266–2290) | 28/16/8/3/1, 11 keys (run-1 · event 2293) |
| run-2 | 1,074 | read (run-2 · event 17) | 28 right (run-2 · event 2998) | right | 13 right | 28, 11 keys (run-2 · event 3041) |
| run-3 | 1,020 | **missed**: run-3 · event 13 failed (channel_not_found) and was not retried | 34 (+ZOM-30/49/50/161/262/275 as Live) (run-3 · event 2683) | right | 13 right | 34 / 22 Live, no keys (run-3 · event 2733) |
| run-4 | 897 | **missed**: run-4 · event 6 parse printed text only, no thread call | 34 (run-4 · event 2430) | right | 13 right | 34 / 22 Live, no keys (run-4 · event 2476) |
| run-5 | 812 | read (run-5 · event 22) | 28 right (run-5 · event 2028) | right | 13 right | 28, 11 keys (run-5 · event 2071) |
| run-6 | 769 | read (run-6 · event 24) | 28 right (run-6 · event 1925) | right | 13 right | 28, 11 keys (run-6 · event 1973) |

Every run found the checklist, Blake's 'not tiers' review on #265 (run-1 · event 2160) and the attached notes doc (run-1 · event 26). The Rules in force tab was right in all six (starting tier after the 10th game, > 90, both demotion rules, the level drop, the enrage copy). Grader script: scratchpad base/grade.py.


**MODE B (pre-check).** There is one unhinted Opus 5.5 run and no baseline yet, so this report gives provisional verdicts, a predicted `/hardness` band and a projected average. It has no gate statistics.

Inputs read:
- 00_Assigments.md
- 01_Universe_Inject.sql (before: a58a5d1e61b3; after: 10c1ee9238d4)
- 01_Grounding_Dossier.md, 01_Scenario_Design.md, 01_Hardness_Manifest.json
- 04_Prompt.txt (22f26066688c, unchanged)
- 03_Error_Async_Config.txt (Friction: none)
- 06_PreCheck_Trajectory/trajectory.json (a copy of task_inputs/Run1_trajectory.json, sha256 ecfae005…, 2,174 events)
- the platform report /home/sumit/Downloads/6adfee3ef9092601a61245bb_1a_hardness.md (FAIL 2, Easy, gate HOLD INSUFFICIENT_DIFFICULTY)

Inputs missing: 07_Baseline_Trajectories, 10_Baseline_Verifier_Results.md and 12_Difficulty_Stats.txt (no baseline yet). There are no reference files.

**Run validity (B0)** for run-1:
- **Model:** the main agent and all 11 subagents ran on claude-opus-5-5 (741 tool calls, all claude-opus-5-5).
- **Hints:** none. The run starts cold: profile (event 2), Leonard search (event 4), the DM (event 6), then the card search (event 13).
- **Source match:** the run saw the SQL a58a5d1e61b3 overlay. Its results contain the rule-5 "Copy its Live tab as it stands" text (event 13) and the comment "written out (ATK on its own" (event 16).
- **Completeness:** the run completed with a final reply (event 2171). The second init (event 907) is the same session after background agents, not a new run.
- **Horizon:** 741 calls, 619 of them `linear_list_comments` (415 in subagents). That is far above the author's ≥ 120-call target.

**Round 2 inputs.**
- The platform report /home/sumit/Downloads/6adfee3ef9092601a61245bb_1a_hardness (1).md: FAIL 2, Easy, on SQL 10c1ee9238d4.
- Its run is run-2: "Run1_trajectory (2).json", sha256 a6b52c7a…, 222 calls, Opus 5.5. That file was not supplied to this workspace, so run-2 is **not read** here. Every run-2 verdict below cites the platform report's event numbers, marked "(report)".
- What run-2 did:
  - opened Leonard's thread reply (run-2 · event 13, 20, 29 (report));
  - fetched the card with checklists and actions (run-2 · event 18, 22 (report));
  - scanned comments only on keyword and Blake-assigned tickets, about 107 (report §6);
  - wrote "after the 10th level" for the starting tier although it read TierManager.cs (run-2 · event 553, 658 (report)).

Round 2 changed SQL 10c1ee9238d4 → see §11.

**Round 3 inputs.**
- The platform report /home/sumit/Downloads/6adfee3ef9092601a61245bb_1a_hardness (2).md: FAIL 2, Easy, on SQL 52c581f442c1.
- Its run is run-3: /home/sumit/Downloads/trajectory-run-1 (4).json, sha256 1c38d9bc8a99…, 836 calls (596 top-level, 240 in 4 subagents that failed with autocompact), Opus 5.5. It is **read** here; run-2's file (/home/sumit/Downloads/trajectory-run-1 (3).json, sha256 a6b52c7a120e…) is now read too.
- What run-3 did:
  - opened the thread reply (run-3 · event 29) and the card with checklists and actions (run-3 · event 22);
  - scanned the comments of 499 ZOM tickets itself after its subagents failed (739 `linear_list_comments` calls), so it found ZOM-281 (L3);
  - wrote "10 games played, wins and losses both count" for the starting tier (run-3 · event 2074), so L4 did not bind;
  - asked `trello_get_card` for attachments with the string "true", got "attachments must be true, false, or \"cover\"" (run-3 · event 18) and retried without them (run-3 · event 22); run-2 did the same (run-2 · event 18, 22);
  - used GitHub only through `github_list_pull_requests` (run-3 · event 320–434), `github_search_code` and `github_get_file_contents` (run-3 · event 2001–2050): 0 calls to `github_get_pull_request_reviews` or `github_get_pull_request_comments` in 836 calls; run-2 the same (0 in 222).

Round 3 changed SQL 52c581f442c1 → see §11.

## 2 Gate status, projection and mechanism weight share

**Round 7 projection from the round-6 SQL runs** (payloads scored against the round-6 answer key): runs 2 to 6 pass every row (24 rows and statuses, all 69 assignee / done day / priority cells, 9 comments, shares, the DM with 24 / 16 / 4 / 1 / 3 and the keys: run-2 · event 2076, run-6 · event 2789); run-1 fails the thread rows (34 rows at run-1 · event 2326, Brian writer at run-1 · event 2335). Projected average about 95%, pass@1 5 of 6, one failure pattern. With difficulty mode medium the average limit is 85%; pass@1 and the pattern gate fail regardless. The round-6 lever (Robert's thread) landed 0 of 6: every run read it (run-1 · event 80, run-5 · event 74).

**Round 7 levers and replay.** (1) Blake's 'not tiers' inline comment on PR #271 (ZOM-295 off): over 15 runs, #271's inline comments were fetched by 5 (run-2 · event 1986, run-3 · event 3812, run-5 · event 2051, plus two earlier runs); run-4 and run-6 read #271's reviews list but not its inline comments (run-4 · event 1866, run-6 · event 2665). GitHub comment search does not reach review comments. (2) Robert's done day in pacific time: every run wrote the UTC day for ZOM-200, ZOM-274 and ZOM-282 (run-3 · event 3844, run-6 · event 2751). Replay of lever 1 alone: round-5 batch 6 failing runs in 3 patterns (largest 50%), average about 78%; round-6 batch 3 failing runs, two identical (largest 67%), so lever 2 has to split them. Risks stated: the approval with an empty body may draw more runs into the inline comments than the replay shows; lever 2 compliance is untested.


**Round 6 projection from the round-5 SQL runs** (no verifier file; rows scored from the payloads on the 68-row rubric): runs 3, 5 and 6 pass every row; runs 1, 2 and 4 fail the thread rows (R5–R7, R39, R52–R55, 38 of 160). Projected average about 88%, one failure pattern (100% of failing runs), pass@1 3/6. Both gates fail; the round-5 levers (T30 Gmail reply in its own thread, T31 builds in comments) landed 0/6: every run found the reply with a sender search (run-1 · event 54, run-3 · event 58) and every run named the builds, which also sit in the first mail (run-1 · event 1556, run-6 · event 2127).

**Read-habit rates across 22 runs** (three baseline batches plus four hardness runs): thread replies opened about 45%; PR #271 review comments about 50%; PR file lists about 55%; PR #243 / #244 review comments 70 to 75%; code about 80%; the card, notes doc, both Blake mails, the invite and every Linear comment 100%. Every judgement trap was resisted in 22 of 22 runs (all 24 statuses right in every register); ZOM-312 was kept only by runs that skipped the #265 review comments (2 of 22), ZOM-258 once.

**Round 6 lever:** a third thread reply in a different conversation (group chat CAFC495E4006), carrying three graded Tickets-tab columns, so graded weight behind thread replies rises from 24% to about 45% and failing runs split by which threads they opened. Monte Carlo (scratchpad r6/mc8.py, 3 columns, 5 spot checks plus a volume row each): with the threads missed together 50% of the time and a 55% miss rate, average about 74%, P(largest pattern ≤ 50%) about 0.6, P(all gates) about 0.25; when runs open all threads or none (correlation 0.9) P(all gates) falls to about 0.02. The risk is stated, not hidden.


**Round 5 baseline gates** (tools/difficulty_stats.py on 10_Baseline_Verifier_Results.md, platform view = valid view, no corrections):

| Gate | Value | Verdict |
|---|---|---|
| errored runs | 0 of 6 | PASS |
| pass@1 | 1/6 (run-5) | PASS |
| average weighted pass | 77.1% (76.2 / 66.9 / 66.9 / 76.2 / 100 / 76.2) | FAIL (< 75%) |
| per-rollout SD | 0.111 | PASS (band edge) |
| failure patterns | 2; largest 60% of 5 failing (run-1, run-4, run-6) | FAIL (signature over-concentrated) |
| horizon | golden run 832 counted calls | PASS |

**Clean average:** 77.1%, the same. No CONFOUNDED criterion: the verifier matches the trajectories on every row (§7), and no all-fail row exists.

**Mechanism weight share:** 38 of 160 (24%) depends on the thread replies (R5–R7, R39, R52–R55), plus 13 on the DM keys for runs that also skip them. Every other row passed in all six runs. Below the ~30% floor (Hardness_Mastery §11, NF2), so even 5 of 6 landed misses leave the average at 77%.

**Concentration:** one carrier (Slack thread replies) drives every failure. Runs either open every thread (run-5 · event 19, 21) or none, so both thread levers (L1, L7) cascade into the same rows: pattern 1 = run-1/4/6, pattern 2 = run-2/3 (pattern 2 adds the keys the L1 reply asks for).

**Round 5 projection** (Monte Carlo over the per-run habits observed here: thread miss pT, Gmail reply miss pG, review-comment miss 0.17, keys omitted 0.4 when the thread is missed; scratchpad rub/mc5.py), with the two round-5 levers and their planned rows:

| pT / pG | Projected average | P(avg < 75%) | P(largest pattern ≤ 50%) |
|---|---|---|---|
| 0.5 / 0.5 | 72.4% | 0.66 | 0.94 |
| 0.6 / 0.5 | 69.8% | 0.79 | 0.92 |
| 0.33 / 0.6 | 75.1% | 0.50 | 0.96 |
| 0.8 / 0.5 | 64.3% | 0.96 | 0.91 |

Lever-dependent weight rises from 24% to about 45%: the Gmail reply now decides the Editor only statuses (4 status rows, 4 key rows, 4 comments, the counts) and ZOM-199's comment, and the thread reply decides the build numbers in 7 comments.


**Round 4 baseline gates (on 2ee488e28ab5, before this round's change).** pass@1 4/6 = 67% (> 50%: FAIL, too easy). Projected average 83–88% under any fair rubric: runs 1, 2, 5, 6 near 100%, runs 3, 4 lose only the thread-reply rows.

**Round 4 weight plan** (facts and weights for /create-rubric-writing; the "exactly" set rows are the natural reading of a register):

| Block | Rows · weight | Depends on |
|---|---|---|
| non-lever | 64: Not shipped set 3; ZOM-254 replaced by ZOM-282 3; ZOM-199/254 comments 6; the 7 Editor only + Not shipped comments 5; folder 3; Robert writer 3; Leonard commenter 3; Arthur reader 3; two tabs 3; rules tab 5 × 3 = 15; DM place 3; ZOM-312 off 3; ZOM-258 off 3; DM 254 → 282 3; DM starting tier 5 | — |
| L1 (thread under the ask) | 26: 6 exclusions × 3 = 18; the Live set is exactly the 16 (5); Not shipped keys in the DM 3 | Leonard's reply under the ask |
| L7 (thread under Julia's question) | 32: 4 exclusions × 3 = 12; no comment on each of ZOM-162/163/201/250 × 3 = 12; Brian commenter 3; the Editor only set is exactly ZOM-173/200/277/315 (5) | Leonard's reply under Julia's Sep 29 question |
| shared | 13: DM total 24 (5); DM per-status counts (5); Editor only keys in the DM 3 | either thread |
| Total | 135 | lever share 71 / 135 = **53%** |

p1 = 2/6 (baseline). Every run that misses the ask's thread misses L7 too (same DM, same thread tool), so p7 = p1 + (1 − p1)·q, where q is the rate at which a run that reads the ask's thread skips the thread under the older message. Projected average = 1 − (26·p1 + 32·p7 + 13·p7) / 135:
- q = 0.3: 76%
- q = 0.5: **71%**
- q = 0.7: 67%

pass@1 = (1 − p1)(1 − q): about 2 of 6 at q = 0.5. The per-rollout scores (100 / 67 / 47%) give SD ≈ 0.2 and two failure patterns.


There is no baseline, so there are no gate numbers. The projection below uses the weight plan in §11, which is facts and weights only and is to be confirmed at `/create-rubric-writing`.

| Block | Rows · weight | Depends on |
|---|---|---|
| status per kept ticket | 29 × 1 = 29 | — |
| other non-lever rows | 51: replaced-by 3; ZOM-199/254 comments 6; folder 3; Robert, Leonard and Arthur shares 9; two tabs 3; rules tab 5 × 3 = 15; DM place 3; Editor only / Not shipped / Replaced counts 9 | — |
| L1 (thread reply) | 40: 6 exclusions × 3 = 18; total and Live counts 2 × 5 = 10; 12 keys in the reply × 1 = 12 | Leonard's thread reply |
| L2 (checklist) | 39: 12 comments × 3 = 36; Brian as editor 3 | the card's checklist |
| Total | 159 | mechanism weight share 79 / 159 = **50%** |

Projected average = (80 + 40·p1 + 39·p2) / 159, less about 2 points of natural slips. p1 is the rate of opening the thread reply and p2 the rate of opening the checklist.

| p1 / p2 | Projected average | Basis |
|---|---|---|
| 0.30 / 0.45 | ≈ 67% | Hardness_Mastery A14: 67/124 Slack-using runs made zero thread-reply calls. Run-1 made none (it printed ts/user/text only, event 10). The checklist shows only as `badges.checkItems: 2` in the search result (event 13) |
| 0.40 / 0.40 | ≈ 68% | middle case |
| 0.50 / 0.50 | ≈ 73% | upper case, still under 75% |

Other projected gates:
- **SD:** the run outcomes are about 98% (both levers found), about 73–74% (one found) and about 50% (neither), so the SD is ≈ 0.15–0.20.
- **pass@1:** only runs that open both carriers pass (p1·p2 ≈ 0.14–0.25).
- **Failure patterns:** the patterns differ by carrier, so there are ≥ 2 and none is above 50%.

**Round 3 projection.** Runs 2 and 3 both opened L1 and L2 (p ≈ 0.8 now, not 0.5), and run-3 opened L3 and answered L4. Two levers on surfaces no run has touched are added:
- **L5** (A3, PR review blind spot): rule 1 "a title match Blake marked 'not tiers' in his review on its PR stays off"; Blake's review on match3d#265 has an empty body, and its inline comment says "not tiers". Rows: ZOM-312 off (5), no comment on ZOM-312 (5), Editor only count 8 (5), the keys in the reply (5). p5 ≈ 0.4–0.5 (0 of 3 runs used a review tool).
- **L6** (A3, card attachment blind spot): Leonard's "notes for monday" doc, linked from the card (badges.attachments 1). Rows: ZOM-258 off (5), Arthur as viewer (3), "ZOM-254 replaced by ZOM-282" in the reply (3), Live count 16 (5). p6 ≈ 0.5 (both readable runs dropped attachments after the error).
- The total (5) needs L1, L3, L5 and L6 together, about 0.8 × 0.8 × 0.45 × 0.5 ≈ 0.14.

With the weight plan (status rows 1; exclusions 3, or 5 for the L5/L6 rows; comments and shares 3; counts and keys 5), the replay model gives about 72–77%, depending on p1/p2 (0.7–0.8). **Below 75% is likely but not certain.** The rubric must keep the L5/L6 rows at 5, or the average rises.

`/hardness` (one run): a run that misses L5 keeps ZOM-312, writes an unrequested comment on it and sends Leonard wrong Editor only and total counts and keys. A run that misses L6 keeps ZOM-258, sends a wrong total and Live count, gives Arthur comment access and leaves out the replacement. Each is a consequential failure (band 3), and a run must find both to reach band 2: P(band 2) ≈ 0.45 × 0.5 × 0.8 ≈ 0.18.

**Round 2 projection.** Two blocks are added:
- **L3:** the ZOM-281 row (3) and its status (1).
- **L4:** the starting-tier timing in the DM (5) and on the rules tab (3; it was a non-lever row before).

The total and Live counts (10) now need both L1 and L3. The new totals are: non-lever 77, L1 30 + shared counts 10, L2 39, L3 4, L4 8 = 168. The lever share is 91/168 = **54%**.

Rates:
- p1 = p2 = 0.5 (run-1 found neither, run-2 found both);
- p3 ≈ 0.5 (run-1 scanned 447 tickets, run-2 about 107);
- p4 ≈ 0.2 (0 of 2 runs wrote "games").

E ≈ (77 + 30·0.5 + 10·0.25 + 39·0.5 + 4·0.5 + 8·0.2) / 168 ≈ 117.6 / 168 ≈ 70%, less about 2 points of slips: **≈ 68%**.

**Clean average:** no CONFOUNDED criterion exists yet (there is no rubric).

## 3 Predicted /hardness band

**Round 7:** the round-6 hardness run scored 3 (it missed ZOM-281 after stopping the subagent that found it). On the round-7 SQL a run that skips #271's inline comments keeps ZOM-295 (23 expected, 24 given); a run that keeps the UTC day misses three done dates. Predicted band 3, or 4 when both are missed. A fresh unhinted Opus run on SQL b64bc2f2c6dc is needed.


**Round 6:** the /hardness run on the round-5 SQL scored 4 (NON-FAIL, PROCEED): it missed both DM thread replies (F1). Round 6 adds a third thread; a run that misses threads also misses Robert's columns, so the band stays 4 or rises toward 5. A fresh unhinted Opus run on SQL f6afeda7b086 is needed.


**Round 5.** A run that misses both carriers (Slack threads and Blake's reply) keeps 10 extra rows, marks the attack-power editor tickets Live, misses ZOM-199's comment, writes Brian as editor and sends Leonard wrong counts and keys: material failures across the result → band 4. A run that misses one carrier → band 3 (one consequential failure family). A run like run-5 that opens both → band 2. Not band 5: the Rules tab, shares and the replaced-by line stay right in every observed run.


**Round 4.** A run that misses L7 keeps ZOM-162/163/201/250, posts 4 comments Leonard said not to post, gives Brian edit access and sends Leonard 28 / 8 Editor only with 4 extra keys: consequential wrong writes → band 3. A run like run-3/run-4 misses both → band 3–4. A run that reads both threads is band 2. P(band ≥ 3) ≈ p7 ≈ 0.67 at q = 0.5.


**Run-1 on the new universe.** The facts from run-1's write payloads are:
- it made no thread-reply call and no checklist call;
- its register (event 2150) has 35 rows, including ZOM-30, ZOM-49, ZOM-50, ZOM-161, ZOM-262 and ZOM-275;
- it wrote 2 comments (events 2165, 2167);
- it shared with Brian as commenter (event 2163);
- its DM reply (event 2169) gives counts only.

| Requirement | Result on the hardened universe | Evidence |
|---|---|---|
| R1 membership (29) | MATERIAL_FAIL: 6 extra rows | run-1 · event 2150 |
| R6 reply counts and keys | MATERIAL_FAIL: 35/22 and no keys | run-1 · event 2169 |
| R7 ticket comments (14) | MATERIAL_FAIL: 2 of 14 | run-1 · event 2165, event 2167 |
| R8 shares | MINOR_GAP: Brian commenter, not editor | run-1 · event 2163 |
| R2–R5, R9 | MET | run-1 · event 2150, event 2152, event 2154 |

Predicted band: **4** for a run like run-1. There are two independent root causes (the unopened thread reply and the unopened checklist), and each needs correction across the result: the rows and counts for one, 12 writes for the other. It is not 5, because the core register, folder, rules tab and statuses are correct and usable. It is not 3, because there are two consequential failures, not one bounded one.

A run that opens one carrier lands at **3**. A run that opens both lands at 1–2.

**Round 2.** A run like run-2 (both carriers found) still fails two things:
- **L4:** its DM tells Leonard the wrong rule ("after level 10"). This is a consequential failure to the requester, on the rules tab too. It is not one cell any more.
- **L3:** by its own scan scope (report §6), it misses ZOM-281, so the row and the total and Live counts are wrong.

That predicts band **3–4** for a run-2-like run, and **4** for a run-1-like run.

## 4 Designed-difficulty register (verdicts)

**Round 7 verdicts (round-6 SQL runs):**

| Trap | Verdict | Evidence |
|---|---|---|
| T32 (Robert's thread reply) | RESISTED 6/6 | run-1 · event 80, run-2 · event 100 |
| T22 / T28 / T29 (Leonard's two thread replies) | LANDED 1/6 | run-1 · event 2326 (34 rows), run-1 · event 2335 (Brian writer) |
| T26 (ZOM-312 'not tiers' on #265) | RESISTED 6/6 | 24 rows without ZOM-312 at run-3 · event 3844 |
| T1 to T21, T24, T25, T27, T30, T31 | RESISTED 6/6 | statuses all right at run-4 · event 1946 and run-5 · event 2076 |
| T33 (round 7: 'not tiers' on #271) | NEW, replay: missed by run-1, run-4, run-6 of this batch | run-4 · event 1866 (reviews only), run-6 · event 2665 (reviews only) |
| T34 (round 7: pacific done day) | NEW, untested: all six wrote the UTC day | run-3 · event 3844, run-6 · event 2751 |


**Round 6 verdicts (round-5 SQL runs):**

| Trap | Verdict | Evidence |
|---|---|---|
| T22 / T28 / T29 (Leonard's two thread replies) | LANDED 3/6 | run-1 · event 1540 (34 rows), run-2 · event 13 (channel_not_found), run-4 · event 2188 (Brian writer) |
| T26 (ZOM-312 'not tiers' in #265 review comments) | LANDED 1/6 (only the run that skipped them) | run-2 · event 2280 |
| T30 (Blake's reply in its own thread) | RESISTED 6/6 | run-1 · event 54, run-5 · event 64 |
| T31 (builds in comments) | RESISTED 6/6 (builds also in the first mail) | run-3 · event 2152, run-6 · event 2119 |
| T1–T21, T24, T25, T27 | RESISTED 6/6 | statuses all right in run-3 · event 2122 and run-1 · event 1540 |
| T32 (round 6: Robert's thread reply) | NEW, untested: today every register has the five agenda columns only (run-3 · event 2122, run-1 · event 1540) | slack abe096ff0b5d7216efbc889e91d6d13a |


**Round 5 (6 baseline rollouts on dd7536cdea3f).** Counts LANDED · CONFOUNDED · LEAKED · BYPASSED · NOT-REACHED out of 6:

| Node | Records | Verdict | Counts | Evidence |
|---|---|---|---|---|
| T22 thread reply under the ask (L1) | D05HB64NMQU/1759262838.442871 | LANDED 5 / LEAKED 1 | 5·0·1·0·0 | no thread call in run-1 · event 6 … run-6 · event 6; run-5 · event 19 read it |
| T28/T29 reply under Julia's Sep 29 question (L7) | D05HB64NMQU/1759267002.665190 | LANDED 5 / LEAKED 1 | 5·0·1·0·0 | Brian shared as editor run-1 · event 3486 … run-6 · event 1959; run-5 · event 21 read it, Brian commenter run-5 · event 2129 |
| T26 'not tiers' review comment (L5) | match3d#265#rc_7 | LANDED 1 / LEAKED 5 | 1·0·5·0·0 | run-1 · event 3337 read reviews only (empty body) and kept ZOM-312 (run-1 · event 3479); run-2 · event 2167 read the comment |
| T27 notes doc (L6) | f_f494073fc667097c3c2c6b | LEAKED | 0·0·6·0·0 | run-1 · event 27 … run-6 · event 27; Arthur reader and ZOM-258 off in all registers |
| T23 checklist (L2) | 68dc033bf7d24e86b8a9cc67 | LEAKED | 0·0·6·0·0 | run-1 · event 20 get_card checklists all; Editor only / Not shipped comments in all runs (run-1 · event 3493) |
| T6 reply in the store-builds thread (> 90) | julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> | LEAKED | 0·0·6·0·0 | run-1 · event 44 get_thread returned both messages; ZOM-199 comment in all runs |
| T30 (new) Blake's reply in its own thread | julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> | NOT-REACHED (new) | 0·0·0·0·6 | absent from the baseline universe; the habit: every run opened only the first 'store builds' thread from an id-only search (run-2 · event 35 → 41) |
| T31 (new) build numbers in the Editor only / Not shipped comments | D05HB64NMQU/1759262838.442871 | NOT-REACHED (new) | 0·0·0·0·6 | absent from the baseline universe; rides the L1 thread (run-5 · event 19 is the only thread read) |


**Round 4 (6 baseline rollouts on 2ee488e28ab5).** Counts LANDED · CONFOUNDED · LEAKED · BYPASSED · NOT-REACHED out of 6:

| Node | Records | Verdict | Counts | Evidence |
|---|---|---|---|---|
| T22 thread reply under the ask (L1) | D05HB64NMQU/1759262838.442871 | LANDED 2 / LEAKED 4 | 2·0·4·0·0 | run-3 · event 13 (channel_not_found, not retried); run-4 · event 6 (no thread call); run-1 · event 17 found it |
| T23 card checklist (L2) | 68dc033bf7d24e86b8a9cc67 | LEAKED | 0·0·6·0·0 | run-1 · event 22 get_card checklists all; 13 comments in all runs |
| T26 'not tiers' review (L5) | match3d#265#rc_7 | LEAKED | 0·0·6·0·0 | run-1 · event 2160 get_pull_request_reviews; ZOM-312 off in all registers |
| T27 notes doc (L6) | f_f494073fc667097c3c2c6b | LEAKED | 0·0·6·0·0 | run-1 · event 26 trello_get_attachments; Arthur reader in all runs |
| T28 (new) level editor drop (L7) | D05HB64NMQU/1759267002.665190 | NOT-REACHED (new) | 0·0·0·0·6 | absent from the baseline universe; the habit: run-1 · event 6 to 17 open only the newest message's thread |
| T29 (new) Brian comment only (L7) | D05HB64NMQU/1759267002.665190 vs checklist 68dc033bf7d24e86b8a9cc67 | NOT-REACHED (new) | 0·0·0·0·6 | absent from the baseline universe; all six runs gave Brian edit from the checklist (run-1 · event 2257–2263) |


Counts are LANDED · CONFOUNDED · LEAKED · BYPASSED · NOT-REACHED, out of 1 completed run.

| Node | Mechanism / records | Verdict | Counts | Evidence (rollout · step) |
|---|---|---|---|---|
| T1 attack-power amendment | card comment 68dbfa4362a051efb5e0ae45 | LEAKED | 0·0·1·0·0 | run-1 · event 16 read the comment; event 70 regex includes "attack power" |
| T2 window up to Aug 31 | rule 1; ZOM-517 out | LEAKED | 0·0·1·0·0 | run-1 · event 70 filters createdAt ≤ 2025-08-31 |
| T3 ZOM-271 "ATK POWER" | card comment "written out" | LEAKED | 0·0·1·0·0 | run-1 · event 70 whole-word regex; ZOM-271 absent at event 2150 |
| T4 duplicates | ZOM-203, ZOM-276 Duplicate | LEAKED | 0·0·1·0·0 | run-1 · event 2150 omits both |
| T5 ZOM-45 / ZOM-277 scope alias | notes cmt_bed381141007e04f1aac, cmt_b0aa45d307c981ce4487 | LEAKED | 0·0·1·0·0 | run-1 · event 2150: ZOM-45 Live, ZOM-277 Editor only |
| T6 deck ">= 90" | Blake's reply in the thread | LEAKED | 0·0·1·0·0 | run-1 · event 23 gmail_get_thread; event 2152 "> 90" |
| T7 Brian's recap | C090N54TG79/1759185077.402611 | BYPASSED | 0·0·0·1·0 | run-1 never read #zombie-design (no slack channel or search call after event 6) |
| T8 ZOM-282 → #401 → sheet | note, PR comment, sheet | LEAKED | 0·0·1·0·0 | run-1 · event 48 sheet read; event 2152 enrage per monster, hp 0 |
| T9 Next pass tab | sheet tab | LEAKED | 0·0·1·0·0 | run-1 · event 48 read all tabs; event 2152 uses Live |
| T10 ZOM-42 full spec | ZOM-42 description | LEAKED | 0·0·1·0·0 | run-1 · event 359 get_issue ZOM-42; event 2152 both demotion rules |
| T11 deck +25% HP | deck vs sheet | LEAKED | 0·0·1·0·0 | run-1 · event 41 deck; event 48 sheet; event 2152 no HP |
| T12 Domino Delights card | 683dbef4e319167a802bd888 | LEAKED | 0·0·1·0·0 | run-1 · event 13 search returned both cards; it used card 80 |
| T13 invite as share list | evt_91674a9c23d012a9ac34da | LEAKED | 0·0·1·0·0 | run-1 · event 20 attendees; events 2157–2163 shares |
| T14 comment set / no new tickets | rule 6 | LEAKED | 0·0·1·0·0 | run-1 · event 2165, event 2167 only |
| T15 shared PRs #243/#265 | notes + PR files | LEAKED | 0·0·1·0·0 | run-1 · event 2105–2128 PR files; event 2150 ZOM-173/312 Editor only |
| T16 Vincent's channel request | C090N54TG79/1759248760.118527 | BYPASSED | 0·0·0·1·0 | run-1 never read #zombie-design; reply in the DM at event 2169 |
| T17 Domino Delights sheet | f_34f0950581934de1278969 | BYPASSED | 0·0·0·1·0 | run-1 · event 31/32 searches "difficulty"/"enrage" never surfaced it |
| T18 untagged Blake tickets | no "tiers:" | LEAKED | 0·0·1·0·0 | run-1 · event 105 subagent filter on "tiers:"; event 2150 excludes them |
| T19 old iOS build | C08R27X0EAH/1758081917.318539 | BYPASSED | 0·0·0·1·0 | run-1 never read #zombie-bugs; mail at event 23 |
| T20 lives tickets | ZOM-305 tagged, ZOM-352 not | LEAKED | 0·0·1·0·0 | run-1 · event 2150: ZOM-305 in, ZOM-352 out |
| T21 #401 as a replacement | rule 4 record-based | LEAKED | 0·0·1·0·0 | run-1 · event 2150 ZOM-282 Live; event 2167 |
| T22 Leonard's thread reply (round 1) | D05HB64NMQU/1759262838.442871 | LEAKED in run-2; NOT-REACHED in run-1 | 0·0·1·0·1 | run-2 · event 13, 20, 29 (report) opened the thread; run-1 · event 10 shows the habit that misses it |
| T23 card checklist (round 1) | 68dc033bf7d24e86b8a9cc67 | LEAKED in run-2; NOT-REACHED in run-1 | 0·0·1·0·1 | run-2 · event 18, 22 (report) fetched the card with checklists; run-1 · event 13/16 shows the read path that misses it |
| T24 (round 2) ZOM-281 tag outside the scan groups | cmt_df69e4a92767cbff0000 | NOT-REACHED (new) | 0·0·0·0·0 | run-1 · event 105 batch scan covered every completed ticket (would reach ZOM-281); run-2 (report §6) scanned only keyword and Blake-assigned tickets (about 107), so a run-2-like run misses it |
| T26 (round 3) Blake's 'not tiers' inline comment on match3d#265 (ZOM-312) | harmonygames-Games/match3d#265#rev_8, harmonygames-Games/match3d#265#rc_7 | NOT-REACHED (new) | 0·0·0·0·0 | run-3 · event 320–434 and run-2: PR lists only, 0 review or review-comment reads; the comment sits under an empty-body COMMENTED review |
| T27 (round 3) Leonard's 'notes for monday' doc attached to the card | 68dbfcc8aa008dbd8cccea3e → f_f494073fc667097c3c2c6b | NOT-REACHED (new) | 0·0·0·0·0 | run-3 · event 18 → 22 and run-2 · event 18 → 22: attachments dropped after the parameter error |
| T25 (round 2) starting-tier timing (games, not levels) | TierManager.cs totalGames == 10; WinHistory.GetTotalGames | was the emergent F1 (MINOR) in both runs | 0·0·0·0·0 | run-1 · event 2152 and run-2 · event 658 (report) both wrote "10 levels" after reading the code (run-1 · event 435; run-2 · event 553 (report)) |

Emergent, not designed: the starting-tier window "first 10 levels" vs the code's 10 games (run-1 · event 2152) was a MINOR_GAP in the platform report. It stays off the rubric (the prompt review and injection advisories).

## 5 Per-rollout ledger (run-1)

**Round 5 ledger (run-1, the largest run; the others differ only where §1 says).**

| Step | Tool | Input | What came back | Decision | Rubric(s) |
|---|---|---|---|---|---|
| run-1 · event 6 | slack_read_channel | DM D05HB64NMQU | the ask (reply_count 1) and Julia's Sep 29 question (reply_count 1) | no thread call | R5–R7, R39, R52–R55 |
| run-1 · event 20 | trello_get_card | card, checklists all, actions all | rules 1–7, checklist, attack-power comment | applied all | R5, R45–R51 |
| run-1 · event 27 | gdocs_get_document_text | notes doc | ZOM-258 off, Arthur view, which replaced which | applied | R41, R65 |
| run-1 · event 36 → 44 | gmail_search_messages → gmail_get_thread | "store builds" (ids only) → the first thread | the mail and Blake's reply | > 90, editor/debug stripped | R13–R16, R43 |
| run-1 · event 3337 | github_get_pull_request_reviews | #265 | empty-body COMMENTED reviews | no review-comment call; kept ZOM-312 | R5, R7, R52 |
| run-1 · event 3479 | gsheets_values_update | Tickets tab | 35 rows | — | R5–R7 |
| run-1 · event 3486 | gdrive_share_file | brian.foster | writer | checklist's rule 7 change | R39 |
| run-1 · event 3493 … | linear_create_comment | 14 tickets | — | incl. ZOM-162/163/201/250/312 | R52 |
| run-1 · event 3522 | slack_send_message | DM | 35 / 22 / 9 / 3 / 1 + keys | — | R53–R55 |


| Step | Tool | Input (query / IDs) | What came back | Agent's decision | Requirement |
|---|---|---|---|---|---|
| event 6–10 | slack_read_channel + Bash print | DM D05HB64NMQU | 83 KB of history; the printout kept ts/time/user/text only | read the ask; no thread call | R1, R6 |
| event 13 | trello_search | "difficulty baseline" | card 80 (desc + badges) and the DD card | used card 80 | R1–R9 |
| event 16 | trello_get_comments | card 80 | the attack-power comment | applied it | R1 |
| event 18–23 | gmail search + get_thread | "store builds" | both messages | > 90; editor/debug stripped | R2, R4 |
| event 20 | gcal_search_events | "tuning" | invite, 5 attendees | share list | R8 |
| event 39–48 | gdocs, gslides, gdrive, gsheets | agenda, deck, folder, sheet tabs | rules, layout, enrage | two tabs; Live values | R4, R9 |
| event 56–70 | linear_list_issues ×3 + Bash | ZOM, 500 issues | titles/states | title-word cohort (31 + 4 tagged) | R1 |
| event 105–1224 | 11 subagents, 415 linear_list_comments | candidate batches | only "tiers:" / "replac" / "supersede" matches reported | tagged tickets, ZOM-282's replacing note | R1, R3 |
| event 344 | subagent "Ticket shipping research" | member list + mail rules | statuses | Live / Editor only / Not shipped | R2 |
| event 359–607 | get_issue ZOM-42/303/293/199; code reads | TierManager, WinRateRule, GameLoader | rules in code | rules tab | R4 |
| event 2033–2128 | get_issue ×30; PR files #243/#244/#265/#271 | member descriptions; PR file tables | statuses confirmed | — | R2 |
| event 2146–2169 | writes | sheet, tabs, move, 4 shares, 2 comments, DM | — | — | R1–R9 |

Where it stopped: it never called `slack_read_thread` or `slack_conversations_replies`, `trello_get_card`, `trello_get_checklist` or `trello_get_card_actions`, `github_get_pull_request_comments` or reviews, or any Slack channel other than the DM.

## 6 Friction, tool-defect and horizon checks

**Round 5.** Friction: none configured. Tool defects: the first two trello_get_card calls in every run failed on the attachments flag ('attachments must be true, false, or "cover"', run-1 · event 16, 18) and the runs retried (run-1 · event 20); no outcome changed. Horizon: counted calls 1,204 / 762 / 864 / 719 / 832 / 738 (difficulty_stats), golden run 832: PASS. The round-5 change adds about 2 Gmail calls (search for the reply, open it).


- **Friction:** none is configured (03_Error_Async_Config.txt). There are no async or forced errors.
- **Unconfigured tool defects:** event 6 returned 83 KB, saved to a file. The agent read it with python (event 10), so it is not a defect. No errored calls changed an outcome.
- **Horizon:** 741 calls (619 comment reads). After hardening the budget is 161 unconditional calls (01_Hardness_Manifest.json), which is above the ≥ 120 author target.

## 7 Verifier sanity

**Round 5.** The platform verifier matches the trajectories on every row: its fails are exactly the replay's (run-1, run-4, run-6 fail R5, R6, R7, R39, R52–R55; run-2, run-3 add R58–R64). Six verifier titles differ from 09_Rubrics.json only by link markup on emails and '&gt;' escaping; no judge text concedes a fact and still fails it. No all-fail rubric. No collapsed run (lowest 66.9%, median 76.2%).


Not applicable: there is no verifier or rubric yet (`10` is absent).

## 8 Why Opus passed

**Round 7:** Opus reads every carrier the card names and applies each rule it reads. The round-6 runs made 716 to 1,356 calls and opened all three thread replies in five of six runs. What they skip is a second read inside a record they have already opened: a PR's inline comments after its reviews list (run-4 · event 1866), and they keep Linear's UTC stamp as the date (run-2 · event 2041).


**Round 6:** runs that open the DM threads make no other mistake. Opus resolves every judgement trap (status splits, replacements, decoys, title aliases) from records it reads anyway, so the only failures are records it never opens. One carrier gives one failure pattern.


**Round 5.** Every pointed source was opened by all six runs: the card with checklists and actions (run-1 · event 20), the attached notes doc (run-1 · event 27), the store-builds thread (run-1 · event 44), PR reviews (run-1 · event 3337), all ZOM comments, the code (run-1 · event 3409). The only habit that varied is opening Slack thread replies (run-5 · event 19 vs none elsewhere), and it is all-or-nothing per run, so both thread levers fail together. Class: genuine capability on every reachable rule; the single landed carrier is A14 (Slack replies). The fix is a second, independent carrier whose miss changes graded values (not only counts).


**Round 4.** Four of six runs passed every graded point. Opus requests every surface a tool exposes (checklists all, actions all, attachments, PR reviews; run-1 · event 22, 26, 2160) and follows every pointer the card or the ask gives. Its only miss is mechanical: the DM read overflows to a file, the run parses it with a script, studies only the newest message, and opens that message's thread after a channel_not_found retry (run-1 · event 13 → 17). Class: retrieval breadth is saturated; the remaining lever is a second thread on an older message.


| Point scored | Mechanism | Class |
|---|---|---|
| Membership, 35 exact | every membership rule sat in the card desc and comment (read at event 13/16) and in notes found by keyword subagents (event 105) | universe leak: the rules sat where Opus reads first |
| All statuses | the notes state the status plainly; the mail lists what is stripped (event 23) | genuine capability plus over-findable notes |
| > 90, enrage, demotion | the thread is opened with get_thread (event 23); the sheet tabs are read in full (event 48); ZOM-42 in full (event 359) | genuine capability |
| Shares, comments, DM | rule 7 + invite (event 20); rule 6 is closed (event 2165/2167) | genuine capability |
| BYPASSED Slack decoys | the run never opened #zombie-design / #zombie-bugs, so Brian's recap and Vincent's request were never met | universe leak: the decoys were off the true path |

## 9 Purge list

**Round 5.** No node purged. T6 (reply in the same thread) was LEAKED 6/6 because get_thread returns the whole conversation; it is rebuilt as T30 (the reply in its own conversation), not deleted.


- **T7, T16, T19 (Slack decoys):** BYPASSED in run-1. They are kept for realism and coherence: they are base-consistent and cost nothing. They are no longer counted as difficulty, and no weight is planned on them.
- **T17 Domino Delights sheet:** BYPASSED; kept as is.
- **The timing lever proposed by the platform report:** rejected. No member's PR merged after the Sep 26 cut or closed unmerged (match3d PRs #243–#319 all merged 2025-06-25..07-19, github data.json), so seeding one would be a false code claim.

## 10 Candidates and selection (rebuild)

**Round 7 candidates:**

| # | Candidate | Verdict | Reason |
|---|---|---|---|
| 30 | 'not tiers' inline comment on PR #271 (ZOM-295) | ACCEPTED | fetched by 5 of 15 runs; card rule 1 already governs it; the comment calls the PR a bug fix (enrage was meant to clear on refill health and push back), true to the ticket and the diff |
| 31 | Robert asks for the done day in pacific time | ACCEPTED | every run wrote the UTC day; three tickets differ (ZOM-200, 274, 282); unique answer |
| 32 | Another 'not tiers' on #243 (ZOM-173) | REJECTED | #243's inline comments were fetched by 10 of 15 runs, twice the #271 rate |
| 33 | A lever in the #zombie-prs feed or GitHub issue comments | REJECTED | no run opened the feed; a lever no run reaches is an all-fail row |


**Round 6 candidates:**

| # | Candidate | Verdict | Reason |
|---|---|---|---|
| 26 | Move the ZOM-277 / ZOM-315 editor evidence into Blake's PR review comments | REJECTED | neither ticket has a PR (GitHub data.json search: only ZOM-173, 295, 303 and 312 do) |
| 27 | Blake 'not tiers' review comments on #271 (ZOM-295) or #244 (ZOM-303) | REJECTED | both are core gameplay tier work; their descriptions match the code, so a 'not tiers' or 'text is wrong' mark is not credible |
| 28 | 'not tiers' on #243 (ZOM-173) | REJECTED | changes count rows only, which the thread misses already fail; Monte Carlo P(all gates) about 0.02 |
| 29 | Third thread reply in a different conversation: Robert's three Tickets-tab columns in the group chat, card rule 2 points to it | ACCEPTED | unique positive rows (assignee, done day, priority for 24 tickets); separate conversation; earlier batch showed runs opening one thread and not another (4 of 6) |


**Round 5 candidates.**

| # | Candidate | Evidence | Selected |
|---|---|---|---|
| 18 | Blake's reply in its own Gmail conversation (subject changed), carrying the editor/debug stripping rule and both ZOM-199 corrections; card rule 3 names the reply | gmail_search_messages returns ids only (run-2 · event 35); every run opened only the first thread (run-1 · event 44), 2 of 6 opened any other thread (run-2 · event 54); A14: 41/60 Gmail runs never opened a thread | yes (L8, T30) |
| 19 | Leonard's thread reply asks the Editor only / Not shipped comments to name the two builds | A21 per-surface output rule in an incorporated source; adds 7 positive rows to the thread carrier | yes (L9, T31) |
| 20 | a closed-unmerged PR for a Done member (never merged → Not shipped) | every run lists all match3d PRs with merged state (run-1 · event 3337 area; list_pull_requests state=all); a new PR number breaks the 1..544 sequence | no |
| 21 | a title-match ticket on the Aug 31 PT/UTC edge | no base ticket in 2025-09-01 00:00–07:00Z; ZOM-509 (Aug 28) → ZOM-510 (Sep 1): a new number would break Linear's sequence | no |
| 22 | Blake marks ZOM-307 (Easy Quantity slider, #243) as tier work in a review comment | #243 removed the field 'throughout the app': Editor only vs Live is arguable (two end states) | no |
| 23 | Blake flags ZOM-300 ('Randomized') or ZOM-282 ('+50%') as wrong | GameLoader.cs calls RemoveRandomObjects (ZOM-300 is right); enrage values live in prefabs, not code | no |
| 24 | Leonard adds cancelled editor tickets ZOM-309 / ZOM-197 to the list | contradicts his own cut ('they don't change how hard a level plays') | no |
| 25 | another 'not tiers' review comment | only moves counts, which thread-missers already fail: no pattern split | no |

**Lazy solver (round 5).** DM read, card, notes doc, 'store builds' search → first thread, code, sheet, invite: 34 rows, the attack-power editor tickets judged from titles, no ZOM-199 comment, comments without build numbers, Brian editor. Fails L1, L7, L8 and L9.

**A5b check.** Incorporated: rule 3 and rule 6 name 'his reply to it'; the L1 thread is part of the ask. Survives retrieval: the reply's rule must still be applied per ticket (ZOM-45 and ZOM-303 stay Live; ZOM-277, ZOM-315 are editor stats panel work). Tool surface: gmail_search_messages 'from:arthur.blake@harmonygames.co' or 'ZOM-199' returns the reply; gmail_get_thread on its thread id returns it. Graded weight: about 45% lever-dependent after the rubric update.


**Round 4 candidates.**

| # | Candidate | Evidence | Selected |
|---|---|---|---|
| 13 | Leonard's reply in the thread under Julia's Sep 29 question: ZOM-162, 163, 201, 250 off ('just those four'), no comments, Brian comment only | every run studies the newest DM message and its thread only (run-1 · event 6–17, run-6 · event 6–24) | yes (L7) |
| 14 | Slack file on the ask | Ask_Carriers: files_json "key present but null", rendering unverified | no: /prompt discoverability risk |
| 15 | Gmail attachment / second mail thread | runs read only the first thread from the "store builds" search (run-1 · event 45) but a pointed mail is opened | no: found once pointed |
| 16 | revert or side-branch merge of a difficulty PR | match3d history copy: reverts are UI/ads/sound only | no |
| 17 | Linear comment pages / issue_not_found | the 404s are ZOM-416/460/522/529, non-existent numbers | no |


| # | Anchor storyline (cited) | Coupling | Discovery-order proof | Gradable fact | Selected |
|---|---|---|---|---|---|
| 1 | Leonard follows up under his own ask (D05HB64NMQU/1759261706.530914 → reply D05HB64NMQU/1759262838.442871, 2025-09-30T20:07:18Z) | drops 6 rows (ZOM-30, 49, 50, 161, 262, 275) → totals 29 / 16 Live → the reply needs 12 keys | the parent shows reply_count 1; run-1 · event 10 printed text only | 29 rows; 29 / 16 / 9 / 3 / 1; keys 202, 280, 293 + 9 Editor only | yes (A14) |
| 2 | Leonard's "Before Monday" checklist on card 80 (68dc033bf7d24e86b8a9cc67, addChecklistToCard 2025-09-30T16:20:11Z) | rule 6 change → 12 more comments; rule 7 change → Brian edits | the search result shows only badges.checkItems 2 (run-1 · event 13); the items need trello_get_checklist / get_card | 14 comments; Brian writer | yes (A3) |
| 3 | timing: a Done member whose PR merged after the cut | — | — | — | rejected: no such record (§9) |
| 4 | an owner column (Linear assignee) per row | 29 cells | — | — | rejected: 5 members carry a redacted assignee (EMPLOYEE_0032_EMAIL) |
| 5 | Blake's PR comment carrying a status | — | — | — | rejected: any status claim on a PR is a code claim git history can contradict |

| 6 (round 2) | Blake's tiers: note on ZOM-281 "Win streak not lost when replaying without main menu" (assigned EMPLOYEE_0032, no card word) | +1 row, total and Live counts | run-2 scanned only keyword and Blake-assigned tickets (report §6) | 30 rows, 17 Live | yes (A7) |
| 7 (round 2) | Leonard asks when a new player gets the starting tier; rule 5: go by the build | the DM and rules tab must say "after the first 10 games" | run-1 · event 2152 and run-2 · event 658 (report) wrote "10 levels" | the timing fact | yes (survives retrieval) |
| 9 (round 3) | Blake's 'not tiers' inline comment on his review of match3d#265 (ZOM-312 is linked by its own closing note "merged with match3d#265") | −1 row, −1 comment, Editor only 8, keys 11 | 0 of 3 runs read a PR review (run-3 · event 320–434) | 28 rows | yes (A3) |
| 10 (round 3) | Leonard's "notes for monday" doc attached to card 80 (link; base has 6 cards with unactioned attachments) | −ZOM-258, Arthur viewer, reply names the replacement | run-2 and run-3 dropped attachments after the error (event 18 → 22) | 28 rows, 16 Live | yes (A3) |
| 11 (round 3) | ZOM-295's "reset ALL enrage" vs PR #271 | — | — | — | rejected: Monster.MoveBack calls SetEnrage(0) on every pushed-back monster at the cut, so the ticket text is true |
| 12 (round 3) | a member PR merged after the Sep 26 cut | — | — | — | rejected: the only ZOM PR merged Sep 27–30 is #471 (ZOM-498/536, home-screen UI) |
| 8 (round 2) | a #if UNITY_EDITOR-guarded member change | — | — | — | rejected: the guards are at HEAD and can't be tied to the clock without git history |

**Lazy solver.** One DM read, the card search, its comments, the thread, the sheet and the invite give the register at 35 rows with 2 comments and Brian as commenter. That fails L1 (6 rows, the counts and the keys) and L2 (12 comments, Brian's role).

**A5b check (each node).**
- **Incorporated:** L1 is part of Leonard's ask, which the prompt names ("go through his ask"). L2 is on the card the ask names, and each item says "rule 6 change" / "rule 7 change".
- **Survives complete retrieval:** opening the reply or checklist still needs the rows dropped, the counts recomputed, and 12 comments written.
- **Tool-surface proof:** `slack_read_thread` on D05HB64NMQU/1759261706.530914 and `trello_get_checklist` on 68dc033bf7d24e86b8a9cc67 (both cataloged) return the text.
- **Graded weight:** 50% in the §2 plan.

## 11 Routing

**Round 7 routing:** SQL b64bc2f2c6dc (harden_r7.py): +4 rows: harmonygames-Games/match3d#271#rev_2 (APPROVED, empty body), harmonygames-Games/match3d#271#rc_1 ('not tiers' on MonsterSpawner.cs), two #zombie-prs mirrors (approval and comment) under #271's opened post with reply_count 4 to 6; Robert's thread reply asks for the done day in pacific time; header counts. New answer: 23 tickets (Live 15, Editor only 4, Replaced 1, Not shipped 3); done days ZOM-200 2025-06-12, ZOM-274 and ZOM-282 2025-06-20. Next: /injection, /prompt, /hardness on a fresh run, then OE and rubric, then six baselines.


**Round 6 routing:** SQL f6afeda7b086 (harden_r6.py): +2 slack rows in group chat CAFC495E4006 (Leonard's question cec246a6e43158f200fe144f0dd7039c, Robert's thread reply abe096ff0b5d7216efbc889e91d6d13a); card rule 2 (desc and updateCard action) names the three things Robert asked for; header counts. Next: /injection, then /prompt (card text changed), /hardness on a fresh run, then OE and rubric (new rows for the three columns; spot checks on unambiguous values only), then six baselines.


**Round 5 universe changes** (01_Universe_Inject.sql dd7536cdea3f → 7966b1496ad9; 175 → 180 rows; script support/task_work/jl_difficulty/harden_r5.py):

| Statement(s) | Change |
|---|---|
| gmail_messages julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> and its 4 mailbox copies | thread_id → its own conversation (julia: julia.lawson@harmonygames.co/1844695547248825769), subject 'editor stuff and ZOM-199, before Monday', body: the stripping rule + ZOM-199 is wrong on '>= 90' and on '10 levels' (the code: > 90 when the 10th game ends, wins and losses) |
| gmail_threads (5 new) | one row per mailbox for the reply's conversation |
| gmail_messages <CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> (5) and their thread rows | stripping paragraph removed; thread snippets show the first mail |
| trello card 68daca5871dba40417a00383 desc + updateCard action 68dbe36f4b2b4fffb7525fde | rule 3: 'Blake's store builds mail and his reply to it.' |
| slack D05HB64NMQU/1759262838.442871 | adds: 'and when you comment on the editor only and not shipped ones, put the two builds in the comment (ios 0.3.49 and android 0.3.133) so people can see what you checked against' |

Re-passed: sql_lint 0 errors; base_check PASS; fact_check PASS (8 facts); persona_view check-sql PASS; hardness_gate (long) PASS; stage_gate injection PASS. Manifest: K5, K14, T5, T6, T7, C3 updated; T30, T31, C14 added (manifest_r5.py). Dossier: round-5 section, facts for the human (dossier_r5.py).

**Facts changed (for the prompt, OE and rubric):**
- The answer key is unchanged: 24 rows (16 / 4 / 3 / 1), 9 comments, same shares, same DM counts and keys.
- Statuses: the editor/debug rule now comes from Blake's reply (own thread), not the first mail.
- ZOM-199's comment carries both corrections: > 90, and checked when the 10th game ends (wins and losses).
- The 7 Editor only / Not shipped comments each name iOS 0.3.49 and Android 0.3.133.

**Prompt-side defects:** none. The prompt is unchanged; /prompt re-runs because card rule 3 changed.

**Routed observations:** /create-oe-writing (the reply's search and read become their own events; comment payloads add the builds; status evidence cites the reply) and /create-rubric-writing (new rows: build numbers in each of the 7 comments, ZOM-199 comment '10 games'; evidence on the status rows cites the reply).


**Universe changes made** (`01_Universe_Inject.sql` a58a5d1e61b3 → 10c1ee9238d4; 158 → 163 INSERTs, 1 UPDATE unchanged):

| Statement(s) | Change |
|---|---|
| slack_messages (S_ASK) | reply_count 1, reply_users_count 1, latest_reply 1759262838.442871 |
| slack_messages (new) | 33c941fae57ba8d1e23bc1dff9ce3e2c: Leonard's reply in the ask's thread (2025-09-30T20:07:18Z), dropping ZOM-30, 49, 50, 161, 262, 275 and asking for the Not shipped and Editor only keys |
| trello_checklists, trello_check_items ×2, trello_actions addChecklistToCard (new) | checklist "Before Monday" 68dc033bf7d24e86b8a9cc67 with "rule 6 change: the Editor only and Not shipped tickets get a comment too…" and "rule 7 change: Brian gets edit as well…"; action 68dc033b328def4251f2a731 at 2025-09-30T16:20:11Z |
| trello_cards (card 80) | dateLastActivity 2025-09-30T16:20:11Z; badges.checkItems 2 |

Checks after the change:
- sql_lint: 0 errors, 19 warnings
- base_check: PASS
- fact_check: PASS
- check-sql: PASS (the thread reply is visible to Julia: DM member)
- hardness_gate (long): PASS
- stage_gate scenario and injection: PASS

**Round 3 outcome.** /hardness attempt 4 (/home/sumit/Downloads/6adfee3ef9092601a61245bb_1a_hardness (3).md, run trajectory-run-1 (5).json, 836 calls): NON-FAIL, band 3 (Hard), PROCEED. The run found L2–L6 (notes doc, PR #265 review, Arthur reader, replaced-by line) but missed L1, Leonard's DM thread reply (run-4 · event 12 parsed the DM without reply_count): 34 rows, 22 Live, wrong counts and no keys in the DM. /prompt attempt 9 NON-FAIL 3 for one date fix on PR #401 (updated_at before the injected comment); the one-line UPDATE was built and checked, then withdrawn on the author's decision (NON-FAIL 3 COMPLETE clears the gate); SQL stays 2ee488e28ab5, matching every pass.

**Round 3 changes** (52c581f442c1 → 2ee488e28ab5; 164 → 170 INSERTs, 1 → 2 UPDATEs):

| Statement(s) | Change |
|---|---|
| github_reviews (new) | harmonygames-Games/match3d#265#rev_8: EMPLOYEE_0025 (Blake), COMMENTED, empty body, 2025-07-03T17:50:12Z |
| github_review_comments (new) | harmonygames-Games/match3d#265#rc_7 on Assets/Scripts/LevelEditor/UI/LevelSettings.cs (base hunk of #265#rc_3): "not tiers: this is level settings tooling for the designers, players never see it. leave it out when we list tier work" |
| slack_messages (new) + UPDATE | the GitHub-app mirror of that comment under #265's opened post in C093LEZGF6J; parent reply_count 12 → 13 |
| trello_attachments (new) + card badges | 68dbfcc8aa008dbd8cccea3e "notes for monday" (Leonard, 2025-09-30T15:52:40Z) → docs.google.com/document/d/f_f494073fc667097c3c2c6b; badges.attachments 1 |
| drive_files + docs_documents (new) | f_f494073fc667097c3c2c6b "notes for monday" (Leonard's Drive, shared with Julia): leave ZOM-258 off; Arthur view only; say which ticket replaced which |
| trello_cards + updateCard desc | rule 1 adds "It works the other way too: a title match Blake marked 'not tiers' in his review on its PR stays off." |

**Facts that changed** (round 3 supersedes rounds 1–2 where they differ):
- Register: 28 rows (ZOM-312 and ZOM-258 off). Counts 28 — 16 Live, 8 Editor only (ZOM-162, 163, 173, 200, 201, 250, 277, 315), 3 Not shipped, 1 Replaced.
- 13 comments (no comment on ZOM-312). Shares: Robert and Brian writer, Leonard commenter, Arthur reader.
- The DM reply: 28 and the counts, the 11 keys, ZOM-254 replaced by ZOM-282, and the starting tier after the first 10 games.

**Round 2 changes** (10c1ee9238d4 → 6972a45038e9; 163 → 164 INSERTs):

| Statement(s) | Change |
|---|---|
| linear_comments (new) | cmt_df69e4a92767cbff0000 on ZOM-281 by Blake (usr_cc3e90160f490686), 2025-06-27T09:34:19Z: "tiers: closing. checked on the dev build" |
| slack_messages (S_ASK) | the ask now ends "…how many of each status, and tell me when a new player gets their starting tier" |
| trello_cards + updateCard desc | rule 1 "plus any ticket Blake counts as tier work"; rule 5 adds "where a write-up and the build disagree, go by the build" (narrowed in 52c581f442c1, see below) |

**/prompt attempt 7 fix** (6972a45038e9 → 52c581f442c1; 164 INSERTs, only the card text): /prompt found fork S. The build clause also reached promotion and demotion, where WinHistory.cs counts the first games since a tier change and ZOM-42 says the most recent. Rule 5 now reads "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build. For which games promotion and demotion look at, write it the way ZOM-42 words it." L4 is unchanged. The /prompt report also says to credit "10 levels" as well as "10 games" (rubric note 2), so L4 only fails a run that writes ZOM-42's "6-7 levels" or levels-not-games with replays excluded. L4's projected rate rises from 0.2 to about 0.8, and the six-run projection moves from about 68% to about 71%.

**Facts that changed** (round 2 supersedes round 1 where they differ):
- Register: 30 rows (adds ZOM-281). Counts 30 — 17 Live, 9 Editor only, 3 Not shipped, 1 Replaced.
- The DM reply must also say that a new player gets the starting tier after the first 10 games, won or lost (not after level 10).
- The rules tab's starting tier says the same.

**Facts that changed in round 1**, for the human, OEs and rubric:
- **Register:** 29 rows. Out: ZOM-30, ZOM-49, ZOM-50, ZOM-161, ZOM-262, ZOM-275.
- **Counts:** 29 tickets — 16 Live, 9 Editor only, 3 Not shipped, 1 Replaced (ZOM-254 → ZOM-282).
- **DM reply:** the counts plus the keys. Not shipped: ZOM-202, ZOM-280, ZOM-293. Editor only: ZOM-162, ZOM-163, ZOM-173, ZOM-200, ZOM-201, ZOM-250, ZOM-277, ZOM-312, ZOM-315.
- **Linear comments, 14:** ZOM-199 (> 90), ZOM-254 (replaced by ZOM-282), and one on each of the 9 Editor only and 3 Not shipped tickets saying the change isn't in the store builds.
- **Shares:** Robert and Brian writer; Leonard and Arthur commenter.
- Unchanged: the folder, the two tabs and the rules tab.

**Prompt-side defects:** none. The prompt (22f26066688c) already says "go through his ask and everything it points to", "if his rules say something needs to happen on the tickets, go ahead and do that too" and "reply to leonard in the dm with what he asked for". It stays unchanged.

| # | Quoted span | Rule (doc §) | Defect | Evidence (rollout · step) |
|---|---|---|---|---|
| — | none | — | — | run-1 · event 6–23 read the ask, card and thread the prompt points to |

**Routed observations for `/create-oe-writing` and `/create-rubric-writing`** (facts and weights only, no wording):
- **Weight plan:** keep the §2 plan. Per-ticket status rows at 1. One row per excluded ticket at 3. Total and Live counts at 5. One row per reply key at 1. One row per required comment (14) at 3. One row per share role at 3. Mechanism share ≈ 50%.
- **Keep off:** the "first 10 levels vs games" window, enrage damage stacking, the win-history direction, and values for Mailman, Mayor2 and PartyGirl.

## 12 Self-review

**Round 7 counter-readings:**

| Claim | Counter-reading | Resolution (evidence) |
|---|---|---|
| #271's inline comments are skipped by about half the runs | runs that see an empty-body review may dig, as they did on #265 | on #265 every run was looking for the 'not tiers' mark it had found nowhere else; run-4 and run-6 read #271's reviews list and stopped (run-4 · event 1866, run-6 · event 2665); the risk is stated in section 2 |
| The 'not tiers' mark is credible on an enrage ticket | /prompt may read it as contradicting rule 1's scope | rule 1 says a title match Blake marked 'not tiers' stays off, whatever the title; the comment gives the reason (a bug fix, no tier version or enrage number changes), which the PR's four files bear out |
| The pacific day has one answer | Linear shows UTC and a run may argue for it | Robert names pacific time; only ZOM-200, 274 and 282 differ, and the rubric grades those three days |
| run-1's misses were a tool fault | the DM thread read may have errored | run-1 never called slack_read_thread on the DM; it read Robert's thread at run-1 · event 80 |


**Round 6 counter-readings:**

| Claim | Counter-reading | Resolution (evidence) |
|---|---|---|
| Thread replies are the only lever that lands | a verifier slip could hide other failures | statuses read straight from the write payloads: all 24 right in run-3 · event 2122, run-5 · event 2330, run-6 · event 2099 |
| run-2 missed the threads by habit | it may have hit a tool defect | channel_not_found came from the user id (run-2 · event 13); the DM id works (run-3 · event 19), so it is a run choice, not a defect |
| Robert's reply is fair | the card might not lead there | card rule 2 names 'the three things Robert asked for when I asked him in our group chat'; Julia is a member (check-sql YES, slack abe096ff0b5d7216efbc889e91d6d13a)  |
| The done day has one answer | a UTC versus PT day could split it | rubric spot checks use tickets done between 07:00 and 23:59 UTC, the same day in both |


**Round 5 counter-readings.**

| Verdict | Strongest counter-reading | Resolution (pointer) | Unresolved |
|---|---|---|---|
| T22 LANDED 5 | tool: the DM read did not return reply counts | run-1 · event 6 returned reply_count 1 on the ask; run-5 · event 19 shows slack_read_thread works on the same ts | none |
| T28/T29 LANDED 5 | fairness: the checklist's 'Brian gets edit' is a second valid end state | Leonard's later reply (Sep 30 21:16Z) takes it back; /prompt PASS 5 and /rubric PASS 5 accepted one end state | none |
| T26 LANDED 1 | tool: run-1's review call did not expose the inline comment | the review-comments call exists and returned it in run-2 · event 2167; run-1 never made it | none |
| T27, T23, T6 LEAKED 6 | the traps were never live | all three were read and applied (run-1 · event 27, 20, 44); live but solved, not FALSE | none |
| T30 (new) | fairness: a reply in another conversation is unfindable or not 'his reply' | In-Reply-To/References name the first mail; rules 3 and 6 name the reply; 'from:arthur.blake@harmonygames.co' and 'ZOM-199' searches return it (re-verified in the SQL) | catch rate unmeasured (projection pG 0.3–0.7) |
| T31 (new) | padding: the build numbers are an extra deliverable | it is content of a required write, asked by the requester in his ask's thread (A21) | none |
| Band (4 for a both-miss run) | neighbouring band 3 | two independent consequential families (row set and statuses), not one bounded correction; compare run-5 · event 2153 (both carriers) with run-2 · event 2275 | none |

Re-verified through tools/hg.py and the SQL: TierManager.cs 'totalGames == 10' and 'cpm > 90.0f', WinHistory.cs wins + losses (the reply's claims); Assets/Scripts/LevelEditor and Assets/Scripts/Debug exist; GameLoader.cs RemoveRandomObjects (ZOM-300 rejected); match3d PR numbers 1..544 with no gaps (candidate 20 rejected); ZOM-509 2025-08-28 and ZOM-510 2025-09-01T14:56Z (candidate 21 rejected). Mechanical checks re-run after the SQL change: sql_lint 0 errors, hardness_gate PASS, stage_gate injection PASS. Clean average recomputed with tools/difficulty_stats.py on the verifier matrix: 77.1%.


**Round 4 counter-readings.**

| Verdict | Counter-reading | Resolution (evidence) |
|---|---|---|
| T22 LANDED in run-3 | a tool defect, not a skipped carrier | the call is the run's own wrong argument (Leonard's user id instead of D05HB64NMQU); run-1 · event 17 shows the same tool works with the DM id |
| T22 LANDED in run-4 | the reply was invisible | run-4's own parse (run-4 · event 6) dropped reply_count; the field is in the result, as run-5 printed it |
| T26 LEAKED 6/6 | the review lever never had a chance | it did: run-1 · event 2160 called get_pull_request_reviews only because rule 1 names the review; that is why carriers pointed by the card are no longer levers |
| projection < 75% | argue the neighbouring outcome (≥ 75%) | it holds only if q ≥ 0.35; at q = 0.3 the average is 76%. The reply_count of 1 shows on Julia's message right below the ask in the parse output that runs print (run-1 · event 6), so q is not certain |
| band 3 | argue band 2 | a run that opens both threads gets everything right, as runs 1, 2, 5, 6 did on round 3 (run-1 · event 17 opened the thread); P ≈ (1 − p1)(1 − q) ≈ 0.33 |
| L7 is part of 'his ask' | argue it is outside the ask | the reply is Leonard's, in the same DM, and opens "one more for the baseline"; the prompt says "leonard dm'd me … asking for a baseline … go through his ask" |
| Brian's role | argue the checklist wins | the checklist item is 2025-09-30T16:20:11Z (68dc033b328def4251f2a731); Leonard's reply is 21:16:42Z and says "scratch brian editing" (D05HB64NMQU/1759267002.665190) |


Walked `Evals/1A_Hardness_Eval.md` §3–§5 against this report. There are no LANDED verdicts in run-1. Each LEAKED verdict is counter-read below to check whether the trap was live.

| Verdict | Counter-reading | Resolution (evidence) |
|---|---|---|
| T1 LEAKED | the comment was never in the run's path | live: run-1 · event 16 returned it and event 70 used it |
| T2 LEAKED | the window had no edge case to fail | live: ZOM-517 (created 2025-09-03) exists; event 70 applied ≤ Aug 31 |
| T3 LEAKED | ZOM-271 never surfaced | live: event 70 listed near misses including ZOM-271 |
| T4 LEAKED | duplicates were obvious | live but easy: Linear state Duplicate for ZOM-203 and ZOM-276 is in the list result (run-1 · event 56) |
| T5 LEAKED | the notes handed over the answer | yes, the note is explicit (cmt_b0aa45d307c981ce4487 "nothing changes in the game itself"); this is why L1/L2 were added |
| T6 LEAKED | the thread was not opened | false: event 23 get_thread returned both messages |
| T8 LEAKED | the sheet answered without the chain | yes: event 48 read the Live tab directly; the chain added no difficulty |
| T9 LEAKED | the Next pass tab was not read | false: event 48 requested all three tabs |
| T10 LEAKED | the description was truncated | false: event 359 get_issue returned the full spec |
| T11 LEAKED | the deck was not read | false: event 41 |
| T12 LEAKED | the decoy was not returned | false: event 13 returned both cards (verified: the search result contains 683dbef4e319167a802bd888) |
| T13 LEAKED | the invite was not read | false: event 20 |
| T14 LEAKED | the rule left nothing to get wrong | rule 6 is closed (card 68daca5871dba40417a00383); run-1 · event 2165 / 2167 wrote exactly two, on ZOM-199 and ZOM-254 |
| T15 LEAKED | the notes settled it before the PRs | yes: the notes split the shared PRs; event 2105–2128 only confirmed |
| T18 LEAKED | the subagent filter was given the tag | yes, from rule 1 (event 105 prompt); the tag is a fair, findable rule |
| T20 LEAKED | the lives tickets were not compared | event 2150: ZOM-305 in, ZOM-352 out, as designed |
| T21 LEAKED | rule 4 hands over the answer | rule 4 is record-based by design (prompt round 2); event 2167 |
| T7 / T16 / T19 BYPASSED | the Slack decoys were never live, so they are FALSE, not BYPASSED | they were live (C090N54TG79/1759185077.402611, C090N54TG79/1759248760.118527, C08R27X0EAH/1758081917.318539 exist and are visible to Julia) but off run-1's path (no channel read after event 6); kept for realism, no weight planned (§9) |
| T22 new lever | the thread reply is too easy to see, since the parent shows reply_count | run-1 · event 10 printed only ts/time/user/text from the 83 KB DM dump; Hardness_Mastery A14 (67/124 runs never open replies); estimate p1 0.3–0.5, stated as unresolved |
| T23 new lever | the checklist shows in the search result, so every run opens it | run-1 · event 13 result shows only badges.checkItems and idChecklists (68dc033bf7d24e86b8a9cc67 after hardening); the items need trello_get_checklist; estimate p2 0.4–0.5, stated as unresolved |
| T22 LEAKED (run-2) | the thread reply was too visible to be a lever | run-2 · event 13 (report) found it; run-1 · event 10 did not, so it splits runs (kept) |
| T23 LEAKED (run-2) | the checklist was too visible to be a lever | run-2 · event 18 (report) fetched checklists; run-1 · event 13/16 did not (kept) |
| T26 new lever (round 3) | the rule names the PR review, so every run reads it | the rule names the review, but the review body is empty and the text is an inline comment; 0 of 3 runs called a review tool (run-3 · event 320–434); Douglas: 1 of 20 runs reached a late inline comment; estimate p5 0.4–0.5, unresolved |
| T27 new lever (round 3) | badges.attachments 1 makes every run fetch it | run-2 and run-3 asked for attachments and dropped them after the error (event 18 → 22) before seeing the badge; with the badge at 1 some runs retry; estimate p6 ≈ 0.5, unresolved |
| Band (round 3) | argue band 2: a run reads everything again | that needs both new surfaces in one run (≈ 0.2); run-3 read 836 calls without either tool |
| Band (round 2) | argue band 2: a run that finds every lever and writes "games" is Easy again | that needs the full 110-ticket comment scan (run-2 did about 107, report §6) and the code-over-doc answer that 0 of 2 runs gave (run-1 · event 2152; run-2 · event 658 (report)); the fact is code-true (TierManager.cs totalGames == 10; WinHistory.GetTotalGames) and settled by rule 5 |
| Band 4 (prediction) | argue band 3: only L1 or only L2 would bind | for a run like run-1 (neither carrier opened, events 6–16) both bind, giving two independent root causes; a one-carrier run is 3, as §3 says |
| Band 4 vs 5 | the central result is defeated | no: the register, statuses, folder, rules tab and core shares are correct (run-1 · event 2150–2163) |

Re-verified for round 3 (base exports read-only; git run only on a copy of match3d/.git in the scratchpad):
- match3d#265: author EMPLOYEE_0025, reviews rev_1–rev_7 (Blake COMMENTED empty-body rev_3, rev_5), inline comments rc_1–rc_6, merged 2025-07-03T18:01:36Z; no "not tiers" text anywhere in base GitHub or Linear;
- ZOM-312's closing note "merged with match3d#265" (seeded); ZOM-258 "Icon for Enraged monster" Done (linear data.json);
- Trello base: 106 attachments on 42 cards, 6 cards without an addAttachmentToCard action.

Re-verified through `tools/hg.py` sources, the SQL and the match3d export:
- TierManager.cs (`totalGames == 10`, `cpm > 90.0f`) and WinHistory.cs (`GetTotalGames() = GetTotalWins() + GetTotalLosses()`);
- ZOM-281's title, state Done, assignee EMPLOYEE_0032_EMAIL and updated_at before the clock (linear data.json).

Also re-verified for round 1:
- the thread reply row and the parent's reply_count (01_Universe_Inject.sql S_ASK / 33c941fae57ba8d1e23bc1dff9ce3e2c);
- the checklist rows and action (68dc033bf7d24e86b8a9cc67, 68dc033b328def4251f2a731);
- the match3d PR merge dates for #243–#319 (github data.json);
- the 6 dropped tickets' titles (linear data.json);
- the assignees (5 × EMPLOYEE_0032_EMAIL).

Unresolved:
- p1 and p2 are estimates from one run and Hardness_Mastery A14, not measured. The projected average depends on them (§2). The weight plan must be honoured at the rubric stage, or the average rises.

```
STAGE GATE hardening: PASS — Task_Authoring-2/task_inputs · 01a_Hardening_Report.md#af109e285c76 · 01_Universe_Inject.sql#b64bc2f2c6dc · 01_Hardness_Manifest.json#a3264f8b32ac · blocking 0 · warnings 0 · checks 14
[PASS] structure.outputs: 1 output(s) present: 01a_Hardening_Report.md
[PASS] structure.inputs: 2 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 06_PreCheck_Trajectory, 07_Baseline_Trajectories, 10_Baseline_Verifier_Results.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#b64bc2f2c6dc, 01_Hardness_Manifest.json#a3264f8b32ac, 01_Grounding_Dossier.md#dfb5e8014ce1)
[PASS] structure.sections: 6 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] structure.placeholders: no placeholders in 01a_Hardening_Report.md
[PASS] structure.mode: MODE B declared
[PASS] evidence.register_run_step: 53/53 items carry a source pointer (min 100%)
[PASS] structure.sections: 4 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] revision.injection: injection checks re-run on revision N+1 (current SQL + manifest + dossier): PASS
[PASS] review.counter_readings: 48 evidenced counter-readings (of 50 found; need ≥ 43) in 01a_Hardening_Report.md
[PASS] review.coverage: self-review addresses all 2 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```











## 13 Next steps

**Round 7 next steps:** paste SQL b64bc2f2c6dc into /injection; run /prompt; re-inject and run /hardness; then update the Oracle Events and rubric (23 / Live 15, ZOM-295 off, pacific done days, Robert's columns, round-5 items), run /oe and /rubric, then the six baselines and /create-difficulty.


**Round 6 next steps:** paste SQL f6afeda7b086 into /injection; run /prompt; re-inject and run /hardness; then update the Oracle Events and rubric (Robert's columns, round-5 items), run /oe and /rubric, then the six baselines and /create-difficulty.


**Round 5.**
1. /injection on SQL 7966b1496ad9 (paste task_inputs/01_Universe_Inject.sql), then /prompt (card rule 3 changed; the prompt text is unchanged).
2. Re-inject on the platform, then /hardness on a fresh Opus run.
3. Run the six baseline rollouts and the verifier on the updated rubric.
4. /create-oe-writing (ledger, events, check) and /create-rubric-writing (plan, draft, check) for the round-5 facts, then /oe and /rubric.
5. /create-difficulty on the new verifier results.


**Round 4.** SQL 2ee488e28ab5 → cd185b05da3d → dd7536cdea3f (prompt-11 fork fix) (172 INSERT, 3 UPDATE; adds D05HB64NMQU/1759181932.207413 and D05HB64NMQU/1759267002.665190, and the PR #401 updated_at fix). Prompt unchanged. Human time 16.75 h (was 17.75 h).
1. `/injection` on dd7536cdea3f.
2. `/prompt` with the unchanged prompt.
3. One fresh unhinted Opus run, then `/hardness`.
4. Six new baseline rollouts; `/create-oe-writing` and `/create-rubric-writing` with the §2 round 4 weight plan.


1. Paste the round-3 `01_Universe_Inject.sql` into `/injection` (its sha256 is in the routing section).
2. Run `/prompt` with the unchanged `04_Prompt.txt` (card rule 1, a PR review, a card attachment and a doc changed, so `/prompt` re-checks them).
3. Get a fresh unhinted Opus run, then `/hardness`.
4. Then `/create-oe-writing` and `/create-rubric-writing`, using the §11 facts and the §2 weight plan (rounds 1 and 2).

