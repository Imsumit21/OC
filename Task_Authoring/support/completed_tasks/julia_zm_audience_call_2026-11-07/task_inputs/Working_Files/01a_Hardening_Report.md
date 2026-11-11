# 01a Hardening Report: julia-gtm, rev6 pre-check intake

## 1. Mode, inputs, run validity

**MODE B (pre-check intake).** One unhinted Opus 5.5 run on rev6, plus the platform `/hardness` report on that run (FAIL, score 1, Too easy, HOLD, INSUFFICIENT_DIFFICULTY).

- Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Universe manifest: `Evals/references/universes/synthcut/universe_manifest.json`.
- Task context: `Working_Files/00_Task_Context.json` (refreshed with `task_context.py --write --require-source`). Assignment: Julia Lawson, Product Manager · Product · Marketing and GTM · Analysis and synthesis · long-horizon · difficulty **medium** (unchanged; design target stays Hard < 70 %).
- Inputs read:
  - `04_Prompt.txt` (sha `729d3623…`)
  - `01_Universe_Inject.sql` (sha `16f9657c…`), stored as `run_forensics/rev6/01_Universe_Inject.sql`
  - `06_PreCheck_Trajectory/trajectory.json`, a copy of the upload `trajectory-run-1 (1).json`. The content is identical to the export `/hardness` hashed (`6bc69281…`); only the whitespace differs.
  - The `/hardness` report `6aeed82405095a0cfdffde2a_1a_hardness.md` (Clock line above)
  - `01_Gradable_Surface.json`
  - prior revisions rev1–rev5 under `run_forensics/`
- Inputs missing (not needed for a pre-check):
  - `07_Baseline_Trajectories/`
  - `10_Baseline_Verifier_Results.md`
  - `12_Difficulty_Stats.txt`
  - `08_Oracle_Events.md`, `09_Rubrics.json`
