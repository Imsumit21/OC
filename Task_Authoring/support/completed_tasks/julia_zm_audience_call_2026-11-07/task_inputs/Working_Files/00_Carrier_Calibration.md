# Carrier calibration: observed Opus 5.5 miss rates by hidden-evidence carrier

Status: COMPLETE. 5 tasks x 6 baseline runs = 30 runs, 393 rubric rows.
Sources: `support/completed_tasks/<task>/task_inputs/` (09_Rubrics.json, 10_Baseline_Verifier_Results.md via Working_Files/12_difficulty_input.json, 07_Baseline_Trajectories, 01_Universe_Inject.sql, 11_AF_Justification.md).
Per-run pass counts from 12_difficulty_input.json match the verifier headers in all 30 runs; rubric order matches in all 5 tasks.

## How to read the numbers
- Unit of the rate is the **record-run**: one deciding record in one run. A record that decides 14 rows still counts once per run, so row counts cannot inflate a rate.
- "Missed" = the run did not use the record. Each record was phrase-matched against tool results per run, then compared with its row verdicts.
- NS = never surfaced or only listed. SNA = text surfaced, run did not apply it. Where SNA is not given, all misses are NS.
- Row failures are in notes as failed row-runs / total row-runs.
- Task codes: D Douglas, H Frederick handover, C Frederick card spend, J Julia, B Robert.

## 1. Carrier table

carrier | tasks | rows | runs missed / runs total | miss rate | notes
--- | --- | --- | --- | --- | ---
github_inline_review_comment | D, J | 13 | 21 / 30 | 70% | 5 records. D 18/18, J 3/12: task effect is large. SNA 2 (D run 3). Rows 78/78 failed; J records have no row of their own
confluence_page_comment | D | 5 | 3 / 6 | 50% | 1 record only. Rows 12/30; run 2 passed 3 of 5 rows for a different reason
slack_channel_deep_page | B, H | 7 | 8 / 18 | 44% | 3 records: B Unity 5/6, B Feb 11 decision 3/6 (SNA 2), H #executives 0/6. Class is approximate, see section 5
gmail_reply_in_thread | D, B | 14 | 4 / 12 | 33% | D reply-all 4/6, B Sunset correction 0/6 (inferred from passes). 2 records only. Rows 56/84
gmail_separate_thread | C, H, J, B | 54 | 41 / 150 | 27% | 25 records, split sharply: 12 unpointed notices 41/72 (57%), 13 pointed or vendor-named 0/78. SNA 2
slack_channel_thread_reply | C, B, H | 9 | 4 / 18 | 22% | 3 records: C Sensor Tower 2/6, B Cursor 2/6, H adjoe 0/6. Rows 17/54
github_conversation_comment | B, D | 18 | 6 / 30 | 20% | All 6 are B CodeRabbit (unrelated repo). D's 4 PR comments on the cohort path 0/24
slack_dm_thread_reply | J, H | 14 | 4 / 24 | 17% | 4 records: J second-parent reply 3/6, J ask-thread reply 1/6, J group chat 0/6, H 0/6
linear_comment_on_noncohort_ticket | J | 2 | 1 / 12 | 8% | ZOM-281 1/6, ZOM-221 0/6. 2 records, one task
sheet_other_tab | H, C, B | 16+ | 2 / 30 | 7% | Both misses are H run 1, which used gdrive_read_file and never listed tabs
follow_through_write | all | 22 | 11 / 132 row-runs | 8% | Row-level, no record. 10 are B comments omitting "nothing due"; 1 is C double email. Pure writes 0
github_review_body | D | 8 | 0 / 12 | 0% | Approve state and timing on #41, #43
linear_comment_on_cohort_ticket | B, D, J | 78 | 0 / 150 | 0% | 25 records; 23 are B. Brute-forced by every run
trello_card_comment_or_checklist | D, H, C, J, B | 23 | 0 / 36 | 0% | 6 records in 5 tasks
gdoc_body | C, J, D, B | 5+ | 0 / 24 | 0% | 4 records; D and C partly inferred from passes
calendar_note | D, J, B | 10+ | 0 / 18 | 0% | B date also sat in Gmail; only 1/6 B runs opened gcal, so B is untested
timezone_or_date_rule | J, C | 4 | 0 / 12 | 0% | Pacific day 6/6, statement cycle cut 6/6
warehouse_row | H | 1 | 0 / 6 | 0% | 1 record; all 6 runs queried Snowflake
contacts_field | C | 1 | 0 / 6 | 0% | Untested: no contacts tool called in C; address found another way
(not in list) slack DM top-level message | C | 5 | 0 / 6 | 0% | Griffin's answer relayed by Leonard

