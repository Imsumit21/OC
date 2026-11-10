# /hardness: Opus observed-difficulty review

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

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
Evaluator model: Claude Opus 5.5 (claude-opus-5-5), effort low
Next action: Proceed with dependent authoring (/oe, /rubric); keep the observed failure evidence below. Keep the rubric on the per-item calls, dates and makers these traps decide.
Evidence limits: One run only; no average-score or repeatability claim.

**Why Hard:** this run missed six of the new deciding records and one older trap, so the errors come from seven independent causes spread across calls, due dates, makers and scope. It got about 62% of the task right. It used Wed Oct 15 for every ad because it never found Frederick's Sep 30 thread reply in #zombie-match3d (Android US phone ads due Fri Oct 10), so 30 due dates are wrong. It gave the six Julia statics to Martin, who is on leave Oct 6–15. It got 13 of 58 ad calls wrong or left them out, including ART-831, which is missing entirely. The store side, the deliverables, the sharing and the thread reply are correct and usable.

## 1. Inputs and provenance

| Input | Value |
|---|---|
| Prompt | `Evals/task_inputs/04_Prompt.txt`, sha256 `63d7c0713c3bf811b025cf9f73cbcade00c53401971b0d46ad3e2621cd2543d2` (669 bytes), unchanged |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql`, input revision 8, sha256 `0a08dedecd603c6c32f6b58a0ba6c0bddfffee097d54a2218857bb1bd6c08637` (173,106 bytes), the version that passed /injection (injection-static-v2) and /prompt. Never executed; treated as a proposed overlay. |
| Overlay in the run | The run's reads returned revision-8-only content: the review invite description "I'm in LA Thursday so I'll dial in for this one." (`gcal_get_event` evt_d947bf7cd910549b674b1f, event 53), and ART-795/797/805 with only their first comment (`cmt_art795_2` etc. were removed in revision 8; events 109, 113, 129). So the run saw the current overlay. |
| Trajectory | `Evals/task_inputs/opus/trajectory.json`, sha256 `533b233b426b7ae902c95f693d7c7bc80d4c7d626f1e2d60ce56d8be17b3964f` (1,875,570 bytes), uploaded as `trajectory-run-1 (1).json` with this /hardness command; saved as opus input revision 9 and replaces the earlier run (`8ef0af2a…`), which was made against the older SQL revision 6 |
| Model | All 271 assistant events say `claude-opus-5-5`; init `claude-opus-5-5[1m]`; result `modelUsage` canonicalModel `claude-opus-5-5`. Claude Code 2.1.280, session `01f7bca1-6a18-42fc-b325-192a7a9e9fde`, `terminal_reason: completed`, `stop_reason: end_turn`, no permission denials, 0 sub-agents. |
| Hint status | Unhinted: the export has no user or system text with hints (the prompt was passed outside the event stream). The run finds #zombie_marketing and Leonard's message (ts 1759269913.882683) from scratch. |
| Task/source match | `get_time` 2025-10-01T07:00:16Z (task clock); reads and writes are on this task's records. Match. |
| Reference files | None; the prompt uses no attached files. |
| Assignment | Claire Morgan, Art Lead, Design; Marketing and GTM; Authoring; Task type long-horizon; Difficulty mode medium. |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json`, sha256 `da2f4cf0…a1a` |

## 2. Requirement map (authority_contract: prompt-incorporation-v1)

Incorporation: "take his message and do it all for me" pulls in Leonard's 2025-09-30 #zombie_marketing message (SQL L19). It points to the live creatives sheet, Arthur's release calendar, Robert's seasonal direction, Frederick's October UA plan and the maker split ("Martin has the icon and the stills, Marcus has video and end cards"). Records that change single items, dates or makers are facts that answer those asks, not new obligations. Expected answer: the /prompt review's verified Reading A on the same prompt and SQL hashes. Each deciding record was rechecked here in the SQL and against what the run actually read.

Deciding records the run never opened, all in Claire's visible sources (she is a member of C09ATAJ220H, C08R8CHB0QL, C05KNDCHAAG and C0880U9751A; the Gmail copy is in her inbox; Trello is unscoped; REUSED from /injection and /prompt on SQL `0a08dede…8637`):

