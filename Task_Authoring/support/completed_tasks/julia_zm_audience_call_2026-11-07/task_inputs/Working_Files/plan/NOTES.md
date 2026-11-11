# Injection generator notes

Started 2026-11-08. Design of record: 01_Scenario_Design.md.

## Milestones
- [start] plan/ created; reading design.
- [reading] CONFLICT found: design rows R1 question/answer, R2b, R3 sit under the note (base rc 0, no thread) and R5 under Vincent's post (base rc 0, no thread). The brief's non-negotiable forbids replies under a thread-less base message. Decision pending; see below.
- [reading] Second defect: delegation quote "when you asked who those players were" is Leonard to Julia, but Robert asked at C090N54TG79/1758691397.679889. Plan: keep the quote verbatim; R4 reply says Julia asked too.
- [reading] Design says sender mailbox copies exist for human mail (Integrations, gmail row) but the manifest mints only Julia-copy ids.

## Decisions before generating (2026-11-08)
- D1 Thread-less roots. The note (rc 0) and Vincent's post 1759165414.829399 (rc 0) have no thread in base, so the five design replies (R1 question, R1 answer, R2b, R3, R5) cannot be replies under the non-negotiable. They are seeded TOP-LEVEL in C090N54TG79 with the design's ts and row ids, and text says what they refer to. data.THREADLESS_ROOT_REPLIES=False; set True to restore the design's threading. Design change needed: section 11(d), F-AGE/F-GATE/F-INDUSTRY/F-RET containers, "under my note" quotes.
- D2 Copies. Per-mailbox thread ids differ in base; sender copies get minted thread ids, the same RFC Message-ID. Leonard's forward copy keeps the manifest id, which differs from Julia's copy (design defect, reported).
- D3 Notes Docs: owner = observer, in the observer's root, shared with Julia. Not write targets.
- D4 Comments carrying device: author Julia, one per ticket, minutes after the ticket.
- D5 Friday event: design id is Julia's copy; Claire's copy gets a minted evt id, shared ical_uid (base keeps a distinct event_id per calendar).
- Retention verified through hg: 47 rows weighted D7 9.0885; 45 rows through 09-08 simple mean 8.6311. kpi_rows.json holds the 45 rows.
- [built] first generator run done; running lints.
- [run 2] sql_lint 0 errors. hg lint FAIL 0, CHECK 1 (seq, kept by instruction). base_claims PASS. Audience table from generated rows: 17 counted, casual 3.833 v RPG 3.375, 15 of 15 miss combinations past 0.25, smallest 0.270. Sweep PASS.
- F root D05GU6L0XFH/1758901945.292269 is a raw-shape export row with no id field. base_check FAILs an id-keyed UPDATE on it, so it is keyed on channel_id and ts. sql_lint warns once on that line; accepted.
- base_check needs --manifest 01_Hardness_Manifest.draft.json so the rev_3/rev_4 containers are read as declared.
- persona_view check-sql julia_lawson: verdict PASS, 0 load-bearing rows not visible (run 2 SQL).

## Final state (2026-11-08)
- Gate Doc sentence tidied; quote kept verbatim. All tools rerun on the final SQL; see the last run below.
- Open for the caller: D1 threading (five records top-level, ask quotes still say "under my note" and "under Vincent's post"); R4 opens with "julia asked me the same thing" so the ask quote is true (added clause, not in the design); Leonard forward copy has a different Message-ID from Julia's in the manifest; sql_lint warning on the F root UPDATE; base_check PASS needs --manifest draft (no final manifest exists yet).
- Rebuild: python3 plan/build.py, then plan/audience_check.py and plan/sweep.py.

