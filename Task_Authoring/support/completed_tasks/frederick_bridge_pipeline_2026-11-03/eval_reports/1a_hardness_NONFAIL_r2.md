# /hardness review: Opus observed (model-aware-v3)

## 1. Scope and provenance

- Review: chat review for contributor attempt 6ae4e299a13034b7eb8305f8. Mode `OPUS_OBSERVED`, selected spec `Evals/1A_Hardness_Eval.md`. Review date 2026-11-02.
- Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
- Universe: `Universe_SynthCut/` (hg4-synth-sep30cut v16). Manifest: `Evals/references/universes/synthcut/universe_manifest.json` (archive sha256 `d04f295b…aeb0fb0c`).
- Assignment: Executive / Frederick Stone (Co-founder) / Corporate Ops / Retrieval / long-horizon / difficulty mode medium.
- Inputs reviewed (sha256):
  - Prompt `04_Prompt.txt` (rev 15): `b5ea6f0ff28c9baa2976c08d05edda90dc21774e48d597c572f966efae5317b9`
  - Injection SQL `01_Universe_Inject.sql` (rev 14): `4895577edea84edb71253b2c53e41f0eb638fbbc2d60f04927fc0c84c5c6eef9`
  - Task details: `1d795090d3476539561f58917410dab7275f800863d3be3084150ecd9a383c37`
  - Run `opus/trajectory.json` (rev 16, uploaded as "Run1_trajectory (2).json"): `da7f8dd741eb1ec511a36599cf0b84b1e7a76e460fd93216cf14f11f7d3877ed`. It replaces the earlier saved run (`885ed68d…`), which was made on an older prompt and SQL version. The earlier report's score is not inherited.
- Run identity:
  - The init record has `model: claude-opus-5-5[1m]`. All 143 assistant messages have `claude-opus-5-5`, and `modelUsage.canonicalModel` is `claude-opus-5-5`.
  - Session 148d06ce-…, Claude Code 2.1.280, 91 turns, `terminal_reason: completed`, `is_error: false`.
  - The export is complete: it ends with a final `result` record.
- Unhinted: yes. The export has no hint text. The run found Leonard's email itself (call 1, `gmail_search_messages from:leonard after:2025/09/29`) and found every rule by reading task records. The original user-prompt turn is not in the export. The run's actions match the saved prompt exactly: the Q4 2025 investor update folder, the Existing Investor Update card, the reply on Leonard's thread and the Monday Oct 6 review.
- Task/source match: the run read the SQL rev 14 records. The send-list doc text in call 8 (`f_3b9e61c04d7a52e8f1a6c2`, 3,073 characters) is byte-identical to the SQL rev 14 INSERT. The run also read the README `f_c61a0e93…` ("Q4 update - send list"), the deck `f_a47d0e2c…`, the Trello comment `68c64270…`, the ZOM-567 comments, the Anton DM `99b22482…`/`f7261dd1…` and the contact Edith Vane. So this overlay was live in the run.
- Tool calls: 90. The Long Horizon tier is 100+. That belongs to /prompt and baseline QC; call count is not hardness evidence.
- Evidence contract `stage-evidence-v1`. Reused evidence: none. Every fact below is NEW. Authority contract `prompt-incorporation-v1`.

## 2. Input and authority issues

- None blocking. The model is confirmed, the export is complete, and the SQL overlay is shown to be applied.
- Incorporation chain: the prompt says "His email lays out what he's after". Leonard's email (`<CAxDeR9C…>`, 2025-09-30T21:05Z, read in calls 3 and 5) incorporates the following:
  - the "Q4 update send list doc", with its groups and details;
  - the draft update deck, which shows what each group gets;
  - the folder README, which sets the naming;
  - the Existing Investor Update card ("whatever the card says to do for firms that pass"). The card's comment requires a Keep warm checklist, one item per firm that passed after a call or meeting this round;
  - "reply here with how many firms and angels are in each group";
  - "Let's not" on sending to the whole 2025 list.
