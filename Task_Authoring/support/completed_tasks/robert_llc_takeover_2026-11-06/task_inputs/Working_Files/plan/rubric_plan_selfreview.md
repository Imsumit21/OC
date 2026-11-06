## Self-review

**1. Re-read as /rubric** (3_Rubrics_Eval.md 1.4 and 3.1, in order, against this plan).
- Every prompt requirement has a row on its own artifact:
  - the calls: one comment row per issue (P6–P9, P11, P69, P70, P101–P130) plus the cost in the comment on every priced item (P131–P138); one state row per issue (P12–P33, P141–P162); the VO issue P1–P4 and the new-issue count P171; sheet decisions P37–P44;
  - the sheet's item count and owners: P68, P72, P73;
  - the costs and steps: P45–P57, P66, P67, P76;
  - the shares: P58–P60;
  - the reply: P61–P64, P71;
  - the order: P65.
- **Check-mode revision 1 (2026-11-06).** A blind /rubric-style reviewer and the check found:
  - coverage gaps: no sheet item count, the Owner column, and the ENG-2439 and ENG-2440 comments;
  - acceptance problems: the P58 shares, the P10 vendor comment, P52 Metabase + dbt bundled, P5 without a call, the HG labels too narrow, and P36 with founder rows labelled LLC;
  - a reply-thread cascade;
  - six samples in the comments group;
  - five weights one level off.
  The plan now carries P68–P73 and P76, drops P10, and re-weights P28, P39, P40, P45, P48, P49, P62 and P63. The told-fact reply rows take their own fact ids (dd_reply, zm_reply), so each game call is graded once per surface the prompt asks for (comment, sheet, reply).
- Every write OE maps to a direct row or a cohort control (§B).
- The told facts ("what I'd do", "what it costs each of us a month", "the link to the sheet") each have a row.
- There are no exclusion rows. One-offs are graded as a value on a required row (P10, P55), not as a leave-alone.
- Friction: none.

**2. Counter-readings per row.**
- (a) Can a valid answer fail a title naming exactly these values?
- (b) Can a wrong answer pass?
- Each is resolved with a record, a rule § or a risk number.

@@TABLE@@

**3. Re-verify.**
- Every value in §A was re-verified in this run through tools/hg.py: plan/oe_reads.py re-read the 25 Slack posts, the 194 REVENUE_DAILY rows (/tables/12/rows/2040–2233), the Drive root /drive_files/14368, contacts /contacts/169 and /168, and Linear /users/13, /35, /26. The result is identical to the read behind the /oe-passed OEs.
- Seeded values were read from 01_Universe_Inject.sql statements (L45, L48, L51, L54, L56, L68, L80, L92, L100, L140–L289), never executed.
- Recomputed: 183.11, 0.00 and 7.36 over 62 rows each; 140 + 62 + 3,000 + 100 + 100 + 48 = 3,450; 3,450 / 3 = 1,150; 1,150 − 248 = 902; LLC 7, Founder 3, HG 28 (solver/truth.json).

**4. Predicted all-fail re-check.**
- Every row's deciding records are visible to Robert. Proof: the check-sql YES LB lines and the can-see lines pasted in §E, re-run by the gate (reach.plan_fids).
- Every write is cataloged: linear_create_issue, linear_create_comment, linear_update_issue, gsheets_create_spreadsheet, gsheets_values_update, gdrive_share_file, slack_send_message (with thread_ts).
- There is no forced error and no rate-1.0 retry.
- No row needs evidence outside the persona's view, or the content of a Gmail/Slack attachment.
- Count on the four bases (target_data_absent, required_tool_absent, filter_impossible, entity_unreachable): 0. The six baselines passed every row type at least once: b3 passed the VO rows, b3/b6 Feb 28, b3 the layer.ai step (BASELINE_DECODE.md).

**5. Draft grounding.** Prep mode: no criterion text is drafted here.

**6. Shortcut and diversity.**
- §F holds the probe output (33 values, 4 populations, k 3, all services and the SQL overlay). It reports one HIT: Leonard's draft sheet holds the three column headers.
  - **Strongest case it collapses the task:** a run could copy the layout from it.
  - **Resolution:** the layout is what the prompt asks the agent to copy, and the draft's numbers are the stale values (T3, T5, T6), so it answers only P35.
  - An earlier run with 46 values (generic tokens such as LLC, Todo and user ids, plus the superseded $95 and ~300) gave 30 noise hits. Those literals were removed: superseded values are not acceptance values.
- The largest unit of discovery is recomputed by the gate (diversity.authority_share). The traps land on separate rows (§E), so failing runs differ on two or more rows. In the six baselines, the VO miss, ENG-2462 Done or Mar 1, and the b5 DD/$95 errors fall on different rows.

**6a. Unit-of-discovery origins (changed in this pass, ledger re-gated).**
- **F2, the LLC take-over project.** Its origin now leads with `prompt`, because the prompt names it: "Go through the LLC project in Linear".
- **F3, the ground-rules doc.** Its origin now leads with `prompt ("make the call on every item the way he lays it out")`, because the DM the prompt hands over names it: "the ground rules doc has how we decide".
  - **Strongest counter-reading:** the doc is found one hop away, through the DM, so it is a discovered unit, and the honest share is 54% after trimming over-citations in P5, P48 and P65.
  - **Resolution:** the prompt directs the agent to Leonard's laid-out method, the DM names the doc that holds it, and all six baselines opened it (BASELINE_DECODE.md). So it is handed over in substance.
  - The next unit, the card (F4), decides 34%.
- 08_OE_Writing_Ledger.md was re-gated (oe-writing PASS) and 08_OE_Check.md re-pasted (oe-check PASS) after the edit.

**7. Surface dispositions.**
- R2 (Arthur's $902 cash in the reply). The strongest case that it is core: the split mail says he "puts the difference in as cash". But brief §4b (risk 3) and /prompt accept the even third alone, so requiring $902 would be overly_specific. The wrong value (his $248 paid on top) is still rejected by P64. Holds.
- R6 (support build in the reply). The strongest case that it is core: §4b lists it under "what Robert would do". But "what I'd do" (prompt) asks for the calls, and the step is graded on the sheet (P47) and the issue state (P22). A concise valid reply without it must pass the final-reply test. Holds.

**7a. /rubric round 1 (FAIL 1, reviewed 8296aaf8dc71).** The Fix List was applied exactly:
- **Deleted:** P5, P27, P36, P49, P76 and P71.
- **Retitled or re-weighted:** 19 rows, using its exact titles.
- **Added:** its 63 rows (P101–P138, P141–P162, P171–P173).
- **Wording repairs:** done.
Its checks: 82 of its titles are in the JSON verbatim with their weights; the other 43 reviewed rows are byte-identical, so DELTA locks hold.

**8. Weights.** Weights are set by the kind of work, using the Q4 /rubric round-1 calibration:
- **5:** a superseding or joined record ($140, $62, $248 vs ~300, the VO line, the take test, App Review over "done", layer.ai's thread, the full-audit counts and the shares).
- **3:** one rule applied to one item.
- **1:** a value copied off one record.
No weight was raised to move the average.

Unresolved: none. Open items for the draft:
- The draft writes the V3 rubric_rows evidence (00_V3_Authoring_Evidence.json), with dates acceptance for P47, P48 and P57.
- The rubric-writing gate's v3.rubric_evidence passes only once 09_Rubrics.json exists.
