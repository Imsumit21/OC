# Rule-text attack on revision 9 (P1 and P4 standard)

Inputs: `inputs/04_Prompt.txt` (sha 2a23afd8...) and `inputs/01_Universe_Inject.sql` (sha 892f7edd...). Both match the files in `Task_Authoring/task_inputsS/`. Nothing was executed from the SQL. Nothing outside this file and `work/` was written.

Labels. Kill means a quoted prompt sentence or Julia-reachable record rules out Reading B. Basis labels are from the brief: RECORD, SCOPE_GAP, SILENCE. B1 to B27 are the brief's sentences, numbered in section 7.

## 1. Result

One fork has no killing quote. It is new in revision 9 and it sits in the sentence the revision was built to close. Everything else has a kill, though four items are more exposed than they need to be.

| Rank | Item | Status | Fix |
|---|---|---|---|
| 1 | A1: "as not done since this brief" parses two ways | **No kill.** Changes Still to do contents | Move "since this brief" next to "flagged" |
| 2 | C1: "A window the release instant pre-empts does not count." | No UGT effect. The word runs backwards and the sentence is now an orphan that reads as a riddle | Delete it. B9 already decides the value |
| 3 | A2, A3: "that beat" and the colon | Killed, but revision 9 made Reading B stronger than it was in revision 8 | Same rewrite as A1 |
| 4 | A5: Oliver's new shader reply | Killed by "for that beat", but it repeats the shape the platform rejected on ZOM-534 | Have Vincent, not the owner, close it |
| 5 | D1: quest rollover "which weeks it runs" | Killed, by inference across three records. truth.json has no value for a cell the brief now requires | One clause in the Trello note, plus a truth value |

Clean after a real attempt: "An established failure" (the leaderboard still qualifies), "starts late", the cadence move, the Push copy supersession, and Robert's reworded withdrawal.

**One rewrite covers ranks 1 and 3, and it also protects rank 4:**

> For each beat, what still has to land before it runs for bought users and who owns it: its fix if it is held, and anything flagged since this brief as still needed for it (prod deploy, config or player-facing art). Nothing else goes in: not what already shipped, not analytics, not polish nobody flagged.

Fix-text check (deep_recheck step 5), run against every item:

| Item | Record wording | Under the rewrite |
|---|---|---|
| Vials | "The final vial models are missing" (Sep 29) | In |
| C&W icon | "still to do on my side" (Sep 30) | In |
| Premium strip | "It needs the November range" (Sep 30) | In |
| Server windows | "still on the DEV stack only" (Sep 30) | In |
| November config | "I just need the two extra days" (Sep 26) | In |
| Leaderboard fix | held limb, no date test | In |
| ZOM-565 | "not needed for the beta" | Out |
| ZOM-526 | "does not have to land before the beta" | Out |
| Trello quests note | "does not wait on them" | Out |
| lightSweep | "nothing waits on it" | Out |
| #477 title | "do not have to land before the beta" | Out |
| Desert and Port themes | nobody says needed | Out |
| Pre-brief flags | date test | Out |

No truth.json value moves. The earlier adversary warned against a stricter flag such as "as having to land first". "still needed" is a lower bar than that, and every graded record meets it in plain words.

If "still needed" is unwanted, the smaller edit is "...and anything flagged since this brief as not done for it (...)". That fixes A1 and A2 but leaves A3 as it is.

New HEADING_2 offsets:
- Rewrite only: Push copy 2316-2325, Config locks 2632-2644.
- Rewrite and C1 deletion: Held or not 1169-1180, One-offs 1736-1744, Still to do 1944-1955, Push copy 2261-2270, Config locks 2577-2589.

## 2. Diff against revision 8 (done by hand from the two SQL files)

Rule text:
- Span: "Collect & Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC." moved here from When a beat starts.
- Scope: "Not only the events everyone lists." removed.
- When a beat starts: "so a window the release instant pre-empts does not count" is now its own sentence. "A beat that is only waiting on that release" became "A beat whose server windows are waiting on that release". "whether the beat is in and whether its push is ready" became "whether the beat is in, which weeks it runs and whether its push goes out".
- Held: "an unverified build or platform is a still-to-do, not a hold" became "an unverified one does not".
- Still to do: rewritten as above.
- Push copy: "only" dropped twice.

