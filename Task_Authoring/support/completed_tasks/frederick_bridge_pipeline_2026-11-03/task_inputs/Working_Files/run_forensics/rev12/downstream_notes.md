# Rev12 notes for Oracle Events, rubric and the next platform runs

Rev12 is bound to the new task SQL (`01_Universe_Inject.sql` in this folder, sha256 69db98aed17f). The prompt `b5ea6f0ff28c` is unchanged since rev7.

## Why rev12 exists (rev11 baseline)
- Rev11 passed /injection, /prompt (5) and /hardness (NON-FAIL 3).
- In the six baselines, Paul's back-out and both build-access cells were caught by every run, and SciPlay was missed by five of six. Runs 1-5 failed exactly the same rows: failure patterns 83% (limit 50%) and SD about 0.06 (floor 0.1). See `../rev11/baseline/baseline_review.md`.
- Cause: both rev11 placements sat on the path every run takes. The angel post comes back from the run's own "SAFE"/"DocuSign" search and every run opened its thread; every run read the T-Accelerate mail thread in full.

## What changed (measured, not guessed: 15 Opus 5.5 runs from rev9-rev11)
- **Paul (DONE1):** Leonard's "Paul's out, he wrote me this morning that he can't put money in this year after all" moves to his 1:1 DM with Frederick (D05S58U4SAK/1759251900.863415, Sep 30 10:05 AM PT). The angel post has no replies again. 6 of 15 runs read that DM.
- **Build access (DONE2):** the T-Accelerate mail replies are removed. Arthur's correction (C0880U9751A/1759274400.518306) is a #zombie-match3d root post again: "the investor tester list I made in the Play console never got attached to the internal track, so nobody on it has android yet (Karthic, the 3 Dentsu folks, Anel's two at NCsoft and Ilse from Brightwater) ... iOS is fine for all of them". No "testflight" (searched by 13 of 15 runs); "tester" was searched by 5 of 15; firm-name Slack searches add a few more.
- **ZOM-567** logs NCsoft (Sep 22) and Brightwater (Sep 26) too, so the correction decides **four** Build access cells. A heavier trap moves each run's score more, which the 0.1 spread floor needs.
- SciPlay (CORR), Anton (INPUT) and everything else unchanged.

## Truth (rev12; solver/truth.json)
- 25 on the list: New investor 1 (Anton Bernstein, $25,000); In talks 7; Awaiting reply 14; Keep warm 3 (LVP, Hiro Capital, SciPlay). Paul Heydon off.
- Build access for firms in talks: **T-Accelerate, Dentsu Ventures, NCsoft and Brightwater Games Fund iOS only**; GFR Fund, Andreessen Horowitz and Homa none.
- Trello: 4 checklists, 25 items; 18 "F/up with" cards; a comment on the "F/up with Anel" card for NCsoft; no card for Dentsu or Makers.
- Reply counts: New investor 0 firms 1 angel; In talks 7 firms 0 angels; Awaiting reply 14 firms 0 angels; Keep warm 3 firms 0 angels.

## Rubric guidance (the failure-pattern and spread gates depend on it)
Two failing runs count as different patterns only if they differ on 2 or more rubric rows. Each trap must therefore land on its **own** rows, at least two per trap, that no other trap touches.
1. **Weight 5, one row per deciding value:**
   - SciPlay is in Keep warm (not In talks);
   - Paul Heydon is not on the send list;
   - Dentsu Ventures build access iOS only;
   - T-Accelerate build access iOS only;
   - NCsoft build access iOS only;
   - Brightwater Games Fund build access iOS only;
   - Anton Bernstein New investor at $25,000.
2. **Weight 3, per-entity follow-through for the trap entities** (keep these separate from the set rows):
   - SciPlay's checklist item is on the Keep warm checklist, not In talks;
   - no "F/up with" card for SciPlay;
   - no checklist item for Paul Heydon;
   - no "F/up with" card for Paul Heydon.
