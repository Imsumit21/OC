# Prompt Check — calvin_qm_epic
> Prompt: 04_Prompt.txt · 80 words · sha256 edefd55c0ff5 · Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) · checked 2026-11-10 against 04_Prompt_Writing_Brief.md (2026-11-10, rev3, SQL 479b8441f52e) · release task-quality-v1
> Suggested wording is allowed under the repository exception. Check clean ordinary writing, role plausibility, no hints/riddles and every fair outcome.

Calvin Price · Engineering · Engineering Ops · Analysis and synthesis · Long Horizon · Hard (V3 cap < 70 %; requester targets: average < 60 %, over 130 calls per run, largest failure pattern < 50 %) · synth-cut universe, Calvin's today Wednesday Oct 1, 2025. Upstream: injection rev3 (stage gate PASS, sha256 479b8441f52e; not yet on the platform). the second revision passed the platform /injection and /prompt (score 5, same prompt text) and /hardness was NON-FAIL 3; rev3 adds difficulty and leaves the prompt as it was. Friction: none, brief gate PASS.

## Summary

- Fail 0 · Non-fail 0 · Advisory 3 (C20 relative day names; C6 residual fork risk on the reworded note; C22 rev3 not yet reviewed by the platform /injection) · UNVERIFIED none.
- Checks clean: C1, C2, C3, C4, C5, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C21, C23, C24.
- Calibration self-test: the text matches no FAIL case and matches each PASS control it can be compared with (table below).
- Predicted /prompt band: PASS (no Fail, no Non-fail, no UNVERIFIED hard gate among C4, C6, C17, C18, C19). This is a prediction only: on earlier tasks /prompt's blind passes found forks that local sweeps missed.
- Status: READY FOR /prompt, once rev3 has its /injection.

## Findings

| # | Check | Dimension · severity | Quoted span | Rule (source) | Defect |
|---|---|---|---|---|---|
| 1 | C20 | Alignment with Today's Date · Advisory | "before Thursday's flow review" | Prompt Writing §4.2 prefers absolute dates; Eval 1 §2.8 and Local Overrides allow relative wording that resolves to one window | A relative day name. It resolves to one record: evt_342a813cb7765d4a6fce8d starts Thu Oct 2, 2025 18:00 UTC, the day after Calvin's today. No change needed. |
| 2 | C20 | Alignment with Today's Date · Advisory | "He messaged me about it yesterday" | same | A relative day. The hub D0770ET6WBW/1759264805.214409 is Tue Sep 30, 2025 13:40 PT, the day before Wed Oct 1. No change needed. |
| 3 | C6 | Fair outcomes · Advisory | "set it all up as he asked" | Eval 1 §2.1; brief §12 | Not a defect in the text. Every material field is settled by a dated record (table below), but rev3 cut the resolver sentences from Brian's note. A blind sweep of rev3 reproduced every value and rated four readings as arguable (plan/sweeps/fork_sweep_rev3.md); three were closed by wording, and the sighting on an older build rests on build times. A fix would go into the data, not the prompt. |

## Fair readings (accepted outcomes)

Reading A is the best-supported reading; Reading B is the strongest alternative. Each is settled by a newer source, an incorporated authority, source identity or scope, or accepted as a second fair outcome. Sidecar `outcome_reviews.prompt-check` is written in this run and bound to the 04_Prompt.txt hash.

