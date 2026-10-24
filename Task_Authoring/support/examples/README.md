# support/examples/ — engine test runs

Each folder is a run of `/create-scenario` → `/create-injection` on a test assignment,
kept to show what the engine produces and to regression-test the playbooks and tools.
They are **not platform tasks**. Do not copy a cohort, rule vocabulary or record set
from here into a real task (originality, `playbooks/01_Scenario_Design.md` S1). They
contain no prompt, Oracle Event or criterion text (GEN_EXECUTION §2).

## sample_task_01 — known-defects schedule for the IP sale (Arthur Blake · Engineering Ops · Long Horizon)

Two iterations of `/create-scenario` → `/create-injection` by a fresh agent following only the
playbooks (Oct 3–4 2026).

- Iteration 1: 12 services, 120 rows, 22 traps, 4 hidden authorities — but **321** necessary
  calls; the agent refused to pad. Led to `Hardness_Mastery.md` §2.5 (seeded per-record
  surfaces under a necessity rule) and the stricter gate.
- Iteration 2: a seeded two-platform pre-sale retest (69 Slack triage threads + 67 Linear
  comments) decides which rows count. `sql_lint` 0 errors; `hardness_gate` PASS (design and
  SQL): 551 necessary calls, per-record 417, 320 INSERTs over 12 schemas, 28 traps / 11
  families, 8 independent chains.
- Open before any platform use: the Android half lives in Linear comments, which have no base
  precedent — confirm in the Opus pre-check that `linear_list_comments` returns them; ~150
  budgeted calls depend on unverified tool behaviour (floor ≈ 400 if both resolve to bulk).
- Iteration 3 (after the red team, `01b_Redteam_Review.md`): every finding fixed or
  accepted; honest budget fell to 386, with 290 calls conditional on four unverified tool
  behaviours.
- Those four were then measured on ~6,000 recorded calls in 277 V1 Opus trajectories
  (`references/Ask_Carriers.md` §6b): Slack search returns replies (sweepable); Linear list
  returns parents; injected Linear comments render with no bulk path; PR search does not index
  comments.
- Iteration 4 (verified behaviour only): **honest budget 190**, 0 conditional rows; the gate
  fails on volume by design. The cohort (73 open defects) is too small; ≥ 500 needs ≈ 225
  issues + 225 candidate PRs with comment facts (`Hardness_Mastery.md` §2.5 sizing rule).
  Kept as the reference case for the sizing rule, not as a passing example.
- **Later finding (iteration 5):** the GitHub Slack app mirrors PR comments into `#engineering-bots`
  / `#zombie-prs`, so sample_task_01's 73 per-PR reads sweep for ~15–20 calls — its honest total is
  ~135. Its 13 seeded PR comments also lack their Slack copies, so its SQL is **not injectable
  as is** (reference case only).

## sample_task_02 — strict-500 attempt (iteration 5, blocked → iteration 6)

Widened to 277 issues (67 open bugs + 210 Done tickets with release-audit notes) and 253
candidate PRs. Blocked: PR comments are mirrored to Slack, so only Linear comments are
per-record, and the 50 % share cap held Linear back (honest 386). The cap now applies outside
the per-record phase only (`Hardness_Mastery.md` §2.5 sizing rule).
- **Iteration 6 — PASS.** 499-record cohort (67 open defects with two-platform retests + 424
  Done tickets since 2025-06-01 with release-audit notes; 80 May tickets also noted so a note
  reveals nothing). Flip rate ~19 % (ROLLED BACK / NOT RELEASED), uncorrelated with ticket
  fields. **565 honest necessary calls, 0 conditional**; 491 per-record Linear comment reads;
  PR comments budgeted as a Slack sweep of their mirror copies; 778 INSERTs (1,364 rows) over
  12 schemas; 28 traps, 10 chains, 5 hidden authorities. `sql_lint` 0 errors; `hardness_gate`
  PASS (design + SQL), verified independently. Known realism gap: all 504 notes are by the
  persona in ~16 h — spread authorship next time (`Hardness_Mastery.md` §2.5 realism rule).
- **Red team on iteration 6** (`sample_task_02/01b_Redteam_Review.md`): the 491 Linear reads
  are plausibly necessary, but (1) the change-list requirement has no delegation edge in any
  record — 424 of the 565 calls rest on an unauthorized ask; (2) release notes state the
  classification in prose, so the volume is transcription; (3) cross-service decoys do not
  compete with targeted searches; (4) hand-typed dossier totals drift from the generator.
  All four are now engine rules (`Hardness_Mastery.md` §2.6 items 11–14) and the gate requires
  `delegated_by_record` per fragment and ≥ 1 same-service decoy — **both examples now fail the
  stricter gate** until rebuilt.