Records: Robert's withdrawal reworded; Leonard's S23 reply; Oliver's lightSweep reply; Douglas's ZOM-534 note reworded; Leonard's ZOM-534 comment; Brian's ZOM-566 comment; Vincent's ZOM-563 close; Trello note; Brian's Sep 22 mail; Pushes tab headers. All match `apply_review_fix_rev9.py`.

The earlier adversary's text (`rev9/rule_adv/new_body.txt`) said "what an owner has flagged for that beat as not done". "since this brief" and the passive voice were added after that review, so it did not test them.

## 3. Forks on the Still to do sentence (B21, B22)

### A1. "flagged ... as not done since this brief": which word does "since" attach to? NO KILL

- **Reading A (intended):** flagged since the brief. Only flags dated after Sep 24 count.
- **Reading B (the adjacent parse):** flagged at any time as "not done since this brief", meaning it has stayed undone since Sep 24. Pre-brief flags come back.
- **Material difference, Still to do contents.** Reading B adds these, and Reading A's date test is the only thing that removes them:
  - Endless, art: ZOM-465, the one unstruck item: "Refill Timer ticking animation as well as color change from 5 to 1", with Marcus's open "do we still need to do that?". Owner Marcus. ZOM-565's "P1/P2 endless polish" note covers it only by inference.
  - Endless, config: #zombie-design Sep 13, Leonard: "first step is to cut coins back to half", then "Let's add this swap to your to do list on Trello". Nothing Julia can open shows it landing.
  - Plague Race, config: #zombie-design thread 1757478958.104989, Sep 10. Leonard: "Can we please cut it it in half by tomorrow?". Vincent: "I'm asking Douglas to change them as 60, 120, 250?". Leonard: "sounds good". It landed only in a DM Julia cannot see (census SO-11).
- **Kill:** none. Both parses are ordinary English, and the adjacent one is the easier parse. No record defines the phrase. Basis: SILENCE on the parse.
- **Also:** the parenthesis now follows "this brief", so it reads as a gloss on the brief. It is harmless, but it is the same misplacement.
- **Fix:** the rewrite in section 1.

### A2. "that beat": antecedent is "each beat" or "a held beat"? Killed, weakly

- **Reading A:** the flag limb applies to every beat.
- **Reading B:** the nearest noun is "a held beat", so only a held beat lists flagged items. Collect & Win and Season Pass cells go empty (S08 to S11).
- **Kill:** "For each beat," opens the sentence, and the DM asks for this on "Every beat players can see". B is strained but it is a real pronoun slip. The rewrite removes it.

### A3. Does the colon define "what still has to land"? Killed, but stronger than in revision 8

- **Reading A:** "what still has to land" stays the outer test, so a flagged item its flagger calls unnecessary stays out.
- **Reading B:** a colon defines. Whatever was flagged as not done since the brief is in, and "not polish nobody flagged" implies flagged polish is in.
- **Material difference:** Endless gains ZOM-565 (Calvin). Quest rollover gains more quests and reward balance. C&W gains the #477 title.
- **Kill:** the head "what still has to land before it runs for bought users" read with each record: "so it is not needed for the beta" (Marcus, ZOM-565), "so it does not have to land before the beta" (Brian, ZOM-526), "The rollover does not wait on them" (Trello), "so they do not have to land before the beta" (Brian, ZOM-566).
- **Why it matters:** the platform accepted these at F24 under the old wording, where the kinds sat in a parenthesis. "as not done" is now the test word and those items literally meet it. "still needed" turns each record into a direct negation of the rule word.

### A4. Who can flag? Anyone. No value moves

- **Reading A:** anyone. truth.json needs this, because Arthur flagged the vials, the strip and the server windows and owns none of them.
- **Reading B1:** only an owner. Nothing in the passive says so, and it would empty S08 and S09. Killed by the text.
- **Reading B2:** anyone includes review bots. CodeRabbit on match3d#471, Sep 29 22:04, on `Assets/Sprites/Daily Gift/img - DailyGift.png.meta`: "Restore the original sprite GUID to avoid broken references." The suggested revert was not applied: the HEAD meta still has guid aab786ac.... This would put an item in Daily gift, whose empty cell is S07.
- **Kill:** Samuel, ZOM-432, Sep 30 21:07, later than the bot: "so nothing is left here. Closing." Author is the PR's author, so a reviewer could call this an owner's claim. RECORD for a bot note, and the platform took this quote at F25.
- **Non-owner flags with no owner answer:** Robert, Sep 30, #zm-animations: "We also could use a better "enraged" effects on zombies, it's not obvious enough". Killed by "for that beat": no beat is named, and enrage is a core-level mechanic.