## Coordinator decisions applied (for the final manifest and design_delta)
Changed delegation quotes (old -> new, all on ask C090N54TG79/1759266627.418203; data.QUOTE_CHANGES):
- F-AGE, F-INDUSTRY, F-GATE: "the rules we set under my note still stand" -> "the rules I posted in the channel after my note still stand"
- F-PANELDEF: "read the panel the way I set out when you asked who those players were" -> "read the panel the way I set out when Robert asked who those players were"
- F-RET: "retention the way Robert set it under Vincent's post" -> "retention the way Robert set it in the channel after Vincent's post"
Other changes:
- R1 question, R1 answer, R2b, R3, R5 stay top-level (THREADLESS_ROOT_REPLIES False); note_root_counters and R5 reply_count in the manifest no longer apply.
- R4: opening "julia asked me the same thing so this is for both of you." removed. The earlier plan to keep the "you asked" quote is void.
- Forward: both copies carry Message-ID <CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>. Leonard's row id is now leonard.hayes@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com> (base pattern <mailbox>/<same Message-ID>); it replaces manifest planned_records.panel_forward.leonard_copy <CAe46b4091acf4d325ec499084142670a7ee70@mail.gmail.com>.
Additions for design_delta:
- 17 sender mail copies (15 forms, re-sent form, K1 mail), each with a minted thread id, plus Leonard's forward thread, same Message-IDs as Julia's copies.
- Claire's calendar copy of the Friday event (data.CLAIRE_EVT), shared ical_uid (data.ICAL_UID).
- F root UPDATE keyed on channel_id and ts: D05GU6L0XFH/1758901945.292269 is a raw export row with no id.

## Injection completion (solver onward), started 2026-11-08
- [read] GEN_EXECUTION 5/6/6a/6b, playbook, spec, design, kit docstrings read. Pre-check risk found: gradable_surface.solver_value returns NOT_SOLVER for selectors "text" and "reason_matches", and oracle_kit contract.slots fails direct/aggregate slots that read NOT_SOLVER. S-K1b/K3b/K4b/K5b (direct, reason_matches) and S-H1/G2/D1/E1 (aggregate, text) are in that shape. To confirm once solver exists.
- [solver] solver/solver.py written; truth from records matches the plan on all 60 sessions: 17 counted, 43 not, casual 9 at 3.833, RPG 8 at 3.375, gap 0.458, hold; panel 3.33/9; retention 9.09/47 rows. Base retention rows in solver/base_retention_rows.json, read through hg.py records (a call takes about 5 minutes).
- [BLOCKER candidate] oracle_kit contract.slots FAILS on 8 surface slots: S-K1b/K3b/K4b/K5b (direct + reason_matches) and S-H1/G2/D1/E1 (aggregate + text). solver_value returns NOT_SOLVER for those selectors whatever the solver does. Fix needs the surface or a tool, both out of bounds here. Not worked around.
- [mutation] 26 results dispositioned in 01c_Dispositions.json. Solver made key-local (over-application acts only on truth-counted sessions). U 74/77 = 0.961 PASS; L_max 25/77 = 0.325, but the tool reads only field/total slots: K-miss shows 10 of the 35 declared. R_F, R_D, R_E SURVIVED: flip no solver-read slot.
- [gate] hardness_gate extreme PASS on the final manifest; fact_check PASS. Scratch test: reclassing the 8 slots to write_content makes contract PASS and gs.validate PASS; task surface untouched.
- [SQL fix] stage_gate re-runs base_check with no --manifest, where rev_4 FAILs INT-01. rev_4 row removed from emitters.py (rc_28 stays; rev_3 keeps its exception), design_delta row added. rc_28 becomes a warning in that run (83% rate). SQL rebuilt; all checks re-run.
- [state] SQL rebuilt without rev_4 (sha ca411c50). sql_lint 0 errors, base_check PASS with and without --manifest, base_claims PASS, hg lint FAIL 0 CHECK 1 (seq), fact_check PASS, check-sql PASS, hardness_gate PASS, mutation 26/26 dispositioned, liveness 6/6. oracle_kit FAIL on contract.slots only. Preflight FAIL for that reason only. Next: gate rehearsal, forecast once, final preflight, store rev1, gate dry run.
- [done] Forecast hev_a5bdd23c22790fbd, P(all) 0.000-0.167. Preflight FAIL on solver_contract only. rev1 stored, identical to the SQL. Dossier written. Dry run: STAGE GATE injection FAIL on solver.contract only (38 checks PASS). Not pasted.
- [amendment] Coordinator ordered a scenario-stage amendment: 8 slots reclassed to write_content, design text refreshed, section 12 amendment note, scenario gate PASS pasted, evidence hash 97a52ca239d1. Pre-amendment design and surface saved in run_forensics/rev1/design/. SQL unchanged (rev1, ca411c50). Solver contract PASS, preflight PASS.
- [forecast] hev_31aeef573fe8aea8 (design mode, declared attributions) supersedes hev_a5bdd23c22790fbd, because the reclass does not make solver-mode read text slots. P(all) 0.307-0.352.
- [fresh] mtime-only touch of SQL, solver and dispositions after the scenario amendment: contents unchanged (SQL cmp equal to rev1), checks re-run after the amendment.

