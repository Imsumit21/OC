# /hardness review: Opus observed (model-aware-v3)

## 1. Scope and provenance

- Review: chat review for contributor attempt 6ae4e299a13034b7eb8305f8. Mode `OPUS_OBSERVED`, selected spec `Evals/1A_Hardness_Eval.md`. Review date 2026-11-01.
- Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
- Universe: `Universe_SynthCut/` (hg4-synth-sep30cut v16). Manifest: `Evals/references/universes/synthcut/universe_manifest.json` (archive sha256 `d04f295b…b0fb0c`).
- Assignment: Executive / Frederick Stone (Co-founder) / Corporate Ops / Retrieval / long-horizon / difficulty mode medium.
- Inputs reviewed (sha256):
  - Prompt `04_Prompt.txt`: `cecfad824fd8037af82be1f41d010c98f920db4cfe57c5087c056b7098ffed32`
  - Injection SQL `01_Universe_Inject.sql` (rev 9): `3ba2b413458f437b3bac5c3ebae97ec7009afb6965ef8017341bf5873cca7f87`
  - Task details: `1d795090d3476539561f58917410dab7275f800863d3be3084150ecd9a383c37`
  - Run `opus/trajectory.json` (uploaded as Run1_trajectory.json): `885ed68d96e2457fc59967fec0e7e9dd51d05641ba0e6c76618ad39be16779cb`
- Run identity. The init record has `model: claude-opus-5-5[1m]`, every assistant message has `claude-opus-5-5`, and `modelUsage.canonicalModel` is `claude-opus-5-5`. Session b131a417-…, Claude Code 2.1.280, 108 turns, `terminal_reason: completed`, `is_error: false`. The export is complete: it has a final `result` record.
- Unhinted: yes. The run has no hint text. It discovered Leonard's email itself (call 1: `gmail_search_messages from:leonard`) and found every rule by reading task records. The original user-prompt turn is not in the export, but the run's actions match the saved prompt exactly: the board folder, the Trello card, the thread reply and the Oct 6 review.
- Task/source match: the run read the injected records (template doc `f_3b9e61c04d7a52e8f1a6c2`, README `f_c61a0e93b7d24f58a2e917`, folder `d_5e8a1c3f9b07d2e64a1b93`, Trello cards `68c5a49e…`/`68d8193c…`, Linear ZOM-567, contacts Edith Vane and Ilse Marrow) with the same content as SQL rev 9. That shows this SQL overlay was live in the run.
- Tool calls: 107 (Long Horizon tier is 100+). Call count is not hardness evidence.
- Evidence contract `stage-evidence-v1`. Reused evidence: none. Every fact below is NEW. Authority contract `prompt-incorporation-v1`.

## 2. Input and authority issues

- None blocking. The model is confirmed, the export is complete, and the SQL overlay is shown to be applied.
- Incorporation chain. The prompt says "His email has what he wants". Leonard's email (`<CAxDeR9C…>`, 2025-09-30T21:05Z) incorporates the following, all of which are valid requirement sources:
  - the "board pre-read template" buckets and definitions;
  - the folder README (naming);
  - the Existing Investor Update card ("whatever the card says to do for firms that pass");
  - the Board Deck card (which numbers the slide takes);
  - the "Let's not" on emailing the board.
- Unincorporated text, treated as distractors only:
  - Robert's 9/29 email asking to send the pipeline to the board;
  - the 9/29 Slack suggestion "just list who Leonard emailed this month";
  - the July template `f_8d2c47a91e05b3f6d7c418` (older, superseded by the Oct 14 version).

## 3. Requirement map (expected vs observed)

