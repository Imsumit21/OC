# 08 OE Check — vincent-zm3d-release-gate (ZM store candidates QA gate, injection rev18)
Checked 2026-11-06 · Events 35 · Characters 35703 (300–50,000: ok) · Ledger 2026-11-05 (oe-writing PASS) · release task-quality-v1
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
/oe prediction (a prediction only; /oe gives the verdict): PASS 5
Completeness 5 · Accuracy 5 · Path feasibility SUPPORTED · Task solvability SUPPORTED_BY_OE

Inputs: 08_Oracle_Events.md (35 events, saved as the Evals `oe` input, sha256 34878e63a31d), 08_OE_Writing_Ledger.md (41 facts), 04_Prompt.txt (prompt rev 6), 01_Universe_Inject.sql (rev18), 00_Assigments.md. Independent evidence, two sets of blind deep-recheck passes: (a) this session's O1 (GPT-6.1 Sol, accuracy, complete, 0 findings), O2 (GPT-6.1 Sol, completeness; four runbook-process writes proposed, rejected below as unincorporated) and O3 (GPT-6.1 Sol, open-instruction inventory, 31 items, every one matched), then a final adversarial pass on the revised set (PASS, predicted Completeness 5 / Accuracy 5, two advisories applied); (b) a parallel session's passes in research/oe/deep_recheck/ (O1 two findings and O3 one mismatch on ZOM-506, all rejected against the records; the `verify` oracle tier upheld every rejection, round 2 PASS, research/oe/deep_recheck/oracle_adjudication.md). The format-2 /oe record built from primary anchors validates PASS 5 / COMPLETE with 798 Expected-line values ledgered, 0 absence claims, 0 unresolved (Evals/tools/hg_oe_review.py validate). Platform history: Eval Portal /oe gave PASS 5 on sha 6be5f26b and NON-FAIL 3 (Accuracy 3) on sha 3ddf0464, whose only change was the heading dashes; the NON-FAIL came from a qualifier in OE 14 that both runs read, not from the dashes (plateform_report/6ae9909f7b5249d3148f3707_2_oe (1).md and (2).md). Findings 15 to 30 fix that qualifier, the three optional notes of the PASS report, and every further qualifier found by four blind hunts (GPT-6.1 Sol and Opus 5.5 redteam passes) and a narrow final check of the changed spans.

## Inventory
| Segment (quoted start) | Role | Event |
|---|---|---|
| OE 1  Find the candidates and the thread the QA call goes back to. | STEP | OE 1 |
| OE 2  Read the store release ticket the post points to. | STEP | OE 2 |
| OE 3  Read the push notes on the release ticket. | STEP | OE 3 |
| OE 4  Find the two process docs ZOM-570 says are shared. | STEP | OE 4 |
| OE 5  Read Leonard's rules, which decide the register's scope and every call. | STEP | OE 5 |
| OE 6  Read Arthur's note on how submission builds are cut, which decides whether a fix is in the candidates. | STEP | OE 6 |
| OE 7  Read the gate sheet's rules for the register and the previous gate's tab. | STEP | OE 7 |
| OE 8  Read the tech-issues card ZOM-570 names. | STEP | OE 8 |
| OE 9  Find when the last gate's builds were cut, which sets the Done-ticket cutoff. | STEP | OE 9 |
| OE 10  Derive the register population. | STEP | OE 10 |
| OE 11  Read every in-scope ticket's comments. | STEP | OE 11 |
| OE 12  Pick out Leonard's per-ticket rulings and the art, UI-layout and animation follow-ups among the comments from OE 11 | STEP (reasoning) | OE 12 |
| OE 13  Call the no-call tickets. | STEP (reasoning) | OE 13 |
| OE 14  Pick out the open bugs whose latest report shows a blocker symptom, and which of them were re-checked on the candidates | STEP (reasoning) | OE 14 |
| OE 15  Pick out the latest checks on the open bugs that still show a visible but non-blocking problem | STEP (reasoning) | OE 15 |
| OE 16  Pick out the latest checks that show bugs fixed on the candidates | STEP (reasoning) | OE 16 |
| OE 17  Pick out the comments on the tickets whose call or build status another record settles | STEP (reasoning) | OE 17 |
| OE 18  Call the tickets filed on Sep 30 after the candidates were cut, which carry no QA comment, from their own reports. | STEP (reasoning) | OE 18 |
| OE 19  Read Vincent's own re-checks posted in #zombie-bugs. | STEP | OE 19 |
| OE 20  Read what Brian found, which the ZOM-458 and ZOM-535 comments point to, and his later candidate checks. | STEP | OE 20 |
| OE 21  Check outside test reports on the candidates. | STEP | OE 21 |
| OE 22  Confirm who sent the session notes. | STEP | OE 22 |
| OE 23  Confirm which server-side fixes are live on prod. | STEP | OE 23 |
| OE 24  Check whether the ZOM-567 backend fix is fully on prod. | STEP | OE 24 |
| OE 25  Check which Done fixes are in the candidates. | STEP | OE 25 |
| OE 26  Read the QA regression runbook's gate rule for the matrix. | STEP | OE 26 |
| OE 27  Read Brian's regression matrix, the record behind his "green" reply. | STEP | OE 27 |
| OE 28  Read Brian's update-path results. | STEP | OE 28 |
| OE 29  Check whether anyone already filed this update failure. | STEP | OE 29 |
| OE 30  Confirm the deadline. | STEP | OE 30 |
| OE 31  File the new ticket for the unfiled runbook finding. | STEP (write) | OE 31 |
| OE 32  Add the gate tab to Vincent's release gate sheet. | STEP (write) | OE 32 |
| OE 33  Write the register into the new tab. | STEP (write) | OE 33 |
| OE 34  Put the blockers on the release ticket. | STEP (write) | OE 34 |
| OE 35  Give the QA call in Arthur's candidates thread. | STEP (write) | OE 35 |