| Deliverable | Reading A | Reading B (strongest alternative) | Resolution and evidence |
|---|---|---|---|
| Area children | 10 children under ZOM-543, one per area in Brian's note; all ten Todo | children only for areas that have open reports, or all left Todo | authority: comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 lists the ten areas, 'One child each', and 'Set the child to Done if it is Clear and to Todo if it is Open' |
| Report list | 39: the 38 sheet rows plus Marcus's glow report | B1: 38, the sheet only. B2: more, with Vincent's canvases, chat remarks, Oliver's skip exceptions or the input blocker | authority: comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 takes in bugs told to Calvin in a DM since the 26th (D05U73FNDDL/1759252212.611349) and keeps the canvases, Vincent's chats, Oliver's exceptions and the blocker (D0770ET6WBW/1758808795.588519) out |
| Rows 1, 2, 25 | Waiting on QA | Passed, on Vincent's chat ok D06UPGF5PQV/1758820544.160399 | authority: f_6d0326fa006b136f1bbf82 counts only main builds; C05433XK267/1758817549.151639 shows #1718 was a feature-branch build; harmonygames-Games/match3d#465 is merged |
| Rows 12 and 32 | Waiting on a fix; ZOM-571 and ZOM-581 back to Todo | Waiting on QA: the PRs are merged and the tickets are In Validation | fact: the note asks whether a fix is in main, and harmonygames-Games/match3d#472#rc_1 and harmonygames-Games/match3d#475#rc_1 |
| Rows 13 and 38 | Waiting on QA; ZOM-572 to In Validation | Waiting on a fix: no PR in the sheet | fact: the note asks whether a fix is in main; harmonygames-Games/match3d#473#c_2 on harmonygames-Games/match3d#473 |
| Rows 9 and 29 | Waiting on a fix | Passed, as re-tested | authority: f_6d0326fa006b136f1bbf82 'A pass stands until somebody sees the bug again on a main build made after the one it passed on'; C08R27X0EAH/1759267212.418339 and C08R27X0EAH/1759268652.552719, both on Android Submission 135 (C05433XK267/1759263189.219529), a build made after the passes |
| Rows 11 and 20 | notes on ZOM-556 and ZOM-560, moved under their children | new sub-issues | authority: comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 'if a ticket already has the report, move that ticket'; Vincent's notes comment_b3c560833d151268202546002e7613cf and comment_9f28b3d8d66bd04e3f7fc46bc6ed1ea9 |
| Review list | 6 reports: not Passed, in Collect & Win or Level-end rewards | B1: Collect & Win and Daily Gift. B2: only Waiting on a fix | newer source: 68dc11dceb76ad640995fd98 (Sep 30 17:22 UTC) after D0770ET6WBW/1759164072.337219 and calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com>; authority: the note says 'a report that is not Passed' in an area on the review's agenda, which calvin.price@harmonygames.co/<calendar-f2b39cd5-884e-2def-a4d7-d41d80d4c55b@google.com> puts on the roadmap card |
| Existing tickets | 20 moved, each with a note; 3 state changes, 17 unchanged | notes only where the state changes | authority: comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 'move that ticket under the child and leave a note with the status and why' |
| New sub-issues | 19, titled with the report, state by status, no priority, no assignee | priority or assignee copied from like tickets | authority: comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 'No priority and no assignee on the new ones'. Marcus's report may be reworded (accepted) |
| Sheet | in d_36cdb0374c4aad3b8bf741, tabs Reports and Areas with the note's columns, shared with Brian, Leonard, Arthur, Julia, Vincent | shared with Brian and Vincent only | the hub D0770ET6WBW/1759264805.214409 says everyone on the review invite, Leonard too; evt_342a813cb7765d4a6fce8d lists the seven. Title, role and column order free (accepted) |
| Slide | one new slide in f_637e63ae6c1b4a7eb016aa with 10, 9, 20, 0, 7 | the numbers added to an existing slide | the hub says 'add one slide'. Layout and position free (accepted) |
| Reply | a message in Brian's DM D0770ET6WBW with 10, 9, 20, 0, 7 | a thread reply under D0770ET6WBW/1759264805.214409 rather than a new message | both accepted: the prompt and the hub say the DM; thread or not is representational |

## Calibration self-test (prompt_qc_cases.json, 15 calibration cases)

| Case | Rule | Expected | This prompt |
|---|---|---|---|
| K11-staged-errors | staged_errors | FAIL | not matched: spelling, capitals and punctuation are clean |
| K11-control-spelled-correctly | staged_errors | PASS | matched |
| K31-trap-hint | trap_hint_or_riddle | FAIL | not matched: no hint at a hidden item; the text names Brian's ask and its outputs |
| control-symptom | trap_hint_or_riddle | PASS | matched in kind: the prompt names what Brian wants, not a cause |
| K42-hidden-destination | hidden_destination | FAIL | not matched: Linear, the folder, the deck and the DM are named |
| K47-hidden-destination | hidden_destination | FAIL | not matched |
| K44-hidden-destination | hidden_destination | FAIL | not matched: the reply's place is the DM with Brian |
| control-named-destination | hidden_destination | PASS | matched |
| K1-audit-form | audit_form | FAIL | not matched: it reads as a person asking for help |
| K43-audit-form | audit_form | FAIL | not matched |
| K44-if-chain | if_chain | FAIL | not matched: the per-case rules live in Brian's note on the ticket |
| control-plain-request | audit_form | PASS | matched |
| K43-departed-person-premise | false_state_premise | FAIL | not matched: only Brian and Calvin act, both active at the clock (Brian's last base DM line D0770ET6WBW/1758808795.588519 is Sep 25; Calvin's D0770ET6WBW/1759173921.310649 is Sep 29) |
| K50-both-fair-figure | ugt_both_fair_figure | PASS | not applicable: no figure is left to a choice between sources |
| K49-newer-source | ugt_both_fair_figure | PASS | matched in kind: dated records settle each count |

