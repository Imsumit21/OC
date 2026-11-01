# 08 OE Check — jl-zm-difficulty-baseline (round 7)
Checked 2026-11-01 · Events 45 · Characters 32557 (300–50,000: ok) · Ledger 2026-11-01 (08_OE_Writing_Ledger.md, oe-writing PASS)
/oe prediction (a prediction only; /oe gives the verdict): PASS 5
Completeness 5 · Accuracy 5 · Path feasibility SUPPORTED · Task solvability SUPPORTED_BY_OE

## Inventory
| Segment (quoted start) | Role | Event |
|---|---|---|
| "Read Julia's DM with Leonard" | STEP (×3) | OE 1–3 |
| "Find the rules card the ask names" | STEP (×4) | OE 4–7 |
| "Find the group chat the card's rule 2 names" | STEP (×2) | OE 8–9 |
| "Read Blake's store builds mail" | STEP (×7) | OE 10–16 |
| "Read ZOM-42, the tier spec" | STEP (×9) | OE 17–25 |
| "Work out the register from rules 1 to 4" | STEP | OE 26 |
| "Create the register spreadsheet" | STEP (×5) | OE 27–31 |
| "Share the register with Robert" | STEP (×4) | OE 32–35 |
| "Comment on ZOM-199" | STEP (×9) | OE 36–44 |
| "Reply to Leonard in the DM" | STEP | OE 45 |

No CONTEXT, RESPONSE_DESCRIPTION or NON_ACTION segments: every event is a read, one calculation or one write.

## Coverage
| R / F | Event(s) | Covered / missing / partial | Route (ledger / other valid) |
|---|---|---|---|
| R1 / F1 Leonard's ask and the DM history | OE 1 | covered | ledger: DM history |
| R2 / F2 reply under the ask | OE 2 | covered | ledger: thread replies of the ask |
| R2 / F3 reply under Julia's Sep 29 question | OE 3 | covered | ledger: thread replies of Julia's message |
| R2 / F4–F7 card, comment, checklist, notes doc | OE 4–7 | covered | ledger: Trello card, actions, checklists, attachment → Docs |
| R2 / F20 Robert's columns in the group chat (card rule 2) | OE 8–9 | covered | ledger: group DM history, then the thread under Leonard's question |
| R2 / F8 store builds mail; F9 Blake's reply in its own thread | OE 10–11 | covered | ledger: two Gmail reads (search, then a sender search) |
| R2 / F10–F13 agenda, invite, folder, enrage sheet | OE 12–15 | covered | ledger: Docs, Calendar, Drive, Sheets |
| R2 / deck and Blake's enrage note (rule 5 sources) | OE 16, 19 | covered | ledger F19: Slides, Slack search |
| R2 / F14 ZOM-42; F18 build code | OE 17–18 | covered | ledger: Linear issue, GitHub file contents |
| R2 / F15 population and notes | OE 20–21 | covered | ledger: list team ZOM issues to the end, comments per issue |
| R2 / F16, F21 the four title-match PRs' review comments (243, 244, 265, 271); F17 PR 401 comment; F19 ZOM-303 | OE 22–24 | covered | ledger: GitHub reviews and inline review comments on every title-match PR, Linear issue |
| R3 / F22 Linear assignee, completed_at, priority | OE 25 | covered | ledger: Linear issue fields |
| R3 / F23–F24 register and rules tab | OE 26, 27–30 | covered | ledger: calculation, create, write rows, add tab, write rules |
| R4 / F13 folder | OE 31 | covered | ledger: move into the folder (creating it there is another valid route) |
| R5 / F12 shares | OE 32–35 | covered | ledger: 4 shares, one per event |
| R6 / F25 ticket comments | OE 36–44 (9 events) | covered | ledger: one comment per ticket |
| R7 / F26 DM reply | OE 45 | covered | ledger: DM message (thread or top level) |
| R8 act without asking | all writes | covered | constraint: no event asks Julia |

