# P4 deep recheck findings (rev14, stands alone for this hash)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Inputs: 04_Prompt.txt; 01_Universe_Inject.sql (sha256 edae63f3e83852f212c19892a9c9cf7304404b80db3178f92a470f301a598e13, verified); prev/01_Universe_Inject.rev13.sql (sha256 1f2175a2…289b, verified); Evals references; Universe_SynthCut exports.

## Result

**Prompt: `none`.** All 6 sentences are clean on every P4 topic. The prompt text is identical to earlier rounds, and every record its destinations rest on is unchanged.

**Does anything reach a scored fail? No.**
- **Prompt dimensions:** no P4 topic is hit, so Contrived, Naturalness and Explicit Tool Mention have nothing to fail on.
- **Eval 0 grader-facing clause:** this is the only rule that reaches record text, and on my reading nothing meets it. Every candidate is an in-world statement to Julia or on a ticket; none speaks to a solver or grader or describes the test. The closest quotes are DR5, DR10, DR18 and DR22.
- **§1.2 argument:** a reviewer could try to extend §2.7 to the brief as an incorporated record. §1.2 governs requirements, and §2.7 says "A per-case rule belongs in a seeded record, not in the prompt", so that extension is exposure, not a score.

**This round's two sentences:**
- **B6a (new):** "Endless goes down as its weekly windows, with the daily reset noted." Reads as a person, and Confluence backs it. One new LOW item (DR25).
- **B26 (changed):** "…and you tell its owner in a reply on the mail where they committed to it." Better: the passive is gone and it now says who acts. "any time before it" and the unnamed mail remain, so DR18 and DR7 stay MED.

**Extended test: 24 open items: 4 HIGH, 12 MED, 8 LOW.** The HIGH items are DR2, DR3, DR4 and DR19. Severity means exposure if a reviewer extends the prompt tests to records. It is not a score. Under the current text the score effect is none, for three reasons:
- Eval 1 §2.7 applies its red flags to prompt wording.
- deep_recheck P4 says "the persona's own Slack or mail style is not a standard."
- Eval 0 puts "Writing style, voice matching" outside its review but keeps grader-facing text in scope.

## Count

| Item | Checked |
|---|---|
| Prompt | 6 sentences, 100 words |
| Frederick's DM | 6 sentences, 130 words |
| Frederick's thread reply | 5 sentences, 90 words |
| Brief | 29 sentences, plus title and byline (8 headings read) |
| Other injected records | 7 Slack, 3 GitHub, 32 Linear, 1 Trello, 2 Gmail bodies (6 copies), 1 GCal description (4 copies), 3 slide boxes, 2 sheet header rows; 121 sentences |
| SQL diff from rev13 | 2 lines, both the brief row: 2 sentences, plus heading offsets (all 9 style runs match the new body) |

The 3 Slack bot mirrors only repeat GitHub comments. Of the other injected records, 37 table rows settle something (the 3 slide boxes share one row). The other 10 Linear comments are background.

Measured counts come from a raw scan of the base exports, not a persona view: 610,468 Slack messages in all channels, 3,687 Linear issues.

## P4 prompt findings

`none`, 6 sentences checked.

| # | Sentence | Reads as |
|---|---|---|
| S1 | "Frederick messaged me yesterday asking for the live-ops and push calendar for the Zombie Match 3D beta, the four buy weeks that start Monday the 6th." | Person, no flag |
| S2 | "Can you take it on for me?" | Person, no flag |
| S3 | "What he wants in it is in his message, and his working rules for building it are in the brief he shared with me." | Person, no flag |
| S4 | "It goes in my live-ops calendar sheet." | Person, no flag |
| S5 | "If a beat ends up held, leave a note on its ticket so the owner picks it up." | Person, no flag |
| S6 | "Once the sheet's done, link it on the calendar ticket and send Frederick the recommendation he asked for." | Person, no flag |

