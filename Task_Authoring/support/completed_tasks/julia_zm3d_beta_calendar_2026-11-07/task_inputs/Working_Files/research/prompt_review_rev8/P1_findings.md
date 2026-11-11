# P1 findings on the revised SQL: Unique Ground Truth and Clarity

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Persona: Julia Lawson.

**Inputs.** SQL sha256 0e8c8ad83f3be435db1f9268f114c916f52293993eb687a55b34005015f9f815, confirmed on disk. Prompt, assignment and date files are byte-identical to the last round. "SQL Lnn" is a line of the revised `01_Universe_Inject.sql`; lines after L143 moved, so numbers differ from my last report. Mail citations use Julia's mailbox copy. SQL was read, not run.

**Checked:** 49 sentences: prompt 6, Frederick's DM 6, his thread reply 5, the brief 27 (one added), the UA deck 5 (plus its 4 week lines). I diffed the SQL line by line and read every changed statement in full.

**Result**
- The two fail-level forks are settled. DR1 and DR2 each close on a quoted, persona-visible record.
- DR3 and DR4 stay open as BOTH_FAIR_FIGURE candidates. The rubric must accept the values listed.
- DR5, DR6 and DR7 stay open. No changed statement touches them. They are weak and additive, but none has a clean rejection quote yet (see "What the main session needs to decide").
- The revision opens no new fork and leaves no new still-to-do unsettled.
- Clarity: **no finding.**

## Status of DR1 to DR7

| DR | Topic | Status | Deciding record |
|---|---|---|---|
| DR1 | Weekly leaderboard hold end | **Settled** (Reading A) | SQL L103 |
| DR2 | Quest rollover Still to do | **Settled** (Reading A) | SQL L180, SQL L235 |
| DR3 | Brian's new handoff date | **Still open**, unchanged; BOTH_FAIR_FIGURE candidate | No record names the date |
| DR4 | Season Pass First window | **Still open**; evidence moved from #473 to #472; BOTH_FAIR_FIGURE candidate | SQL L148 |
| DR5 | Premium buy on a prod build | **Still open**, unchanged; weak, additive | None |
| DR6 | #477 title change | **Still open**, unchanged; weak, additive; SC-18 | None |
| DR7 | ZOM-563 golden frames on prod | **Still open**, unchanged; weak, additive; SC-16 | None |

### DR1: settled

**Quote.** Brief, SQL L103, new sentence: "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date."

This ends the fork. The leaderboard hold has no dated fix: ZOM-429 is Backlog with `due_date` null (linear/data.json /issues/3495), SQL L161 says "Leaving as-is for now", and SQL L84 covers only "server windows that are still on the DEV stack". So the Hold until cell reads "until the fix is confirmed on prod", with no date. "instead of guessing a date" rules out Reading B (Mon Oct 13) and Reading C (all four weeks, or the pivot call).

**Residual, not a fork.** A held beat can show its Monday 00:00 UTC cadence marked held, or leave Windows blank. Both say the beat does not run until the fix is confirmed, so the rubric should not pin either form. Listing the leaderboard as running W1 to W4 would contradict the hold.

### DR2: settled

**Quote.** ZOM-534, Douglas (the assignee), Sep 25, SQL L180: "Quest points rollover now syncs quests-end with the client instead of waiting on a restart. That is on main, so nothing else has to land for the beta. I am keeping this open to watch one backend timing edge case on the day boundary."

This rules out Reading B directly: the edge case is watch-only and "nothing else has to land for the beta". The ticket staying In Progress is explained in the same comment.

**Strongest remaining reading, tested.** "On main" is not "on prod", and the brief names "prod deploy" as a still-to-do, so a strict reader could list a deploy. Two records kill that:
- The owner's own words, "nothing else has to land for the beta".
- The still-to-do must land "before it runs", and the beat runs regardless. SQL L235: "the current quests keep running either way". SQL L103: "a reset that needs a restart" does not hold a beat.

**Limit of this check.** I could not confirm "on main" from code. The only code hits were `QuestsEndPoint`, an unrelated URL field. The `commits` export holds no match3d-backend or match3d-quests commits from September (FD-2880), so this is unverifiable, not contradicted. The settlement rests on Douglas's statement.

### DR3: still open, unchanged

Records unchanged: SQL L111 "moves earlier"; spec "locked 24h before each season opens"; SQL L68 Fri Oct 31, 10:00 Istanbul (07:00 UTC, 7 hours past the Oct 31 00:00 UTC lock); SQL L39 "agreed with Product is for Wed Oct 29"; SQL L70 "drop the Oct 29 one".

