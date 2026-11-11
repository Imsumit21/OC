## HARDNESS REPORT (Opus observed)

### Task: Julia closes out Leonard's friend-session audience read (60 sessions) and posts the keep/hold call on the cards-earlier change

## 1. Scope

- Stage: `/hardness`, chat review, audit mode. Review date: 2026-11-08T16:31Z.
- Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
- Universe: `Universe_SynthCut` (hg4-synth-sep30cut v16), manifest `Evals/references/universes/synthcut/universe_manifest.json` (SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a`).
- Selected spec: `Evals/1A_Hardness_Eval.md` (SHA-256 `576f18709fddd835a5d63d13a31167b36e14fb828342a7e8eb206669961fe627`), assessment version model-aware-v3, WORKFLOW SHA-256 `d5702ee24b3995a980f417ef930545801bf894f0d7c22279432e8d87d2573e33`.
- Assignment (platform record, `00_Task_Assigned_Inputs.md`, SHA-256 `2bd41165…1c6d`): Julia Lawson, Product Manager; Product; Marketing and GTM; Analysis and synthesis; **long-horizon**; difficulty mode **medium**.
- Inputs reviewed:
  - Prompt `04_Prompt.txt`, 724 bytes, SHA-256 `729d3623902ef87c67c5350fa319d715a57d65f45aecc62c03c2b0c2fbb053cc`.
  - Injection SQL `01_Universe_Inject.sql`, 259,393 bytes, SHA-256 `16f9657c587a0b1e8821585cb0288a64e071594d84eea875e5e6a8d7269df68e` (read as a proposed overlay, never executed).
  - Opus run `Evals/task_inputs/opus/trajectory.json` (upload `trajectory-run-1 (1).json`), 3,035,039 bytes, SHA-256 `6bc69281f37306108dd7604637fee3f6bfdf14aadab6d891d5f922ef178a26c9`.
  - Reference files: none referenced by the prompt; none supplied.

## 2. Input / authority issues

- **Model:** confirmed Opus from the export: init `model: claude-opus-5-5[1m]`, every assistant message `model: claude-opus-5-5`, result `modelUsage` canonicalModel `claude-opus-5-5`. Session `bd922189-b478-45e7-bee7-8dec1b5b7bae`, Claude Code 2.1.280, 274 turns, `terminal_reason: completed`, `is_error: False`.
- **Task match:** the export does not include the opening user turn (it starts at the system init). Match is established from behavior: the first call searches for `#zombie-design`, the run finds Leonard's 2025-09-30 21:10 UTC message (SQL L707) and produces exactly the prompt's five deliverables (Register tab, memo in Julia's folder, 60 ticket close-outs, thread reply to Leonard, post to Brian). Every record it read is from the saved SQL overlay or base, so the overlay was live in the run's environment.
- **Unhinted:** no hint text appears anywhere in the export; the run's progress notes (`idx 27, 105, 195, 231, 255, 273`) show it discovering each rule by search. Treated as unhinted. Limit: the missing opening turn means the exact prompt text the run received cannot be byte-matched.
- **Evidence reuse (stage-evidence-v1):** the expected 60-session outcome was recomputed NEW for this review from the current SQL (notes docs: build/age/relation/observer; ticket comments: phone; Log tab: audience/stars). It agrees with the `/prompt` report's ledger for the same prompt and SQL hashes. The panel (3.33) and retention (9.09%, 47 cohorts, 6,040 installs) figures are REUSED from the `/prompt` report ledger (`1_prompt.md`, prompt/SQL hashes identical) and cross-checked against the run's own Snowflake result (`snowflake_execute_query` result: `D7_WEIGHTED 9.088`, `COHORTS 47`, `INSTALLS 6040`).
- `input_manifest.json` was not updated: this review's writer path covers the report only; provenance is recorded here.
- authority_contract: prompt-incorporation-v1. Leonard's message (SQL L707) is incorporated by the prompt ("his message lays out what he needs and where the rules are. can you do all of it"); it in turn names the post-note rule posts, the audience read criteria deck, the log note, Robert's DM, the roadmap card, the panel forward/thread and Robert's retention post. No unincorporated policy was used.

## 3. Checklist

| Item | Status |
|---|---|
| Task date / universe | NEW, SELECTED synth-cut |
| Inputs listed, run saved under `opus` | NEW |
| Model, task match, hint status | NEW (Opus confirmed; opening turn missing, noted) |
| EXECUTION, ENVIRONMENT, UNIVERSE_MAP, 1A, shared guide | NEW |
| Requirement map | NEW |
| Expected outcome recomputed from SQL (60 sessions) | NEW |
| Every write checked against expected outcome | NEW (register payload, 61 ticket updates, 21 comments, memo body, folder move, 2 Slack posts) |
| Narrow-miss, failure-pattern, tool-call lines | NEW |

## 4. Requirement map and observed outcomes

Expected outcome (recomputed from SQL): 17 counted (casual 9: ZOM-595, 600, 602, 605, 621, 622, 625, 626, 627 = 34.5/9 = 3.833; RPG 8: ZOM-589, 592, 597, 598, 599, 604, 623, 624 = 27/8 = 3.375); gap 0.458 ≥ 0.25, both ≥ 6 → casual lead → **hold**. 43 not counted: 9 game industry (Brian, ZOM-568–576), 13 coached (Claire, ZOM-607–619), 10 dev build 0.3.127 (1943) (Robert, ZOM-577–586), 11 Samsung with no on-device pass (ZOM-587, 588, 590, 591, 593, 594, 596, 601, 603, 606, 620).

| # | Requirement (source) | Expected | Observed (trajectory) | Outcome |
|---|---|---|---|---|
| R1 | Find Leonard's request and his rule sources (prompt; SQL L707) | Request + post-note rules L683/L693/L697/L699/L701, criteria deck, log note, Robert DM, roadmap card | Found request and channel rules by `idx 27`; read criteria deck, gate doc, log note, Trello card, Robert DM (`idx 273`) | MET |
| R2 | Game-industry exclusion (Leonard L697; Brian DM) | Brian's 9 out | Register rows ZOM-568–576 "not counted, Game-industry player… (Brian, DM Sep 23)" (`idx 474`) | MET |
| R3 | Coaching correction (feedback note; Claire's Sep 29 mail overriding her "no coaching" form) | Claire's 13 out | Decoded Claire's mail (`idx 214`); ZOM-607–619 "not counted, Coached" (`idx 474`) | MET |
| R4 | Dev build exclusion (gate doc L134; Leonard L701) | Robert's 10 on (1943) out; (127), 0.3.38, 0.3.40 fine | ZOM-577–586 "not counted, Dev build" (`idx 474`) | MET |
| R5 | Samsung device gate (gate doc L134; Arthur PR #476 comment, editor-only; ZOM-567 Done decoy) | 11 Samsung sessions out | All 11 "not counted, Samsung device… Vision Bot pass is editor-only" (`idx 474`); ZOM-567 not treated as a pass | MET |
| R6 | Relation rule (Leonard L699: family, neighbours, classmates count) and age band 25–45 | 9 family/neighbour/classmate counted sessions kept | All kept as counted (`idx 474`) | MET |
| R7 | Labels and lead (criteria deck L272) | Observer label as recorded; mean over counted; ≥6; gap <0.25 = no lead | Casual 9 at 3.83, RPG 8 at 3.38, gap 0.46 (`idx 493`, `idx 673`) | MET |
| R8 | Fill Register tab (workbook L262 header: ticket, audience, stars, verdict, reason) | 60 rows, correct verdicts with reasons | `gsheets_values_update` Register!A3, 60 rows × 5, `updatedRows: 60` (`idx 474`); all 60 verdicts match expected | MET |
| R9 | Memo with the audience call and numbers, panel and retention as context, in Julia's folder with the log note (Trello L679; log note parent `d_8140f09bf9f1b94cb8ee2d`, SQL L6) | Casual/hold, 9 vs 8, 3.83 vs 3.375, gap, panel 3.33, D7 9.09% | Doc `6f9ba27e17d663966b84e633` created (`idx 493`) with all figures and exclusions; moved to `d_8140f09bf9f1b94cb8ee2d` (`idx 495`); shared with Leonard (`idx 497`) | MET |
| R10 | Panel read (Leonard L695: one number per player, void out of sum and count) | 30/9 = 3.33 | 3.33, player 8 void (`idx 493`) | MET |
| R11 | Retention (Robert L705: install-weighted D7, mature cohorts with D14, platforms pooled) | 9.09% | 9.09%, 47 cohorts, 6,040 installs; simple mean 8.69% flagged as not to quote (`idx 493`) | MET |
| R12 | Close tickets per log note (L136: counted → Done, not counted → Canceled) | 17 Done, 43 Canceled | 60 successful `linear_update_issue` results; every final status matches expected. One ECONNRESET on ZOM-589 was retried successfully | MET |
| R13 | Re-run notes per Robert's DM (L703: technical drop → re-run note; other drops just closed) | Comments on the 21 build/device drops only | 21 `linear_create_comment` calls, exactly on ZOM-577–586 and the 11 Samsung tickets; none on Brian's or Claire's | MET |
| R14 | Reply in Leonard's thread with keep or hold (L707) | "hold" in thread `1759266627.418203` | `slack_send_message` C090N54TG79, thread_ts 1759266627.418203, "**Hold.**…" `ok: true` (`idx 673`) | MET |
| R15 | Tell Brian in #zombie-design whether tutorial/level order work goes on | Work does not go on | Top-level post @Brian "The tutorial and level order work for it does not go on" `ok: true` (`idx 675`) | MET |
| R16 | One call, not a maybe; final response | Single call, honest summary | Single "hold" with reasons; final response accurate to the writes | MET |

**Output capability:** every required write path was SUPPORTED and succeeded in the run (Sheets update, Docs create + Drive move, Linear update/comment, Slack send).

## 5. Grouped failures and independent causes

No MATERIAL_FAIL or MINOR_GAP outcomes. Independent causes: 0. The single ECONNRESET on ZOM-589 was an environment blip the run recovered from; it is not a model failure and left no effect.

Task/environment defects: none found that affected the run.

## 6. Narrow-miss, failure-pattern and tool-call lines

- **Narrow miss: NO** (0 independent causes; failed share 0% over 16 core items; difficulty mode medium, loss 15%). Not applicable: the run made no material miss, so the score comes from the band table.
- **Failure-pattern risk: YES.** Traps (each with its own deciding record), all got right by this run:
  - Brian's game-industry group (Brian DM + Leonard L697): flips the call if missed (RPG 4.15 → keep). Share ≈ 45%.
  - Claire's coaching correction (Sep 29 mail vs her Sep 26 form): flips the call (RPG 4.17 → keep). Share ≈ 50%.
  - Robert's dev build 1943 (Leonard L701 + gate doc): flips the call (casual 3.11 → keep). Share ≈ 45%.
  - Samsung device pass (gate doc + Arthur's PR #476 comment vs ZOM-567 Done): flips the call (casual 3.03 → keep). Share ≈ 45%.
  - Re-run note rule (Robert DM L703): ≈ 5%. Panel void (L695): ≈ 3%. Retention weighting (L705): ≈ 3%. Relation widening (L699): would drop 9 counted sessions; ≈ 20%.
  - Largest trap share ≈ 50% (Claire's coaching correction). Each of the four main traps alone decides the keep/hold call, the thread reply, the Brian post and the memo headline.
- **Tool calls: 273** (273 main agent, 0 sub-agents; both count). Task type long-horizon, minimum 100 on average; not under 90% of the minimum (90).

## 7. Correct work and usability

The whole result is correct and usable as delivered: the call (hold), the 17/43 split with the right reason per session, the means and gap, all 60 register rows, all 60 ticket states, the 21 re-run comments and no extra ones, the memo in the right folder with the right context figures, and both Slack posts in the right places. The run also flagged that the exclusions decide the call, which is accurate and useful to Leonard.

## 8. Why this run found every trap (advice for revision)

Read against "Making a Task Hard for Opus 5.5":
- **Leonard's request spells out where every rule lives** (SQL L707: the posted rules, the criteria deck, the log note, "Robert already told you", the roadmap card, the panel thread, Robert's retention post). Hardness guideline, Part 8 warns against spelling out the rules; here the request works as an index that leads the agent straight to each deciding record.
- **The corrections are signposted.** The gate doc's "Update Sep 30: Arthur opened his Vision Bot PR today. What a pass covers gets discussed there" points straight at Arthur's editor-only comment, and "A closed ticket isn't a pass" defuses the ZOM-567 decoy in advance. Claire's correction is a direct mail to Julia. Part 3, 2 (A correction somewhere else) works best when the agent has to find the link itself.
- **The inventory is clean.** All 60 sessions are on the Log tab and in ZOM-568–627, so the obvious search finds every item (Part 4: long inventories and routine bulk writes pass on their own).
- Natural revisions: remove the pointers in Leonard's request and the gate doc's update line (keeping each rule in its own dated record so nothing becomes a fork); put a session just outside the obvious filter (Part 3, 7); add a "done" source with a missing piece or a completion note elsewhere (Part 3, 1 / 9). Then get a new unhinted Opus run.

## 9. Unassessed scope

None material. The exact prompt text the run received is not in the export (see section 2); the run's behavior matches the saved prompt in every deliverable.

## 10. Score rationale

Score 1 (Too easy): the run met every core requirement with no meaningful defect. Not 2: there is not even a minor defect, and no tool-call shortfall. Scores 3–5 need an actual material Opus failure, and none exists.

### FINAL VERDICT: FAIL
Assessment version: model-aware-v3
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Assessed model: Opus
Assessment mode: OPUS_OBSERVED
Score: 1
Execution status: COMPLETE
Difficulty: Too easy
Gate decision: HOLD
Gate reason: INSUFFICIENT_DIFFICULTY
Evaluator model: Opus 5.5 (claude-opus-5-5), effort not reported by runtime
Next action: Revise the task so a correction or rule is no longer signposted (start with Leonard's request and the gate doc's Sep 30 update), add an independent trap in another part of the task, get a new unhinted Opus run and send /hardness again.
Evidence limits: One run only; no average-score or repeatability claim. The export omits the opening user turn, so the prompt text the run received is matched by behavior, not byte for byte.
