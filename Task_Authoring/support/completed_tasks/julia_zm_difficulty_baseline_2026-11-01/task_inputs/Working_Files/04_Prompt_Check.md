# Prompt Check — jl-zm-difficulty-baseline
> Prompt: 04_Prompt.txt · 103 words · sha256 22f26066688c · checked 2026-10-30 against 04_Prompt_Writing_Brief.md (2026-10-30)
> Suggested wording allowed. Typos and capitalisation are not assessed (scored by /prompt §1.2).

## Summary

Fail 0 · Non-fail 0 · Advisory 2 (C20, C23) · UNVERIFIED 0 · checks clean: C1–C19, C21, C22, C24.
Predicted /prompt band: PASS. Status: READY FOR /prompt.

Revision 9 (hardening round 3, /home/sumit/Downloads/6adfee3ef9092601a61245bb_1a_hardness (2).md): Opus run 3 found every earlier lever, so two levers were added on surfaces no run has read. Card rule 1 now adds "It works the other way too: a title match Blake marked 'not tiers' in his review on its PR stays off"; Blake's empty-body review on match3d#265 carries an inline comment "not tiers: …" (ZOM-312 off). Leonard's "notes for monday" doc, attached to the card, drops ZOM-258, gives Arthur view access and asks the reply to say which ticket replaced which. Final state: 28 rows (16/8/3/1), 13 comments, Arthur reader. SQL sha256 2ee488e28ab5. Prompt unchanged. Revision 8: /prompt attempt 7 (/home/sumit/Downloads/6adfee3ef9092601a61245bb_1_prompt (7).md, FAIL 2) found one fork (S): rule 5's "where a write-up and the build disagree, go by the build" also reached promotion and demotion, and WinHistory.cs counts the first 10/4 games since the last tier change while the deck and ZOM-42 say the latest. Rule 5 now limits the build clause to when a new player gets the starting tier and says to write which games promotion and demotion look at the way ZOM-42 words it (up to the most recent 10; 4 losses in a row at any time). SQL sha256 52c581f442c1. Prompt unchanged. Revision 7 (hardening round 2): Opus run 2 found both round-1 levers, so Blake's "tiers:" note on ZOM-281 (assigned to someone else; card rule 1 now "any ticket Blake counts as tier work") and Leonard's question "when a new player gets their starting tier" (rule 5: "where a write-up and the build disagree, go by the build"; answer: after the first 10 games, won or lost) were added. Final state: 30 rows (17/9/3/1). Prompt unchanged. Revision 6 (hardening round 1, 01a_Hardening_Report.md): /hardness scored Easy, so Leonard's thread reply under the ask (D05HB64NMQU/1759262838.442871: drop ZOM-30, 49, 50, 161, 262, 275; keys in the reply) and the card checklist (68dc033bf7d24e86b8a9cc67: rule 6 change, rule 7 change) were added. Final state: 29 rows (16/9/3/1), 14 comments, Brian writer. Prompt unchanged; the prompt's "go through his ask and everything it points to" and "if his rules say something needs to happen on the tickets" incorporate both. Revision 5: /prompt attempt 4 (6adfee3ef9092601a61245bb_1_prompt (3).md) scored everything 5 except UGT: (1) whether the rules tab lists Mailman, Mayor2 and PartyGirl at 0.8/0.8 or as not copied yet; (2) whether ZOM-271's "ATK POWER" counts. Card rule 5 now says to copy the sheet's Live tab as it stands, including "not copied yet", and Leonard's comment says attack power must be written out, not ATK. A scan of all ZOM titles up to Aug 31 found no other near-miss form. Prompt unchanged. Revision 4: /injection attempt 4 failed the enrage sheet's History date (values reached main 2025-09-06 via PR #417); the sheet is now dated 2025-09-08, and Mailman, Mayor2 and PartyGirl are marked "not copied yet". Prompt unchanged. Revision 3: /prompt attempt 3 (6adfee3ef9092601a61245bb_1_prompt (2).md) scored every prompt dimension 5 and failed only Cross-Service Coherence: the enrage sheet's Mailman, Mayor2 and PartyGirl rows had values no match3d commit before the cut set. Those rows are removed (MonsterBase 0.8/0.8 covers them), and card rule 4 now says "another ticket's closing note" (injection advisory A6). Prompt unchanged. Revision 2: /prompt attempt 2 (6adfee3ef9092601a61245bb_1_prompt (1).md, FAIL 2) closed every earlier fork but found ZOM-250 Editor only vs Replaced by ZOM-277, and hp texts contradicting commit b511fcbcd5. Rule 4 is now record-based (only a replacing closing note counts), which closes every such pair; the hp texts now match the commit. Prompt unchanged. Revision 1: /prompt attempt 6adfee3ef9092601a61245bb_1 (FAIL 2) found three record-driven UGT forks (open rule-6 comment set, ZOM-282 Live vs Replaced by match3d#401, the Apr 21 UTC/Pacific edge), a hidden destination and audience (Contrived), and a card description older than the records it cites (Coherence). All five are fixed. The card's rules 1, 4 and 6 are rewritten, and an updateCard action at 2025-09-30T14:04:31Z is added (re-dated after /injection attempt 2, F1) (SQL sha256 6972a45038e9, local injection gate PASS). The prompt now names the ZM Difficulty folder and Monday's tuning invite. The evaluator's derivation also showed that ZOM-315 is Editor only (StatsPanel.cs). The answer key and ZOM-315's note are corrected: 22 Live, 9 Editor only, 3 Not shipped, 1 Replaced.

Revision 11 (hardening round 4, after six baseline runs on SQL 2ee488e28ab5: four runs fully correct, two missed the DM thread reply): Julia's Sep 29 DM question to Leonard ('anything you need from me before monday's tuning session?') and Leonard's reply in its thread, 2025-09-30T21:16:42Z ('one more for the baseline: leave the level editor tickets off too (162, 163, 201 and 250) … so no comments on them either. and scratch brian editing … comment access is enough for brian'). Answer: 24 tickets (16 / 4 / 3 / 1), 9 comments, Robert writer, Brian and Leonard commenter, Arthur reader, 7 keys in the reply. The reply is Leonard's and names 'the baseline', so it is part of his ask; it is later than the checklist (16:20Z), so Brian's role is settled by time. Also folds in the PR #401 updated_at UPDATE (/prompt attempt 9 DR3). SQL 2ee488e28ab5 → cd185b05da3d → dd7536cdea3f (prompt-11 fork fix) (172 INSERT, 3 UPDATE). Prompt unchanged.

