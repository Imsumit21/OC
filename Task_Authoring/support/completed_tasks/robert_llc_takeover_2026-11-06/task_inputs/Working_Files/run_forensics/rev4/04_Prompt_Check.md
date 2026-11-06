# Prompt Check — robert_llc_takeover
> Prompt: 04_Prompt.txt · 130 words · sha256 ccd229a59a17 · Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) · checked 2026-11-06 against 04_Prompt_Writing_Brief.md (2026-11-06, rev4, SQL f1a290ced176) · release task-quality-v1
> Suggested wording is allowed under the repository exception. Check clean ordinary writing, role plausibility, no hints/riddles and every fair outcome.

Robert · Executive · Finance · Planning and decision support · Long Horizon · Easy (V3 cap < 90 %, requester target < 85 % average) · normal universe, Robert's today Saturday Feb 14, 2026. Upstream: injection rev4 (01_Universe_Inject.sql sha256 f1a290ced176, not yet submitted; rev3 passed /injection and /prompt with every dimension at 5, then failed /hardness at 2), 03_Error_Async_Config.txt (Friction: none, re-gated for rev4), no reference files. The text was read byte for byte; the 04_Prompt.txt hash was ccd229a59a17 before and after this run.

This is the re-check of the unchanged prompt against the rev4 data. rev4 rewords four records and adds two (Arthur's 'jenkins' email, Leonard's layer.ai reply) so that four corrections sit off the swept path (Working_Files/01a_Hardening_Report.md; 01_Scenario_Design.md §14). The first check of rev4 (same prompt, SQL 0d4fb218f314) was BLOCKED: a focused fifth blind sweep rated ENG-2454 layer.ai's state OPEN between Todo and Canceled. It was routed to `/create-injection`. Leonard's reply now ends "the art goes with CF, there's nothing on the layer account for our new company to take, it just lapses" (SQL f1a290ced176), with no 'LLC' keyword. A fresh blind re-check then rated the state SETTLED (Working_Files/plan/sweep_dispositions.md, 'Re-check of the fix'). This report re-runs C1–C24 on that data.

## Summary

- Fail 0 · Non-fail 0 · Advisory 2 (C20 relative day names; C23 same-scenario neighbour at 0.776, gate PASS on the platform for this exact text) · UNVERIFIED none.
- Checks clean: C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C21, C22, C24.
- Calibration self-test: the text matches no FAIL case and matches all five PASS controls/cases it can be compared with (table below).
- Predicted /prompt band: PASS (no Fail, no Non-fail, no UNVERIFIED hard gate among C4, C6, C17, C18, C19).
- Status: READY FOR /prompt.

## Findings

| # | Check | Dimension · severity | Quoted span | Rule (source) | Defect |
|---|---|---|---|---|---|
| 1 | C20 | Alignment with Today's Date · Advisory | "on Thursday night" … "before Monday's call" | Prompt Writing §4.2 prefers absolute dates; Eval 1 §2.8 allows relative wording that resolves to one window | Relative day names. Each resolves to one record: the hub D04UP2L3E3S/1770961200.890407 is Thu Feb 12 2026 21:40 PST, and Monday's call is evt_f5f279f282d20ec86bb8e5, Mon Feb 16 10:00–10:45 PT. No change suggested. |
| 2 | C23 | Originality · Advisory (no supplied sample) | "what it costs each of us a month" | Eval 1 §2.9; platform STEP 0.6 dataset duplicate (meaning ≥ 0.80 caps the score at 2) | Measured on the platform for this exact text (run_forensics/rev3/1_prompt_PASS_r3.md, Dataset Similarity): nearest neighbour 0.776 ('same scenario', a completed Robert task with an LLC go/no-go doc), next 0.708; gate PASS. The prompt is unchanged. |

## Fair readings (accepted outcomes)

Reading A is the best-supported reading; Reading B is the strongest alternative. Each is settled by a newer source, an incorporated authority, source identity or scope, or accepted as a second fair outcome. Sidecar `outcome_reviews.prompt-check` is rewritten in this run and bound to the 04_Prompt.txt digest.