## 2. Five highest-miss row families

1. **D inline comments on #38, #39, #46: 18/18, 13 rows at 0/6.** Runs read reviews and issue comments (14-25 calls each) but 5 of 6 never called the inline tool. Run 3 surfaced two and kept Y.
2. **B CodeRabbit bot comment, Combo-Fighters PR 38: 6/6, 5 rows at 0/6.** Unrelated repo. 5 runs made no GitHub call; run 3 made one code search.
3. **C Webflow and Murf notices: 12/12, 2 rows plus run-rate totals at 0/6.** Murf never surfaced; Webflow appeared in one listing, unopened. Prices fell back to the September charge.
4. **C WeWork, SavvyCal, Buttondown forwards: 15/18, 5 rows at 1/6.** Only run 6 opened them, through list_threads and get_thread. Runs 2 and 4 saw them listed and did not open them.
5. **B Unity note in #executives: 5/6, 5 rows at 1/6.** Top-level note in a channel the ask never named. Only run 5 reached it.

Next: H AdMob deactivation mail 4/6 (2 SNA, kept the row anyway) and D Arthur's reply-all 4/6 (see section 4).

## 3. Carriers effectively never missed (do not use these)

- linear_comment_on_cohort_ticket 0/150, trello 0/36, gdoc_body 0/24, calendar_note 0/18, github_review_body 0/12, timezone_or_date_rule 0/12.
- warehouse_row 0/6 and contacts_field 0/6 have one record each; contacts is untested rather than safe.
- Close to never: sheet_other_tab 2/30, with both misses from one run.
- gmail_separate_thread is safe only when pointed at: named sender, named vendor or a thread the ask cites gave 0/78.
- These zeros mostly sit on the path a run walks anyway. They show those placements do not discriminate, not that the carrier could never hide anything.

## 4. One hidden record changing a block

Weight share = share of task rubric weight in the record's own rows, before aggregate rows.

Record | own rows | outputs reached | aggregates also moved | rollout split | weight share
--- | --- | --- | --- | --- | ---
D Arthur's reply-all | 14 | register, DM, Linear state, Linear comment | R22, R23, R33, R43 (already 0/6) | runs 2, 5 opened the thread; 1, 3, 4, 6 read one message | 21.7%
D inline #38/#39/#46 | 13 | register, DM, Linear state, Linear comment | same 4 | no split, 0/6 | 20.1%
J second-parent DM reply | 4 | register, share role, Linear comments, DM | R5, R66 | runs 3, 5, 6 opened the second parent; 1, 2, 4 did not | 11.6%
J ask-thread DM reply | 7 | DM (register through R5, R6 aggregates) | R5, R6, R66, R67 | only run 1 missed; it read no DM thread | 8.7%
H three vendor notices | 6 | register, DM, Trello checklist | R23, R30, R31 at 3/6 | runs 4, 5, 6 got all; 1, 2, 3 each missed at least one | 23.5%
D Confluence reply | 5 | register, DM, Linear state, Linear comment | none unique | runs 1, 4, 5 read it; run 2 got N for another reason | 7.3%
B Unity note | 5 | register status, source, Linear state, Linear comment | R78 | only run 5 | 4.6%
B CodeRabbit | 5 | register status, source, Linear state, Linear comment | R78 | no split, 0/6 | 4.6%
B Cursor reply | 6 | register, Linear state, Linear comment | R78 | runs 4, 6 missed | 5.6%
C three forwards | 5 | run-rate tab, reply, Trello comment | R51, R62 at 1/6 | only run 6 | 10.3%