| Ref | Record (SQL line) | Fact |
|---|---|---|
| FS | Frederick, #zombie-match3d reply `ca1f761b…`, 09-30 23:42Z (L31) | "any new ad going on Android US phone has to be with me by Fri Oct 10, not the 15th. iOS UK stays on the 15th." |
| MV/LV | Martin, #company-internal `c50f7403…` 09-30 14:41Z; Leonard reply `a3734776…` 23:31Z (L13–14) | Martin away Oct 6–15; "<@EMPLOYEE_0005> takes the ad statics while I'm out, store art stays with me"; "julia on the ad statics works for me" |
| MR | Marcus, #zm-animations `2c9fbac7…` 09-25 (L9) | Re-recorded couch alpha 50 (#1935), barrel marketing2 4:5 (#1896) and balloons alpha 50 (1) (#1966), so ART-795/805/797 are on current-build captures |
| RR | Robert reply `258fa1a8…` on Marcus's #zombie-art test `4c2fdbe4…` (L10–12) | "this is the July capture … We can't ship these, they need doing again from the Sep 16 one"; Marcus: "ok, i will redo both" |
| G1 | Frederick email "Unity retention restart", 09-29 23:48Z (L251) | squirrelfail and mrfluffernot landscapes (ART-811, ART-813) left off iOS UK tablet, Android US tablet only, so Skip |
| TR | Trello comment `68d6cff0…` on "Marketing Video Refresh", 09-26 (L322) | end card 001 and its 16:9, 1:1 and 4:5 cuts still show the old zombies and need a re-render (ART-833/834/835/848, so Refresh first) |