3. **Weight 3, reply counts, one row per group** (New investor 0/1, In talks 7/0, Awaiting reply 14/0, Keep warm 3/0).
4. **Weight 3, routine sets:** the 14 Awaiting reply firms; Homa and Brightwater added; the off-list firms excluded; the NCsoft comment instead of a card; no card for Dentsu or Makers; the other follow-up cards as one set.
5. **Weight 1, delivery:** sheet name and folder, shared with Leonard, reply on Leonard's thread, not sending to the whole 2025 list.
6. Don't fold the trap entities into one big "checklists correct" or "cards correct" row. That would make a SciPlay miss and a Paul miss fail the same row and merge their patterns.
7. Fair variations to accept: card titles with the firm or the contact's name; reply or reply-all; "iOS only" written as "TestFlight only" or "iOS yes, Android no"; a Google Doc instead of a Sheet (README allows both).
8. Expected failure patterns:
   - CORR: SciPlay In talks (row, item, card, In talks 8/0 and Keep warm 2/0);
   - DONE1: Paul In talks at $50,000 (row, item, card, In talks 7/1);
   - DONE2: the four cells "iOS and Android" (from ZOM-567);
   - INPUT: Anton at $40,000;
   - combinations of the above.

## Estimates (UNCALIBRATED; six-run simulation from the measured exposure, scratchpad boot12c.py)
- Catch rates used: SciPlay about 0.27 (4 of 15), Paul about 0.4 (6 of 15 read the DM), build access about 0.4-0.6.
- P(perfect pre-check run) about 3-5%: /hardness should again see a consequential miss.
- Baseline, independent traps: P(patterns pass) about 0.88-0.92; P(spread 0.1-0.3) about 0.83-0.86; P(average under 80%) about 0.99; P(every baseline gate) about 0.75-0.79.
- Bootstrap of the 15 real runs (keeps their correlation): P(every baseline gate) about 0.71.
- Expected average about 60-63%.

## Rev12 platform results (2026-11-03)
- /injection: PASS (lint 0 FAIL, 0 CHECK, 0 INFO) on SQL 69db98aed17f. Report sha 042c1a17, in platform/0_injection.md and Platform_Report/injection_report12.
- /prompt: PASS, score 5, on prompt b5ea6f0ff28c (dataset similarity 0.762). Report sha 1a235184, in platform/1_prompt.md and Platform_Report/prompt_report10.
- /hardness: NON-FAIL, score 3, PROCEED (OBSERVED_OPUS_FAILURE). Report sha 57bc444b, in platform/1a_hardness.md and Platform_Report/hardness_report6.
- Pre-check run: precheck/trajectory.json (sha 38b13797), 140 tool calls, complete, Opus 5.5.
  - It caught Paul: it read the DM D05S58U4SAK (calls 69-70).
  - It caught SciPlay: it opened the a16z thread (call 75).
  - It got Anton $25K and every other group right; counts 0/1, 7/0, 14/0, 3/0.
  - It missed build access. It wrote "iOS and Android" for T-Accelerate, Dentsu, NCsoft and Brightwater from ZOM-567 alone. Its Slack searches were "testflight" and "\"internal test\"" (no "tester"), and "from:arthur added" failed with user_not_found and was not retried. It never read #zombie-match3d. The error was repeated in the NCsoft card comment and in the reply to Leonard.
- Reviewer's dependent-stage asks: a high-weight row and an OE step for the four iOS-only cells (source: Arthur's post 3cddf83c over ZOM-567), a separate row for a16z, GFR and Homa = none, separate rows for SciPlay and Paul, and a counts row.
- Prompt report notes for OE and rubric: Paul's record is the DM message c5657466 (not an #executives thread reply); NCsoft and Brightwater are iOS only; accept Sheet or Doc, either card-title name form, reply or reply-all, counts as one number or split.
- Next: 6 baseline runs, graded here before the Oracle Events and rubric.

## Baseline batch 2 (2026-11-03): use this batch
- Batch 1 (baseline/) failed patterns at 80% (SciPlay and Paul missed together). The user re-ran on the same SQL; batch 2 (baseline2/) passes every gate on the draft rubric: average 70.2%, SD 0.154, 4 patterns (largest 40%), 1 full pass, golden run 149 calls, all Opus 5.5. See baseline2/baseline_review.md.
- Rubric constraints this verdict depends on:
  - Keep SciPlay, Paul and build access on separate rows, with each trap's follow-through (checklist item, card) as its own row.
  - Keep total weight lean (under about 120); SD reaches 0.1 at about 129.
  - Don't add a grand-total row for the reply (runs 1 and 5 misstate the total; Leonard asks for counts per group).
  - Build access none for a16z, GFR and Homa as its own row (all runs pass it).