| # | Requirement (source) | Expected | Observed (trajectory) | Outcome |
|---|---|---|---|---|
| R1 | Find and apply the Oct 14 template, not the July one (email → "board pre-read template") | Use `f_3b9e61…` (Sep 26) | Call 11 read the Oct 14 doc. All rows use its buckets (In talks / Passed / Awaiting reply / Not contacted this round) | MET |
| R2 | Rows: one per unique name on the 2025 list, angels included, duplicates merged (template) | 80 list rows (No. 1–55, 65–89); Progression, BITKRAFT and Acterra appear twice, so 77 unique | 77 list rows. Duplicates merged and noted in the source column (sheet rows 23, 32, 61) | MET |
| R3 | Add non-list firms with a pitch call on Fred's calendar since Sep 3 that were investment talks; exclude SVB, RFP, service and engine calls, and calls only Leonard took | Homa (call Sep 18, co-dev investment path, #bridge-pitch) and Brightwater (call Sep 25 on Fred's calendar, injected `evt_2f86b0…`). Exclude SVB catch-up (Sep 5), the UA syncs, Mattel (RFP only, injected Slack `398502c0…`) and the 9/29 "Turkish VC" call (not on Fred's calendar) | Homa and Brightwater added. SVB, Mattel and the Turkish VC were excluded, with the reasons given in the final reply | MET |
| R4 | Status per template, as of EOD Sep 30 PT | See the status checks below | All checked statuses correct | MET |
| R5 | Committed = signed SAFE (DocuSign Completed), at the latest amount | Anton: $40K (Slack 9/19, Bridge angels sheet), cut to $25K by email 9/24 (`SAFE amount`), DocuSign Completed 9/26. Committed $25,000 | Sheet D5 = 25000. Total formula = 25000 | MET |
| R6 | Soft-circled = unsigned yes with an amount | Paul $50K, still unsigned (Leonard's 9/29 DocuSign nudge). Initial Capital "might write a small check" has no amount, so it is excluded. Row 69's "$500K previously" and 1Up's "$500k if they like you" are earlier-round or hypothetical, so excluded | Sheet E6 = 50000. Total = 50000. Initial Capital set to Awaiting reply with no amount, and the reason stated | MET |
| R7 | Build access for in-talks firms (Arthur's tester log) | ZOM-567: T-Accelerate "iOS and Android"; Dentsu "iOS only" (TestFlight 9/26, Play not added). Others "none". Angels left blank | Matches exactly (sheet C68, C38; others "none"; angels blank) | MET |
| R8 | Totals at the bottom; columns per slide 9 (firm, status, build access, committed, soft-circled) | Present | Rows 82–84 hold COUNTA/SUM formulas. Read-back (call 102) gave 79 / 25000 / 50000. Columns match slide 9 text (call 25) plus an extra source column | MET |
| R9 | Google Sheet named per README, in the Board - Oct 14 2025 folder | "Fundraising - Oct 14 board", Google Sheets, parent `d_5e8a1c3f9b07d2e64a1b93` | Call 99 `gdrive_create_file` with exactly that name, parent and native Sheets mime (success). Call 101 wrote 84 rows (success) | MET |
| R10 | Trello: Keep warm checklist on Existing Investor Update, one item per firm that passed after a pitch call or meeting this round; email-only no's excluded (card comment `68c64270…`) | LVP (call Sep 9, written no 9/25), Hiro (call Sep 23, written no from partner Edith Vane 9/26; contacts map her to Hiro), SciPlay (call Sep 15, phone pass written in #bridge-pitch thread 9/29). Exclude Play, 1AM/March, Grishin, Lakestar and Iamgaming (email-only) | Calls 103–106: checklist "Keep warm" on card `68c5a49e…` with exactly LVP, Hiro Capital and SciPlay (all succeeded) | MET |
| R11 | Reply on Leonard's thread with the three slide numbers (Board Deck card comment) | Firms 79, Committed $25,000, Soft-circled $50,000 | Call 107 `gmail_reply_to_message` on `<CAxDeR9C…>` with exactly those three numbers, a sheet link, the Keep warm note and judgment calls (success) | MET |
| R12 | Do not email the board (Leonard: "Let's not") | No board email | No send to the board. The decline is stated in the reply and the final answer | MET |
| R13 | Final response to Fred | Summary of outputs and numbers | Accurate summary, matches the writes | MET |

### Status checks (R4)

All checked against the records the run itself retrieved, re-verified in base or SQL where noted.

- **In talks (9).** Each has a call on Fred's calendar since Sep 3 and no pass.
  - Anton and Paul: angels who said yes.
  - GFR: Sep 30 17:30Z call. PERSON_0787 is the GFR contact per the "Re: GFR Fund <> HG" thread.
  - a16z: speedrun interview Sep 18. The speedrun rejection posted in #executives is not their bridge answer, per the template.
  - Dentsu: Sep 23 5:30pm PT call `[PERSON_NAME_35100]`. The invite was sent within minutes of the Dentsu reply in thread `1843473831194478743`.
  - T-Accelerate: Sep 22 call with PERSON_3242 (Karthic).
  - NCsoft: Sep 10 and Sep 19. The Gemini notes name Anel Ceman.
  - Homa and Brightwater.
- **Passed (8), each with a written no this round.**
  - LVP: thread 9/25, "we won't be joining this round".
  - Play: no relayed via Griffin, counts per the template; confirmed by the injected 9/25 correction.
  - March / 1AM: 9/8 forwarded email; list note "They don't do bridge".
  - Hiro.
  - Grishin: "GRx Feedback" 9/8.
  - Iamgaming (row 69): list note "They don't do bridge".
  - Lakestar: 9/4.
  - SciPlay.
- **Awaiting reply (14).** Outreach backed by the list's 09/11 notes, Leonard's 9/8 tracker, and the 9/12 #bridge-pitch "reached out to GFR, Play, Dentsu, General Catalyst, Sciplay, Triptyq, Turkven, Harlem Capital" (IH outreach counts as "us"). Treo: inbound, Leonard sent the deck 9/3 (injected Slack). Initial Capital: LinkedIn ping 9/9.
- **Not contacted this round (48).** Status-column and comment-column rejections such as Konvoy, Courtside, Signia and Backed are correctly ignored, as the template requires. Plans to reach out (Transcend, Acterra, Early Bird and the other Matthew intros) correctly count as no contact. Mattel's RFP-only talk is correctly excluded.

## 4. Grouped failures and independent causes

No consequential model failure was found. Every trap the injection builds was handled correctly:

- Anton's later, lower amount, plus the DocuSign Completed notice, was used (wrong-input-to-total trap). Result: $25K, not $40K.
- Paul was not counted as committed (signed-only rule).
- Initial Capital was not soft-circled (no amount given).
- Hiro's pass was resolved through the contacts entry "Partner, Hiro Capital" (alias trap).
- SciPlay's phone pass, written in a #bridge-pitch thread reply (thread on the 9/12 message), was found and turned into a Keep warm item.
- Play's no via Griffin was counted, following the correction.
- a16z's speedrun rejection was not treated as a bridge pass.
- Dentsu's Play-track gap gave "iOS only", not "iOS and Android".
- Mattel (RFP only), the SVB catch-up and the Leonard-only "Turkish VC" call were excluded.
- Robert's board-email request and the "list who Leonard emailed" Slack suggestion were ignored.
- The July template was not used.

Minor observations, none of which is a defect against an authorized requirement:

- Row 69's firm name is redacted in the list. The run labeled it "Iamgaming" from the Slack tracker and flagged that as an inference. Its status (Passed) does not depend on the label.
- The sheet adds a "Basis / source" column and keeps the default tab name "Sheet1". Neither is restricted by the template or README.

## 5. Task/environment defects

- None found that affected the run. Every needed record was visible to Frederick through the run's own tool results: Drive docs shared to him, his calendar and mailbox, #bridge-pitch and #executives membership, Trello, Linear ZOM-567 and contacts. All five writes returned success. The Sheets, Trello and Gmail write paths are SUPPORTED, as the observed successful calls show.

## 6. Unassessed scope

- I did not independently re-derive all 48 "Not contacted" rows against every possible mailbox and Slack record. I checked all rows the run gave another status, every calendar investment call Sep 3–30 (full 190-event list from call 27), the Sep 3 bridge outreach threads in Fred's mailbox, Leonard's 9/8 tracker and the 9/12 IH list, and found no contradiction. Any residual unseen mismatch would at most touch a status count; it would not change the three slide numbers, the Keep warm set or the writes. It does not affect the band.

## 7. Score rationale

**Score 1, Too easy.** The unhinted Opus 5.5 run met every core requirement with no meaningful defect:

- the correct sheet in the correct place with the correct name and columns;
- correct firm count (79), committed ($25,000) and soft-circled ($50,000);
- correct build access;
- the exact Keep warm set;
- the reply on the right thread with the right numbers;
- the decoy board email avoided.

Why not 2: score 2 requires minor defects, and I found none against authorized requirements. Why not 3: no consequential failure needing correction exists.

### Why it came out easy (Hardness guideline v2)

- **Part 8, "don't spell the rule out in the prompt".** The Oct 14 template doc lists every deciding rule in one record the email points straight to: the speedrun exception, "a partner writing from their own address… check contacts", the Griffin/advisor no rule, "latest amount", "DocuSign Completed", "calls only I took don't", and the RFP/SVB/engine exclusions. One read hands Opus the whole rulebook. A central rule doc works like rules in the prompt.
- **Part 2 / Part 7, same-place check.** Several corrections sit where Opus already reads:
  - the Play correction is in #bridge-pitch, the channel the run paged through in full;
  - Anton's $25K email and the DocuSign Completed notice are top-level in Fred's own inbox;
  - the Mattel "only RFP, haven't pitched the bridge" Slack states its own conclusion;
  - Leonard's email itself defuses Robert's decoy ("Let's not").
- **Part 4, "a caveat Opus can see".** The Dentsu Play-track gap and the Initial Capital "no amount" are both stated in plain view in the record the run reads for that item.

### Revision ideas (task-relevant, don't add steps)

- Take rules out of the template doc and put each in a separate dated record the agent must connect back. For example, put the speedrun-is-not-a-bridge-answer point only in an older #bridge-pitch thread reply, and the "signed only" definition only in a prior board-prep email. Make sure each rule is still settled somewhere in the data.
- Move a correction to another service, tied to the same item. For example, an amount change for Paul that shows up only in a DocuSign "Corrected" notice or a Linear/Trello comment, not in a thread Opus already reads.
- Add a "done" source with a missing piece: a firm Arthur's ZOM-567 log marks "added", where a later TestFlight bounce email shows the invite never landed.

Any change to the prompt or SQL needs a new matching Opus run before /hardness is rerun.

### FINAL VERDICT: FAIL

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Assessment version: model-aware-v3

Assessed model: Opus

Assessment mode: OPUS_OBSERVED

Score: 1

Execution status: COMPLETE

Difficulty: Too easy

Gate decision: HOLD

Gate reason: INSUFFICIENT_DIFFICULTY

Evaluator model: Opus 5.5 (claude-opus-5-5), effort unconfirmed

Next action: Revise the task so deciding rules and corrections sit in separate, out-of-the-way records (not the single template doc), then obtain a new unhinted Opus run on the revised inputs and rerun /hardness.

Evidence limits: One run only; no average-score or repeatability claim. The 48 "Not contacted" rows were cross-checked against outreach trackers, calendar and Sep 3 outreach threads, not every possible record; this cannot change the slide numbers, Keep warm set or writes.
