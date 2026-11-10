# Rule-text adversary: task_inputsS, revision 8 to 9

Read for this slice: the DM, thread reply and brief in `01_Universe_Inject.sql` (sha 0e8c8ad8...), `04_Prompt.txt`, Eval 1 §2.1, §2.6, §2.7, `deep_recheck.md`, `common_errors.md`, `prompt_qc_examples.md`, `solver/truth.json`, `solver/solver.py`, `01_Gradable_Surface.json`, the platform report lines 338-476, and the earlier platform and local rounds. Nothing was edited.

## Bottom line

1. **"an unverified build or platform is a still-to-do, not a hold" is dead weight and the worst fork source.** No value in truth.json depends on it. Its only consumer was the revision-1 Zombie Lane cell ("iOS verification (the Zombie Lane fix is verified on Android only; owner)"), and that row left in revision 2. It has produced six candidates so far, two of them confirmed by the platform.
2. **The still-to-do list is open for two reasons.** "an owner has flagged" attaches only to art, so "prod deploy" and "config" carry no test. And the in-list and out-list leave a middle, which is exactly the platform's words on #477: "neither analytics nor clearly polish".
3. **Three rewordings close it (E1, E2, E3 in Q2).** They name no ticket, PR, report, beat or person. Every truth.json value stays as it is, every trap and decoy still works, and E1 plus E2 kill the S23 and ZOM-534 forks by quote.
4. **Two things stay open after the rewording, and they need records, not rule text.** The first is the Sep 30 #zombie-bugs shader thread, which no round has raised and which already sits inside "player-facing art an owner has flagged" (Marcus: "fix the shader", Oliver: "will work on this asap"). The second is one hostile reading of #477.
5. **A latent grading fault:** the brief tells Plague Race "not its window dates", but S02 grades a value in Weeks running. E3 fixes the text. S04, S05 and C01 also need "In" added to their accepted outcomes, because the brief says "whether the beat is in".
6. **The Hold-until sentence is not a trap hint.** Keep it. Caveat: the platform's P4 pass read only the six prompt sentences, so the brief has never had a dedicated hint test. If one comes, "Not only the events everyone lists." is the sentence at risk. It is dead weight and should go.

## Q1. Each clause: what could fork it, what depends on it

"Generates" means the clause can pull a stray record into a cell. "Limiter" means it pushes records out. Ids are mine: M = Frederick's DM, Y = his thread reply, B = the brief. D1-D11 and T1-T15 are the design's decoys and traps. Rule names and slots come from solver.py and the surface file. The solver reads no brief words: `_body()` is called only for `TRELLO_QUESTS` and `NOTE_VIALS`, and `BRIEF` is only a presence check. So "depends" below is a reasoned deletion test, not a tool result.

### DM

| Id | Clause | Record class that could fork it | Generates? | What depends on it | Verdict |
|---|---|---|---|---|---|
| M1 | "the live-ops and push calendar for the beta buy we start Mon Oct 6 through Sun Nov 2" | A record that moves the buy start (UA deck: "starting once the stores approve") | No | Span of every row | Needed |
| M2 | "Every beat players can see in those weeks" | Any live-ops feature or roadmap card | Yes, rows; bounded by B4, B6, Y3, Y5 | R_SCOPE_BEATS; V01, S04, S05 | Needed |
| M3 | "which windows it runs in" | A cadence for a beat the brief exempts from dates | Mild, collides with B11 | S01, S02 | Needed; see Q3 |
| M4 | "if anything is held and until when" | A held push row; a date near a fix | Mild; bounded by B12, B16 | S03; Hold until column (no solver field) | Needed |
| M5 | "the push that goes with it" | A beat with no row (Endless); a row with no beat (lapse, FTUE, lives) | Mild | Calendar Push column (no solver field) | Needed by the ask, ungraded |
| M6 | "what still has to land before it runs and who owns that" | Any open ticket, PR, bug or request | **Yes, the widest sentence: no kinds at all** | S07-S11, through the brief | Needed; safe only because M9 hands it to the brief |
| M7 | "Put it in the calendar sheet in your ZM Live Ops folder and link it on the calendar ticket" | Other calendar sheets, a new ticket | No | W04 | Needed |
| M8 | "send me your recommendation back here, with the trade-offs, on what we run and what we hold" | None | No | W01-W03 | Needed |
| M9 | "The working rules for the calendar are in my brief, shared with you." | None | Limiter of M6 | Every brief rule | Needed |
| M10 | "so I need your call, not a list of what we have" | None | No | Nothing | Harmless; supports a closed still-to-do |