No CONTEXT, RESPONSE_DESCRIPTION or NON_ACTION segment: every event is a read, a reasoning step over earlier reads, or one write.

## Coverage
| R / F | Event(s) | Covered / missing / partial | Route (ledger / other valid) |
|---|---|---|---|
| R1 candidates, scope, every call and build status (F1, F6, F7, F9–F32, F38) | OE 1, OE 5–OE 25 | Covered | Ledger route: population from Linear (F13, F14) before any call; every BLOCKER / KNOWN ISSUE / FIXED / NO CALL row has a reading event (OE 11–OE 25) |
| R2 the release ticket's background (F2–F8, F11) | OE 2, OE 3, OE 4, OE 5, OE 6, OE 8 | Covered | Ledger route: ZOM-570 → both docs → the tech-issues card |
| R3 register in a new tab (F9, F10, F38, F41) | OE 7, OE 32, OE 33 | Covered | Ledger route: How we gate rules read, tab added, 133 rows written |
| R4 blockers in ZOM-570's description (F39) | OE 34 | Covered | Ledger route: description update with all 19 keys |
| R5 new ticket for unfiled runbook findings (F33–F36, F40) | OE 26, OE 27, OE 28, OE 29, OE 31 | Covered | Ledger route: runbook rule, matrix, update-path run, duplicate check, one create |
| R6 reply in Arthur's thread with the QA call (F1, F3, F39) | OE 1, OE 3, OE 35 | Covered | Ledger route: thread located, Leonard's "not a new post", threaded reply |
| R7 before Friday's go/no-go (F37) | OE 30 | Covered | Ledger route: calendar event starts 2025-10-03T16:00:00Z |

