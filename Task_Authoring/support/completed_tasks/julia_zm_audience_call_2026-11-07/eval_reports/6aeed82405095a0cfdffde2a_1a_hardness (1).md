## HARDNESS REPORT (Opus observed)

### Task: Julia closes out Leonard's friend-session audience read (80 logged sessions plus Owen's 2 late ones) and posts the keep/hold call on the cards-earlier change

## 1. Scope

- Stage: `/hardness`, chat review, audit mode. Review date: 2026-11-09T12:49Z.
- Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
- Universe: `Universe_SynthCut` (hg4-synth-sep30cut v16), manifest `Evals/references/universes/synthcut/universe_manifest.json` (SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a`).
- Selected spec: `Evals/1A_Hardness_Eval.md` (SHA-256 `576f18709fddd835a5d63d13a31167b36e14fb828342a7e8eb206669961fe627`), assessment version model-aware-v3, WORKFLOW SHA-256 `d5702ee24b3995a980f417ef930545801bf894f0d7c22279432e8d87d2573e33`.
- Assignment (platform record, `00_Task_Assigned_Inputs.md`, SHA-256 `2bd41165…1c6d`): Julia Lawson, Product Manager; Product; Marketing and GTM; Analysis and synthesis; **long-horizon**; difficulty mode **medium**.
- Inputs reviewed:
  - Prompt `04_Prompt.txt`, 672 bytes, SHA-256 `c3da944d7da5a32891a9c1e06664e6111bb3bccd1a1efe31bb0c713f7b795088`.
  - Injection SQL `01_Universe_Inject.sql`, 362,887 bytes, SHA-256 `ffec30c85dd7b5a27d4e6dc3adbb5bfcae85d34ca8a34e4d8a6ef64975d30443` (read as a proposed overlay, never executed).
  - Opus run `Evals/task_inputs/opus/trajectory.json` (upload `trajectory-run-1.json`, saved as opus revision 11 for this review), 2,586,750 bytes, SHA-256 `bc8509fbcd8e128968094afb140e1966c2b4f753eb8b9d03b21f94e156a61e58`. It replaces the earlier run (`6bc69281…`), which was against an older prompt/SQL.
  - Reference files: none referenced by the prompt; none supplied.

## 2. Input / authority issues

- **Model:** confirmed Opus from the export: init `model: claude-opus-5-5[1m]`, every assistant message `model: claude-opus-5-5`, result `modelUsage` canonicalModel `claude-opus-5-5`. Session `b4299472-73bb-4554-9fe9-935af9c71136`, Claude Code 2.1.280, 327 turns, `terminal_reason: completed`, `is_error: false`.
- **Task and source match:** the export starts at the system init and does not include the opening user turn. Match is established from behavior: the first calls look for #zombie-design and read Leonard's 2025-09-30 21:10 UTC request (SQL L889); the run sees 80 tickets ZOM-568–647 and Owen's late Sep 30 mail (SQL L434), which exist only in the current SQL revision (the earlier revision had 60 sessions). It produces exactly the prompt's five deliverables.
- **Unhinted:** no hint text appears anywhere in the export; progress notes (`idx 23, 235, 431`) show it discovering the rules by search. Treated as unhinted. Limit: without the opening turn the prompt text the run received cannot be byte-matched.
- **Evidence reuse (stage-evidence-v1):** the expected outcome is REUSED from the current `/prompt` report (`1_prompt.md`, PASS; same prompt SHA `c3da944d…` and SQL SHA `ffec30c8…`, ledger section 4 "Counting" and UGT readings A–I). The deciding records were re-read NEW for this review: gate doc L174, log note L176, Claire's form L452 and Sep 29 mail L508, Leonard L865/L877/L879/L881/L883/L889, roadmap card L859, panel forward L368, panel rule L875, Robert's retention rule L887, KPI note L346. The run's own RPG total with Claire's 13 included (123.5/31 = 3.98) matches the report's reading D exactly.
- `input_manifest.json` was not updated: this review's writer path covers the report only; provenance is recorded here.
- authority_contract: prompt-incorporation-v1. Incorporated: Leonard's request (L889, "his message says what he needs"), the feedback note and its posted amendments (the prompt names "his feedback note"), the roadmap card via the request. Robert's re-run-note DM and the log note's "gets a ticket and a log row" are **not** incorporated (per the `/prompt` ledger) and are not scored either way.

## 3. Checklist

| Item | Status |
|---|---|
| Task date / universe | REUSED saved selection, synth-cut |
| Inputs listed, new run saved under `opus` | NEW |
| Model, task match, hint status | NEW (Opus confirmed; opening turn missing, noted) |
| EXECUTION, ENVIRONMENT, UNIVERSE_MAP, 1A, shared guide | NEW (1A and shared guide read in full) |
| Requirement map | NEW |
| Expected outcome | REUSED from `/prompt` ledger (matching hashes), deciding records re-read NEW |
| Every write checked against expected outcome | NEW (Log append, Register payload 82 rows, 83 ticket updates, 2 tickets created, 2 comments, memo body + edit, folder move, 2 shares, 2 Slack posts) |
| Search coverage for the missed records | NEW (every Gmail search result list and the channel read inspected) |
| Narrow-miss, failure-pattern, tool-call lines | NEW |

## 4. Requirement map and observed outcomes

Expected outcome (`/prompt` ledger, matching hashes): 45 counted of 82: casual 27 (sum 103.5, mean 3.833), RPG 18 (sum 63, mean 3.500); gap 0.333 ≥ 0.25, both ≥ 6 → **casual lead → hold**; the tutorial and level order work does **not** go on. 37 logged sessions not counted: 11 game industry (Brian's 9 ZOM-568–576, ZOM-598, ZOM-622), 13 dev build 1943 (ZOM-577–586, 632, 637, 645), 13 coached (Claire, ZOM-607–619). Samsung sessions count (Vincent's Sep 29 matrix, SM-A546E, 0.3.127 (127)). Owen's 2 late sessions join. Logged tickets: 43 Done, 37 Canceled. Memo context: panel 3.33 (player 8 void), retention 10.47% install-weighted D7.

| # | Requirement (source) | Expected | Observed (trajectory) | Outcome |
|---|---|---|---|---|
| R1 | Find Leonard's request and its sources (prompt; L889; roadmap card L859) | Request, criteria deck, log note, gate doc, card | Request read at `idx 8–9`; criteria deck `idx 49`; workbook `idx 24–27`; card and log note found | MET |
| R2 | Game-industry exclusion (Leonard L877/L879; Brian DM; contacts) | 11 out | ZOM-568–576, 598, 622 "not counted, works in games" (Register payload `idx 581`) | MET |
| R3 | **Coaching exclusion** (Leonard L881: "a coached session doesn't count… that goes for sessions already run too"; Claire's Sep 29 mail L508 "Before anyone touched their phone I sat them all down and took them through how ZM plays", overriding her Sep 26 form L452 "No coaching") | Claire's 13 (ZOM-607–619) out | All 13 marked **counted** (`idx 581`). The run never retrieved L508 or L881: its only Gmail searches (`idx 247` "friend sessions OR Vision Bot OR feedback note", `idx 476` "vision OR samsung…") returned 19 and 0 messages, none of them L508; its channel read (`idx 8`, 30 newest messages, `has_more: true`) stops at Sep 29 and was never paged; no Slack search hit L881. The memo states "All 82 sessions report no coaching" (`idx 584`). | **MATERIAL_FAIL** |
| R4 | Dev build exclusion (gate doc L174; Leonard L883) | 13 on (1943) out | All 13 "not counted, Dev build" (`idx 581`) | MET |
| R5 | Samsung gate (gate doc; Vincent matrix; ZOM-567 decoy) | 13 Samsung sessions count | All counted on the SM-A546E matrix pass; Vision Bot ZOM-567 explicitly not relied on (`idx 581`, memo `idx 584`) | MET |
| R6 | Owen's late form (log note L176; mail L434) | 2 sessions join the read | ZOM-648/649 created and counted, Log rows appended (`idx 568–576`); resend from Marcus correctly not double-counted | MET |
| R7 | Relation and age (L879, L865) | Family/neighbours/classmates kept; 25–45 | Kept (`idx 581`); memo notes all players 26–44 | MET |
| R8 | Read the lead (criteria deck) | Casual 27 @ 3.83 vs RPG 18 @ 3.50, gap 0.33 → casual lead | Casual 27 @ 3.83 (correct) vs RPG **31 @ 3.98**, gap 0.15 → "no clear lead" | MATERIAL_FAIL (same cause as R3) |
| R9 | Fill Register tab | 82 rows, correct verdict and reason | `gsheets_values_update` Register!A3, `updatedRows: 82` (`idx 581`); 69 of 82 verdicts correct, 13 (Claire's) wrong | MATERIAL_FAIL on 13 rows (same cause) |
| R10 | Memo: call and numbers, panel and retention as context, in Julia's folder (L859) | Hold; 27 vs 18; 3.83 vs 3.50; gap 0.33; panel 3.33; retention 10.47% | Doc created (`idx 584`), corrected (`idx 591`), moved to `d_8140f09bf9f1b94cb8ee2d` (`idx 593`), shared with Leonard and Robert. Call "KEEP", RPG 31 @ 3.98, gap 0.15 | Placement MET; call and numbers MATERIAL_FAIL (same cause) |
| R11 | Panel context (Leonard L368 per-player stars; L875 void rule) | 30/9 = 3.33, player 8 out | "Playtestcloud is still at 3–3.5 stars" (from a Sep 22 Slack line). L368 never retrieved (not in either Gmail result list) | MINOR_GAP |
| R12 | Retention context (Robert L887: install-weighted D7, mature cohorts with D14, pooled; KPI note L346 cohort cutoff 2025-07-24) | 10.47% over 16 rows from 2025-07-28 | "September cohorts… D7 10.4%, flat against August… 10.5%" from a query of cohorts ≥ 2025-08-01 (`idx 559`); Robert's method not applied | MINOR_GAP |
| R13 | Close tickets per log note (counted → Done, not counted → Canceled) | Logged: 43 Done, 37 Canceled | 82 final states: 58 Done, 24 Canceled; the 13 Claire tickets set **Done**; the rest match. One connection error on ZOM-587 retried successfully | MATERIAL_FAIL on 13 tickets (same cause) |
| R14 | Reply in Leonard's thread with keep or hold | "hold" in thread `1759266627.418203` | `slack_send_message` thread_ts 1759266627.418203, "**Keep.**" `ok: true` (`idx 777`) | **MATERIAL_FAIL** (same cause) |
| R15 | Tell Brian in #zombie-design whether the tutorial and level order work goes on | Does not go on | "@Brian the tutorial and level order work goes on… please carry on with it" `ok: true` (`idx 779`) | **MATERIAL_FAIL** (same cause) |
| R16 | One call, not a maybe; honest final response | Single correct call | Single call, but the wrong one; the final response repeats "keep" and claims robustness ("No reading of the sessions produces a casual lead"), which is false once Claire's sessions are dropped | MATERIAL_FAIL (same cause) |

**Output capability:** every required write path was SUPPORTED and succeeded (Sheets append/update, Docs create + batch update, Drive move/share, Linear create/update/comment, Slack send). No capability or environment defect affected the result.

## 5. Grouped failures and independent causes

- **Cause 1 (material): Claire's coaching correction never found.** Deciding record: Claire Morgan's 2025-09-29 mail "a small thing from Friday" (SQL L508, Julia's inbox), read with Leonard's coaching amendment (SQL L881, #zombie-design, Julia is a member). Both were discoverable and visible to Julia; the run's Gmail queries were keyword-narrow and its channel read was never paged. It trusted Claire's Sep 26 form and the tickets' "Coaching: none reported". Affected outputs: 13 Register verdicts, 13 ticket states, the RPG count/mean and gap, the memo's call, the thread reply (keep instead of hold), the post telling Brian to carry on, and the final response. One cause, many affected outputs; counted once.
- **Minor, separate:** the panel (R11) and retention (R12) context figures rest on records the run never retrieved (L368/L875; L887/L346). They are context only ("Sessions decide. Panel and other numbers are context.", criteria deck) and their values are close to expected (3–3.5 vs 3.33; 10.4% vs 10.47%), so they stay MINOR_GAP.
- **Independent material causes: 1.**
- Task/environment defects: none found that affected the run.

## 6. Narrow-miss, failure-pattern and tool-call lines

- **Narrow miss: NO.** 1 independent material cause, but the failed share is about **45–50%** (well above the medium loss of 15%). Basis: 15 weighted core items (thread call 5, Brian post 5, memo call and numbers 5, RPG count/mean 3, coaching exclusion 3, Register 3 with 13/82 wrong, tickets 3 with 13/80 wrong, panel 1 and retention 1 minor, plus the right items: memo placement 3, game industry 3, dev build 3, Samsung 3, Owen 3, casual count/mean 3); about 22 of 47 weight points wrong. Difficulty mode medium, loss 15%. The narrow-miss rule needs a share below 15%, so the band table applies.
- **Failure-pattern risk: YES.** Traps, each with its own deciding record, and this run's result:
  - Claire's coaching correction (L508 + L881): **wrong**. Flips the call (RPG 31 @ 3.98, gap −0.15 → keep). Share ≈ 50%.
  - Game-industry players (L877, Brian DM, contacts): right. Flips the call if missed. Share ≈ 45%.
  - Dev build 1943 (L883 + gate doc): right. Flips the call. Share ≈ 45%.
  - Samsung pass via Vincent's matrix (gate doc + matrix; ZOM-567 decoy): right. Flips the call. Share ≈ 45%.
  - Owen's late sessions (log note L176 + mail L434): right. Flips the call. Share ≈ 40%.
  - Relation widening (L879): right. Flips the call. Share ≈ 45%.
  - Panel void (L368/L875): wrong, ≈ 2%. Retention method (L887/L346): wrong, ≈ 2%.
  - Largest trap share ≈ 50%. Every one of the six main traps alone decides the keep/hold call and both Slack posts, so runs that miss any one of them fail the same block of rows.
- **Tool calls: 326** (326 main agent, 0 sub-agents; both count). Task type long-horizon, minimum 100 on average; not under 90% of the minimum (90).

## 7. Correct work and usability

Substantial work is correct: Owen's late sessions found, ticketed and counted; the Samsung trap resolved correctly with the ZOM-567 decoy rejected; all 13 dev-build sessions and all 11 game-industry players excluded with accurate reasons; the relation rule applied; 69 of 82 Register rows and 67 of 80 logged ticket states correct; the memo placed in Julia's folder with the log note. But the one decision Leonard has to act on is wrong and has been posted under Julia's name, and Brian has been told to continue work that should stop. The central delivery is not usable without redoing the count, the memo and both Slack posts.

## 8. Unassessed scope

None material. The prompt text the run received is not in the export (section 2); the run's behavior matches the saved prompt and the current SQL in every deliverable.

## 9. Score rationale

Score 5 (Really hard, PASS): a genuine retrieval failure (Claire's discoverable Sep 29 correction, plus Leonard's coaching amendment, never retrieved) flipped the single call the prompt exists to produce ("he has to act on this, so give him one call"). Hold became keep in the thread reply, the Brian post, the memo and 13 rows and 13 tickets. The eval allows a single root cause that invalidates the central result to score 5. Not 4: score 4 describes substantial correction across a result whose core stays usable. Here the core result (the call and both outbound messages) is wrong and actively harmful, not just in need of correction. Not 2: the failed share (≈ 45–50%) is far above the medium loss of 15%, so the narrow-miss rule does not apply. The tool-call count (326) clears the long-horizon minimum.

### FINAL VERDICT: PASS
Assessment version: model-aware-v3
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Assessed model: Opus
Assessment mode: OPUS_OBSERVED
Score: 5
Execution status: COMPLETE
Difficulty: Really hard
Gate decision: PROCEED
Gate reason: OBSERVED_OPUS_FAILURE
Evaluator model: Opus 5.5 (claude-opus-5-5), effort not reported by runtime
Next action: Proceed with dependent authoring (/oe, then /rubric); keep the observed failure evidence. Consider the failure-pattern warning: six traps each flip the same call.
Evidence limits: One run only; no average-score or repeatability claim. The export omits the opening user turn, so the prompt text the run received is matched by behavior, not byte for byte.