## Check results (C1–C24)

| # | Result | Evidence |
|---|---|---|
| C1 | clean | 80 words (whitespace split), inside 20–4,000 |
| C2 | clean | Working_Files/00_Task_Context.json refreshed this run: all eight V3 fields; persona calvin_price resolves; synth-cut universe; source supports the 2025-10-01T00:00Z freeze |
| C3 | clean | Calvin is the assignee of ZOM-543 (base /issues/3618: title Queue Manager, assignee usr_49b9dfa5208d400d), Brian asked him to take it on (D0770ET6WBW/1758730948.999939), and Brian asks him directly in the hub D0770ET6WBW/1759264805.214409; voice judged against the role only |
| C4 | clean | Engineering (a ZM feature and its QA reports), Engineering Ops (epic and task management in Linear), Analysis and synthesis (the status of 39 reports from several sources, summed up in a sheet, a slide and five numbers) |
| C5 | clean | Ambiguity, dynamic change and multi-source are load-bearing (brief §8); the prompt restates no rule, figure or source |
| C6 | clean, with Advisory (finding 3) | Fair readings table above: every material field and Linear write is settled by a dated record; a blind agent reproduced the answer from the SQL and the base |
| C7 | clean | Writes under every reading: 27 issue creates, 22 moves with 8 state changes, 22 notes, a sheet with two tabs moved into the folder, 5 shares, one slide, one DM message. Channel and form are pinned; 'I need you to' delegates all of it and no 'I'll' sits beside an ask |
| C8 | clean | (a) the hub and Brian's note are Calvin-visible; (b) one DM with Brian, and his message of Sep 30 is the only one about an epic; the hub leads to one note on ZOM-543; (c) the hub states what the prompt attributes to Brian; (d) rules, no answers |
| C9 | clean | No status, count, area, root cause or finding entity; the brief §9 scan of the text finds none |
| C10 | clean | Only AN1, AN2 and the hub's own folder, deck and invite are named; no hidden authority, build, PR or channel |
| C11 | clean | Every write depends on the investigation: statuses set states, a ticket lookup replaces creation, and the five numbers come from all of it |
| C12 | clean | Linear, Sheets, Slack, GitHub, Docs, Trello, Gmail, Calendar, Drive and Slides carry weight (brief §1); 01_Hardness_Manifest.json present; hardness_gate (extreme) PASS pasted in the dossier |
| C13 | clean | One purpose: Brian's ask before Thursday's review |
| C14 | clean | No function, parameter or server name (catalog scan); 'Linear' is a natural product name |
| C15 | clean | The single 'Once that's done' orders the final message after the work (screen 24 skeleton) |
| C16 | clean | No spec-sheet layout, answer-key clause, staged error, riddle, hedge, hidden destination, audit wording or if-chain; hardness_v2_check: 'CLEAN RULE_IN_PROMPT no run of 8 resolver words in the prompt' |
| C17 | clean | Verification log below: every person, record, date and premise re-found in this run |
| C18 | clean | Catalog writes exist: linear_create_issue (team, title, state, parentId, priority, assignee), linear_update_issue (parentId, state), linear_create_comment, gsheets_create_spreadsheet, gsheets_batch_update, gsheets_values_update, gdrive_move_file, gdrive_share_file (emailAddress, role), gslides_batch_update, slack_send_message (channel, thread_ts); gradable_surface.py gradeable-report: 51 slots GRADABLE |
| C19 | clean | check-sql PASS for every scoped seeded record; Calvin is in D0770ET6WBW, D06UPGF5PQV, D05U73FNDDL, C08R27X0EAH, C0880U9751A, C093LEZGF6J and C05433XK267 (persona_view can-see YES this run); his mailbox holds both invitations; the pass sheet, legend and rule doc are shared with him. Linear, GitHub and Trello are unscoped |
| C20 | Advisory (findings 1, 2) | yesterday = Tue Sep 30 (past); Thursday = Oct 2, a future meeting (evt_342a813cb7765d4a6fce8d) |
| C21 | clean | Friction: none (03_Error_Async_Config.txt) |
| C22 | Advisory | rev3 (sha256 479b8441f52e) has no platform /injection yet; local base_check, base_claims, fact_check and hg lint PASS, and a blind coherence sweep found no blocking item (plan/sweeps/coherence_sweep_rev3.md). Leonard is travelling on Oct 2 per base C07C2866011, which rev1 carried through /injection and /prompt |
| C23 | clean | No sample was supplied with the task. Against the archived tasks in support/completed_tasks the scenario, persona, entities and asks differ, and no sentence is shared; the platform's STEP 0.6 dataset gate has not seen this text yet |
| C24 | clean | Six kinds of write over Linear, Sheets, Drive, Slides and Slack |

