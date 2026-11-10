# /hardness: Opus observed-difficulty review

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

### FINAL VERDICT: FAIL
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Assessment version: model-aware-v3
Assessed model: Opus
Assessment mode: OPUS_OBSERVED
Score: 2
Execution status: COMPLETE
Difficulty: Easy
Gate decision: HOLD
Gate reason: INSUFFICIENT_DIFFICULTY
Evaluator model: Claude Opus 5.5 (claude-opus-5-5), effort low
Next action: Add independent, discoverable traps in other parts of the task (see Recommended revisions), get a new unhinted Opus run and send /hardness again.
Evidence limits: One run only; no average-score or repeatability claim.

**Why Easy:** this run made no material failure. It got every one of the 58 ad calls, all 48 assignments, all 58 ticket comments, all four store calls, the two store tickets, both deliverables, all 12 shares and the thread reply right. Its only defects are minor: the two new store tickets carry an Oct 15 due date while Arthur's calendar sets the Oct 16 12:00 PT cut (the run states that cut in both tickets), and it added an unsourced "refresh by Oct 8" interim date. It got about 97% of the task right. The baseline averages six runs; runs like this score far above the medium limit (85%). Add a second, independent trap in a different part of the task (another item, source or decision), get a new unhinted Opus run and send /hardness again. See the [hardness guide, Part 8](/?guide=hardness#part-8-if-the-run-comes-back-too-easy).

## 1. Inputs and provenance

| Input | Value |
|---|---|
| Prompt | `Evals/task_inputs/04_Prompt.txt`, sha256 `63d7c0713c3bf811b025cf9f73cbcade00c53401971b0d46ad3e2621cd2543d2` (669 bytes) |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql`, sha256 `d8cb3dd46a8ae12e691d9003659e5116e94dd0e1eec0b2f491aa54586e9eed8c`, the same version that passed /injection and /prompt. Never executed; treated as a proposed overlay. The run's reads returned the injected records (live creatives sheet, release calendar doc, Frederick's Sep 30 mail, Robert's deck, ART-793..854 comments, Trello comment, #zombie-art thread), so the overlay was in place for this run. |
| Trajectory | `Evals/task_inputs/opus/trajectory.json`, sha256 `8ef0af2a473dc10fae7cf26de86deb1e896dd845d7631ddb6a134272c896fea9`, uploaded as `trajectory-run-1.json` |
| Model | Every assistant event says `claude-opus-5-5`; init `claude-opus-5-5[1m]`; result `modelUsage` canonicalModel `claude-opus-5-5`. Claude Code 2.1.280, session `e69a88a4-4811-4d57-857a-a5ba6b1ee526`, `terminal_reason: completed`, `stop_reason: end_turn`, no permission denials. |
| Hint status | Unhinted as far as the export shows. It has no user/system text with hints (the prompt was passed outside the event stream). The run's first steps find #zombie_marketing and Leonard's 2025-09-30 message (ts 1759269913.882683) from scratch. |
| Task/source match | `get_time` returned 2025-10-01T07:01:02Z (the task clock). The run read the records this prompt names and the SQL injects, and wrote to Leonard's thread. Matches the task. |
| Reference files | None; the prompt uses no attached files. |
| Assignment | Claire Morgan, Art Lead, Design; Marketing and GTM; Authoring; Task type long-horizon; Difficulty mode medium. |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json`. |

## 2. Requirement map (prompt-incorporation-v1)

Incorporation: "take his message and do it all for me" pulls in Leonard's #zombie_marketing message, which points to the live creatives sheet, Arthur's release calendar, Robert's seasonal direction, Frederick's October UA plan and the Martin/Marcus maker split. Other records supply facts only. Expected answer: the /prompt review's verified Reading A on the same prompt and SQL hashes, rechecked here against the run's own tool results.

