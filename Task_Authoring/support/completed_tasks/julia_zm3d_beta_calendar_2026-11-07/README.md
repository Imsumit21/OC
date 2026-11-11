# Julia: ZM3D beta live-ops calendar (archived 2026-11-07, not completed)

Persona Julia Lawson (Product Manager) · Long Horizon · Product / Marketing and GTM / Planning and decision support · difficulty mode medium (cap < 85%) · universe date Oct 1, 2025 (synth-cut, clock 2025-10-01 00:00 PT) · platform attempt 6aea4c1e9b621f28dc3a5332.

Prompt (2 paragraphs, 513 bytes): take on Frederick's live-ops and push calendar for the Zombie Match 3D beta, the four buy weeks from Monday the 6th, built from his message and his brief, in Julia's calendar sheet; leave a note on the ticket of any held beat; link the sheet on the calendar ticket and send Frederick the recommendation.

**This task never passed /prompt.** The author reported it moved on 2026-11-07 because it could not be completed. It is kept for its failure history, not as a finished slot. No run, Oracle Event, rubric or baseline exists. Every pass rate below is a forecast.

## Final state

| Slot | State |
|---|---|
| `01_Universe_Inject.sql` | rev14, sha256 edae63f3e838, 111 statements (81 INSERT, 30 UPDATE). The platform last reviewed rev8; rev9 to rev14 were only reviewed locally |
| `04_Prompt.txt` | sha256 2a23afd87c4c, unchanged since platform /prompt round 2 |
| Platform /injection | 4 reports: FAIL, then PASS three times. The last PASS is on rev8 |
| Platform /prompt | 3 reports on disk, all FAIL 2. The author counted four failed rounds, so one report may not have been saved |
| /hardness, /oe, /rubric | Never run |
| Local /injection on rev14 | PASS / COMPLETE, no demonstrated defects. Not a platform result |
| Local /prompt on rev14 | PASS 5, all 18 dimensions 5, Originality N/A; cold P1 pass found no forks in 34 candidates. Not a platform result |
| `06_PreCheck_Trajectory/`, `07_Baseline_Trajectories/` | README only: no run exists |
| `05`, `08`, `09`, `10`, `11_AF` | Empty |
| `03_Error_Async_Config.txt` | Friction: none. Its text is stale: it cites call budget 208 and a 47-member cohort; the final manifest has 164 planned (154 counted) and 41 |
| Stage gates | `Working_Files/research/REPASTE_STEPS_rev14.md` was never run, so the pasted gate blocks do not cover rev14. `hardness_gate` fails on 4 lines on the Mac whose tools lag (no `volume_exception.rows_floor`) |

## Platform rounds

| Round | SQL | Result | What it found |
|---|---|---|---|
| /injection r1 | 7112c82b | FAIL | "Fri Oct 29" in 12 Gmail rows, doc `style_runs` offsets, `#470#rc_10` with no review of its own |
| /injection r2 | 25070fda | PASS | |
| /prompt r1 | rev1 4c6328ab | FAIL 2 | UGT, Clarity and Contrived at 2: seven forks led by the push plan, and a per-row field list in the prompt. Prompt rewritten after this |
| /injection r3 | rev2 3afbf7cb | PASS | |
| /prompt r2 | rev2 3afbf7cb | FAIL 2 | Cross-Service Coherence 2: ZOM-521 ticks token travel while ZOM-526 is In Progress (known issue SC-15). UGT passed |
| /injection r4 | rev8 0e8c8ad8 | PASS | |
| /prompt r3 | rev8 0e8c8ad8 | FAIL 2 | UGT and Clarity: the ZOM-534 fix (on main or on prod), Leonard's S23 freeze under the brief's unverified-platform clause, the #477 header title change |

## Local revisions

Each is a text transform with asserted anchors; the docstrings in `work/julia_zm3d_beta_calendar/scripts/apply_review_fix_rev*.py` give the detail.

