# HARDNESS REPORT (Eval 1A, Opus observed)

- Attempt: 6aed9d01a1cb8067d8ac7dee (chat review)
- Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
- Assignment (platform record): Leonard Hayes, Co-founder & Creative Director · Executive · Finance · Authoring · long-horizon · difficulty mode medium
- authority_contract: prompt-incorporation-v1

## 1. Inputs and provenance

| Input | Source | SHA-256 |
|---|---|---|
| Prompt | `Evals/task_inputs/04_Prompt.txt` (712 B) | `424c70d34fdfba5e323649f44e4c228d3b3694d2196fc2891d6d55f5fb1407a2` |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (74,125 B; proposed overlay, not executed) | `bc72db9c31e9982751e47762f94939c7c5367ee7979830e28acb55627b957f2d` |
| Run | `Evals/task_inputs/opus/trajectory.json` (uploaded as trajectory-run-1.json, 7,934,992 B) | `f059ce8331b7001d7e45270399dcef907a7c3670fa875169b0d08ebf8f6b76c5` |
| Universe | `Universe_Normal` (`hg4-2026-08-31` v37); `Evals/references/universes/normal/universe_manifest.json` | n/a |

- **Model:** every assistant event is `claude-opus-5-5`; init model `claude-opus-5-5[1m]`; Claude Code 2.1.280, session 6ae2a995-3b42-4351-ab58-f2f6440e974a; `subtype: success`, `terminal_reason: completed`, 239 turns. Confirmed Opus.
- **Task match / hint status:** the export carries one context compaction (event 835). Its summary quotes the original user message word-for-word, and the text matches the saved prompt exactly. No other user text, hints or extra rules appear. Unhinted, same task.
- **Source match:** the records the run read (close-out notes doc `f_a37b403d5200d4f0a31d31`, Linear project "Holder records" with issues ENG-2438–2463, #winddown thread replies, KPMG and Sunset threads, Robert's Feb 12 email, the contacts, the Trello card) match the saved SQL word-for-word. Base records it cited (Carta termination emails, the Feb 9 Griffin email, Feb 11 termination letters, the Feb 11–12 group DM) were spot-checked against `Universe_Normal` (for example `threads/leonard@harmonygames.co_1856958794180374704.json`, `…_1770141224265557526.json`, and the 14 "Termination details for" Carta threads).

## 2. Requirement map (expected vs observed)

These requirements come from the prompt plus the sources it tells the Agent to follow: the close-out notes doc, the Linear project description, and through them the #winddown draft and thread, the update outline, Sunset's intake email and KPMG's request and clarification.

| # | Requirement (source) | Expected | Observed (trajectory) | Outcome |
|---|---|---|---|---|
| R1 | Holder sheet in the close-out folder (notes doc; Sunset email) | One row per Linear issue (26), founders only in totals; holdings today (vested only for options); last day; labels / Covered; counts; totals; directors; preferred vote; notice routes incl. special terms | Reused "Holder list (draft)" `f_5ecaa967db3adcfa440b09` in folder `d_601064334a0b493022fe83`; Holders (26 rows), Summary and KPMG tabs written (#167–#173, ev. 767–785) | MET |
| R2 | "Carta is the record; last day passed = holds nothing" | ES-2, ES-3, ES-5, ES-6, ES-16, ES-17 → Nothing; Nov 2024 owner-list figures are not used for options | Six lines Nothing/Canceled using the Carta termination emails; vested amounts from Carta, not the Nov 2024 list | MET |
| R3 | "Told" = written, direct, from a founder; for a fund, its partner | Griffin (Feb 9 email to Senior Partner), SEMC (Feb 9 DM), [0127] (Robert's Feb 12 email) → Already told; Feb 11 letters/group DM → told; Vincent and Oliver not told | 4 Already told; Julia/Claire/Brian/Marcus/Owen/Martin → Last day; Vincent and Oliver → Closing and last day | MET |
| R4 | Family rule (Leonard's #winddown thread reply) | Libra CEO's note covers Patrick Lewis and [27652] (he sent all three investor profiles, Jun 30 2023); those lines marked Covered | ENG-2444/2445 Covered and Done with comments; covering note lists all three holdings | MET |
| R5 | Sharing (notes + thread correction) | Sheet → Robert and Arthur; letter → Robert | #177–#179 exactly so | MET |
| R6 | Order: earliest last day first | Vincent (Feb 21) first, then Mar 31, then Apr 30, then holders with no last day | Same order in the sheet, the #winddown reply and the summary | MET |
| R7 | Holder notes as Gmail drafts, unsent; each states the holding, the closing if not told, the last day; unanswered holding questions answered | 14 drafts; Claire's Feb 12 equity question answered | 14 drafts (#180–#193), none sent; Claire's draft answers "you don't need to do anything" | MET (minor gaps G2, G3) |
| R8 | Notice route: the email we have, unless a document says otherwise | TOR side letter terms recorded; other holders' known email | Sheet records TOR's side-letter route correctly; other rows give the email on file | MET (minor gap G2/G3 on draft addressing) |
| R9 | Investor letter from the #winddown draft, in the outline's sections, in the close-out folder | Updated letter (Sunset, data licence, IP kept, board change, no distribution) | Doc `4e34ab72a6e4bc0d1ea7b40a` created and moved into the folder; follows the five outline sections | MET |
| R10 | Linear states + comments (project description) | Canceled where the line holds nothing; Todo where its own note waits; Done otherwise; a "why" comment on every issue without its own note | 14 Todo / 6 Done / 6 Canceled; 12 comments (#194–#231) | MET |
| R11 | Griffin heads-up on the Feb 12 Board position thread, after the sheet, sent | Reply to Griffin's partner with what is still needed | Reply-all on thread 1856958794180374704 to PERSON_4337 (cc Griffin colleague, Robert, Arthur): holdings + 3 asks (#232) | MET |
| R12 | #winddown reply under Leonard's list saying who goes first | Vincent Parker | Posted in thread 1770934638.035469 (#237) | MET |
| R13 | KPMG confirmation, reply to all, as of Dec 31, 2025 | Shares by class with each Griffin fund; option lines by Carta effective date (Dec 31 terminations vested-only per clarification; Jan 30 terminations full grant; lapsed ES-2/ES-6 out); total; shares+options; events since | Common 6,000,000; Seed 3,155,643 (Griffin 2,662,255 / 84,438); 12 lines, total 139,993; 9,295,636; events list. First reply-all reached only the sender, so the Agent resent it to all four (#235–#236) | MET (minor gap G1) |
| R14 | Final response | Accurate summary; drafts unsent; flags open points | Accurate; flags placeholder names and the open ES-8–ES-11 question | MET |

## 3. Failures, causes and correct work

**Material failures:** none demonstrated.

**Minor gaps**
- **G1 (KPMG delivery):** `gmail_reply_to_message` with `reply_all: true` (ev. 944) went to the sender only. The Agent spotted this and sent the same confirmation to sender + 3 cc's (ev. 950), so the sender got it twice. The end state is correct. This may also be how the tool behaves.
- **G2 (option-holder draft addresses):** six drafts go to @harmonygames.co work addresses. Leonard sent the Feb 11 termination letters to personal addresses (PERSON_2360/2361, PERSON_4243, PERSON_4363, PERSON_3140) and told the Turkish group the letters would go "to your personal account". Under "the email we have", either address can be defended, so this is not a proven error. The drafts wait for Leonard's review anyway.
- **G3 (TOR draft recipients):** the draft goes to two TOR directors (cc Thompson Legal), not to the side letter's "Attn" notice address. The sheet records the side-letter route correctly, and Sunset says the notes don't need to double as formal notices.

**Unassessed scope (evidence limit, not counted):** Carta activity (thread `leonard@harmonygames.co_1782897835407336831`) shows option grants ES-9 (Matthew Collins) and ES-11 (PERSON_3941 [0127]), and there is no Carta termination email for either. No grant sizes exist in the data the evaluator or the Agent could find. The Nov 2024 owner list ("diluted ownership") may fold these grants into the 86,470 and 31,536 totals. The run booked those totals as Series Seed and left ES-9/ES-11 out of KPMG item 2. Base records also contain a "2nd Close" for angels (Jul–Aug 2023 thread), which supports the Agent's Series Seed total of 3,155,643 over the 3,051,881 "initial closing" figure. Whether ES-9/ES-11 were still outstanding can't be settled from the data. Item 3 (shares + options) is unaffected either way. The Agent disclosed the open point to Leonard but not to KPMG.

**Independent causes:** 0 material.

**Correct work and usability:** all 14 requirements are met, and every deliverable can be used as written: the sheet, the letter, 14 drafts, 26 Linear states with 12 comments, and the three sent replies.

**Task / environment defects:** reply-all dropped the CCs on the KPMG thread but not on the Griffin thread. That behaviour is environment-level and was recovered.

## 4. Score lines

- **Narrow miss: NO.** 0 independent material causes; failed share ≈ 3% (about 40 core items: 26 per-row decisions, 14 drafts and Linear states, 3 sends, sheet totals, KPMG figures; only the minor gaps above); difficulty mode medium, loss 15%. The narrow-miss rule doesn't apply because there is no material failure. The band table alone gives Easy.
- **Failure-pattern risk: NO.** Traps (all answered correctly by this run):
  - T1 Carta lapse rule (six lapsed option lines → Nothing/Canceled, ES-2/ES-6 out of KPMG): ≈ 18%
  - T2 Feb 11 termination letters / group DM count as "told" (six option holders → Last day): ≈ 14%
  - T3 Not told despite channel announcements (Vincent, Oliver → Closing and last day; Vincent goes first): ≈ 8%
  - T4 Fund and investor "told" records (Griffin Feb 9 email to its partner, SEMC Feb 9 DM, Robert's Feb 12 email): ≈ 10%
  - T5 Family Covered rule (thread reply): ≈ 7%
  - T6 KPMG effective-date + as-of-date clarification: ≈ 8%
  - T7 Claire's unanswered equity question: ≈ 3%
  - T8 TOR side-letter notice terms: ≈ 3%
  - T9 Sheet also goes to Arthur (thread correction): ≈ 2%

  Largest share ≈ 18%, below 30%.
- **Tool calls: 237** (237 by the main agent, 0 by sub-agents; no `parent_tool_use_id` events, `subagent_stats.spawned` = 0). Task type long-horizon, minimum 100, 90% threshold 90. Not under 90% of the minimum.

## 5. Score rationale

The run met the core requirements across every deliverable. Each designed decision point checked out against the records: the told/not-told split, the lapse rule, the family coverage, the sharing correction, the send order, Claire's question, the TOR terms and KPMG's effective-date clarification. The only defects are minor and recoverable (a duplicate KPMG email, contestable draft addressing). That is **2 (Easy)** and not 1, because the run still has the minor gaps G1–G3. It is not 3, because no consequential failure needing correction was shown.

**Why it came out easy (advice).** The close-out notes doc and the Linear project spell out every rule: what "told" means, the labels, the lapse rule, the state mapping, the comment rule, the ordering. Each rule's deciding records are also easy to reach from where the Agent starts. Per the hardness guideline, Part 8 ("If the run comes back too easy"), and Part 3:
- Move at least one deciding fact out of plain view. For example, a later correction in another service that flips a holder's status (Part 3.2, "A correction somewhere else"), such as a holder's reply in a different thread showing they were never actually reached.
- Add a "done" source with a missing piece (Part 3.1). For example, a Carta termination email whose last day was later extended in a separate notice.
- Put one holder behind an alias that only a contact or history record resolves (Part 3.6).
- Don't add more holders or rows, and don't write the rules into the prompt.

After changing the task, get a new unhinted Opus run and send /hardness again.

### FINAL VERDICT: FAIL
Assessment version: model-aware-v3
Assessed model: Opus
Assessment mode: OPUS_OBSERVED
Score: 2
Execution status: COMPLETE
Difficulty: Easy
Gate decision: HOLD
Gate reason: INSUFFICIENT_DIFFICULTY
Evaluator model: Claude Opus 5.5 (claude-opus-5-5), standard effort
Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
Next action: Make the task harder (move a deciding fact out of plain view, per hardness guideline Part 8), get a new unhinted Opus run, and send /hardness again.
Evidence limits: One run only; no average-score or repeatability claim. The ES-9/ES-11 option sizes and status can't be determined from the data and were not scored.