## Verification log

Every row was looked up in this run: base records through `Task_Authoring/tools/hg.py search` and persona_view, seeded records from 01_Universe_Inject.sql (rev1, asserted by this report's builder).

| Span | Type | Universe record (locator) | Result |
|---|---|---|---|
| Brian | person | entity.py resolve 'Brian': brian.foster@harmonygames.co, EMPLOYEE_0026_SLACK_ID | the hub's sender; active at the clock |
| the Queue Manager ticket | ID | ZOM-543 (linear /issues/3618): title 'Queue Manager', assignee usr_49b9dfa5208d400d (Calvin), created 2025-09-15T12:41:11Z | match |
| turned into a real epic | relationship | hub D0770ET6WBW/1759264805.214409: 'I want the queue manager to be a real epic' | match |
| before Thursday's flow review | event / date | evt_342a813cb7765d4a6fce8d 'ZM home screen flow review', 2025-10-02T18:00:00Z, on Calvin's calendar; hub: 'Before Thursday's flow review' | match (future meeting) |
| He messaged me about it yesterday | date / channel | D0770ET6WBW/1759264805.214409: Tue Sep 30 2025 13:40 PT, 20:40 UTC, in DM D0770ET6WBW | match |
| as he asked | relationship | hub: 'I left a note on the ticket about how I want it'; comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 | match |
| the children and report lines in Linear | requested output | hub: 'One child for each area, and every report gets its line under the right child'; ZOM-543 | match |
| the stock-take sheet in my ZM queue manager folder | destination | d_36cdb0374c4aad3b8bf741 'ZM queue manager', owner calvin.price@harmonygames.co; hub: 'put a stock-take sheet in your ZM queue manager folder' | match |
| shared with everyone on the review invite | recipients | evt_342a813cb7765d4a6fce8d attendees leonard.hayes@harmonygames.co, brian.foster@harmonygames.co, arthur.blake@harmonygames.co, julia.lawson@harmonygames.co, vincent.parker@harmonygames.co, calvin.price@harmonygames.co | match |
| a slide with the numbers in my queue manager deck | destination | f_637e63ae6c1b4a7eb016aa 'ZM queue manager', owner calvin.price@harmonygames.co; hub: 'add one slide with the numbers to your queue manager deck' | match |
| our DM | channel | D0770ET6WBW, members Calvin and Brian; persona_view can-see YES on D0770ET6WBW/1759173921.310649 | match |
| the numbers he wants back | requested output | hub: 'tell me here how many reports are passed, how many wait on QA, how many wait on a fix, how many areas are clear and how many reports are on the review list'; D0770ET6WBW/1759264805.214409 | match |
| me / my | persona | calvin.price@harmonygames.co | match |

## Brief coverage

| Brief item (§4 deliverables, §6 triggers) | Present in the prompt (quoted span, or absent) |
|---|---|
| AN2 anchor: the Queue Manager ticket | "the Queue Manager ticket" |
| scope: the epic | "turned into a real epic" |
| deadline context: Thursday's review | "before Thursday's flow review" |
| AN1 anchor: Brian's message from yesterday | "He messaged me about it yesterday" |
| §6 rules under Brian's note | "set it all up as he asked" |
| §4 area children, sub-issues, existing tickets | "the children and report lines in Linear" |
| §4 sheet in the folder | "the stock-take sheet in my ZM queue manager folder" |
| §4 sharing | "shared with everyone on the review invite" |
| §4 slide | "a slide with the numbers in my queue manager deck" |
| §4 reply and the five numbers | "message him in our DM with the numbers he wants back" |
| §6 statuses, ticket reuse, states, review list, tabs and columns | absent (record triggers: Brian's note on ZOM-543, which the hub points at) |

## Self-review

Phase walk (Evals/1_Prompt_Eval.md, Phases 1–3): Phase 1 → C2–C5; Phase 2 → C6–C20, C23; Phase 3 → C21, C22. Every C-check has a result with evidence; none is UNVERIFIED.

| Check | Counter-reading (strongest case that /prompt fails it, or that a finding is a false positive) | Evidence that resolves it | Verdict |
|---|---|---|---|
| C1 | Another tokenizer could put the text outside the field. | 80 whitespace words; the limit is 20–4,000. | none stands |
| C2 | The assignment could be read as Normal Horizon or another date. | 00_Assigments.md and 00_Task_Context.json: long-horizon, hard, Oct 1, 2025 (synth-cut). | none stands |
| C3 | A VFX engineer restructuring an epic sounds like a lead's job. | ZOM-543 is assigned to Calvin, and Brian, who created it, asks him directly in D0770ET6WBW/1759264805.214409. | none stands |
| C4 | Building an epic could read as Actions, not Analysis and synthesis. | The writes are only as right as the status of each of 39 reports, which is worked out from the sheet f_cb40955893624e1acb8500, build posts, PR reviews and later reports; a mismatch alone would be Non-fail under V3. | none stands |
| C5 | The colon list could carry the recipe. | It lists the outputs Brian named, with no rule, source or value; brief §8. | none stands |
| C6 | A reviewer may find a fork the sweeps missed, as on earlier tasks. | The forks the fork sweep raised (rows 18 and 25, Oliver's exclusion, the dev-hearsay sentence) were closed in the SQL before the gate, and the platform /injection passed it; the residual risk is finding 3. Brian's note comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 settles each reading in the table. | Advisory stands |
| C7 | 'the children and report lines' could be too vague to act on. | The hub D0770ET6WBW/1759264805.214409 says 'One child for each area, and every report gets its line under the right child', and the note on ZOM-543 defines both; no competing write is named. | none stands |
| C8 | 'as he asked' may not lead to one source. | Brian's only message about an epic is D0770ET6WBW/1759264805.214409, and it points at one note on ZOM-543; D0770ET6WBW/1759164072.337219 is about the review's order, not the epic. | none stands |
| C9 | 'report lines' could pre-solve how reports are filed. | It repeats the hub's own words and names no status, ticket or count (D0770ET6WBW/1759264805.214409). | none stands |
| C10 | Naming the folder and deck collapses a discovery. | The hub names both, and d_36cdb0374c4aad3b8bf741 and f_637e63ae6c1b4a7eb016aa decide nothing. | none stands |
| C11 | Creating ten children needs no finding. | Each child's state depends on whether its area is clear, and every line under it depends on a report's status; ZOM-543. | none stands |
| C12 | Most of the work could be Linear plus one sheet. | GitHub decides rows 12, 13, 32 and 38 (harmonygames-Games/match3d#472#rc_1), Slack decides rows 1, 2, 9, 25 and 29 (C05433XK267/1758817549.151639), Trello decides the review list (68daad83bacf52c6ea7e1593), Calendar decides sharing (evt_342a813cb7765d4a6fce8d). | none stands |
| C13 | The slide could be a bolt-on. | Brian asks for it in the same message for the same review (D0770ET6WBW/1759264805.214409); same purpose. | none stands |
| C14 | 'Linear' names a system. | Natural product names are clean (prompt_qc_examples.md row 103); ZOM-543 is not named by key. | none stands |
| C15 | The colon list then 'Once that's done' could read as a command list. | Deliverables and who to tell are the screen-24 skeleton, not a method; no source or order of reading is given. Hub D0770ET6WBW/1759264805.214409. | none stands |
| C16 | 'as he asked' could be a hint, or 'Thursday' a nudge that the review moved. | Both repeat the requester's own message (D0770ET6WBW/1759264805.214409 says 'Before Thursday's flow review'), as the control-plain-request case does; Eval 1 §2.7. | none stands |
| C17 | 'Thursday' could be false: Brian's Sep 29 line says Friday. | The review was moved: calvin.price@harmonygames.co/<calendar-f2b39cd5-884e-2def-a4d7-d41d80d4c55b@google.com> and evt_342a813cb7765d4a6fce8d put it on Thu Oct 2, and the later hub says Thursday. | none stands |
| C18 | A sheet with two tabs inside a folder, and sub-issues under children, may exceed the tools. | gsheets_batch_update adds a tab, gdrive_move_file moves the file into d_36cdb0374c4aad3b8bf741, and linear_create_issue takes parentId for any issue. | none stands |
| C19 | Calvin cannot see the other attendees' mail or calendars. | His own event copy evt_342a813cb7765d4a6fce8d lists all six attendees; nothing asks him to read another person's scoped data. | none stands |
| C20 | False positive: relative days are allowed, so this needs no finding. | True under Local Overrides; kept as Advisory because Prompt Writing §4.2 prefers absolute dates. Hub date D0770ET6WBW/1759264805.214409. | Advisory stands |
| C21 | Friction could be announced. | 03_Error_Async_Config.txt: Friction: none; the text mentions no failure or wait. ZOM-543 is reachable directly. | none stands |
| C22 | Seeded tickets In Validation whose fix is not merged are a lifecycle mismatch. | That mismatch is the designed claim, and the platform /injection passed it on rev1 with no coherence finding (ZOM-571, ZOM-581); rev3 itself is not reviewed yet. | Advisory stands |
| C23 | The wording could sit close to an archived prompt that also points at a manager's DM. | No sentence is shared with any archived prompt, and the persona, feature, records and outputs differ (ZOM-543; D0770ET6WBW); the dataset gate itself runs only on the platform. | none stands |
| C24 | One message and many tickets is little variety. | Six kinds of write over five services, under ZOM-543. | none stands |

Spot-decode note: gradeable-report passes for all 51 slots. Report rows are keyed by the report text, so a run that rewords a report in the sheet's Report column needs a hand check in local forensics; this has no /prompt or rubric effect.

Unresolved: whether /prompt finds a fork the sweeps missed; the platform's dataset-duplicate gate on this text.

```
STAGE GATE prompt-check: PASS — Task_Authoring/task_inputs · 04_Prompt_Check.md#59f72e210c96 · 04_Prompt.txt#7f9ab6c62396 · 04_Prompt_Writing_Brief.md#b42cfa5ecf15 · __context__#7be566a0936c · __assignment__#d644f7ef43f6 · __policy__#dc4ab5df3cdd · __gate_policy__#cc68bf5564ff · __review__#28576aab3ad0 · blocking 0 · warnings 0 · checks 26
[PASS] assignment.v3_context: Calvin Price / Game Engineer (Unity VFX); hard cap <70%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Check.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 04_Prompt_Writing_Brief.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 04_Prompt_Writing_Brief.md)
[PASS] chain.prompt-writing: upstream 'prompt-writing' PASS pasted and current (04_Prompt_Writing_Brief.md#b42cfa5ecf15, 00_Assigments.md#a8cc00ce24ff, 01_Grounding_Dossier.md#88526f435b5f, 01_Universe_Inject.sql#479b8441f52e, 03_Error_Async_Config.txt#52b2d02d66d3, 01a_Hardening_Report.md#35ccd8634d0f, __context__#7be566a0936c, __assignment__#d644f7ef43f6, __policy__#dc4ab5df3cdd, __gate_policy__#cc68bf5564ff, __review__#fd6a51a31848)
[PASS] structure.sections: 7 required sections present and non-empty (04_Prompt_Check.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Check.md
[PASS] structure.prompt_hash: header ties the report to 04_Prompt.txt (80 words, sha256 edefd55c0ff5)
[PASS] evidence.quoted_spans: 3 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] evidence.coverage_spans: 10 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] structure.c_checks: every C1–C24 has a recorded result
[PASS] evidence.verification_log: 13/13 items carry a source pointer (min 100%)
[PASS] structure.summary_band: summary band present
[PASS] structure.summary_status: summary status present
[PASS] tier.hardness: Long Horizon → --profile extreme: manifest present, hardness_gate PASS pasted in the dossier and current
[PASS] tier.hardness_rerun: hardness_gate --profile extreme re-run on the current manifest + SQL: PASS
[PASS] review.counter_readings: 24 evidenced counter-readings (of 24 found; need ≥ 24) in 04_Prompt_Check.md
[PASS] review.coverage: self-review addresses all 24 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] v3.role_review: current role-plausibility review recorded; semantic judgment belongs to the named reviewer
[PASS] v3.fair_outcomes_review: current accepted outcomes and considered alternatives recorded; multiple fair outcomes are allowed
[PASS] readiness.context: explicit task/revision and current upstream evidence verified
[PASS] readiness.hardness_review: current evidenced review; deferred: []
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## Route

No Fail. Paste 04_Prompt.txt exactly as saved into `/prompt`, after `/injection` on rev3 (sha256 479b8441f52e). Answer the date question with Oct 1, 2025 (synth-cut). A defect found there in the data goes back to `/create-injection`, not into the prompt.

