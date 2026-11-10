# P1 findings: Unique Ground Truth and Clarity

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Persona: Julia Lawson.

**Checked:** 48 sentences: prompt 6, Frederick's DM 6, his thread reply 5, the brief 26, the UA deck 5 (plus its 4 week lines). I also read all 14 PNs Beta rows, Brian's 2 mails, Robert's 2 messages, the 22 Linear tickets the SQL touches and the key ZM ROADMAP cards. I scanned the titles of all 97 open ZOM tickets post-SQL, and the state and review history of match3d, match3d-backend and liveops PRs from mid-July on. SQL was read, not run. "SQL Lnn" is a line of `R/inputs/01_Universe_Inject.sql`; mail citations use Julia's mailbox copy.

**Result**
- Unique Ground Truth: 7 forks. DR1 and DR2 are fail-level. DR3 and DR4 are both-fair candidates. DR5, DR6 and DR7 are weak and additive.
- Clarity: **no finding.** No reading changes the set of write actions. See "Clarity" below.

---

## Findings

### DR1 | P1 | common_errors section 2, "which number or date" | Unique Ground Truth | Proposed: fail-level (UGT 2)

**Quote.** Frederick, SQL L11: "if anything is held and until when". Prompt: "If a beat ends up held, leave a note on its ticket". Sheet header, SQL L132: "Hold until (UTC)".

**Records**
- SQL L19, Vincent, #zombie-match3d, 2025-09-30T20:50:12Z: "Re-tested the weekly leaderboard on the current prod build: it still does not start a new week. I killed the app and reopened it twice ... Same on the second device." This settles that the beat is held. It gives no end date.
- SQL L165, Douglas on ZOM-429, Sep 16: "so not blocking. Leaving as-is for now."
- linear/data.json /issues/3495, ZOM-429: state Backlog, `due_date` null.
- SQL L84, GCal Oct 8 15:00Z: "The server windows that are still on the DEV stack go live with this release". It does not mention a leaderboard fix.
- The brief, SQL L93-111: no rule for how a hold ends. "until the pivot call" appears for Boss Arena and spend, and no record gives that call a date (Leonard's Sep 22 #zombie-design note says only "in 15-20 days").

**Fork**
- Reading A: Held, no date on record, open until ZOM-429 is fixed and re-tested on prod. No weeks running.
- Reading B: Held to a named instant, Mon Oct 13 00:00 UTC, the first Monday reset after the only scheduled backend release. W2 to W4 running. The brief says "the calls are yours".
- Reading C: Held for all four weeks, through Sun Nov 2 23:59 UTC, or until the pivot call.

These differ in the Hold until, Windows, Weeks running and First window cells, and in the recommendation.

**Looked for a settling record and found none.** ZOM-429 has no dated comment. Vincent's message has `reply_count` 0. No PR title or body, and no commit since Aug 15, cites ZOM-429 or a weekly-rollover fix (the export's `commits` list is a subset, FD-2880). Julia's calendar has no such event. A full scan of Julia's Sep-Oct mail found no fix note.

**Would settle it:** a dated, persona-visible fix commitment on ZOM-429 or in that channel, or a brief sentence saying how to state the hold when no fix date exists.

### DR2 | P1 | section 2, "which items are in the set" | Unique Ground Truth | Proposed: fail-level (UGT 2)

**Quote.** Brief, SQL L107: "For each beat, what still has to land before it runs for bought users (prod deploy, config, player-facing art an owner has flagged) and who owns it. Not what already shipped, not analytics, not polish nobody flagged."

**Records**
- SQL L184, Douglas on ZOM-534, Sep 25: "Quest points rollover now syncs quests-end with the client instead of waiting on a restart. Watching one backend timing edge case on the day boundary."
- linear/data.json /issues/3608, ZOM-534: state In Progress, priority 1, "Quest points not resetting until app restart in production".
- SQL L239, Trello card 61: "Nothing in the beta waits on them". This covers only the added quests, not ZOM-534.

**Fork**
- Reading A: Quest rollover is in, with nothing to land. "now syncs" means done, and "Watching" is not a landing.
- Reading B: Quest rollover Still to do: Douglas, ZOM-534 backend day-boundary case. The ticket is open and urgent, and no record says the sync is on prod. "prod deploy" is a named category.

The hold rule ("a reset that needs a restart") settles Held only, not the Still to do cell.

**Looked for a settling record and found none.** No PR or commit in the export cites ZOM-534 or quests-end, and Julia's Sep-Oct mail has nothing on it. Sibling comments each close this question in words (ZOM-526, ZOM-565, ZOM-542 and ZOM-471 say the work is not needed or need not land for the beta). ZOM-534 does not, and that makes the gap stand out.

