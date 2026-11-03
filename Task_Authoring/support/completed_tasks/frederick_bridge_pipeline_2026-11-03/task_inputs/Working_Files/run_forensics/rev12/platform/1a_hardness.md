# /hardness review: Opus observed (model-aware-v3)

## 1. Scope and provenance

- Review: chat review for contributor attempt 6ae4e299a13034b7eb8305f8. Mode `OPUS_OBSERVED`, selected spec `Evals/1A_Hardness_Eval.md` (sha256 `a3d48e0484a39548be6c09ab40d63fbebabbbbbba67b0df9387a0916a37503a3`). Review date 2026-11-02.
- Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
- Universe: `Universe_SynthCut/` (hg4-synth-sep30cut v16). Manifest: `Evals/references/universes/synthcut/universe_manifest.json` (sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a`).
- Assignment: Executive / Frederick Stone (Co-founder) / Corporate Ops / Retrieval / long-horizon / difficulty mode medium.
- Inputs reviewed (sha256):
  - Prompt `04_Prompt.txt` (rev 27): `b5ea6f0ff28c9baa2976c08d05edda90dc21774e48d597c572f966efae5317b9`. The text is the same as in the previous /hardness review.
  - Injection SQL `01_Universe_Inject.sql` (rev 26, "01_Universe_Inject (15).sql"): `69db98aed17f40cbcbbfad417b7eb21a118dffdbb63b798cf8322ddac226182b`.
  - Task details: `1d795090d3476539561f58917410dab7275f800863d3be3084150ecd9a383c37`.
  - Run `opus/trajectory.json` (rev 28, uploaded as "Run1_trajectory (6).json"): `38b13797136a43fccb0cb6c3c08698a2d9fe9826887db541e620c0879ce482e9`. It replaces run `9edcc952…` (SQL rev 23, score 3). That score is **not** inherited.
- SQL changes since the previous /hardness review (rev 23 `75b6cb2a…` → rev 26), from a statement-level diff:
  - **Paul's back-out moved to a DM.** Leonard's "Paul's out, he wrote me this morning that he can't put money in this year after all" is now message `c5657466…` in DM `D05S58U4SAK` (2025-09-30T17:05Z), not a thread reply in #executives. The Sep 19 "angel update" parent no longer has replies.
  - **The Android correction moved to one top-level Slack post that names four firms.** Karthic's and Arthur's emails (`<CAz_RUxJ…>`, `<CAU8zEO-…>`) were removed. Arthur's #zombie-match3d `C0880U9751A` message `3cddf83c…` (ts `1759274400.518306`, 2025-09-30T23:20Z = 16:20 PT) is now a top-level post: "found a problem with investor android access: the investor tester list I made in the Play console never got attached to the internal track, so nobody on it has android yet (Karthic, the 3 Dentsu folks, Anel's two at NCsoft and Ilse from Brightwater), whatever the Linear log says. iOS is fine for all of them". Leonard's reply `301ad67f…` (23:48Z) says "ok thx, ping me when it's live so I can tell Karthic, Ryo-san and the others".
  - **ZOM-567 gains two comments.** `lc_4369758f…` covers NCsoft ("TestFlight and Play internal track both added Sep 22") and `lc_5e2ff140…` covers Brightwater ("both added Sep 26"). Arthur wrote both on Sep 30, 17:45Z and 18:05Z. The Dentsu comment is now sequence 4.
- Run identity:
  - The init record has `model: claude-opus-5-5[1m]`. Every assistant message has `claude-opus-5-5`, and `modelUsage.canonicalModel` is `claude-opus-5-5`. So the model is Opus 5.5.
  - Session 7d6bd403-…, Claude Code 2.1.280. There is one `result` record (index 512), with `subtype: success`, `terminal_reason: completed`, `is_error: false` and 141 turns. The export ends with the final response, so it is complete. No subagents were spawned.
- Unhinted: yes. The export has no user text turn and no hint text; the only "hint" match is base64 data. The run found Leonard's email itself (call 1, `gmail_search_messages from:leonard after:2025/09/29`).
- Task/source match: the run read the rev 26 records.
  - The DM read (call 70) returned the rev 26 Paul message.
  - `linear_list_comments ZOM-567` (call 85) returned all four rev 26 comments, including the new NCsoft and Brightwater ones.
  - The send-list doc text (call 8) matches the SQL INSERT `f_3b9e61c04d7a52e8f1a6c2`.
- Tool calls: 140, all by the main thread. Call count is not hardness evidence.
- Evidence contract `stage-evidence-v1`. Authority contract `prompt-incorporation-v1`.
- Reused evidence:
  - The expected values for these rows are REUSED from the previous `1a_hardness.md` (sha256 `e7800edbd0e231d0cca7c289810c17982b72d9286b64d91421e7bdf5bef9bb9d`, §3): R1 (scope), R2 (Anton), R4 (the 14 Awaiting reply firms), R5 (Keep warm LVP, Hiro and SciPlay), R6 (off-sheet firms), R8, R10 (the 18-card set), R11 and R13.
  - Their dependencies are byte-identical between rev 23 and rev 26:
    - the send-list doc, README and deck;
    - the Trello comments, the Anel card and the calendar events;
    - the DocuSign/Anton records;
    - the #executives "signed" note `20924cc7…`;
    - the SciPlay reply `229090ba…`;
    - the #bridge-pitch posts (Treo, Initial Capital, 1AM, Play Ventures, Mattel).
  - The rows that rev 26 changes are re-checked NEW:
    - R3 (Paul, now a DM);
    - R7 (build access, now four firms);
    - R12 and R14 (counts and the statements carried to Leonard and Fred).

## 2. Input and authority issues

- None blocking. The model is confirmed, the export is complete, and the run shows the rev 26 overlay was applied.
- The incorporation chain is unchanged:
  - The prompt says "His email lays out what he's after".
  - Leonard's email (decoded at call 4) asks for "the groups and details in the Q4 update send list doc".
  - The doc's **Build access** section reads: "For firms in talks: whether they can get the current internal build, TestFlight on iOS and the Play internal test track on Android, so the update can carry the right link. Write iOS only, Android only, iOS and Android, or none … Arthur tracks the tester adds." The doc's **Sheet** section lists "build access (firms in talks)" as a column.
- Visibility of the deciding record:
  - #zombie-match3d `C0880U9751A` is private and not archived, with 25 members. `EMPLOYEE_0008_SLACK_ID` (Frederick Stone) is a member (slack `channels.json`).
  - Arthur's post `3cddf83c…` is top-level and falls inside the doc's "end of day Tue Sep 30 (Pacific)" window and before the clock.
  - Nothing later reverses it. Leonard's 23:48Z reply confirms Android is still not live. ZOM-567's comments (17:25Z–18:40Z) are all earlier, and Arthur's post overrides them by name ("whatever the Linear log says").
- Discoverability:
  - The run's Slack searches do index this channel. Call 64 returned a `C0880U9751A` message.
  - The post contains "android", "investor", "tester list", "Play console", "internal track" and "Linear log", and it is from Arthur, the person the doc names as owner of the tester adds.
  - A Slack search on any of those terms, a read of #zombie-match3d, or a look at Arthur's recent messages would have surfaced it.

## 3. Requirement map (expected vs observed)

| # | Requirement (source) | Expected | Observed (trajectory) | Outcome |
|---|---|---|---|---|
| R1 | Scope: 2025-list names deduplicated, plus off-list firms with a pitch call on Fred's calendar since Sep 3 (doc) | Homa and Brightwater added. Mattel, SVB, Rollic, Metaplay, Supercell and Laton excluded (REUSED) | Homa Games and Brightwater Games Fund on the sheet; Mattel and the others off (call 90; reply call 140) | MET |
| R2 | New investor = signed SAFE per the #executives note, with amount | Anton only, $25K (REUSED) | Anton, New investor, "$25,000" (call 90) | MET |
| R3 | Angels who said yes but haven't signed → In talks, unless they passed | **NEW:** Paul is out per Leonard's DM `c5657466…` (Sep 30 17:05Z). No call with Paul, so he stays off | Paul off: "He told you Sep 30 he can't invest this year, and we never had a call with him" (call 140). The run read the DM itself (calls 69–70) | MET |
| R4 | Awaiting reply | 14 firms (REUSED) | The same 14: Initial Capital, BITKRAFT, Makers, Raine, General Catalyst, BBQ, Treo VC, Superplay, Sony Mobile, Revo, e2vc, Triptyq, Turkven, Harlem (call 90) | MET |
| R5 | Keep warm = passed after a call this round | LVP, Hiro, SciPlay (REUSED; SciPlay per Robert's reply `229090ba…`) | LVP, Hiro, SciPlay; SciPlay "Call Sep 15; passed Sep 30 (call with Robert)" (call 90). The run opened thread `1759196326.309469` (call 75) | MET |
| R6 | Off the sheet | Play, 1AM/March, Grishin, Lakestar, Transcend, Acterra, Mattel, and list angels with no outreach (REUSED) | Off the sheet; Play and Mattel explained in the reply | MET |
| R7 | Build access for firms in talks: "whether they can get the current internal build … Arthur tracks the tester adds" | **NEW:** T-Accelerate, Dentsu, NCsoft and Brightwater **iOS only** (ZOM-567 records the TestFlight adds; Arthur's Sep 30 23:20Z post says the Play list was never attached, so none of them has Android). a16z, GFR and Homa **none** (no tester adds; REUSED for these three) | **T-Accelerate, Dentsu, NCsoft and Brightwater "iOS and Android"**, from ZOM-567 alone (call 90: "TestFlight + Play internal added … (ZOM-567)"). a16z, GFR and Homa "none". The run's reasoning (index 378): "Arthur's tracker gives build access: iOS and Android for Dentsu, Brightwater, NCsoft, and T-Accelerate". It never read #zombie-match3d. No tool result contains "never got attached", "investor android" or "found a problem". Its searches "testflight" (call 78) and "\"internal test\"" (call 84) don't match the post's wording, and "from:arthur added" (call 81) failed with `user_not_found` and was not retried | **MATERIAL_FAIL** |
| R8 | Sheet: Google Sheet named per README, in Fred's Q4 2025 folder; one row per recipient with firm, group, amount, build access | Native Sheet "Q4 update - send list" in `d_5e8a1c3f9b07d2e64a1b93` | Call 88 created the Sheets file in `d_5e8a1c3f…`. Call 89 initialized it, and call 90 wrote 25 rows × 6 columns to `Sheet1!A1:F26`; the result was `updatedCells: 156`. Call 91 shared it with Leonard. All succeeded. The four build-access cells are wrong (R7) | MET (container); content defect under R7 |
| R9 | Trello: own checklist for New investor, In talks and Awaiting reply, plus the Keep warm checklist, one item per firm or angel | New investor (1), In talks (7), Awaiting reply (14), Keep warm (3) on card `68c5a49e…` | Calls 92–95 created 4 checklists. Calls 96–120 added 25 items with exactly those splits | MET |
| R10 | "F/up with <name>" cards in To Do for In talks + Awaiting reply. Skip anyone with a meeting on Fred's calendar after Sep 30; comment on an existing To Do card instead | 18 cards: GFR, a16z, T-Accelerate, Homa, Brightwater + 13 Awaiting reply (no Makers, Oct 8). No Dentsu card (Oct 1) (REUSED) | Calls 121–138 created exactly those 18 cards in To Do `640643a3fd8f3ca308d93195`. No Dentsu or Makers card | MET |
| R11 | Existing To Do card → comment instead | Comment on "F/up with Anel…" `68c99e98…` for NCsoft (REUSED) | Call 139 commented on `68c99e98…`; no new NCsoft card. The comment text repeats the R7 error ("iOS and Android build access") | MET (action); R7 error repeated |
| R12 | Reply on Leonard's thread with firm and angel counts per group | New investor 0/1, In talks 7/0, Awaiting reply 14/0, Keep warm 3/0 | Call 140 replied on `<CAxDeR9C…>` with exactly 0/1, 7/0, 14/0, 3/0 (total 24 firms and 1 angel). The reply also states "Dentsu, T-Accelerate, NCsoft and Brightwater have iOS and Android" | Counts MET; R7 error repeated to Leonard |
| R13 | Don't send to the whole 2025 list | Declined | "Per your note, I didn't use the whole 2025 list" (call 140) | MET |
| R14 | Final response to Fred | Accurate summary | Accurate, except that it repeats R7 ("Dentsu, T-Accelerate, NCsoft and Brightwater can get the iOS and Android builds") | R7 error repeated |

## 4. Grouped failures and independent causes

**F1 (one root cause, MATERIAL_FAIL): took ZOM-567 as final and missed Arthur's later correction that no investor has Android.**
- Cause:
  - The doc says "Arthur tracks the tester adds". The run found ZOM-567 (calls 83 and 85) and stopped there (index 378).
  - ZOM-567 says "Play internal track added" for T-Accelerate, NCsoft, Brightwater and Dentsu. Arthur himself overrides that at 23:20Z the same day in #zombie-match3d, naming all four firms' testers and saying "whatever the Linear log says".
  - The run never read that channel. Its build-access searches used words the post doesn't contain ("testflight", "internal test"). Its one search aimed at Arthur's messages failed on a bad `from:` handle (call 81), and it did not retry.
- Affected outputs (one cause, several places):
  - four build-access cells in the sheet (4 of the 7 In talks rows; every non-"none" value is wrong);
  - the NCsoft card comment (call 139);
  - the build-access statement in the reply to Leonard (call 140);
  - the final response.
- Impact:
  - The doc says build access exists "so the update can carry the right link".
  - With this output, the update would send a Play internal-track link to four investors in active talks who can't use it. Arthur's post says Android won't be fixed until "tomorrow's push", and Leonard is asking to be told when it's live.
  - The run also told Leonard in writing that all four firms have Android.
- Attribution:
  - The source is visible to Fred, discoverable and inside the window (§2).
  - The requirement comes from the incorporated doc, not an unmentioned policy.
  - Nothing in the environment blocked the read: the failed `from:arthur` search was the run's own wrong argument, and other Slack reads and searches worked.
  - So this is a neglected discoverable source, which counts as a genuine model failure (1A §3).

Things challenged and rejected:
- Is "iOS and Android" a defensible reading, given that ZOM-567 is "Arthur's tracker"? No. The doc asks "whether they can get the current internal build", which is actual access, not whether a tester add was logged. Arthur, the owner the doc names, says later that same day that nobody on the list has Android, and he names the Linear log explicitly as wrong.
- Could the four firms have Android by the cutoff? No. Leonard's 23:48Z reply ("ping me when it's live") and Arthur's "I'll attach it with tomorrow's push" both put the fix after Sep 30. Nothing later in the window reverses it.
- Is iOS also in doubt? No. ZOM-567 records the TestFlight adds and Arthur says "iOS is fine for all of them", so "iOS only" is the expected value.
- Is the error minor because it's a single column? No. The doc defines the column's purpose (the right link), it is wrong for every firm that has any access, and the error was sent to Leonard.
- Were the other traps handled? Yes, all checked against the run:
  - Paul (DM read, call 70);
  - SciPlay (thread read, call 75);
  - Anton $25K;
  - Treo VC as Sep 3 outreach;
  - Play Ventures' no via Griffin;
  - the a16z speedrun rule;
  - Homa and Brightwater off-list;
  - the Anel → NCsoft card;
  - the Dentsu and Makers card skips;
  - Robert's "send to everyone".

## 5. Correct work and usability

- These are all correct:
  - every group assignment (25 recipients) and every off-sheet decision;
  - all 8 reply counts;
  - Anton's amount;
  - 3 of the 7 build-access values (a16z, GFR and Homa "none");
  - the sheet name, type, location and sharing;
  - all 25 checklist items in the right checklists;
  - exactly the 18 expected follow-up cards;
  - the NCsoft comment in place of a card;
  - the reply on the right thread.
- Usability: the result is usable after a bounded correction. That means changing four sheet cells from "iOS and Android" to "iOS only", correcting the build-access line sent to Leonard, and editing the NCsoft card comment. Who gets the update, and which paragraph each recipient gets, is right.

## 6. Task/environment defects and unassessed scope

- No task or environment defect affected the result.
- Output capability is SUPPORTED, and all 53 writes returned results without errors: Drive create/share, Sheets create/write, Trello checklists, items, cards and comment, and the Gmail reply.
- Minor non-scored observation: the spreadsheet's single tab is "Sheet1" (the create call's `initialSheetTitle: "Send list"` was not applied). The README sets no tab name.
- No relevant known base-data issue.
- `input_manifest.json` is not updated by this review. The report writer handles only the report, and this report records its own input fingerprints in §1.
- Unassessed: none material.

## 7. Score rationale

- **Band 3 (Hard, NON-FAIL).** One genuine model failure (F1): the run used a stale tracker over its owner's explicit later correction. Every non-"none" build-access value is wrong (4 of 7 In talks firms), and the error reached Leonard in writing. It is consequential: the update would carry an unusable Android link to four investors in talks. The fix is bounded to one column for four firms plus two text corrections, and the rest of the core work is correct and usable.
- **Why not 2:** a minor defect would leave the result correct for its purpose. Here the doc gives build access its own purpose ("so the update can carry the right link"), the value is wrong for every firm that has access, and the run reported it to Leonard as fact.
- **Why not 4:** there is one root cause, confined to one column. All 25 group placements, all counts, amounts, Trello checklists, cards and the comment action are correct. The correction is local, not substantial across the result.
- **Why not 5:** the central result is intact. Who gets the update and which paragraph each recipient gets are right, and every deliverable was delivered.
- Variance note: across the last three runs, Opus missed one trap per run. With SQL rev 20 it missed build access, with rev 23 it missed SciPlay's pass, and with rev 26 it missed build access again. One run can't show how often either happens, so this score covers this run only.

## 8. Next action and suggestions

- Gate: PROCEED (OBSERVED_OPUS_FAILURE). Keep this run's evidence.
- Suggestions for the dependent stages:
  - Put a high-weight rubric row and an OE step on build access: T-Accelerate, Dentsu, NCsoft and Brightwater = iOS only, sourced from Arthur's Sep 30 #zombie-match3d post `3cddf83c…` over ZOM-567. Add a separate row for a16z, GFR and Homa = none.
  - Keep separate rows for SciPlay = Keep warm and Paul staying off. This run got both right, but an earlier run missed SciPlay.
  - Check the reply-count row against 0/1, 7/0, 14/0 and 3/0.
- Next stages: /oe, then /rubric. If the SQL or prompt changes again, first send /injection, /prompt and /hardness again (with a new matching Opus run).

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

Evidence limits: One run only; no average-score or repeatability claim. Earlier runs on prior SQL versions failed different traps, so results vary between runs. The original user-prompt turn is not in the export; the task match was established from the rev 26 records the run read.