| Topic | Result |
|---|---|
| Catalog tool names | No finding. 298 catalog names searched, 0 hits. |
| MCP or "tool" wording | No finding. |
| Section 3 search hits (`linear_`, `gmail_`, `slack_`, `MCP`, `tool`, `First`, `Then`, `Finally`) | No finding. 0 hits. |
| First / then / finally list | No finding. "Once the sheet's done" is one real dependency: a sheet can't be linked before it exists. |
| Bolt-on | No finding. S5 consumes the hold call the calendar makes. S4 and S6 repeat the DM, but they name destinations the persona knows, which §2.7 wants. |
| Opaque id or exact timestamp | No finding. "Monday the 6th" is human and correct. |
| Stated cause (§6.7) | No finding. No cause is stated. |
| Trap hint or riddle | No finding. "If a beat ends up held" is a neutral conditional, the same shape as the GOOD example in common_errors §6.5 ("If a bill is missing from those, say it is missing."). |
| Hidden destination | No finding. See the four checks below. |
| Audit or compliance form | No finding. Nothing resembles #1 or #43. |
| If / but-not / then-also chains | No finding. One "If" and one "Once", no chain. |
| Staged typos, emoji, broken punctuation | No finding. |
| Spec-like or polished voice | No finding. 0 of 4 register triggers, no document formatting, no polished connectives. Sentence lengths are 26 / 7 / 24 / 7 / 18 / 18 words. |

Hidden destination checks:
- "my live-ops calendar sheet" is Julia's own sheet.
- "the calendar ticket" is ZOM-78, "Event Calendar For Zombie Match 3D". Frederick's comment on it names it.
- "its ticket" can't be named without pre-solving the hold. ZOM-429 is the only open ZOM ticket with leaderboard in its title.
- "send Frederick" is resolved by "back here" in the DM.

S3 is the most written sentence, but it trips no flag and is a valid incorporation pointer. "Beat" is Frederick's word in the DM and brief, and Leonard's Sep 10 Slack has "engagement beats".

## Extended test findings

Format: DR# | pass | checklist section | quote | record | dimension | severity. Ids are kept from earlier rounds; DR14 was closed and is not reused. Sentence ids (F, R, B) are in the tables that follow. B3a, B6a and B17a are later additions to the brief.

