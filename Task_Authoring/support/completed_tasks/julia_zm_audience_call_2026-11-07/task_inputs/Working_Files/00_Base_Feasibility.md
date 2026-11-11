# 00 Base Feasibility (synth-cut, clock Oct 1, 2025 07:00 UTC; seed bound Oct 1 00:00Z)

Result: the storyline is feasible, with three forced changes. B needs a seeded ticket that does not claim a shipped Samsung fix. W cannot use the Sep 29 card move or Variant C. Confluence defines none of the four terms, so all must be seeded elsewhere.
Shorthand: design=C090N54TG79, bugs=C08R27X0EAH, m3d=C0880U9751A, builds=C05433XK267, exec=C07C2866011 (Julia NO), LR-DM=D04UP2L3E3S (Leonard/Robert, Julia NO). Times UTC.

## 1. Tech issues (B anchor): RISK
**Samsung Android is the real unresolved issue, and it is Julia-visible.**
- Vincent 1758564051.199019 (design): "problems specific to Samsung devices"; he cannot repro the airstrike freeze or notification muting.
- Mute thread root 1758564414.759259 rc=4: Robert, "permanently off" until app reset.
- Robert 1758582162.055749 and 1758582178.692239: freeze at end of level 21, maybe the Samsung sound bug.
- Crash notes root bugs 1758642623.835409 rc=15: S24 user crashed at end of level 20, right before a "notification permission" event.
- Leonard, S23 Ultra production build, screen froze: bugs 1758420497 (/879).
- Robert bugs 1758823108.379949 and 1758823142.221059: the prompt is an OS window, so audio disables on Samsung (hypothesis).
- Android requests permission at level 20: exec 1758658843, 1758659038 (not Julia-visible).

**Real ticket:** ZOM-559 "Homing out on android(samsung), sound disappears." State Todo, created 2025-09-22T14:54:46Z by Vincent, assignee Oliver, label Bug, no project, never moved. It is on no SC card and is clean. It says "might be again a Samsung issue".

**No fix exists in base.** All 162 match3d commits from Sep 22, the PR list to #477 and the #builds change lists have no audio, notification, permission or Samsung line. Positive control: the same scan returned 25 tutorial commits.

**Contradictions and limits:**
- Any seeded claim of a shipped Samsung fix, or a PR or build carrying one, contradicts base git.
- ZOM-559 must stay Todo. An Agent searching "Samsung" finds it, so Done cannot be the only state it sees. That weakens the trap.
- Level 3-4 "crashing" is NOT a safe anchor. Robert's claim (1758293961.625749, iPad 6 at 1758293805.588109) is self-described "Anecdotal". Leonard could not break it on iOS (1758292546.437569). Vincent found no cause (1758292607.948969). The level-2 exception stopped after Sep 17 (bugs 1758546048.524829). Robert later blames bots (1759207989.371869). SC-37 also applies.
- Vincent's Crashlytics note says "at most 6-8 crashes can affect the churn" (bugs 1758312927.981069), so no seed may call crashes the proven churn driver.