| # | Requirement | Expected | Observed (trajectory evidence) | Outcome |
|---|---|---|---|---|
| R1 | Call for every live ad | 58 ads (56 sheet rows + ART-826 + ART-831); 14 Halloween version, 34 Refresh first, 2 Reuse (ART-808, ART-816), 8 Skip; ART-836..839 excluded | Tracker write `gsheets_values_update` Ads!A1 (event 287): all 58 per-item calls match the expected lists exactly; ART-836..839 left out | MET |
| R2 | Trap: ART-831 missing from sheet | Included, Refresh first (rendered from #1450) | `linear_get_issue ART-831` (event 54); included, Refresh first | MET |
| R3 | Trap: ART-826 via Frederick's Trello comment | Included, Refresh first, Martin | `trello_search` (event 43); included, Refresh first, Martin | MET |
| R4 | Trap: ART-809 music baked in (Aug 13 thread) | Refresh first | `slack_read_thread` C06DJBJL798/1755114007.441789 (event 207); Refresh first, re-cut from no-music master | MET |
| R5 | Trap: ART-840 Boris opening added later | Refresh first (captured Jul 28) | Refresh first, "gameplay captured Jul 28" | MET |
| R6 | Trap: ART-808/816 existing Halloween cuts | Reuse | Reuse, "already in ZM3D Halloween 2025 / UA masters" | MET |
| R7 | Frederick's Sep 30 change overrides Sep 12 draft | Tablet-only ads Skip; ads due Wed Oct 15 (not Oct 17) | Both mails read (events 27, 29, decoded event 31); 8 Skips; every non-skip ad due Wed Oct 15 | MET |
| R8 | Makers | Julia statics ART-825..830 to Martin; the other 42 to Marcus | 48 `linear_update_issue` calls: 6 Martin, 42 Marcus, dueDate 2025-10-15 | MET |
| R9 | Due dates in plan, tracker and comments | Ads Wed Oct 15 (none for Skip); icon and iPad set by Thu Oct 16 12:00 PT | Ads correct. Store tickets ART-855/856 `dueDate: 2025-10-15`; tracker "Wed Oct 15 to Arthur (hard cut: merge Thu Oct 16 12:00 PT)". 34 refresh-first rows also carry "Refresh by Wed Oct 8", a date no record sets (tracker Key dates tab labels it "Plan (buffer before Oct 15)") | MINOR_GAP |
| R10 | Store calls | Icon and iPad 12.9" set Halloween version; iPhone 6.5" and Google Play sets Reuse | Store tab (event 294) and plan section 4 match | MET |
| R11 | Trap: store-ticket scope (Leonard's reply in Martin's #zombie-art thread) | 2 new ART tickets (icon, iPad set) to Martin; none for exported sets | `slack_read_thread` C08R8CHB0QL/1759245641.309714 (event 225); `linear_create_issue` ART-855 (iPad) and ART-856 (icon), both Martin | MET |
| R12 | Trap: icon "around the 24th" vs Arthur's calendar | Icon tied to the Oct 16 cut / Oct 17 submission | Doc, ticket, tracker and reply all say iOS icon ships in the build and can't swap on Oct 24 alone | MET |
| R13 | Comment each ad's call and due date on its ART ticket | 58 comments | 58 `linear_create_comment` calls, one per ticket, no duplicates, no errors; each states call, maker, due date | MET |
| R14 | Plan doc + tracker in Claire's Drive | Doc + Sheet | `gdocs_create_document` (event 299, 8,178 chars), `gsheets_create_spreadsheet` + Store/Ads/Key dates tabs | MET |
| R15 | Shared with the review so they can comment | Leonard, Frederick, Martin, Marcus, Robert, Arthur | 12 `gdrive_share_file` calls, role commenter, all succeeded | MET |
| R16 | Reply in Leonard's thread with both links before the review | One reply, thread_ts 1759269913.882683 | `slack_send_message` (event 568) with both links, ok:true, Oct 1 | MET |
| R17 | Final response | Summary to Claire | Accurate summary; it says the store tickets are due Oct 15 and that it changed status | MET |

Side effect (no requirement): the 48 assignments also moved the tickets from Done to `unstarted`. Nobody asked for that; the run says so and gives its reason. It's a minor, disclosed side effect that doesn't change any graded result.

## 3. Failures and independent causes

- MATERIAL_FAIL outcomes: **none**.
- Minor gaps: (a) store tickets due Oct 15, not the Oct 16 12:00 PT cut (Arthur's calendar, doc `f_fdd6d2d2f4a4d2f5b908fb`); the cut is stated in both tickets, so it's an earlier internal date, not a wrong deadline. (b) An unsourced "Refresh by Wed Oct 8" interim date on 34 rows and comments; the required Oct 15 date is present everywhere. (c) An unrequested status change, disclosed.
- **Independent causes:** 0 material (3 minor).
- **Failed share:** about 3%. It rests on about 236 core items: 58 calls, 58 due dates, 58 comments, 48 assignments, 4 store calls, 2 store tickets with 2 due dates, the doc, the tracker, sharing and the thread reply. The two store due dates are the only items with a real deviation, and they're partly correct.

## 4. Gate lines

- **Narrow miss: NO.** There's no material failure (0 independent causes; failed share about 3% of about 236 core items). Difficulty mode medium, loss 15%. The score comes from the band table: only minor defects, so 2.
- **Failure-pattern risk: NO.** Traps (all got right in this run): ART-831 off-sheet (about 2%), ART-826 via the Trello comment (about 2%), ART-809 music baked in (about 1%), ART-840 later edit (about 1%), ART-808/816 Reuse (about 2%), store-ticket scope from Leonard's #zombie-art reply (about 3%), icon date vs Arthur's calendar (about 2%), Frederick's Sep 30 change superseding the Sep 12 draft (8 Skips plus the Oct 15 date on every working ad, about 28%). Largest share: about 28%, Frederick's Sep 30 mail. That's just under the 30% line, so if you rework the task, don't let that one record carry more of the answer.
- **Tool calls: 233** (233 main agent, 0 sub-agents). The task type is Long-Horizon, with a minimum of 100. That's not under 90% of the minimum, so the count doesn't affect the score. The calls break down as 58 `linear_list_comments`, 58 `linear_create_comment`, 50 `linear_update_issue` and 12 `gdrive_share_file`; about 60 calls are research.

## 5. Correct work and usability

The result can be used as delivered. Every deciding record was found and applied item by item. That includes the corrections and exceptions spread across Gmail (the Sep 30 change), Trello (ART-826), the Linear comments (capture builds, ART-831's own note, ART-840), an older Slack thread (ART-809), a #zombie-art thread reply (store tickets) and a Google Doc (the icon window). All writes succeeded; the only tool error was an oversized `gcal_list_events` result, which the run worked around.

## 6. Task/environment defects and unassessed scope

- No capability gaps: every deliverable is a native Docs/Sheets/Linear/Slack/Drive write, and the run shows each one succeeding.
- Base issue SC-11 (Unity spend/CPI 0 in Snowflake) is not used. The run cites the CPI claim only from Frederick's Trello comment. Keep rubric rows off CPI values.
- Unassessed: none material. The plan doc's text after the first 6,000 characters was skimmed rather than checked line by line. It repeats the tracker's per-item calls, which were checked in full.

## 7. Score rationale

Score 2 (Easy). Opus met every core requirement, and every trap the task sets went the right way. What's left are minor date choices: an early internal due date for the two store tickets (with the true cut stated) and an extra interim milestone. Score 1 doesn't fit, because the store due-date deviation from Arthur's calendar is a real, if small, defect. Score 3 doesn't fit, because nothing needs a consequential correction: no call, inclusion, maker, write or destination is wrong.

## 8. Recommended revisions (advice; Hardness guideline, Part 8. If the run comes back too easy)

Opus got all of the heavy, per-item work right. Per Part 8, don't add more items or rows, and don't put rules in the prompt. Make the existing traps harder to find instead:

1. **Move the self-announcing corrections.** ART-831's own ticket comment says "Not on the live creatives sheet yet", and the sheet's Read me points straight to the Trello card holding the ART-826 correction. Move each one to a record that isn't where the agent is already looking, for example a Unity-campaign note in Frederick's mail or a DM (Part 3, 2. A correction somewhere else; 7. Items outside the obvious filter).
2. **Take the store-ticket rule out of the thread it governs.** Leonard's "no tickets for exported art" reply sits right under Martin's post. Move it elsewhere (a DM or an older review note) so it fails the same-place check.
3. **Add a "done" source with a missing piece.** For example, the Halloween iPhone set in the Store folder has fewer screens than the live set, or one of Marcus's Reuse cuts is the music-baked version. Then a call that looks finished actually needs work (Part 3, 1. Proving "done" across services).
4. **Put one capture build behind an alias.** Give a ticket only an iOS build number or a capture date, which another record maps to the #1452 cutoff (Part 3, 6. Different names for the same thing).

After changing the SQL, send /injection, /prompt and /hardness again, with a new unhinted Opus run.