- The send-list doc delegates "what counts as signed" to Leonard's #executives note (`20924cc7…`: only a DocuSign Completed notice counts), and build access to "Arthur tracks the tester adds".
- Unincorporated text, treated as distractors only:
  - Robert's 9/29 email ("send it to everyone on the 2025 investor list");
  - Arthur's 9/29 Slack ("just use who Leonard emailed this month");
  - the Q3 send-list doc `f_8d2c47a9…`.
- Snowflake and Confluence play no part in the requirements.

## 3. Requirement map (expected vs observed)

| # | Requirement (source) | Expected | Observed (trajectory) | Outcome |
|---|---|---|---|---|
| R1 | Scope: every 2025-list name (angels included, duplicates merged) plus off-list firms with a pitch call on Fred's calendar since Sep 3 (send-list doc) | Homa (Sep 18 call, co-dev investment path) and Brightwater (injected `evt_2f86b0…`, Sep 25) added. Mattel (RFP only, `398502c0…`), SVB, Rollic, Metaplay, Supercell and Laton excluded | Same (sheet rows; final reply's off-sheet list) | MET |
| R2 | New investor = signed SAFE per the #executives note, with the amount | Anton only, $25K. The $40K was voided (DM `99b22482…`, 9/24), "Anton signed the 25 one" (`f7261dd1…`), DocuSign Completed 9/26 (`<CAiKDPIo…>`). Paul unsigned (9/29 nudge `<CAP6Gn2L…>`) | Anton "New investor", $25,000. Paul "In talks", $50,000 (call 85) | MET |
| R3 | In talks = call on Fred's calendar this round, not passed; angels said yes but unsigned | Firms: a16z, GFR, Dentsu, T-Accelerate, NCsoft, Homa, Brightwater (**7**). Angel: Paul $50K. **SciPlay is not in talks**: it passed (see R5) | 8 firms, **including SciPlay** (call 85, row 9) | MATERIAL_FAIL (F1) |
| R4 | Awaiting reply = our outreach this round, no call, no no | Makers, Initial Capital, Raine, General Catalyst, BBQ, BITKRAFT ("reached out to bitkraft", #bridge-pitch 9/22), Treo (deck 9/3, `19e1e65d…`), Superplay, Sony Mobile, Revo, e2vc, Triptyq, Turkven, Harlem (14) | Same 14 | MET |
| R5 | Keep warm = passed after a call or meeting this round | LVP (call 9/9, written no 9/25), Hiro (call 9/23, Edith Vane's no 9/26) and **SciPlay**. SciPlay's call was Mon Sep 15 1:30 PM PT on Fred's calendar, with Leonard's 9/17 "thank you again for taking the time to chat with us on Monday". Then Robert in #executives, thread reply `229090ba…` (2025-09-30T16:06Z = 9:06 AM PT Sep 30): "Sciplay's out too. D called me this morning, they're passing on this round" | LVP and Hiro only | MATERIAL_FAIL (F1) |
| R6 | Off the sheet: passed without a call, or no contact since Sep 3 | Play (no relayed via Griffin, no call, `c183280a…`), 1AM/March, Grishin, Lakestar, Gorkem's fund (row 69), Transcend and Acterra (plans only), the other list rows with no outreach. Kevin Lin, Mike Fischer and Demetri: no Sep 2025 Slack hits (complete scan) and no Fred-mailbox hits (run call 77) | Same | MET |
| R7 | Build access for firms in talks: iOS only / Android only / iOS and Android / none ("Arthur tracks the tester adds"; the deck: "internal build links they can use") | T-Accelerate: **iOS only**. Dentsu: **iOS only**. Others: none. ZOM-567 says both were added to TestFlight and Play. But Arthur's later #zombie-match3d post `3cddf83c…` (2025-09-30T23:20Z = 4:20 PM PT Sep 30) says the investor tester list "never got attached to the internal testing track, so nobody on it has android yet (Karthic and the 3 Dentsu folks), even though ZOM-567 has them as added. testflight is fine for all of them" | T-Accelerate and Dentsu both "iOS and Android" (call 85, rows 6–7). Others "none". Angels blank | MATERIAL_FAIL (F2) |
| R8 | Sheet: Google Sheet named per README, in Fred's Q4 2025 investor update folder; columns firm, group, amount, build access; only people who get the update | "Q4 update - send list", native Sheets, parent `d_5e8a1c3f9b07d2e64a1b93` | Call 83 created exactly that (success). Call 85 wrote 27 rows × 4 columns (success). Shared with Leonard (call 86) | MET (structure). Row content: see F1 and F2 |
| R9 | Trello: Keep warm checklist on the card, one item per qualifying firm | Checklist "Keep warm" on `68c5a49e…` with LVP, Hiro Capital and SciPlay | Calls 87–89: checklist with LVP and Hiro Capital only (success) | MATERIAL_FAIL (F1) |
| R10 | Reply on Leonard's thread with firm/angel counts per group | New investor 0/1; In talks **7**/1; Awaiting reply 14/0; Keep warm **3**/0 | Call 90 on `<CAxDeR9C…>` (success): 0/1; **8**/1; 14/0; **2**/0. It also says T-Accelerate and Dentsu have "iOS and Android" | MATERIAL_FAIL (F1, F2) |
| R11 | Don't send to the whole 2025 list (Leonard: "Let's not") | Robert's suggestion declined | Declined, and stated in the reply and the final answer | MET |
| R12 | Final response to Fred | Accurate summary of the outputs | Accurately describes what was written, but repeats the F1 and F2 errors | MINOR_GAP (carries F1/F2; not counted separately) |

Reply recipients: `reply_all: true` returned only Leonard as recipient. The prompt asks for a reply on his thread, and Leonard received it. This is not a failure, and the run disclosed it.

## 4. Grouped failures and independent causes

### F1: missed SciPlay's pass, so it was put in the wrong group (MATERIAL_FAIL)

- **Root cause (retrieval).** Robert's pass notice is a thread reply in #executives (`C07C2866011`), under Leonard's 9/29 speedrun message `99aa9133…` (ts 1759196326).
  - The run paged through #executives for all of September (calls 20–33). Call 20 returned that parent message with `thread_ts` set, so the thread was visible. The run never opened the thread.
  - It also never searched Slack for "SciPlay". A Slack search finds the record directly.
  - Fred (`EMPLOYEE_0008_SLACK_ID`) is a member of #executives. The send-list doc says a pass is any no "for this round", and Robert counts as "us". The accelerator-only rule ("has to come on our bridge thread or in #bridge-pitch") applies to accelerator programs, not SciPlay, so the strongest alternative reading does not save the run's answer.
- **Affected outputs (one cause, three deliverables):**
  1. Sheet row 9 says "In talks". It should be "Keep warm".
  2. The Trello Keep warm checklist is missing SciPlay (2 of 3 items).
  3. The reply's In talks firm count (8 → 7) and Keep warm firm count (2 → 3) are wrong. That is 2 of the 8 count cells.
- **Practical effect.** SciPlay would get the "thanks for the time, here is where we are" paragraph after telling us no. SciPlay would also be left off the checklist Leonard uses to track keep-warm firms.

### F2: build access taken from the stale Linear log, so both build-holding firms are wrong (MATERIAL_FAIL)

- **Root cause (retrieval / correction missed).**
  - The run took build access from ZOM-567 alone (call 76).
  - Arthur's correction in #zombie-match3d (`C0880U9751A`) explicitly overrides that log for the same people. It came later the same day and still falls within the "as of tonight" cut-off.
  - Fred is a member of #zombie-match3d. The channel appeared in the run's channel list (call 17), but the run never read it.
  - The run searched Drive, Linear and Confluence for "tester" (calls 73–75), but not Slack.
- **Affected outputs:** sheet rows 6–7 (Dentsu, T-Accelerate) say "iOS and Android". Both should be "iOS only". These are the only two non-"none" build-access values, so every positive entry in the column is wrong. The reply and the final answer repeat the claim.
- **Practical effect.** The update's "Try the game" paragraph would send Play internal-test links to both firms, and those links don't work for them. Avoiding exactly that is the stated purpose of the column ("so the update can carry the right link").

F1 and F2 are independent: different records, different services and different deliverable fields.

## 5. Correct work and usability

- The headline amount trap was handled: Anton is New investor at $25K, from the DocuSign Completed notice and the voided $40K. Paul is In talks at $50K, not New investor.
- a16z is kept In talks despite the speedrun rejection. Play is kept off despite the "discussing" decoy. Mattel is excluded as RFP-only. Homa and Brightwater are correctly added as off-list firms. Initial Capital's "small check" reply is correctly treated as Awaiting reply. Treo's Slack-only outreach is counted.
- The Awaiting reply group (14) and the off-sheet decisions are all correct.
- The sheet name, format, folder, columns and sharing are correct. A Trello checklist exists with the right name on the right card. The reply is on the right thread. Robert's "send to everyone" suggestion is declined.
- Usability: 23 of 26 sheet rows are fully correct. Fixing the rest is bounded: one group cell, two build-access cells, one checklist item and two numbers in the reply. However, every deliverable (sheet, Trello and reply) contains at least one wrong value.

## 6. Task/environment defects and unassessed scope

- No missing tool, inaccessible record or contradictory requirement affects the failures. Both deciding records are in channels Fred belongs to, within the cut-off, and findable by ordinary Slack search or by opening the thread. Output capability: Sheets creation and write, Trello checklist and Gmail reply are all SUPPORTED, and all succeeded in the run.
- No relevant known base-data issue: the SciPlay, ZOM-567 and investor-list items do not appear in `guidelines/known_data_issues.md` or `Evals/references/known_base_issues.md`.
- Residual consideration for F2: Arthur says he will attach the list "when I push tomorrow's build". The email asks for the list "as of tonight", and no record shows that Android access was fixed, so "iOS only" is the supported answer. In any case, the run never saw the correction, so its answer was not a reasoned interpretation.
- Unassessed: none material. The other in-talks, awaiting-reply and off-sheet statuses were checked against the list's Latest Status notes, #bridge-pitch, Fred's calendar and the injected records. They match the run.

## 7. Score rationale

- **Band 4 (Hard, NON-FAIL).** Two independent genuine retrieval failures, each a missed correction that overrides an easier source, spread across all three required deliverables:
  - one firm is in the wrong group, so it gets the wrong paragraph and is missing from the Trello checklist;
  - the entire positive build-access column is wrong;
  - half of the reply's group counts are wrong.
  Leonard asked for exactly these details "so I know which paragraph each one gets" and "the right link". Correcting them means changes across the sheet, the card and the reply. Substantial correct work remains usable: 23 of 26 rows, the Anton amount trap, the Awaiting reply group, the scope decisions and the delivery mechanics.
- **Why not 3:** score 3 is a single consequential failure with a bounded correction. Here there are two independent material failures, and every deliverable is affected, including the whole positive build-access column.
- **Why not 5:** the central result is not invalidated. The send list is mostly correct, the New investor group (the email's "get the new investors right") is exactly right, and the structure and delivery are correct. Much of the core task succeeded.

## 8. Next action

This gate is cleared (PROCEED). Keep this run and the F1/F2 evidence for /oe and /rubric. Rubric rows that check SciPlay → Keep warm (sheet group, Trello item, reply counts 7/1 and 3/0) and Dentsu/T-Accelerate → "iOS only" are the observed discriminators. Any change to the prompt or SQL needs a new matching Opus run before /hardness is rerun.

### FINAL VERDICT: NON-FAIL

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Assessment version: model-aware-v3

Assessed model: Opus

Assessment mode: OPUS_OBSERVED

Score: 4

Execution status: COMPLETE

Difficulty: Hard

Gate decision: PROCEED

Gate reason: OBSERVED_OPUS_FAILURE

Evaluator model: Opus 5.5 (claude-opus-5-5), effort unconfirmed

Next action: Proceed with dependent authoring (/oe, /rubric); retain the F1 (SciPlay Keep warm) and F2 (iOS-only build access) failure evidence.

Evidence limits: One run only; no average-score or repeatability claim. The original user-prompt turn is not in the export (task match established from the injected records the run read).