| DR# | Pass | Section | Quote | Record | Dimension / issue | Severity |
|---|---|---|---|---|---|---|
| DR2 | P4-ext | §2.7 trap hint, riddle | B19: "only with the latest dated approval from Product, and if he takes that back his later word is the one that counts." | Brief f_7c3e91a4… (SQL l.121), dated Sep 24, six days before the reversal it anticipates. "Product … he" withholds the name: base Slack uses Product as a team ("Product team", "Product said"), and only Confluence "ZM3D Season Pass — Spec" (/pages/20) maps it ("Owner: Robert (Product)"). | Contrived (extended): foretells the trap | HIGH |
| DR3 | P4-ext | Planted-record test | "Parking it, nothing here has to land for the beta." (cmt_zom471_1, Sep 17) | "has/have to land" sits in 7 comments by 4 authors: slack a08ff7cb, cmt_zom471_1, cmt_zom534_1, cmt_zom526_2, cmt_zom565_2, cmt_zom566_1, cmt_zom465_3 (Brian wrote 4). "not needed for the beta" adds cmt_zom565_1 and cmt_zom542_1. The phrase is Frederick's (F2, B20). Base: 0 uses of "has to land", and the one "have to land" is about objects falling (Marcus, 2023). "before the event runs" also has 0 base hits and is shared by #468 rc_38 and cmt_zom465_3. Sep 17 and Sep 22 predate the brief, and all but the lightSweep reply predate the DM. Only that reply answers a question in its thread. | Contrived (extended): one template across many voices | HIGH |
| DR4 | P4-ext | §2.7 audit form | B15-B16: "a change request outside the Aug-Sep live-ops cohort"; "An unresolved change-request review blocker on an in-scope live-ops PR from that cohort does hold it." | SQL l.119. The vocabulary matches FAIL example #43 in §2.7 ("the full in-scope upload-thread cohort"). No record defines this cohort. In the sampled Slack hit, Frederick's "cohort" is a user cohort ("the 9/12 cohort"). GitHub `reviews`: 74 CHANGES_REQUESTED, the latest 2025-07-16 (match3d#303, posted by the CodeRabbit account), so B15's exclusion has one obvious target and B16 has no review in that state in Aug-Sep. | Contrived (extended): audit form, rule with no visible case | HIGH |
| DR19 | P4-ext | Planted-record test | "Marcus, the Collect & Win icon does have to land before the event runs, it is the one event icon with no animation."; "Keep it on this ticket, the master VFX list was ticked before that event merged." | cmt_zom465_3 (SQL l.210), 8 minutes after Marcus's note, which asked nothing. Sentence 1 inverts the DR3 template with emphatic "does". Sentence 2 explains a record discrepancy nobody raised on this ticket (ZOM-521's ticked "animations on these icons"). It is true on the dates: ZOM-521's base list is dated Sep 17, #468 merged Sep 29. "master VFX list": 0 Slack hits. | Contrived (extended): planted to settle | HIGH |
| DR5 | P4-ext | §1.2 voice; Eval 0 closest quote | B5: "A PT/PDT rendering of the same instant is fine, a different instant is not." | SQL l.113. Reads as a rubric tolerance clause. deep_recheck P1 uses the same idea ("one instant whose Pacific and UTC days differ"). B4's "closing 23:59 UTC on its last day" adds to the register. Frederick in Slack: "rendering" 0, "UTC" 0 of 4,780 messages, while the brief says UTC 8 times. Partly offset: he does use PT/PDT (12 messages), so the content is plausible for him. | Contrived (extended): grader register | MED |
| DR6 | P4-ext | §2.7 | B12: "put down whether the beat is in, which weeks it runs and whether its push goes out, not its window dates." | SQL l.117. Cuts against F2 ("which windows it runs in") for three beats with no stated reason. Reads as scoping what is checked. | Contrived (extended) | MED |
| DR7 | P4-ext | §2.7 hidden destination, riddle | B25-B26: "before its lock"; "in a reply on the mail where they committed to it." | SQL l.127. "Its lock" is never defined in the brief; only Confluence has it (/pages/20: "locked 24h before each season opens"). The rule has one application, Brian. Same form as #47, though a persona-visible record does name the place. Brian's Sep 26 mail pairs with it ("reply on this mail"). Julia's 253 base mail threads hold 0 mails from Brian, so the only two are injected. | Contrived (extended): hidden destination form | MED |
| DR8 | P4-ext | §2.7 trap hint | B13, B15: "even after a restart"; "a reset that needs a restart" | The rule's dividing line matches Vincent's post exactly: "I killed the app and reopened it twice" (Slack C0880U9751A id b5f2955c, SQL l.19). That post is top-level, answers nobody, doesn't mention ZOM-429, and sits in #zombie-match3d although his Sep 15 issue list went to #zombie-bugs. | Contrived (extended): rule cut to a planted record | MED |
| DR9 | P4-ext | Planted-record test | "The Plague Race, leagues, Endless and Season Pass schedules are already running on prod."; "Fine for this PR. Separately, the Season Pass premium strip art still shows the October range." | match3d#470 rc_10 (SQL l.154) sits on CollectAndWinMainScreenController.cs, 9 seconds before merge. match3d#472 rc_1 (SQL l.164) sits on RewardVFXManager.cs, and #472 has no other review comment. Both state calendar facts on unrelated files. | Contrived (extended): planted to settle | MED |
| DR10 | P4-ext | Eval 0 closest quote | "That was my report, it is good on prod now." | cmt_zom534_2 (SQL l.198). ZOM-534's description already shows "@Leonard said", so the sentence serves an outside reader, not the ticket. | Contrived (extended) | MED |
| DR11 | P4-ext | Planted-record test | "The weekly rollover does not wait on them, the current quests keep running either way." | Trello action 68dac820… (SQL l.259), on a card with 0 comments and no question. The last base Trello comment is 2025-07-02, so this lands about three months later. | Contrived (extended): planted to settle | MED |
| DR12 | P4-ext | §1.2 voice | "Let us use this ticket…"; "we are not spending art time" | Whole SQL: 0 contractions and 46 uncontracted forms across 52 texts, by 12 named authors. The five I measured in base Slack (Frederick, Robert, Vincent, Leonard, Arthur) contract 53-79% of the time. "Let us" vs "let's": 322 vs 3,520 overall, 1 vs 55 for Frederick. Possessives (Nathan's, Martin's) show apostrophes were not a technical barrier. | Contrived (extended): machine-even voice | MED |
| DR18 | P4-ext | §1.2 voice; Eval 0 closest quote | B26: "moves to any time before it" | SQL l.127. Reads as an acceptance range: a founder moving a dependency names a date or says "before the lock", not "any time". No in-world reason is given. Same family as DR5. This round's "you tell its owner" does not touch this clause. | Contrived (extended): grader register | MED |
| DR20 | P4-ext | §1.2 voice | B3a: "Clip anything that starts before or runs past that to those two instants." | SQL l.113. Closes an edge-value fork. "clip" in Frederick's Slack is only an audio clip. "instant(s)" appears 5 times in the brief. A rules doc is a fair home for this; the register is the issue. | Contrived (extended): spec register | MED |
| DR22 | P4-ext | §2.7 trap hint; Eval 0 closest quote | B22: "(Login Calendar and Weekly Rankings are fine)"; B23: "with which of those its row is missing." | SQL l.125. These are exact strings from two row copies on PNs Beta ("Check the login calendar"; "Weekly Rankings Reset!"), inside a general rule dated Sep 24. Both rows already fail "Ready and LIVE" (Not Ready/WIP and Ready/WIP), so the carve-out only changes the "what is missing" cell, which B23 limits to the listed conditions. That is rubric-level precision. By elimination it also points at the names that are not fine. | Contrived (extended): per-case carve-out | MED |
| DR23 | P4-ext | Planted-record test | "That update carried only these, the Collect & Win server windows wait for the Oct 8 release." | cmt_zom563_1 (SQL l.255), on a teams bug ticket with no mention of Collect & Win and no question. The base DM it builds on (D079SNE2TL4) is Vincent and Douglas only, so Julia can't see what the sentence corrects. Third injected statement of the same fact, after GCal and #470 rc_10. "server windows": 0 base hits. | Contrived (extended): planted to settle | MED |
| DR1 | P4-ext | §2.7 trap hint | "Coming back on the themed prop set I okayed in Martin's thread: pulling my ok." | Slack D05GU6L0XFH id 669d15f6… (SQL l.17). Volunteered in a DM that is otherwise prototype talk, and "my ok" has 0 base hits. It gives a real reason ("a theme we may not ship at all"), and pivot talk is live that day, so it reads as a person. | Contrived (extended) | LOW |
| DR13 | P4-ext | Planted-record test | R2-R5: "as it stands, one line per row"; "just those four"; "Copy that does not name the game at all is fine to go out" | SQL l.13. Nobody asked any of this. R4 narrows his own B22 unprompted. R5's "no window or reset" repeats B7's scope words. Frederick is the rule source, so this is in role. | Contrived (extended): reads as a patch | LOW |
| DR15 | P4-ext | §2.7 | B9-B10: "the backend release instant read in UTC, not when its client PRs merged"; "starts late, it is not held." | SQL l.117. A generic rule with one case, Collect & Win (#470 rc_10 says only it is on DEV). It states the rule outright, so it is not a riddle. "DEV stack": 0 base hits. | Contrived (extended) | LOW |
| DR16 | P4-ext | §1.2 voice | B2: "The rules stay here; the calls are yours."; B14: "An established failure holds it; an unverified one does not." | Balanced aphorisms. "provably" (B13): 0 of 610,468. Semicolons in 4 of 29 brief sentences vs 62 of Frederick's 4,780 Slack messages, a weak signal across different media. | Contrived (extended) | LOW |
| DR17 | P4-ext | Planted-record test | Collection level | Base Linear has 0 comments on 3,687 issues, so all 32 comments an agent sees are injected, on 22 tickets, all about this task. This is an export fact, not a contributor defect. | Context | LOW |
| DR21 | P4-ext | §1.2 voice | B17a: "A held beat keeps its usual windows and weeks on its row, marked held." | SQL l.119. A layout rule for the sheet, in plain words. | Contrived (extended) | LOW |
| DR24 | P4-ext | §1.2 voice, bolt-on form | B8: "and the rotating shop is not a beat." | SQL l.115. Tacked onto an unrelated Boss Arena sentence. "rotating shop" is the company term (160 Slack hits), and the exclusion is fair, so only the form is exposed. | Contrived (extended) | LOW |
| DR25 | P4-ext | §1.2 voice | B6a: "Endless goes down as its weekly windows, with the daily reset noted." | SQL l.113, new this round. Plain and grounded: Confluence /pages/27 has "daily and weekly resets". It is one more per-beat layout rule that closes a fork nobody raised. A reader sees the brief's density, not its history: B3a, B6a, B17a, B8's clause, B22's parenthetical and B23 all do this job. | Contrived (extended) | LOW |

## Frederick's DM

SQL l.11. Trap column: none, states rule (open and direct), foretells, or riddle form.

| # | Sentence | Voice | Trap | Note |
|---|---|---|---|---|
| F1 | "Julia, I need the live-ops and push calendar for the beta buy we start Mon Oct 6 through Sun Nov 2." | Person | None | |
| F2 | "Every beat players can see in those weeks: which windows…who owns that." | Mixed | None | Five-part spec in one sentence. Source of the DR3 phrase. |
| F3 | "Put it in the calendar sheet in your ZM Live Ops folder and link it on the calendar ticket." | Person | None | Names both places. |
| F4 | "Then send me your recommendation back here, with the trade-offs, on what we run and what we hold in those weeks." | Person | None | |
| F5 | "The working rules for the calendar are in my brief, shared with you." | Mixed | None | "shared with you" reads as an access pointer. |
| F6 | "This goes into the pivot call, so I need your call, not a list of what we have." | Person | None | The pivot is real in base (Frederick, Sep 29). |

The whole message is one 130-word block. His 111 base messages in this DM have a median of 13 words and a maximum of 71.

## Frederick's thread reply

SQL l.13. Posted 4 minutes after the parent.

| # | Sentence | Voice | Trap | Settles something nobody asked |
|---|---|---|---|---|
| R1 | "Two things on top of the brief." | Person | None | n/a |
| R2 | "Pushes: plan the PNs Beta tab as it stands, one line per row, local notifications included." | Authoring | States rule | Yes |
| R3 | "Leave off the four rows for things that are not in the beta: Hourly Coins, Nathan's Treasure Hunt, Streak Fever and Axe Arena, just those four." | Mixed | States rule | Yes |
| R4 | "Copy that does not name the game at all is fine to go out, the naming rule is only about wrong names." | Authoring | States rule | Yes |
| R5 | "And keep Zombie Lane off the calendar, it is a permanent track with no window or reset to plan." | Mixed | States rule | Yes |

## Frederick's brief

SQL l.109-127. Totals: 6 Person, 10 Mixed, 13 Authoring of 29, plus title and byline (Person). A rules doc is the right home for per-case rules, so "states rule" is not a defect in itself. Every brief sentence is in a rules doc, so the unasked test does not apply; the Note column says where one closes a fork.

| # | Sentence (opening) | Voice | Trap | Note |
|---|---|---|---|---|
| B1 | "How I want the beta calendar built…" | Person | None | |
| B2 | "The rules stay here; the calls are yours." | Authoring | None | DR16 |
| B3 | "The calendar covers Mon Oct 6 00:00 UTC to Sun Nov 2 23:59 UTC…" | Person | None | |
| B3a | "Clip anything that starts before or runs past that to those two instants." | Authoring | None | DR20 |
| B4 | "Every window is stated in server time (UTC) as a start-end instant, closing 23:59 UTC on its last day." | Authoring | None | DR5 |
| B5 | "A PT/PDT rendering of the same instant…" | Authoring | None | DR5 |
| B6 | "Collect & Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC." | Person | None | Plain fact. |
| B6a | "Endless goes down as its weekly windows, with the daily reset noted." | Person | None | **New.** DR25. |
| B7 | "Every ZM3D beat a player can see…" | Mixed | None | Definition form. |
| B8 | "Boss Arena is off this calendar until the pivot call, and the rotating shop is not a beat." | Mixed | States rule | DR24 |
| B9 | "A beat starts with the first window that opens after…" | Authoring | States rule | DR15 |
| B10 | "A beat whose server windows are waiting…starts late, it is not held." | Mixed | States rule | DR15 |
| B11 | "Season Pass seasons open on the 1st at 00:00 UTC." | Person | None | Matches Confluence. |
| B12 | "For the quest rollover, the daily gift (Login Calendar on the push sheet, same beat)…not its window dates." | Authoring | States rule | DR6 |
| B13 | "Hold a beat only when players provably cannot…" | Authoring | States rule | DR8, DR16 |
| B14 | "An established failure holds it; an unverified one does not." | Authoring | States rule | DR16 |
| B15 | "Wrong counters, a reset that needs a restart…" | Authoring | States rule | DR4, DR8 |
| B16 | "An unresolved change-request review blocker…" | Authoring | States rule | DR4 |
| B17 | "A hold with no dated fix runs until…" | Mixed | States rule | "say that instead of guessing a date" sounds human; "dated fix" does not. |
| B17a | "A held beat keeps its usual windows and weeks on its row, marked held." | Mixed | None | DR21 |
| B18 | "One-offs may overlap recurring beat slots." | Mixed | None | Rule register. |
| B19 | "A one-off may take a recurring beat slot only with…" | Authoring | Foretells, riddle form | DR2 |
| B20 | "For each beat, what still has to land…" | Mixed | States rule | "(prod deploy, config or player-facing art)" lists the planted item types. |
| B21 | "Nothing else goes in: not what already shipped…" | Mixed | States rule | Rhythmic triple. |
| B22 | "A push goes out only if its row is Ready and LIVE…(Login Calendar and Weekly Rankings are fine)." | Mixed | Mildly, by elimination | DR22 |
| B23 | "Anything else is held, with which of those its row is missing." | Mixed | None | DR22 |
| B24 | "Beta pushes are English-only…the old Domino set…" | Person | States rule | Tab claim is accurate. |
| B25 | "Every config a beat needs lands before its lock…" | Authoring | Riddle form | DR7 |
| B26 | "A committed date that misses the lock moves to any time before it and you tell its owner in a reply on the mail where they committed to it." | Authoring | Riddle form | **Changed.** DR7, DR18. "you tell" is better and is addressed to Julia, the brief's reader, like B2 and B17, so it is not grader-facing. |

## Injected records that settle something

"Planted" means settling a question nobody in the record asked. Totals: 14 Yes, 9 Partly, 14 No of 37 rows.

| Record | Settles | Voice | Points at a trap | Planted |
|---|---|---|---|---|
| Slack 933cee9f, Robert, Sep 18 | Halloween may take a slot | Mixed | Sets up the reversal | Partly. Martin asked about a theme, not slots. |
| Slack 669d15f6, Robert, Sep 30 | Withdraws that approval | Person | No | Partly (DR1) |
| Slack b5f2955c, Vincent | Leaderboard failure is established | Mixed | Matches B13 | Yes (DR8) |
| Slack e343557b, Leonard | Airstrike freeze not reproduced | Person | No | No. Follows up his own Sep 21 report. |
| Slack a08ff7cb, Vincent | lightSweep needs nothing | Mixed | DR3 phrase | Partly. His thread did ask about squeezing it in. |
| Slack 532747cb, Robert | No new themes needed | Mixed | No | Partly. Martin asked "What do you think?"; the tail goes further. |
| Slack 7d70c775, Douglas | Reward tables updated | Person | No | No. Brian asked "Could you update them?" in that thread. |
| GitHub #470 rc_10, Arthur | C&W on DEV, others live | Mixed | States the fact | Yes (DR9) |
| GitHub #468 rc_38, Arthur | Final vial models, Claire | Person | States the need | No. A normal review note ("Not a blocker for this PR"). |
| GitHub #472 rc_1, Arthur | November strip art, Oliver | Mixed | Fits B20's "player-facing art" | Yes (DR9) |
| Trello 68dac820, Leonard | Quests rollover goes ahead | Mixed | No | Yes (DR11) |
| Gmail Sep 22, Brian | Handoff Oct 29 | Mixed | "committing" pairs with B26 | Partly. "Handing over" opens a mail that hands nothing over. |
| Gmail Sep 26, Brian | Moves to Oct 31 10:00 Istanbul | Mixed | "reply on this mail" pairs with B26 | Partly (DR7) |
| GCal evt_5c1e83a7, Douglas | Release Oct 8 15:00 UTC | Mixed | No | No. A calendar entry is the normal place. |
| Slides, UA plan (3 boxes) | Buy weeks, geos, budget | Person | No | No |
| cmt_zom429_1, Douglas | Restart clears it (stale) | Person | Decoy | No |
| cmt_zom556_1, Vincent | Daily gift claims work | Mixed | "claiming works" matches B13 | Partly. Retest of his own bug. |
| cmt_zom565_1, Marcus | Polish, not needed | Mixed | DR3 phrase | Yes |
| cmt_zom565_2, Brian | Polish can follow | Authoring | DR3 phrase | Yes |
| cmt_zom526_2, Brian | Token travel not needed | Mixed | DR3 phrase | Yes |
| cmt_zom526_3, Calvin | Only Axe Arena left | Person | No | No |
| cmt_zom534_1, Douglas | Fix shipped, kept open | Mixed | DR3 phrase | Yes |
| cmt_zom534_2, Leonard | Reset works on prod | Authoring | No | Yes (DR10) |
| cmt_zom432_2, Samuel | Frame shipped, closed | Person | No | No |
| cmt_zom78_1, Frederick | Ticket for the sheet | Mixed | No | Partly. A fair reason to write; "Let us" is the only tell. |
| cmt_zom465_2, Marcus | C&W icon still to do | Authoring | Uses the "still to do" heading | Yes |
| cmt_zom465_3, Brian | C&W icon must land | Authoring | States the answer | Yes (DR19) |
| cmt_zom471_1, Samuel | Red dot parked | Authoring | DR3 phrase | Yes. Predates the brief. |
| cmt_zom504_1, Vincent | Bot-only, visual | Person | No | No |
| cmt_zom517_1, Robert | Not reproduced | Person | No | No |
| cmt_zom546_1, Owen | Not reproduced | Person | No | No |
| cmt_zom542_1, Samuel | Layout refresh not needed | Authoring | DR3 phrase | Yes. Predates the brief. |
| cmt_zom566_1, Brian | Title and text not needed | Mixed | DR3 phrase | Partly. Restates a real Sep 30 exchange in #zm-collect-win; the tail is the template. |
| cmt_zom563_1, Douglas | Prod update scope | Mixed | Closes the reading that it shipped the windows | Yes (DR23). Sentence 1 restates his real base DM; sentence 2 is the plant. |
| cmt_zom563_2, Vincent | Teams work on prod | Person | No | No |
| cmt_zom344_1, Marcus | Quest box signed off | Person | No | No |
| cmt_zom521_2, Calvin | Card pack in, kept open | Person | No | No |

Background, settling nothing and reading as people: cmt_zom543_1, zom526_1, zom552_1, zom432_1, zom465_1, zom442_1, zom521_1, zom544_1, zom549_1, zom566_2.

Voice mismatch alone (for example Marcus's clean comments against his real "its gona be") is not scored, per the P4 rule quoted above. It is why several rows read Mixed.

## Handoffs to other passes (not P4 findings)

- **P1:** B26 allows any time before the lock, so the moved date has no single value. The rubric must accept any time before it.
- **P1:** B22's carve-out only affects the "what is missing" cell, because both rows are held on status anyway.
- **P1:** #468 rc_38 and cmt_zom465_3 tie their deadline to "before the event runs", so the Collect & Win items are due by that beat's first window.
- **P1:** the DR3 comments are mostly owners' own claims (SCOPE_GAP). cmt_zom465_3 and #468 rc_38 are third-party flags, so they are stronger.
- **P1/P2:** B16 has no CHANGES_REQUESTED review in Aug-Sep. Someone should decide whether it has any case, or what "change request" means.
- **P2:** Douglas's "Both tables are updated." sits in #zm-collect-win, which is not private but does not list Julia as a member.
- **P2:** the amended push rules sit in a thread reply, and S3 says only "his message". This DM has 2 threaded replies in 241 messages; the parent's reply_count of 1 does signal it.

## Platform defects

None.

## Blindness note

I read R14/REVIEW_SETUP.md first. My session's working directory moved into Task_Authoring/task_inputsS this round, a blind folder, so I used absolute paths and opened nothing there. A listing of R14/out showed three other passes' filenames; I did not open them. I opened no sibling review folder. Helpers are under R14/work/p4. Findings carried over are my own from earlier rounds, rechecked against this SQL.
