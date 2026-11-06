# /hardness review: Opus observed (Eval 1A)

## 1. Scope

- Review: chat review, attempt 6adfee3b47f7621feba5b96c; mode `OPUS_OBSERVED`; spec `Evals/1A_Hardness_Eval.md`, assessment version `model-aware-v3`, `authority_contract: prompt-incorporation-v1`, `evidence_contract: stage-evidence-v1` (reused_evidence: none).
- Review date: 2026-11-05. Universe: `Universe_Normal` (hg4-2026-08-31 v37), `Evals/references/universes/normal/universe_manifest.json` (SHA-256 5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450).
- Assignment (platform record): Robert, Co-founder & Creative Director; Executive / Finance / Planning and decision support; **Task type: long-horizon; Difficulty mode: easy**.
- Inputs reviewed:
  - Prompt `Evals/task_inputs/04_Prompt.txt`, SHA-256 ccd229a59a178f6edfb7eacc90beff4cce4a43305666c343a9bd960810fb1cc1 (627 bytes).
  - Injection SQL `Evals/task_inputs/01_Universe_Inject.sql`, SHA-256 4236a0301de9f4d287fb4a5be26e1dd6538cabe70f0c69b2031b167be11e1b76 (proposed overlay; never executed).
  - Run `Evals/task_inputs/opus/trajectory.json` (uploaded as Run1_trajectory.json), SHA-256 53c30765e132a9430ef6b6867ebb723e5a0b88c3a4f92b969905a2cd1f36df5c.
  - Prompt reference files: none (the prompt points only to environment records).

## 2. Run provenance and input issues

- Model: init event `model: claude-opus-5-5[1m]`, assistant messages `model: claude-opus-5-5`, result `modelUsage.claude-opus-5-5[1m].canonicalModel: claude-opus-5-5`. Confirmed **Opus 5.5**. Claude Code 2.1.280, session 6832431f-fa7a-4e34-bd26-1aa8558680d8, `terminal_reason: completed`, `num_turns: 176`, no permission denials, no sub-agents.
- Hint status: the export doesn't include the user prompt turn (the first event is an assistant message). Nothing in the run shows a hint. Each source it used was found through its own searches (DM read, Linear project search, Drive search, Slack/Gmail/Snowflake queries), so the run is treated as **unhinted**.
- Task/source match: the run acts on the injected records: Leonard's DM `6257a3c4…` in D04UP2L3E3S, Linear project "LLC take-over" ENG-2438…ENG-2474, ground-rules doc `f_1e468a9d69ea0f0a2001f5`, draft sheet `f_d996e4c434ce160dc52596`, Blake's DM `ad623a2f…`, #prototype reply `6908b2f1…`, Gmail split/billing emails and Trello card 456. The run's environment matches the saved SQL.
- No input defects block the review.

## 3. Requirement map (prompt-incorporation-v1)

Incorporation chain: the prompt says "take care of what he asked for… make the call on every item the way he lays it out". Leonard's DM incorporates the ground-rules doc ("the ground rules doc has how we decide") and the split email ("I'll email you how we split the money"). The ground-rules doc incorporates Trello card 456 ("How things move is on the LLC card on our board") and the #winddown decisions. The Linear project description sets the status mapping (Todo = LLC takes it, Done = one of us already carries it, Canceled = stays with HG). All of these are visible to Robert: he is a writer on the Drive docs, a member of D04UP2L3E3S, D04V95AAAHW, C09UHHN6PFZ and C0ADGSZKR3R (local `slack/channels.json`), and the Gmail copies sit in robert@'s mailbox.

