Sweep dispositions (each re-checked against the base through hg.py before changing the design). Full tables are in the two sweep files.

| Severity | Finding | Disposition | Evidence and change |
|---|---|---|---|
| BLOCK | inline_td, inline_axe dated after merge | Fixed | re-dated before Arthur's reviews: 2025-11-19T13:04:10Z (approved 13:05:32Z) and 2025-11-20T01:50:40Z (approved 01:51:51Z); harmonygames-Games/GameOfDominoes#1905, #1908 |
| BLOCK | td_note, axe_note predate the tickets starting | Fixed | re-dated after the merges and scoped to the main screen only; ENG-2434, ENG-2426 |
| BLOCK | shop icons line re-closed by Brian's later posts | Fixed | correction moved to Dec 1, after C09Q4S613CN/1764192110.492299 and /1764364896.416939 |
| BLOCK | ENG-2432 and ENG-2433 Done while their shop icons are Broken | Fixed | H1 now says a bug on a screen doesn't hold its child |
| BLOCK | later DD economy canvas unscoped | Fixed | H1 leaves it out; distractor D_ECONCANVAS C4208B207A1A/1765298859.629579 |
| BLOCK | 'An open PR doesn't count' is false for #1914 | Fixed | reworded: a PR that never made it into that build doesn't count; #builds shows the build line C05433XK267/1765310004.760809 |
| FORK | train and team lines have later commits, two standards | Fixed | H1 states the test once; seeded Vincent replies after each commit keep them Broken (commits 4189eca5, 100612a7) |
| FORK | Win & Collect disabled Dec 16: ticked lines and ENG-2424 | Fixed | H1 first-fit order keeps ticked lines Fixed; ENG-2424 stays (C9CA62B5180A/1765927876.696389), so 23 children end Done |
| FORK | 'has a comment thread' gives 61 or 63 lines | Fixed | H1 says every ticked or unticked line; two empty-text roots have no line (CE156FDFB428/1763042124.247899) |
| FORK | no record for ENG-2427, 2429, 2431 | Fixed | default-Done rule plus a Brian check note on each moving child |
| FORK | Tavern correction predates Brian's blanket posts | Fixed | moved to Marcus's DM on Dec 3, D05USBTQY1F, after those posts |
| FORK | lives lines could be Fixed by Oliver's commit 3646982c | Fixed | Vincent replies say the same after that change (CE156FDFB428/1763845812.703339) |
| FORK | ENG-2331 and ENG-2277 against Fixed and Gone | Fixed | H1 first-fit order: Fixed, Gone, Covered, Broken |
| FORK | still-broken count 7 or 9 | Fixed | H1: Covered ones count as still broken in the reply, so 9 |
| FIX | rule doc cited a later amendment; 'on Thursday' on a Thursday | Fixed | H1 now says 'If anything changes after this' and 'today'; ENG-2401 |
| FIX | hub overclaims and ignored Owen's guest status | Fixed | hub softened ('most of', 'once the data export is done') and gives read access back; D05S1S2AB5M |
| FIX | deck false, not stale, after the gift note | Fixed | deck dated Nov 21 and the gift note Nov 24, so the note overturns it; f_d15a8c70e3f2b94a61c8d3 |
| FIX | season note rivalled by Dec 4 commits | Fixed | note moved to Dec 5 and names the reward track; ENG-2428 |
| FIX | alias notes overclaimed the tickets | Fixed | reworded to fit ENG-2073 and ENG-2363 |
| FIX | Gmail and Trello ids did not match their dates | Fixed | regenerated from the seeded dates; mailbox id for owen.baker@harmonygames.co |
| FIX | 'sprint' is not the team's word | Fixed | seeds say 'UI work'; C09Q4S613CN has no use of it |
| LIMIT | 0.3.310 has no base record tying it to Feb 12's build | Accepted | H1 is the authority; sequence holds (C09SWTHEMEW/1770753609.436139); no row joins it to a review version (NB-21) |
| LIMIT | 'no later fix' rests on commit titles | Accepted | the rule's test is a commit named for the bug; prefab diffs are not in the export |