## Expected-data sign-off
| Event | Claim (quoted) | Source re-read (hg.py pointer) | Value found | Match / minor / wrong / unresolved |
|---|---|---|---|---|
| OE 1 | "tell me when a new player gets their starting tier" | 01_Universe_Inject.sql SQL L52; D05HB64NMQU/1759261706.530914 | seeded ask, Sep 30 19:48:26Z | match |
| OE 2 | "forgot one thing: leave the analytics and tutorial tickets off the list" | 01_Universe_Inject.sql SQL L52; D05HB64NMQU/1759262838.442871 | reply Sep 30 20:07:18Z | match |
| OE 3 | "take 162, 163, 201 and 250 off the list too" | 01_Universe_Inject.sql SQL L60; D05HB64NMQU/1759267002.665190 | reply Sep 30 21:16:42Z | match |
| OE 4 | "The card shows 1 comment, a checklist with 2 items and 1 attachment" | 01_Universe_Inject.sql SQL L78 badges_json | comments 1, checkItems 2, attachments 1 | match |
| OE 5 | "ATK on its own doesn't" | 01_Universe_Inject.sql SQL L88; trello 68dbfa4362a051efb5e0ae45 | comment Sep 30 15:41:55Z | match |
| OE 6 | "rule 7 change: Brian gets edit as well" | 01_Universe_Inject.sql SQL L90; trello 68dc033bf7d24e86b8a9cc67 | checklist Sep 30 16:20:11Z | match |
| OE 7 | "leave ZOM-258 off the list" | 01_Universe_Inject.sql SQL L12; f_f494073fc667097c3c2c6b | doc owner Leonard, Julia reader | match |
| OE 10 | "Arthur Blake to Leonard, Julia, Robert and Brian" | 01_Universe_Inject.sql SQL L103; julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> | to Julia, Leonard, Robert, Brian | match |
| OE 11 | "the starting tier check in the code is cpm > 90, not >= 90" | 01_Universe_Inject.sql SQL L143; julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> | Sep 30 13:26:05Z, own thread julia.lawson@harmonygames.co/1844695547248825769 | match |
| OE 10 | "the only message in its thread" | 01_Universe_Inject.sql SQL L101; julia.lawson@harmonygames.co/1844679607844896665 | 1 message | match |
| OE 8 | "robert anything you want on julia's difficulty list for monday" | 01_Universe_Inject.sql SQL L48; CAFC495E4006/1759226461.318204 | Leonard Sep 30 10:01:01Z, reply_count 1 | match |
| OE 9 | "the day it got marked done, pacific time" | 01_Universe_Inject.sql SQL L50; CAFC495E4006/1759229513.774912 | Robert Sep 30 10:51:53Z | match |
| OE 2 | "put the two builds in the comment (ios 0.3.49 and android 0.3.133)" | 01_Universe_Inject.sql SQL L52; D05HB64NMQU/1759262838.442871 | reply text | match |
| OE 22 | "not tiers: this is a bug fix, enrage was always meant to clear on refill health and push back" | 01_Universe_Inject.sql SQL L184; harmonygames-Games/match3d#271#rc_1 | inline comment under APPROVED empty-body review #271#rev_2, Jul 4 01:05:22Z | match |
| OE 25 | "ZOM-200 was marked done on 2025-06-12" | hg.py get linear --file data.json /issues ZOM-200 completed_at 2025-06-13T01:17:38Z (PDT = UTC-7) | 06-12 PT | match |
| OE 25 | "ZOM-293 assignee Robert, completed never, priority 4 (Low)" | linear data.json /issues ZOM-293 assignee_id usr_Robert, completed_at null, priority 4 | Robert, none, 4 | match |
| OE 12 | "One sheet with two tabs, Tickets and Rules in force" | 01_Universe_Inject.sql SQL L10; f_9ec79682ff351aa466364a | agenda body | match |
| OE 13 | "brian.foster@harmonygames.co. So the shares go to" | 01_Universe_Inject.sql SQL L164; evt_91674a9c23d012a9ac34da | 5 attendees incl. Julia | match |
| OE 14 | "Folder "ZM Difficulty", created Jun 13 2025; Julia can write to it" | 01_Universe_Inject.sql SQL L8; d_96489e1e00a56685625939 | permissions julia writer | match |
| OE 15 | "Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP): speed not copied yet" | 01_Universe_Inject.sql SQL L14; f_0ba93ae0238d9ed4178212#0 | Live tab last row | match |
| OE 19 | "90 or more starts you on tier 1" | 01_Universe_Inject.sql SQL L16; f_048bf5e69f8e7f1a659a5c | deck slide text | match |
| OE 16 | "enrage adds speed and damage only" | 01_Universe_Inject.sql SQL L64; C090N54TG79/1756912929.304417 | Blake Sep 3 15:22:09Z | match |
| OE 17 | "We promote if if win rate is 80% or higher" | hg.py get linear --file data.json /issues ZOM-42 description | verbatim incl. the doubled 'if' | match |
| OE 18 | "if (totalGames == 10)" | HarmonyGames_GitHub match3d Assets/Scripts/DynamicDifficulty/TierManager.cs line 31 | line 31 | match |
| OE 18 | "return GetTotalWins() + GetTotalLosses();" | match3d Assets/Scripts/Player/WinHistory.cs line 166 | line 166 | match |
| OE 20 | "ZOM-203 and ZOM-276 also match but are Duplicates" | hg.py get linear --file data.json /issues ZOM-203, ZOM-276 state Duplicate | Duplicate | match |
| OE 20 | "31 title matches that are not in the Duplicate state" | linear data.json /issues: 33 ZOM title matches up to Aug 31 minus 2 Duplicates | 31 | match |
| OE 21 | "tiers: closing. checked on the dev build" | 01_Universe_Inject.sql SQL L287; cmt_df69e4a92767cbff0000 | Blake on ZOM-281, Jun 27 | match |
| OE 21 | "no other comment on a ZOM issue starts with" | hg.py search linear "tiers:" over linear data.json /comments → 0 base hits; seeded only the 5 | 5 | match |
| OE 22 | "not tiers: this is level settings tooling for the designers" | 01_Universe_Inject.sql SQL L180; harmonygames-Games/match3d#265#rc_7 | inline comment, empty-body review #265#rev_8 | match |
| OE 22 | "PR 243 has no reviews and PR 244 has only the automated review bot's reviews" | github data.json /reviews for match3d PRs 243, 244 (bot PERSON_6026_GITHUB_USERNAME, 'Actionable comments posted') | 243: none; 244: 2 bot | match |
| OE 22 | "Only four title matches have a PR in the match3d repo" | github data.json /pull_requests: titles and bodies naming the 31 title matches → match3d#243, #244, #265, #271 only | 4 PRs | match |
| OE 19 | "because the build (OE 18) sets the tier when the player's 10th game ends" | TierManager.cs line 31 (read in OE 18, before OE 19) | totalGames == 10 | match |
| OE 23 | "they shared one since ZOM-282" | 01_Universe_Inject.sql SQL L173; harmonygames-Games/match3d#401#c_2 | Aug 25 17:02:28Z | match |
| OE 24 | "we also need to demote the level difficulty for the level" | hg.py get linear --file data.json /issues ZOM-303 description | substring of the Solution line | match |
| OE 26 | "Counts: 15 Live, 4 Editor only (ZOM-173, ZOM-200, ZOM-277, ZOM-315), 3 Not shipped (ZOM-202, ZOM-280, ZOM-293)" | support/task_work/jl_difficulty/truth.json /counts less ZOM-295 (r7/truth7.py) | 15/4/3/1 | match |

