# /hardness review: Opus observed (Eval 1A)

## 1. Scope

- Review: chat review, attempt 6adfee3b47f7621feba5b96c; mode `OPUS_OBSERVED`; spec `Evals/1A_Hardness_Eval.md`, assessment version `model-aware-v3`, `authority_contract: prompt-incorporation-v1`, `ruthless-grading-v1`.
- Review date: 2026-11-05. Universe: `Universe_Normal` (hg4-2026-08-31 v37), `Evals/references/universes/normal/universe_manifest.json` (SHA-256 5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450).
- Assignment (platform record): Robert, Co-founder & Creative Director; Executive / Finance / Planning and decision support; **Task type: long-horizon; Difficulty mode: easy**.
- Inputs reviewed:
  - Prompt `Evals/task_inputs/04_Prompt.txt`, SHA-256 ccd229a59a178f6edfb7eacc90beff4cce4a43305666c343a9bd960810fb1cc1 (627 bytes).
  - Injection SQL `Evals/task_inputs/01_Universe_Inject.sql` (revision 9), SHA-256 f1a290ced1765a5b5ed0fe039b0f65428ea3924ab4269267bfea352a04211f10. Proposed overlay; never executed.
  - Run `Evals/task_inputs/opus/trajectory.json` (uploaded as `Run1_trajectory (2).json`), SHA-256 cb1259b5b2fdc97c8cf4a5d388496ca65edcd522d6ebe1bc312a6e554aba4ada, 1,801,435 bytes. This replaces the earlier saved Opus run (53c30765…), which was graded against SQL revision 6.
  - Prompt reference files: none (the prompt points only to environment records).
- Evidence reuse: the Snowflake January revenue totals (DD $183.11, ZM $0.00) and the decision sweep come from the current `/prompt` report on the same prompt and SQL hashes. They agree with the run's own Snowflake result (event 144). Every SQL record cited below was re-read from the saved SQL in this review (NEW). The trajectory analysis is NEW.

## 2. Run provenance and input issues