Injection sweep (/create-injection rev1): a third fresh reviewer read the new seeds against the base. Each finding was re-checked through hg.py before the change. It printed some SQL rows outside its list, so its view of those rows is not blind.

| Severity | Finding | Disposition | Evidence and change |
|---|---|---|---|
| BLOCK | ENG-2419 note dated before the retry screen fix | Fixed | note moved to Nov 20, after #builds DD Android #2179 and Owen's reply CE156FDFB428/1763549617.765149 |
| BLOCK | ENG-2430 note dated before the offers fix | Fixed | note moved to Nov 21, after Brian's fix on CE156FDFB428/1763549271.970799 and #2205 |
| BLOCK | ENG-2427 note dated before the River Rush sail fix | Fixed | note moved to Nov 21 15:00, after #2214 on Nov 21 04:08 (CE156FDFB428/1763394845.067219) |
| BLOCK | ENG-2425 note dated minutes after a banner bug | Fixed | note moved to Nov 21, after #2187, #2189 and #2208 (CE156FDFB428/1763131864.808869) |
| BLOCK | ENG-2398 'no bug behind it' contradicts the ticket | Fixed | reworded as the stopgap for the relogin problems |
| BLOCK | Marcus says he is on the window after finishing it | Fixed | reply now only says he hasn't got to the mega tile; C05V5FNLB9V/1764256187.655299 |
| FIX | ENG-2410 shipped offer work through #1898 | Fixed | note moved to Nov 21 with ENG-2430 |
| FIX | ENG-2429 note after the checklist tick | Fixed | note moved to 14:27, before the ENG-2404 tick at 14:29:13 |
| FIX | #1902 and #1903 claims beyond their files | Fixed | comments now name the pop up, banner and stars, and the out of moves screen; harmonygames-Games/GameOfDominoes#1902, #1903 |
| FIX | Vincent's 'too' and a same-day 1 pixel gap | Fixed | reply now reads 'looks ok now'; his gap post is about navigation tooltips, CE156FDFB428/1763394941.178509 |
| FIX | tracker and deck timing | Fixed | tracker stays Nov 20 with Season Pass 'next'; deck moves to Nov 21 after #2214; gift note moves to Nov 24 |
| FIX | tracker and deck list 6 of 15 Core children | Fixed | all 15 are listed |
| FIX | 'new atlases' has no source | Fixed | 'optimized sprites', from the #1905 body, in the deck and the Trello card |
| FIX | deck and tracker differ on Daily Gift | Accepted | tracker Nov 20 'last pass', deck Nov 21 claims it shipped, Brian's Nov 24 note corrects it: a dated human sequence |
| FIX | inline comments cite prefabs not in the export, and one hunk has identical lines | Fixed | both now anchor on files the PRs changed (CodeRabbit summaries #1905#c_2 and #1908#c_2) with new-file hunks |
| FIX | ENG-2426 note before the Axe Arena overflow report | Fixed | note moved to Nov 21 15:30, after Arthur's Done on CE156FDFB428/1763643032.027129 |
| LIMIT | could not verify the Purple fix, the 24 hours checkbox's screen, ENG-2406's video, or every channel | Accepted | the Purple line is ticked; no record about it says otherwise, and the tick rule decides it |

Later change: the Linear notes on PR-state children left the design with the hazard change (design_delta 'tree states and notes'), so the re-dated ENG-2419, ENG-2425, ENG-2427, ENG-2426 and ENG-2434 notes no longer exist; Brian's ticks on card 690b27282f4c1b7a6e93d512 carry no date. The ENG-2410, ENG-2429 and ENG-2430 fixes stand.

Fork sweep before /prompt (rev2): a fresh agent with no answer key reproduced 58 Fixed, 3 Gone, 2 Covered, 7 Broken, 68 new tickets and 9 still broken. Each finding was re-checked through hg.py.

| Severity | Finding | Disposition | Evidence and change |
|---|---|---|---|
| BLOCK | which build each child note names; held and Done children | Fixed | Brian's comment 690b29bc3c7d2e51b0f86a47 now says the current public build; the rule doc applies it to the line on every child; f_3ca9e15d7b20f4e681ad52 |
| BLOCK | ENG-2424 Done or stays | Fixed | the rule doc adds 'or the screen is switched off there'; Owen disabled it, C9CA62B5180A/1765927876.696389, and no later record turns it back on |
| BLOCK | Dec 31 no-ads post a bug or not | Fixed | C05V5FNLB9V/1767191512.428539 is Arthur's question; the rule doc now says a design question for Leonard isn't a bug post |
| FIX | fragments and alike lines merged | Fixed | 'One Linear record per canvas line and one per bug posted after it, even where two read alike' |
| FIX | title form | Fixed | 'the line without its tick box' |
| FIX | fix notes on Done tickets | Fixed | hub reworded; 'nothing in the description' |
| FIX | Tavern against 'Gacha visuals updated' | Accepted | H1 needs a commit named for the bug; that one isn't |
| FIX | Axe Arena and Tile Dozer against the checklist ticks | Accepted | H1: a record showing part of the screen isn't in the build holds the child; the checklist is also wrong on Season Pass |

Re-check of the rev2 wording: all three BLOCKs closed and every write traced to the DM or doc. It raised three small new forks, each fixed by the wording above: 'at the time' for children closed in November, Robert's music post ending 'intended?', and Dec 22's two top-level posts for one bug. Tavern and the checklist ticks stay as accepted.

/prompt on rev2 and the rev3 sweeps: the platform report is run_forensics/rev2/1_prompt_FAIL_r2.md. rev3 fixes F1 to F4, NB-1, NB-14 and the inline comment dates. A fresh item-by-item sweep then reproduced every count and raised:

| Severity | Finding | Disposition | Evidence and change |
|---|---|---|---|
| BLOCK | the deck and checklist are newer than the inline comments and name both screens | Fixed | they now speak of main screens, so nothing newer says the popups were done; f_d15a8c70e3f2b94a61c8d3, harmonygames-Games/GameOfDominoes#1905#rc_1 |
| FIX | Dec 5 Gacha commit after Marcus's note | Fixed | Marcus's note moved to Dec 11, after that commit and the night's Android build #2301; D05USBTQY1F/1765452012.418229 |
| FIX | bottom bar reply names only the bar | Fixed | it now covers the top panel; C05V5FNLB9V/1767021345.207719 |
| FIX | 'the canvas's last line' could be the canvas body | Fixed | 'the last line in that comment channel'; f_3ca9e15d7b20f4e681ad52 |
| FIX | 'part of its screen isn't in that build' could catch removals | Fixed | 'a piece of its UI work never made it into that build'; f_3ca9e15d7b20f4e681ad52 |
| FIX | backend errors line as Gone | Accepted | inference only; no record ties it to the removal; CE156FDFB428/1763042058.918579 |
| FIX | mentions in titles | Accepted | §4b accepts raw or readable mentions |

Blind coherence audit of rev3. Each finding was re-checked through hg.py.

| Severity | Finding | Disposition | Evidence and change |
|---|---|---|---|
| BLOCK | 'read access back' has no account change: multi-channel guests were ruled out | Fixed | hub: back on a paid seat; five seats, three kept, C0ADGSZKR3R/1770842395.641349 and C0ADGSZKR3R/1770842309.637769 |
| BLOCK | Vincent's Nov 22 replies follow his farewell and name commits that don't exist | Rejected | commit 3646982c lands Nov 22 03:30 and 'Fix trains a bit better' Nov 22 19:07 (C050WGU41HR); D07GMT8NVM2 Nov 21 mentions a new job only; he posts until Nov 23 |
| BLOCK | masters stay Todo; ENG-2405 has #1905 merged | Accepted | /prompt on rev2 raised no issue with their state; the rule doc keeps masters as they are; base_check blocks an UPDATE of ENG-2405 (L03) |
| BLOCK | held children stay in stale states | Accepted | /prompt on rev2 settled them as staying (F8); the rule doc says 'it stays where it is'; ENG-2426, ENG-2434 and ENG-2424 are hazard tokens |
| FIX | ENG-2363 in progress though Leonard said it stopped | Fixed | Vincent's note: Android still hits this; ENG-2363 |
| FIX | deck lists Daily Gift, 'All' overclaims | Fixed | 'UI pass wrapped up', Daily Gift off the page; f_d15a8c70e3f2b94a61c8d3 |
| FIX | join rows with no earlier leave | Partly fixed | #builds and BoomBit rows dropped, since a paid seat covers them; the three channels /prompt named stay, with C050WGU41HR |
| FIX | mirror ids out of sequence | Fixed | base review ids 3482612642 and 3485366118; comment ids follow the base sequence |
| FIX | Marcus 'hasn't got to it' though Owen owned the fix | Fixed | 'still happens on today's build'; C05V5FNLB9V/1764262971.568809 |
| FIX | card activity with no action | Fixed | the card's last activity is its comment; 690b27282f4c1b7a6e93d512 |
| FIX | 0.3.310 is Android only | Fixed | 'the Android build players have'; f_3ca9e15d7b20f4e681ad52 |
| FIX | ENG-2405's checklist kept | Accepted | all four boxes are unticked and all four children open, so it agrees; ENG-2405 |
| FIX | ev_N numbers follow 'closed' | Accepted | suffixes must be the next free number, and the times are right |

/injection on rev3: FAIL on C1, Owen's join rows in CE156FDFB428 and C09Q4S613CN, with no leave in the base (run_forensics/rev3/0_injection_FAIL_r3.md). The coherence audit had flagged this as a FIX and I kept the rows because the /prompt report named those channels. rev4 removes them.

/prompt on rev4: every prompt dimension 5, Coherence 2. Owen's guest period needs a leave and a join in each task channel, which /injection on rev3 had also said; and the card date I removed on the audit's advice was the wrong call, so it is restored. rev5 applies both, adds the same pair in C09SWTHEMEW, and changes nothing else.

rev6 (2026-11-08): two rev5 baseline batches missed four corrections in every run, so the spread and pattern gates failed. rev6 repeats all four in Brian's DM with Owen on Dec 11 (Tavern, Apple tie, the two popups from Arthur's reviews), a place some runs read and others don't. Each new line agrees with the record it repeats; no new fork: Vincent's last activity is Dec 2 and the notes say he tied lines before he left; nothing later says either popup was swapped.