Observations:
- Blocks that split the runs are the ones that spread scores: D reply-all, J second parent, H notices. A block with no split moves the average and adds no spread.
- Exact-count and total rows compound. C R16/R28 stayed 0/6 although run 6 found three of the six vendor changes. D's four count rows failed 6/6, because no run had all records.
- J R5 passed in only 1 of 6 runs, though each single J record was missed in 1-3 runs: 5 separate failure routes (reply1, reply2, rc265, rc271, ZOM-281).
- Per-run outcome followed one search choice: which tool, which thread parent, or opening a listed mail. Fail patterns equal the surfaced pattern for every missed record, except the SNA cases and D run 2.

## 5. Caveats

Sample size
- 30 runs, but only 5 tasks. Most carriers rest on 1-5 records, several on one task. Record-runs within a record are not independent, so no confidence intervals are given.
- Single-record or single-task rates (confluence 3/6, reply-all 4/6, noncohort 1/12) are anecdotes with a number.
- Carrier averages hide task effects. Inline is 100% in D and 25% in J; conversation comment is 100% on one record and 0% on four. I did not establish why D and J differ.
- Placement looks at least as important as carrier type: whether the path points at the record. That is my reading, not a tested result; the pointed vs unpointed Gmail split was drawn after seeing the outcomes.
- Selection bias: these records survived hardening rounds that favoured misses, and D and J went through several rounds (J 7). Rates are likely high for a fresh design.

Conflicts with stated context
- **gcal 0/30 does not match the stored runs.** gcal_search_events appears once in 13 of 30 runs (D 6, J 6, B 1). Contacts only in one task does match (H 6/6). Please check what the earlier count measured.
- **J README "Pacific-time conversion landed 0/6" is stale.** It describes an earlier round. In the stored baseline R26 passes 6/6; only ZOM-200 is graded.
- J README names ZOM-281 and inline comments as discriminators; stored rates are 1/6 and 3/12. The channel_not_found error hit only runs 5 and 6, and both recovered next call. Runs 1, 2, 4 missed reply 2 by not opening the second parent.

Method limits
- Phrase matching sees only main-trajectory tool results. C and J used subagents and Bash on saved output, so some "never surfaced" could be read inside a subagent. Verdicts agree with exposure in every missed record.
- Zero-miss records are often inferred from 6/6 rows, not phrase-checked (C close notes, adjustments, feed notes; B Linear comments and receipts; D prod deploys doc). B's 23 Linear and 9 Gmail records were counted from rubric evidence fields.
- One primary carrier was assigned per row; many rows need a second source.
- Verifier passes can be right for the wrong reason: D run 2 R6 (self-approval reason). B R78 passed in run 2 while Unity and CodeRabbit failed; I did not inspect that set.

Could not classify, or classified loosely
- Aggregate rows, 17, excluded from carriers: D R22, 23, 33, 43; H R23, 30, 31; C R16, 28, 51, 62; J R5, 6, 66, 67; B R78, 135.
- B R36, R116 (each passed 4/6): two runs read Layer's in-app notice as vendor confirmation. Decoy judgement, not a carrier.
- B R135 (passed 2/6): extra decoy clashes. C R7 (passed 5/6): vendor volume in run 5.
- slack_channel_deep_page is loose. B Unity failed from an unread channel, not paging. B Feb 11 is the true depth case: run 2 read one page, and two more runs read it and did not call it a clash.
- H YouTube Removed users tab excluded: confounded with the YouTube notice in run 1.
- J rc265 and rc271 have no row of their own; misses were read from register contents in verifier notes.
- Remaining rows are direct lookups or guards with no hidden record. Rows passing 6/6: D 40, H 22, C 44, J 65, B 111 (282 of 393).