Revision 12 (/prompt attempt 11, /home/sumit/Downloads/6adfee3ef9092601a61245bb_1_prompt (11).md, FAIL 2 on Unique Ground Truth and Clarity, fork Y): Leonard's reply said 'leave the level editor tickets off too (162, 163, 201 and 250), the designers keep their own list for those', and ZOM-173 (label Level Editor), ZOM-277 and ZOM-315 are level-editor work too, so the list read as an open category. Fixed per the report's option (a): the reply now reads 'take 162, 163, 201 and 250 off the list too. just those four, on top of the ones i already left off. no comments on them either …' — no category label, no reason that covers other tickets, an explicitly closed list. ZOM-173, 277 and 315 stay Editor only with comments; ZOM-202 stays Not shipped. Answer unchanged: 24 tickets (16 / 4 / 3 / 1), 9 comments.

Revision 10 (/prompt attempt 9, /home/sumit/Downloads/6adfee3ef9092601a61245bb_1_prompt (9).md, NON-FAIL 3 on Cross-Service Coherence): the injected comment match3d#401#c_2 (2025-08-25T17:02:28Z) post-dated base PR #401 updated_at 16:42:14Z; base GitHub never has a comment after its PR's updated_at. The one-line fix (UPDATE github.github_pull_requests SET updated_at = '2025-08-25T17:02:28Z' for #401) was built and checked, then withdrawn on the author's decision: /prompt NON-FAIL 3 COMPLETE clears the gate, and keeping SQL 2ee488e28ab5 keeps the matching /injection PASS and /hardness band 3. Swept the same class: the only other injected GitHub rows (#265 rev_8 / rc_7 at 17:50:12Z) precede #265 updated_at 18:01:36Z, as the report confirms. The prompt is unchanged; no graded value moves.