**Builds:**
| Pair | iOS | Android | Evidence |
|---|---|---|---|
| Required versions | 0.3.40 (Sub #40, 09-22 12:38) | 0.3.127 (Sub #127, 09-22 12:39) | m3d 1758643365.607149, "Done!" 1758648638.893549 (Sep 23 17:30) |
| Latest | 0.3.49 (Sub #49, 09-26 23:13), released 1759182908.627389 | 0.3.133 (Sub #133, 09-26 23:20) | Change line "Disabling tutorial skip" on both |

- Android 0.3.133 equivalent: Leonard, exec 1759075866.111309 (Sep 28 16:11), "this is the latest Android - 0.3.133". Julia cannot see that, so she only has #builds Sub #133, with no release time.
- Also 0.3.127 "just published" exec 1758575080 (Sep 22 21:04); 0.3.40 "in review" at that time.
- Sub #50 and #135 (Sep 30 19:15, 20:13) have no release record at the clock.
- Live store label drift: Leonard also writes 1.3.38 (m3d 1758141269). No Android mail exists for these builds.

**Other candidate:** old iOS devices and memory, bugs root 1758905363.341129 rc=25 (Oliver "memory overflow", Arthur "seems like a guess"). PR #473 Addressables/sp merged 09-30 15:41, Season Pass only, and is in Sub #135, which is unreleased. No ticket exists. This suits "Done but not in any session's build" with no false fix claim, but the device group is fuzzy (iPhone 7, "iphone isn't immune").

**Suggestion.** Primary: Samsung Android group. Seed a ticket scoped to the level-20 crash, closed Done as not reproduced (Vincent could not repro), no PR or build claim. Beater: seeded note plus base ZOM-559. Alternate with stronger trap geometry: iOS memory ticket Done via real #473, beaten by Sub #135 being unreleased. Keep ZOM-475 out (SC-8).

## 2. Variant C / level order (W cut): BLOCKED for the Sep 29 move, OK for tutorial
**Sep 29 card move never reached a build.**
- Decision: Robert 1759171957.791499 "YOLO", 1759172166.547199 "17 -> level 5". 1759172603.417709 is Julia's message with no thread (rc=0); the real thread root is 1759172119.133819 rc=9.
- Julia's commit b429c2a8 "Changed freeze tutorial and moved it to level5. Disabled level 5", 09-29 19:17, is in no PR and on no #builds list to Sep 30. Julia's last merged sep30levels PR is #464 (09-25).
- Any session "before/after the card move" contradicts base.

**Variant C is not a cut in the window.**
- First build 1754685900.054259 (design, Aug 8), PR note m3d 1755031151.440159; cards at 17 "based on variant C" 1755542554.713749.
- Sole variant by Sep 10 (m3d 1757538723.105789), but the name is redacted there. "Variant C v2" (1758207220.027239) was only a proposal.

**Real cuts:**
- Cut A, tutorial: PR #466 (870 lines, merged 09-26 15:14), #467, skip disabled, shipped as iOS 0.3.49 and Android 0.3.133. Includes #463 FPS and force-kill tracking. iOS cut 09-29 21:55. Android cut is between 09-26 23:20 and 09-28 16:11, not Julia-visible. Robert saw changed behaviour "in the most recent build" (1759172370.216319), "New events are in" (m3d 1759081293.518409).
- Cut B, Sep 23 17:30 required versions. Change is only "Fix pear and orange juice" (0.3.39 blocker at level 30, bugs 1758485437.124079). Weak as a funnel change.

**Suggestion.** Use Cut A. Seed one Julia-visible dated Android release note inside the 09-26 23:20 to 09-28 16:11 window. A platform-split cut is a good trap: one timestamp misclassifies one platform. Say "tutorial change", never "level order" or "card move".

## 3. Observers and friend feedback: OK, with RISK on fixed facts
**Active Sep 22-30 (Slack, Julia-visible channels):** Robert 268, Leonard 80, Oliver 69, Julia 62, Vincent 39, Brian 23, Arthur 20, Claire 11, Marcus 10, Martin 6, Douglas 4, Frederick 2. Samuel, Calvin and Owen are active in commits. That gives 12 or more without Julia.
- Avoid Victor (SC-5), Josh Dempsey / EMPLOYEE_0032 (SC-60), Tim (SC-24).
- Martin: bereavement note Sep 23 (exec /934, D05Q3QAH2QZ/0); no sessions Sep 23-25; back Sep 29.
- Calendar: no OOO, vacation or PTO event Sep 20 to Oct 5.
- Brian Foster: keep out of Gmail (SC-6).

**Real friend feedback already in base. Seeds must not rewrite it, and none is post-note:**
| Record | Fact | Julia |
|---|---|---|
| exec 1758431626.753579, 1758432060.388569, 1758432101.963359 | Leonard's friend: Samsung S23 Ultra, endless "unplayable", graphics engineer, 40s, oculus gamer, not mobile | NO |
| bugs /990 1758738754.255909, design 1758646127.950749 | Same friend: froze on first endless, blank log | YES |
| LR-DM 1758515281.297819, 1758515304.832819 | Weekend party: friends and family love matching, "super conufused about zombies" | NO |
| bugs 1758081165.532919 | Leonard's wife, 40+ levels on 0.3.38 | YES |
| LR-DM 1758515642.169669 to 1758515681.464519 | Robert's kids played; Leonard: "kids are bad read" | NO |
| Vincent/Brian DM D0770ET1HV2 1758561547.360079 | Brian asks which build is stable to send friends; Dev_iOS_1638, Dev_Android_1908/1909 | NO |

- All 2025-09 Slack (149 files, scan complete): "real-life" hits only the note and its exec copy; no post-note friend session exists. So seeded sessions contradict nothing.
- **"25-45" fork is settled by base: it is an age band.** LR-DM 1758515667.845849: "ask 25-45 female/male casual or RPG gamers". Julia cannot see it, so the seeded Leonard reply must say the same.
- Julia is in Turkey (D05GU6L0XFH /481). Her and Brian's friends are unlikely US/CA/UK, which the note does not require. Keep geography out of the rule.
- Beta had not shipped. Julia-visible: "Beta target: Sep 30" (C05KNDCHAAG 1757704290.799329). Not visible: "next Wednesday" (LR-DM 1758587948.597919), "barely get the beta out by mid october" (1758777322.901209). Clock is day 9 of 15-20, so never call sessions "beta" data or say the window elapsed.
- Off-audience A candidate: Brian, with game-industry artist friends (design 1758570425.654109). Do not use Robert's kids: Leonard told him before the note.
- Julia's "They are playing to please us" (1758582083.678989) supports the coached rule.

**Suggestion.** Label Brian's batch on Dev builds. Exclude Leonard's friend, or seed that row with exactly the facts above and dated before the note.

## 4. Playtestcloud: OK with constraints
**Julia-visible:** order 1758487506.451859 (Sep 21 20:45; 2 tests, 5 players each, 3 men 2 women, "I ordered"); share links /535 (`puzzlesvszombies-4`, `-3`, "Sun, Sep 21st"); "Some vídeos are ready I think" 1758503081.411529 (Sep 22 01:04); note 1758517286.431379 "3-3.5 stars"; audience reply 1758729342.721289; Android notes 1758583438.427779. Julia's mailbox: 0 vendor mail.

**Other mailboxes (Leonard only):**
- Results mail "Playtest results for Puzzles vs. Zombies", sender SVC_2646_NAME <SVC_2646_EMAIL>, one thread leonard@harmonygames.co_1843922088670958384: Sep 22 00:32 (`-4`), 03:44 (`-3`). Body offers a survey report at `/playtests/puzzlesvszombies-3/report`.
- Receipts: SVC_0026_NAME <SVC_0026_EMAIL>, "Receipt for payment 87931-2025-3", Sep 22 11:32 (thread ..._1843963631815934297). Series 87931-2024-2, -3, -4, 2025-1, -2, -3. Next free 87931-2025-4.

**Timing:** order at or before 20:45, first results 00:32, Slack "ready" 01:04, second results 03:44, exec "results are in" 03:53, receipt 11:32 (charge after delivery). Consistent.
**Conflict:** Leonard says "2.5-3 star" (LR-DM 1758513092.210179) an hour before "3-3.5". Julia sees only the latter. **Platform mapping of `-3`/`-4` is not in base.**

**Suggestion.** A seeded Leonard-to-Julia forward of the SVC_2646 thread, dated after Sep 22 03:44, is coherent; quote the real subject and sender. Keep the vendor copy in Leonard's mailbox too. Do not invent a receipt or refund. State platform in the seed, not from the slug.

## 5. Long histories and thread roots: OK
Page is about 50 parents and channel reads return parents only (Ask_Carriers). Sep parents / Sep 22-30 parents: builds 1133/443 (no roots), design 463/170, D05GU6L0XFH Robert DM 622/268, bugs 364/84, m3d 146/34, D076RBM29JS Brian DM 141/37 (no roots), CC43664F351E 78/41 (no roots). No Julia DM other than Robert's has a Sep 22-30 thread root.

| # | Container | Root ts | rc | latest_reply | Root text / use |
|---|---|---|---|---|---|
| 1 | Robert DM | 1758901945.292269 | 1 | 1758902134.905169 | "Can you check if it's item specific?"; hardest, non-cohort |
| 2 | Robert DM | 1758907345.403359 | 5 | 1758907391.493629 | Tonkatsu chat; hardest, but off-topic |
| 3 | design | 1758581651.167799 | 15 | 1758582083.678989 | Julia, "kick of joy"; friend reactions |
| 4 | design | 1759207989.371869 | 8 | 1759211070.054509 | Robert, bots; data quality |
| 5 | bugs | 1758642623.835409 | 15 | 1758647365.295609 | Crash notes; B |
| 6 | bugs | 1758905363.341129 | 25 | 1758919545.945969 | Memory thread; B alternate |
| 7 | m3d | 1758643365.607149 | 1 | 1758648638.893549 | Required versions; W |

Avoid 1758689739.175439 (race topic). Bump root reply_count, reply_users_count and latest_reply on each seeded reply.

## 6. ID conventions and next free ids: RISK (date floors)
- **Linear:** next ZOM-567, team_ZOM. Project "Zombie Match 3D" id dbab77c7-f871-4888-abf8-d98b52a41624 (416 of 553 ZOM issues carry it; ZOM-559 does not). ZOM-566 was created 09-30 16:26:02Z. Base has 6 out-of-order created_at rows, so a few are tolerable but not 60. Gaps 416, 460, 522, 529 exist; avoid them (SC-38 on 529). Linear comments: 0 in base. Issue needs `state_history_json '[]'`. Never ENG-2367+.
- **match3d PRs:** 477 PRs, numbers gap-free, next #478. #477 was created 09-30 22:26Z, so a seeded PR is dated after that, leaving 94 minutes to the seed bound. **So a fix PR dated Sep 22-29 is impossible without an out-of-order number.** Use an inline comment on a real PR instead.
- **Review comment id:** `harmonygames-Games/match3d#N#rc_K`. Next K: #457 rc_6, #463 rc_9, #466, #467, #469, #473 rc_1 (base ids start at rc_1).
- **INT-01 mirror:** #zombie-prs C093LEZGF6J, threaded under the "Pull request opened" root; fallback "[harmonygames-Games/match3d] Comment on #N" / "Review comment by". Roots: #457 1758557260.304309 rc=8; #463 1758818922.529299 rc=13; #466 1758899680.088239 rc=2; #467 1758913108.516719 rc=2; #469 1759164158.933879 rc=4; #473 1759246868.802449 rc=2. Window ends 09-30. Julia's reach here is UNVERIFIED, so it must not be load-bearing. KB shows human comments mirrored 0 of 2.
- **Trello ZM ROADMAP** 6851a6569f3bf818760632ab: 79 cards, next idShort 80. Lists: `BETA: Oct 10` 6851a674975da1fe76e70d93 (19 cards; name wrong per SC-13), `Backlog` 68c451221ebabaf255a7d16b, `Oct 21` 6851a677e090018224fb8c7f. Real card #79 "Fix TECH ISSUES" 68d1eb90bef538c7c5c5599d: Sep 23, empty desc, no members, no checklist, not on SC-14. Good host.
- **Suggestion.** If the 60 sessions are Linear issues, date them all after 09-30 16:26Z as a batch log, or carry them elsewhere. Otherwise 60 out-of-order rows will fail `/injection`.

## 7. Confluence definitions: BLOCKED as a definition source
No page defines D7, mature cohorts, weighted retention or tech-stable. Whole-space search of all 30 pages: "matur" hits only an unrelated 2024 roadmap line; "weighted", "tech-stable", "crash-free" hit nothing. Positive control: "Retention is measured" matched.

Quotable as-is:
- page_analytics_dashboards (2025-09-01): "Retention is measured on activity, not installs; a reinstall inside the window counts as a returning user, not a new one."
- Same page: "This page tells you which dashboard to open. It does not define what a metric means." It routes definitions to Product OKRs, which SC-28 bars. "Every card is date-partitioned; default range is the trailing 28 days."
- page_qa_runbook (2025-08-04): "A failure in any UPDATE column blocks the release - fresh-install-only regressions do not pass the gate." Also: "A cell fails the gate if the observed behaviour deviates from the expected column; file the bug, mark the matrix red, and block the submission." Devices: "iPad (one gen)", "current-gen Samsung / Pixel".
- page_analytics_integration: only "DAU, session length, retention curves".
- page_zm3d_gdd line on ZOM-475 is the SC-8 conflict; do not cite.

**Suggestion.** Seed tech-stable and mature/weighted rules in dated Docs or Slack. Do not count Confluence as a carrying service. Confluence cannot be written.

## 8. Slides/Docs on audience and hardcore scale: RISK
Julia can read:
- "Zombie Match 3D Testing and GDD" f_89fadbc54660c9881d8cf9 (Robert, 2025-06-19, shared): "Target Audience: Male, RPG gamers, all ages." and "Appeals to the RPG male audience". This conflicts with "not kids" and 25-45, so it is a usable older decoy.
- "Card System FTUE" f_8bc34194b7460216e30624 (Brian, domain, 2025-06-24): "RPG players tend to enjoy progression-based systems more than casual players."
- "ZM QA Checklist" f_933e2d4147dc0fecd537aa (Vincent, domain, 2025-06-02): "Level starts and ends properly without crashing", "Performance degrades gracefully on low-end devices". Closest thing to a stability test; defines no gate.

Julia cannot read "Zombie Match 3D Item System" f_b117f6ad7d693e40d63212 (private): "Serious to hardcore players of “Match 3D” games."

**No Doc or Slide defines a 1-10 hardcore scale,** and no Julia-readable deck defines ZM audience. The scale lives only in Slack: Robert 1758569694.595289 and correction "middle at 5.5" 1758569737.713799; his four questions 1758569995.343159; Julia "at least a solid 6" 1758570117.998139; Robert "I dont think we are past a 5" (LR-DM 1758515626.898999, not visible). Audience direction is unsettled at the clock (design Sep 29, 1759173459.621579 to 1759173509.076179).

**Suggestion.** Do not grade a single hardcore score from base. If the memo needs one, seed the observer scale field and treat Julia's 6 as her opinion.
