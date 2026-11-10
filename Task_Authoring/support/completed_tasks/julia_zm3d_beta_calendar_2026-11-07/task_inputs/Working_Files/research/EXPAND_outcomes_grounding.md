# EXPAND: outcome grounding for the 6 candidate reconciliations

Clock 2025-10-01 00:00 PT (07:00Z) · synth-cut · Julia Lawson. Build persisted this from the grounding worker's
final report (worker ran out of steps before writing the bodies). Every record below verified against base.

Governing rules: **R3** a beat is HELD only on a provable enter/score/claim failure even after a restart; cosmetic /
VFX / performance / analytics / unverified-platform / infra = still-to-do, never a hold. **R5** still-to-do = what a
beat needs before it runs for bought users (prod deploy, config, owner-flagged player-facing art), NOT shipped work,
analytics/telemetry, known issues or unflagged polish.

Fixed slots a new slot must not contradict: S02 Plague Race RUNS · S03 Leagues HELD · S04 Quests RUN · S05 Daily
Login RUN · C01-C05 all RUN · S06 Quests todo=new set Oct 13 · **S07 Daily Login todo = NOTHING LEFT** · S08 C&W
todo=vials · S09 SP todo=premium strip · S10 SP todo=Nov config · S11 C&W todo=icon.

## Verdicts

**R1 queue-coverage** — ZOM-543 (Queue Manager, In Progress, Calvin, "orchestrate panels… we'll add its order")
+ #459 ("queue manager for level_end/daily_gift/season_pass/tutorial") + #472 ("Implement Win&Collect into Queue
Manager", merged 09-30 15:53Z). The queue is an **animation/ordering** orchestrator, additive per beat; an un-queued
panel is a STILL-TO-DO (wire the order), **NOT a hold** — nothing shows players cannot enter/score/claim. No conflict
with S02/C02/C03. BUT not uniquely assignable to one beat row → **use as an over-application distractor, not a graded
column.**

**R2 tokens-to-live-ops** — ZOM-526 (child, In Progress, no assignee, "tokens… implement together with season pass
and collect&win"); ZOM-521 parent all-ticked (SC-15 bars grading the parent checklist); #408/#468 partially shipped
the token path. Honest state = still-to-do on SP+C&W — but those rows already carry S08/S09/S10/S11. **DROP as a slot;
keep as an over-application distractor.**

**R3 C&W idle-icon** — ZOM-465 master VFX ticket struck "Idle Icon Animation **for all event icons**" as done; #454
("Animated icons… Quests, Season Pass, Endless, Zombie Lane, Plague Race" — no C&W), #456 (enumerates the same six
icons, no C&W), #475 ("card pack animation", not an event icon). Correct answer = **C&W icon animation still to do**,
consistent with S11, NOT held. Multi-source (master ticket vs three PRs). **UPGRADE S11 weight 3 → 5 (safe).**

**R4 addressables SP-only** — #473 ("Addressables/sp", merged 09-30 15:41Z, **zero reviews**, SP screens only) +
Arthur `C08R27X0EAH/1758905363` ("create linear tasks to move **each** liveops feature to Addressables… I'll start
moving season pass soon"); NO addressables ZOM issue exists (searched all 553). Infra still-to-do (create the non-SP
migration tasks), **NOT a hold** (addressables is a load-time optimization, R3-excluded). Not a per-beat value →
**over-application distractor, not a graded column.**

**R11 C&W telemetry + name** — ZOM-566 (Todo, "Analytic logs for collect&win"); #477 open (SC-18 bars grading its
state). Confluence: C&W "**is the same feature as Win & Collect on Domino Delights, under a different name**". (i)
telemetry = analytics, R5-excluded → not gradeable. (ii) the "Win & Collect" label is a documented naming convention,
not an old-title defect. **DROP** (existing distractor D5 already covers the push-copy angle).

**R13 login persistence** — ZOM-544 (Implement Google/Apple Login, In Progress, Blake, lists SP/ZL/league/quest
progression to store) + Julia `C05KNDCHAAG/1758558302` ("he's working on Apple/Google login") + ZOM-563 (prod team
data bug, a different feature; SC-16 bars its Linear status). Login = pre-beta account framework; under R3 it does not
stop play, under R5 it is cross-beat foundation not a per-beat flagged item. Any still-to-do it yields lands on Daily
Login (contradicts S07) or SP/C&W/ZL (collides S08-S11). **DROP as a slot; keep as the S07 over-still-to-do
distractor.**

## Decision

| cand | correct outcome | action |
|---|---|---|
| R1 queue | all beats RUN; panel-order is a still-to-do, not a hold | over-application distractor D10 → R_INFRA_SCOPE |
| R2 tokens | SP/C&W token travel partly shipped; child open | over-application distractor D12 → R_INFRA_SCOPE |
| R3 icon | C&W icon animation still to do (multi-PR) | **UPGRADE S11 3→5**, mechanism R_ICON_SCOPE |
| R4 addressables | non-SP migration tasks outstanding; no hold | over-application distractor D11 → R_INFRA_SCOPE |
| R11 telem/name | not gradeable (analytics + naming convention) | **DROP** (D5 covers the push copy) |
| R13 login | pre-beta infra, not a per-beat still-to-do | **DROP as slot**; feeds the S07 over-still-to-do distractor |

Net: **1 genuine weight-5 upgrade (S11 icon)** + **1 new over-application mechanism R_INFRA_SCOPE** (infra-gap twin of
the fault-thread R_HOLD_SCOPE) fed by distractors D10/D11/D12, flipping C01/C05 (runs) and S07 (nothing-left). The
other 11 cohort reconciliations make the 48-member reads decision-bearing (retrieval difficulty) without manufacturing
graded columns.
