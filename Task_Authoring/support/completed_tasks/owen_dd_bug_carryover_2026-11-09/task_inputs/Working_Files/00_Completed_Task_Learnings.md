# Learnings from the eight completed tasks, and how they bind this design

Written 2026-11-07, before `/create-scenario`. Sources:

- `Task_Authoring/support/completed_tasks/*/README.md` (each folder's Lessons carried forward)
- each task's `12_difficulty_input.json`, `01a_Hardening_Report.md` and stored baseline trajectories
- the Frederick learnings in `frederick_q4_commitments_2026-11-05/task_inputs/Working_Files/00_Completed_Task_Learnings.md`
- the root `learnings` file §1–62

Every number below is measured on real Opus runs, except where marked UNCALIBRATED. The table is reproduced by `00_PreScenario/completed_tasks_table.py`.

## Requester targets for this task (stricter than the assignment)

| Target | Requester | Assignment / gate | Design target |
|---|---|---|---|
| Counted tool calls | **Over 130 in each run** | Long Horizon ≥ 100 (golden run, else the average) | Weakest of six runs about 160 or more |
| Average weighted pass | **Strictly under 80 %** | Medium < 85 % | E[avg] ≤ 72 % (8 points under the requester line) |
| Spread, passes, patterns, errors | All other difficulty guidelines | SD 0.10–0.30, < 5 full passes, ≥ 2 patterns (largest ≤ 50 %), ≤ 2 errored, six Opus 5.5 slots | P(all gates together) ≥ 0.6 at 0.7× design rates (UNCALIBRATED) |

## What the eight tasks measured

| Task | Rows | Avg | SD | Full passes | All-pass weight | Mixed weight | All-fail weight | Counted calls | Writes | Reads |
|---|---|---|---|---|---|---|---|---|---|---|
| **Douglas beta sign-off** | 76 | **56.3 %** | **0.117** | 0 | 44.6 % | 29.0 % | 26.4 % | **163–238** | 19–29 | 137–211 |
| Bridge pipeline | 40 | **77.7 %** | **0.106** | 1 | 61.3 % | 38.7 % | 0 % | 109–150 | 53–55 | 54–95 |
| Account handover (Normal) | 37 | 80.8 % | 0.161 | 1 | 50.4 % | 49.6 % | 0 % | 68–100 | 6–11 | 57–93 |
| Card spend | 63 | 78.3 % | 0.054 | 0 | 65.0 % | 26.7 % | 8.2 % | 554–573 | 12–22 | 535–561 |
| Q4 commitments | 102 | 71.0 % | 0.016 | 0 | 61.1 % | 15.1 % | 23.7 % | 151–212 | 88–93 | 61–119 |
| Julia ZM baseline | 81 | 83.8 % | 0.099 | 1 | 66.5 % | 33.5 % | 0 % | 357–1,209 | 19–25 | 342–1,185 |
| Robert LLC | 130 | 83.6 % | 0.103 | 1 | not stored | not stored | 0 % | 149–162 | 80–86 | 69–81 |
| Robert close-out | 136 | 85.7 % | 0.034 | 0 | 77.4 % | 18.0 % | 4.6 % | 116–143 | 43–48 | 73–96 |

**Only Douglas met all three of your targets** (under 80 %, SD at least 0.10, every run over 130). Bridge met the first two, but its weakest run was 109.

## What landed and what leaked, by carrier

| Carrier | Measured | Task |
|---|---|---|
| Inline PR review comment | Read 4 of 20 on early PRs, 1 of 20 on the late one; landed in all 6 baselines | Douglas |
| PR review body | Swept: 109 calls on Douglas, 504 on Julia | stored runs |
| Reply under an unrelated root | Caught 2 of 8, then 3 of 6 | Bridge |
| Later post in another channel | Caught 0 of 7, then 3 of 6 | Bridge |
| 1:1 DM about one item | About 3 of 6 | Bridge |
| Mail a keyword search won't return | Missed 5 of 6 | Handover |
| Mail with an empty-looking snippet | Landed on the pre-check | Robert LLC |
| Linear comments on in-scope tickets | Swept: all 37 issues, 632 reads on another run | Robert |
| Rule in a doc every run reads | Leaked 6 of 6 | Handover, Robert |
| Calendar-only item | Leaked | Bridge |
| Same-thread correction, visible caveat | Leaked | every task |
| Judgement after retrieval (status, title match) | 0 landings in 28+ runs | Julia |
| Correction hidden so well no run finds it | Missed 6 of 6, which flattened SD to 0.016 | Q4 |

Linear writes are safe at volume: `linear_update_issue` 339 calls and `linear_create_comment` 523 calls, 0 errors. `linear_create_issue` is lightly proven: 2 calls, both clean, one setting `state`.

## Rules this design takes from them

1. **The weakest run is set by writes.** Reads fall to about 54–70 on ticket and list tasks. Q4 and Robert LLC cleared 130 with 80–93 writes; Bridge's 53–55 left a 109 run. So this task needs about 110 per-entry writes that happen in every run, whichever traps land.
2. **High-count writes must be template-identical.** /rubric gives one row to each write whose content differs by target. That took Robert LLC from 73 to 130 rows and its proxy from about 76 % to 83.6 %. Template-identical writes are sampled at ≤ 5 plus a volume row (Bridge: 55 writes on 40 rows).
3. **Keep distinct-content writes for trap members.** The reply carries counts, never a member list, because each list member becomes a row.
4. **Use two levers, one for the mean and one for the spread.** Near-certain misses lower the average but add no spread. Traps caught about half the time add spread. Douglas had both (26.4 % all-fail, 29.0 % mixed). Q4 had almost only the first (SD 0.016). Handover had only the second (80.8 %).
5. **Target about 45 % all-pass, 40 % mixed and 10–15 % near-certain miss.** SD tracks mixed weight: roughly 0.10 at 36 %, 0.13 at 43 %.
6. **Weight trap rows honestly and keep control rows light.** A value copied from one record is weight 1; only real joins are 5. Never raise a weight (learnings §48, §60).
7. **Every trap moves at least 2 rows, including a weight-5 row.** A one-row trap chains failure patterns (Bridge rev12 batch 1).
8. **Spread traps across different habits.** Traps found by the same thorough search act as one trap (Bridge batch 1: 80 % concentration). One missed record can fail a whole cluster (Robert LLC: 14 rows).
9. **Rate judgement traps low.** Julia's never landed. Carriers discriminate, so a trap that needs only a join gets a low landing rate in the model.
10. **A rule doc stays plain definitions.** Naming sources sent Opus straight to the answers on Samuel's and Robert's tasks.
11. **Keep a task keyword out of hidden corrections.** A plain search for the task's own word found them on Robert LLC, and on Bridge a pointer's word led to the correction.
12. **All-fail rows are legal when VALID, and need justification.** Budget for them at `/create-allfail`.
13. **At `/rubric`, apply the Fix List word for word.** Check count-plus-identity, two artifacts in a title, cross-service order rows, and names only in the evidence before the first run. Diff the builder export field by field before the verifier (R14/R15 flipped Bridge's SD; R101 drifted on Robert LLC).
14. **At `/oe`, never put a value seen only in run output on an Expected line.** Search terms come from the prompt or an earlier event, and Gmail attachments return no bytes.
15. **A rebuild is not the only answer to a failed batch.** Bridge rev12 failed patterns on batch 1 and passed every gate on batch 2 with the same SQL.

## Originality

Do not copy a cohort, rule vocabulary, record set, prompt, Oracle Event or criterion from these tasks (`completed_tasks/README.md`). This design shares no cohort with them. Its nearest neighbours in shape are Robert's two Linear close-outs, and the job here (a bug list moved out of Slack) is different. STEP 0.6 cannot be measured locally.