**Would settle it:** a clause on ZOM-534 saying the fix is on prod and nothing is left to land, or that the edge case is still to land.

### DR3 | P1 | section 2, "which number or date" | Unique Ground Truth | Proposed: BOTH_FAIR_FIGURE candidate

**Quote.** Brief, SQL L111: "A committed date that misses the lock moves earlier and its owner is told in a reply on the mail where they committed to it."

**Records**
- Confluence /pages/20, page_season_pass_spec: "locked 24h before each season opens". With the season opening Nov 1 00:00 UTC, the lock is Fri Oct 31 00:00 UTC.
- SQL L68, Brian, Sep 26: "moves from Wed Oct 29 to Fri Oct 31, 10:00 Istanbul time", which is 07:00 UTC. It misses the lock by 7 hours.
- SQL L70: "drop the Oct 29 one".
- SQL L39, Brian, Sep 22: "The config handoff we agreed with Product is for Wed Oct 29".

**Fork.** Only the new date differs. The decision, the reply on the Sep 26 mail and the recipient are the same.
- Value A: any instant before Fri Oct 31 00:00 UTC, so Thu Oct 30 at the latest (derived from the spec).
- Value B: back to Wed Oct 29, the date agreed with Product.

No record names the new date. Nothing the Agent does next changes. Any rubric row must accept any instant before the lock.

### DR4 | P1 | section 2, "which number or date" | Unique Ground Truth | Proposed: BOTH_FAIR_FIGURE candidate

**Quote.** Brief, SQL L101: "A beat starts with the first window that opens after its server windows are live on prod" and "Season Pass seasons open on the 1st at 00:00 UTC". SQL L97: "The calendar covers Mon Oct 6 00:00 UTC". Sheet column: "First window (UTC)".

**Records**
- SQL L138, Arthur, #470: "Season Pass schedules are already running on prod".
- SQL L144, Arthur, #473: "still set to the October range".
- SQL L39: "opens on Sat Nov 1".

**Fork.** The First window cell for Season Pass differs.
- Oct 1 00:00 UTC: the October season, already open.
- Oct 6 00:00 UTC: clipped to the span.
- Nov 1 00:00 UTC: the only season that opens inside the span.

"Season Pass runs only from Nov 1" is killed by #473's October range, so Weeks running stays W1 to W4 under every value. The status, writes and destination are the same. Any rubric row must accept these values.

### DR5 | P1 | section 2, "which items are in the set" | Unique Ground Truth | Proposed: weak, additive only

**Quote.** Brief, SQL L103: "an unverified build or platform is a still-to-do, not a hold."

**Records**
- #zombie-ops, ts 1757646802.623469, Oliver, Sep 12: "We need to test the premium buy on a prod build".
- Confluence /pages/20: "No Season Pass purchase has been recorded yet".
- #zombie-bugs, Sep 16, Vincent: "After purchasing premium pass, lives are reset to 8 after every win" (on "latest builds", not stated as prod).

**Fork.** Reading A has two Season Pass items: Nov config (Brian) and premium strip (Oliver). Reading B adds "premium buy checked on a prod build (Arthur)". No record closes it. Reading B is a superset and does not contradict A.

**Would settle it:** one line saying the buy passed on a prod build, or the rubric treating the list as a minimum.

### DR6 | P1 | section 2, "which items are in the set" | Unique Ground Truth | Proposed: weak, additive only; known issue SC-18

**Quote.** Brief, SQL L107 (as DR2). Frederick, SQL L11: "what still has to land before it runs and who owns that".

**Record.** GitHub match3d#477 "Collect And Win Analytics and title change": `state` open, created 2025-09-30T22:26:30Z, after the iOS 50 and Android 135 builds started. Its body lists analytics plus "Initial color/state corrected". No record says what the "title change" is.

**Fork.** Reading A: excluded as analytics. Reading B: add "#477 title change and bug fix (Owen)". The brief's "not analytics" covers most of it but not the title change. SC-18 says not to grade #477's state, so any rubric row must stay neutral on it.

### DR7 | P1 | section 2, "which items are in the set" | Unique Ground Truth | Proposed: weak, additive only; known issue SC-16

**Quote.** Brief, SQL L107 (as DR2).

**Record.** linear/data.json /issues/3640, ZOM-563 "Teams' lives, golden frames and names not working on prod env": In Progress, Douglas, updated Sep 30, "It works great in dev env, but in prod it doesn't." Golden frames and names are premium-pass perks: #zombie-bugs, Sep 15, Vincent: "the correct golden name after premium pass".