rev7 (2026-11-08): /prompt on rev6 (platform revision 10) re-opened the navigation bar tooltips thread in its deep recheck. Vincent's 1 pixel gap 'but that's okay' (Nov 21 18:03 UTC) is followed by Brian's 'I'll send another fix' (18:07 UTC), and no later record speaks to the gap, so the notes' 'unless a later record about that bug says otherwise' left Done and Bugs both fair. Earlier rounds and both blind sweeps kept the tick on 'that's okay' and did not weigh Brian's later reply. rev7 adds Vincent's reply in that thread on Nov 22 21:05 UTC, in his retest session, saying Brian's second fix closed the gap. Truth unchanged. Sweep lesson: on a ticked line, read the last reply in the thread, not the last tester verdict.

rev8 (2026-11-08): /hardness on rev7 scored 1; the pre-check run listed all of Brian's messages from Nov 1 to Dec 15 and read the three Dec 11 lines. rev8 removes the Apple line only. No new fork: Apple Covered by ENG-2073 rests on Vincent's email to Owen (Nov 20), the record /prompt accepted on its own on rev5; the popup line now follows the Tavern line and still opens with 'And'.

rev9 (2026-11-08): /hardness on rev8 scored 2, with one cause (Vincent's email). rev9 removes Brian's Tavern line, so Tavern rests on Marcus's DM as on rev5, which /prompt accepted. It also moves Brian's own Daily Gift note from ENG-2437 to his DM on Dec 11, keeping the words 'the panel never got its last pass'. Fork check: no base commit touches Daily Gift after Dec 4. Brian's Trello checklist leaves Daily Gift unticked and his tracker says 'last pass', which agrees. The notes doc's 'Brian and Oliver left notes on some of the open children' stays true through Oliver's ENG-2428 note and Brian's check notes. The popups line drops its opening 'And'.
