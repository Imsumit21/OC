"""Round 6 blocks for 01a_Hardening_Report.md: inserted at the top of each section (after its heading).

Usage (from Task_Authoring-2): python3 support/task_work/jl_difficulty/report_r6.py <round-5 report> <out report>
"""
import sys

src, out = sys.argv[1], sys.argv[2]
s = open(src).read()
s = s.replace("· rounds 1–5", "· rounds 1–6", 1)
P_ID, R_ID = 'cec246a6e43158f200fe144f0dd7039c', 'abe096ff0b5d7216efbc889e91d6d13a'

B = {}
B["## 1 Mode, inputs and run validity"] = """**Round 6: MODE B (baseline, no verifier yet).** Six Opus 5.5 baseline rollouts on SQL 7966b1496ad9 (round 5), plus the /hardness run on the same SQL (NON-FAIL 4, task_inputs/Audit-Report/1a_hardness_NONFAIL_r5.md). The rubric was not yet brought to round 5, so no verifier file exists; verdicts below come from the write payloads.

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

"""
B["## 2 Gate status, projection and mechanism weight share"] = """**Round 6 projection from the round-5 SQL runs** (no verifier file; rows scored from the payloads on the 68-row rubric): runs 3, 5 and 6 pass every row; runs 1, 2 and 4 fail the thread rows (R5–R7, R39, R52–R55, 38 of 160). Projected average about 88%, one failure pattern (100% of failing runs), pass@1 3/6. Both gates fail; the round-5 levers (T30 Gmail reply in its own thread, T31 builds in comments) landed 0/6: every run found the reply with a sender search (run-1 · event 54, run-3 · event 58) and every run named the builds, which also sit in the first mail (run-1 · event 1556, run-6 · event 2127).

**Read-habit rates across 22 runs** (three baseline batches plus four hardness runs): thread replies opened about 45%; PR #271 review comments about 50%; PR file lists about 55%; PR #243 / #244 review comments 70 to 75%; code about 80%; the card, notes doc, both Blake mails, the invite and every Linear comment 100%. Every judgement trap was resisted in 22 of 22 runs (all 24 statuses right in every register); ZOM-312 was kept only by runs that skipped the #265 review comments (2 of 22), ZOM-258 once.

**Round 6 lever:** a third thread reply in a different conversation (group chat CAFC495E4006), carrying three graded Tickets-tab columns, so graded weight behind thread replies rises from 24% to about 45% and failing runs split by which threads they opened. Monte Carlo (scratchpad r6/mc8.py, 3 columns, 5 spot checks plus a volume row each): with the threads missed together 50% of the time and a 55% miss rate, average about 74%, P(largest pattern ≤ 50%) about 0.6, P(all gates) about 0.25; when runs open all threads or none (correlation 0.9) P(all gates) falls to about 0.02. The risk is stated, not hidden.

"""
B["## 3 Predicted /hardness band"] = """**Round 6:** the /hardness run on the round-5 SQL scored 4 (NON-FAIL, PROCEED): it missed both DM thread replies (F1). Round 6 adds a third thread; a run that misses threads also misses Robert's columns, so the band stays 4 or rises toward 5. A fresh unhinted Opus run on SQL f6afeda7b086 is needed.

"""
B["## 4 Designed-difficulty register (verdicts)"] = """**Round 6 verdicts (round-5 SQL runs):**

| Trap | Verdict | Evidence |
|---|---|---|
| T22 / T28 / T29 (Leonard's two thread replies) | LANDED 3/6 | run-1 · event 1540 (34 rows), run-2 · event 13 (channel_not_found), run-4 · event 2188 (Brian writer) |
| T26 (ZOM-312 'not tiers' in #265 review comments) | LANDED 1/6 (only the run that skipped them) | run-2 · event 2280 |
| T30 (Blake's reply in its own thread) | RESISTED 6/6 | run-1 · event 54, run-5 · event 64 |
| T31 (builds in comments) | RESISTED 6/6 (builds also in the first mail) | run-3 · event 2152, run-6 · event 2119 |
| T1–T21, T24, T25, T27 | RESISTED 6/6 | statuses all right in run-3 · event 2122 and run-1 · event 1540 |
| T32 (round 6: Robert's thread reply) | NEW, untested: today every register has the five agenda columns only (run-3 · event 2122, run-1 · event 1540) | {CAFC495E4006 thread} |

""".replace("{CAFC495E4006 thread}", f"slack {R_ID}")
B["## 8 Why Opus passed"] = """**Round 6:** runs that open the DM threads make no other mistake. Opus resolves every judgement trap (status splits, replacements, decoys, title aliases) from records it reads anyway, so the only failures are records it never opens. One carrier gives one failure pattern.

"""
B["## 10 Candidates and selection (rebuild)"] = """**Round 6 candidates:**

| # | Candidate | Verdict | Reason |
|---|---|---|---|
| 26 | Move the ZOM-277 / ZOM-315 editor evidence into Blake's PR review comments | REJECTED | neither ticket has a PR (GitHub data.json search: only ZOM-173, 295, 303 and 312 do) |
| 27 | Blake 'not tiers' review comments on #271 (ZOM-295) or #244 (ZOM-303) | REJECTED | both are core gameplay tier work; their descriptions match the code, so a 'not tiers' or 'text is wrong' mark is not credible |
| 28 | 'not tiers' on #243 (ZOM-173) | REJECTED | changes count rows only, which the thread misses already fail; Monte Carlo P(all gates) about 0.02 |
| 29 | Third thread reply in a different conversation: Robert's three Tickets-tab columns in the group chat, card rule 2 points to it | ACCEPTED | unique positive rows (assignee, done day, priority for 24 tickets); separate conversation; earlier batch showed runs opening one thread and not another (4 of 6) |

"""
B["## 11 Routing"] = f"""**Round 6 routing:** SQL f6afeda7b086 (harden_r6.py): +2 slack rows in group chat CAFC495E4006 (Leonard's question {P_ID}, Robert's thread reply {R_ID}); card rule 2 (desc and updateCard action) names the three things Robert asked for; header counts. Next: /injection, then /prompt (card text changed), /hardness on a fresh run, then OE and rubric (new rows for the three columns; spot checks on unambiguous values only), then six baselines.

"""
B["## 12 Self-review"] = """**Round 6 counter-readings:**

| Claim | Counter-reading | Resolution (evidence) |
|---|---|---|
| Thread replies are the only lever that lands | a verifier slip could hide other failures | statuses read straight from the write payloads: all 24 right in run-3 · event 2122, run-5 · event 2330, run-6 · event 2099 |
| run-2 missed the threads by habit | it may have hit a tool defect | channel_not_found came from the user id (run-2 · event 13); the DM id works (run-3 · event 19), so it is a run choice, not a defect |
| Robert's reply is fair | the card might not lead there | card rule 2 names 'the three things Robert asked for when I asked him in our group chat'; Julia is a member (check-sql YES, slack {R})  |
| The done day has one answer | a UTC versus PT day could split it | rubric spot checks use tickets done between 07:00 and 23:59 UTC, the same day in both |

""".replace("{R}", R_ID)
B["## 13 Next steps"] = """**Round 6 next steps:** paste SQL f6afeda7b086 into /injection; run /prompt; re-inject and run /hardness; then update the Oracle Events and rubric (Robert's columns, round-5 items), run /oe and /rubric, then the six baselines and /create-difficulty.

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