## Findings
| # | Severity | Component | Event | Quoted span | Rule (Eval § / source) | What is wrong | Evidence (ledger fact + source pointer) |
|---|---|---|---|---|---|---|---|
| 1 | ADVISORY | Readability | OE 21 | "Read the comments on every ZOM issue created up to Aug 31" | screen 44 (population reads may stay one event) | one read over ~498 issues makes a long event; allowed | F15; cmt_df69e4a92767cbff0000 |
| 2 | ADVISORY | Route | OE 31 | "Move the spreadsheet into the ZM Difficulty folder" | Eval 3.1 (any valid route) | a run that creates the file inside the folder needs no move; both reach the same end state | F13; d_96489e1e00a56685625939 |

## Pre-verdict sweep
| Eval 4.0 check (7) | Result |
|---|---|
| one wrong count/ID/channel/tool | none: 31 title matches, 23 rows, 15/4/3/1, 5 attendees, 9 comments, Robert's columns re-read (sign-off) |
| one missing write | none: create, rows, tab, rules, move, 4 shares, 9 comments, 1 DM reply |
| one Expected fact with no retrieving event | none: every value in OE 26 and the writes is read in OE 1–25; no event cites a later one |
| one act-vs-defer conflict | none: ledger §C defer search complete |
| one non-action or final-response event | none: OE 26 is a calculation with stated results |
| one prompt-forbidden write | none: no comment on ZOM-162/163/201/250, no new issues, Brian not writer |
| one missing recovery/wait event | none: Friction: none (03_Error_Async_Config.txt) |