| Rev | Why |
|---|---|
| rev3 | SC-15 repair on ZOM-521 and ZOM-526 |
| rev4 | Coherence: notes moved off long-merged PRs, six ticket states, threading, bot mirrors |
| rev5 | Claim-by-claim audit of every injected record against the base |
| rev6, rev7 | Oct 13 quest set fork and two wording residuals |
| rev8 | Blind round: two P1 forks, four P2 low-impact items. This is the last revision the platform saw |
| rev9 | Root-cause fix after /prompt r3: census of about 90 candidates, still-to-do rule closed |
| rev10 | Six agents attacked rev9 before review and tested 200+ candidates; the new rule text was reworded |
| rev11 to rev14 | Formal and cold rounds: Collect & Win icon settled by the list owner, window closes stated once, Trello payload restored, passive "its owner is told" made active |

## Key answers

Do not reuse these (originality). Answer key: `task_inputs/Working_Files/solver/truth.json`, sha256 7bef2209a351.

- **Beats (7):** Plague Race, Collect & Win, Season Pass, Endless Monster Mode, Weekly Leagues, Quests, Daily Login. Boss Arena is off until the pivot call; the rotating shop is not a beat.
- **Held:** only Weekly Leagues, on the weekly reset (Douglas), until the fix is confirmed on prod. No date is given.
- **Starts late:** Collect & Win, first window Fri Oct 10 00:00 UTC, 10 windows, because the Oct 8 backend release lands after the Wed window opens.
- **Season Pass:** first window Mon Oct 6 00:00 UTC. Brian's November config date, Oct 31 10:00 Istanbul, is about 7 hours past the Oct 31 00:00 UTC lock.
- **Still to do:** Collect & Win: final vial models (Claire), event icon animation (Marcus), server windows to prod (Douglas). Season Pass: premium strip to the November range (Oliver), November config before the lock.
- **One-off:** Robert approved the themed prop set, then withdrew it, so it is off the calendar.
- **Pushes (10 lines):** send Lives recharged and 7-day lapse, hold the other 8, each with what its row is missing.
- **Writes:** the calendar and pushes in Julia's sheet, a note on ZOM-429, the link on ZOM-78, a reply on Brian's Sep 26 mail, the recommendation in DM D05SD5QLG94.

## Difficulty (forecast only, no run exists)

| Measure | Value |
|---|---|
| Verifier pass rate | About 76%, range 70 to 83. Under 85: about 95%. Under 80: about 75%. Under 70: about 10% |
| Spread | SD about 0.075, likely under the 0.1 floor |
| Calls per run | Median about 130, range about 92 to 210. Six-run average about 140. Every run at 130+: under 5% |
| Design forecast | E[avg] 0.614 [0.503, 0.722]; solver 0.808 [0.739, 0.876]. Uncalibrated, and it does not see record text |
| Manifest | 30 slots, weight 102, cohort 41, 111 statements, call budget 154 of 164 |

So the design goal of under 70% and 130+ calls in every run was not met even on paper. Detail: `task_inputs/Working_Files/research/prompt_review_rev14/difficulty.md`.

## Lessons carried forward