## rev2: 01d_SQL_Review.md applied (run_forensics/rev1 untouched)
Changed delegation quote (data.QUOTE_CHANGES):
- F-LIMIT (gate Doc f_748d26e760e54651eaa0d8): "limits on a pass sit in review on the PR for the branch the job ran on" -> "What a pass does and doesn't cover gets discussed on his Vision Bot PR"
- The three ask quotes from the previous round stand (F-AGE/F-INDUSTRY/F-GATE, F-PANELDEF, F-RET).
Text changes: M1 R0 relay carries the note's no-coaching line, the age band, the Doc fields and the mail fields. M2 Vincent's line says the repro was in the editor with no Samsung phone. M4 gate Doc rewritten in plain terms (one "whatever day", ZOM-559 as a bug-queue note, the closed-ticket sentence, Arthur's Vision Bot PR as where pass coverage is discussed); log note says only "The ticket date is just the day I typed it"; card says "the audience call and the numbers behind it". m1 R3 adds "that goes for sessions already run too". m2 a/an rule. m4 forward names both runs, says the mails link videos and survey reports, and quotes the 03:44 mail body in full. m5 Brian Docs 01..09 ascend from 09:05:00 (01 is the form, the T-K4 version time). m7 Julia asks in Turkish first.
Removed ids (design_delta): harmonygames-Games/match3d#476#rc_28, #rev_4 (already absent), mirror row 2386636f2f828606f470fa38df201f16. #zombie-prs root 637fc98b... now rc 30, latest 1759263026.184402. PR #476 updated_at 2025-09-30T20:10:26Z.
Added id (design_delta): Julia's K4 question, D076RBM29JS/1758658884.207315, row sha256(channel|ts)[:32].
m6 content swaps (design_delta; ticket, observer, form, date, Doc and comment ids stay): ZOM-589<->ZOM-601, ZOM-592<->ZOM-603, ZOM-595<->ZOM-606, ZOM-597<->ZOM-620. K3 tickets are now ZOM-587, 588, 590, 591, 593, 594, 596, 601, 603, 606, 620; the swapped-in clean ones are ZOM-589, 592, 595, 597. Counts and means unchanged. The manifest's K3 ticket range (ZOM-587..597), trap/surface ticket lists and re-run note targets need the same update.
- [rev2] run_forensics/rev2 stored (1485546c). Solver: gate-Doc parser and a/an device parse generalised, controls moved to truth-counted sessions; rev1 truth reproduced byte for byte (run_forensics/rev1/truth.json). Truth unchanged in aggregates: 17 counted, casual 9 at 3.833, RPG 8 at 3.375, hold; K3 = 587,588,590,591,593,594,596,601,603,606,620. Kadikoy fact home adds Julia's question. All checks PASS; hev_31aeef573fe8aea8 stands (design-mode inputs unchanged). STAGE GATE injection: PASS pasted.

## rev4: Slack parent-id fix (run_forensics/rev1..rev3 untouched)
- [defect] Hand edit (sha fb77a415) replaced Robert's DM reply 167dc58affb9902420038f71d0f5af28 thread_parent_id '8450048848997da8d669cd475badfbd7' (minted sha of D05GU6L0XFH|1758901945.292269; the base root is a raw-shape row with no id) with a subquery on channel_id and ts.
- [generator] emitters.py: Raw SQL-expression type in q(); slack_parent() emits the subquery for every root in data.RAW_ROOTS, else the sha id. build.py output is byte-identical to the hand edit (sha fb77a4153f49...).
- [sweep] plan/parent_check.py reads every seeded reply root through hg.py records: R4_panel_definition, K5_reply, mirror_rc27 parents equal the base row ids; F_reply was the only parent pointing at no row.
- [checks] sql_lint 0 errors / 1 warn line 710 (raw UPDATE), hg lint FAIL 0 CHECK 1 L676; neither objects to the subquery. Dossier sql_lint/LINT lines re-derived, rev4 open-item note added.
- [rev4 done] run_forensics/rev4/ stored (SQL fb77a415, clean copy, parent_check.json, rev3_to_rev4.diff). base_check (with/without --manifest), base_claims, check-sql, audience_check, sweep, fact_check, hardness_gate PASS; oracle_kit contract PASS (sql fb77a4153f49), mutation dispositioned, preflight PASS (label still reads rev2 from the tool). Dossier pasted outputs refreshed from rev4 runs (plan/repaste_rev4.py). Manifest unchanged: no id or quote changed. STAGE GATE injection: PASS pasted; dry run handoff.pasted current.
- [error-async] 03_Error_Async_Config.txt: Friction: none, 4 counter-readings. STAGE GATE error-async: PASS pasted; dry run confirms.

## rev5: timezone-neutral relative-time wording (run_forensics/rev1..rev4 untouched)
- [scan] plan/reltime_scan.py over every seeded statement. Frames: Pacific (evaluator) and Turkey (Julia). Four texts false in one frame; every other hit is an absolute weekday+date, a titled event, or a same-day phrase true in both (log note "typing the tickets up in one batch today": note 16:24Z, tickets 17:14-19:42Z, Sep 30 in both frames).
- [edit] data.py: R1Q "your note from this morning" -> "your note" (note 05:01Z Sep 22 = Sun Sep 21 22:01 PT). K4_Q "bu sabah paylaştığın notlara" -> "paylaştığın notlara" (Brian Docs 09:05Z Sep 23 = 02:05 PT / 12:05 TR). ASK "change from yesterday" -> "change from Monday" (b429c2a8 2025-09-29T19:17:46Z, Mon in both; ask 21:10Z Sep 30 = Tue PT but Wed 00:10 TR). K1 Claire mail (Mon 10:02Z, Monday in both) "this week was all items" -> "last week was all items" (same length, size_estimate and snippet length unchanged).
- [build] SQL sha 5b6e0111... ; diff vs rev4 = exactly those four texts (lines 422/424/426/428 snippet+body, 683, 689, 705). Clean copy matches.
- [checks] chain_rev5.sh: sql_lint 0 errors / 1 warn L710, hg lint FAIL 0 CHECK 1 L676, base_check (with/without --manifest), base_claims, check-sql, audience_check, sweep, parent_check (unhandled []), fact_check --no-leak, hardness_gate PASS; oracle_kit contract PASS (sql 5b6e01119505), mutation dispositioned, liveness, preflight PASS. Outputs equal rev4 apart from the sha (v2 RULE_IN_PROMPT now CLEAN since the prompt exists). Stored in run_forensics/rev5/ (SQL, clean, rev4_to_rev5.diff, reltime_scan, checks/).
- [manifest] unchanged: no changed text is a delegation_quote or fact text (grep of manifest, surface, solver).
- [dossier] Rev5 open-item note; pasted outputs refreshed (repaste_rev4.py); LINT L676 and sql_lint L710 unchanged. STAGE GATE injection: PASS pasted.
- [brief] 04_Prompt_Writing_Brief.md: rev5 sha, prompt quotes and 6b rows matched to current 04_Prompt.txt (date phrases gone; "the ones that came out of his feedback note", "he has to act on this, so give him one call, not a maybe", 143 words); checklist and truthfulness row updated.
- [error-async] stale on the SQL sha only; config re-checked (rev5 line added, Friction: none stands). STAGE GATE error-async: PASS pasted.
- [prompt-writing] 00_V3_Authoring_Evidence.json outcome_reviews.prompt-writing re-bound to the brief (6e4a12109b17) with a re-review note; outcomes unchanged. STAGE GATE prompt-writing: PASS pasted. 04_Prompt_Check.md not touched.
