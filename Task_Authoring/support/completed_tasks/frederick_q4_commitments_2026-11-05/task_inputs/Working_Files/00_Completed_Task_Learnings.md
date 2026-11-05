# Learnings from the three completed Frederick tasks, and how they bind this design

Written 2026-11-03, before /create-scenario. Sources:

- `Task_Authoring/support/completed_tasks/frederick_*/README.md`
- each task's `Working_Files/12_Difficulty_Stats.txt`, `12_difficulty_input.json` and `01a_Hardening_Report.md`
- the root `learnings` file §1–62
- the auto-memory notes on the bridge task

Every number below is measured on real Opus 5.5 runs, except where marked UNCALIBRATED.

## Requester targets for this task (stricter than the assignment)

| Target | Requester | Assignment / gate | Design target |
|---|---|---|---|
| Counted tool calls | **> 130 in every run** | Long Horizon ≥ 100 (golden run, else the average) | ≥ 150 necessary calls in a lean, correct run; ≥ 170 typical |
| Average weighted pass | **< 80 %** | Easy < 90 % | E[avg] ≤ 72 % (8 points under the requester line) |
| Spread / passes / patterns | all other gates | SD 0.10–0.30, < 5 full passes, ≥ 2 patterns (largest ≤ 50 %), ≤ 2 errored | P(all gates incl. < 80 %) ≥ 0.6 (UNCALIBRATED) |

## What the three tasks measured

| Task (mode) | Counted calls per run | Average | SD | Full passes | Patterns | What drove the calls | What decided the score |
|---|---|---|---|---|---|---|---|
| Card spend Q3 (medium) | 558, 560, 560, 554, 555, 573 | 78.3 % | **0.054 (spread too flat)** | 0/6 | — | 496 seeded per-period Sheets, each read on its own (`gdrive_read_file` × 505–630). No bulk read spans spreadsheets | Every per-record trap LEAKED: Opus scripted full reads. Only off-path items (a Webflow forward and a Murf email nobody opened) failed, so every run lost the same rows |
| Account handover (medium, Normal) | 68, 88, 86, 90, 88, 100 | 80.8 % | 0.161 | 1/6 | 4 | Normal horizon; one register | **Bimodal**: runs 4–6 found all Gmail partner notices (93–100 %), runs 1–3 missed them (60–72 %). A deactivation mail found only by a publisher-id search: missed 5/6. Arthur's email outside the money date window: missed 2/6. Rules on tabs, listed sheets and the DM every run reads all LEAKED 6/6 |
| Bridge send list (medium) | 140, 150, 126, 141, 109, 123 (golden 123) | 77.7 % | 0.106 (0.006 over the floor) | 1/6 | 4 (largest 40 %) | 25 Trello checklist items + 18 cards + 1 comment, one write per entry. Before that write lever: 60–83 calls | Three traps landed about 3/6 each: Paul's back-out in Leonard's DM, SciPlay's pass in an #executives thread reply under an unrelated post, and build access in Arthur's later #zombie-match3d post. Calendar-only firms (Homa, Brightwater) were caught by every run |

## Rules this design takes from them

1. **Horizon (requester > 130 in every run).**
   - Opus bulk-reads mail (`gmail_get_messages_batch`), whole channels and one calendar listing; reads alone stall near 60–90 calls (bridge rev8, handover).
   - Two levers proved real, with no padding:
     - per-entry single-object writes with no batch form (bridge: about 44 writes took every run to 109–150);
     - per-record native documents that each need their own read (card spend: about 560 calls).
   - This design uses both, sized so a lean correct run clears 150. That means ≥ 30 cohort members, each with:
     - its own paper (a native Doc in Drive: order form, proposal or terms), which must be read for its terms;
     - ≥ 2 writes of its own (a contact, plus a reply, reminder or routing card).
   - Every read and write is asked for by an incorporated record and changes the result (no filler, Reaching the
     Tool-Call Minimum 2026-10).
2. **Per-record surfaces buy calls, never difficulty** (card spend: every per-record trap leaked). Paper-level terms are
   read by every run, so a clause on the member's own paper is a control or a horizon surface, never a landing trap.
3. **What landed sits off the swept path, and stays findable by an ordinary search:**
   - a 1:1 DM about one item (bridge Paul, ~3/6);
   - a thread reply under an unrelated #executives root (bridge SciPlay, 2/8 then 3/6);
   - a later post in another channel where that person naturally posts (bridge build access, 0/7 then 3/6);
   - mail a money or keyword search won't return (handover deactivation, 5/6 missed);
   - mail outside the date window the run searches (handover Arthur 569, 2/6).
4. **What leaked:**
   - rules in the hub or a doc every run reads;
   - a correction in the same thread or channel as the original;
   - calendar-only members (the calendar listing is read whole by every run);
   - tabs every run lists;
   - "visible caveats" ("still sitting with you");
   - a correction worded with the pointer's keywords ("tester" led to a "tester" search).
5. **Spread (the Easy-mode binding gate).**
   - Card spend failed SD with 0/6 full passes because all runs missed the same off-path items. The bridge passed SD by
     only 0.006, and every all-pass row lowers SD.
   - So:
     - ≥ 5 independent landing channels, each ~35–60 %;
     - **each moving ≥ 2 weight-5 rows**, because a 1-row trap chains patterns (bridge rev12 batch 1);
     - found by **different behaviours**, because traps found by the same thorough-search habit act as one trap;
     - always-pass weight kept to about one third of the rubric.
   - Never fix spread by re-weighting rows.
6. **Correlation check.** Bridge rev12 batch 1 failed patterns at 80 % because SciPlay and Paul were both caught by the
   same thorough name-search run. Each channel here is discovered by a different behaviour: DM read, thread open under an
   unrelated root, a later channel post, a search outside the date window, a rule-exception join.
7. **UGT and coherence:**
   - every decision settled by a dated, persona-visible record;
   - both blind sweeps (forks, then seeded-vs-base coherence) before `/prompt`;
   - census every seeded entity across the whole universe;
   - seed money states only on companies with no base footprint;
   - never grade known-data-issue cards (SC-39 Singular plan, SC-49 founder status, SC-7 channel membership, SC-54 pay).
8. **Writes:**
   - make Frederick the owner of the Drive / Sheets targets (in both rows);
   - reply on the counterparty's own thread;
   - one Process order row per write kind;
   - prefer positive rules ("note it on the existing card") over "skip" rules;
   - grade exclusions as an exact count or scope on a required write, never as a do-nothing row.
9. **Rubric (bridge /rubric FAIL 1, FAIL 2, then PASS 5):**
   - cross-service joins weigh 5;
   - never bundle a count with an identity;
   - every accepted name form goes in the title;
   - every count population gets a named member row;
   - diff the builder export field by field before the verifier.
10. **Originality.** STEP 0.6 fails a meaning score ≥ 0.80. This job (commercial offers waiting on HG, decided under
    the founders' runway rule, each answered and routed) shares no cohort or job with the three tasks or the library's
    board pre-read and investor-list tasks.