### A5. What is "not done"? One exposed item

A flagged thing can be unstarted, on a branch, merged, in a build, or on prod.

| Item | Stage | Outcome and quote |
|---|---|---|
| lightSweep box (Sep 30) | Pushed, "goes out with the next build" | See below |
| Daily gift frame | In submission builds, not yet on stores | Out: "so nothing is left here. Closing." |
| #477 title | Open PR | Out: "they do not have to land before the beta" |
| ZOM-534 day-boundary watch | Open, watching | Out: none of the three kinds. Leonard: "it is good on prod now" |
| ZOM-521 / 528 / 541 | "open until Brian has seen it in a build" | Out: no beat; "went in with #475" |
| ZOM-543 queue manager | "in progress" | Out: none of the kinds |

**lightSweep.** Vincent, Sep 30: "i think we should squeeze in the fix for that issue if it's an easy fix." New reply from Oliver: "Pushed the fix for the lightSweep on the box. It is only that sweep on the art, it goes out with the next build and nothing waits on it."
- **Reading A:** nothing listed.
- **Reading B:** flagged since the brief, player-facing art, explicitly not yet on prod, so a beat gets "lightSweep fix, next build (Oliver)". ZOM-565 calls "the icon item (the box)" part of the Endless start screen, which gives a reader a route to Endless.
- **Kill:** "for that beat". No message in the thread names a beat. The material came in with "the 2d reward box" (commit 41a5cf8c2c), so it is a shared box. Second kill: "nothing waits on it".
- **Exposure:** "nothing waits on it" is the owner's own claim about a gap he states himself, which is the ZOM-534 shape. The defence is that the need claim, not the fact, is what the owner is speaking to, as at F24.
- **Smallest fix:** let Vincent, who raised it, say in that thread that it can ride the next build. It must be dated after 2025-09-30T21:24:52Z and before the clock.

### A6. What does "since this brief" cut off? Killed

- **Reading A:** the brief's own date.
- **Reading B:** when Julia was pointed at it, the Sep 30 20:20 DM. That would drop every graded flag, because the last of them is Marcus at 18:05 the same day.
- **Kill:** the dateline "Frederick, Sep 24"; Drive created 17:15:22, modified 17:40:52.
- **Same-day edge:** four injected comments fall on Sep 24 (ZOM-556 15:20, ZOM-432 16:10, ZOM-526 17:30, ZOM-546 19:00). Each is overtaken by a later comment, names no gap, or is none of the kinds. No value depends on the boundary.

### A7. A flag raised before and repeated after? Counts by the text. No value moves

Nothing says "first flagged", so a repeat counts.

| Item | Before | After | Outcome |
|---|---|---|---|
| November config | Sep 22 mail | Sep 26 mail | In either way |
| Endless polish | Sep 12 list | Sep 25, Sep 29 | Out: "not needed for the beta" |
| More quests | Sep 12 | Sep 29 | Out: "does not wait on them" |

### A8. A ticket opened in the window? Counts if it says the thing is not done

Three tickets opened in the window.
- ZOM-564 (Sep 24 16:38, before the doc existed): no beat.
- ZOM-566 (Sep 30): analytics.
- ZOM-565 (Sep 25): the only live one. Marcus's "the glow behind its on all and the bar its the old bar" meets every limb. Out only through A3's kill.

Marcus's Sep 25 #zm-animations post is the same case ("I also need to add few text animations like for the combo"). ZOM-565's note names the screen and "the P1/P2 endless polish", so the gameplay VFX sits inside it only through "P1/P2". That is SCOPE_GAP-leaning, and the census accepted it at SO-45.

### A9. Is the parenthesis a filter or examples? Killed

- **Reading B:** examples, so a client fix or a test could go in.
- **Kill:** "Nothing else goes in".
- **Polish:** C&W's icon is animation, not obviously "art". "not polish nobody flagged" shows flagged polish counts as art, which keeps S11.

### A10. Is Brian's slip a "flag"? Killed

- **Reading B:** the Sep 26 mail is a commitment, not a flag, so "Nothing else goes in" drops the November config from the cell (S10), leaving only the reply to Brian.
- **Kill:** Sep 26: "the November Season Pass config handoff moves", "I just need the two extra days on the premium track." It is after the brief and says the config is not done.