| Deliverable | Reading A | Reading B (strongest alternative) | Resolution and evidence |
|---|---|---|---|
| Plan sheet | A new Google Sheet in Robert's Drive root d_9f7ba94f7526d54d8482ba with the draft's eight columns, 38 rows (ENG-2438…ENG-2474 + the CF VO campaign) and the three shares per month; shared with leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co | B1: copy Leonard's draft f_d996e4c434ce160dc52596 and rewrite it. B2: edit the draft in place | B1 accepted (same location, columns, rows, readers). B2 rejected by source identity: the draft is Leonard's file and the hub says "keep it in your drive" (D04UP2L3E3S/1770961200.890407). Title, column order, extra columns, share role and one vs two Metabase/dbt rows are representational (brief §4b). |
| Plan sheet figures | DD prod 140, CF stacks 62, VO campaign 3,000, Metabase 100, dbt 100, GitHub 48; total 3,450, a third 1,150 | CF stacks at $95 (ENG-2445 note); the draft's ~$1k / ~$300; the campaign at $100 × 31 | Settled under the costing rule ('Cost every item at what it bills now', f_1e468a9d69ea0f0a2001f5) by later owner records: Arthur's 'jenkins' email robert@harmonygames.co/1856982378087295205 ("bills $62 a month now", 04:20Z, after the 00:58Z note), his DM reply D04V95AAAHW/1770952200.665739 ($140), his billing mail robert@harmonygames.co/1856975772058401508 ($248 carried), Leonard's status C09UHHN6PFZ/1770938400.370665 ("capped at $3,000 a month"). |
| Campaign payer | The LLC from March | Leonard (his card), counted as his carried cost | Settled: "it's on my card till the end of Feb and moves to our new company's card from March … so count it as its own line in what we pay each month" (C09UHHN6PFZ/1770938400.370665); the plan runs Mar 1–May 31 (ground rules). |
| Issue states | The 6 LLC issues and the new campaign issue Todo with the runner; Metabase, dbt, GitHub Done; the HG issues Canceled | ENG-2462 Done (Arthur's "done"); GitHub Canceled (HG keeps the org) or Todo (Leonard's "then the repos transfer") | ENG-2462: the App Review notice robert@harmonygames.co/1856994331853686118 (07:30Z) is later than Arthur's note (01:30Z) and leaves the support build to ship, so Todo/Arthur. GitHub: the Done test comes first, "if one of us pays it himself through May (even if HG still owns it)", with Arthur's "count it as mine like the other two". Both settled (fifth sweep: WEAK, record beats it). |
| ENG-2454 layer.ai state | Canceled (the account lapses with HG) | Todo, Robert (the art goes with CF; the export is left) | Settled since the fix: the reply C09UHHN6PFZ/1770923700.470906 says "there's nothing on the layer account for our new company to take, it just lapses", and the project description allows Todo only "if the LLC takes it". A fresh blind re-check rated it SETTLED. |
| layer.ai export step's row | On the layer.ai row | On the Combo Fighter row ("the art goes with CF") | Both accepted (brief §4b): the same step, owner and date on the same sheet. The writes, destination and next action are identical; only the row holding the text differs. |
| layer.ai step, owner, date | Robert pulls CF's concept art out by Mar 3 | Leonard owns it (he cancelled it; the card's 'whoever runs it'); by Mar 2 ('before then') | Owner settled by the reply's direct ask ("can you pull it out yourself"); the date set accepts by/before Mar 3 and Mar 1–3 (brief §4b). |
| Todo assignees | ENG-2438 Robert, ENG-2439 Leonard, ENG-2441 and ENG-2445 Arthur, ENG-2451 Leonard, ENG-2462 Arthur, the new VO issue Leonard | ENG-2439 Arthur; ENG-2451 Arthur | Settled by each runner's note ("I'll handle it with Sunset", "I'll set CF up on it") under 'assign whoever moves it' and the card 698e6548aa9516b76c4ab475. |
| Build machines and Jenkins | ENG-2446 Canceled; no Jenkins line | The LLC takes the build boxes; a $0 Jenkins line and issue | Settled: the 'jenkins' email says "the build boxes are HG's" and the jobs run on Arthur's own machine with no bill; the ground rules count only monthly bills. |
| Missing plan line | A new issue for the CF VO campaign, Todo, Leonard | No new issue (the DM says "everything we might need from HG") | Settled: "count it as its own line" (C09UHHN6PFZ/1770938400.370665), the project description's "or pay for", and the prompt's "the project should match the sheet". |
| Reply to Leonard | A thread reply under D04UP2L3E3S/1770961200.890407 | A new top-level DM message | Settled by the prompt ("in that DM thread"). |
| Monthly cost each | $1,150 each (a third of $3,450), optionally with Arthur's $902 cash after his carried $248 | $902 given as Arthur's cost | Settled by the split email robert@harmonygames.co/1856989298688559716 (what one already pays "counts toward his third"); the platform's rev3 review rejected "$902 as Blake's cost" (run_forensics/rev3/1_prompt_PASS_r3.md DR1). Brief §4b tightened to match in this run. |

