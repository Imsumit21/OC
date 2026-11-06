# Prompt Check — robert_llc_takeover
> Prompt: 04_Prompt.txt · 130 words · sha256 ccd229a59a17 · Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) · checked 2026-11-05 against 04_Prompt_Writing_Brief.md (2026-11-05) · release task-quality-v1
> Suggested wording is allowed under the repository exception. Check clean ordinary writing, role plausibility, no hints/riddles and every fair outcome.

Robert · Executive · Finance · Planning and decision support · Long Horizon · Easy (V3 cap < 90 %, requester target < 85 % average) · normal universe, Robert's today Saturday Feb 14, 2026. Upstream: injection rev2 (01_Universe_Inject.sql sha256 edf1fd903611, platform /injection PASS twice), 03_Error_Async_Config.txt (Friction: none), no reference files. The text was read byte for byte; the 04_Prompt.txt hash was ccd229a59a17 before and after this run.

## Summary

- Fail 0 · Non-fail 0 · Advisory 2 (C20 relative day names; C23 STEP 0.6 neighbour risk, unmeasurable locally) · UNVERIFIED none.
- Checks clean: C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C21, C22, C24.
- Calibration self-test: the text matches no FAIL case and matches all five PASS controls/cases it can be compared with (table below).
- Predicted /prompt band: PASS (no Fail, no Non-fail, no UNVERIFIED hard gate among C4, C6, C17, C18, C19).
- Status: READY FOR /prompt.

## Findings

| # | Check | Dimension · severity | Quoted span | Rule (source) | Defect |
|---|---|---|---|---|---|
| 1 | C20 | Alignment with Today's Date · Advisory | "on Thursday night" … "before Monday's call" | Prompt Writing §4.2 prefers absolute dates; Eval 1 §2.8 allows relative wording that resolves to one window | Relative day names. Each resolves to one record: the hub D04UP2L3E3S/1770961200.890407 is Thu Feb 12 2026 21:40 PST, and Monday's call is evt_f5f279f282d20ec86bb8e5, Mon Feb 16 10:00–10:45 PT. Both fall on the right side of the clock (past fact, future meeting). No change suggested: Robert would not write the date of a message from two days earlier. If wanted: "on Thursday night (Feb 12)". |
| 2 | C23 | Originality · Advisory (no supplied sample) | "what it costs each of us a month" | Eval 1 §2.9; platform STEP 0.6 dataset duplicate (meaning ≥ 0.80 caps the score at 2) | Same persona and date as the completed robert_winddown_closeout (support/completed_tasks): per-issue Linear calls, a sheet shared with Leonard and Arthur, a reply in Leonard's thread with monthly money. The job differs: the founders' LLC take-over of Combo Fighter and how the three founders fund it, against an account close-out register. The prompt avoids that task's vocabulary ('register', 'close-out', 'accounts', 'settle', 'two monthly totals'), as planned in 00_Pre_Scenario_Analysis.md §5. hg_similarity.py is not in the local bundle, so the score can be read only on the platform. Precedent: frederick_q4_commitments kept a neighbour's hand-off skeleton with a different job and scored 0.658. |

No Fail or Non-fail finding. Clean spans are not quoted here.

## Fair readings (accepted outcomes)

Reading A is the best-supported reading; Reading B is the strongest alternative. Each is settled by a newer source, an incorporated authority, source identity or scope, or accepted as a second fair outcome (sidecar `outcome_reviews.prompt-check`, artifact hash 7b6f4963690a).