### A11. Other post-brief art, new to the rule: Killed, SILENCE-leaning

Martin, #zombie-art, Sep 29: "I'm preparing a *desert theme* for the *Endless Mode*! What do you think?". Sep 30: "*Port theme* to have more variants to choose for Endless or Main gameplay mode".
- **Reading B:** Endless Still to do: desert theme (Martin). Art, a beat, not done, after the brief. Julia herself replied.
- **Kill:** it is a preview asking for opinions, so nothing is "flagged ... as not done", and #470 says Endless is "already running on prod", so nothing here "has to land before it runs". Under "still needed" it is dead.

## 4. Other forks, by the question asked

### "An established failure holds it; an unverified one does not."

Reading A: an established failure is one shown on prod after a restart. **The leaderboard still qualifies.**

| Candidate | Reading B | Kill |
|---|---|---|
| Weekly Leaderboard | Not established: ZOM-429's title says killing the app works; Douglas Sep 16 "they land in the new week fine, so not blocking"; Vincent Sep 22 "after a moment, I am now in the weekly leaderboard" | Vincent, Sep 30, newest and not the owner: "it still does not start a new week. I killed the app and reopened it twice ... Same on the second device." Ticket body gives the claim half: "or let me claim my rewards" |
| Leaderboard, one tester | Not established without a second person | No text asks for one. Revision 9 removed "platform", the only word that could have asked for more |
| FTUE exits, Sep 24-28 (Robert: "restarting the app doesn't seem to help") | Established prod failure after restart | Not a beat. Oliver: "I dont even think it is the FTUE anymore"; Robert Sep 30: bots |
| Endless freeze of Leonard's friend, Sep 24 18:32 | Post-brief Endless failure | "had to restart his app", so a restart cleared it; B14 needs "even after a restart" |
| S23 freeze | Hold or to-do | Leonard: "Could not get it to freeze"; dated before the brief; none of the kinds |
| Collect & Win before the release | Players cannot enter on prod | B11: "starts late, it is not held" |

### "A beat whose server windows are waiting on that release starts late"

- **Reading B1:** another beat qualifies. Quests and the daily gift are not in Arthur's list. Kill: no record has them waiting; Leonard's ZOM-534 note has quests on prod. SILENCE, but nothing supports B.
- **Reading B2:** the leaderboard fix rides Oct 8, so it starts late instead of held. Kill: Arthur: "leagues ... already running on prod"; GCal scopes the release to "server windows that are still on the DEV stack".
- **Reading B3:** C&W also waits on art, so the sentence fails. Revision 8's "only" allowed this; revision 9 removed it. Clean.

### Cadence moved to "Span and time base"

- **Reading B:** the prod cron is `0 0 * * 3,4`, so a window opens Thu Oct 9. Kill: B6 "Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC" plus Confluence "three staggered windows (Mon-Tue, Wed-Thu, Fri-Sun)".
- The move creates no fork, and it makes the solve two-section, which is its purpose.

### C1. "A window the release instant pre-empts does not count."

- **Literal sense:** to pre-empt is to come first, so this names windows the release comes before, which is every later window. Reading that way, Fri Oct 10 "does not count", and B9 contradicts it, so the literal reading is dead by B9 ("the first window that opens after").
- **Reading C, interrupts:** gives the Wed-Thu window and the same Oct 10.
- **Reading D, general:** without the old "so", it could apply to any beat with a window open at the release. Killed by the beat rule, and no such beat carries window dates.
- **So:** no value moves. But revision 8's "so" made it a consequence of the cadence, and alone it is a one-line puzzle with exactly one possible referent. The platform's F6 quotes it, but B9 settles F6 by itself.
- **Fix:** delete it. Fallback if it must stay: "A window already open at the release instant does not count."

### "which weeks it runs and whether its push goes out"