- Model: init event `model: claude-opus-5-5[1m]`; all 186 assistant messages `model: claude-opus-5-5`; result `modelUsage.claude-opus-5-5[1m].canonicalModel: claude-opus-5-5`. Confirmed **Opus 5.5**. Claude Code 2.1.280, session 50e9ed83-f780-4184-b04c-29642025d14d, `terminal_reason: completed`, `subtype: success`, `num_turns: 158`, no permission denials, no sub-agents spawned.
- Hint status: the export leaves out the user prompt turn (event 1 is an assistant message). Nothing in the run shows a hint: no "hint" text, and the run never mentions the VO campaign or App Review, which are the two records a hint would point to. It found every source it used through its own searches. Treated as **unhinted**.
- Task/source match: the run acts on SQL revision 9 records. It read Blake's "jenkins" email `CAcq2o5f…` (SQL line 93, new in revision 9) and wrote "not the $95 above" on ENG-2445 (revision 9 comment). It also read the DM `6257a3c4…` (line 55), project "LLC take-over" (line 142), the ground-rules doc `f_1e468a9d69ea0f0a2001f5` (line 17), the draft sheet `f_d996e4c434ce160dc52596` (line 24), Trello card 456 (line 58), the split email `CAxkiKZL…` (line 81), the billing email `CA-Uw65…` (line 69) and Blake's $140 DM `ad623a2f…` (line 52).
- Known data issues: none of the listed issues covers the graded items (REVENUE_DAILY January totals, the AWS bills, the Linear statuses, the #prototype VO reply, the Apple email). The #prototype VO reply (2026-02-12T23:20Z) is before the Feb 13 10:03 UTC Slack export cut.
- No input defect blocks the review.

## 3. Requirement map (prompt-incorporation-v1)

Incorporation chain: the prompt says "take care of what he asked for… make the call on every item the way he lays it out" and "reply… with what I'd do and what it costs each of us a month". Leonard's DM incorporates the ground-rules doc ("the ground rules doc has how we decide") and the split email ("I'll email you how we split the money"). The ground-rules doc incorporates the LLC card ("How things move is on the LLC card on our board") and #winddown. The project description sets the scope ("One issue per thing the LLC might take from HG or pay for") and the move rule (Done / Todo with the mover / Canceled). Leonard's VO reply and the Apple email are **facts** that answer existing asks (what the LLC pays each month; whether anything is left to do on DD support). They add no new obligation.

Visibility: Robert is a member of C09UHHN6PFZ (#prototype), D04UP2L3E3S and D04V95AAAHW (local `slack/channels.json`). The Apple email and Blake's/Leonard's emails sit in robert@'s INBOX. He is a writer on the Drive docs. Linear, Trello and Snowflake are unscoped.

| # | Requirement | Expected (source) | Observed (trajectory event) | Outcome |
|---|---|---|---|---|
| R1 | Find the request and its inputs | DM, project, ground rules, draft, split email, LLC card, #winddown, billing emails | Read all of them (events 10–37, 129, 159, 181) | MET |
| R2 | DD revenue test | REVENUE_DAILY January: DD $183.11 covers its current $140 prod bill (Blake DM `ad623a2f…`), so DD comes over | Snowflake query (event 144) returned DD 183.11; took DD; costed prod at $140 | MET |
| R3 | ZM test | ZM $0.00 in January, so ZM stays with HG | ENG-2440/2443 Canceled with reasons | MET |
| R4 | CF and its needs | CF via Sunset's sale; CF AWS $62 (later jenkins email beats ENG-2445's $95); AppsFlyer free tier assigned to Leonard | Todo with the right owners; $62 costed; AppsFlyer Todo / Leonard / Mar 1 | MET |
| R5 | **Hidden LLC cost outside Linear** | Leonard's #prototype reply `6908b2f1…` (SQL line 46, 2026-02-12T23:20Z): the Meta VO campaign is "capped at $3,000 a month… moves to our new company's card from March if we keep CF going, so count it as its own line in what we pay each month". It goes on the sheet at $3,000. The project holds "one issue per thing the LLC might take from HG or pay for", and the prompt wants the project to match the sheet, so it also needs its own issue (Todo, Leonard) | Never found. The run's Slack searches were "Sunset", "lifestyle", "AWS", "Calm Play" and Blake's messages since Feb 8 (event 177). It never searched Leonard's own recent messages or read #prototype. No VO row on the sheet, no VO issue, and the total is $450 | **MATERIAL_FAIL** |
| R6 | Already carried | Metabase $100, dbt $100, GitHub $48 on Blake's card through May (Gmail `CA-Uw65…`): Done | Done (events 349–353); $248 as Blake's personal payment | MET |
| R7 | Overrides | Figma stays with HG (later ENG-2453 comment beats the draft); Calm Play not the vehicle ("the new one"); layer.ai lapses (Leonard's reply, line 49); #winddown keeps | All Canceled with the right reasons | MET |
| R8 | Monthly only | Playable vendor $3,750 one-off and the yearly/one-time store fees excluded | Excluded | MET |
| R9 | **DD player support (ENG-2462)** | Blake's ENG-2462 comment (01:30Z, "done, support goes to the email address now") is overtaken by Apple's App Review rejection of Domino Delights, Feb 13 07:30Z in robert@'s INBOX (`<136285951.151027292.1770967800000@email.apple.com>`, SQL line 101): "The support option in the app only opens an email draft… users can't reach you from the app". Something is still to do, so **Todo, Blake** under the project rule | Never opened or listed the Apple email (no Gmail search for Domino, App Review or recent inbox). Set ENG-2462 **Done** (event 355) with "nothing is left to do" (event 312). The ENG-2461 comment (310), sheet row 26 ("Done, nothing left to do") and the Slack reply ("DD player support (support email): done, $0") repeat it | **MATERIAL_FAIL** |
| R10 | Status, assignee and date per item | Project rule + LLC card: 6 Todo (incl. ENG-2462), 3 Done, 28 Canceled, plus the VO issue; sale items move at close, else Mar 1 | 5 Todo, 4 Done, 28 Canceled. The 36 items other than ENG-2462 are right, with the right assignees and dates | MET for 36 of 37 (ENG-2462 counted under R9; the VO issue under R5) |
| R11 | Comment on every issue | 37 base issues, plus the VO issue | 37 `linear_create_comment` calls, all successful | MET for the 37 (no VO issue, under R5) |
| R12 | Sheet in Robert's Drive, laid out like the draft, shared | Columns Item / Game / Decision / Monthly cost / Paid by / Next step / Owner / By; three shares per month | Created (event 242), 45 rows (244), shared as writer with Leonard (248) and Blake (250). Blake's personal-payment formula pointed at the wrong rows ($148) and was fixed (256) | MET for layout and sharing; content carries R5/R9 |
| R13 | **Shares** | $3,450 total ($140 + $62 + $248 + $3,000); a third each is $1,150; Blake's $248 counts toward his third, so he puts in $902 cash (split email `CAxkiKZL…`) | $450 total, $150 each, Blake "$98 over his third, the LLC pays him back $98/mo" | **MATERIAL_FAIL** (knock-on of R5) |
| R14 | Reply in the DM thread | thread_ts 1770961200.890407, with what Robert would do, what each pays a month and the link | Sent in the thread (event 416, ok:true) with the link | MET for delivery; content says $150 each and that DD support is done (R5, R9) |

Capability: every required write (Linear comment/update/create, gsheets create/update, gdrive share, Slack send) is **SUPPORTED**: the catalog lists each one, and every write the run made returned success. No capability-caused miss.

## 4. Grouped failures and independent causes

- **F1: Missed the Meta VO campaign ($3,000 a month), an LLC cost that's not in Linear.** Deciding record: Leonard's #prototype reply `6908b2f1…` (Feb 12 23:20Z), in a channel Robert belongs to, from the person who asked. Affected outputs: no VO row on the sheet; no VO issue in the project; the total is $450 instead of $3,450; the shares are $150 instead of $1,150; Blake's position is backwards (the LLC "pays him back $98/mo" when he should put in $902 cash); the Slack reply gives the same wrong figures. Leonard and Blake would go into Monday's call thinking the LLC costs a seventh of what it does. It's a retrieval failure: the run searched Blake's recent messages (event 177) but never Leonard's, and never read #prototype, even though the request is about what the LLC pays each month.
- **F2: DD player support called done after Apple rejected the email-only support.** Deciding record: the Apple App Review email of Feb 13 07:30Z in Robert's own inbox, about Domino Delights. Affected outputs: ENG-2462 status (Done, should be Todo), its comment, the ENG-2461 comment, sheet row 26 and the Slack reply line. It's a retrieval failure: the run never looked at Robert's recent inbox or searched Gmail for Domino Delights.
- **Independent causes: 2.** They rest on different deciding records (a Slack reply vs an Apple email), different items (a new cost line vs an existing issue) and different services. A run could make either one without the other.
- No task or environment defect affects either failure. Both records are visible to Robert, dated before the clock, and nothing later overrides them.

## 5. Narrow miss, failure pattern and tool calls

- **Narrow miss: NO.** Independent causes: 2. Failed share ≈ 38% of the weighted core answer. Core items: 37 per-item calls (status, owner, date, comment; lower weight each), the VO line and issue, the total, the three shares, the sheet, the sharing and the reply (the total, the shares and the reply's cost line weigh most). That's about 45 items. F1 makes the VO line and issue, the total, all three shares and the reply's figures wrong (≈33%). F2 makes ENG-2462's status and note wrong, with knock-on lines on ENG-2461, the sheet and the reply (≈5%). Difficulty mode **Easy**, loss **10%**. Two causes and a share well above 10%, so the narrow-miss rule doesn't apply.
- **Failure-pattern risk: YES.** Traps, each with its share of the weighted core answer if missed, and this run's result:
  - T1, Meta VO $3,000 in #prototype (`6908b2f1…`): VO row, VO issue, total, three shares, reply. ≈33%. **Wrong.**
  - T2, DD revenue test (REVENUE_DAILY $183.11 vs the $140 DM): DD game, DD prod AWS, DD support, total, shares, reply. ≈30%. **Right.**
  - T3, monthly-only exclusion (playable vendor $3,750): total, shares, reply. ≈25%. **Right.**
  - T4, CF AWS $62 (jenkins email) over $95 (ENG-2445): ENG-2445 note and row, total, shares. ≈20%. **Right.**
  - T5, Blake's $248 already carried: three Done statuses, Blake's cash. ≈12%. **Right.**
  - T6, DD support rejected by Apple (ENG-2462): ≈5%. **Wrong.**
  - T7, ZM $0 revenue: ≈5%. **Right.**
  - T8–T10, Figma later comment, Calm Play vs "the new one", layer.ai lapses: ≈3% each. **Right.**
  - Largest share: T1 ≈33% (30% or more). T1–T4 all change the total and shares, so runs that miss any one of them fail the same total/share/reply rows. They're told apart only by their own item rows.
- **Tool calls: 157** (157 by the main agent, 0 by sub-agents; both count). Task type long-horizon, minimum 100, 90% threshold 90. **Not under 90% of the minimum.** The run is above 100 too, but only through 37 list + 37 comment + 37 update calls. A run that skips the per-issue comment reads would fall below 100.

## 6. Correct work and usability

36 of the 37 Linear calls are right: decision, status, assignee, date and a reasoned comment. The run applied the revenue test from the warehouse table and used current bills over stale ones ($140 not ~$1k, $62 not $95, $100 + $100 + $48 not ~$300). It overrode Figma and Calm Play correctly, excluded the one-off and yearly items, laid the sheet out in the draft's columns and shared it, and posted the reply in the right thread. The share formulas follow Leonard's rule. That per-item work can be reused. The result the request turns on, what each founder pays a month, is wrong in the sheet and in the reply, and the project is missing one LLC cost.

## 7. Score rationale

**5 (Really hard, PASS).** The prompt and Leonard's DM end on one decision question: what the LLC costs each of us a month. F1 makes that answer wrong in every place it appears: on the sheet, in the project (no VO issue) and in the reply. The run reports $450 a month and $150 each when the plan costs $3,450 and $1,150 each, and it reverses Blake's position from paying $902 cash to being paid back $98. That invalidates the central result and the final delivery. The band table says one root cause can do that. F2 is a second, independent miss that changes a Linear status, so the project doesn't follow the move rule for ENG-2462.

Why not 4: band 4 fits when material failures need substantial correction but the central result is still usable. Here the per-item grid is usable, but the bottom line Leonard asked for is wrong by about 87% and points the wrong way for one partner. Acting on it would commit the founders to a plan that's $3,000 a month short. Why not 3: neither failure is a bounded local fix. F1 changes the total, all three shares, a sheet row, a Linear issue and the reply.

⚠ **Failure-pattern risk:** the Meta VO campaign trap (Leonard's #prototype reply of Feb 12, `6908b2f1…`) decides about 33% of the task's answer. If most runs miss it, they fail the same rows and the baseline's failure-pattern check can fail. Consider spreading the difficulty: 2–3 independent traps in other parts of the task, each with its own deciding record. See the [failure patterns guide, section 4](/?guide=patterns#4-build-at-least-three-traps-that-split-the-rollouts).

## 8. Suggested task revisions (advice only; the score stands)

- **Spread what the total depends on.** T1–T4 all land on the same total/share/reply rows, so runs that miss different ones can still fail alike. Make sure the rubric checks each trap on its own item row too (the VO row and issue, ENG-2445's $62, the playable vendor's exclusion, DD's row), so the runs split by item.
- **Keep the ENG-2462 trap.** It now changes a status (Todo vs Done), which it didn't in the earlier version. This run missed it, independently of F1.

## 9. Evidence limits

- One run only; no average pass rate or repeatability claim.
- The DD/ZM January revenue figures come from the run's Snowflake result (event 144) and the `/prompt` review's re-sum on the same inputs. They weren't re-aggregated again here. The margins ($183.11 vs $140; $0 vs any bill) make the calls insensitive to small differences.
- The export leaves out the initial user turn; unhinted status is inferred from the run's own discovery path.
- `input_manifest.json` was not updated: the output writer has no manifest key, and this report records its own input fingerprints (section 1).

### FINAL VERDICT: PASS

Assessment version: model-aware-v3

Assessed model: Opus

Assessment mode: OPUS_OBSERVED

Score: 5

Execution status: COMPLETE

Difficulty: Really hard

Gate decision: PROCEED

Gate reason: OBSERVED_OPUS_FAILURE

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Evaluator model: Opus 5.5 (claude-opus-5-5), session-default effort

Next action: Proceed with dependent authoring (/oe, /rubric); keep the F1 and F2 evidence and make sure the rubric checks each trap on its own item row.

Evidence limits: One run only; DD/ZM January revenue taken from the run's Snowflake result and the /prompt re-sum, not re-aggregated here; export omits the initial user turn.
