# Fork sweep rev3 — blind solve and fork hunt

Clock: Oct 1, 2025, 00:00 Pacific (synth-cut). Persona: Calvin Price.
Sources read: `04_Prompt.txt`, `01_Universe_Inject.sql` (in full), base data through `hg.py search` only (Slack #builds C05433XK267, #zombie-bugs, #zombie-match3d, #zombie-prs, Calvin's six active DMs; GitHub PRs #465/#472/#473/#475 with reviews, comments, commits, timelines; Linear ZOM-543/556/560 and title search).
Not read: anything under Working_Files, Evals, claude, memory.

## Part 1 — Solve

### Governing records

- Ask: Brian DM `446ba45665ed73d2f06caca6963c6ffc` (D0770ET6WBW, 2025-09-30 20:40Z).
- Rules: Brian's note on ZOM-543, `comment_faaa792418a942cd40be046d8d217a7d` (20:25Z).
- Pass rule: Arthur's doc `f_6d0326fa006b136f1bbf82` "ZM builds and QA passes" (main-branch builds only; a branch pass must be redone after merge; a pass stands until the bug is seen again on a main build made after the one it passed on, whoever saw it).
- Decoy: `f_ea7517885d11570b54bf13` "DD hotfix builds and QA passes" (branch pass is enough) — DD only, not ZM.
- Legend: `f_d3a1aa5976285aac98ffda`. Sheet: `f_cb40955893624e1acb8500` (38 rows).
- Agenda: Trello card `68daad83bacf52c6ea7e1593`, current desc "Collect & Win, Level-end rewards" (action `68dc11dceb76ad640995fd98`, 09-30 17:22Z; replaced "Collect & Win, Daily Gift").

### Builds (from #builds posts, base)

| Build | Branch | Result post (UTC) | Message id |
|---|---|---|---|
| iOS Internal 1698 | feature `…/QueueManager` | 09-24 18:07 | ed765a45… |
| iOS Internal 1718 | feature `…/QueueManager` | 09-25 16:25 | 62fc1c52… |
| iOS Internal 1713 | main | 09-25 11:27 | e06c2e3a… |
| iOS Internal 1727 | main (merge of #465) | 09-25 22:21 | a5aad8e6… |
| Android 1974 | main | 09-24 23:13 | 46508024… |
| Android 1984 | main | 09-25 22:21 | 7755ceb7… |
| Android Submission 129 | main | 09-26 02:39 | 4128ad29… |
| Android 2006 | main | 09-29 15:39 | dd410e61… |
| iOS Internal 1745 | main | 09-29 16:19 | c0cc32e7… |
| iOS Internal 1746 | feature `…/AnimatedIcons` | 09-29 19:24 | a98bfd1e… |
| Android 2010 | main | 09-29 19:26 | 933f99c5… |
| Android 2013 | main | 09-29 23:34 | 929935ad… |
| iOS Internal 1750 | main | 09-30 01:55 | 7398f500… |
| iOS Internal 1757 | main | 09-30 18:43 | 812398b0… |
| Android Submission 135 | main | started 09-30 18:45, done 20:13 | a9b83581… / 3efd19c6… |

### PRs (GitHub, base + overlay)

| PR | Merged (UTC) | What the records say it fixes |
|---|---|---|
| #465 | 09-25 22:15:51 | Coin replay after kill; queued tutorials (body). |
| #473 | 09-30 15:41:20 | Author comment `#473#c_2` (Oliver, 15:42): rows 13, 38, 14, 37. No review. |
| #472 | 09-30 15:53:04 | Body (edited): pre-level panel vs coins = row 6. Arthur `#472#rc_1`: rows 12 and 15 are NOT in the diff; "the other two Collect & Win ones are" = rows 17, 18. |
| #475 | 09-30 16:09:15 | Body (edited): stars on tablets = row 8. Arthur `#475#rc_1`: pack sound (row 32) is NOT in it. |

### Reports (39)

P = Passed, QA = Waiting on QA, FIX = Waiting on a fix. Review = on the review list.

| # | Area | Status | Ticket | Review | Deciding record |
|---|---|---|---|---|---|
| 1 | Tutorials | QA | new | no | "ok, chat" = Vincent's "Looks ok to me" (DM `b547e6e0…`, 09-25 17:15) on iOS 1718, a feature-branch build; #465 merged later; no main re-test. |
| 2 | Tutorials | QA | new | no | Same as row 1. |
| 3 | Tutorials | P | new | no | nr iOS 1745 (main); no later sighting. |
| 4 | Tutorials | FIX | ZOM-567 | no | No fix; Oliver cannot reproduce yet (`comment_a4cc96d8…`). |
| 5 | Level-end rewards | P | new | no | ok iOS 1745 (main), #465 merged. |
| 6 | Level-end rewards | QA | ZOM-568 | yes | #472 body lists the fix; merged 09-30 15:53; sheet re-test blank. |
| 7 | Level-end rewards | P | new | no | nr iOS 1745 (main). |
| 8 | Level-end rewards | QA | ZOM-569 | yes | #475 body lists the fix; merged 09-30 16:09; re-test blank. |
| 9 | Daily Gift | FIX | new | no | nr iOS 1745, then Vincent saw it again on Submission 135 (`b156fdcd…`, #zombie-bugs thread reply, 21:20Z). No fix. |
| 10 | Daily Gift | FIX | ZOM-570 | no | "again Android 2013", no fix. |
| 11 | Daily Gift | FIX | ZOM-556 | no | Vincent's comment on ZOM-556 "Same thing" (`comment_b3c56083…`); no fix. |
| 12 | Season Pass | FIX | ZOM-571 | no | Arthur: not in #472 diff. |
| 13 | Season Pass | QA | ZOM-572 | no | Oliver's #473 comment; merged; not re-tested. |
| 14 | Season Pass | QA | ZOM-573 | no | Same. |
| 15 | Collect & Win | FIX | ZOM-574 | yes | Arthur: not in #472 diff. |
| 16 | Endless Mode | FIX | ZOM-575 | no | No fix. |
| 17 | Collect & Win | FIX | ZOM-585 | yes | ok iOS 1757, then Samuel saw it on Submission 135 (`comment_5f530dc1…`, 21:52Z). Fix already tried by QA on main. |
| 18 | Collect & Win | QA | ZOM-576 | yes | Fix in #472 (Arthur confirms). "again Android 2013" predates the merge by 16 hours; no try on a main build with the fix. |
| 19 | Collect & Win | FIX | ZOM-577 | yes | Owen: fix is local only (`comment_fbf3c978…`). |
| 20 | Win Streak | FIX | ZOM-560 | no | Vincent's comment on ZOM-560 (`comment_9f28b3d8…`); no fix. |
| 21 | Win Streak | FIX | ZOM-578 | no | Samuel "checking". |
| 22 | Zombie Lane | P | new | no | nr Android 2006 (main). |
| 23 | Zombie Lane | P | new | no | ok Android 2006 (main). |
| 24 | Zombie Lane | FIX | ZOM-586 | no | nr iOS 1757, then Owen saw it on Submission 135 (`comment_16aff20e…`, 22:07Z). No fix. |
| 25 | Boss Arena | QA | new | no | "ok, chat" = "Boss arena as well" (DM `bfdfa295…`) on branch build 1718; #465 merged later. |
| 26 | Boss Arena | P | new | no | nr Android 2006 (main). |
| 27 | Boss Arena | P | new | no | nr iOS 1745 (made 16:19). Robert's sighting (`ecf80487…`) is on Android 2006, made 15:39, before 1745. Pass stands. |
| 28 | Endless Mode | FIX | ZOM-579 | no | No fix. |
| 29 | Endless Mode | FIX | new | no | ok iOS 1750, then Robert saw it on Submission 135 (`a4082477…`, 21:44Z). No fix. |
| 30 | Endless Mode | FIX | ZOM-580 | no | No fix. |
| 31 | Card packs | P | new | no | ok iOS 1757 (main, after #475 merge). |
| 32 | Card packs | FIX | ZOM-581 | no | Arthur: pack sound not in #475. |
| 33 | Card packs | P | new | no | ok iOS 1757 (main). |
| 34 | Card packs | FIX | ZOM-582 | no | "again iOS 1757", a main build made after the #475 merge. |
| 35 | Tutorials | P | new | no | nr iOS 1745 (main). |
| 36 | Level-end rewards | FIX | ZOM-583 | yes | No fix. |
| 37 | Win Streak | QA | ZOM-584 | no | Oliver's #473 comment; merged; not re-tested. |
| 38 | Season Pass | QA | new | no | Oliver's #473 comment; merged; not re-tested. |
| 39 | Season Pass | FIX | new | no | Marcus DM to Calvin (`806f4a67…`, `bb5dd875…`, 09-30 17:10Z): pass icon glow stays on, today's main build, 3 levels in a row. Not a sheet row. |

### Five numbers

| Passed | Waiting on QA | Waiting on a fix | Areas clear | Review list |
|---|---|---|---|---|
| 10 | 10 | 19 | 0 | 7 |

- Passed: 3, 5, 7, 22, 23, 26, 27, 31, 33, 35.
- Waiting on QA: 1, 2, 6, 8, 13, 14, 18, 25, 37, 38.
- Waiting on a fix: 4, 9, 10, 11, 12, 15, 16, 17, 19, 20, 21, 24, 28, 29, 30, 32, 34, 36, 39.
- Review list: 15, 17, 18, 19 (Collect & Win) and 6, 8, 36 (Level-end rewards).

### Areas (all Open, all children Todo)

| Area | Reports | Not passed |
|---|---|---|
| Tutorials | 1, 2, 3, 4, 35 | 3 |
| Level-end rewards | 5, 6, 7, 8, 36 | 3 |
| Daily Gift | 9, 10, 11 | 3 |
| Season Pass | 12, 13, 14, 38, 39 | 5 |
| Collect & Win | 15, 17, 18, 19 | 4 |
| Win Streak | 20, 21, 37 | 3 |
| Zombie Lane | 22, 23, 24 | 1 |
| Boss Arena | 25, 26, 27 | 1 |
| Endless Mode | 16, 28, 29, 30 | 4 |
| Card packs | 31, 32, 33, 34 | 2 |

### Linear writes

- 10 children under ZOM-543, team ZOM, no assignee.
- 22 existing tickets moved under children: ZOM-567 to ZOM-586, ZOM-556, ZOM-560.
- State changes (9):
  - To In Validation: ZOM-568, ZOM-569, ZOM-572, ZOM-573, ZOM-584.
  - To Todo: ZOM-571, ZOM-574, ZOM-581, ZOM-585.
- Unchanged: ZOM-576 stays In Validation; ZOM-556, 560, 567, 570, 575, 577, 578, 579, 580, 582, 583, 586 stay Todo.
- 17 new sub-issues, no priority, no assignee:
  - Done: 3, 5, 7, 22, 23, 26, 27, 31, 33, 35.
  - In Validation: 1, 2, 25, 38.
  - Todo: 9, 29, 39.
- No existing ticket goes to Done; every Passed report is ticketless.

### Sharing

Invite `evt_342a813cb7765d4a6fce8d` attendees other than Calvin: arthur.blake, brian.foster, julia.lawson, leonard.hayes (organizer), vincent.parker.

## Part 2 — Forks

Percent = how strongly the records support the reading I used.

### Major

**F1. Rows 13, 14, 37, 38 — Waiting on QA vs Waiting on a fix (85 %).**
- QA: Oliver's comment `#473#c_2` on a PR merged at 15:41:20.
- FIX: the only evidence is the author's own comment, posted 50 seconds after he merged his own PR with no review. The PR is titled "Addressables/sp" and its summary describes an addressables refactor. The sheet Fix column is blank and all four tickets are Todo.
- No reviewer confirms or denies it, unlike #472 and #475. One quoted record settles it only if an author's claim is accepted as "a fix is in main".
- Moves 4 reports between two numbers and 3 ticket states (ZOM-572, 573, 584).

**F2. Rows 6 and 8 — Waiting on QA vs Waiting on a fix (85 %).**
- QA: one line each in the edited PR bodies of #472 and #475, both merged.
- FIX: sheet Fix blank, tickets Todo, no comment anywhere says a fix exists. Arthur's #472 review says what is and is not in the diff for the Collect & Win rows and does not mention the level-end fix. #475 changes 2 files and is about card packs; a tablet star fix there is surprising.
- A single record (the PR body) settles each. Review-list count is unaffected.

**F3. Row 17 (ZOM-585) — Waiting on a fix vs Waiting on QA (80 %).**
- FIX: QA tried the fix on main (ok on 1757), so the "not tried yet" clause fails.
- QA: the fix is in main, the report is open again, and QA has not re-tried since the re-open.
- Brian's wording supports FIX. State follows: Todo vs stays In Validation.

**F4. Row 18 (ZOM-576) — Waiting on QA vs Waiting on a fix (85 %).**
- QA: Android 2013 (09-29 23:34) predates the #472 merge (09-30 15:53), so QA never tried the fix.
- FIX: "again Android 2013" is a failed try on a main build, read without the dates.
- Settled by two records together (build post `929935ad…` and the PR merge time), not one.

**F5. Row 39 — a report or not; a duplicate of row 12 or not (85 %).**
- Report: DM, from a teammate, since the 26th, in a build, home screen after a level.
- Not: Marcus names no build number; a solver may fold it into row 12 (pass icon animation). Marcus's second message "its not the vfx, the animation itself is fine, its just the glow" separates them.
- Changes the total (39 vs 38) and Waiting on a fix (19 vs 18).

**F6. Row 9 — re-opened vs still Passed (85 %).**
- Re-opened: Arthur's rule says "whoever saw it"; Submission 135 was made after 1745.
- Passed: Brian says "don't add new reports from his chats". That sentence is about new reports, and this is a channel thread, but a solver can over-apply it.

### Minor

**F7. Rows 1, 2, 25 — Waiting on QA vs Passed (90 %).** Chat plus build post `62fc1c52…` plus Arthur's doc settle it. Three records are needed; the legend only says "the build is there". The DD doc is the decoy.

**F8. Row 27 — Passed vs re-opened (90 %).** Robert posted after the pass (22:40) but on a build made 40 minutes before the pass build. Needs both #builds timestamps.

**F9. Agenda — card vs Brian's DM of 09-29 (85 %).** Card and Leonard's update note are later and Brian's note points at "the agenda". "Level-end rewards" appears only on the card.

**F10. Rows 11 and 20 — existing ticket vs new (90 %).** Sheet Ticket cells are blank; only Vincent's comments on ZOM-556 and ZOM-560 link them. ZOM-560's title (reward "not granted") differs from row 20 (never "shows up on the home screen").

**F11. Submission 135 "made after" 1757.** 135 started 18:45:34, 1757 finished 18:43:07. Every reading agrees, but the start gap is under three minutes.

**F12. Row 34 — is #475's fix real.** Nobody confirms the pack-count fix is in #475. Either way the status is Waiting on a fix.

**F13. Who tried what on Submission 135.** Vincent and Robert both played 135 on 09-30 and recorded no ok/nr for the Waiting on QA rows. Treated as not tried.

**F14. DM from EMPLOYEE_0021 (D05S1S2H55M, 09-29 22:14, base): "Se ve un poco mas lento todo".** A remark on Calvin's video of his own branch, not a bug seen in a build; it also overlaps row 17. Not a report.

### Design observations

- **Review-list count does not separate the agenda trap.** The stale agenda (Collect & Win + Daily Gift) with correct statuses also gives 7 (4 + 3). Only the per-report flags differ.
- **Areas clear = 0** rests on two single records: Owen's comment on ZOM-586 (Zombie Lane) and the branch reading of row 25 (Boss Arena). Missing either gives 1; missing both gives 2.
- **Naive answer** (sheet only, "ok, chat" counted, no re-opens): Passed 17, areas clear 2.

## Contradictions and oddities

None blocking. Items found:

1. Calvin's invite emails show "Central Standard Time - El Salvador"; his Slack profile says America/Los_Angeles. All UTC times agree (18:00Z = 12pm CST = 9pm Türkiye = 2pm EDT).
2. D05U73FNDDL and the other DMs are `is_im: true` with 5 members (base quirk; real participants are Marcus and Calvin).
3. Android 1974 is a main build on 09-24 whose changes already list "Initial queueManager", a day before #465 merged (base).
4. Base #zombie-bugs thread 09-30 16:24 (`d0dd5d3a…`) has Marcus discussing a light-sweep shader on gold parts. It is close in theme to his injected "glow" DM 46 minutes later but does not contradict it.
5. PR body edits carry `updated_at` equal to Arthur's review time, later than the merge. Harmless.
6. Reply counts set by the overlay match base thread sizes (12, 5, 3, 4, 4).
7. Dates check: Oct 2, 2025 is a Thursday; card rename, invite update and email follow in order (17:22:05, 17:22:36, 17:24:03, 17:24:09); Brian's note (20:25) precedes his DM (20:40).

Not verified: "Julia's point about your tickets", Oliver's skip-tutorial exceptions in #zombie-bugs, Vincent's canvases, and whether Calvin can open the ZM ROADMAP Trello board.