Value A: any instant before Fri Oct 31 00:00 UTC. Value B: back to Wed Oct 29. Same decision, reply and recipient. The rubric must accept any instant before the lock. The new "guessing a date" sentence covers holds only and does not reach this.

### DR4: still open, evidence moved

The October-season proof moved from #473 to #472. SQL L148, Arthur, review comment on #472, 2025-09-30T15:52:58Z: "Fine for this PR. Separately, the Season Pass premium strip is still set to the October range. It needs the November range before that season opens, Oliver is taking the date change."

The wording on the October range is identical, so the analysis holds. The First window cell can be Oct 1, Oct 6 or Nov 1 00:00 UTC. "Season Pass runs only from Nov 1" stays killed, so Weeks running is W1 to W4 under every value. The rubric must accept these values.

### DR5, DR6, DR7: still open, unchanged

No statement in the revised SQL mentions ZOM-563, #477 or the premium buy (grep count 0 for each).

- **DR5.** Brief, SQL L103: "an unverified build or platform is a still-to-do, not a hold." Oliver, #zombie-ops, Sep 12: "We need to test the premium buy on a prod build". Spec: "No Season Pass purchase has been recorded yet". Reading B adds that check (Arthur) to Season Pass Still to do.
- **DR6.** #477 "Collect And Win Analytics and title change" is open, and no record says what the title change is. Reading B adds it (Owen) to Collect & Win Still to do. SC-18 says not to grade #477's state.
- **DR7.** ZOM-563 "Teams' lives, golden frames and names not working on prod env" is In Progress: "It works great in dev env, but in prod it doesn't." Vincent, #zombie-bugs, Sep 15: "the correct golden name after premium pass". Reading B adds a prod deploy (Douglas) to Season Pass. SC-16 says not to grade this ticket's status.

## What the main session needs to decide

Under the deep-recheck rule, a P1 finding is rejected only by a quote that rules out Reading B. Each of DR5 to DR7 is a superset of Reading A, so none contradicts the expected answer, but the best quotes available are not clean kills:

| DR | Best available quote | Does it kill Reading B? |
|---|---|---|
| DR5 | SQL L107: "(prod deploy, config, player-facing art an owner has flagged)" | No. SQL L103 "an unverified build or platform is a still-to-do" cuts the other way |
| DR6 | SQL L107: "not analytics" | Partly. It covers the analytics, not the title change |
| DR7 | SQL L107: "For each beat", with the ticket title "Teams'" | Nearly. No record ties it to a beat, but none rules it out |

If the main session keeps them, one closing line on each record would settle them, as ZOM-534's revision did. If it records them as additive, the rubric must treat those Still to do lists as a minimum, not as exact sets.

## Fork list

- F1: Weekly leaderboard hold end | Settled by: "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date." (SQL L103)
- F2: Quest rollover Still to do | Settled by: "That is on main, so nothing else has to land for the beta." (SQL L180)
- F3: Brian's new handoff date | before Oct 31 00:00 UTC | Wed Oct 29 | Both fair: BOTH_FAIR_FIGURE; rubric must accept any instant before the lock.
- F4: Season Pass First window | Oct 1 00:00 UTC | Oct 6 or Nov 1 00:00 UTC | Both fair: BOTH_FAIR_FIGURE; rubric must accept these values.
- F5: Season Pass Still to do | two items | plus premium buy check on prod | Missing: a record that the buy passed on a prod build.
- F6: Collect & Win Still to do | analytics excluded | plus #477 title change | Missing: what the title change is. SC-18.
- F7: Season Pass Still to do | Teams is not a beat | plus ZOM-563 prod deploy | Missing: a record tying it to a beat or closing it. SC-16.

## Every changed statement, and its effect

| SQL | Change | Effect on P1 |
|---|---|---|
| L103 | New hold-end sentence in the brief | Settles DR1 |
| L111 | Style-run offsets shifted by 103 | None. I confirmed each heading still sits at its offset |
| L130 | `web_view_link` added to the calendar sheet | Gives "link it on the calendar ticket" a real URL. No base file has this link |
| L148, L150, L152 (old L144-148, L158-160 removed) | Premium strip note moved from a post-merge #473 comment to a #472 review comment, with its #zombie-prs mirror and thread count | DR4 evidence moves. See N1 |
| L180 | ZOM-534 comment revised | Settles DR2 |
| L210 | ZOM-521 comment adds ZOM-541 | No effect. Card VFX, tied to no beat |
| L220 | ZOM-542 comment reworded | No effect. Still "not needed for the beta" |
| L235 | Trello card 61 comment reworded | Narrower closure. See N2 |