| Beat | Reading A | Reading B | Kill |
|---|---|---|---|
| D1 Quest rollover | All four weeks | From Oct 13, or week 2 only: the one dated rollover is Trello's "the Mon Oct 13 rollover" | Trello: "the current quests keep running either way". Leonard, ZOM-534: "the 00:00 UTC reset". match3d-quests `getWeeklyTimer`: Monday 6 days left, Sunday 0, so a Monday boundary. Each is indirect and none says "every week" |
| Daily gift | All four weeks | None supported | Row 12 "Daily/Monthly Rollover" |
| Plague Race | All four weeks | Three of four because of the one-off | Robert's withdrawal; CDK "PROD: every day at 00:00 AM UTC"; #470 "already running on prod" |
| Push, Plague Race | Held | Ready, so it goes (revision 8's "ready") | Revision 9's "goes out" plus B23: row is WIP |

D1 is new. The brief now requires a cell that truth.json leaves blank for Quests and Daily Login. Smallest fix: in the Trello note, change the tail to say the current quests keep rolling over every Monday either way, and set "All four weeks" in truth for both beats. The Monday boundary is verified against the code above.

### Push copy without "only", against the reply

**Clean supersession.**
- **Reading A:** rows 3 and 5 go out.
- **Reading B:** the prompt says the rules "are in the brief", B23 now requires copy that "names the game as Zombie Match 3D", so both are held and no row goes out.
- **Kill:** reply, Sep 30, same author, same subject, six days newer: "Copy that does not name the game at all is fine to go out, the naming rule is only about wrong names." §2.1 check 1 covers exactly this: "A later update can resolve an earlier conflicting statement without explicitly announcing replacement."
- **Residual:** revision 8 had no conflict; revision 9 made one on purpose, and "Two things the brief does not spell out" now slightly undersells a correction. It does not change the answer. The prompt's "his message" reaches the reply only as a reply under that message; the platform has already treated it as incorporated.

Two more readings:
- **Reply frees rows 1, 9, 14 (no game name):** killed by the same sentence, "the naming rule is only about", and by "only if its row is Ready and LIVE".
- **Rows 4 and 6 go, because the client already says Zombie Match 3D** (`NotificationManager.cs` lines 146, 158): killed by "plan the PNs Beta tab as it stands" and "its row ... its English copy". Not new in revision 9. If a reviewer opens the code, that quote is the answer.

### Robert: "the themed prop set I okayed in Martin's thread"

**Ties to the Halloween one-off and only to it. The one-off is not left in doubt.**
- The phrase matches his Sep 18 reply in Martin's Halloween thread word for word: "one themed prop set only".
- Julia-visible sweep from Jun 1 on `prop set`, `themed`, `props`, `one-off`, `halloween`, `okayed`: 26 base hits, no other prop set, and Robert okays no theme.
- All Robert replies with an ok-word in Martin-rooted threads: 5 hits, about the endless icon (Aug 7), a Sep 9 yes and rapid fire (Sep 18). None concerns a theme or set.
- Desert (Sep 29): three thread replies, none from Robert. Port (Sep 30, under six hours before the withdrawal): no thread. "a theme we may not ship at all" could evoke these, but "I okayed" cannot.
- Arthur's Sep 19 "Halloween: Pumpkin Lantern, Witch Hat..." list is not Martin's and has no Robert ok. Robert's Sep 26 "class room set" is not in Martin's thread.

| Reading B | Kill |
|---|---|
| Only the props are pulled, the one-off stays | Approval: "one themed prop set only", so the set is the one-off. "Take it off the beta calendar" |
| Martin's "app icon" half survives | An icon is not a beat |
| B19 "One-offs may overlap" lets it run without approval | "Take it off the beta calendar" |

D05GU6L0XFH lists Julia and Robert as members. Spec: "Owner: Robert (Product)".

## 5. Edge values

| Value | Computation | Result |
|---|---|---|
| Release | Oct 8 18:00-19:00 Istanbul (UTC+3) = 15:00-16:00 UTC = 08:00-09:00 PDT. Start or end gives the same answer | Wed Oct 8 |
| C&W windows in span | 12 in all. Mon Oct 6 and Wed Oct 8 open before the release; 10 open after | First window Fri Oct 10 00:00 UTC (Thu Oct 9 17:00 PDT) |
| Rejected C&W starts | Oct 8 00:00 opens 15 hours early. Oct 8 15:00 is mid-window, not an opening. Thu Oct 9 is not an opening under B6 | Only Fri Oct 10 survives |
| C&W last window | Fri Oct 31 to Sun Nov 2 23:59, inside the span | Not clipped |
| Hold | Leaderboard only. No dated fix: ZOM-429 has no due date and the release is scoped to the DEV-stack windows | "until the fix is confirmed on prod"; Mondays Oct 6, 13, 20, 27 in span |
| Lock | Nov 1 00:00 UTC less 24 h = Fri Oct 31 00:00 UTC = Thu Oct 30 17:00 PDT | Brian's 07:00 UTC is 7 h late; Oct 29 clears it |
| Plague Race | Daily cron; withdrawal removes the only displacement | All four weeks |
| Quest rollover, daily gift | See D1 | All four weeks |

Push calls, platform numbering:

| Row | Status / LIVE column | Copy | Brief alone | With reply |
|---|---|---|---|---|
| 1 Quests | Not Ready / LIVE | no game name | Held | Held |
| 3 Lives | Ready / LIVE | no game name | Held | **Go** |
| 4 1-day | Ready / LIVE | "Puzzles vs Zombies" | Held | Held |
| 5 7-day | Ready / LIVE | no game name | Held | **Go** |
| 6 FTUE | Ready / LIVE | "Puzzles vs Zombies" | Held | Held |
| 7 Win & Collect | Not Ready / WIP | wrong event name | Held | Held |
| 9 Plague Race | Ready / WIP | fine | Held | Held |
| 12 Login | Not Ready / WIP | "login calendar" | Held | Held |
| 13 Season Pass | Not Ready / WIP | fine | Held | Held |
| 14 Leaderboard | Ready / WIP | fine | Held | Held |

Rows 2, 8, 10, 11 are left off. Ten lines, two go.

## 6. Sheet columns

| Column | Fork | Material? | Kill or action |
|---|---|---|---|
| First window | Season Pass: Oct 1, clipped Oct 6, or Nov 1 | Date only, not graded | F16 covers the first two. Rubric stays off or accepts all three |
| First window | Held leaderboard: blank or Mon Oct 6 | Not graded | Rubric stays off |
| Windows | C&W end: Tue 23:59 or Wed 00:00, while B5 says "a different instant is not" fine | Not graded | The span's own "23:59" sets the style. Rubric stays off end instants |
| Weeks running | Only three beats are told to fill it. Held leaderboard: none or all four marked held | Not graded | Rubric stays off the other four |
| Weeks running | Quest rollover | Required, no truth value | D1 |
| Status | "In" against Runs; "Starts late" against Runs | Wording, but the surface would fail it | See section 8 |
| Hold until | C&W blank or Oct 10 | Closed | "it is not held" |
| Push | Name of the push or its state; Endless has no row | Wording | Rubric accepts either |
| Still to do | A1, A2, A3 | Yes | Rewrite |
| Still to do | Fix owner: Douglas or Oliver (Sep 19 and 22 client revert, census U7) | Owner field | Prompt "the owner picks it up" with ZOM-429 assignee Douglas |
| Pushes: Send | Trigger or time | Closed | Header "Send (UTC or trigger)" |
| Pushes: Send or hold | Copying the sheet's Status | Closed | New header |
| Pushes: What is missing | Row 12 may add a name note | Wording | Do not make the text exact |

## 7. Trap hints and naturalness, every brief sentence

Plain test: would Frederick write this to a colleague if he did not know the answer key, and does it point at one trap without naming it? §2.7 and P4 apply to the prompt, and the platform's P4 read only the six prompt sentences, so this is exposure, not a scored fail. §2.7 also says a per-case rule belongs in a seeded record. The six prompt sentences are unchanged and clean.

| # | Sentence | Plain test | Verdict |
|---|---|---|---|
| B1 | How I want the beta calendar built... | Normal opener | OK |
| B2 | The rules stay here; the calls are yours. | Normal | OK |
| B3 | The calendar covers Mon Oct 6... | Normal | OK |
| B4 | Every window is stated in server time... | Normal ops rule | OK |
| B5 | A PT/PDT rendering... | A little precise, fits a US/Istanbul team | OK |
| B6 | Collect & Win runs Mon-Tue... | Fact, but the only beat-specific line in a time-base section | OK |
| B7 | Every ZM3D beat a player can see... | Normal | OK |
| B8 | Boss Arena is off this calendar... | Normal | OK |
| B9 | A beat starts with the first window... not when its client PRs merged. | Names the wrong answer, but as a rule. Passed the platform | WATCH |
| B10 | A window the release instant pre-empts... | **Fails.** Nobody says this; only one window fits it; the word is misused | CHANGE: delete |
| B11 | A beat whose server windows are waiting... | Normal | OK |
| B12 | Season Pass seasons open on the 1st... | Normal | OK |
| B13 | For the quest rollover, the daily gift... | A bit list-like, but a real instruction | OK |
| B14 | Hold a beat only when players provably... | "provably" is firm but natural | OK |
| B15 | An established failure holds it; an unverified one does not. | Passes, slightly redundant with B14. Could be cut: B14 decides alone | OK |
| B16 | Wrong counters, a reset that needs a restart... | Mirrors ZOM-429 and ZOM-556 closely | WATCH |
| B17 | An unresolved change-request review blocker on an in-scope live-ops PR from that cohort... | **Authoring voice:** "in-scope", "cohort", "review blocker". Moves no value | WATCH: most spec-like line left |
| B18 | A hold with no dated fix runs until... | Natural | OK |
| B19 | One-offs may overlap... | Natural | OK |
| B20 | ...and if he takes that back his later word is the one that counts. | Anticipates the withdrawal six days ahead. Survived the platform | WATCH |
| B21 | For each beat, what still has to land... since this brief... | "since this brief" is a patch: what still has to land is a state, not a date. A person writes "since I wrote this". Points at no item | CHANGE: rewrite (A1) |
| B22 | Nothing else goes in... | Natural closing line | OK |
| B23 | A push goes out only if... | Natural | OK |
| B24 | Anything else is held, with what is missing. | Natural | OK |
| B25 | Beta pushes are English-only... | Natural | OK |
| B26 | Every config a beat needs lands before its lock, read in server time (UTC). | "read in server time" leans at the Istanbul gap, mildly | WATCH |
| B27 | A committed date that misses the lock moves earlier... | Conditional, asserts nothing | OK |

DM and reply: all natural. "just those four" and "Two things the brief does not spell out" read like a person.

Records, not rule text:
- Robert's "my later word on this one is the one that counts" repeats B20 nearly word for word. It is the clearest authoring fingerprint left. Ending at "Sorry for the flip." loses nothing.
- "the themed prop set I okayed" is stiffer than "the Halloween thing", but it is believable because it echoes his own note.

## 8. Downstream, outside the rule text

- `01_Hardness_Manifest.json` and the draft: all 10 `delegation_quote` strings still match the revision 9 SQL, and none depends on the proposed rewrite or the C1 deletion. The prose still carries old brief text: "an unverified build or platform" (2), "an owner has flagged", "only waiting on", "names the game only". I did not run `hardness_gate`.
- `01_Gradable_Surface.json`: S04, S05 and C01 still lack "In", and C05 lacks "Starts late", though B11 and B13 invite both. The pushes deliverable still expects "Push" and "What is missing (owner)", while the tab now says "Push name" and "What is missing". The change script's "headers match" holds for the sheet only.
- `truth.json`: no Weeks running value for Quests or Daily Login (D1).
- Dossier, solver and surface prose still say "only waiting on" or "whether its push is ready".
- Brief style runs in the SQL are correct for revision 9; I recomputed all nine.

## 9. Scanned and not scanned

**Read message by message, Julia-visible, Sep 24 00:00 UTC to the clock:** 796 of the 1,130 messages in her conversations, membership by `channels.json`: #zombie-bugs 156, #zombie-match3d 64, #zombie-design 157, #zm-animations 63, #zombie-art 31, the Robert DM 278, and the other DMs and mpdms. Each message was shown up to its first 220 to 330 characters; the ones cited here were read whole.

**Keyword only:** #builds in the window, 309 rows. Julia-visible Slack from Jun 1 for theme, prop, one-off and quest-cadence terms. #random and #playablex in the window (25 rows) were not read.

**Complete listings in the window:** Linear issues created or completed (the base has no Linear comments, so all comments come from the SQL); Trello actions; Confluence pages, versions and comments; Drive family modified; match3d PRs, human reviews and inline comments, bots included. CodeRabbit bodies read only as first lines, except #471.

**Read in full:** Confluence calendar and Season Pass spec, PNs Beta rows, ZOM-429, 465, 534, 543, 546, 559, 565, 566. CDK schedules, `getQuestRemainingTime.ts` in part, `NotificationManager.cs` lines 146 and 158.

**Taken from the census, not redone:** Gmail and GCal in the window, Slack before Sep 24 apart from the sweeps, sections on other beats (SO, TMD, GH, CF, L ids).

**Not scanned:** Snowflake; Slack images (no content, so Vincent's box image is unread and the box's beat rests on text and the commit); prefab bodies, truncated in SynthCut; channels Julia is not in.

**Not run:** `hardness_gate`, lint, preflight. Whether a reviewer raises A1 is my judgment; that no quote kills it is not.