**Fork.** Reading A: Teams is not a beat. Reading B: Season Pass Still to do adds a prod deploy for premium frames and names (Douglas). No persona-visible record ties it to a beat or closes it. SC-16 says not to grade this ticket's status.

---

## Fork list

- F1: Weekly leaderboard hold end | no date, until fix verified | a named instant (Oct 13) or all four weeks | Missing: a dated, persona-visible fix commitment or a brief rule for undated holds.
- F2: Quest rollover Still to do | none | ZOM-534 day-boundary case, Douglas | Missing: a statement on ZOM-534 of what, if anything, is left to land.
- F3: Brian's new handoff date | before Oct 31 00:00 UTC | Wed Oct 29 | Both fair: BOTH_FAIR_FIGURE; rubric must accept any instant before the lock.
- F4: Season Pass First window | Oct 1 00:00 UTC | Oct 6 or Nov 1 00:00 UTC | Both fair: BOTH_FAIR_FIGURE; rubric must accept these values.
- F5: Season Pass Still to do | two items | plus premium buy check on prod | Missing: a record that the buy passed on a prod build.
- F6: Collect & Win Still to do | analytics excluded | plus #477 title change | Missing: what the title change is. SC-18.
- F7: Season Pass Still to do | Teams is not a beat | plus ZOM-563 prod deploy | Missing: a record tying it to a beat or closing it. SC-16.

---

## Still-to-do audit: every open note, and whether a record settles it

| Note | Beat | Verdict | Settled by, or what is open |
|---|---|---|---|
| ZOM-429, SQL L165 and L19 | Weekly leaderboard | Settled: held, fix owned by Douglas | Vincent's Sep 30 re-test is newer than Douglas's Sep 16 note. The hold end is open (DR1) |
| ZOM-534, SQL L184 | Quest rollover | **Open** | DR2 |
| Trello card 61, SQL L239 | Quest rollover | Settled: not a still-to-do | "Nothing in the beta waits on them" |
| #470 rc_10, SQL L138 and GCal L84 | Collect & Win | Settled: prod deploy, Oct 8, Douglas | Douglas organizes the event. The brief says starts late, not held |
| #468 rc_38, SQL L141 | Collect & Win | Settled: final vial models, Claire | The review state is COMMENTED, so it is a still-to-do, not a change-request hold |
| ZOM-465, SQL L194-195 | Collect & Win | Settled: icon animation, Marcus | The owner flagged it, and comment 2 corrects comment 1. The brief's "an owner has flagged" covers it |
| ZOM-465 description, "Refill Timer ticking" | Endless | Settled: not a still-to-do | Unstruck polish in the base ticket. Marcus asks if it is still needed and nobody asks for it |
| ZOM-543, SQL L173 | Collect & Win | Settled: not a still-to-do | Same comment: "plus Collect and Win". ZOM-526 c3: "go through the queue manager now (#472)". #472 merged. Trello card 63 dueComplete true |
| ZOM-526, SQL L176-178 | Collect & Win | Settled: not a still-to-do | Only Axe Arena travel is left |
| ZOM-521, SQL L213-222 | None | Settled: no beat | Card pack animation waits on Brian's review, tied to no beat |
| ZOM-566, ZOM-552, ZOM-549, ZOM-442 | Collect & Win, Season Pass, others | Settled: excluded | Brief: "not analytics" |
| #477 | Collect & Win | **Open, weak** | DR6 |
| #473 c_2, SQL L144 | Season Pass | Settled: November range, Oliver | Arthur's note names the owner |
| Brian's mails, SQL L39, L68 | Season Pass | Settled: Brian, moved before the lock | The new date is DR3 |
| #zombie-ops premium buy, Sep 12 | Season Pass | **Open, weak** | DR5 |
| ZOM-563 | Season Pass or none | **Open, weak** | DR7 |
| ZOM-556, SQL L167 | Daily gift | Settled: not held, nothing to land | "claiming works and nothing is lost", a wrong counter |
| ZOM-432, SQL L188 | Daily gift | Settled: shipped | "so nothing is left here", closed Done |
| ZOM-471, SQL L204 | Plague Race | Settled | "nothing here has to land for the beta" |
| ZOM-565, SQL L170; ZOM-542, SQL L224 | Endless | Settled | "not needed for the beta" |
| ZOM-504, ZOM-517, ZOM-546 | Endless | Settled | Visual only; the two re-tests did not reproduce |
| match3d-backend#34 | Endless | Settled: not a still-to-do | Draft since Aug 1, no review, no record asks for it |
| Martin's Endless themes, #zombie-art, Sep 29-30 | Endless | Settled: not a still-to-do | Ideas, not flagged as needed to run |
| ZOM-544, SQL L227; Trello card 54 | None | Settled: no beat | A login feature, tied to no window or reset |
| Trello cards 58 and 79 | None | Settled: no beat | Generic lists. ZOM-557 and ZOM-558 are Done |
| Trello "Oct 21" list, Axe Arena | None | Settled: out | Frederick, SQL L13: "just those four" |
| Store approval of the Sep 30 builds | All | Settled: not a beat item | The UA deck gates the buy itself on it. ZOM-432 treats the submission builds as landed: "so nothing is left here" |