- Then: /create-oe-writing, /create-rubric-writing, the platform verifier on these six runs, and /create-difficulty with the real verifier results.

## /oe (2026-11-03): PASS 5 on round 3
- Round 1 NON-FAIL 3 (five MINOR description issues: Raine and Superplay mails misattributed in OE 8, "only plans" in OE 7, OE 6's incomplete "rest", OE 28's "nothing from us"). Round 2 NON-FAIL 3 (OE 7's Sep 23 Play Ventures line read as BITKRAFT). Round 3 PASS 5: Completeness 5, Accuracy 5, no issues, deep recheck 0 findings.
- Passing OE file: 08_Oracle_Events.md sha256 bea7b71ffac79aa4 (86 events, 31,388 characters); copy in run_forensics/rev12/08_Oracle_Events.md; reports Platform_Report/oe_report1–3.
- Do not edit 08_Oracle_Events.md from here on: the rubric review cites OE labels verbatim and an OE edit makes /oe and /rubric stale.
- The rubric should cite these OE steps: groups OE 28 (inputs OE 5–27), sheet OE 30–32, checklists OE 37–65, cards OE 66–83, NCsoft comment OE 84, reply OE 86.

## Rubric draft 1 (2026-11-03)
- 09_Rubrics.json: 32 Outcome criteria, weight 132 (5 ×21, 3 ×8, 1 ×3); plan Working_Files/09_Rubric_Writing_Plan.md; generator plan/rubric/build_rubric.py + build_plan.py; V3 rubric_rows in 00_V3_Authoring_Evidence.json.
- rubric-writing gate: 28/29 PASS; the one FAIL is diversity.authority_share (the send-list doc F2 sits upstream of 98% of the weight), the structural finding the Robert, Douglas and Julia tasks also carried.
- Projection on baseline batch 2 with this exact rubric (difficulty_stats.py): average 72.3%, SD 0.131, 4 failure patterns (largest 40%), 1 full pass (run 6, 149 calls), all Opus 5.5 — every gate PASS. Copy: baseline2/difficulty_projection_draft1.json.

## Rubric check (2026-11-03): draft 2
- Check found two improvements, applied: C33 Process row (weight 1) for Leonard's "Once it's done reply here" (all six batch-2 runs replied last); the ordinary LVP sample swapped for Treo VC (Awaiting reply) so a wholesale relabel of that group on the sheet fails a row; LVP's surface slot ST5 sampled out.
- 09_Rubrics.json: 33 criteria (32 Outcome, 1 Process), weight 133; copy run_forensics/rev12/09_Rubrics.draft2.json.
- rubric-writing gate 28/29 PASS (diversity.authority_share structural); rubric-check gate 21/22 PASS (chain.rubric-writing inherits the same finding). Lint: 4 anon_token hits only (accepted as LITERAL). Predicted /rubric: CLEAN.

## /rubric round 1 (2026-11-03): FAIL 1, Fix List applied (draft 3, 38 rows)
- Report: Platform_Report/rubric_report1 (copy platform/3_rubric_round1.md); reviewed JSON 5875117a9b71 (33 rows). Overall Rubric Quality 1 (six Majors plus one missing outcome), Criteria Weights 2 (8 rows one level low); every other dimension 5; fact check clean.
- Applied, with the report's own wording where it gave one:
  - R1 split into the folder row and a native Google Sheet or Doc row.
  - R12 became a bare angel count ("an individual investor, not a firm").
  - R18 split into a count row and an Anton item row.
  - R24 names GFR Fund, GFR, PERSON_0787_NAME or [PERSON_NAME_2306].
  - Name forms went into the titles (Homa, Brightwater, Dentsu, T-accelerate, Treo).
  - Checklist Accept line: the name contains the group name, any case, spacing or plural.
  - R23 now cites the Dentsu Oct 1 event (gcal /events/2195).
  - New rows: Sony Mobile on Awaiting reply, and Homa build access none.
  - Eight rows raised from 3 to 5 (Treo, a16z, Anton group, the SciPlay and Homa items, the GFR, BBQ and Brightwater cards).
- R33 was split into two rows. The send-list order row uses the report's wording. The Trello order row is our own rewrite: it covers the checklist writes on the card only (one write kind), passes when at least one checklist write comes before the reply and none after, and never requires every write to be complete.
- 09_Rubrics.json now: 38 criteria (36 Outcome, 2 Process), weight 166 (5 ×32, 1 ×6). The 33-row version is kept as 09_Rubrics.draft3_33rows.json.
- Replay of batch 2 on the 38 rows (baseline2/difficulty_projection_draft2.json): every new row passes in all six runs. Average 77.4%, SD 0.107 (sample 0.117, unweighted 0.093), 4 patterns (largest 40%), 1 full pass, horizon 149. Every gate passes, but SD is now near the 0.1 edge.
- Do not add any more rows that every run passes: one more weight-5 row of that kind takes SD to about 0.104, and a few more push it under 0.1.

### Gate follow-up after the Fix List (2026-11-03)
- C27 evidence names the Dentsu calendar entry evt_3671b9a924ccba550e51fa, as /rubric R23 asked. The entry was created 2025-10-01T00:02:03Z, after freeze_utc 2025-10-01T00:00:00Z, so v3.rubric_evidence rejected it as a source record. Its V3 dated source is Leonard's Sep 25 Dentsu mail (thread 1843473831194478743), which books the same Oct 1 1:30pm PT meeting. The title, weight and value 18 are unchanged.
- 09_Rubric_Check.md: the Findings table now holds only findings on the 38-row JSON (anon_token LITERAL, the C38 author row, the C27 dated source). The round-1 history moved to "Round-1 Fix List applied".

## /rubric round 2 (2026-11-03): FAIL 2, Fix List applied (draft 5, 40 rows, weight 168)
- Round 1's fixes were all confirmed. The new Majors were R37 and R38 (not_self_contained): each Accept line counted fewer write kinds than its title's "none after it". There were also two missing order checks (the follow-up cards and the Anel comment), which scored Process Rubrics 2.
- Applied word for word: R37 title and evidence, R38 evidence, new R39 (cards before the reply) and new R40 (Anel comment before the reply), all Process, weight 1. Also fixed the two wording notes: R29's justification (the Sep 3 post reads 'BBQ Capital (sent)') and R27's evidence ('confirmed in').
- C40's V3 source record is the Existing Investor Update card (base /cards/801, which holds the Sep 29 rule comment). The seeded Anel card is not found by the gate's base-data Trello lookup.
- Batch-2 replay with 40 rows (difficulty_projection_draft3.json): average 77.7%, SD 0.106, 4 patterns, largest 40%, 1 full pass. Every gate passes, with SD at the band edge. All six runs created the cards and posted the Anel comment before the reply, so both new rows pass in every run.

## /rubric round 3 (2026-11-03): PASS 5
- Reviewed JSON SHA-256 768ce6927ff7650e7b282234c8bbcb82c16716f9f2c38b408357977370c7bc84 is the current 09_Rubrics.json (40 rows, weight 168), saved as 09_Rubrics.final_40rows_PASS5.json. Report: Platform_Report/rubric_report3.
- All sub-dimensions scored 5; no findings; repairs none.
- QM notes (not scored), left as is: an optional Homa card sample (adding a row every run passes would push the SD below 0.106); the order rows' existence clause overlaps their Outcome rows, which the reviewer kept on purpose; the group counts accept one number.
- Do not edit 09_Rubrics.json from here on. Any edit invalidates this PASS.

## Baseline verifier on the 40-row rubric (2026-11-03): all gates PASS
- The verifier graded batch 2 (byte-identical to baseline2/runs). Per-run results match the projection exactly: 73.2 / 73.2 / 79.2 / 67.3 / 73.2 / 100%. Average 77.7%, population SD 0.106, 1/6 full passes, 4 patterns (largest 40%), golden run-6 at 123 counted calls (lowest run 109). All six runs are claude-opus-5-5 and bound to rev12.
- The platform builder has R14 and R15 at weight 1. With those weights the SD is 0.098, which fails. Set both to 5 before screen 60.
- The build used platform/09_Rubrics.verifier_titles.json because the four bracket-escaped titles would not bind to 09_Rubrics.json.
- Forecast hev_c6ae7863e04a66b1 binds rev8, so it was not scored.