## Advisory (no effect on the prediction)
| Event | Note |
|---|---|
| all | the field blocks pasting: 32557 characters to type; long quotes (OE 4, 11, 21, 28) can be trimmed to the decisive sentences if needed |

## Tally
Blocking 0 (incomplete 0 · inaccurate 0 · length 0) · moderate 0 (non-action 0 · final-response 0 · format 0) · minor 0 · unresolved 0 · advisory 2

## Self-review
Walked `Evals/2_Oracle_Events_Eval.md` 1.2, 1.3, the HARD GATE, 2.1–2.7, 3.1–3.6 and 4.0 in order against this report; re-verified the sign-off values this run through `tools/hg.py` reads, the match3d export and the SQL rows (b64bc2f2c6dc). Round 7 rebuild (r7/build_oe_r7.py reads every quote from the SQL row): OE 2 adds the builds request; OE 4 carries the current card (rule 2 names Robert's group chat, rule 3 and rule 6 name Blake's reply); OE 8–9 read Robert's group chat and its thread; OE 10–11 read Blake's two mails, the reply in its own thread; OE 22 finds the 'not tiers' marks on PR 265 and PR 271; OE 25 reads assignee, completed_at and priority; OE 26 has 23 rows (15 Live); OE 28 writes Robert's columns with the Pacific day (UTC day also accepted per /prompt r14); OE 38–44 name the two builds; OE 45 says 23 / 15. Earlier /oe r1 fixes kept: the deck follows the code read (now OE 19 citing OE 11, 16, 17, 18); every title-match PR is checked; OE 26 gives a reason per non-Live row. Sweep: every (OE n) citation re-checked and points to an earlier event that holds the value.

