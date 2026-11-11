# H2: Leagues Re-test Relocation + Per-Thread Reads for R3

Status: complete (all three sections)

Clock: 2025-10-01 00:00 PT (07:00Z) · Seed bound 2025-10-01T00:00:00Z · Persona: Julia Lawson (`EMPLOYEE_0005_SLACK_ID`)

## 1. Leagues prod re-test relocation

### Decision

Move the T7 superseding record out of `#zombie-bugs` entirely. It becomes a **root post in `#zombie-match3d` (`C0880U9751A`)** on Tue **2025-09-30 20:50:12Z**, not a thread reply anywhere.

| field | value |
|---|---|
| channel | `C0880U9751A` (`#zombie-match3d`, private, 25 members) |
| **new ts** | **`1759265412.481907`** |
| UTC | **2025-09-30 20:50:12Z** (= 13:50 PT) |
| kind | root, `thread_ts = null`, `reply_count = 0` |
| author | `EMPLOYEE_0012_SLACK_ID` (Vincent Parker) |
| beat | weekly leagues / leaderboard → **HELD** |
| replaces | `C08R27X0EAH/1759266900.274551` (a reply under Vincent's Sep 22 root `C08R27X0EAH/1758546048.524829`) — **delete that seed; do not inject it** |

Why the old form was wrong: the record it supersedes (`C08R27X0EAH/1758546119.789009` → last reply `1758546777.731809`, "after a moment, I am now in the weekly leaderboard…") and the superseding re-test both sat in `#zombie-bugs`, so the same channel both resolved and unresolved the beat — a reviewer reads that as an in-thread contradiction rather than as a chronology. As a root in `#zombie-match3d`, the final state is a *cross-channel* supersede: the last word on leagues is in a different channel from the "working fine right now" recovery, and both are Julia-visible.

### Intended meaning (verbatim proposal for the seed text)

> Checked 0.3.49 on iOS and submission #135 on Android. Weekly leaderboard / leagues still don't start the new week — old board is still showing with 0 points and I can't claim last week's rewards. Killing the app doesn't help this time, so I'm holding the leagues for now.

What it pins, in R3 terms: on the submission builds the player cannot **score** (board stuck on the old week at 0 points) and cannot **claim** (last week's rewards), and it survives a **restart** ("killing the app doesn't help this time") — so the leagues beat is HELD, not merely at-risk. It also directly overturns the Sep 22 "yep, it's working fine right now" (`1758546777.731809`) and the ZOM-429 owner note that a restart recovers the next week, which is exactly the T7 dependency.

Wording note: keeping "weekly leaderboard / leagues" **in** the text is deliberate. The difficulty being added is channel reconciliation (a solver who only sweeps `#zombie-bugs`, or who stops at the Sep 22 "working fine", misses the overwrite), not keyword concealment. A keyword sweep for `leaderboard` should return both records so the two can be ordered; that keeps the trap fair rather than a Where's-Waldo.

### Collision + ordering check (verbatim tool output)

Loaded `raw/slack_C0880U9751A_2025-09.json` (473 messages, Sep 2025 only):

```
C0880U9751A_2025-09.json exact ts hits: 0
same-second ts in file: []
max ts in file: 1759248267.162909
global raw hits across 44 files: []
newts UTC: 2025-09-30T20:50:12.481907+00:00
lo/iOS0.3.49 1759182908.627389 UTC: 2025-09-29T21:55:08.627389+00:00
seed bound 1759276800 UTC: 2025-10-01T00:00:00+00:00
after iOS release: True | before bound: True
```

Also checked: `grep -rl 1759265412 Task_Authoring/task_inputsS Task_Authoring/tools Universe_SynthCut/` → no files.

So `1759265412.481907` is free in that channel-month and across all 44 cached raw channel-months; it is 82 504 s (≈ 22 h 55 m) after the iOS 0.3.49 release (`1759182908.627389`, 2025-09-29 21:55:08Z), 2 223 s (37 m) after Android `Submission #135` (`1759263189.219529`, 2025-09-30 20:13:09Z — so "checked … submission #135" is chronologically true), and 11 388 s (3 h 10 m) before the seed bound.

Context of the slot — every base message in `C0880U9751A` from the 0.3.49 release to the seed bound (10 messages, none later than 16:04:27Z):

```
1759182908.627389 2025-09-29 21:55:08 EMPLOYEE_0038 | I just released 0.3.49 on IOS
1759187344.387499 2025-09-29 23:09:04 EMPLOYEE_0016 | <@EMPLOYEE_0025> Can I switch over to new Unity? Or wait?
1759189361.525409 2025-09-29 23:42:41 EMPLOYEE_0025 | we haven't merged it yet. I'll let you know
1759189388.874759 2025-09-29 23:43:08 EMPLOYEE_0025 | just install the latest version. Unity hub will automatically open ...
1759211437.306779 2025-09-30 05:50:37 EMPLOYEE_0016 | ... Unity is sending us a lot of bot installs or fake installs ... (rc=4)
1759236043.004679 2025-09-30 12:40:43 SLACK_BOT_0007 | (Linear status change, inside thread 1758142305.677109)
1759240715.635619 2025-09-30 13:58:35 EMPLOYEE_0008 | 1. Both platforms, or one more than the other? ...
1759248076.284779 2025-09-30 16:01:16 EMPLOYEE_0016 | Android
1759248130.580729 2025-09-30 16:02:10 EMPLOYEE_0016 | I didn't look at it by pubs.
1759248267.162909 2025-09-30 16:04:27 EMPLOYEE_0008 | We are only running the retention campaigns...
```

The new root therefore becomes the **most recent message in the channel** at the seed, which is correct (it is the current state of the beat) and also keeps it plainly visible on any recency-ordered channel read. Free window in this channel after the base data: `1759248268` – `1759276799`; recommended slot is the one above. Alternate if a sibling seed ever claims 20:50: `1759265573.118442` (2025-09-30 20:52:53Z).

### Julia visibility (verbatim)

```
julia_lawson slack C0880U9751A/1759211437.306779: YES
  reason:   message inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-match3d
  evidence: channel=C0880U9751A, name=zombie-match3d, kind=private, members=25, persona_slack_id=EMPLOYEE_0005_SLACK_ID, message=[ts 1759211437.306779 2025-09-30 user EMPLOYEE_0016_SLACK_ID]

julia_lawson slack C0880U9751A/1759182908.627389: YES
  reason:   message inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-match3d
  evidence: channel=C0880U9751A, name=zombie-match3d, kind=private, members=25, persona_slack_id=EMPLOYEE_0005_SLACK_ID, message=[ts 1759182908.627389 2025-09-29 user EMPLOYEE_0038_SLACK_ID]
```

Both checked on base records; the seeded root inherits the same channel membership (visibility is per-channel, not per-message). Julia is a member of `#zombie-match3d`, so the new root is visible.

### Knock-on edits this forces

1. Delete the seed at `C08R27X0EAH/1759266900.274551` (2025-09-30 20:35:00Z). Leaving it would put the same claim in two channels 15 minutes apart and re-create the same-channel supersede the reviewer flagged.
2. T7's `evidence_ids` / carrier pointer must change from a `#zombie-bugs` reply to **`C0880U9751A/1759265412.481907`**, and its "trap location" text from "reply under his own Sep 22 post" to "root in a different channel from the Sep 22 recovery".
3. `#zombie-bugs` loses its Sep 30 leagues record, so the Sep 22 chain there now ends at `1758546777.731809` ("…I am now in the weekly leaderboard…"), i.e. the channel's own tail says *fixed*. That is what makes the cross-channel read necessary — and it is the intended, fair difficulty.
4. `#zombie-match3d` has **no** base message in Sep 2025 carrying `leaderboard` or `league` (checked: zero hits in the 473-message channel-month), so the seeded root is the only leagues record in that channel and no decoy there competes with it. A global keyword sweep for `leaderboard` now returns exactly two records — the Sep 22 `#zombie-bugs` chain ("working fine right now") and this root — which the solver must order by channel and date.

## 2. Fault threads requiring per-thread reads

Three picks, one per independent beat, all **open at the seed** (no later record closes them — checked against `#builds` Sep 26–30 and every cached channel), all **Julia-visible**, none owned by T7 (leagues) or T10 (daily-gift frame / daily login). In each, the root is insufficient and the *last reply* is the decisive record; in all three the deciding reply carries **no beat keyword** (F2's tail does contain "shader" — diagnostic vocabulary, not a beat name — so it is reachable only by a non-beat search or by opening the thread).

| # | channel | root ts (UTC) | beat | rc | deciding last reply | consequence under R3 | covered by an existing trap? |
|---|---|---|---|---|---|---|---|
| **F1** | `#zombie-bugs` `C08R27X0EAH` | `1758903616.346579` · 2025-09-26 16:20Z | **Zombie Lane / Trophy Path** | 6 | `1758917074.996069` · Vincent Parker · "Can you trigger an ios build" | fix verified on **Android build 1977 only**; the iOS claim path was never built and never tested → **still-to-do** (iOS re-verification is a calendar item, and the claim path is R3's own predicate) | **No.** No trap touches Zombie Lane / Trophy Path |
| **F2** | `#zombie-bugs` `C08R27X0EAH` | `1759249488.495439` · 2025-09-30 17:42Z | **Season Pass** (gold-parts lightsweep shader) | 4 | `1759254162.721499` · Vincent Parker · "<@…0004> ı think [PERSON_NAME_0022] will handle the problem. It might be about the shader" | root cause found (Unity upgrade broke bone-deforming UI sprites), owner named, **no fix at seed** → **still-to-do**; a visible regression the team wants "squeezed in" | **No.** T8/T9 cover Season Pass *config-date* timing, a different decision and different evidence |
| **F3** | `#zombie-bugs` `C08R27X0EAH` | `1758145553.265559` · 2025-09-17 21:45Z | **Endless Monster Mode** (thermal/fps) | 8 | `1758152171.908029` · Robert · "If top is disabled.. why.." | the obvious explanation (HUD/animations) is eliminated in-thread and nothing follows → heating is **unexplained and unfixed**; endless stays a hold candidate on iOS, not a "reported once" note | **No.** No trap touches Endless mode |

### F1 — Zombie Lane / Trophy Path, `C08R27X0EAH/1758903616.346579`

Thread as seeded (6 replies, all Julia-visible):

```
1758903616.346579 Vincent Parker · rc=6
  After I skipped the zombie lane tutorial, ı got the exception and skipping couldn’t claim the ice cream.
1758913350.470119 Oliver Brooks  · sent a fix
1758913366.419089 Oliver Brooks  · android 1977, can you test it please?
1758913375.794899 Oliver Brooks  · I tested on my phone and its working
1758917016.015499 Vincent Parker · Thank you!
1758917022.439979 Vincent Parker · Checking it rn
1758917074.996069 Vincent Parker · Can you trigger an ios build      <-- deciding
```

Why the tail decides: the root is a **claim** failure ("skipping couldn't claim the ice cream") — literally the R3 predicate — and the three "sent a fix / 1977 / working" replies make it *look* closed. Only the last line shows the closure is Android-only. Nothing after 2025-09-26 20:04Z refers to this fix: sweeping every cached channel to the seed bound, the only later `ice cream` hit is an unrelated Sep 29 level-design note in `#zombie-design` (`1759171957.791499`, shuffling the ice-cream-bar level), the only `1977` hits are a GitHub comment id, and `#builds` carries no line for the skip-tutorial claim path. So the honest state at the seed is "claim path fixed and verified on Android, unverified on iOS" — which is a still-to-do, and a hold if the iOS build never gets tested before the calendar opens. A run that reads only the root writes "Zombie Lane broken at Sep 26"; a run that stops at "I tested on my phone and its working" writes "Zombie Lane fixed". Both are wrong, and a keyword sweep cannot fix either, because the tail is "Can you trigger an ios build".

### F2 — Season Pass shader, `C08R27X0EAH/1759249488.495439`

```
1759249488.495439 Vincent Parker · rc=4
  i think we should squeeze in the fix for that issue if it's an easy fix. annoying and players can see that for 10 times in a day if they make it that far.
1759250924.694619 Marcus Bennett · …them old shaders dont deform no more the sprites with bones, so i had There a lightSweep Box Variant material that has a shader that used to work before now it doesnt deform the mesh no more :disappointed:.
1759250986.434259 Marcus Bennett · solution would be to fix the shader to include deformabile ui sprites some how, or just get rid of it and we dont have any lightsweep across the gold parts, it will be more dull but its gona be a quicker fix!
1759254098.279269 Oliver Brooks  · will work on this asap
1759254162.721499 Vincent Parker · <@…0004> ı think [PERSON_NAME_0022] will handle the problem. It might be about the shader   <-- deciding
```

Why the tail decides: the **root names no beat at all** ("that issue", "the fix for that issue") and the last reply names a *person*, not an outcome. Neither root nor tail carries a beat keyword, so the record is invisible to any `season pass` / `pass` / gold-parts sweep — the tail's only searchable word is "shader", which is not a beat name, so it is reachable in practice only by opening a thread under a root that itself does not say what it is about (a channel read of `#zombie-bugs` for Sep 30 is the realistic route). Consequence: a real beta regression (Unity upgrade → bone-deforming UI sprites lose their material) with a diagnosis, two candidate fixes and an owner, but **zero fix by the seed**. Under R3 this is still-to-do, and it is the one record that says the Unity upgrade has a *class* of shader breakage, not a one-off.

### F3 — Endless heating, `C08R27X0EAH/1758145553.265559`

```
1758145553.265559 Leonard Hayes · rc=8
  I let endless level to run for 5 mins+ and my phone is burning right now. I’m not as sure as you guys are about the zombie animation performance based on what I’ve observed
1758146194.755589 Robert        · This is with the animation disabled right? the top part gone?
1758146356.287679 Vincent Parker· Yes i also experienced the same thing on ios.
1758147450.401459 Leonard Hayes · yup, top part disabled
1758147472.006259 Leonard Hayes · I mean I can still see health bars and mini-maps
1758147477.260509 Leonard Hayes · but no zombie animation
1758147510.451039 Leonard Hayes · when I hit air strike at the 7th minute with 50+ invisible zombies fps dropped to 10
1758152164.648419 Robert        · That's weird
1758152171.908029 Robert        · If top is disabled.. why..      <-- deciding
```

Why the tail decides: the root reads as "one tester's phone got hot". The replies are what make it a defect: reproduced on iOS by Vincent, with the top HUD and all zombie animation disabled, still ≥ 50 zombies and fps 10 at minute 7 — and the thread ends on the question nobody answers. Nothing later in `#builds` or any channel addresses heating (the only endless-adjacent later line is "Infinite/endless analytics, balance changes (#451)" and "removing popup tutorial from level model endless_02", neither of which is a perf fix). Consequence: endless is a **hold candidate** on thermal grounds, and the honest write-up is "unexplained thermal/fps defect, mitigation attempts disproved" — a materially different calendar decision from "no open endless issues".

### Why these three and not the obvious neighbours

- **`C08R27X0EAH/1758905363.341129` (R-B §1 #16, Season Pass memory/addressables, rc=25)** looks like the best candidate — 25 replies, tail "maybe it'll do the spell we need" — but it is **superseded before the seed**: `#builds` `1759247404.098179` merges `#473 addressables/sp` and `1759247779.842079` runs "setting addressables for season pass objects" on 2025-09-30 15:50–15:56Z. Its tail is *not* the outcome (same failure mode as the claim-SFX thread). Do not use it as an R3 decider; it is a good "thread tail ≠ truth" trap instead.
- **`C0880U9751A/1758062348.988239` (R-B §1 #18, endless instrumentation, rc=14)** ends "let me check and get back to you", but `#builds` `1758121241.121539` (2025-09-17 15:00Z) ships "Infinite/endless analytics, balance changes (#451)" the next day. Superseded — exclude.
- **`C08R27X0EAH/1757999990.759409` (R-B §1 #6, season-pass claim SFX)** ends "will add first thing in the morning"; the fix is in `Submission #122` (`1758111759.933039`). Superseded — exclude (already R-B §5 item G).
- **`C08R27X0EAH/1758130096.275899` (R-B §1 #9, daily login reset)** is open and Julia-visible but its last reply contains the keyword "daily", so a sweep finds it without opening the thread — it adds no forced read, and it is the same beat family as T10.
- Beats with **no** reply-bearing fault thread in the window: **Plague Race**, **Collect & Win**, **quests rollover** (its two rc>0 roots are the animation thread above and a design agreement `1759176983.189479` — neither reports a rollover fault), and **daily login** beyond #9.

## 3. Necessary-read count for R3

### Rule used

A thread counts only if all four hold: (a) the beat is in scope; (b) it is **open at the seed** — no later record closes it; (c) the record that decides its status is a **thread reply**, not the root (so channel history alone shows only a first line); (d) that deciding reply carries **no beat keyword**, so a keyword sweep over replies returns nothing. Under (c)+(d) the only route is to open the thread.

### The seven necessary thread reads

| # | channel | root ts | beat | deciding reply | state at seed |
|---|---|---|---|---|---|
| 1 | `#zombie-bugs` | `1757999557.589779` | quests (animation blocker) | `1758004594.680929` Calvin Price · "I sent a PR, is not merged yet" | open — no merge ever confirmed for the animation PR; later quest lines are a different bug (`Fix KeyNotFoundException in QuestsMainScreen`) |
| 2 | `#zombie-bugs` | `1758145553.265559` | endless (thermal) | `1758152171.908029` Robert · "If top is disabled.. why.." | open — unexplained, unfixed (F3) |
| 3 | `#zombie-bugs` | `1758903616.346579` | zombie lane / trophy path | `1758917074.996069` Vincent · "Can you trigger an ios build" | open on iOS (F1) |
| 4 | `#zombie-bugs` | `1759249488.495439` | season pass (shader) | `1759254162.721499` Vincent · "…will handle the problem. It might be about the shader" | open, owner named, no fix (F2) |
| 5 | `#zombie-match3d` | `1758130794.208109` | endless (perf/#1643) | `1758139113.585359` Vincent · "…after playing endless mode my device starts to heat up similar to earlier" | open — the animation-disable mitigation tested and **disproved** |
| 6 | `#zombie-bugs` | `1757939514.864549` | multi (quests claim, reward anim, premium pass price, leaderboard frame) | `1757947882.581049` Martin Walsh (EMPLOYEE_0033) · "Needs to be like this: image.png image.png" | open — 11 issue replies, no fix confirmed; root ("here is the list of issues that will be part of submission today") and tail are keyword-free, so the in-scope sub-issues are invisible to a sweep |
| 7 | `#zombie-bugs` | `1758031982.956109` | multi (premium-pass lives reset, zombie-lane card rewards invisible, chest reward screen, refill 5 vs 8, season-pass trampoline timer) | `1758032834.666619` Vincent · "• Boss arena reward screen shows x2 label which should be removed." | open — 6 sub-bugs posted, none confirmed fixed; root "Remaining Issues Based on latest builds" carries no beat keyword at all |

**Count: 7 necessary thread reads** (of the 14 threads with replies in R-B §1). They cover every in-scope beat that has any unresolved thread-decided fault: quests, endless, Zombie Lane/Trophy Path, Season Pass — plus the two submission-day bundles (rows 6–7) that carry otherwise-unconfirmed quests / season-pass / zombie-lane sub-issues.

Strictness note: if the parent wants the *minimum* rather than the honest surface, drop row 5 (a second endless thread — row 2 alone already fixes endless's status, row 5 only adds that the #1643 mitigation failed) and the count is **6**. Rows 6–7 can only be dropped if the calendar is allowed to assert "nothing else on the submission lists was left open", which the evidence does not support. I recommend budgeting **7**.

### Explicitly excluded (and why) — do not add these to the budget as facts

| thread | exclusion |
|---|---|
| `C08R27X0EAH/1758546119.789009` (leagues Sep 22) | superseded by the relocated T7 root; the beat's status is set by a **root**, not a thread reply |
| `C08R27X0EAH/1758905363.341129` (R-B #16, season pass addressables) | superseded by `#builds` `1759247404`/`1759247779` (PR #473 merge, 2025-09-30) |
| `C08R27X0EAH/1757999990.759409` (R-B #6, claim SFX) | superseded by `Submission #122` (`1758111759.933039`) |
| `C0880U9751A/1758062348.988239` (R-B #18, endless analytics) | superseded by `#builds` `1758121241` ("Infinite/endless analytics … (#451)") |
| `C08R27X0EAH/1758130096.275899` (R-B #9, daily login) | deciding reply contains "daily" → keyword-findable |
| `C08R27X0EAH/1758082051.562129`, `1759176983.189479` (R-B #20, #24) | decisions (defer / agree), not faults |
| 10 rc=0 roots (R-B #2 #3 #5 #7 #11 #12 #14 #21 #22 #23) | no thread exists; 1 channel-history call each, no thread read |

### Budget effect

- **+7 reads** for the fault threads above (one thread read each).
- **+1 read** to find the relocated leagues re-test: a channel-history read of `C0880U9751A` covering Sep 29–30, or a second `search leaderboard` pass with the channel filter widened — the record is a **root**, so it needs no thread read.
- Total added surface ≈ **8 reads** (~1.3 % of a 600-call plan). What it buys is that four in-scope beats (quests, endless, Zombie Lane, Season Pass) are stated at their true seed state instead of the state their thread roots imply — and the weekly-leagues hold is derivable only by crossing two channels.

Julia visibility spot-check (verbatim, base records; seeded records inherit the same channel membership):

```
julia_lawson slack C08R27X0EAH/1758903616.346579: YES   (member of private zombie-bugs, 23 members)
julia_lawson slack C08R27X0EAH/1758917074.996069: YES   (thread reply inherits channel)
julia_lawson slack C08R27X0EAH/1759249488.495439: YES
julia_lawson slack C08R27X0EAH/1759254162.721499: YES   (thread reply inherits channel)
julia_lawson slack C08R27X0EAH/1758145553.265559: YES
julia_lawson slack C08R27X0EAH/1758152171.908029: YES   (thread reply inherits channel)
julia_lawson slack C08R27X0EAH/1757999557.589779: YES
julia_lawson slack C08R27X0EAH/1758031982.956109: YES
julia_lawson slack C08R27X0EAH/1757939514.864549: YES
julia_lawson slack C0880U9751A/1758130794.208109: YES
```
