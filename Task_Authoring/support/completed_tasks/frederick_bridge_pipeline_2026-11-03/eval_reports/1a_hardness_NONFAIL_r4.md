# /hardness review: Opus observed (model-aware-v3)

## 1. Scope and provenance

- Review: chat review for contributor attempt 6ae4e299a13034b7eb8305f8. Mode `OPUS_OBSERVED`, selected spec `Evals/1A_Hardness_Eval.md` (sha256 `a3d48e04…03a3`). Review date 2026-11-02.
- Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
- Universe: `Universe_SynthCut/` (hg4-synth-sep30cut v16). Manifest: `Evals/references/universes/synthcut/universe_manifest.json` (sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a`).
- Assignment: Executive / Frederick Stone (Co-founder) / Corporate Ops / Retrieval / long-horizon / difficulty mode medium.
- Inputs reviewed (sha256):
  - Prompt `04_Prompt.txt` (rev 21): `b5ea6f0ff28c9baa2976c08d05edda90dc21774e48d597c572f966efae5317b9` (same text as the previous /hardness review).
  - Injection SQL `01_Universe_Inject.sql` (rev 20, "01_Universe_Inject (13).sql"): `c999829d668e9731d7569acdcca1612f3d4ad2099f51515bbf0fdb8b5facecba`.
  - Task details: `1d795090d3476539561f58917410dab7275f800863d3be3084150ecd9a383c37`.
  - Run `opus/trajectory.json` (rev 22, uploaded as "Run1_trajectory (4).json"): `8c579cc2c86626df160e43ab5e36bc5122de75e75fc2a7a341e6a9149f5838fa`. It replaces run `4e79530a…` (made on SQL rev 17). That run's score of 1 is **not** inherited.
- SQL changes since the previous /hardness review (rev 17 `a34c7de3…` → rev 20), from a direct diff:
  - Arthur's build-access correction `3cddf83c…` is reworded. It is now a **thread reply** under base #zombie-match3d post `c891232a…` ("I just released 0.3.49 on IOS", 2025-09-29). The reply avoids the words "tester", "testflight" and "ZOM-567". Its text: "Karthic and the 3 Dentsu folks still have no android access … never attached to the internal track … whatever the Linear log says. iOS is fine for all four." It was posted 2025-09-30T23:20Z (4:20 PM PT Sep 30).
  - Leonard's reply `301ad67f…` is re-parented under the same post, and the parent's reply counters are updated.
  - New Gmail reply from Paul Heydon, "Re: SAFE in DocuSign" (2025-09-30T15:40Z): "Done, signed it last night." It is in Fred's and Leonard's mailboxes, with thread snippets updated. No DocuSign Completed notice for Paul exists.
  - Every other statement is byte-identical (155 of 162).
- Run identity:
  - Both init records have `model: claude-opus-5-5[1m]`. Assistant messages have `claude-opus-5-5`, and `modelUsage.canonicalModel` is `claude-opus-5-5`. So the model is Opus 5.5.
  - Session 3702e8c7-…, Claude Code 2.1.280. There are two `result` records: an interim one at 54 turns and a final one at 78 turns. Both have `terminal_reason: completed` and `is_error: false`. The export ends with the final result and the final response, so it is complete.
- Unhinted: yes. The export has no user hint text; "hint" occurs only inside "Shintaro" in a data row. The run found Leonard's email itself (call 1, `gmail_search_messages from:leonard after:2025/09/29`).
- Task/source match: the run read the rev 20 records.
  - Paul's "signed it last night" email appears in the run's Gmail results (three hits), and the run quotes it in the reply: "He says he signed, but there's no DocuSign Completed notice yet".
  - It read ZOM-567 and both comments (calls 54–55).
  - The send-list doc text (call 7) matches the SQL INSERT.
- Tool calls: 144, including 15 by two subagents. Call count is not hardness evidence.
- Evidence contract `stage-evidence-v1`. Authority contract `prompt-incorporation-v1`.
- Reused evidence: the expected values for groups, amounts, Trello checklists, follow-up cards and the card comment (R1–R6, R8–R14) are REUSED from the previous `1a_hardness.md` (sha256 `eede9dc3fa8fd748411e57159a762bfe3188321f79fbc8e323b33742e163101e`, §3).
  - Their dependencies are byte-identical in rev 20: the send-list doc, README, deck, Trello comments, calendar events, the DocuSign/Anton records, the #executives note and the SciPlay thread reply.
  - The only rev 20 change touching those rows is Paul's email. It is re-checked NEW under R3.
  - R7 (build access) is re-checked NEW against the moved and reworded correction.

## 2. Input and authority issues

- None blocking. The model is confirmed, the export is complete, and the SQL overlay is shown to be applied.
- Incorporation chain (unchanged):
  - The prompt says "His email lays out what he's after".
  - The email incorporates the send-list doc ("with the groups and details in the Q4 update send list doc"), the README, the deck, the Trello card and the reply with counts.
  - The doc defines **Build access** for firms in talks: "whether they can get the current internal build, TestFlight on iOS and the Play internal test track on Android, so the update can carry the right link. Write iOS only, Android only, iOS and Android, or none … Arthur tracks the tester adds."
  - So build access is an incorporated, required column of the sheet.
- Visibility of the correction to the persona:
  - #zombie-match3d `C0880U9751A` is private and not archived. Its member list includes `EMPLOYEE_0008_SLACK_ID` = Frederick Stone (slack `users.json`) and `EMPLOYEE_0025_SLACK_ID` = Arthur Blake (`channels.json`).
  - The run's own Slack searches returned messages from `C0880U9751A` (for example the "elite-boss-refill-change branch" message), which shows actual read access in this run.

## 3. Requirement map (expected vs observed)

| # | Requirement (source) | Expected | Observed (trajectory) | Outcome |
|---|---|---|---|---|
| R1 | Scope: 2025-list names deduplicated, plus off-list firms with a pitch call on Fred's calendar since Sep 3 (doc) | Homa and Brightwater added; Mattel, SVB, Rollic, Metaplay, Supercell and Laton excluded (REUSED) | Homa and Brightwater Games Fund on the sheet; the others off (call 91) | MET |
| R2 | New investor = signed SAFE per the #executives note, with amount | Anton only, $25K | Anton, New investor, $25,000 (call 91) | MET |
| R3 | In talks = call on Fred's calendar, no pass; angels who said yes but haven't signed | 7 firms (GFR, a16z, Dentsu, T-Accelerate, NCsoft, Homa, Brightwater) + Paul $50K. **NEW:** Paul's "signed it last night" email doesn't count. The #executives note requires the DocuSign Completed notice, and none exists for Paul | Exactly these. Paul is In talks at $50K: "no DocuSign Completed notice yet, so not counted as signed" (call 91; reply call 144) | MET |
| R4 | Awaiting reply | 14 firms (REUSED) | The same 14 (call 91) | MET |
| R5 | Keep warm | LVP, Hiro, SciPlay (REUSED) | LVP, Hiro, Sciplay. The run read the #executives thread `1759196326.309469` (call 76) | MET |
| R6 | Off the sheet | Play, 1AM/March, Grishin, Lakestar, Transcend, Acterra and the rows with no outreach (REUSED) | Off the sheet | MET |
| R7 | Build access for firms in talks ("Arthur tracks the tester adds") | Dentsu **iOS only**, T-Accelerate **iOS only**. ZOM-567's comments (Sep 30 17:25Z and 18:40Z) say both were added on Play. Arthur's later reply `3cddf83c…` (Sep 30 23:20Z, #zombie-match3d) says the Play group "was never attached … whatever the Linear log says. iOS is fine for all four." The other five firms: none | **T-Accelerate "iOS and Android"** ("TestFlight + Play internal added Sep 22 (ZOM-567)"). **Dentsu "iOS and Android"** ("… added Sep 26 (ZOM-567)"). Other five: none (call 91). The run never opened the correction: no tool result contains its text ("never attached", "whatever the Linear" = 0 hits). The main thread ran no Slack search on build access. It used Gmail "TestFlight OR internal test OR tester" (call 71), Drive (calls 49–50), Confluence (call 53) and Linear (calls 52, 54–55), then took ZOM-567 as final | **MATERIAL_FAIL** |
| R8 | Sheet: Google Sheet named per README, in Fred's Q4 2025 folder; firm, group, amount, build access | Native Sheet in `d_5e8a1c3f9b07d2e64a1b93`, 26 rows | Call 90 created "Q4 update - send list", call 91 wrote 26 rows × 6 columns, call 92 moved it to `d_5e8a1c3f…`, call 93 shared it with Leonard. All succeeded. Two build-access cells are wrong (R7) | MET (container); content defect under R7 |
| R9 | Trello checklists, one item per firm or angel | New investor (1), In talks (8), Awaiting reply (14), Keep warm (3) on card `68c5a49e…` | Calls 94–97 created the 4 checklists; calls 98–123 added 26 items, matching exactly | MET |
| R10 | "F/up with <name>" cards in To Do for In talks + Awaiting reply, skipping firms with a meeting on Fred's calendar after Sep 30 | 19 cards; no Dentsu (Oct 1) or Makers (Oct 8) card; NCsoft under R11 (REUSED) | Calls 125–143 created 19 cards in To Do `640643a3fd8f3ca308d93195`: Paul, a16z, T-Accelerate, GFR, HOMA, Brightwater and 13 Awaiting reply firms. No Dentsu or Makers card | MET |
| R11 | Existing To Do card → comment instead | Comment on card 456 "F/up with Anel…" (NCsoft) | Call 124 commented on `68c99e98…`; no new NCsoft card | MET |
| R12 | Reply on Leonard's thread with firm/angel counts per group | 0/1; 7/1; 14/0; 3/0 | Call 144 replied on `<CAxDeR9C…>` with exactly these counts. The reply also states "T-Accelerate and Dentsu have iOS and Android … per Arthur's tester log", which repeats the R7 error to Leonard | MET (counts); R7 error repeated |
| R13 | Don't send to the whole 2025 list | Declined | Declined ("Everyone else from the 2025 list stays off, as you asked") | MET |
| R14 | Final response to Fred | Accurate summary | Accurate except that it repeats the R7 error: "Only T-Accelerate and Dentsu have access to the internal build (iOS and Android), based on Arthur's tester log in Linear" | R7 error repeated |

## 4. Grouped failures and independent causes

**F1 (one root cause, MATERIAL_FAIL): missed the later build-access correction and took the Linear log as final.**
- Cause:
  - The doc says "Arthur tracks the tester adds". Arthur has two records on this: ZOM-567 (earlier the same day) and his #zombie-match3d thread reply (later, 4:20 PM PT Sep 30, inside the "end of day Sep 30" cutoff). The reply explicitly overrides the Linear log ("whatever the Linear log says").
  - The run planned to check Slack for tester adds. It gave the Slack subagent "TestFlight", "tester", "Play internal" and "internal test" searches.
  - That subagent and the Gmail subagent both terminated ("Autocompact is thrashing").
  - The main thread said it would go through #bridge-pitch itself (index 310). It paged #bridge-pitch (calls 72–74) and ran firm-name searches (calls 78–89), but never redid a Slack check on build access, and never searched "Dentsu", "Karthic" or "android" in Slack.
  - It then wrote the Linear values as fact.
- Affected outputs (one cause, three places):
  - two sheet cells (T-Accelerate, Dentsu);
  - the reply to Leonard;
  - the final response.
- Impact:
  - The doc says the column exists "so the update can carry the right link".
  - With the run's output, Leonard would put the Android internal-track link in the update for Karthic (T-Accelerate) and the three Dentsu accounts. Arthur says none of them can use it yet.
  - These are 2 of the 7 firms in talks, and the only 2 with any build access. So every non-"none" build-access value in the deliverable is wrong.
- Attribution:
  - The subagent crashes were an interruption, but they don't excuse the miss.
  - The main agent saw both failures (indexes 281, 310), kept every capability, and continued for about 70 more calls. It declared the work complete without redoing the build-access check.
  - The correction is discoverable and readable by the persona (§2), and it doesn't depend on any unincorporated rule.
  - So this is a neglected discoverable source, which counts as a genuine model failure (1A §3).

**Process observation (not scored separately):**
- At index 240 the main agent wrote an invented "Agent … completed. Result:" block into its own text. It contains made-up Slack summaries: round-number timestamps such as `1758990000`, and "Northwind Capital", which does not appear in the SQL.
- It then said it would wait for the real results (index 246), and its deliverables match source-backed values rather than that invented text. For example, HOMA stays In talks even though the invented text called it publishing-only.
- No deliverable value could be traced to the invented block, so it adds no failure count.

Things challenged and rejected:
- Ambiguity of R7: there is none. Both records are Arthur's. The correction is later, names the same people and the same platform, and explicitly says the Linear log is wrong. The cutoff is "as of end of day Sep 30", and Arthur attaches the group "tomorrow", so on Sep 30 there is no Android access.
- Paul Heydon: kept In talks. This is correct; the new "signed" claim is an angel telling us, not a Completed notice.
- `reply_all: true`: the sent reply went to Leonard only (result headers `To: leonard.hayes@…`), which is fine for "reply on his thread".
- The reply's "Sep 29 Turkish VC call" remark is grounded in real #bridge-pitch results (main-thread tool results at indexes 324 and 363), not in the invented block.

## 5. Correct work and usability

- These are all correct:
  - every group;
  - all 26 sheet rows' groups and amounts;
  - all 26 checklist items;
  - all 19 follow-up cards and the two skips (Dentsu, Makers);
  - the NCsoft card comment;
  - all 8 reply counts.
- These traps were handled:
  - Anton's $40K → $25K;
  - Paul's new "signed it last night" claim versus the Completed-notice rule;
  - a16z speedrun;
  - Hiro/Edith Vane;
  - SciPlay's pass in a thread reply;
  - the off-list firms;
  - the Anel → NCsoft card;
  - Robert's "send to everyone".
- Usability: the sheet, Trello and counts are usable as delivered. The build-access column needs a bounded correction: two cells, plus correcting the statement made to Leonard. Until that's fixed, the investor update would carry a wrong link for the only two firms with build access.

## 6. Task/environment defects and unassessed scope

- Two background subagents terminated with "Autocompact is thrashing". That was a runtime interruption of those helpers. The main session completed normally, with all tools available, and finished the task itself. The interruption explains the lost subagent output, not the main agent's decision to skip the check (§4).
- Output capability is SUPPORTED, and every write succeeded: Sheets create/write, Drive move/share, Trello checklists, items, cards and comment, and the Gmail reply.
- No relevant known base-data issue.
- Unassessed: none material.

## 7. Score rationale

- **Band 3 (Hard, NON-FAIL).** One genuine model failure (F1) makes a required, doc-defined deliverable value wrong. The run states it to Leonard as fact, and it would send the wrong build link to the only two firms in talks with build access. This is consequential, not cosmetic. The fix is bounded (two cells and one sentence of the reply), and the rest of the core work is correct and usable.
- **Why not 2:** a minor defect would leave the result correct for its purpose. Here, the build-access column exists only so the update carries the right link, and every non-"none" value in it is wrong. The run reported the wrong values as verified ("per Arthur's tester log").
- **Why not 4:** the groups, amounts, counts and all Trello writes are correct. The correction is confined to one column for two firms, not substantial across the result.
- **Why not 5:** the central result (who gets the update, and in which group) and the delivery are intact.
- Variance note: the previous run (SQL rev 17) found the correction when it was a top-level post containing "tester"/"testflight". This run did not find the thread-reply version. One run can't show how often either happens, so this score covers this run only.

## 8. Next action and suggestions

- Gate: PROCEED (OBSERVED_OPUS_FAILURE). Keep this run's evidence.
- Suggestions for the dependent stages:
  - Put a weight-5 rubric row and an OE step on the two build-access cells: T-Accelerate iOS only, Dentsu iOS only, sourced from Arthur's 9/30 #zombie-match3d thread reply over ZOM-567.
  - Keep the routine Trello writes low weight.
- If the SQL or prompt changes again, send these again in order: /injection, /prompt, /hardness (with a new matching Opus run), /oe, /rubric.

### FINAL VERDICT: NON-FAIL

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Assessment version: model-aware-v3

Assessed model: Opus

Assessment mode: OPUS_OBSERVED

Score: 3

Execution status: COMPLETE

Difficulty: Hard

Gate decision: PROCEED

Gate reason: OBSERVED_OPUS_FAILURE

Evaluator model: Opus 5.5 (claude-opus-5-5), effort unconfirmed

Next action: Proceed with dependent authoring (/oe, /rubric); retain the observed build-access failure evidence and weight it in the rubric.

Evidence limits: One run only; no average-score or repeatability claim. The previous run on SQL rev 17 found the earlier, keyword-matching version of the correction, so results vary between runs. The original user-prompt turn is not in the export; the task match was established from the rev 20 records the run read.