| # | Requirement | Expected | Observed (trajectory evidence) | Outcome |
|---|---|---|---|---|
| R1 | Call for every live ad | 58 ads: Halloween version 12, Refresh first 36, Reuse 0, Skip 10; ART-836..839 excluded | 57 ads in `data.py` (event 273) and tracker `gsheets_values_update` Ads!A1 (event 296): Halloween version 12, Refresh first 35, Reuse 2, Skip 8. 13 items wrong or missing (R2–R8). ART-836..839 correctly left out | MATERIAL_FAIL |
| R2 | ART-831 (running, off the sheet) | Included, Refresh first | Never opened (no `linear_get_issue`/`list_comments` for ART-831); absent from tracker, comments and assignments; final reply says "57 ads" | MATERIAL_FAIL |
| R3 | ART-795/797/805 re-recorded (MR) | Halloween version | Refresh first, "Android #456 / #633, Apr" from the ticket comments; #zm-animations never read | MATERIAL_FAIL |
| R4 | ART-808/816 test rejected (RR) | Halloween version, assigned to Marcus | Reuse, "ready now, Frederick please queue it" (comment on ART-808); not assigned. Read Marcus's DM (search event 72) but never opened the #zombie-art thread | MATERIAL_FAIL |
| R5 | ART-811/813 off iOS UK tablet (G1) | Skip | Refresh first, assigned to Marcus, due Oct 15. Gmail search "october UA plan" (event 19) didn't return the restart mail, and no other mail search was run | MATERIAL_FAIL |
| R6 | End card 001 + cuts need re-render (TR) | Refresh first (ART-833/834/835/848) | Halloween version: "Rendered from current-build footage (Android #1529, Aug 4)" (event 280 override). Only the Halloween push card's comments were read (event 68) | MATERIAL_FAIL |
| R7 | ART-809 music baked in | Refresh first (deck: a music-baked master "is re-cut first from a master without music") | Halloween version, "cut from" Marcus's Aug 13 no-music export. The deck rule (event 29) makes the re-cut a refresh step, so the call is wrong, though the comment does say to cut from the no-music master | MATERIAL_FAIL (low weight) |
| R8 | Traps got right: ART-826 via Trello, ART-840 later edit, Android-tablet-only Skips (806, 820, 821, 822, 824, 842, 844, 849), 836..839 paused | As expected | All correct (Trello comment event 68; ART-840 comment event 142; Sep 30 mail event 31) | MET |
| R9 | Due dates (FS + Sep 30 mail) | 30 Android US phone ads due Fri Oct 10; 18 others due Wed Oct 15; Skip none | Every working ad Oct 15 in tracker, comments and all 47 `linear_update_issue` dueDate `2025-10-15`; 30 Oct-10 items wrong (29 written + ART-831 missing); ART-811/813 and ART-816 also misdated through R4/R5 | MATERIAL_FAIL |
| R10 | Makers (MV/LV) | Julia statics ART-825..830 to Julia Lawson; other 42 to Marcus | 47 updates: 41 Marcus, 6 Martin (ART-825..830). Martin is on leave Oct 6–15, so all six statics due Oct 15 sit with someone away. Also 808/816/831 unassigned and 811/813 wrongly assigned | MATERIAL_FAIL |
| R11 | Comment each ad's call and due date on its ART ticket | 58 comments with correct call and date | 57 `linear_create_comment`, no errors; about 36 carry a wrong call or date or are missing | MATERIAL_FAIL (propagated, see §3) |
| R12 | Store calls | Icon and iPad 12.9" set Halloween version; iPhone 6.5" and Google Play sets Reuse | Store tab (event 301) matches | MET |
| R13 | Store-ticket scope (Leonard's #zombie-art reply) | 2 new ART tickets (icon, iPad) to Martin ("store art stays with me") | ART-855 icon, ART-856 iPad, both Martin (events 266, 268); none for the exported sets (thread read event 77) | MET |
| R14 | Store due dates / icon vs "around the 24th" | Tied to the Thu Oct 16 12:00 PT cut | Icon due Tue Oct 14, iPad due Wed Oct 15, both naming the Oct 16 12:00 PT cut; icon "can't be swapped on Oct 24 on its own" | MINOR_GAP (earlier internal date, cut stated) |
| R15 | Plan doc + tracker in Claire's Drive | Doc + Sheet | `gdocs_create_document` (7,270 chars, event 316), `gsheets_create_spreadsheet` + Ads/Store/Key dates/Summary tabs | MET as delivery; contents carry R1–R10 errors |
| R16 | Shared with the review so they can comment | Leonard, Frederick, Martin, Marcus, Robert, Arthur | 12 `gdrive_share_file`, role commenter, all succeeded | MET |
| R17 | Reply in Leonard's thread with both links | thread_ts 1759269913.882683 | `slack_send_message` (event 585), both links, ok:true; repeats the wrong counts and "all due … Oct 15" | MET as delivery |
| R18 | Final response | Accurate summary | Accurately describes what it did (57 tickets, 47 assigned); repeats the same errors | MET as delivery |

## 3. Failures and independent causes

| Cause | Deciding record never read | Items it makes wrong |
|---|---|---|
| C1 | FS, Frederick's Oct 10 reply (#zombie-match3d) | 30 due dates (tracker, comments, Linear dueDate) |
| C2 | MV/LV, Martin's leave post + Leonard's OK (#company-internal) | 6 assignments (ART-825..830) and their maker in comments/tracker |
| C3 | MR, Marcus's re-record post (#zm-animations) | 3 calls (ART-795, 797, 805) and their comments |
| C4 | RR, Robert's rejection (#zombie-art thread) | 2 calls, 2 missed assignments, 1 date (ART-808, 816) |
| C5 | G1, "Unity retention restart" email | 2 calls, 2 wrong assignments and dates (ART-811, 813) |
| C6 | TR, Trello comment on Marketing Video Refresh | 4 calls (ART-833, 834, 835, 848) |
| C7 | ART-831's own ticket (never opened) | 1 ad left out entirely: call, date, comment, assignment |
| C8 | Deck rule on music-baked masters, misapplied | 1 call (ART-809) |

- **Independent causes:** 8 (7 retrieval misses on separate records plus 1 misapplied rule). Each rests on a different record and item; a run could make any one without the others.
- **Failed share:** about 38%, from about 236 core items (58 calls, 58 due dates, 58 comments, 48 assignments, 4 store calls, 2 store tickets with 2 due dates, doc, tracker, sharing, reply). Wrong or missing: 13 calls, about 32 due dates, about 36 comments (each wrong call or date makes its comment wrong), 9 assignments wrong or missing plus 2 extra. Store, delivery and sharing items are correct.
- **Minor gaps:** store due dates Oct 14/15 rather than the Oct 16 12:00 PT cut (cut stated); an unsourced "refreshed base by Wed Oct 8" interim date on Refresh-first rows and comments.

## 4. Gate lines

- **Narrow miss: NO.** 8 independent causes; failed share about 38% of about 236 core items; difficulty mode medium, loss 15%. Scored by the band table.
- **Failure-pattern risk: NO.** Traps, each with its share and this run's result: Frederick's Oct 10 reply, about 25% (wrong); Sep 30 changes mail (tablet Skips + Oct 15), about 18% (right); Julia hand-off, about 5% (wrong); Trello end card note, about 3% (wrong); Robert's rejection of the test cuts, about 3% (wrong); Sep 29 restart mail, about 3% (wrong); Marcus's re-record post, about 3% (wrong); store-ticket scope, about 3% (right); ART-831 off the sheet, about 2% (wrong); ART-826 via Trello, about 2% (right); icon date vs Arthur's calendar, about 2% (right); ART-840 later edit, about 1% (right); ART-809 music, about 1% (wrong); archived ART-836..839 after the restart, about 1% (right). Largest share: about 25%, Frederick's Oct 10 reply. That's under the 30% line, but it's the trap to watch. Don't let any rubric rows stack on it beyond the due dates it decides.
- **Tool calls: 229** (229 main agent, 0 sub-agents). Task type Long-Horizon, minimum 100; not under 90% of it, so the count doesn't affect the score. Breakdown: 57 `linear_list_comments`, 57 `linear_create_comment`, 47 `linear_update_issue`, 12 `gdrive_share_file`, 2 `linear_create_issue`, about 50 research and file-build calls.

## 5. Correct work and usability

Usable as delivered: all four store calls, the two store tickets (right scope and maker), the doc and tracker (built, in Claire's Drive, shared as commenter with all six reviewers), the thread reply with both links, 45 of 58 ad calls, the 18 ads whose correct date is Oct 15, and 39 of 48 assignments. All 128 writes succeeded; the only tool error was an oversized `gcal_list_events` result, which the run worked around. The structure needs no rework. The fix is a list of item edits, but it touches calls, dates and makers on more than half the ad tickets.

## 6. Task/environment defects and unassessed scope

- Capabilities: every deliverable is a native Docs/Sheets/Linear/Slack/Drive write, and each one succeeded (SUPPORTED). No miss is caused by tooling.
- Authority: no miss depends on an unincorporated rule. Each missed record supplies a fact (a date, maker, capture or campaign) answering an ask Leonard's message makes: "who makes what by when", "what needs work first", "every ad we're running".
- Base issue SC-11 (Unity spend/CPI) isn't used; the run cites the CPI only from Frederick's Trello comment. Keep rubric rows off CPI values.
- Unassessed: the plan doc body after the opening sections was skimmed, not checked line by line. It repeats the tracker's per-item calls, which were checked in full.

## 7. Score rationale

Score 4 (Hard, NON-FAIL). Eight independent causes produce material errors across every per-item dimension: about 55% of due dates, 22% of calls, 19% of assignments and about 62% of ticket comments are wrong or missing, and one live ad is left out. The six statics are assigned to someone on leave during their due window. That calls for substantial correction across the result.

Score 3 doesn't fit: the correction isn't bounded to one area or one cause. It spans dates, calls, makers and scope on more than half the tickets.

Score 5 doesn't fit: the central result isn't invalidated. Most calls (45/58), all store decisions, the store tickets, both deliverables, sharing and the thread reply stay correct and usable, and the plan's structure stands.

## 8. Notes for authoring (advice only)

- This run got every trap from the earlier revision right except ART-831 and ART-809. Almost every miss came from the new records added in revision 8, which sit in channels and threads the agent had no pointer to. That's the spread the failure-pattern check needs, so keep the scenario as it is.
- For /oe and /rubric: give each trap its own rows (call and comment for the item-level traps; Linear due date and comment for the Oct 10 rule; assignee for the Julia hand-off). Make ART-831's inclusion its own row. Keep the store due date at the Oct 16 12:00 PT cut and accept an earlier internal date that names the cut.
- Changing the prompt or SQL now would make this run outdated; you'd need a new run and /hardness again.