## New-fork check

- **N1, #472 note as a change-request hold: settled.** The note now sits in a review on an in-scope Aug-Sep live-ops PR, so it could be read as "an unresolved change-request review blocker". Killed by #472 rev_1 state APPROVED (2025-09-30T15:52:58Z) and the note's own "Fine for this PR. Separately". Season Pass stays not held, and the strip stays a still-to-do owned by Oliver.
- **N2, Trello wording: settled.** "Nothing in the beta waits on them" became "The rollover does not wait on them, the current quests keep running either way." The narrower wording could leave added quests open as a Quest rollover still-to-do. Killed for the beat by that same sentence, because nothing has to land for it to run. The same sentence covers the card's untouched "balance quest rewards" half.
- **N3, Quests push date: not a fork.** Row 1 says "Revisit once new quests roll out" and Trello says Oct 13 "if they are ready". The push is held either way (Not Ready). SQL L109 asks for "what is missing", not a date, and "if they are ready" means Oct 13 is not firm. The rubric should not pin Oct 13 as a push hold end.
- **N4, new hold sentence applied to pushes: not a fork.** Read either way, no held push gets a date.
- **N5, two link forms: not a fork.** The `web_view_link` id differs from the file id `f_e4a17c90b3d25f6a8c1d73`, but both reach the same sheet. The rubric should check the sheet is linked, not one exact URL.

## Still-to-do audit: every open note, and whether a record settles it

| Note | Beat | Verdict | Settled by, or what is open |
|---|---|---|---|
| ZOM-429, SQL L161 and L19 | Weekly leaderboard | Settled: held, fix owned by Douglas | Vincent's Sep 30 re-test is newer than Douglas's Sep 16 note. Hold end settled by SQL L103 |
| ZOM-534, SQL L180 | Quest rollover | **Settled** (was open): not a still-to-do | "nothing else has to land for the beta" |
| Trello card 61, SQL L235 | Quest rollover | Settled: not a still-to-do | "The rollover does not wait on them, the current quests keep running either way" |
| #470 rc_10, SQL L138 and GCal L84 | Collect & Win | Settled: prod deploy, Oct 8, Douglas | Douglas organizes the event. The brief says starts late, not held |
| #468 rc_38, SQL L141 | Collect & Win | Settled: final vial models, Claire | The review state is COMMENTED, so it is a still-to-do, not a change-request hold |
| ZOM-465, SQL L190-191 | Collect & Win | Settled: icon animation, Marcus | The owner flagged it, and comment 2 corrects comment 1 |
| ZOM-465 description, "Refill Timer ticking" | Endless | Settled: not a still-to-do | Marcus asks if it is still needed and nobody asks for it |
| ZOM-543, SQL L169 | Collect & Win | Settled: not a still-to-do | "plus Collect and Win"; ZOM-526 c3 "go through the queue manager now (#472)"; #472 merged; Trello card 63 dueComplete true |
| ZOM-526, SQL L172-174 | Collect & Win | Settled: not a still-to-do | Only Axe Arena travel is left |
| ZOM-521 and ZOM-541, SQL L209-218 | None | Settled: no beat | Card VFX waits on Brian's review, tied to no beat |
| ZOM-566, ZOM-552, ZOM-549, ZOM-442 | Collect & Win, Season Pass, others | Settled: excluded | Brief: "not analytics" |
| #477 | Collect & Win | **Open, weak** | DR6 |
| #472 rc_1, SQL L148 | Season Pass | Settled: November range, Oliver | Arthur's note names the owner |
| Brian's mails, SQL L39, L68 | Season Pass | Settled: Brian, moved before the lock | The new date is DR3 |
| #zombie-ops premium buy, Sep 12 | Season Pass | **Open, weak** | DR5 |
| ZOM-563 | Season Pass or none | **Open, weak** | DR7 |
| ZOM-556, SQL L163 | Daily gift | Settled: not held, nothing to land | "claiming works and nothing is lost", a wrong counter |
| ZOM-432, SQL L184 | Daily gift | Settled: shipped | "so nothing is left here", closed Done |
| ZOM-471, SQL L200 | Plague Race | Settled | "nothing here has to land for the beta" |
| ZOM-565, SQL L166; ZOM-542, SQL L220 | Endless | Settled | "not needed for the beta" |
| ZOM-504, ZOM-517, ZOM-546 | Endless | Settled | Visual only; the two re-tests did not reproduce |
| match3d-backend#34 | Endless | Settled: not a still-to-do | Draft since Aug 1, no review, no record asks for it |
| Martin's Endless themes, #zombie-art, Sep 29-30 | Endless | Settled: not a still-to-do | Ideas, not flagged as needed to run |
| ZOM-544, SQL L223; Trello card 54 | None | Settled: no beat | A login feature, tied to no window or reset |
| Trello cards 58 and 79 | None | Settled: no beat | Generic lists. ZOM-557 and ZOM-558 are Done |
| Trello "Oct 21" list, Axe Arena | None | Settled: out | Frederick, SQL L13: "just those four" |
| Store approval of the Sep 30 builds | All | Settled: not a beat item | The UA deck gates the buy itself on it. ZOM-432: "so nothing is left here" |