| Deliverable | Reading A | Reading B (strongest alternative) | Resolution and evidence |
|---|---|---|---|
| Plan sheet | A new Google Sheet in Robert's Drive root d_9f7ba94f7526d54d8482ba with the draft's eight columns (Item · Game · Decision · Monthly cost · Paid by · Next step · Owner · By), 38 rows (ENG-2438…ENG-2474 + the CF VO campaign) and the three shares per month; shared with leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co | B1: copy Leonard's draft f_d996e4c434ce160dc52596 into Robert's Drive and rewrite it. B2: edit the draft itself in place | B1 accepted: same location, columns, rows and readers, so the same material result. B2 rejected by source identity: the draft is Leonard's file (owner leonard.hayes@harmonygames.co) and the prompt and hub put the sheet in Robert's Drive ("keep it in your drive", D04UP2L3E3S/1770961200.890407). Title, column order, extra columns, the share role and one vs two Metabase/dbt rows are representational and all accepted (brief §4b). |
| Plan sheet figures | Costs at what each item bills now, by whoever runs it: DD prod 140, CF stacks 62, VO campaign 3,000, Metabase 100, dbt 100, GitHub 48; total 3,450, a third 1,150 | The draft's or #winddown's older figures (~$1k DD, ~$300 Metabase/dbt), or the campaign left off | Settled by newer sources under the ground rules' costing rule f_1e468a9d69ea0f0a2001f5: Arthur's DM reply D04V95AAAHW/1770952200.665739 ($140), his mail robert@harmonygames.co/1856975772058401508 ($248 carried), Leonard's #prototype status C09UHHN6PFZ/1770938400.370665 (campaign moves, $3,000 cap). Cheapest-reading test: copying the draft gives wrong rows and figures, so it is no shortcut. |
| Call on each issue | A comment with the call and reason on each of ENG-2438…ENG-2474, and the state from the project description (Todo + assignee / Done / Canceled) | The call in each description or as a label; or only the state | Settled by the incorporated project description of 0fa95761-d59b-4ff4-a8a3-15df3210ca6e ('Leave your call on each one as a comment and move it') and the prompt ("leave the call on each issue", "the project should match the sheet"). GitHub ENG-2447 group: Done or Canceled, both accepted (Arthur pays, the org stays HG's; robert@harmonygames.co/1856975772058401508). |
| Missing plan line | A new issue for the CF VO campaign in the LLC project | No new issue (the project 'already lists everything') | Rejected: the sheet carries the campaign row (C09UHHN6PFZ/1770938400.370665 says it moves to the LLC and to count it), and the prompt says the project should match the sheet. Any title naming the VO/Meta campaign and any team_ENG state are accepted. |
| Reply to Leonard | A thread reply under D04UP2L3E3S/1770961200.890407 with what Robert would do, what it costs each founder a month and the sheet's link | A new top-level message in D04UP2L3E3S | Settled by the prompt ("in that DM thread"). |
| Monthly cost each | $1,150 each (a third of $3,450) | Cash after carried costs: Leonard $1,150, Robert $1,150, Arthur $902 | Both accepted, and both together. The split email robert@harmonygames.co/1856989298688559716 states both: each 'carries a third', and what one already pays 'counts toward his third, and he puts the difference in as cash'. This is not a BOTH_FAIR_FIGURE fork (no source contradicts another; both numbers come from one rule). Writes, destinations and the next action are identical. |

## Calibration self-test (prompt_qc_cases.json, 15 calibration cases)

| Case | Rule | Expected | This prompt |
|---|---|---|---|
| K11-staged-errors | staged_errors | FAIL | not matched: spelling, capitals and punctuation are clean (only , . ? and ' appear) |
| K11-control-spelled-correctly | staged_errors | PASS | matched (clean, ordinary spelling) |
| K31-trap-hint | trap_hint_or_riddle | FAIL | not matched: no 'nagging feeling' or hint at a hidden item; the closing 'project should match the sheet' is a sync instruction (C16 below) |
| control-symptom | trap_hint_or_riddle | PASS | matched in kind: the prompt names the situation (Leonard's ask), not a cause |
| K42-hidden-destination | hidden_destination | FAIL | not matched: Drive, the LLC project and the DM thread are named |
| K47-hidden-destination | hidden_destination | FAIL | not matched |
| K44-hidden-destination | hidden_destination | FAIL | not matched: the reply's place is "in that DM thread" |
| control-named-destination | hidden_destination | PASS | matched |
| K1-audit-form | audit_form | FAIL | not matched: no reconcile / classify / complete-the-record wording |
| K43-audit-form | audit_form | FAIL | not matched |
| K44-if-chain | if_chain | FAIL | not matched: no if / but-not / then-also chain; the per-item rules live in the ground rules doc |
| control-plain-request | audit_form | PASS | matched: a plain ask pointing at the record that holds the rules |
| K43-departed-person-premise | false_state_premise | FAIL | not matched: only Leonard, Blake and Robert act, all active (C0ADGSZKR3R/1770842402.772039 'keep maybe the three of us') |
| K50-both-fair-figure | ugt_both_fair_figure | PASS | not applicable: no figure is left to the run's choice between sources |
| K49-newer-source | ugt_both_fair_figure | PASS | matched in kind: every figure fork is settled by a newer dated record, and the prompt adds no 'go with the most recent' line |

## Check results (C1–C24)

| # | Result | Evidence |
|---|---|---|
| C1 | clean | 130 words (whitespace split), inside 20–4,000 |
| C2 | clean | Working_Files/00_Task_Context.json: all eight V3 fields; persona robert resolves (roster persona_key robert); normal universe, source supports the 2026-02-14T00:00Z freeze |
| C3 | clean | Robert is a co-founder running the wind-down with Leonard and Arthur (C0ADGSZKR3R/1770839322.836779), Combo Fighter is his game (C07C2866011/1770084297.911029) and Leonard asks him directly (D04UP2L3E3S/1770961200.890407). Preparing a plan and recommending it before a joint founders' call is inside his remit. Voice: first person, plain, lower-key, judged against the role only (A-27) |
| C4 | clean | Executive: a founders' strategic call on carrying a game on through a new company (task_categories.md 'Founders / Exec / Strategy'). Finance: the three-month cost and each founder's share (split email robert@harmonygames.co/1856989298688559716). Planning and decision support: the per-item call and the recommendation. The authored artifact is the plan sheet |
| C5 | clean | Ambiguity, dynamic change and multi-source are all load-bearing (brief §8): the figures and population live across Linear notes, Slack, Gmail and Snowflake, and older figures are overturned later (F9, F11, F12, F14). The prompt restates no rule, figure or source beyond the two anchors |
| C6 | clean | Fair readings table above; every material field settled by a record or accepted; sidecar outcome review current (7b6f4963690a) |
| C7 | clean | No 'I'll / I need to / I'm going to [verb]'. 'I want my answer ready' assigns nothing to Robert. Writes under every reading: sheet create + values + share ×2, a comment + state ×37, one issue create, one thread reply. Channel, time and form are pinned for each deliverable: Drive, before Monday's call, a sheet; each issue, as a comment (project description); the DM thread. Open fields (title, share role, wording) are not channel, time or form |
| C8 | clean | (a) the hub D04UP2L3E3S/1770961200.890407 is Robert-visible (DM member EMPLOYEE_0016_SLACK_ID); (b) one thread, one draft 'LLC 90 days (draft)' f_d996e4c434ce160dc52596, one project 'LLC take-over'; (c) the hub states the three questions, the ground rules, the layout, the Drive, the sharing and the reply; (d) instructions, not answers (the draft's numbers are stale, not a key). Every brief §6 requirement has a trigger (prompt or record) |
| C9 | clean | No decision, figure, count, root cause or finding entity in the prompt; brief §9 scan: no term present except a single 'Then' (C15) |
| C10 | clean | Only AN1 (Leonard's DM) and AN2 (the LLC project in Linear) are named. 'his draft' and 'Monday's call' are loose references the hub itself makes, not exact titles or ids; no hidden authority, async target or §5 'No' item is named |
| C11 | clean | Every write depends on the investigation (brief §3): rows, decisions, costs, states, the new issue and the reply's figures |
| C12 | clean | Slack, Linear, Gmail, Drive/Sheets/Docs/Slides, Snowflake, Trello, GitHub, GCal and Confluence carry weight (brief §1). Tier: 01_Hardness_Manifest.json present; the dossier's 'HARDNESS GATE (extreme): PASS' is pasted and current (tier.hardness, re-run by the gate) |
| C13 | clean | Every ask serves one purpose, Leonard's ask before Monday's call: the per-item call, the sheet, the project matching it, the reply. Stacking, not bolt-ons |
| C14 | clean | No function, parameter or server name; 'in Linear', 'my Drive' and 'DM thread' are natural product names (prompt_qc_examples.md row 103). Catalog scan of tool names: none |
| C15 | clean | No sourcing script. The sentences give deliverables and who to tell; the single 'Then' orders the final reply after the work (the screen 24 skeleton), not a read order |
| C16 | clean | No spec-sheet layout, answer-key clause, staged error, riddle, hedge, hidden destination, audit wording or if-chain. hardness_v2_check: 'CLEAN RULE_IN_PROMPT no run of 8 resolver words in the prompt' |
| C17 | clean | Verification log below: every person, channel, doc, date, state premise and narrative claim found in this run; no near-match or phantom |
| C18 | clean | gsheets_create_spreadsheet (driveFileId optional), gsheets_values_update, gdrive_share_file (emailAddress, role), gdrive_move_file, linear_create_comment, linear_update_issue, linear_create_issue, slack_send_message (thread_ts) in Evals/references/tools/catalog.json; every fact has a cataloged read (brief §5a) |
| C19 | clean | Every scoped read is Robert's: DM member, his INBOX, his calendar, files shared with him (check-sql PASS in the dossier); Linear, Trello, GitHub, Snowflake and Confluence are unscoped; no ask reads someone else's scoped data |
| C20 | Advisory (finding 1) | Thursday night = Thu Feb 12 21:40 PT (past); Monday's call = Mon Feb 16 10:00 PT (future meeting); no post-clock event described as done |
| C21 | clean | Friction: none (03_Error_Async_Config.txt); nothing announced |
| C22 | clean | /injection PASS on rev2 reused (run_forensics/rev2/0_injection_PASS_r2.md); A-4/A-5/A-6, left for /prompt, are each settled by a later dated record (dossier, Platform review). Pre-existing cards touched: NB-31 (DM member lists, never graded), NB-29 (no window starts at the shutdown decision) |
| C23 | Advisory (finding 2) | No sample supplied with the task; guideline examples only. STEP 0.6 is read on the platform |
| C24 | clean | Four kinds of write over Sheets, Drive, Linear and Slack, far more than one investigate-and-post |

## Verification log

Every row was looked up in this run: base records through `Task_Authoring/tools/hg.py search` (outputs in Working_Files/plan/check/), seeded records from 01_Universe_Inject.sql through base_check.parse_sql.

| Span | Type | Universe record (locator) | Result |
|---|---|---|---|
| Leonard | person | slack users.json /23: EMPLOYEE_0038_SLACK_ID 'Leonard Hayes' leonard.hayes@harmonygames.co (hg.py get-many) | the hub's sender; unique Leonard (entity.py resolve) |
| a DM | channel | D04UP2L3E3S, channels.json /414: is_im true, members include EMPLOYEE_0016_SLACK_ID (Robert) and EMPLOYEE_0038_SLACK_ID (hg.py get) | match; the member list is never graded (NB-31) |
| on Thursday night | date | hub ts 1770961200.890407 = Thu Feb 12 2026 21:40 PST | match (Pacific; Fri 05:40 UTC) |
| setting up the LLC so we can keep Combo Fighter going | event | D04UP2L3E3S/1770961200.890407: 'if you really want to keep combo fighter going, let's set the LLC up properly' | match |
| after the shutdown | state | C0ADGSZKR3R/1770931777.561519 (Leonard: 'wind down agreement and data agreement reviewed and signed', hg.py get-many); the Feb 11 decision in #winddown C0ADGSZKR3R | match; wind-down acknowledged, no business as usual |
| Monday's call | event / date | evt_f5f279f282d20ec86bb8e5 'LLC: decide', 2026-02-16T18:00–18:45Z (Mon 10:00–10:45 PT), attendees leonard.hayes@harmonygames.co, robert@harmonygames.co, arthur.blake@harmonygames.co; hub 'we decide on Monday's call' | match (future meeting) |
| the LLC project in Linear | ID / project | 0fa95761-d59b-4ff4-a8a3-15df3210ca6e 'LLC take-over' (seeded); base linear data.json /projects: 0 matches for 'LLC', scan complete; positive control 'Zombie Match' → /projects/1 (hg.py search) | match; the only LLC project |
| the way he lays it out | relationship | hub: 'make the call on each one: what the LLC takes if Sunset can't sell it, what it costs us March through May, and who pays what. the ground rules doc has how we decide'; f_1e468a9d69ea0f0a2001f5 'LLC ground rules (Combo Fighter and whatever else we take)', owner leonard.hayes@harmonygames.co | match |
| he and Blake | person | Arthur Blake arthur.blake@harmonygames.co (entity.py resolve 'Blake': sole candidate); hub 'share it with Blake and me', 'so we can see it there' | match (the hub's own name for him) |
| my Drive | destination | Robert's root d_9f7ba94f7526d54d8482ba (entity.py resolve Robert: gdrive root_folders) | match |
| his draft | doc | f_d996e4c434ce160dc52596 'LLC 90 days (draft)', owner leonard.hayes@harmonygames.co, created 2026-02-10T18:30Z (Tue 10:30 PT); hub 'my draft from Tuesday' | match |
| share it with both of them | recipients | leonard.hayes@harmonygames.co, arthur.blake@harmonygames.co | match |
| the plan sheet | requested output | evt_f5f279f282d20ec86bb8e5 description 'Robert's plan sheet' | new output, not a premise |
| the project should match the sheet | requested output | project 0fa95761-d59b-4ff4-a8a3-15df3210ca6e, issues ENG-2438…ENG-2474 (seeded; no base project matches, hg.py search above) | new state, not a premise |
| reply to him in that DM thread | channel | thread_ts 1770961200.890407 in D04UP2L3E3S; hub 'then tell me here' | match |
| what it costs each of us a month | figure (requested) | split email robert@harmonygames.co/1856989298688559716 'LLC money', from leonard.hayes@harmonygames.co, Thu Feb 12 22:10 PT | the rule exists; the figure is a requested output |
| me / my | persona | robert@harmonygames.co (persona robert, Co-founder & Creative Director) | match |

## Brief coverage

| Brief item (§4 deliverables, §6 triggers) | Present in the prompt (quoted span, or absent) |
|---|---|
| AN1 anchor: Leonard's DM | "Leonard sent me a DM on Thursday night" |
| deadline: Monday's call | "I want my answer ready before Monday's call" |
| AN2 anchor and the per-item scope | "Go through the LLC project in Linear" |
| §6 decide each candidate under the ground rules (incorporated by the hub) | "make the call on every item the way he lays it out" |
| §4 call on each issue | "leave the call on each issue so he and Blake can see it there" |
| §4 plan sheet in Robert's Drive; §6 sheet layout | "Put the plan sheet in my Drive, laid out like his draft" |
| §4 sheet shared with Leonard and Arthur | "share it with both of them" |
| §4 missing plan line (new issue) | "the project should match the sheet" |
| §4 reply in Leonard's thread | "reply to him in that DM thread" |
| §4 reply contents; §6 the split | "what I'd do and what it costs each of us a month, with the link to the sheet" |
| §6 the take test from the warehouse | absent (record trigger: the ground rules name the daily revenue table) |
| §6 cost each item at what it bills now | absent (record trigger: the ground rules) |
| §6 owners and dates | absent (record trigger: the ground rules point at the LLC card) |

## Self-review

Phase walk (Evals/1_Prompt_Eval.md, Phases 1–3, read again for this run): Phase 1 assignment fit, persona, complexity and seeding → C2–C5; Phase 2 UGT/fair outcomes, feasibility A–E, truthfulness hard gates (phantom identifiers, state premises), tool use, clarity hard gates (delegation scan, write-action divergence), contrived indicators, today's date, originality → C6–C20, C23; Phase 3 injected friction and coherence → C21, C22. Every C-check has a result with evidence above; none is UNVERIFIED.

| Check | Counter-reading (strongest case that /prompt fails it, or that a finding is a false positive) | Evidence that resolves it | Verdict |
|---|---|---|---|
| C1 | A word count over a different tokenizer could fall outside the field. | 130 whitespace words; the field limit is 20–4,000 (Eval 1 field rule); the gate recomputes it (structure.prompt_hash). | none stands |
| C2 | The assignment could be read as Medium/Normal, changing the cap. | 00_Assigments.md and Working_Files/00_Task_Context.json: Long Horizon, Easy, Feb 14, 2026; error-async gate line 'easy cap <90%'. | none stands |
| C3 | A Creative Director costing an LLC could look like a CFO job, so role-implausible. | Leonard asks Robert himself (D04UP2L3E3S/1770961200.890407); Robert is a co-founder (roster; C0ADGSZKR3R/1770839322.836779) and the decision is the founders' (evt_f5f279f282d20ec86bb8e5 attendees). A better-fitting colleague alone is not a Fail (C3 rule). | none stands |
| C4 | Business Function could score 3 as 'Finance fits better', as on robert_winddown_closeout. | That task was account bookkeeping; this one is a strategic call on carrying a game on in a new company, with Finance as the assigned competency (task_categories.md 'Founders / Exec / Strategy'); under V3 a mismatch alone is Non-fail at most, and here none is shown. | none stands |
| C5 | 'the way he lays it out' could carry the recipe. | It points at the hub; the rules live in f_1e468a9d69ea0f0a2001f5, the split in robert@harmonygames.co/1856989298688559716 and the moving rule in Trello 698e6548aa9516b76c4ab475, none restated (brief §9 scan clean). | none stands |
| C6 | Reading B for the cost each (cash) could be rejected by a rubric that takes only $1,150. | Both are accepted in brief §4b and in the sidecar outcome review (7b6f4963690a); the split email states both. | none stands |
| C7 | 'leave the call on each issue' could mean a description edit vs a comment, two different writes. | The project description of 0fa95761-d59b-4ff4-a8a3-15df3210ca6e settles it ('as a comment and move it'); the state move is also required by 'the project should match the sheet'. No 'I'll [verb]' beside an agent imperative (Eval 1 §2.6 scan). | none stands |
| C8 | 'his draft' could be ambiguous (Leonard owns other drafts) or hand over an answer. | One Leonard draft about the LLC, f_d996e4c434ce160dc52596, created Tue Feb 10 as the hub says (brief §5a F5 'LLC 90 days', 1 seeded hit); its figures are stale (brief §5 F5), so it supplies a layout, not answers. | none stands |
| C9 | 'what it costs each of us a month' could presuppose that each founder pays the same. | It asks for each founder's figure without giving one; Arthur's differs as cash (split email robert@harmonygames.co/1856989298688559716). | none stands |
| C10 | Naming 'Monday's call' or 'his draft' could collapse discovery of a §5 'No' item. | Brief §5: F8 may be named as 'Monday's call'; the draft is named by the hub itself ('my draft from Tuesday') and is not a hidden authority; no exact title or id is given. | none stands |
| C11 | The writes might not depend on findings (copy the project into a sheet). | Decisions, costs and states turn on F9–F14 and F18 (brief §5); the new issue exists only if the campaign row is found (C09UHHN6PFZ/1770938400.370665). | none stands |
| C12 | The second service could be trivial (only Linear + Sheets). | Weight sits in Slack, Gmail, Snowflake, Trello and GitHub too (brief §1, §5); the dossier's hardness_gate (extreme) PASS is current (tier.hardness). | none stands |
| C13 | The new-issue sentence could read as a bolt-on. | It keeps Leonard's project in line with the plan he asked for; the same purpose and deadline (hub D04UP2L3E3S/1770961200.890407). | none stands |
| C14 | 'DM thread' or 'in Linear' could count as a tool mention. | Natural product names are clean (prompt_qc_examples.md row 103); no catalog function name appears (scan over Evals/references/tools/catalog.json). | none stands |
| C15 | 'Go through … make the call … Put … Then reply' could be a sequenced command list. | It scripts no sources or read order: the 'Then' only orders the reply after the work (C15 rule, screen 24 skeleton); calibration case control-plain-request matches. | none stands |
| C16 | 'When you're done, the project should match the sheet' could hint that something is missing (case K31-trap-hint). | It names no item, cause or doubt; it states the end state Leonard's project needs. K31 fails on 'a nagging feeling … not on anybody's list', which this sentence lacks; hardness_v2_check RULE_IN_PROMPT is CLEAN. | none stands |
| C17 | 'a DM' could be wrong (D04UP2L3E3S lists 5 members), or 'Blake' a loose slip for Arthur. | channels.json /414 is_im true; member lists are not graded (NB-31). 'Blake' is the hub's own name for Arthur and resolves to one person (entity.py resolve). Thursday night = 21:40 PT. | none stands |
| C18 | A sheet created by the tool might land outside Robert's root, or the reply cannot be a thread reply. | gsheets_create_spreadsheet takes driveFileId and gdrive_move_file exists; slack_send_message takes thread_ts (catalog.json); the stored wind-down baselines wrote both as Robert. | none stands |
| C19 | Arthur's DM or mail might be Arthur-only. | D04V95AAAHW is Robert's DM with Arthur (member); the mail robert@harmonygames.co/1856975772058401508 is in Robert's INBOX; check-sql PASS on every seeded load-bearing record (dossier). | none stands |
| C20 | Finding 1 is a false positive: relative day names are ordinary. | Agreed that /prompt allows it (Eval 1 §2.8); it stays Advisory only because Prompt Writing §4.2 prefers absolute dates; both resolve to one record (D04UP2L3E3S/1770961200.890407, evt_f5f279f282d20ec86bb8e5). | Advisory kept |
| C21 | A configured friction could be implied by 'take care of'. | 03_Error_Async_Config.txt: Friction: none; nothing announced. | none stands |
| C22 | The platform left A-4/A-5/A-6 for /prompt, so coherence could score below 5. | Each is settled by a later dated record and re-tested by the second blind sweep (plan/sweep_dispositions.md; dossier, Platform review): the App Review notice robert@harmonygames.co/1856994331853686118, Calm Play's 2023 subsidiary post C04UEQVDVB7/1701383740.580749, ZM's $0.00 January income in snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY. | none stands |
| C23 | Finding 2 could be a real Fail: STEP 0.6 ≥ 0.80 against robert_winddown_closeout. | The job differs (LLC take-over and founder funding vs an account close-out register) and the prompt avoids that task's vocabulary (00_Pre_Scenario_Analysis.md §5); frederick_q4_commitments kept a neighbour's skeleton with a new job and scored 0.658. Unmeasurable locally, so it stays Advisory. | Advisory kept |
| C24 | The task could reduce to one Slack post. | Four write kinds over Sheets, Drive, Linear and Slack (§4 of the brief). | none stands |

Mechanics: every quoted span in Findings and Brief coverage was checked as an exact substring of 04_Prompt.txt by script before the gate (the gate re-checks: evidence.quoted_spans, evidence.coverage_spans); severities follow the C-table; the 04_Prompt.txt hash ccd229a59a17 is the same before and after this run. Facts were re-read in this run through hg.py (Working_Files/plan/check/) and the SQL, not carried from the brief.

Unresolved: none. UNVERIFIED: none. The two Advisory findings are the human's call; neither blocks.

```
STAGE GATE prompt-check: PASS — Task_Authoring/task_inputs · 04_Prompt_Check.md#cda2fda9f6b4 · 04_Prompt.txt#7b6f4963690a · 04_Prompt_Writing_Brief.md#75df2d4fffd6 · __context__#226493b2011a · __assignment__#b4220a529c0a · __policy__#dc4ab5df3cdd · __gate_policy__#115714063000 · __review__#0cedc3e9031a · blocking 0 · warnings 0 · checks 24
[PASS] assignment.v3_context: Robert / Co-founder & Creative Director; easy cap <90%; freeze 2026-02-14T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe normal; KB bound; clock Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Check.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 04_Prompt_Writing_Brief.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 04_Prompt_Writing_Brief.md)
[PASS] chain.prompt-writing: upstream 'prompt-writing' PASS pasted and current (04_Prompt_Writing_Brief.md#75df2d4fffd6, 00_Assigments.md#97be9960492b, 01_Grounding_Dossier.md#b5ecaa709bea, 01_Universe_Inject.sql#edf1fd903611, 03_Error_Async_Config.txt#08fb87a4b11f, __context__#226493b2011a, __assignment__#b4220a529c0a, __policy__#dc4ab5df3cdd, __gate_policy__#115714063000, __review__#65afaa257571)
[PASS] structure.sections: 7 required sections present and non-empty (04_Prompt_Check.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Check.md
[PASS] structure.prompt_hash: header ties the report to 04_Prompt.txt (130 words, sha256 ccd229a59a17)
[PASS] evidence.quoted_spans: 3 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] evidence.coverage_spans: 10 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] structure.c_checks: every C1–C24 has a recorded result
[PASS] evidence.verification_log: 17/17 items carry a source pointer (min 100%)
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
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## Route

No Fail. Paste 04_Prompt.txt exactly as saved into `/prompt`, paired with `/injection` (01_Universe_Inject.sql rev2, sha256 edf1fd903611), using the GEN_EXECUTION §7 paste list; no error/async config (Friction: none) and no reference files. When `/prompt` and `/injection` ask the task date, answer "February 14, 2026". A `/prompt` FAIL is fatal: fix the cause and re-run. Then `/create-humantime`.