- **Design a closed answer set from the start.** Fourteen SQL revisions never reached a baseline. The brief's "what still has to land" was an open set, and a census found about 90 candidates, so one settling record per item could never converge. A closed rule with a tail ("anything flagged since this brief as still needed for it (...). Nothing else goes in") plus a date cutoff did converge locally.
- **Delete any clause no truth value depends on.** "An unverified build or platform is a still-to-do" fed no answer and produced six forks. Check every rule sentence against the answer key before the first review.
- **Patch the class, not the last list.** Each platform round found something new. The clause and the ZOM-534 note that failed UGT in /prompt r3 were already in rev1 and rev2, and /prompt r2 passed UGT on them. A passed dimension is not clearance for the next round.
- **After two /prompt failures on one family, redesign.** This is a judgement from this history, not a measured rule: rev3 to rev8 patched items; only rev9 fixed the rule, and by then the brief was heavily patched.
- **Local PASS does not predict the platform.** The local bundle lacks `ugt-fork-v1`, `base-data-v1` and the known-issue list. Those rules are visible only through platform reports, so do not state them as Eval text. The local review waved forks through as "closest calls" and the platform then failed them.
- **The fork bar:** reject a fork only with a quoted, persona-visible record that rules out the other reading. "Weak", "additive" and "superset" are not grounds. An owner's own claim does not settle its own gap (`SCOPE_GAP`), so use the reporter, flagger or list owner: Leonard on ZOM-534, Vincent on the shader, Brian on the icon. No record at all is `SILENCE`.
- **Census whole channels.** Keyword searches missed the S23 report in #zombie-bugs. The window from brief date to clock is short enough to read completely, which proves the set instead of sampling it.
- **Every new sentence is a fork risk, so attack it before installing it.** "Not done since this brief" had a second parse. "Douglas's teams update" exposed a prod update. "Remote device list" clashed with the cancelled BrowserStack. "First-pass models" clashed with Claire's Aug 14 revision. "Pre-empts" read backwards.
- **Keep rule words neutral.** "Reviewer", "PR", "ticket" or "re-test" in a rule point runs at the carrier and cost difficulty. A passive ("flagged") avoids that, but a passive on who acts is a fork: "its owner is told" became "you tell its owner".
- **Cold reviewers are the bar.** Resumed reviewers confirm their own list and give cheap deltas; fresh blind P1 and P2 passes found new items in rounds where the resumed ones found none.
- **Audit claims against the whole base,** including private notes and git: POD notes, BrowserStack, LFS art, merged-PR timing, ticket state against comments. Rev5 exists because records looked right and the base said otherwise.
- **Notes on merged PRs count as activity on closed records.** Place them on a live record, or under a base approval just before the merge.
- **Keep the exact platform-accepted record shape.** Dropping `list` from the Trello payload created rare and then zero-match key sets; rev13 restored the accepted shape, which matches 14 base rows.
- **Moving a graded record has a call cost.** Taking the note off PR conversation comments in rev8 left 39 calls returning nothing a rule uses, because the base comments on those PRs are all bots. Re-run the necessity count after any move.
- **Patches raise the planted look.** Rev14's extended P4 test (unscored) listed 24 open items: 4 HIGH, 12 MED, 8 LOW. "Has to land" sat in 7 comments by 4 authors. Vary settling records across authors and wording.
- **Every clarifying sentence also costs difficulty.** The brief settles cells a run would otherwise explore, and forks are closed by giving facts away. The levers that added some back: de-naming Robert's withdrawal, dropping "only" from the push copy sentence, moving the Collect & Win cadence to the Span section, deleting "pre-empts".
- **Few writes means no honest route to 130+ calls in every run.** There are only four write kinds here, and the floor needed a volume exception (calls 130, per-record 75, rows 70, cohort 40). Build necessary reads into the design, not into a later exception.
- **Tooling on this Mac:** `hg_store_input.py` writes are denied and `Evals/task_inputs/` can hold another session's task, so review from a scratch copy; use `~/.local/bin/python3.12 -B`; `search-many` rejects a `service` key; zsh does not split a command held in a variable. Asserted-anchor text transforms kept 12 revisions safe, so keep that pattern.

## Layout

`task_inputs/` is the slot as last worked, with two omissions: `plateform_reports/` (now `eval_reports/`) and the 10 raw dumps over 1 MB in `Working_Files/research/raw/` (93.6 MB of base-export copies, which can be regenerated). `Working_Files/run_forensics/rev1` to `rev13` hold every earlier SQL, prompt and truth. `Working_Files/research/prompt_review_rev*/` holds each local review, `rev9_census/` and `rev9_attack/` the census and the attack. `eval_reports/` holds every platform report on disk, renamed by stage, verdict and round. `work/julia_zm3d_beta_calendar/` holds the revision transforms, `build_manifest.py`, `build_surface.py` and the solver.