- **Validity** (`trajectory_ledger.py`):
  - stream-json, status completed, final result event 678, no compaction, no events after the result
  - models `claude-opus-5-5` / `claude-opus-5-5[1m]`, mixed=False, `v3_valid=True`, 0 subagents, 0 briefs
  - counted calls 263 (the `/hardness` report's raw count is 273, including 3 errored calls and the Bash helpers)
  - binding **BOUND: rev6** on discriminating content (the seven-revision `--sql` set, rev1–rev6)
- **Intake results:**
  - Proposals and dispositions: 23 proposals, all dispositioned (section 4) and reviewed; review queue event 474 read in full.
  - Deliverable diff: `surface_grader`, coverage 77/77, score **100 %**, 0 failed slots.
  - Ledger: 23 records appended (`added 23 · rejected 0`).
  - Posterior forecast: **`hev_858b5d6b82656490`** (UNCALIBRATED). V3 E[avg] 0.868–0.955 across scenarios; P(all four gates) 0.000–0.016.
  - Structured diagnosis: `Working_Files/Mode_B_Diagnosis.json` (`mode_b_report.py`, verdict PASS, scope PROVISIONAL_SINGLE_PRECHECK) from `Working_Files/mode_b_request.json`; matrix `run_forensics/rev6/precheck.mode_b_matrix.json` (23 surface slots, raw = corrected, no judge corrections), receipt `run_forensics/rev6/precheck.export_review.json`. Heavy all-pass: S-K1a, S-K3a, S-K4a, S-K5a, S-H1, S-G1, S-G2; all-fail: none. Repairs mirror §9–§11; the added ~20-session cohort is classed missing-data volume, not a difficulty repair.
  - Tool refresh (2026-11-08): `trajectory_ledger/2` and `node_verdicts` re-run on rev1–rev6; calls, writes, briefs, proposals and node verdicts are byte-identical to the earlier run (only the tool version and binding-candidate order changed). The 23 dispositioned records are already in the ledger; none re-appended.
- **Go / no-go: NO-GO.**
  - `/hardness` = 1 (needs ≥ 3).
  - Corrected proxy 100 % (needs ≤ 80 %).
  - Independent loss channels failed: 0 (needs ≥ 2). The go-rule tally is 0.
  - The forecast had to run with `--no-channels`. The declared `delegation:handling` channel's ledger records are on a `run` basis while the channel declares a `batch` latent. The run had no briefs, so this is disclosed and left for S0r to correct in the manifest declaration.

## 2. Gate status

Pre-check only: no six-run statistics exist. Not applicable.

## 3. Predicted `/hardness` band (B3c)

Observed, not predicted: the platform report scored **1**. The requirement map is reproduced from that report, sections 4–6. R1–R16 are all MET, with step citations matching our ledger:

| Item | Event |
|---|---|
| Register write | 474 |
| Memo create | 493 |
| Memo move | 495 |
| Memo share | 497 |
| Thread reply | 673 |
| Brian post | 675 |
| Ticket updates | 61 (one ECONNRESET retried) |
| Re-run comments | 21 |

Neighbour argument for 2: a 2 needs a minor gap, and there isn't one. Every verdict, state, comment and figure matches the truth. Score 1 stands.

## 4. Designed-difficulty register (node verdicts, run `precheck`)

| Node | Mechanism | Deciding record | Verdict | Evidence (run · event) | Disposition |
|---|---|---|---|---|---|
| R_K4 Brian's group is game industry | A18 | Brian's Turkish DM reply (D076RBM29JS 1758659012.418207) + Leonard L697 | LEAKED | opus · event 474 (ZOM-568–576 "not counted, game industry"); found by searching "Kadıköy" copied from the notes docs (call #92) | accepted |
| R_K3 Samsung pass is editor-only | A24 done_gap | Arthur's inline comment on PR #476 (rc_27) vs ZOM-567 Done | LEAKED | opus · event 474 (11 Samsung rows not counted); the gate doc's "Update Sep 30" line led to the PR (calls #106, #110–#113) | accepted |
| R_K5 build 1943 is a dev build | A17 | Leonard's thread reply L701 | LEAKED | opus · event 474; found by searching "0.3.127" (call #107) | accepted |
| R_K1 Claire coached | A13 | Claire's Sep 29 mail to Julia | LEAKED | opus · event 474; broad Gmail sweep `newer_than:30d` (calls #84–#88) | accepted |
| R_F re-run notes on technical drops | A14 | Robert's DM L703 | LEAKED | opus · event 474 + 21 `linear_create_comment` on exactly the 21 technical drops; Leonard's request pointed at it ("Robert already told you") | accepted |
| R_D panel void rule | A19 | Leonard's thread reply L695 | **LEAKED** (tool said BYPASSED) | opus · event 493: the memo states 3.33. The tool only checks the Register, which carries no panel value | corrected BYPASSED→LEAKED |
| R_E install-weighted mature D7 | A15 | Robert's post L705 + Snowflake | **LEAKED** (tool said BYPASSED) | opus · event 493: the memo states 9.09 %, 47 cohorts, 6,040 installs (Snowflake call #178) | corrected BYPASSED→LEAKED |

Per-node counts out of 1 completed run: LANDED 0 · CONFOUNDED 0 · LEAKED 7 · BYPASSED 0 · NOT-REACHED 0. Controls held (11). Channels scale, tool_surface, delegation, chain and synthesis all HELD.

## 5. Per-rollout ledger (precheck)

Full ledger: `run_forensics/rev6/precheck/calls.jsonl`, `writes.json`. Read-path summary:

| Step (call #) | Tool | Input | What came back | Decision |
|---|---|---|---|---|
| 1–7 | slack search/read | #zombie-design, 2 pages + panel thread | Leonard's request L707 (a full index of rule locations), L683–L701 rules | committed to the rule list from the index |
| 8–16 | drive/sheets/slides | "audience sessions", Julia's folder | workbook, criteria deck, gate doc | gate doc's Sep 30 line → PR #476 |
| 17–80 | gdocs get ×62 | every notes doc | build/age/relation per session | brute-forced the cohort |
| 81 | linear list | "Friend session", limit 100 | all 60 tickets | clean inventory |
| 82–88 | gmail | "session", "panel", `newer_than:30d` | every form mail incl. Claire's correction | K1 found |
| 92–94 | slack | "Kadıköy", Robert DM, Brian DM | Brian's Turkish reply | K4 found |
| 104–108 | slack | Robert sessions, "0.3.127", "0.3.40" | Robert's DM rule, L701 | F, K5 found |
| 106–113 | github | "Vision Bot", PR #476 comments (spilled, parsed by python) | Arthur rc_27 editor-only | K3 found |
| 114–172 | linear comments ×60 | every ticket | phone per session | brute-forced |
| 173–178 | slack/snowflake | "pass Samsung", D7 query | no pass; 9.09 % | E met |
| 180–273 | writes | Register, memo, 61 updates, 21 comments, 2 posts | all correct | — |

Skipped: nothing that mattered. Every deciding record is in a result the main thread saw. No calls were left unreviewed: the review queue was event 474, and every write payload was read (493, 673, 675, the comment bodies).

## 6. Friction, tool-defect and horizon checks

- Friction: none configured (`03_Error_Async_Config.txt`).
- Unconfigured errors, none outcome-changing:
  - 2 ECONNRESET (events 196, 505), retried
  - 1 `jq` missing, rerouted to python
  - 1 spilled PR-comment result, parsed from the file
- Horizon: 263 counted calls (long-horizon minimum 100). It met the floor only by brute force: 62 doc reads, 60 comment lists and 61 updates. That is volume, not difficulty (v2 Part 4).

## 7. Verifier sanity

No verifier or rubric yet. The `/hardness` report agrees with our solver on all 60 verdicts.

## 8. Why Opus passed

`hardness_v2_check.py` on rev6:

```
CLEAN SAME_PLACE    7 trap(s) with two or more version records; 0 flagged
CLEAN DONE_CHECK    an A24 / done_gap node exists
CLEAN TWO_DECISIONS cross-source rules decide 7 requirements
FLAG  DECISION_FLIP 4 of 7 rules can flip a weight-5 slot; not: ['R_F', 'R_D', 'R_E']
CLEAN INPUT_CHECK   1 weight-5 total(s); 1 with an input a rule can change
CLEAN FILTER_CHECK  an in-scope item sits outside the obvious filter
CLEAN RULE_IN_PROMPT no run of 8 resolver words in the prompt
```

The checker is CLEAN where the run shows the opposite. It cannot see the following, so it is a blind spot to record:

- **Signposting inside the data.** L707 maps every rule location, and the gate doc's Sep 30 line points at the PR.
- **A "filter" item that sits inside the brute-forced set.**

V2 failure kind per settled trap:

| Trap | V2 failure kind |
|---|---|
| K4 | `on_delegation_path`: the notes docs' odd relation value "Kadıköy ekibi" handed the agent a literal search term (call #92) |
| K3 | `on_delegation_path`: the gate doc's "Update Sep 30 … discussed there" names the PR, and "A closed ticket isn't a pass" defuses the ZOM-567 decoy before it is met (decoy never live) |
| K5 | `first_read`: L701 is a reply in the channel the request sits in, and it lists the store builds verbatim |
| K1 | bulk call carried the answer: `newer_than:30d` returned every mail to Julia, including Claire's correction |
| F | `on_delegation_path`: "Robert already told you how not-counted sessions get handled" |
| D, E | `on_delegation_path`: L707 names the panel thread and "the way Robert set it in the channel after Vincent's post" |

The inventory was brute-forced: the 60 docs, 60 comment lists and 60 log rows are all reachable with one keyword each.

Heavy rows that passed: every weight-5 slot (S-K1a, S-K3a, S-K4a, S-K5a, the call, the thread reply, the Brian post, Register verdicts). These are the parts Opus finds easy, and the rebuilds below add none of them.

Evidence from completed tasks: a forensic subagent read `support/completed_tasks/*` and `learnings`. Mechanisms that beat an exhaustive Opus once it had the text:

1. **Done in one service, missing piece only in a joined second service.** Douglas: PR inline comments joined to the Drive deploy log. 6/6 missed, 17 all-fail rows.
2. **Forward-effective change that the ledger or tie-out cannot show.** Frederick card spend: 6/6 priced at September.
3. **Work already done, recorded in an unrelated container.** Robert winddown: a CodeRabbit comment in an unnamed repo, 6/6.
4. **Inclusion by attribute, not keyword.** Julia ZM ZOM-281, 1/6; Frederick AdMob notice in `minimal` format, 5/6.
5. **A stated binary test softened after reading the evidence.** Robert winddown, 2/6.

Inline PR comments, same-thread corrections, ticket comments, doc bodies and Trello all brute-force at 0 % missed. Placement alone will not beat this reader.

## 9. Purge list (proposed; S0r decides)

| Item | Why | Proposal |
|---|---|---|
| L707 rule index (Leonard's request) | `on_delegation_path` for F, D, E, K-rules; the report's #1 cause | Rebuild: keep only the asks (one call with his casual/RPG/no-lead → hold/keep mapping, memo per the roadmap card, reply here, tell Brian, current game only). Delete "the rules I posted…", "the audience read criteria", "close the tickets the way your log note says", "Robert already told you…", the panel and retention pointers |
| Gate doc "Update Sep 30" line + "A closed ticket isn't a pass." | Points straight at the decider and defuses the decoy | Purge both lines. Restore rev5's "Arthur Blake owns the Vision Bot job and says what a pass does and doesn't cover." |
| Prompt span "and where the rules are" | Same index effect from the prompt | Prompt-side (section 11) |
| K5 / K1 / F / D / E as designed | LEAKED via first-read or bulk; repairable only by de-signposting | Keep as low-cost controls with no added weight. Not counted on for difficulty |

## 10. Proposed rebuilds (S5a candidates; v2 moves only, no added rows or steps)

Each has its own deciding record in a different service. The S0r tuning target is that each one, missed alone, flips the call or a weight-5 count (sim: `scratchpad/s/sim.py`, option A family).

1. **K3 two-sided "done across services" (A24, ranked #1).**
   - Today the safe default ("no pass found → exclude Samsung") is the right answer, so a non-finder still passes.
   - Invert it. Add a real on-device pass:
     - Vincent (QA owner per base Confluence `page_qa_runbook`: "on real devices, not just the emulator", "QA posts the completed matrix in #zombie-bugs") posts on Sep 29 in #zombie-bugs: "0.3.127 (127) regression matrix done, all green, sheet in thread".
     - The matrix Sheet lists the Samsung row only as a model number (SM-A546E, real device).
   - Keep ZOM-567 (Vision Bot green) plus Arthur's editor-only comment as the decoy.
   - Truth: Samsung sessions COUNT (gate: "once there is a pass, it covers all the Samsung sessions"), and none get re-run notes.
   - Miss modes:
     - Stopping at "no pass" excludes the Samsung sessions.
     - Trusting ZOM-567 alone gives the right inclusion for the wrong reason. That's acceptable; the matrix is the decider.
   - Uses base Confluence as a read-only decider. S0r re-tunes the Samsung stars (the game held up, so they're no longer the crash-depressed 2s).
2. **G: inclusion by attribute through Contacts (A13/kind 6, new service).**
   - Notes docs gain "Player: First Last".
   - Julia's Contacts group "ZM playtest players" (gift-code list, created Sep 22) holds each player's job. Most are non-games.
   - Two counted players (not Brian's) have a games job, e.g. "Live ops producer, mobile games studio". Leonard L697 excludes them.
   - No keyword in any doc or ticket. The fact is established per player from Contacts, which is persona-owned and unscoped.
3. **T: items outside the obvious filter (kind 7).**
   - Owen's Sep 30 evening reply in his own form thread reports two more sessions inline (no notes doc, no ticket, no Log row).
   - Julia's log note gains the standing instruction "forms that come in after this batch get a ticket when I see them".
   - Truth: two new tickets, Register rows, and inclusion in the means. The ticket count goes from 60 to 62.
4. **R_E: rule that changes a number (A15 + forward/effective scope).**
   - Robert's retention rule stays in L705.
   - A later, separate correction in Vincent's KPI sheet note or a Linear comment (S0r picks): Calm Play cohorts before the 2025-07-24 transfer are excluded when quoting ZM retention.
   - This changes D7 from 9.09 %. The memo figure becomes weight 5 only if the rubric stage agrees (rubric stage, not here).
5. **Binary test (kind 5 lesson).** No new rule. The criteria deck's lead test (≥ 6 per side, gap ≥ 0.25) already is one. Keep the margins of the truth and of each single-miss outcome off the 0.25 edge (clause-sweep rule).

Volume (requester ask: 400+ calls, all 13 services):
- **Services:** 11 injected (adds `contacts`). Confluence and Snowflake are used as read-only base deciders (`page_qa_runbook`; USER_COHORT_RETENTION). Injected Confluence or Snowflake writes are forbidden: portal Eval 0 Check B, `hg_injection_lint read_only_service`.
- **Calls:** necessary per-session work becomes doc + comments + contact + update ≈ 4 calls per session, plus T's 2 creates and re-run notes. Reaching ≥ 400 honestly needs about 80–85 sessions. Opus measured about 4.4 calls per session at 60 sessions.
- **Recommendation to S0r:** add one more observer cohort of about 20 sessions, all governed by the existing rules, not new traps. That is necessary volume, never padding (tool-call minimum guide). Volume earns no hardness credit (v2 Part 4), so it is planned separately from the traps above.

## 11. Routing (proposed; S0r decides)

- **Universe** → `/create-scenario --revise` (S0r, S5a), then `/create-injection` as **rev7**, then `/injection`. Facts that change:
  - L707 text
  - gate doc text
  - Samsung verdicts (11 → counted) and their stars
  - re-run note set (21 → 10)
  - new Contacts rows and group
  - "Player:" lines in all notes docs
  - Owen's late reply (2 new sessions)
  - the log note sentence
  - the retention correction and the new D7
  - new QA matrix sheet and #zombie-bugs post
  - added cohort
  - the truth: counts, means, call
- **Prompt-side defects:**

| # | Quoted span | Rule (doc §) | Defect | Evidence |
|---|---|---|---|---|
| P1 | "his message lays out what he needs and where the rules are" | 6_Prompt Writing Guidelines §06; Hardness v2 Part 8 | Tells the agent the request is a rule index. Discovery collapses to a fetch | precheck · calls #4–#16 follow L707's pointers in order |

  Proposed wording: "his message says what he needs." The rules stay incorporated through Leonard's request and his posts as the requester. `prompt-incorporation-v1` is satisfied because the request names the deliverables and Leonard's own dated posts govern.
- **OE / rubric:** none exist yet. After rev7, plan two atomic weight-5 rows per trap: verdict plus state, or verdict plus count.

## 12. Self-review

Counter-readings (each LEAKED verdict, plus the band), resolved with a pointer:

| # | Verdict | Counter-reading (strongest argument against it) | Resolution and evidence |
|---|---|---|---|
| 1 | R_K4 LEAKED | Counter: the trap was never live, because the notes docs hand over the search term | Partly true. The odd relation value "Kadıköy ekibi" in all 9 docs (L138–L154) gave the literal query; Brian's reply L691 sits in the DM D076RBM29JS, not on first read. Live but leaked → rebuild by attribute (G, §10.2) |
| 2 | R_K4 LEAKED | Counter: Opus would fail without the DM | The DM is the only decider; L697 alone doesn't name the group. Opus searched it (call #92) → genuine capability, not tool luck |
| 3 | R_K3 LEAKED | Counter: the ZOM-567 decoy was never live | True. "A closed ticket isn't a pass" (L134) defused it before Opus met it. FALSE as built → purge the line (§9) and make it two-sided (§10.1) |
| 4 | R_K3 LEAKED | Counter: the PR comment was reached only through the gate doc's Sep 30 pointer | True. The L134 "Update Sep 30" line names the PR; on_delegation_path → purge |
| 5 | R_K5 LEAKED | Counter: the correction was in the same place | L701 is a reply in C090N54TG79, the request's channel, and lists the store builds verbatim: first_read. Live but weak; kept as a control |
| 6 | R_K5 LEAKED | Counter: Opus could have failed by trusting the form | Robert's form mail (L294) gives no build; the docs carry "(1943)". No conflicting decoy existed, so there was no way to fail |
| 7 | R_K1 LEAKED | Counter: a bulk call carried the answer | True. `newer_than:30d` returned Claire's correction with every form mail (calls #84–#88). Kept as a control |
| 8 | R_K1 LEAKED | Counter: the correction was met before the claim | No. The form (claim) and the correction came back in one batch; same-batch, which Hardness_Mastery §13 calls first_read |
| 9 | R_F LEAKED | Counter: it was trivially satisfied through delegation | True. L707 said "Robert already told you"; D05GU6L0XFH read at call #93. FALSE as designed → purge the pointer |
| 10 | R_D LEAKED | Counter: the tool said BYPASSED, so it was off-path | No. Memo event 493 states 3.33 per L695. Corrected to LEAKED; reached through the L707 pointer |
| 11 | R_E LEAKED | Counter: a bulk Snowflake query would pass anyway | Partly. One query (call #178) gives 9.09 % once L705 is read; L707 pointed to L705. Rebuild with a later correction (§10.4) |
| 12 | Band 1 | Counter: argue for band 2 (any minor gap?) | The grep of the write payloads (writes.json) found no missed flag: 21 comments on exactly the technical drops, memo figures = solver, folder d_8140f09bf9f1b94cb8ee2d correct. Band stays 1 |
| 13 | Go rule | Counter: the forecast without channels understates difficulty | Channels HELD in node_verdicts (precheck.node_verdicts.json); adding them could only lower P(fail). NO-GO stands |
3. **Facts re-verified** against the SQL lines quoted from rev6:
   - L134 (gate doc text)
   - L707 (request)
   - L691 (Brian's Turkish reply)
   - L676 (Arthur rc_27)
   - L701 (1943 reply)
   - L703 (Robert DM)
   - L705 (retention rule)

   Base Confluence `page_qa_runbook` was confirmed in `Universe_SynthCut/.../confluence/confluence_working.json` ("on real devices, not just the emulator"; "QA posts the completed matrix in #zombie-bugs").
4. **Mechanical checks:**
   - `trajectory_ledger`, `node_verdicts`, `surface_grader`, `hardness_v2_check` and `hardness_forecast` were run on the bound revision; outputs are quoted above.
   - No difficulty_stats run: there's no six-run matrix.
5. **Unresolved:**
   - The forecast's delegation channel basis (run vs batch) needs S0r to fix the manifest declaration.
   - The 400+ call target depends on the cohort-size decision in S0r.

## 13. Next steps

1. `/create-scenario --revise` (S0r): disposition this report and pick the rev7 traps and numbers. S0r tunes stars so each single miss flips the call or a weight-5 count, with margins off 0.25, and runs the clause sweep.
2. `/create-injection` → rev7 SQL, solver and truth, dossier and lints (sql_lint, base_check incl. forward_references, hardness_gate, hg lint). Then `/injection`.
3. Prompt: apply P1. Run `/prompt`.
4. Re-inject, run a new unhinted Opus pre-check, then `/hardness`. Stop rule: this is pre-check 1 of 2 for this scenario. After a second miss, change the scenario.