## Calibration self-test (prompt_qc_cases.json, 15 calibration cases)

| Case | Rule | Expected | This prompt |
|---|---|---|---|
| K11-staged-errors | staged_errors | FAIL | not matched: spelling, capitals and punctuation are clean |
| K11-control-spelled-correctly | staged_errors | PASS | matched |
| K31-trap-hint | trap_hint_or_riddle | FAIL | not matched: no hint at a hidden item; 'the project should match the sheet' is a sync instruction |
| control-symptom | trap_hint_or_riddle | PASS | matched in kind: the prompt names Leonard's ask, not a cause |
| K42-hidden-destination | hidden_destination | FAIL | not matched: Drive, the LLC project and the DM thread are named |
| K47-hidden-destination | hidden_destination | FAIL | not matched |
| K44-hidden-destination | hidden_destination | FAIL | not matched: the reply's place is "in that DM thread" |
| control-named-destination | hidden_destination | PASS | matched |
| K1-audit-form | audit_form | FAIL | not matched |
| K43-audit-form | audit_form | FAIL | not matched |
| K44-if-chain | if_chain | FAIL | not matched: the per-item rules live in the ground rules doc and the project description |
| control-plain-request | audit_form | PASS | matched |
| K43-departed-person-premise | false_state_premise | FAIL | not matched: only Leonard, Blake and Robert act, all active (C0ADGSZKR3R/1770842402.772039) |
| K50-both-fair-figure | ugt_both_fair_figure | PASS | not applicable: no figure is left to the run's choice between sources |
| K49-newer-source | ugt_both_fair_figure | PASS | matched in kind for every figure fork (CF stacks, ENG-2462): a newer dated record settles it |

## Check results (C1–C24)