## Expected-data sign-off
| Event | Claim (quoted) | Source re-read (hg.py pointer) | Value found | Ledger entry (result · quote · evidence_check / not_a_claim) | Match / minor / wrong / unresolved |
|---|---|---|---|---|---|
| OE 1 | "regression matrix green on #135 and #50 from my side :+1:" | SQL L118, L119 (C08R27X0EAH/1759263900.484190, C08R27X0EAH/1759266600.265963) | both messages verbatim; created_at 20:25:00Z / 21:10:00Z | F1 VERIFIED | Match |
| OE 2 | "created 2025-09-30T20:20:00Z by Arthur Blake" | SQL L11–L17 (ZOM-570); linear data.json /users/35 | creator usr_cc3e90160f490686 = arthur.blake; In Progress | F2, F4 VERIFIED | Match |
| OE 3 | "created 2025-09-30T20:52:00Z" | SQL L32 cmt_zom570_1 | Leonard, "not a new post" | F3 VERIFIED | Match |
| OE 4 | "ZM submission rules.docx" | SQL L221, L234, L243 (f_632c44650df44fe252ee59, f_a038a576ca8db6955fae95, f_fcb4f7c9b508088e0d5803) | owners, created times, reader Vincent | F5 VERIFIED | Match |
| OE 5 | "Release tickets, ZOM-359 and ZOM-475 stay out" | SQL L222 body_text (f_632c44650df44fe252ee59) | every quote verbatim | F6 VERIFIED | Match |
| OE 6 | "Merged is not live." | SQL L235 (f_a038a576ca8db6955fae95) | every quote verbatim | F7 VERIFIED | Match |
| OE 7 | "One tab per gate, named after the candidate builds. One row per ticket." | SQL L257, L258 grid_json (f_0ebfccf33076f9dbf086bc) | vocabulary, meanings, 8 Sep 22 rows | F9, F10 VERIFIED | Match |
| OE 8 | "same as ZOM-435" | SQL L277, L278 (Trello 68dc3ef455344e471b1d2ea9, 68dc63484a5b2d0a869e758f) | both comments, dates | F11 VERIFIED | Match |
| OE 9 | "Match3D Android Submission - #127 Started by user Arthur Blake" | hg.py get slack C05433XK267/2025-09.json /692, /693, /694, /696 | fallback strings; ts → 12:30:43 / 12:32:20 / 12:38:18 / 12:39:43 UTC | F12 VERIFIED (times by calculation) | Match |
| OE 10 | "132 tickets" | hg.py get-many linear data.json /issues (reverify/linear_base_hg.json) + SQL L8–L29 | 112 open + 20 Done after the cut; equals solver/truth.json | F13, F14 VERIFIED | Match |
| OE 11 | "38 of the 132 tickets have comments" | SQL L30–L87 cmt_ rows; linear data.json /comments | 57 in-scope comments on 38 tickets; base comments 0 | F15 VERIFIED (count by calculation) | Match |
| OE 12 | "No call for the store gates." | SQL L82–L86 (cmt_zom477_1, cmt_zom558_1, cmt_zom536_1, cmt_zom498_1, cmt_zom555_1) | authors and times | F16 VERIFIED | Match |
| OE 13 | "85 tickets are NO CALL" | linear data.json /issues titles; SQL L22, L24 | 85 keys = truth.json NO CALL set | F17 VERIFIED | Match |
| OE 14 | "both gone, 600 coins worth." | SQL L45, L60, L61, L63, L65, L69, L70, L87 | eight latest checks | F18 VERIFIED | Match |
| OE 15 | "Purchase goes through at the shown price." | SQL L47–L71 (cmt_zom237_2 … cmt_art793_1) | 14 latest checks, 2025-09-30 | F19 VERIFIED | Match |
| OE 16 | "Couldn't reproduce on #135 or #50" | SQL L46, L50, L56 | three passes on the candidates | F20 VERIFIED | Match |
| OE 17 | "fixed on my branch, the join popup only opens one SP screen now" | SQL L30, L31, L53, L59, L66, L74 | six comments | F21 VERIFIED | Match |
| OE 18 | "only the gems land and the tier is marked claimed, so the boosters are gone." | SQL L18–L27 (ZOM-571 … ZOM-580) | descriptions and labels | F22 VERIFIED | Match |
| OE 19 | "ZOM-558 weekly board says Level: now. rest tomorrow" | SQL L121, L116 (C08R27X0EAH/1759274400.792657, C08R27X0EAH/1759140300.935009) | both posts | F23 VERIFIED | Match |
| OE 20 | "coinler x2 olmadan geldi, run'ın coinlerinin yarısı gitti. ZOM-473" | SQL L120, L122, L123 (D0770ET1HV2 messages) | Turkish text verbatim | F24, F25 VERIFIED | Match |
| OE 21 | "Each of them lost a life and had to start the fight again." | SQL L129–L130 (vincent.parker@harmonygames.co/1844730396672762606) | body, subject, date | F26 VERIFIED | Match |
| OE 22 | "QA Lead, Cobalt Playtesting (ZM3D playtests)" | SQL L283 contact 29016e2ba1a844a2509b847b | job field | F27 VERIFIED | Match |
| OE 23 | "Yep it works as expected" | hg.py get slack D079SNE2TL4/2025-09.json /260, /263, /265; SQL L126 | text, ts → 16:38 / 18:16 / 21:58 / 22:01 UTC | F28, F29 VERIFIED | Match |
| OE 24 | "I'm holding the prod load until after the store push" | SQL L287, L289, L290, L291 (match3d-backend#36, #rev_1, #rev_2, #rc_1) | merge, reviews, review comment | F30 VERIFIED | Match |
| OE 25 | "Fix season pass main screen instance from join popup" | hg.py get slack C05433XK267/2025-09.json /1120–/1132 | Started lines, #2027, #2028, #1759 | F31, F32 VERIFIED | Match |
| OE 26 | "A failure in any UPDATE column blocks the release - fresh-install-only regressions do not pass the gate." | hg.py get confluence confluence_working.json /pages/7/body (page_qa_runbook) | three contiguous sentences | F33 VERIFIED | Match |
| OE 27 | "Fresh install - Android #135 (Pixel 6)" | SQL L261 grid_json (f_b91db376f65604b8602657) | 5 rows Pass, update columns empty | F34 VERIFIED | Match |
| OE 28 | "install the N-1 build from the App Store, play past level 200, install TestFlight 50 over it, launch." | SQL L263 (f_5e40215b7d4d24b0455412) | 4 rows, 1 FAIL | F35 VERIFIED | Match |
| OE 29 | "Updating the game from earlier build breaks the core game." | linear data.json /issues/3490 (ZOM-424) | Done 2025-07-23T11:23:10Z, object-id breakage | F36 VERIFIED (absence scan in ledger) | Match |
| OE 30 | "Go/no-go for the ZM store push (ZOM-570)." | SQL L216 (evt_81e6dc4dbfd331f1a6a317) | starts 2025-10-03T16:00:00Z | F37 VERIFIED | Match |
| OE 31 | "after the update the save came back at level 1 with 500 coins instead of level 212 with 18,400 coins" | SQL L263 | values of the FAIL row | F40 not_a_claim (created content), values VERIFIED | Match |
| OE 32 | "like "Sep 30 - Android #135 / iOS #50"" | SQL L257 ("named after the candidate builds") | example name of a created tab | F41 not_a_claim | Match |
| OE 33 | "Totals: 19 BLOCKER, 10 FIXED, 19 KNOWN ISSUE, 85 NO CALL" | solver/truth.json; SQL L257 | per-call lists equal the answer key plus the new ticket | F38 VERIFIED (counts by calculation) | Match |
| OE 34 | "lists all 19 blockers by their existing keys" | SQL L11 (ZOM-570); SQL L277 (reuse rule) | 18 keys + the new ticket | F39 VERIFIED | Match |
| OE 35 | "the QA call is NO-GO" | SQL L118 (thread ts 1759263900.484190); SQL L32 | destination and call | F39, F41 VERIFIED | Match |

## Findings
| # | Severity | Component | Event | Quoted span | Rule (Eval § / source) | What is wrong | Evidence (ledger fact + source pointer) |
|---|---|---|---|---|---|---|---|
| 1 | RESOLVED (rewritten) | Accuracy | OE 4 | among the results Vincent can read are | Eval 2.4 (every Expected value quotable) | The inherited draft stated the exact result set of a Drive search ("four files"), which the tool path cannot be shown to return; now names only the records it needs | F5; SQL L221, L234, L243 |
| 2 | RESOLVED (trimmed) | Accuracy | OE 6 | A submission has exactly what was on main when its job started (the Started line in #builds) | Eval 2.4 absence cue | The draft quoted "and nothing that landed after", an absence cue on an Expected line; now quoted up to the Started line and paraphrased | F7; SQL L235 |
| 3 | RESOLVED (paraphrased) | Accuracy | OE 7 | go by when the ticket was closed | Eval 2.4 absence cue | The draft quoted "if nothing shows when the fix landed" and "nobody re-tested"; the clause is now paraphrased with exact fragments | F9; SQL L257 |
| 4 | RESOLVED (rewritten) | Accuracy | OE 7 | the previous gate's register for #127 / #40 | Eval 2.2 / O1 (an asserted fact must be in a record) | The draft said the tab was "made before Leonard's Sep 23 rules", which no record time on the tab states | F10; SQL L258 |
| 5 | RESOLVED (paraphrased) | Accuracy | OE 8 | he asks for a new ticket only for a problem that hasn't been filed yet | Eval 2.4 absence cue | The draft quoted "nobody filed it yet" | F11; Trello 68dc3ef455344e471b1d2ea9 (SQL L277) |
| 6 | RESOLVED (rewritten) | Completeness | OE 11 | In Linear, run linear_list_comments on each of the 132 tickets from OE 10, one issue at a time. | Eval 3.1 (population derived before it is narrowed) | The draft read comments only on hand-picked subsets; OE 11 now reads all 132 and OE 12–OE 18 work on that read | F15; SQL L30–L87 |
| 7 | RESOLVED (paraphrased) | Accuracy | OE 13 | ZOM-577 (level_fail fires without booster_used) is analytics | Eval 2.4 absence cue | The draft quoted ZOM-577's title, which contains "missing" | F17; SQL L24 |
| 8 | RESOLVED (trimmed) | Accuracy | OE 14 | Android #135 on the same low-end device: cold start into level 3 froze again | Eval 2.4 absence cue | The draft quoted "taps did nothing until I force-quit" | F18; cmt_zom449_2 (SQL L70) |
| 9 | RESOLVED (paraphrased) | Accuracy | OE 15 | the boss buster still renders with half its body gone | Eval 2.4 absence cue | The draft quoted "boss buster still half missing" and ZOM-348's "the other ribbons are still missing" | F19; cmt_zom468_2 (SQL L71), cmt_zom348_2 (SQL L48) |
| 10 | RESOLVED (trimmed) | Accuracy | OE 21 | Each of them lost a life and had to start the fight again. | Eval 2.4 absence cue | The draft quoted "Nothing could clear them, the board never emptied" | F26; SQL L130 |
| 11 | RESOLVED (added) | Completeness | OE 22 | QA Lead, Cobalt Playtesting (ZM3D playtests) | Eval 3.1 (a fact used needs a retrieving event) | The draft relied on "Puzzles vs Zombies" being ZM3D without a step that shows it; the Contacts read now does | F27; contact 29016e2ba1a844a2509b847b (SQL L283) |
| 12 | RESOLVED (rewritten) | Accuracy | OE 24 | and his chest claim there didn't land | Eval 2.4 absence cue | The draft quoted "nothing landed" and "does nothing on prod yet"; the review comment is now quoted in two clean sentences | F30; match3d-backend#36#rc_1 (SQL L291) |
| 13 | RESOLVED (trimmed) | Completeness | OE 26 | File the bug with device, OS version, source build and repro steps | prompt-incorporation-v1; Eval 3.3–3.4 | O2 proposed four writes from the runbook's process bullets (link the bug on the page, mirror to the Support Playbook, post the matrix, link it from ZOM-570). Rejected: the prompt incorporates the runbook's checks for the new-ticket ask only ("for anything the checks in the QA regression runbook turn up"), and prescribing those writes would be unauthorized; the quote no longer carries "and link it here" | F33; page_qa_runbook (confluence_working.json /pages/7) |
| 14 | RESOLVED (rewritten) | Accuracy | OE 30 | every write below is made now, before it | Eval 2.5 (clock) | The draft stated the writes are made "on 2025-10-01", a date no record holds; now tied to the event start | F37; evt_81e6dc4dbfd331f1a6a317 (SQL L216) |
| 15 | RESOLVED (rewritten) | Accuracy | OE 14 | Re-checked on the candidates and still failing | Eval 2.3 qualifiers (platform /oe on sha 3ddf0464) | The header "the latest checks on the open bugs that still fail" grouped ZOM-559 (latest report on #133) and ZOM-293 (a July comment, no build) with candidate re-checks; the event now splits re-checked from not re-checked, names the build of each re-check, states the fixed rule as applied to two open tickets, and gives ZOM-293's description | F18; cmt_zom559_1 (SQL L45), cmt_zom293_1 (SQL L87), SQL L60-L70; linear /issues ZOM-293 |
| 16 | RESOLVED (rewritten) | Accuracy | OE 5 | also counts as fixed if its fix is actually in the candidate builds (or live on prod), noted as not re-checked. | Platform PASS report, optional note 1 | The fixed rule skipped Leonard's Done-not-re-checked sentence; it is now quoted so the ZOM-569 reasoning in OE 25 is self-contained | F6; SQL L229 |
| 17 | RESOLVED (rewritten) | Accuracy | OE 12 | though ZOM-536 and ZOM-555 carry the Bug label and all three are Done | Platform PASS report, optional note 2; Eval 2.3 qualifiers | The Bug label was stated for all three tickets, but ZOM-498 is labelled Improvement; the heading also called all three "art follow-ups" | F16; linear /issues ZOM-536, ZOM-555, ZOM-498; SQL L82-L84 |
| 18 | RESOLVED (rewritten) | Accuracy | OE 16 | although all three are still open in Linear (ZOM-429 and ZOM-517 Backlog, ZOM-564 Todo) | Platform PASS report, optional note 3 | Only two of the three were said to be open; ZOM-564 is Todo | F20; linear /issues ZOM-429, ZOM-517, ZOM-564 |
| 19 | RESOLVED (rewritten) | Accuracy | OE 25 | more than eight days before both Started lines | Eval 2.3 qualifiers | "a week before" understated the gap (8 d 3-4 h); the close-time fallback is now quoted with its condition, the #1974 change is placed before both Started lines, #1759's time is labelled as its Changes post, and the #135 change "fix trampoline and glue count being set to 0 on game start" is shown not to be a re-check of ZOM-293 | F31, F32; SQL L257; C05433XK267/2025-09.json /902, /1124, /1131 |
| 20 | RESOLVED (rewritten) | Accuracy | OE 33 | the result of its latest check where there is one | Eval 2.3 qualifiers | "each row has the result of its latest check" overstated: ZOM-559, ZOM-293 and ZOM-569 were not re-tested on #135 / #50 and NO CALL rows need no check | F38; SQL L31, L45, L87 |
| 21 | RESOLVED (rewritten) | Accuracy | OE 27 | the columns are "Area", "Fresh install - iOS #50 (iPhone 13)" | Eval 2.3 (lists exact) | The column list left out "Area" | F34; SQL L261 |
| 22 | RESOLVED (rewritten) | Accuracy | OE 7 | open bugs not re-tested | Eval 2.3 qualifiers | The n/a paraphrase dropped "open" from the not-re-tested branch, which would also take in Done bugs | F9; SQL L257 |
| 23 | RESOLVED (rewritten) | Accuracy | OE 8 | So ZOM-435 still fails on Android #135 (player stuck): a BLOCKER. | Eval 2.3 qualifiers | "a BLOCKER on the candidates" claimed both builds; Leonard re-tested Android #135 only | F11; Trello 68dc63484a5b2d0a869e758f (SQL L278) |
| 24 | RESOLVED (rewritten) | Accuracy | OE 9 | cut at 2025-09-22 12:30:43 UTC (Android #127) and 12:32:20 UTC (iOS #40) | Eval 2.3 qualifiers | One cut time was given for both builds; iOS #40 started 97 seconds later | F12; C05433XK267/2025-09.json /692, /693 |
| 25 | RESOLVED (rewritten) | Accuracy | OE 17 | the comments on the tickets whose call or build status another record settles | Eval 2.3 qualifiers (group label) | "comments that point to evidence elsewhere" included ZOM-562 and ZOM-473, whose comments name no other record; the closing sentence now says which record settles each | F21; SQL L66, L74 |
| 26 | RESOLVED (rewritten) | Accuracy | OE 18 | filed on Sep 30 after the candidates were cut | Eval 2.3 qualifiers (date window) | "filed on the candidates ... Sep 29-30" was wider than the group (all ten were created 2025-09-30 20:40-22:50 UTC) and ZOM-575 names no build | F22; SQL L18-L27 |
| 27 | RESOLVED (rewritten) | Accuracy | OE 20 | in the boss arena the nuke went to a dead zombie | Eval 2.3 (translation of a quoted record) | Two glosses said more or less than the quoted Turkish: the ZOM-535 gloss used words outside the quoted span (the quote now covers them) and the ZOM-473 gloss is now closer to "hala geçilebiliyor" / "x2 olmadan geldi"; the closing labels follow the records | F24, F25; SQL L120, L123-L125 |
| 28 | RESOLVED (rewritten) | Accuracy | OE 29 | the bottom boosts not visible | Eval 2.3 (lists exact) | ZOM-424's symptom list dropped one of four symptoms and narrowed "the items I had" to equipped items | F36; linear /issues/3490 |
| 29 | RESOLVED (rewritten) | Accuracy | OE 31 | install TestFlight 50 over it, launch. Only one new ticket | Eval 2.6 / O1 (required write content) | The new ticket's required content included a sentence citing the runbook row and the gate, which no record asks for | F33, F40; SQL L263-L274; page_qa_runbook |
| 30 | RESOLVED (rewritten) | Accuracy | OE 35 | giving the QA call: NO-GO for Android Submission #135 and iOS Submission #50, because of the 19 blockers | Eval 2.6 / O1 (required write content) | The reply's expected content read as requiring a register mention and the blocker count; the prompt asks for the QA call in the thread | F39, F41; SQL L32, L118 |

## Pre-verdict sweep
| Eval 4.0 check (7) | Result |
|---|---|
| One wrong count, ID, channel or tool | PASS — O1 recounted every list (112 + 20, 38, 85, 133, 19) and every ID; tools all in Evals/references/tools/catalog.json |
| One required write missing | PASS — create (OE 31), add tab (OE 32), write rows (OE 33), description update (OE 34), thread reply (OE 35) |
| One fact in expected data with no retrieving event | PASS — every Expected value traces to OE 1–OE 30 (record validator: 764 values, 0 unledgered) |
| One unledgered Expected value or unbacked absence word | PASS — 0 absence cues on Expected lines; 764 values ledgered |
| One act-vs-defer conflict | PASS — ledger §C defer searches; Arthur's "holding the prod load" (match3d-backend#36#rc_1) holds his data load, not any write |
| One non-action or final-response event | PASS — none |
| One prompt-forbidden write | PASS — no write outside the prompt's four asks |
| One missing recovery/wait event for an injected error | PASS — friction none (03_Error_Async_Config.txt) |

## Advisory (no effect on the prediction)
| Event | Note |
|---|---|
| OE 32 | The tab name is an example; any name that names the candidates is accepted (How we gate, SQL L257). The final red-team pass suggested ending the Expected line at the existing tab names; done |
| OE 11 | The final red-team pass flagged a claim about what the issue list returns as unprovable from the catalog; removed |
| OE 33 | gsheets_values_append is an equally valid route to the same rows |
| OE 12–OE 18 | Reasoning steps over OE 10 and OE 11; they name the records they work on and need no tool call |

## Tally
Blocking 0 (incomplete 0 · inaccurate 0 · length 0) · moderate 0 (non-action 0 · final-response 0 · format 0) · minor 0 · unresolved 0 · advisory 4 · resolved 30

## Self-review

Check self-review (playbook §Self-review, GEN_EXECUTION §6a):

1. Re-read as the eval: walked Eval 2 §1.2 (inventory: 35 STEP segments), §1.3 (five fields per step), the HARD GATE (no non-action or final-response segment), §2.1–2.7 (catalog tools, services, identifiers, numeric observability, expected-data sign-off, clock, act-vs-defer, format), §3.1–3.6 (coverage R1–R7, dependencies, writes, prohibited writes, friction none, path feasibility) and §4.0 (sweep above).
2. Counter-readings, one per Coverage and Findings row (R1–R7, Findings 1–30):

| Judgement | Counter-reading | Resolution (evidence) |
|---|---|---|
| R1 covered | Counter-reading: the gate could be read as the Sep 22 tab's Bug-only scope, so OE 10's 132 rows would over-cover | Leonard's Sep 23 scope f_632c44650df44fe252ee59 (SQL L222) governs; O3 found the same scope; truth.json 132 keys |
| R2 covered | Counter-reading: "the background" is only ZOM-570's description, so OE 4–OE 8 are extra | ZOM-570 (SQL L11) says both docs "apply" and names the tech-issues card; extra reads cannot cost completeness |
| R3 covered | Counter-reading: adding a tab and writing rows in one event would be enough, so splitting them is redundant | Eval 2.7 MULTIPLE_ACTIONS counts two writes in one event as a format defect; two events (OE 32, OE 33) on f_0ebfccf33076f9dbf086bc |
| R4 covered | Counter-reading: a comment on ZOM-570 would satisfy it ("Other push notes go in the comments here", SQL L17) | The prompt names the description; OE 34 updates the description of ZOM-570 |
| R5 covered | Counter-reading: other failing candidates (ZOM-573, ZOM-578) are runbook findings needing tickets too | They already have tickets (SQL L20, L25); the reuse rule (Trello 68dc3ef455344e471b1d2ea9) reuses them |
| R6 covered | Counter-reading: a new post in #zombie-bugs also gives the call | Leonard's cmt_zom570_1 (SQL L32) "not a new post"; OE 35 replies under 1759263900.484190 |
| R7 covered | Counter-reading: the deadline could have passed by the clock | evt_81e6dc4dbfd331f1a6a317 (SQL L216) starts 2025-10-03T16:00:00Z, after the clock 2025-10-01T07:00:00Z |
| Finding 1 resolved | Counter-reading: the "four files" claim was true in the data, so it was not a defect | The data has the files, but a search's result set depends on matching rules the catalog does not fix; the rewrite claims only what F5 (SQL L221, L234, L243) proves |
| Finding 2 resolved | Counter-reading: a verbatim record quote with "nothing" is allowed (≥3 words) | Allowed only when the whole ledger entry is that quote; trimming removes the risk without losing the rule (SQL L235) |
| Finding 3 resolved | Counter-reading: paraphrasing the fallback loses its condition | The paraphrase keeps the condition ("when the time the fix landed doesn't show") and the exact fragment "go by when the ticket was closed" (SQL L257) |
| Finding 4 resolved | Counter-reading: the Sep 22 tab obviously predates the rules | Vincent's note C08R27X0EAH/1758563100.005758 is Sep 22, but no record dates the tab itself; the rewrite asserts only its builds (SQL L258) |
| Finding 5 resolved | Counter-reading: the paraphrase changes Arthur's rule | Same meaning: "only open a new one if" the problem is unfiled (Trello 68dc3ef455344e471b1d2ea9) |
| Finding 6 resolved | Counter-reading: reading only the tickets that turn out to matter is a valid route | The agent cannot know which tickets carry comments without reading all 132 (SQL L30–L87 hold comments on 38) |
| Finding 7 resolved | Counter-reading: ZOM-577's title is needed to show it is analytics | Its Analytics label and the level_fail / booster_used fields (SQL L24) show it |
| Finding 8 resolved | Counter-reading: the trimmed quote loses the force-quit detail | "and he had to force-quit" stays in prose; the freeze alone is a blocker (f_632c44650df44fe252ee59) |
| Finding 9 resolved | Counter-reading: the paraphrase of ZOM-468 is not quotable | It is prose (no quote marks), restating cmt_zom468_1 "half its body missing" (SQL L38) without the absence cue |
| Finding 10 resolved | Counter-reading: the dropped sentence explains why the boss timer ran out | The lost life is what makes ZOM-562 a blocker (SQL L130); the dropped sentence does not change the call |
| Finding 11 resolved | Counter-reading: the Contacts step is unnecessary because the email says "TestFlight build 50" | The email names the game "Puzzles vs Zombies"; contact 29016e2ba1a844a2509b847b (SQL L283) ties the sessions to ZM3D |
| Finding 12 resolved | Counter-reading: splitting rc_1 hides that the prod claim failed | The prose says "his chest claim there didn't land", restating match3d-backend#36#rc_1 (SQL L291) |
| Finding 13 resolved | Counter-reading (false-positive check of the rejection): the runbook's process bullets are part of "the checks" | The prompt asks for a ticket "for anything the checks … turn up"; the /prompt rev18 incorporation chain limits the runbook to the new-ticket ask; page_qa_runbook's bullets are process, not checks |
| Finding 14 resolved | Counter-reading: "2025-10-01" is the persona's today, so it is a fair date | It is the clock, not a record value; tying the writes to the event start (SQL L216) avoids an unquotable date |
| Finding 15 resolved | Counter-reading: "latest check" can cover ZOM-559's #133 report and ZOM-293's July comment, since each is the newest record on its ticket | The platform /oe (sha 3ddf0464) confirmed the header as a wrong qualifier because it said "still fail" on the candidates; cmt_zom559_1 names #133 (SQL L45) and cmt_zom293_1 names no build (SQL L87) |
| Finding 16 resolved | Counter-reading: the extra sentence decides no row, so quoting it is noise | It explains why ZOM-569 (Done, not re-checked) is not FIXED: its fix is not in the candidate builds (OE 25, C05433XK267/2025-09.json /1129); SQL L229 |
| Finding 17 resolved | Counter-reading: "Bug label" was a paraphrase of Leonard's rule, not a claim about each ticket | The parenthetical sat on the three keys; linear /issues shows ZOM-498 labelled Improvement |
| Finding 18 resolved | Counter-reading: naming two open tickets did not say ZOM-564 was closed | Listing only two as "still open" invites that reading; linear /issues ZOM-564 state Todo |
| Finding 19 resolved | Counter-reading: "a week" is a round figure | The gap is 8 d 3 h 32 m to 8 d 4 h 50 m (linear completed_at vs ts 1759257812.041449); "more than eight days" is exact |
| Finding 20 resolved | Counter-reading: an empty QA result is obviously fine for NO CALL rows | The sentence said "each row"; ZOM-569's only comment is a developer's branch note (SQL L31), which a run could copy as a check |
| Finding 21 resolved | Counter-reading: "Area" is the row label, not a result column | SQL L261 grid_json header row lists six columns, "Area" first |
| Finding 22 resolved | Counter-reading: the How we gate cell is the source either way, so the paraphrase does no harm | Without "open" the n/a branch overlaps the Done-bug branches of the same cell (SQL L257) |
| Finding 23 resolved | Counter-reading: one failing candidate makes ZOM-435 a candidate blocker | The call is unchanged; the wording now names the build the re-test used (SQL L278 "android #135") |
| Finding 24 resolved | Counter-reading: the earlier start is the cut that matters for the Done cutoff | Both times are now stated; the first Done move after either is 13:53:29Z, so the population is unchanged (ZOM-435 completed_at, linear /issues/3502; C05433XK267/1758544243.280239 and C05433XK267/1758544340.770929) |
| Finding 25 resolved | Counter-reading: every listed ticket needs another record, so the old label fit | The old label described the comments; ZOM-562's and ZOM-473's comments name no record (SQL L66, L74); the new label describes the tickets |
| Finding 26 resolved | Counter-reading: ZOM-575 is in scope as a ticket filed during the gate whatever build it names | It stays in scope and NO CALL; the change only makes the header and date window match SQL L18-L27 |
| Finding 27 resolved | Counter-reading: glosses are aids, not Expected values | A gloss on a quoted record is read as a claim about it; the new quote (SQL L125) holds every word the gloss uses |
| Finding 28 resolved | Counter-reading: three symptoms are enough to show ZOM-424 is a different bug | True, but a list presented as the record's list must be complete; linear /issues/3490 has four |
| Finding 29 resolved | Counter-reading: citing the gate in the ticket is good practice | It may be written, but stating it as expected content makes it required; the runbook asks for device, OS version, source build and repro (page_qa_runbook) |
| Finding 30 resolved | Counter-reading: a NO-GO without its reasons is a weak sign-off | The blockers stay as the stated basis of the call; the prompt and SQL L32 require the call as a thread reply |

3. Re-verified: every expected value the report relies on was re-read in this run — seeded rows from 01_Universe_Inject.sql by file line, base Linear through hg.py get-many (reverify/linear_base_hg.json), base Slack and Confluence through hg.py get on the cited pointers; Working_Files/research/oe/scripts/oe_lint.py found 189 of 191 quoted spans verbatim in records (the 2 others are a search query and an example tab name) and 0 absence cues; Evals/tools/hg_oe_review.py validate on the format-2 record returned PASS 5 / COMPLETE, 798 values, 0 unledgered.
4. Fixes: every rewritten span in Findings 1–30 was re-checked against its record in this run (oe_lint.py, O1, the four qualifier hunts and the narrow final check of the changed spans).
5. Prediction per component: Completeness 5 (every requirement covered; O2's four proposed writes rejected as unauthorized), Accuracy 5 (O1 complete; both of its findings rejected against the records; 0 format defects). Path feasibility SUPPORTED · Task solvability SUPPORTED_BY_OE.

Unresolved: none.

```
STAGE GATE oe-check: PASS — Task_Authoring/task_inputs · 08_OE_Check.md#55dc1b648e49 · 08_Oracle_Events.md#b4ca728961d2 · 08_OE_Writing_Ledger.md#a9146eb6f4eb · __context__#fb209f3058d7 · __assignment__#c2f3888d53bd · __policy__#dc4ab5df3cdd · __gate_policy__#9b78441396d8 · __review__#4c88e8308ed5 · blocking 0 · warnings 0 · checks 20
[PASS] assignment.v3_context: Vincent Parker / Game Systems Engineer; easy cap <90%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 08_OE_Check.md
[PASS] structure.inputs: 2 input(s) present: 08_Oracle_Events.md, 08_OE_Writing_Ledger.md
[PASS] structure.fresh: every output newer than its inputs (08_Oracle_Events.md, 08_OE_Writing_Ledger.md)
[PASS] chain.oe-writing: upstream 'oe-writing' PASS pasted and current (08_OE_Writing_Ledger.md#a9146eb6f4eb, 00_Assigments.md#90d69427cab7, 04_Prompt.txt#e775405ef8d5, 01_Grounding_Dossier.md#4f38db93303c, 01_Universe_Inject.sql#5a8d995238f3, 03_Error_Async_Config.txt#af03ea097424, __context__#fb209f3058d7, __assignment__#c2f3888d53bd, __policy__#dc4ab5df3cdd, __gate_policy__#9b78441396d8, __review__#4c88e8308ed5)
[PASS] structure.sections: 7 required sections present and non-empty (08_OE_Check.md)
[PASS] structure.placeholders: no placeholders in 08_OE_Check.md
[PASS] structure.header_counts: header matches 08_Oracle_Events.md (35 events, 35703 chars)
[PASS] structure.prediction: /oe prediction line present
[PASS] structure.clock: 'Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)' matches the universe
[PASS] evidence.quoted_spans: 31 quoted span(s) verified as exact substrings of 08_Oracle_Events.md
[PASS] evidence.findings_evidence: 30/30 items carry a source pointer (min 100%)
[PASS] evidence.signoff_reread: 35/35 items carry a source pointer (min 100%)
[PASS] structure.sweep: pre-verdict sweep has 8/7 rows
[PASS] structure.tally: tally Blocking 0 vs 0 BLOCKING findings
[PASS] review.counter_readings: 38 evidenced counter-readings (of 38 found; need ≥ 37) in 08_OE_Check.md
[PASS] review.coverage: self-review addresses all 1 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```




## Reminders
- The tool-call minimum is measured on the golden run or the 6-rollout average, never on the OE count.
- Fix the events (Claude, Codex or the human), re-run check, then run /oe.