### Reply

| Id | Clause | Record class | Generates? | What depends on it | Verdict |
|---|---|---|---|---|---|
| Y1 | "Two things the brief does not spell out." | None | No | Nothing | Harmless; implies the brief is otherwise complete |
| Y2 | "plan the PNs Beta tab as it stands, one line per row, local notifications included" | Other tabs, the Domino sheet | No | R_ASK_FOLLOWUP; V02 | Needed |
| Y3 | "Leave off the four rows for things that are not in the beta: ... just those four" | Another feature "not in the beta" | Bounded by "just those four" | V02 | Needed |
| Y4 | "Copy that does not name the game at all is fine to go out, the naming rule is only about wrong names." | None | No | P04, P05 | Needed |
| Y5 | "keep Zombie Lane off the calendar, it is a permanent track with no window or reset to plan" | Another permanent feature (Confluence: Endless is "a permanent ZM3D board mode") | Bounded by "no window or reset" | V01 | Needed |

### Brief

| Id | Clause | Record class | Generates? | What depends on it | Verdict |
|---|---|---|---|---|---|
| B1 | "The calendar covers Mon Oct 6 00:00 UTC to Sun Nov 2 23:59 UTC, the four buy weeks in my UA plan." | A window open before or past the span | Mild (Season Pass) | K8; span | Needed |
| B2 | "Every window is stated in server time (UTC) as a start-end instant." | A reset with no end | Mild | Windows column (no solver field) | Needed by the sheet, ungraded |
| B3 | "A PT/PDT rendering of the same instant is fine, a different instant is not." | None | No | S01 accepted outcomes | Needed |
| B4 | "Every ZM3D beat a player can see in those weeks: an event window, a reset or a start push." | Every push row, every reset | Yes, rows; bounded by Y3, Y5, B6 | R_SCOPE_BEATS; V01, S04, S05 | Needed |
| B5 | "Not only the events everyone lists." | None | No | Nothing: B4 already states the scope | **Dead weight and a hint risk (Q4)** |
| B6 | "Boss Arena is off this calendar until the pivot call." | None | Limiter | V01; T13; K14 | Needed |
| B7 | "A beat starts with the first window that opens after its server windows are live on prod, the backend release instant read in UTC, not when its client PRs merged." | A beat with no record of its server state | Bounded by Arthur #470 | R_DONE_DEPLOY; S01 | Needed |
| B8 | "Collect & Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC, so a window the release instant pre-empts does not count." | CDK cron also fires Thu 00:00 (`0 0 * * 3,4`) | Mild | S01 | Needed; Q3 |
| B9 | "A beat that is only waiting on that release starts late, it is not held." | Art still open on the same beat | Mild, on "only" | C05 | Needed; Q3 |
| B10 | "Season Pass seasons open on the 1st at 00:00 UTC." | None | No | R_LOCK_BOUNDARY; S10, W07 | Needed |
| B11 | "For the quest rollover, the daily gift (the Login Calendar row on the push sheet) and Plague Race put down whether the beat is in and whether its push is ready, not its window dates." | Cron schedules; rows that are Ready but WIP | Mild | S04, S05 mapping; **collides with S02** | Needed; reword (E3) |
| B12 | "Hold a beat only when players provably cannot enter, score or claim on prod even after a restart." | Any prod bug | Bounded by "provably" and "even after a restart" | R_TECH_HOLD, R_HOLD_SCOPE, R_INFRA_SCOPE; S03, C01, C02, C04 | Needed |
| B13a | "An established failure holds it" | None | No | Restates B12 | Keep; K13 can re-anchor here |
| B13b | "an unverified build or platform is a still-to-do, not a hold" | Any report, test request, branch, device, submission status | **Yes, the worst** | **Nothing since revision 2** | **Dead weight; remove** |
| B14a | "Wrong counters, a reset that needs a restart, cosmetic, VFX and performance gaps and analytics gaps do not hold a beat" | None | Limiter | S04, S05, C02, C04; D7, D8; the contrast in T7 | Needed |
| B14b | "and neither does a change request outside the Aug-Sep live-ops cohort" | #303 (Jul 16, CodeRabbit), backend #4 (June) | Limiter | No truth value | Keep with B15 |
| B15 | "An unresolved change-request review blocker on an in-scope live-ops PR from that cohort does hold it." | A review note read as a change request (#438 in round 2, #477) | Mild; bounded by review state | **No truth value:** the base has no CHANGES_REQUESTED on match3d or match3d-backend in Aug-Sep. Cohort surface 2 (39 calls) stands on it | Truth-dead, horizon-needed. Keep |
| B16 | "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date." | A date near a fix (Oct 8) | Limiter | Hold until column; platform F7; no solver field | Needed (Q4) |
| B17 | "One-offs may overlap recurring beat slots." | None | No | Nothing once Halloween is off | Harmless |
| B18 | "A one-off may take a recurring beat slot only with the latest dated approval from Product, and if he takes that back his later word is the one that counts." | None | No | R_WITHDRAWN; S02, W03 | Needed |
| B19 | "For each beat, what still has to land before it runs for bought users (prod deploy, config, player-facing art an owner has flagged) and who owns it." | Open ticket, open PR, a fix on main, any undeployed change | **Yes: "prod deploy" and "config" carry no flag** | R_REVIEW_FLAGS, R_ICON_SCOPE, R_DONE_DEPLOY, R_HANDOFF_SLIP; S08-S11 | Needed; close (E2) |
| B20 | "Not what already shipped, not analytics, not polish nobody flagged." | An item that is none of the three (a title change, a test request) | **Yes: leaves a middle** | R_DONE_ELSEWHERE, S07; "nobody flagged" protects S11 | Needed; close, but keep "nobody flagged" |
| B21 | "A push goes out only if its row is Ready and LIVE and its English copy names the game only as Zombie Match 3D and events only by their ZM3D names." | None | No | R_COPY_CURRENT, R_WIRED; P01-P03, P07 | Needed |
| B22 | "Anything else is held, with what is missing." | None | No | P06; the Held rows | Needed |
| B23 | "Beta pushes are English-only (UK and US buys); the translated tab is the old Domino set still waiting on ZM3D localization." | Translated tab | Limiter | D4 | Needed |
| B24 | "Every config a beat needs lands before its lock, read in server time (UTC)." | Any config for any beat; Brian's "the daily and weekly quest tables" | Mild | R_LOCK_BOUNDARY; S10, W07; K9 | Needed |
| B25 | "A committed date that misses the lock moves earlier and its owner is told in a reply on the mail where they committed to it." | The earlier mail | No | R_HANDOFF_SLIP; W06, W07 | Needed |

### The generators, by evidence

| Clause | Candidates it has produced | Needed? |
|---|---|---|
| B13b | Daily-gift frame (platform round 1, confirmed); store approval (round 2, rejected); ZOM-544 (local rev 5, cured by rewording the SQL note); premium buy test (local rev 7 and 8, rejected as "the weakest of the three"); card VFX (round 3 alternative D, excluded); S23 freeze (round 3, confirmed) | No |
| B19 | ZOM-534 (round 3, confirmed; local rev 8 F2); ZOM-563 (local rev 7 and 8); quest set (local rev 5) | Yes |
| B20 | #477 title (round 3, confirmed; local rev 7 and 8); ZOM-526 token travel (round 2) | Yes |
| B24 | Quest tables in Brian's mail (not yet raised) | Yes |

### Proof that B13b is dead weight

- Every still-to-do in truth.json already fits B19 by itself: the vials and the icon are flagged art, the server windows are a prod deploy, the November config is a config, the strip is art or config. The Leagues fix comes from an established failure, the opposite of unverified.
- `run_forensics/rev1/truth.json` shows the one cell this clause ever fed: Zombie Lane, "iOS verification (the Zombie Lane fix is verified on Android only; owner)". Y5 took Zombie Lane off in revision 2, and decoy D9 in the trap register already says so.
- Dossier row 12 credits the clause with D7 and D8, but both are decided by B14a ("cosmetic", "performance"). Design row 10 ("a submission-build fault would be a still-to-do") is a contrast nothing tests: Vincent's re-test is on "the current prod build".
- Its only machine dependency is K13's `delegation_quote`, which `hardness_gate` checks as an exact substring. Re-anchoring K13 costs one line.
- The revision 8 local ruling that the clause "sorts failure reports" did not hold. The platform read it as a free-standing still-to-do rule (P1-DR5).

## Q2. The smallest rewordings that close the set

### The three edits

**E1, Held or not.**
Old: "An established failure holds it; an unverified build or platform is a still-to-do, not a hold."
New: "An established failure holds it; an unverified one does not."

**E2, Still to do.**
Old: "For each beat, what still has to land before it runs for bought users (prod deploy, config, player-facing art an owner has flagged) and who owns it. Not what already shipped, not analytics, not polish nobody flagged."
New: "For each beat, what still has to land before it runs for bought users and who owns it: a held beat's fix, and what an owner has flagged for that beat as not done (prod deploy, config or player-facing art). Nothing else goes in: not what already shipped, not analytics, not polish nobody flagged."

**E3, When a beat starts, last sentence.**
Old: "...put down whether the beat is in and whether its push is ready, not its window dates."
New: "...put down whether the beat is in, which weeks it runs and whether its push goes out, not its window dates."

### Why each word is there

- **The flag now comes before the kinds.** Written as "any prod deploy, config or art an owner has flagged", a hostile reader can attach the flag to art alone, which is today's hole. In E2 the flag is the head and the parenthesis only filters it.
- **"Nothing else goes in"** is the quote a reviewer needs. It turns SILENCE into a definite "out". A missing flag stops being a gap in the evidence and becomes the answer.
- **"for that beat"** drops any record that names no beat. All five graded records name theirs in words (table below).
- **"as not done", not "as having to land first".** Arthur says the vials "are missing"; he does not say they gate the beat. A stricter flag would put S08 and S11 at risk, so the bar stays low and "what still has to land" stays the outer test.
- **"a held beat's fix"** sits outside the flag on purpose. Douglas's only note on ZOM-429 says "not blocking", so a flag test alone would empty the Leagues cell and create a new fork. The platform's Reading A lists this fix.
- **"polish nobody flagged" stays.** ZOM-521 calls the VFX work "polish", so a flat "not polish" would knock out the Collect & Win icon (S11).
- **"shipped" stays undefined on purpose.** Do not define it as "on prod". The daily-gift frame is only in the submission builds, so that definition would flip S07.

### Proof 1: every graded item still qualifies

| truth.json cell | Slot | E2 limb | Record words (beat named) |
|---|---|---|---|
| C&W final vial models (Claire) | S08 | art, flagged by Arthur (Co-founder, CTO) | #468#rc_38 "The Collect & Win vials... The final vial models are missing" |
| C&W event icon animation (Marcus) | S11 | art, flagged by its owner | cmt_zom465_2 "The Collect & Win event icon animation is still to do on my side" |
| C&W server windows reach prod | none directly | prod deploy, flagged by Arthur | #470#rc_10 "Server-side windows for Collect & Win are still on the DEV stack only" |
| Season Pass premium strip (Oliver) | S09 | art or config, flagged by Arthur | #472#rc_1 "the Season Pass premium strip is still set to the October range" |
| Season Pass November config | S10 | config, flagged by Brian | Sep 26 mail "the November Season Pass config handoff moves"; B24 |
| Leagues weekly reset fix | none | a held beat's fix | Vincent's re-test; ZOM-429 (assignee Douglas) |
| Daily Login empty | S07 | "not what already shipped" | cmt_zom432_2 "so nothing is left here. Closing." |
| Quests, Plague Race, Endless empty | not slotted | no flag of a listed kind | see Proof 2 |

The strip stays both-fair (F17): E2 keeps both "config" and "art", so the Oct 31 or Nov 1 deadline is untouched.

### Proof 2: what happens to the strays

| Candidate | Today | After E1 + E2 | Killing words |
|---|---|---|---|
| ZOM-534 fix to prod | SCOPE_GAP fork | Out | No owner flagged it as not done. The only owner note says "nothing else has to land for the beta". The main-vs-prod gap no longer matters, because the rule asks for a flag, not for proof of absence |
| S23 freeze | SILENCE fork | Out | E1 "an unverified one does not"; a check is none of the kinds; no owner flagged it |
| #477 title change | SILENCE fork | Out, one hostile reading left | No note flags it. See "What this does not close" |
| Card VFX ZOM-528, ZOM-541 | Excluded | Out | "not what already shipped"; no beat |
| Premium buy test (#zombie-ops, Sep 12) | Rejected locally | Out | A test is none of the kinds |
| ZOM-544 restore | Reworded around | Out | No beat, none of the kinds |
| ZOM-563 prod teams | Rejected locally | Out | No beat named |
| Store approval | Settled | Out | Not flagged for a beat |
| Oct 13 quest set | Settled | Out | Trello "The rollover does not wait on them" |
| ZOM-526 token travel | Settled | Out | "it does not have to land before the beta" |
| ZOM-565, ZOM-542, ZOM-471 | Settled | Out | Each note says it is not needed |
| A held push's fix as a beat to-do | Latent | Out | None of the kinds; it stays on the Pushes tab |

### Proof 3: every trap and decoy still works

| Node | Rests on | Effect of E1, E2, E3 |
|---|---|---|
| T1, D1 | B7, B8, B9 | Untouched |
| T2 | B18 | Untouched; E3 makes S02's column an explicit ask without naming the one-off |
| T3, D2, D3, D6, T13 | B4, B6 | Untouched |
| T4, T5, D4, D5 | B21, B23 | Untouched. T5's bait is the sheet's Status column, not the word "ready" in B11. `trap_liveness` rule placement run on the edited text: no sentence reaches the need for T4 (9) or T5 (12) |
| T6 | M7, cmt_zom78_1 | Untouched |
| T7 | B12, B14a | Untouched; the restart contrast is intact |
| T8, T9 | B10, B24, B25 | Untouched; "config" stays in the list |
| T10 | B20 | Calvin's Sep 24 note now fits the flag limb exactly, and "not what already shipped" still beats it. The trap is a little sharper |
| T11, T14 | "flagged", "art", "polish nobody flagged" | Intact. The flags still sit in inline notes and per-issue comments, so the reads are still needed |
| T12 | Trello note | Out as before |
| T15 | Y2-Y5 | Untouched |
| D7, D8, D10, D11 | B12, B14a | Status unchanged (Runs). D7 has a still-to-do residual below |
| M9 | Y5 | Off the calendar; E1 also removes the last path to an iOS to-do |

The solver's over-application operators and all of truth.json are unchanged, because nothing reads these words. The cohort surfaces stand: a flag can sit on any of the 18 tickets or 39 PRs, so the rule gives no shortcut. Hardness barely moves. Extra to-dos were never graded except on S07, so closing the rule costs almost no difficulty.

### Wording that risks reading as a trap hint

| Wording | Risk | Why |
|---|---|---|
| "An open ticket, open PR or lone bug report is not a still-to-do on its own." | High | The three classes map one to one onto the three forks, and "on its own" tells the reader a stray exists. This is the "point at the items" edit the platform warned against |
| "A report nobody has re-tested on prod does not count." | High | It repeats the deciding record of T7: "Re-tested the weekly leaderboard on the current prod build" |
| "A fix on main counts as landed." | High | It quotes ZOM-534, and it contradicts B7, since C&W's client PRs are on main too |
| "Title or text changes do not count." | High | It points at #477 |
| "One device is not enough." | High | It points at S23 and echoes Vincent's "Same on the second device" |
| "If nobody flagged it, leave it off even if the ticket is still open." | Medium | "even if" steers at open tickets and has if-chain shape (§2.7) |
| "Only what someone has said must land." | Medium | No kinds, and "someone" lets in Oliver's "We need to test" |
| E2 | Low | Names no record class; "flagged" is already in the text; "Nothing else goes in" is an ordinary closing line |
| E1 | Low | Uses only words already in the sentence |
| E1 fallback: stop at "An established failure holds it." | Lowest | Pure deletion. B12's "provably" still decides the hold |

Safest set: E1 as written (or its fallback), E2, E3.

### What this does not close

1. **The shader thread, `C08R27X0EAH/1759249488.495439`, Sep 30. No round has raised it.** Vincent: "i think we should squeeze in the fix for that issue if it's an easy fix". Marcus: "solution would be to fix the shader... or just get rid of it". Oliver: "will work on this asap". It is player-facing art with an owner's flag, in a channel Julia reads, on the last day before the clock. The design labels it Season Pass (D7), but the text says only "the box" and the image is not readable. "for that beat" keeps it out only while no record ties it to a beat, and I could not rule that out. No follow-up shows in Slack through Sep. It needs one settling record, or a check that nothing Julia can reach ties it to a beat.
2. **#477, hostile reading.** A reviewer could say Owen's open PR is itself an owner's flag and the change is a prod deploy. Weak, but this platform has failed the task on weak readings. Its own fix text asks for a record on #477 or ZOM-566. Keep that record, and do not rest it on the PR's state (SC-18).
3. **Brian's Sep 22 mail** lists "the daily and weekly quest tables" inside the November config. With B24 ("Every config a beat needs"), a reader can give Quests a to-do. The subject says Season Pass, which mostly settles it. Writing "the season's quest tables" in the three mailbox copies removes it.
4. **ZOM-534 by rule alone.** It is closed by quote, but the reviewer's habit is to ask for a non-owner record. A record is still cheap insurance, and it must agree with E2.

### If adopted, these must change too

- **SQL:** `body_text` and `style_runs_json` of `f_7c3e91a4d2b85f60e1a9c4`. New HEADING_2 offsets with E1-E3: Held or not 1251-1262, One-offs 1818-1826, Still to do 2026-2037, Push copy 2334-2343, Config locks 2660-2672 (Span, Scope and When a beat starts unchanged). With E4-E6 as well: When a beat starts 575-593, Held or not 1233-1244, One-offs 1800-1808, Still to do 2008-2019, Push copy 2316-2325, Config locks 2642-2654.
- **Manifest (final and draft):** K13 `delegation_quote` breaks in simulation; the other five brief quotes pass. Use "An established failure holds it". Update the prose of requirements R3 and R5. Requirement R3 also says "on the submission builds" where the brief says "on prod".
- **Surface:** add "In" to S04, S05 and C01 accepted outcomes.
- **Prose and solver:** dossier row 12 and the K13 rows; a revision 9 note in solver.py. truth.json should stay byte for byte.

## Q3. Other ambiguous sentences, by sheet column

### Calendar tab

| Column | Sentence | The two readings | Graded? | What closes it |
|---|---|---|---|---|
| First window | B7 | Season Pass: Oct 1, clipped Oct 6, or Nov 1 (the first to open inside the span) | No; F16 both-fair covers only the first two | No text change; the rubric stays off it or accepts all three |
| First window | none | A held beat: blank, or its Monday reset | No | No text change; the platform's Reading A keeps "Monday 00:00 UTC resets" |
| First window | B8 "pre-empts" | Literally "acts before", so the word reads backwards; a reader may land on Thu Oct 9, since cron fires then | **S01** | B7 "opens after" already decides it (F6). Optional E6: "so a window already open at the release instant does not count." |
| Windows | B2, B8 | C&W end instants: Tue 23:59 or Wed 00:00, while B3 says "a different instant is not" fine | No | Optional: "each opening 00:00 UTC and closing 23:59 UTC". Otherwise the rubric stays off the end instants |
| Weeks running | B11 vs S02 (and M3) | Plague Race: "All four weeks", or blank because the brief says "not its window dates" and only "whether the beat is in" | **S02, weight 5** | **E3.** Without it, a run that follows the brief literally fails S02 |
| Weeks running | none | Leagues while held: none, or all four marked held | No | Rubric stays off |
| Status | B11 | "whether the beat is in": a run writes "In" for Quests, Daily Login, Plague Race; accepted outcomes lack it | **S04, S05, C01** | Add "In" to the surface |
| Status | B9 | C&W also waits on art, so "only waiting on that release" is false for the one beat it serves. Reading B: the exemption fails, players cannot enter on prod, so Held | **C05** | B14a mostly kills it (art cannot hold). Optional E4: "A beat whose server windows are waiting on that release starts late, it is not held." |
| Status | B12 vs B15 | "only when players..." then a second hold route | No: no PR triggers it | Leave |
| Hold until | B9, B16 | C&W: blank, or Oct 10 | No solver field | Closed by "it is not held" |
| Push | B11 "is ready" | Plague Race and Weekly Leaderboard rows are Status Ready but WIP, so "ready" and "held" both have a quote. The platform's Reading A says "pushes not ready" against the sheet's own word | No solver field | **E3 ("goes out")** |
| Push | M5 | Name of the push, or its state; Endless has no row | No | Leave; rubric accepts either |
| Still to do | B13b, B19, B20 | Q2 | **S07-S11** | E1, E2 |

### Pushes tab

The seeded headers are Beat, Push name, Send (UTC), Segment, English copy, Status, Notes. The surface grades Push, Send or hold, What is missing (owner), and those three names are not on the tab.

| Column | Reading problem | What closes it |
|---|---|---|
| Beat | Lapse, FTUE and lives rows have no beat | Leave; ungraded |
| Push name | The source has no name column, so a run names rows from Details or When. Wording only | Widen the surface key regex: it has no match for "Finish first tutorial" |
| Send (UTC) | Both Send rows are local notifications on a trigger, with no UTC instant. Held rows have no send. A run can leave it blank, write the trigger, or invent a time | Change the seeded header to "Send (UTC or trigger)". No hint risk |
| Segment | Source "Segmentation" or "UK and US" (B23) | Settled by Y2 "as it stands" |
| English copy | Keep held copy or fix it | Settled by Y2. The token stays as the source string |
| Status | Two source columns carry the word Status, so a run may copy Ready or WIP here and put the call in Notes | Change the seeded header to "Send or held" |
| Notes | "with what is missing" has no named column | Change the header to "What is missing". Drop "(owner)" from the surface: no rule asks for a push owner and PNs Beta holds none |

Do not make what-is-missing text exact. Row 12's copy says "login calendar" where the brief says "daily gift", so a run can fairly add a naming note there.

### Other sentences

| Sentence | Issue | Close |
|---|---|---|
| B14b, B15 "cohort", "in-scope" | Authoring words in Frederick's mouth; "Aug-Sep" by what date is undefined. The manifest's cohort runs Jul 1 - Sep 30 and lists #303 as a member, while the brief puts #303 outside | Optional: "A review still on changes requested on a live-ops PR from Aug or Sep does hold it." Surface 2 keeps its reads, and review notes stop counting |
| B24 "its lock" | Confluence also says "There is no technical content lock" | Settled by the spec's "locked 24h before each season opens" (F13) |
| B20 "shipped" | Merged, in a build, or on the stores | Leave undefined (see Q2) |
| B16 "runs until" | "runs" is also the Status word | Optional: "lasts until". Not needed |

## Q4. "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date."

**Verdict: not a trap hint. Keep it as written.**

- **It points at no trap.** §2.7 defines the fault as "wording that points at the trap without naming it". The trap around this beat is T7: whether the leaderboard is held at all. The sentence is silent on that and only applies once a hold exists. Hold until is not in the trap register and has no solver field.
- **It fails the calibration shape.** #31 fails because it asserts a hidden thing exists and steers toward it ("not on anybody's list"). This sentence is conditional, asserts nothing about the universe, and names no beat, ticket, symptom or person.
- **Rules belong in a seeded record.** §2.7: "A per-case rule belongs in a seeded record, not in the prompt." The platform's warning is about sentences that "point at the items". This one points at none.
- **It does fix a cell's wording,** which is the "answer-key clause" pattern from our own checklist. That is acceptable here because the cell is a boundary case, not a trap. The memory rule on column headers ("Hold until (UTC)") asks for exactly this.

**How strong the evidence is.** The platform report quotes the sentence as S_BRIEF_UNTIL and uses it to settle F7, and Contrived scored 5. My count of 25 brief rule sentences matches the platform's P1 count, so it was read. But P4, the hint pass, covered only the "6 prompt sentences". So there is no dedicated hint test of any brief sentence on record.

**If a reviewer ever extends that test to the brief,** these are at more risk than this one:

| Sentence | Why |
|---|---|
| B5 "Not only the events everyone lists." | It is the plain negation of T3's natural reading ("the beats are the events everyone lists") and sits close to #31's "not on anybody's list". **Delete it (E5): nothing depends on it** |
| B18 "his later word is the one that counts" | Robert's message says "my later word on this one is the one that counts". The echo is a little neat. Leave unless flagged |
| B8 "a window the release instant pre-empts does not count" | Close to stating T1's rule. Needed for S01; leave |

## Limits

- I did not run a data census. The stray list comes from the prior rounds, the SQL and spot reads, so a flagged item the census finds must be run through E2.
- `ugt-fork-v1` is not in the local `Evals/`. RECORD, SCOPE_GAP and SILENCE are taken from the brief and the platform report.
- I checked the edits in memory only: K13's substring break, the other five quotes, heading offsets, and T4/T5 rule placement. `hardness_gate`, `trap_liveness`, preflight and `/injection` were not run on an edited SQL.
- Whether E2 satisfies a platform reviewer is my judgment. A closed rule has not been tested on this task.
- The shader thread's images were not read. A `git log` search of the match3d repo for the fix returned nothing, so I draw no conclusion from git.