| # | Result | Evidence |
|---|---|---|
| C1 | clean | 130 words (whitespace split), inside 20–4,000 |
| C2 | clean | Working_Files/00_Task_Context.json (refreshed this run): all eight V3 fields; persona robert resolves; normal universe, source supports the 2026-02-14T00:00Z freeze |
| C3 | clean | Robert is a co-founder running the wind-down (C0ADGSZKR3R/1770839322.836779), Combo Fighter is his game (C07C2866011/1770084297.911029) and Leonard asks him directly (D04UP2L3E3S/1770961200.890407); voice judged against the role only (A-27) |
| C4 | clean | Executive (a founders' strategic call), Finance (the three-month cost and each founder's share), Planning and decision support (the per-item call and recommendation); the plan sheet is the authored artifact |
| C5 | clean | Ambiguity, dynamic change and multi-source are load-bearing (brief §8): rev4 adds two off-path corrections (F32 the 'jenkins' email over F27; F33 the layer.ai reply over the ENG-2454 note); the prompt restates no rule, figure or source beyond the two anchors |
| C6 | clean | Fair readings table above: every material field and every Linear write is settled by the prompt or a dated record. ENG-2454's state is settled since the fix (blind re-check SETTLED). The export step's row is accepted either way (same material result). Sidecar outcome review rewritten this run |
| C7 | clean | Writes under every reading: sheet create + values + share ×2, a comment + state ×37, one issue create, one thread reply; each issue has one supported state (ENG-2454 Canceled since the fix). Channel, time and form are pinned per deliverable. The open fields (title, share role, wording, the row holding the layer.ai step) are not channel, time or form. No 'I'll [verb]' beside an agent imperative |
| C8 | clean | (a) the hub is Robert-visible (DM member EMPLOYEE_0016_SLACK_ID, channels.json /414 re-read this run); (b) one thread, one draft f_d996e4c434ce160dc52596, one project 'LLC take-over' (base linear /projects has no 'LLC' match, scan complete; control 'Zombie Match 3D' found); (c) the hub states the asks; (d) instructions, not answers |
| C9 | clean | No decision, figure, count, root cause or finding entity in the prompt; brief §9 scan (rev4 additions: layer.ai, CF's art, the 'jenkins' email, $62/$95, issue states) finds none |
| C10 | clean | Only AN1 and AN2 are named; 'his draft' and 'Monday's call' are the hub's own references |
| C11 | clean | Every write depends on the investigation: rows, decisions, costs (F32), states (F14, F33), the new issue and the reply's figures |
| C12 | clean | Slack, Linear, Gmail, Drive family, Snowflake, Trello, GitHub, GCal and Confluence carry weight (brief §1). 01_Hardness_Manifest.json present; hardness_gate (extreme) re-run this run on the current tools: PASS, output identical to the dossier's paste |
| C13 | clean | One purpose: Leonard's ask before Monday's call |
| C14 | clean | No function, parameter or server name (catalog scan) |
| C15 | clean | The single 'Then' orders the final reply after the work (screen 24 skeleton) |
| C16 | clean | No spec-sheet layout, answer-key clause, staged error, riddle, hedge, hidden destination, audit wording or if-chain; hardness_v2_check (re-run on rev4): 'CLEAN RULE_IN_PROMPT no run of 8 resolver words in the prompt' |
| C17 | clean | Verification log below: every person, channel, doc, date, state premise and narrative claim re-found in this run |
| C18 | clean | Catalog writes exist (gsheets_create_spreadsheet, gsheets_values_update, gdrive_share_file, gdrive_move_file, linear_create_comment, linear_update_issue, linear_create_issue, slack_send_message with thread_ts); `gradable_surface.py gradeable-report`: SURFACE.GRADEABLE PASS · 25 slot(s); spot decode of a realistic deliverable set (the rev3 pre-check run, plan/check_rev4/spot_decode.json): the table, plan/reply/new-issue text, thread delivery and link selectors all decode (field slots miss only on that run's ' (ENG-n)' key suffix, the known decoder limit the hardening report dispositioned) |
| C19 | clean | Every scoped read is Robert's: the 'jenkins' email and the App Review notice are his INBOX copies, the layer.ai reply is in #prototype C09UHHN6PFZ where he is a member and @-mentioned (check-sql PASS, dossier); Linear, Trello, GitHub, Snowflake, Confluence unscoped |
| C20 | Advisory (finding 2) | Thursday night = Thu Feb 12 21:40 PT (past); Monday's call = Mon Feb 16 10:00 PT (future meeting) |
| C21 | clean | Friction: none (03_Error_Async_Config.txt, rev4 header) |
| C22 | clean | rev4's injection gate passes on the current tools (01_Grounding_Dossier.md, SQL f1a290ced176: base_check, base_claims, fact_check, sql_lint 0 errors, hg lint FAIL 0, check-sql PASS); the fix changes one reply's text and adds no 'LLC' keyword. Seed-vs-base points from the fifth sweep (Arthur's Feb 11 'transfer to my LLC', the Feb 7 'keep both campaigns live', PR #1917 head_ref, the $140 reply's Feb 2 root) are each superseded by a later record or a base pattern (platform rev3 DR6, NB-13); none blocks |
| C23 | Advisory (finding 3) | No supplied sample; STEP 0.6 read on the platform for this exact text |
| C24 | clean | Four kinds of write over Sheets, Drive, Linear and Slack |

## Verification log

Every row was looked up in this run: base records through `Task_Authoring/tools/hg.py search` (outputs in Working_Files/plan/check_rev4/), seeded records from 01_Universe_Inject.sql (rev4).

| Span | Type | Universe record (locator) | Result |
|---|---|---|---|
| Leonard | person | slack users.json /23: EMPLOYEE_0038_SLACK_ID 'Leonard Hayes' leonard.hayes@harmonygames.co (hg.py get-many, check_rev4/reads.out.json) | the hub's sender; unique Leonard |
| a DM | channel | D04UP2L3E3S, channels.json /414: is_im true, members include EMPLOYEE_0016_SLACK_ID (Robert) and EMPLOYEE_0038_SLACK_ID (hg.py get-many) | match; member lists never graded (NB-31) |
| on Thursday night | date | hub ts 1770961200.890407 = Thu Feb 12 2026 21:40 PST | match |
| setting up the LLC so we can keep Combo Fighter going | event | D04UP2L3E3S/1770961200.890407: 'if you really want to keep combo fighter going, let's set the LLC up properly' | match |
| after the shutdown | state | C0ADGSZKR3R/1770931777.561519 ('wind down agreement and data agreement reviewed and signed', hg.py get-many /172) | match; wind-down acknowledged |
| Monday's call | event / date | evt_f5f279f282d20ec86bb8e5 'LLC: decide', 2026-02-16T18:00–18:45Z, attendees Leonard, Robert, Arthur | match (future meeting) |
| the LLC project in Linear | ID / project | 0fa95761-d59b-4ff4-a8a3-15df3210ca6e 'LLC take-over' (seeded); base linear data.json /projects: 0 matches for 'LLC', scan complete; control 'Zombie Match' → /projects/1 (check_rev4/s_proj*.json) | match; the only LLC project |
| the way he lays it out | relationship | hub: 'make the call on each one … the ground rules doc has how we decide'; f_1e468a9d69ea0f0a2001f5 'LLC ground rules (Combo Fighter and whatever else we take)' | match |
| he and Blake | person | entity.py resolve 'Blake' → sole candidate arthur.blake@harmonygames.co (check_rev4/entity_blake.txt) | match |
| my Drive | destination | Robert's root d_9f7ba94f7526d54d8482ba | match |
| his draft | doc | f_d996e4c434ce160dc52596 'LLC 90 days (draft)', owner Leonard, created 2026-02-10T18:30Z (Tue) | match |
| share it with both of them | recipients | leonard.hayes@harmonygames.co, arthur.blake@harmonygames.co | match |
| the plan sheet | requested output | evt_f5f279f282d20ec86bb8e5 description 'Robert's plan sheet' | new output, not a premise |
| the project should match the sheet | requested output | project 0fa95761-d59b-4ff4-a8a3-15df3210ca6e, issues ENG-2438…ENG-2474 (seeded, 01_Universe_Inject.sql); rev4 description: 'to Done if one of us pays it himself through May (even if HG still owns it) or if the LLC takes it and nothing is left to do on it; to Todo if the LLC takes it and something is still to do … to Canceled if it stays with HG' | new state, not a premise; every issue's state settles under it |
| reply to him in that DM thread | channel | thread_ts 1770961200.890407 in D04UP2L3E3S | match |
| what it costs each of us a month | figure (requested) | split email robert@harmonygames.co/1856989298688559716 'LLC money' | the rule exists; the figure is a requested output |
| me / my | persona | robert@harmonygames.co | match |
| (layer.ai, the fixed reply) | record | base C09UHHN6PFZ/2026-02.json /575 'canceled layer.ai account … we have access until March 3rd' and C0ADGSZKR3R/2026-02.json /64 'I just canceled layer' (hg.py get-many, check_rev4/reads2.out.json); seeded reply C09UHHN6PFZ/1770923700.470906 ending "there's nothing on the layer account for our new company to take, it just lapses" (SQL f1a290ced176; no 'LLC') | all exist; the reply settles Canceled |

## Brief coverage

| Brief item (§4 deliverables, §6 triggers) | Present in the prompt (quoted span, or absent) |
|---|---|
| AN1 anchor: Leonard's DM | "Leonard sent me a DM on Thursday night" |
| deadline: Monday's call | "I want my answer ready before Monday's call" |
| AN2 anchor and the per-item scope | "Go through the LLC project in Linear" |
| §6 decide each candidate under the ground rules | "make the call on every item the way he lays it out" |
| §4 call on each issue | "leave the call on each issue so he and Blake can see it there" |
| §4 plan sheet in Robert's Drive; §6 sheet layout | "Put the plan sheet in my Drive, laid out like his draft" |
| §4 sheet shared with Leonard and Arthur | "share it with both of them" |
| §4 missing plan line; §6 state per issue | "the project should match the sheet" |
| §4 reply in Leonard's thread | "reply to him in that DM thread" |
| §4 reply contents; §6 the split | "what I'd do and what it costs each of us a month, with the link to the sheet" |
| §6 the take test, the costing rule, owners and dates | absent (record triggers: the ground rules and the LLC card) |
| §6 the campaign as its own line | absent (record trigger: Leonard's status 'count it as its own line') |
| §6 the layer.ai step, owner and date | absent (record trigger: the reply's @-mention of Robert) |

## Self-review

Phase walk (Evals/1_Prompt_Eval.md, Phases 1–3, read again for this run): Phase 1 → C2–C5; Phase 2 → C6–C20, C23; Phase 3 → C21, C22. Every C-check has a result with evidence; none is UNVERIFIED.

| Check | Counter-reading (strongest case that /prompt fails it, or that a finding is a false positive) | Evidence that resolves it | Verdict |
|---|---|---|---|
| C1 | Another tokenizer could put the text outside the field. | 130 whitespace words; the limit is 20–4,000. | none stands |
| C2 | The assignment could be read as Normal Horizon. | 00_Assigments.md and 00_Task_Context.json: Long Horizon, Easy, Feb 14, 2026. | none stands |
| C3 | A Creative Director costing an LLC looks like a CFO job. | Leonard asks Robert himself (D04UP2L3E3S/1770961200.890407); the decision is the founders' (evt_f5f279f282d20ec86bb8e5). A better-fitting colleague alone is not a Fail. | none stands |
| C4 | Business Function could score 3 as 'Finance fits better'. | A strategic call on carrying a game into a new company; Finance is the assigned competency; the platform scored rev3 at 5. | none stands |
| C5 | 'the way he lays it out' could carry the recipe. | It points at the hub; the rules live in f_1e468a9d69ea0f0a2001f5 and the project description, none restated. | none stands |
| C6 | ENG-2454 could still read as Todo/Robert ('the art goes with CF'), as the fifth sweep found on the earlier wording; or the export step's row could split the rubric. | The reply now adds "there's nothing on the layer account for our new company to take", and the project description allows Todo only "if the LLC takes it"; a fresh blind agent rated it SETTLED (sweep_dispositions.md, 'Re-check of the fix'). The row placement gives the same writes and values and is accepted either way (brief §4b). | none stands |
| C7 | The other 36 states could hide a second open fork (GitHub's 'then the repos transfer'; ENG-2462's 'done'). | Fifth sweep: both WEAK, a record beats each (the Done test's '(even if HG still owns it)'; the later App Review notice robert@harmonygames.co/1856994331853686118). | none stands |
| C8 | 'his draft' could be ambiguous or hand over an answer. | One Leonard draft about the LLC, f_d996e4c434ce160dc52596; its figures are stale (brief §5 F5). | none stands |
| C9 | 'what it costs each of us a month' could presuppose equal shares. | It asks for each founder's figure without giving one. | none stands |
| C10 | Naming 'Monday's call' or 'his draft' could collapse discovery. | Both are the hub's own references; no hidden authority is named (brief §5). | none stands |
| C11 | The writes might not depend on findings. | Costs and states turn on F14, F32 and F33 (brief §5), the new issue on F12. | none stands |
| C12 | The second service could be trivial. | Weight sits in Slack, Gmail, Snowflake, Trello and GitHub too; hardness_gate (extreme) PASS re-run on the current tools. | none stands |
| C13 | The new-issue sentence could read as a bolt-on. | It keeps the project in line with the plan Leonard asked for. | none stands |
| C14 | 'DM thread' or 'in Linear' could count as a tool mention. | Natural product names (prompt_qc_examples.md row 103). | none stands |
| C15 | 'Go through … Put … Then reply' could be a command list. | No sources or read order scripted; the 'Then' orders the reply after the work. | none stands |
| C16 | 'the project should match the sheet' could hint that something is missing (K31). | It names no item or doubt; RULE_IN_PROMPT CLEAN on rev4. | none stands |
| C17 | 'a DM' could be wrong (D04UP2L3E3S lists 5 members), or 'Blake' a slip. | channels.json /414 is_im true; NB-31; 'Blake' resolves to one person (check_rev4/entity_blake.txt). | none stands |
| C18 | The sheet might land outside Robert's root, or a selector might not decode. | gsheets_create_spreadsheet + gdrive_move_file; gradeable-report PASS 25/25; spot decode of the rev3 run decodes every selector kind. | none stands |
| C19 | The 'jenkins' email or the layer.ai reply might be invisible to Robert. | Robert's INBOX copy robert@harmonygames.co/1856982378087295205; #prototype member, and the reply @-mentions him (brief §5a F32, F33 YES). | none stands |
| C20 | Finding 2 is a false positive. | /prompt allows relative wording (Eval 1 §2.8). | Advisory kept |
| C21 | Friction could be implied by 'take care of'. | Friction: none; nothing announced. | none stands |
| C22 | rev4's new records could clash with base data, or the fix could add a keyword that re-exposes the reply. | Fifth sweep: every seed-vs-base point is superseded by a later record or is a base pattern (DR6, NB-13); the layer.ai parent /575 has its thread fields set by the rev4 UPDATE; the fixed reply holds no 'LLC' (checked in the SQL this run) and agrees with #winddown's 'I just canceled layer' (/64). | none stands |
| C23 | Finding 3 could be a real Fail (STEP 0.6 ≥ 0.80). | The platform measured this exact text at 0.776 (rev3 report). | Advisory kept |
| C24 | The task could reduce to one Slack post. | Four write kinds over Sheets, Drive, Linear and Slack. | none stands |

Mechanics: every quoted span in Findings and Brief coverage is an exact substring of 04_Prompt.txt (checked by script); severities follow the C-table; the 04_Prompt.txt hash ccd229a59a17 is the same before and after this run. Facts were re-read in this run through hg.py (Working_Files/plan/check_rev4/) and the rev4 SQL.

The upstream chain was re-gated on the current tools (commit c16c7a1 changed the gate-policy hash): scenario, injection (SQL f1a290ced176), error-async and prompt-writing all PASS and pasted.

Unresolved: none. UNVERIFIED: none. The two Advisory findings are the human's call; neither blocks.

```
STAGE GATE prompt-check: PASS — Task_Authoring/task_inputs · 04_Prompt_Check.md#969d49a9f6cd · 04_Prompt.txt#7b6f4963690a · 04_Prompt_Writing_Brief.md#c6eac44b80a9 · __context__#226493b2011a · __assignment__#b4220a529c0a · __policy__#dc4ab5df3cdd · __gate_policy__#f8638415ca2c · __review__#7a85c7594f55 · blocking 0 · warnings 0 · checks 24
[PASS] assignment.v3_context: Robert / Co-founder & Creative Director; easy cap <90%; freeze 2026-02-14T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe normal; KB bound; clock Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Check.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 04_Prompt_Writing_Brief.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 04_Prompt_Writing_Brief.md)
[PASS] chain.prompt-writing: upstream 'prompt-writing' PASS pasted and current (04_Prompt_Writing_Brief.md#c6eac44b80a9, 00_Assigments.md#97be9960492b, 01_Grounding_Dossier.md#1188624c21da, 01_Universe_Inject.sql#f1a290ced176, 03_Error_Async_Config.txt#8a2688db32e6, 01a_Hardening_Report.md#ea55f2ba0d17, __context__#226493b2011a, __assignment__#b4220a529c0a, __policy__#dc4ab5df3cdd, __gate_policy__#f8638415ca2c, __review__#0b2f7ae8d29a)
[PASS] structure.sections: 7 required sections present and non-empty (04_Prompt_Check.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Check.md
[PASS] structure.prompt_hash: header ties the report to 04_Prompt.txt (130 words, sha256 ccd229a59a17)
[PASS] evidence.quoted_spans: 3 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] evidence.coverage_spans: 10 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] structure.c_checks: every C1–C24 has a recorded result
[PASS] evidence.verification_log: 18/18 items carry a source pointer (min 100%)
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

No Fail. Paste 04_Prompt.txt exactly as saved (unchanged, sha256 ccd229a59a17) into `/prompt`, paired with `/injection` (01_Universe_Inject.sql rev4, sha256 f1a290ced176), using the GEN_EXECUTION §7 paste list. There is no error/async config (Friction: none) and there are no reference files. When `/prompt` and `/injection` ask the task date, answer "February 14, 2026". A `/prompt` FAIL is fatal: fix the cause and re-run. Then the second (last) Opus 5.5 pre-check and `/hardness`.