---

## Settled outcomes (Reading B tried, and what kills it)

| Outcome | Reading B | Killed by |
|---|---|---|
| Destination sheet | The shared LiveOps Event Calendar sheet | SQL L11 "the calendar sheet in your ZM Live Ops folder". SQL L130 is the one sheet there |
| Calendar ticket | Another ticket | SQL L191, ZOM-78: "Let us use this ticket ... Link the sheet here" |
| Push source | Domino sheet's PNs Beta tab | Prompt names Zombie Match 3D. Frederick's four rows match f_a325dd4af80afc5994d5dc. SQL L109 says the translated tab is the Domino set |
| Push set | Other row counts | 14 rows minus 4 is 10 lines. Rows 3 and 5 go out. Rows 4 and 6 are held for "Puzzles vs Zombies". Rows 1, 7, 9, 12, 13 and 14 fail Ready and LIVE. Result is 2 out, 8 held |
| "whether its push is ready" for Plague Race | Row says Ready, so ready | SQL L109: "Ready and LIVE". The row is WIP, so held |
| Beat set | Boss Arena, Zombie Lane, Halloween, a rotating shop | SQL L99, SQL L13, SQL L17. The client LiveOps folder and backend schedules show no rotating-shop reset. Seven beats remain |
| Collect & Win start | Remainder of the Wed Oct 8 window | SQL L101: "a window the release instant pre-empts does not count". Result is Fri Oct 10 00:00 UTC |
| Held set | Quests, daily gift, Endless, Collect & Win | SQL L101 and L103 (restart, counters, cosmetic, release wait) |
| Change-request rule | A cohort blocker holds a beat | No review has state CHANGES_REQUESTED after Jul 16 in any repo (#303 and backend#4 are outside Aug-Sep). "Cohort" is undefined, but the set is empty under any Aug-Sep definition. CodeRabbit and #468 reviews are COMMENTED, and #470 rev_9 is APPROVED |
| Held push needs a ticket note | A start push is a beat | SQL L11: "the push that goes with it". The sheet splits Status from Push. No push has its own ticket. SQL L103 defines a held beat |
| Halloween | Keep it, per the Sep 18 approval | SQL L17: "my later word on this one is the one that counts"; SQL L105 |
| Which mail | Sep 22 thread | SQL L70: "Treat Fri Oct 31 as the date I am committing to"; "reply on this mail" |
| Who replies to Brian | Agent only records the date | The prompt incorporates the brief, and Brian's mail asks Julia to reply. SQL L70 |
| Lock instant | "the day before" as a loose day | Spec: "locked 24h before"; calendar page: "The 24h season-pass freeze" |
| Recommendation | Other channel | SQL L11: "back here". A thread or DM root reaches the same recipient |

## Edge values

- Collect & Win: 10 windows: Oct 10-12, 13-14, 15-16, 17-19, 20-21, 22-23, 24-26, 27-28, 29-30, Oct 31-Nov 2. The start is the same at 15:00Z or 16:00Z release.
- Endless: 28 daily resets and 4 weekly (Oct 6, 13, 20, 27). Nov 3 is outside the span.
- Weekly leaderboard schedule: Mondays 00:00 UTC (`LEAGUES_SCHEDULE`, CDK stack line 139). Four scheduled resets, all subject to DR1.
- Lock: Oct 31 00:00 UTC, which is 03:00 Istanbul. Brian's handoff misses it in either zone.

## Clarity

No finding. Each reading produces the same writes: both sheet tabs, a note on ZOM-429, the link on ZOM-78, the reply on Brian's Sep 26 mail and the DM to Frederick. DR1 to DR7 change cell contents only, which is the UGT topic. The prompt has no "I'll" statement.

## Platform and known issues

- PLATFORM: no finding rests on FD-2880 or FD-3785. FD-2880 only limits the commit search behind DR1 and DR2. `[PERSON_NAME_2549]` in PN rows 6 and 13 is the source string.
- Known issues touched: SC-18 (DR6), SC-16 (DR7). SC-8 and SC-38 are not relied on.