| Counter-reading | Resolution (evidence) |
|---|---|
| Counter: R1 covered: OE 1 could read the wrong DM message | the ask is the newest message before the clock in the DM (D05HB64NMQU/1759261706.530914) |
| Counter: R2 F2: the reply might not be reachable | reply_count 1 on the ask; check-sql YES (ledger §B) |
| Counter: R2 F3: Julia's Sep 29 thread could be ignored as her own | its reply is Leonard's (D05HB64NMQU/1759267002.665190), the latest instruction |
| Counter: R2 F4–F7: the DD card could be the one meant | the ask says 'on the zm roadmap board'; the DD card is on another board (683dbef4e319167a802bd888) |
| Counter: R2 F8: the mail's first message alone suffices | the > 90 fact and the stripped tooling are only in the reply, its own thread (julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>) |
| Counter: R2 F20: Robert's columns are optional | card rule 2: 'Layout as in the session agenda, plus the three things Robert asked for' (68daca5871dba40417a00383); OE 9 quotes the reply |
| Counter: R2 F21: Blake approved PR 271, so ZOM-295 stays | rule 1 keys on the 'not tiers' mark; harmonygames-Games/match3d#271#rc_1 sits under the approval harmonygames-Games/match3d#271#rev_2 |
| Counter: R3 F22: the done day must be the UTC day Linear shows | Robert asks for pacific time (CAFC495E4006/1759229513.774912); OE 28 accepts the UTC day too, per /prompt r14 |
| Counter: R2 F10–F13: the invite could need Robert only | rule 7 'everyone on the tuning session invite'; 5 attendees (evt_91674a9c23d012a9ac34da) |
| Counter: R2 deck: OE 19 is redundant | rule 5 names the deck; its stale values are traps the later events overturn; /oe does not score redundancy |
| Counter: R2 F14/F18: ZOM-42's '10 level' governs the timing | rule 5 'go by the build' for the starting tier; TierManager.cs line 31 |
| Counter: R2 F15: the population could be title matches only | rule 1 adds 'tiers:' notes on any ticket; ZOM-281 has no title word (cmt_df69e4a92767cbff0000) |
| Counter: R2 F16–F17: #401 replaces ZOM-282 | rule 4 'PRs that change or split its numbers don't' (harmonygames-Games/match3d#401#c_2) |
| Counter: R3 F23: 27 rows (no Sep 29 thread) | OE 3 drops four more (D05HB64NMQU/1759267002.665190) |
| Counter: R4 F13: the move is missing for a create-in-folder run | Eval 3.1 credits any valid route (Finding 2) |
| Counter: R5 F12: Brian writer per the checklist | Leonard's 21:16Z reply takes it back; OE 6 and OE 3 say so |
| Counter: R6 F25: comments on the four dropped tickets | 'no comments on them either' (OE 3) |
| Counter: R7 F26: keys should include the dropped Editor only tickets | they are off the list; the reply lists the register's keys |
| Counter: R8: OE should confirm with Julia | the prompt says 'no need to check with me first' |
| Counter: /oe r1 finding 1: OE 19 (deck) still cites a later event | the deck follows the code read; it cites OE 11, OE 16, OE 17, OE 18, all earlier (f_048bf5e69f8e7f1a659a5c) |
| Counter: /oe r1 finding 2: another title match could have a PR with a not-tiers review | only 4 PRs name a title-match key (match3d#243, #244, #265, #271); harmonygames-Games/match3d#265#rc_7 and harmonygames-Games/match3d#271#rc_1 say not tiers |
| Counter: OE 26 reasons could add an unretrieved fact | each reason cites OE 10, OE 11 or OE 21 (cmt_bb9c4deb176b2c894ca6 ZOM-173, cmt_b0aa45d307c981ce4487 ZOM-277) |
| Counter: Finding 1 ADVISORY could be MULTIPLE_ACTIONS | a population read is not two writes (screen 44); F15, cmt_df69e4a92767cbff0000 |
| Counter: Finding 2 ADVISORY could be INACCURATE (wrong tool) | gdrive_move_file exists in the catalog with fileId and newParentId; F13, d_96489e1e00a56685625939 |

Unresolved: none.

```
STAGE GATE oe-check: PASS — Task_Authoring-2/task_inputs · 08_OE_Check.md#474cfa3c1404 · 08_Oracle_Events.md#047a50102955 · blocking 0 · warnings 0 · checks 17
[PASS] structure.outputs: 1 output(s) present: 08_OE_Check.md
[PASS] structure.inputs: 2 input(s) present: 08_Oracle_Events.md, 08_OE_Writing_Ledger.md
[PASS] structure.fresh: every output newer than its inputs (08_Oracle_Events.md, 08_OE_Writing_Ledger.md)
[PASS] chain.oe-writing: upstream 'oe-writing' PASS pasted and current (08_OE_Writing_Ledger.md#dfba93b14b1f)
[PASS] structure.sections: 7 required sections present and non-empty (08_OE_Check.md)
[PASS] structure.placeholders: no placeholders in 08_OE_Check.md
[PASS] structure.header_counts: header matches 08_Oracle_Events.md (45 events, 32557 chars)
[PASS] structure.prediction: /oe prediction line present
[PASS] evidence.quoted_spans: 2 quoted span(s) verified as exact substrings of 08_Oracle_Events.md
[PASS] evidence.findings_evidence: 2/2 items carry a source pointer (min 100%)
[PASS] evidence.signoff_reread: 36/36 items carry a source pointer (min 100%)
[PASS] structure.sweep: pre-verdict sweep has 7/7 rows
[PASS] structure.tally: tally Blocking 0 vs 0 BLOCKING findings
[PASS] review.counter_readings: 24 evidenced counter-readings (of 24 found; need ≥ 20) in 08_OE_Check.md
[PASS] review.coverage: self-review addresses all 1 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## Reminders
- The tool-call minimum is measured on the golden run or the 6-rollout average, never on the OE count.
- Type the events exactly as saved in 08_Oracle_Events.md, then run /oe.