## Settled outcomes, re-checked on the revised SQL

| Outcome | Reading B | Killed by |
|---|---|---|
| Destination sheet | The shared LiveOps Event Calendar sheet | SQL L11 "the calendar sheet in your ZM Live Ops folder". SQL L130 is the one sheet there |
| Calendar ticket | Another ticket | SQL L187, ZOM-78: "Let us use this ticket ... Link the sheet here" |
| Push source | Domino sheet's PNs Beta tab | Prompt names Zombie Match 3D. Frederick's four rows match f_a325dd4af80afc5994d5dc. SQL L109 says the translated tab is the Domino set |
| Push set | Other row counts | 14 rows minus 4 is 10 lines. Rows 3 and 5 go out. Rows 4 and 6 are held for "Puzzles vs Zombies". Rows 1, 7, 9, 12, 13 and 14 fail Ready and LIVE. Result is 2 out, 8 held |
| Plague Race push "ready" | Row says Ready, so ready | SQL L109: "Ready and LIVE". The row is WIP, so held |
| Beat set | Boss Arena, Zombie Lane, Halloween, a rotating shop | SQL L99, L13, L17. The client LiveOps folder and backend schedules show no rotating-shop reset. Seven beats remain |
| Collect & Win start | Remainder of the Wed Oct 8 window | SQL L101: "a window the release instant pre-empts does not count". Result is Fri Oct 10 00:00 UTC |
| Held set | Quests, daily gift, Endless, Collect & Win, Season Pass | SQL L101 and L103. Only the weekly leaderboard is held |
| Change-request rule | A cohort blocker holds a beat | No review has state CHANGES_REQUESTED after Jul 16 in any repo. "Cohort" is undefined, but the set is empty under any Aug-Sep definition. #468 rev_3 is COMMENTED; #470 rev_9 and #472 rev_1 are APPROVED |
| Held push needs a ticket note | A start push is a beat | SQL L11: "the push that goes with it". The sheet splits Status from Push. No push has its own ticket. SQL L103 defines a held beat |
| Halloween | Keep it, per the Sep 18 approval | SQL L17: "my later word on this one is the one that counts"; SQL L105 |
| Which mail | Sep 22 thread | SQL L70: "Treat Fri Oct 31 as the date I am committing to"; "reply on this mail" |
| Who replies to Brian | Agent only records the date | The prompt incorporates the brief, and Brian's mail asks Julia to reply. SQL L70 |
| Lock instant | "the day before" as a loose day | Spec: "locked 24h before"; calendar page: "The 24h season-pass freeze" |
| Recommendation | Other channel | SQL L11: "back here". A thread or DM root reaches the same recipient |

## Edge values (unchanged)

- Collect & Win: 10 windows: Oct 10-12, 13-14, 15-16, 17-19, 20-21, 22-23, 24-26, 27-28, 29-30, Oct 31-Nov 2. The start is the same at 15:00Z or 16:00Z release.
- Endless: 28 daily resets and 4 weekly (Oct 6, 13, 20, 27). Nov 3 is outside the span.
- Weekly leaderboard schedule: Mondays 00:00 UTC (`LEAGUES_SCHEDULE`, CDK stack line 139), held under DR1's rule.
- Lock: Oct 31 00:00 UTC, which is 03:00 Istanbul. Brian's handoff misses it in either zone.

## Clarity

No finding. Each reading produces the same writes: both sheet tabs, a note on ZOM-429, the link on ZOM-78, the reply on Brian's Sep 26 mail and the DM to Frederick. The open forks change cell contents only. The prompt has no "I'll" statement.

## Platform and known issues

- PLATFORM: no finding rests on FD-2880 or FD-3785. FD-2880 limits only the check of "on main" under DR2. `[PERSON_NAME_2549]` in PN rows 6 and 13 is the source string.
- Known issues touched: SC-18 (DR6), SC-16 (DR7).