| # | Requirement | Expected (source) | Observed (trajectory event) | Outcome |
|---|---|---|---|---|
| R1 | Find the request and all inputs | DM, project, ground rules, draft, split email, Trello card, #winddown | Read all of them (events 6–35, 64–71, 168) | MET |
| R2 | DD revenue test | REVENUE_DAILY Jan: DD $183.11 vs current prod bill $140 (Blake DM `ad623a2f…`, Feb 13), so the LLC takes DD, not Leonard's "~$1k" | Snowflake query event 180 returned DD 183.11, ZM 0.00. Run took DD and costed prod at $140 (events 338, 340) | MET |
| R3 | ZM test | ZM $0 Jan revenue vs a monthly AWS bill, so ZM stays with HG | ENG-2440/2443 set to Canceled with comments (432–434) | MET |
| R4 | CF and its needs | CF via Sunset's sale; CF AWS $62 (ENG-2445); AppsFlyer free tier; Unity Personal | Todo with the right owners; $62 costed | MET |
| R5 | Hidden cost not in Linear | Meta VO campaign $3,000/mo from March (#prototype `6908b2f1…`, Leonard: "count it in what the LLC costs"); project must match the sheet | Created ENG-2475 (event 319), $3,000 on the sheet | MET |
| R6 | Already carried | Metabase $100, dbt $100, GitHub $48 on Blake's card (Gmail `CA-Uw65…`), Done | Done, assigned Blake (368–372) | MET |
| R7 | Current-bill and later-correction overrides | Figma stays HG (later comment beats the Tuesday draft); Calm Play not the vehicle (ground rules "the new one"); #winddown keeps (Slack, Linear, Deel, Gusto, Intuit) | All Canceled with the right reasons | MET |
| R8 | Monthly only | Playable vendor $3,750 one-off and yearly/one-time store fees excluded | Excluded | MET |
| R9 | Status, assignee and date per item | Project mapping; Trello: whoever runs it moves it, sale items move at close, own deadline kept, else Mar 1 | 10 Todo/Done, 28 Canceled, none left in Backlog (489); By column: sale close / Feb 28 / Mar 1 | MET |
| R10 | Comment on every issue | 37 base issues + the new one | 38 `linear_create_comment` calls, all successful | MET |
| R11 | **DD player support (ENG-2462)** | Blake's "done, support goes to the email address now" (ENG-2462 comment, PR #1917) is overtaken by Apple's App Review rejection of Domino Delights on Feb 13 07:30 UTC (Gmail `robert@…/<136285951.151027292.1770967800000@email.apple.com>`, Guideline 1.5: "The support option in the app only opens an email draft… users can't reach you"). Support is not working, Helpshift ends before Feb 28 (#winddown 1770789534), and DD comes over with "its player support" (ground rules), so this is open work for Blake by Feb 28 | Status Todo / Blake / Feb 28 is right. But the ENG-2462 comment (342) says "The support email is already live… keeps its Feb 28 Helpshift deadline (already met)". The ENG-2461 comment (405) says "DD is already off it". Sheet row 5 says "Support email already live". The Slack reply (492) says "player support (email, already live)". The run listed this email (event 265) and fetched only its snippet in `minimal` format (event 270, "Thank you for submitting your items for review"). It never opened the body | **MATERIAL_FAIL** (one cause, four outputs) |
| R12 | Sheet in Robert's Drive, draft layout, shared | Columns Item / Game / Decision / Monthly cost / Paid by / Next step / Owner / By; shares per month | Created (314), 48 rows (316), shared writer with Leonard (326) and Blake (328); a `#NAME?` was fixed (324, 330) | MET |
| R13 | Shares | Thirds of $3,450 = $1,150; Blake's $248 counts toward his third, so he puts in $902 cash (split email `CAxkiKZL…`) | $1,150 / $1,150 / $902 on the sheet and in Slack | MET |
| R14 | Reply in the DM thread | thread_ts 1770961200.890407, with what I'd do, cost each per month and the link | Sent (492), ok:true | MET (content carries the R11 error) |

Capability: every required write (Linear update/comment/create, gsheets create/update, gdrive share, Slack send) is **SUPPORTED** and returned success in the run. Base data check: no listed known data issue covers the graded items (REVENUE_DAILY January, AWS bills, Linear statuses). `REVENUE_DAILY_V2` exists (`/tables/13`, a "versioned all-title revenue mart"). The ground rules' "daily revenue table" matches `ANALYTICS.MONETIZATION.REVENUE_DAILY` (`/tables/12`, "Daily revenue aggregated by game…"), which the run used.

## 4. Grouped failures and independent causes

- **F1 (only failure): DD player support called "live/deadline met" after Apple rejected the email-only build.** Root cause: the deciding record (Apple App Review email, Feb 13) was listed but never opened. Affected outputs: ENG-2462 comment, ENG-2461 comment, sheet row 5 "Next step", Slack reply. The status, assignee and due date for ENG-2462 are still right ("comes with the game"), and no cost or share figure changes. A partner reading the plan would think DD's support was solved while App Review had blocked it with the Helpshift cut-off two weeks away.
- **Independent causes: 1.**
- No task/environment defects affect the result.

## 5. Narrow miss, failure pattern and tool calls

- **Narrow miss: YES.** Independent causes: 1 (F1). Failed share ≈ 4% of the weighted core answer. Core items: about 38 per-item calls (status, owner, date, comment), plus the new VO issue, the total, the three shares, the sheet, the sharing and the Slack reply, about 45 items. F1 makes one item's reasoning and next step wrong (its status is right), with knock-on lines in three outputs. Difficulty mode **Easy**, loss **10%**. With one cause below the 10% loss, the score is 2.
- **Failure-pattern risk: YES.** Traps, each with its share of the weighted core answer if missed and this run's result:
  - T1, DD revenue test (Snowflake REVENUE_DAILY $183.11 vs Blake's $140 DM): decides DD game, DD prod AWS, DD support, the total ($3,450 vs $3,310), the three shares and the reply. ≈35%. **Right.**
  - T2, Meta VO $3,000 hidden in #prototype: new issue, total, shares, reply. ≈28%. **Right.**
  - T3, monthly-only exclusion (playable vendor $3,750): total and shares. ≈25%. **Right.**
  - T4, Blake's $248 already carried: three Done statuses, Blake's cash. ≈12%. **Right.**
  - T5, ZM $0 revenue: ≈5%. **Right.**
  - T6, DD player support rejected by Apple: ≈4%. **Wrong.**
  - T7, Figma later comment over the draft: ≈3%. **Right.**
  - T8, Calm Play vs "the new one": ≈3%. **Right.**
  - Largest share: T1 ≈35% (30% or more).
- **Tool calls: 175** (175 main agent, 0 sub-agents; both count). Task type long-horizon, minimum 100, 90% threshold 90. **Not under 90% of the minimum.**

## 6. Correct work and usability

All 37 base items got the right decision and status, plus the right owner. The hidden VO cost was found and added to Linear. The current-bill figures beat the stale ones ($140 not ~$1k, $100+$100+$48 not ~$300). Figma and Calm Play were overridden correctly. The one-off and yearly items were excluded. The total ($3,450), the thirds ($1,150) and Blake's $902 cash are right. The sheet layout, the sharing and the threaded reply are right. The deliverable can be used after a one-line fix to the DD support note.

## 7. Score rationale

Band table alone: F1 is one consequential misstatement that a bounded edit fixes, which could argue for 3. The narrow-miss rule decides it: one independent cause and a failed share of about 4%, below Easy's 10% loss, gives **2 (Easy)**. A 3 would need a second independent miss or a failed share at or above 10%. A run that avoids F1 (or one that also misses F1, since it changes no status or figure) still scores well above the Easy limit of 90%.

**Why Easy:** this run's only miss was one cause (it never opened Apple's Feb 13 App Review rejection of Domino Delights, so it told Leonard and Blake that DD's support email was live and its Feb 28 deadline met, on ENG-2462, ENG-2461, the sheet and in Slack), and it got about 96% of the task right. The baseline averages six runs, and runs that avoid this one miss score above the Easy limit (90%). Add a second, independent trap in a different part of the task (another item, source or decision), get a new unhinted Opus run and send /hardness again. See the [hardness guide, Part 8](/?guide=hardness#part-8-if-the-run-comes-back-too-easy).

⚠ **Failure-pattern risk:** the Domino Delights revenue test (Snowflake REVENUE_DAILY January $183.11 vs Blake's Feb 13 DM saying the prod account bills $140) decides about 35% of the task's answer. If most runs miss it, they fail the same rows and the baseline's failure-pattern check can fail. Consider spreading the difficulty: 2–3 independent traps in other parts of the task, each with its own deciding record. See the [failure patterns guide, section 4](/?guide=patterns#4-build-at-least-three-traps-that-split-the-rollouts).

## 8. Suggested task revisions (advice only)

- **Rules are spelled out in the request records (Hardness guideline Part 8).** The ground-rules doc settles almost every fork by itself: "whatever we said about them before", "Cost every item at what it bills now… not by what HG used to pay", "no one-offs or yearly fees", "#winddown stays decided". The project description gives the status mapping too. Move one or two of these into separate dated records, for example the monthly-only rule into Leonard's split email or a later Slack message. Don't just delete them: a rule nothing in the data settles becomes a fork.
- **Make the Apple-rejection trap change a status or a number.** Right now the miss only changes the wording. For example, have the fix for DD support carry a monthly cost the LLC pays, so missing the rejection changes the total and all three shares. Or let the base records make "Done" the natural status for ENG-2462 unless the rejection is read.
- **Add a second independent trap elsewhere (Part 3, traps 2/8):** for example a correction in another service to one of the costed items (CF AWS, AppsFlyer or the VO cap), naming that same item and dated after the Linear comment.

## 9. Evidence limits

- One run only; no average pass rate or repeatability claim.
- The DD/ZM January revenue figures come from the run's own Snowflake query result (event 180). The evaluator located `ANALYTICS.MONETIZATION.REVENUE_DAILY` at `/tables/12` in the local export but did not re-aggregate its rows from the 2.6 GB file. The decision margin ($183.11 vs $140; $0 vs any bill) makes the call insensitive to small differences.
- The export omits the initial user turn; unhinted status is inferred from the run's own discovery path.

### FINAL VERDICT: FAIL

Assessment version: model-aware-v3

Assessed model: Opus

Assessment mode: OPUS_OBSERVED

Score: 2

Execution status: COMPLETE

Difficulty: Easy

Gate decision: HOLD

Gate reason: INSUFFICIENT_DIFFICULTY

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Evaluator model: Opus 5.5 (claude-opus-5-5), session-default effort

Next action: Add a second independent trap (and make the DD support trap change a status or number), get a new unhinted Opus run and send /hardness again.

Evidence limits: One run only; DD/ZM January revenue taken from the run's Snowflake result, not re-aggregated locally; export omits the initial user turn.
