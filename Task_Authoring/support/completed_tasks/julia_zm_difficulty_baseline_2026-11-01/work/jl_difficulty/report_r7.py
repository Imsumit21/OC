"""Round 7 blocks for 01a_Hardening_Report.md: inserted at the top of each section (after its heading).

Usage (from Task_Authoring-2): python3 support/task_work/jl_difficulty/report_r7.py <round-6 report> <out report>
"""
import sys

src, out = sys.argv[1], sys.argv[2]
s = open(src).read()
s = s.replace("· rounds 1–6", "· rounds 1–7", 1)
PR = 'harmonygames-Games/match3d#271'

B = {}
B["## 1 Mode, inputs and run validity"] = """**Round 7: MODE B (baseline, no verifier yet).** Six Opus 5.5 baseline rollouts on SQL f6afeda7b086 (round 6), after /injection PASS, /prompt PASS 5 and /hardness NON-FAIL 3 PROCEED on the same SQL (task_inputs/Audit-Report/0_injection_PASS_r12.md, 1_prompt_PASS_r13.md, 1a_hardness_NONFAIL_r6.md). No verifier file exists yet; verdicts below come from the write payloads.

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

"""
B["## 2 Gate status, projection and mechanism weight share"] = """**Round 7 projection from the round-6 SQL runs** (payloads scored against the round-6 answer key): runs 2 to 6 pass every row (24 rows and statuses, all 69 assignee / done day / priority cells, 9 comments, shares, the DM with 24 / 16 / 4 / 1 / 3 and the keys: run-2 · event 2076, run-6 · event 2789); run-1 fails the thread rows (34 rows at run-1 · event 2326, Brian writer at run-1 · event 2335). Projected average about 95%, pass@1 5 of 6, one failure pattern. With difficulty mode medium the average limit is 85%; pass@1 and the pattern gate fail regardless. The round-6 lever (Robert's thread) landed 0 of 6: every run read it (run-1 · event 80, run-5 · event 74).

**Round 7 levers and replay.** (1) Blake's 'not tiers' inline comment on PR #271 (ZOM-295 off): over 15 runs, #271's inline comments were fetched by 5 (run-2 · event 1986, run-3 · event 3812, run-5 · event 2051, plus two earlier runs); run-4 and run-6 read #271's reviews list but not its inline comments (run-4 · event 1866, run-6 · event 2665). GitHub comment search does not reach review comments. (2) Robert's done day in pacific time: every run wrote the UTC day for ZOM-200, ZOM-274 and ZOM-282 (run-3 · event 3844, run-6 · event 2751). Replay of lever 1 alone: round-5 batch 6 failing runs in 3 patterns (largest 50%), average about 78%; round-6 batch 3 failing runs, two identical (largest 67%), so lever 2 has to split them. Risks stated: the approval with an empty body may draw more runs into the inline comments than the replay shows; lever 2 compliance is untested.

"""
B["## 3 Predicted /hardness band"] = """**Round 7:** the round-6 hardness run scored 3 (it missed ZOM-281 after stopping the subagent that found it). On the round-7 SQL a run that skips #271's inline comments keeps ZOM-295 (23 expected, 24 given); a run that keeps the UTC day misses three done dates. Predicted band 3, or 4 when both are missed. A fresh unhinted Opus run on SQL b64bc2f2c6dc is needed.

"""
B["## 4 Designed-difficulty register (verdicts)"] = """**Round 7 verdicts (round-6 SQL runs):**

| Trap | Verdict | Evidence |
|---|---|---|
| T32 (Robert's thread reply) | RESISTED 6/6 | run-1 · event 80, run-2 · event 100 |
| T22 / T28 / T29 (Leonard's two thread replies) | LANDED 1/6 | run-1 · event 2326 (34 rows), run-1 · event 2335 (Brian writer) |
| T26 (ZOM-312 'not tiers' on #265) | RESISTED 6/6 | 24 rows without ZOM-312 at run-3 · event 3844 |
| T1 to T21, T24, T25, T27, T30, T31 | RESISTED 6/6 | statuses all right at run-4 · event 1946 and run-5 · event 2076 |
| T33 (round 7: 'not tiers' on #271) | NEW, replay: missed by run-1, run-4, run-6 of this batch | run-4 · event 1866 (reviews only), run-6 · event 2665 (reviews only) |
| T34 (round 7: pacific done day) | NEW, untested: all six wrote the UTC day | run-3 · event 3844, run-6 · event 2751 |

"""
B["## 8 Why Opus passed"] = """**Round 7:** Opus reads every carrier the card names and applies each rule it reads. The round-6 runs made 716 to 1,356 calls and opened all three thread replies in five of six runs. What they skip is a second read inside a record they have already opened: a PR's inline comments after its reviews list (run-4 · event 1866), and they keep Linear's UTC stamp as the date (run-2 · event 2041).

"""
B["## 10 Candidates and selection (rebuild)"] = """**Round 7 candidates:**

| # | Candidate | Verdict | Reason |
|---|---|---|---|
| 30 | 'not tiers' inline comment on PR #271 (ZOM-295) | ACCEPTED | fetched by 5 of 15 runs; card rule 1 already governs it; the comment calls the PR a bug fix (enrage was meant to clear on refill health and push back), true to the ticket and the diff |
| 31 | Robert asks for the done day in pacific time | ACCEPTED | every run wrote the UTC day; three tickets differ (ZOM-200, 274, 282); unique answer |
| 32 | Another 'not tiers' on #243 (ZOM-173) | REJECTED | #243's inline comments were fetched by 10 of 15 runs, twice the #271 rate |
| 33 | A lever in the #zombie-prs feed or GitHub issue comments | REJECTED | no run opened the feed; a lever no run reaches is an all-fail row |

"""
B["## 11 Routing"] = f"""**Round 7 routing:** SQL b64bc2f2c6dc (harden_r7.py): +4 rows: {PR}#rev_2 (APPROVED, empty body), {PR}#rc_1 ('not tiers' on MonsterSpawner.cs), two #zombie-prs mirrors (approval and comment) under #271's opened post with reply_count 4 to 6; Robert's thread reply asks for the done day in pacific time; header counts. New answer: 23 tickets (Live 15, Editor only 4, Replaced 1, Not shipped 3); done days ZOM-200 2025-06-12, ZOM-274 and ZOM-282 2025-06-20. Next: /injection, /prompt, /hardness on a fresh run, then OE and rubric, then six baselines.

"""
B["## 12 Self-review"] = """**Round 7 counter-readings:**

| Claim | Counter-reading | Resolution (evidence) |
|---|---|---|
| #271's inline comments are skipped by about half the runs | runs that see an empty-body review may dig, as they did on #265 | on #265 every run was looking for the 'not tiers' mark it had found nowhere else; run-4 and run-6 read #271's reviews list and stopped (run-4 · event 1866, run-6 · event 2665); the risk is stated in section 2 |
| The 'not tiers' mark is credible on an enrage ticket | /prompt may read it as contradicting rule 1's scope | rule 1 says a title match Blake marked 'not tiers' stays off, whatever the title; the comment gives the reason (a bug fix, no tier version or enrage number changes), which the PR's four files bear out |
| The pacific day has one answer | Linear shows UTC and a run may argue for it | Robert names pacific time; only ZOM-200, 274 and 282 differ, and the rubric grades those three days |
| run-1's misses were a tool fault | the DM thread read may have errored | run-1 never called slack_read_thread on the DM; it read Robert's thread at run-1 · event 80 |

"""
B["## 13 Next steps"] = """**Round 7 next steps:** paste SQL b64bc2f2c6dc into /injection; run /prompt; re-inject and run /hardness; then update the Oracle Events and rubric (23 / Live 15, ZOM-295 off, pacific done days, Robert's columns, round-5 items), run /oe and /rubric, then the six baselines and /create-difficulty.

"""
for head, block in B.items():
    i = s.find(head)
    assert i >= 0, head
    j = s.find("\n", i) + 1
    if block.splitlines()[0] in s:
        continue
    s = s[:j] + "\n" + block + s[j:]
assert '—' not in ''.join(B.values())
open(out, 'w').write(s)
print('ok')