## Findings

| # | Check | Dimension · severity | Quoted span | Rule (source) | Defect |
|---|---|---|---|---|---|
| 1 | C20 | Today's date · Advisory | "on tuesday" | Prompt Writing §4.2 asks for absolute dates; /prompt §2.8 allows clear relative wording | relative day; resolves to Tue Sep 30 (the ask D05HB64NMQU/1759261706.530914, 19:48Z / 12:48 PT) before the clock; the last /prompt run scored it 5 |
| 2 | C23 | Originality · Advisory | "a baseline of the zm difficulty system" | /prompt §2.9 is N/A without supplied samples | no samples supplied |

## UGT readings

| Deliverable | Reading A | Reading B | Resolution and evidence |
|---|---|---|---|
| W1 register | a Google Sheet in the ZM Difficulty folder with tabs Tickets (35 rows) and Rules in force | a sheet elsewhere, or one tab | the prompt names the folder; card rule 2 → agenda "One sheet with two tabs" (68daca5871dba40417a00383; f_9ec79682ff351aa466364a) |
| W1 rules card | the ZM ROADMAP card | the Domino Delights "Difficulty baseline" card | the ask names "the difficulty baseline card on the zm roadmap board" (D05HB64NMQU/1759261706.530914); the DD card is another board/game (683dbef4e319167a802bd888) |
| W1 membership | 24 tickets created up to Aug 31 incl. ZOM-281 (Blake's tiers: note cmt_df69e4a92767cbff0000), without ZOM-312 (Blake's 'not tiers' inline comment on his review of match3d#265, harmonygames-Games/match3d#265#rc_7), ZOM-258 (Leonard's 'notes for monday' doc attached to the card) and ZOM-30, 49, 50, 161, 262, 275 (Leonard's thread reply D05HB64NMQU/1759262838.442871) and ZOM-162, 163, 201, 250 (Leonard's reply in the thread under Julia's Sep 29 question, D05HB64NMQU/1759267002.665190) (ZOM-271 "ATK POWER" out: card comment 68dbfa4362a051efb5e0ae45 "written out (ATK on its own doesn't)") | 33 (Apr 21 read in Pacific time drops ZOM-23, ZOM-30) | card rule 1 now has no start date ("created up to Aug 31 (so everything since we started ZM)", 68daca5871dba40417a00383); no title match before ZOM-23 (first ZOM ticket 2025-04-18T19:56:53Z) and none 2025-08-30 – 2025-09-02 — same set in UTC and Pacific |
| W1 Replaced set | only ZOM-254 (replaced by ZOM-282) | ZOM-282 by match3d#401; ZOM-250 by ZOM-277 (last /prompt run, F1); ZOM-246 by ZOM-263; ZOM-274 by ZOM-295; ZOM-262 by ZOM-275 | card rule 4 "Replaced: only when another ticket's closing note says it replaces this one … a ticket players never had stays Editor only or Not shipped" (68daca5871dba40417a00383); only ZOM-282's closing note (cmt_912bdd42ad5c8d51521f) says it replaces a ticket |
| W1 ZOM-315 | Editor only | Live | its note says it is the editor stats-panel total (seeded note on ZOM-315); "Total Attack Power" exists only in Assets/Scripts/LevelEditor/UI/StatsPanel.cs; card rule 3 via Blake's mail (julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>) strips the level editor |
| W1 starting tier | > 90 | >= 90 (ZOM-199; the deck f_048bf5e69f8e7f1a659a5c) | Blake's reply 2025-09-30T13:26Z names the build's check (julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>); ZOM-42 agrees |
| W2 shares | Robert writer; Brian and Leonard commenter (Leonard's later reply 2025-09-30T21:16Z takes back the checklist's 16:20Z 'Brian gets edit'); Arthur reader (Leonard's notes doc f_f494073fc667097c3c2c6b, attached to the card) | other roles, or Vincent too | the prompt says "everyone on monday's tuning invite"; card rule 7 "Robert can edit, everyone else comments" (68daca5871dba40417a00383); attendees on evt_91674a9c23d012a9ac34da |
| W3 ticket comments | ZOM-199 (> 90), ZOM-254 (replaced by ZOM-282), and each of the 4 Editor only and 3 Not shipped tickets (checklist 68dc033bf7d24e86b8a9cc67 rule 6 change); none on ZOM-162, 163, 201, 250 | also ZOM-42 ("6-7 levels"), ZOM-275 (tutorial text), ZOM-282, or Not shipped tickets | card rule 6 "only two kinds: where Blake's store builds mail or his reply to it says a ticket's text is wrong … and Replaced tickets … Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included" (68daca5871dba40417a00383); only the reply names a ticket (ZOM-199) |
| W4 reply | Leonard's DM with 24 / 16 Live / 4 Editor only / 3 Not shipped / 1 Replaced, which ticket replaced which (ZOM-254 by ZOM-282, Leonard's notes doc), the Not shipped and Editor only keys (D05HB64NMQU/1759262838.442871), and the starting tier after the first 10 games, won or lost (card rule 5 "go by the build"; TierManager.cs) | a post in #zombie-design (Vincent) | the prompt says "reply to leonard in the dm"; Vincent is not the requester (C090N54TG79/1759248760.118527) |

Cheapest-choice test (C6 step 3): "everyone on monday's tuning invite" still needs the invite read (evt_91674a9c23d012a9ac34da) and the card's roles. The counts in "what he asked for" still need the 109-ticket review.

## Verification log

| Span | Type | Universe record (locator) | Result |
|---|---|---|---|
| "leonard dm'd me on tuesday" | person / channel / date | D05HB64NMQU/1759261706.530914 (EMPLOYEE_0038_SLACK_ID = Leonard Hayes, 2025-09-30T19:48:26Z, a Tuesday); D05HB64NMQU members include EMPLOYEE_0005_SLACK_ID and EMPLOYEE_0038_SLACK_ID | true |
| "a baseline of the zm difficulty system" | event | D05HB64NMQU/1759261706.530914 "i want a baseline of the difficulty system from you" | true |
| "before monday's tuning session" | event / date | evt_91674a9c23d012a9ac34da 2025-10-06T17:00Z (Monday) | true |
| "build the register the way he set it up" | person / doc | 68daca5871dba40417a00383, createCard 68daca5845e48874fb98e25a and updateCard by Leonard (PERSON_6094_TRELLO_USER_ID) | true |
| "put it in the zm difficulty folder" | doc | d_96489e1e00a56685625939 "ZM Difficulty" (Leonard's, Julia writer; Julia's sheet f_0ba93ae0238d9ed4178212 inside) | true |
| "share it with everyone on monday's tuning invite" | person / event | evt_91674a9c23d012a9ac34da "ZM difficulty tuning" on Julia's calendar; attendees Leonard, Julia, Robert, Arthur, Brian | true |
| "if his rules say something needs to happen on the tickets" | state | 68daca5871dba40417a00383 rule 6 | true (conditional, not a premise) |
| "reply to leonard in the dm with what he asked for" | event | D05HB64NMQU/1759261706.530914 "reply here when it's in the folder with how many tickets made the list and how many of each status" | true |

## Brief coverage

| Brief item | Present in the prompt |
|---|---|
| §4 W1 register | "build the register the way he set it up" |
| §4 W1/W2 placement | "put it in the zm difficulty folder" |
| §4 W2 shares | "share it with everyone on monday's tuning invite" |
| §4 W3 Linear comments | "if his rules say something needs to happen on the tickets, go ahead and do that too" |
| §4 W4 reply | "reply to leonard in the dm with what he asked for" |
| §6 anchor A1 | "leonard dm'd me on tuesday" |
| §7 deadline | "before monday's tuning session" |

## Self-review

Walked `Evals/1_Prompt_Eval.md` Phases 1–3 in order against 04_Prompt.txt (hash 22f26066688c unchanged before and after this run). Every quoted span above is an exact substring (verified by the gate). Each fork the last /prompt run raised was re-checked against the rewritten card (68daca5871dba40417a00383).

| Check | Counter-reading | Resolution (evidence) |
|---|---|---|
| C1 | Counter: field length | 103 words, inside 20–4,000 |
| C2 | Counter: assignment incomplete | 00_Assigments.md has all five axes; julia_lawson resolves to one roster entry (julia.lawson@harmonygames.co) |
| C3 | Counter: a PM wouldn't own a build-state register | Leonard asked Julia directly (D05HB64NMQU/1759261706.530914); the card says "Julia owns this one" (68daca5871dba40417a00383); last /prompt run Persona 5 |
| C4 | Counter: the work is not Retrieval / Engineering Ops | last /prompt run scored both 5; the work is reconciling 109 tickets against the store builds (julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>) |
| C5 | Counter: naming the folder and invite carries the recipe | they are a destination and an audience Julia knows; the roles, rules and sources stay in the card (68daca5871dba40417a00383); Ambiguity, Dynamic Change and Multi-Source remain load-bearing (brief §8) |
| C6 | Counter: the comment set, ZOM-282 and the window still fork | UGT readings above: card rules 1, 4 and 6 now close each fork; the comment set is {ZOM-199, ZOM-254} (68daca5871dba40417a00383; julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>) |
| C7 | Counter: "if his rules say something needs to happen on the tickets" splits into two write sets | rule 6 now names exactly two comment kinds and says every other ticket stays as it is (68daca5871dba40417a00383); no "I'll" assigns a write to Julia |
| C8 | Counter: a pointed-to record might hand over answers | the card states rules, not rows or counts (68daca5871dba40417a00383); the invite gives names, not roles (evt_91674a9c23d012a9ac34da) |
| C9 | Counter: pre-solved by naming findings | no ticket, status, count, rule value or share role appears (brief §9) |
| C10 | Counter: naming the folder and invite collapses discovery | neither is a finding: the folder is the write target, and the invite's attendee list still has to be read (evt_91674a9c23d012a9ac34da); the card, mail, sheet and deck stay unnamed |
| C11 | Counter: no write depends on the investigation | the register, ticket comments and reply all carry findings (brief §3) |
| C12 | Counter: only Linear and Slack carry weight | 10 services carry weight (01_Hardness_Manifest.json); HARDNESS GATE (long): PASS in the dossier |
| C13 | Counter: the asks are bolt-ons | every write serves one baseline for one session (D05HB64NMQU/1759261706.530914) |
| C14 | Counter: a tool is named | no function, parameter or server name; "folder", "invite", "dm" and "tickets" are natural nouns (prompt_qc_examples row 103) |
| C15 | Counter: the prompt scripts steps | it lists the deliverables in order (screen 24 skeleton), not sources or method; the last /prompt run rejected Command List (DR12) |
| C16 | Counter: hidden destination and recipients (last run's Contrived 2) | fixed: "put it in the zm difficulty folder and share it with everyone on monday's tuning invite" names both (d_96489e1e00a56685625939; evt_91674a9c23d012a9ac34da); no column list, format rule or opaque id |
| C17 | Counter: "the zm difficulty folder" or "monday's tuning invite" is a near-match | folder name "ZM Difficulty" (d_96489e1e00a56685625939); event "ZM difficulty tuning" Mon 2025-10-06 on Julia's calendar (evt_91674a9c23d012a9ac34da) |
| C18 | Counter: a write is impossible | gsheets_create_spreadsheet, gsheets_batch_update, gdrive_move_file, gdrive_share_file, linear_create_comment and slack_send_message exist (Evals/references/tools/catalog.json) |
| C19 | Counter: a scoped read is invisible | check-sql PASS for julia_lawson on the new SQL (dossier §1.E: D05HB64NMQU/1759261706.530914, evt_91674a9c23d012a9ac34da, d_96489e1e00a56685625939) |
| C20 | Counter: "on tuesday" is relative | Advisory only: resolves to Tue Sep 30, before the clock 2025-10-01T00:00Z (D05HB64NMQU/1759261706.530914) |
| C21 | Counter: friction announced | 03_Error_Async_Config.txt is Friction: none |
| C22 | Counter: the sheet's per-monster rows disagree with the committed prefab values (attempt 3 Coherence 2) | fixed: Live tab keeps only the 10 rows with committed values (f_0ba93ae0238d9ed4178212); Mailman, Mayor2 and PartyGirl fall to MonsterBase 0.8/0.8, as the evaluator's history read of commits 6a4d8ba57e and 476a02949b shows. Earlier: seeded hp claims contradicted commit b511fcbcd5 (attempt 2 Coherence 3); the card cites later records (attempt 1) | fixed: ZOM-282 note, #401 comment and sheet History now say hp was switched off 2025-06-19 (cmt_912bdd42ad5c8d51521f, harmonygames-Games/match3d#401#c_2, f_0ba93ae0238d9ed4178212); updateCard by Leonard at 2025-09-30T14:04:31Z, after Blake's mail (09:12:44Z), his reply (13:26:05Z) and the agenda/invite (Sep 29 18:24–18:31Z), before the comment (15:41:55Z); local injection gate PASS on SQL sha256 6972a45038e9 |
| C23 | Counter: lifted from a sample | no samples supplied (Advisory) |
| C24 | Counter: only investigate + one Slack post | writes over Sheets, Drive, Linear and Slack (brief §4) |

Unresolved: none.

```
STAGE GATE prompt-check: PASS — Task_Authoring-2/task_inputs · 04_Prompt_Check.md#7ea3a085bbd9 · 04_Prompt.txt#22f26066688c · blocking 0 · warnings 0 · checks 19
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Check.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 04_Prompt_Writing_Brief.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 04_Prompt_Writing_Brief.md)
[PASS] chain.prompt-writing: upstream 'prompt-writing' PASS pasted and current (04_Prompt_Writing_Brief.md#382253dc20c2)
[PASS] structure.sections: 7 required sections present and non-empty (04_Prompt_Check.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Check.md
[PASS] structure.prompt_hash: header ties the report to 04_Prompt.txt (103 words, sha256 22f26066688c)
[PASS] evidence.quoted_spans: 2 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] evidence.coverage_spans: 7 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] structure.c_checks: every C1–C24 has a recorded result
[PASS] evidence.verification_log: 8/8 items carry a source pointer (min 100%)
[PASS] structure.summary_band: summary band present
[PASS] structure.summary_status: summary status present
[PASS] tier.hardness: Long Horizon → --profile long: manifest present, hardness_gate PASS pasted in the dossier and current
[PASS] tier.hardness_rerun: hardness_gate --profile long re-run on the current manifest + SQL: PASS
[PASS] review.counter_readings: 24 evidenced counter-readings (of 24 found; need ≥ 24) in 04_Prompt_Check.md
[PASS] review.coverage: self-review addresses all 24 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```




















## Route

No Fail: send the new SQL (SQL sha256 dd7536cdea3f) to /injection first, then paste 04_Prompt.txt exactly as saved into /prompt with all five assignment fields and 'Friction: none'. Then /create-humantime.
