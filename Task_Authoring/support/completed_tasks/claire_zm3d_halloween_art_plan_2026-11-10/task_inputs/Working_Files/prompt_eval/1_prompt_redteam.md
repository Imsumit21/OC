# /prompt — GPT red-team emulation · claire-zm3d-halloween-art-plan

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

- Prompt: `04_Prompt.txt` · 125 words · sha256 prefix `63d7c0713c3b`
- Injection overlay: `01_Universe_Inject.sql` · sha256 prefix `29bc98c6e28b` · 217 INSERT, 3 UPDATE (local static checks only; platform `/injection` not yet run on this hash)
- Friction: none (`03_Error_Async_Config.txt`) · no reference files · no comparison samples (Originality N/A)
- Evaluator: GPT-6.1 Sol (`redteam` subagents), read-only emulation of `Evals/1_Prompt_Eval.md` (task-quality-v1). Not a platform gate receipt.
- Evidence: `Working_Files/prompt_eval/evidence_pack.md` (verbatim SQL rows and base records with SQL line / file + JSON pointer; no answer key), built by `build_evidence_pack.py`; reviewers spot-checked raw sources.

## FINAL VERDICT: PASS — score 5 (all applicable dimensions 5)

| Dimension | Score |
| --- | --- |
| Persona | 5 |
| Business Function | 5 |
| Assigned Competency | 5 |
| Assigned Task Skill | 5 |
| Complexity Dimensions & Data Seeding | 5 (Ambiguity, Dynamic Change, Multi-Source all load-bearing) |
| Command List / Bolt-on / Pre-solving / Explicit Tool Mention | 5 / 5 / 5 / 5 |
| Unique Ground Truth | 5 |
| Feasibility | 5 |
| Persona ACL Reachability | 5 |
| Truthfulness | 5 |
| Tool Use & Cross-Service | 5 |
| Investigation + Action | 5 |
| Clarity & Specificity | 5 |
| Contrived / Unnatural | 5 (0/4 spec-sheet triggers; 0 search hits) |
| Alignment with Today's Date | 5 |
| Originality | N/A (no samples supplied) |
| Universe Data Exists | 5 |
| Cross-Service Coherence | 5 (after fix 4 below) |

Evidence limits (as stated by the reviewers): static review of the proposed base + overlay state; SQL never executed; platform `/injection`, release/hash binding and runtime write effects (e.g. the commenter role value of the share call) not exercised; the deep-recheck passes are emulated by separate GPT passes, not platform Phase 5.

## Rounds and findings

| Round | Pass | Verdict | Finding | Disposition |
| --- | --- | --- | --- | --- |
| 1 | main (Phases 1–4) | NON-FAIL, PARTIAL (no command access, steps exhausted) | open item: ART-809's master note points to Frederick's Aug 13 thread `C06DJBJL798/1755114007.441789`, where the 30 s cut's music is baked in but Marcus posted no-music exports in the same thread — Refresh first vs Halloween version both arguable | fixed (PW3): Robert's deck `f_5ebf55ad29e815d46243c8` slide 2 now reads "re-cut first from a master without music (re-export one from the project if there is none)", slide 4 "Refresh first: re-capture, re-render or re-cut before any seasonal pass"; round-2 P1 confirms Refresh first is unique; solver truth unchanged |
| 1 | P1+P3 blind | partial, no confirmed finding | reconstruction matched the answer key on 57 of 58 ads; the one difference was ART-809 (thread unread) | closed by the PW3 fix |
| 1 | P2+P4 blind | FAIL (DR1) | "Then comment each ad's call…" — a common_errors §3 search hit ("First / Then / Finally: a hit fails") | fixed: prompt v2 drops "Then" ("Comment each ad's call and due date on its ART ticket, …"); v1 kept as `Working_Files/scratch/04_Prompt.v1.txt` |
| 2 | P2–P4 blind (evidence pack) | PASS | none — 15 attack groups (capability, ACL, discovery, cohort mapping, campaign names, Sep 8 vs Sep 9, store files, mail / calendar copies, Trello counters, Linear stamps, Slack counters incl. the base-parent UPDATE, apostrophes, wording) | — |
| 2 | P1 UGT blind (evidence pack) | PASS | none — 62 serving items + 4 archived checked one by one; 16 Halloween version / 34 Refresh first / 4 Reuse / 8 Skip; 58 comments, 48 assignments; Google Play set: an Oct 21 hand-off for the Oct 22 store window proposed as a fair planning choice | acceptance widened: brief §4b and the sidecar outcome reviews accept any October Play date that leaves the 1-day review (no prompt change) |
| 2 | main (evidence pack) | FAIL, score 1 | Cross-Service Coherence: base ART-792 `time_in_status_minutes` 246277 exceeds its lifetime at the clock (created 2025-08-26T18:57:06Z = 51,123 min); known data issue SC-22 | fixed (PW4): `UPDATE linear.linear_issues SET time_in_status_minutes = NULL WHERE id = 'ART-792'` (SQL L165), like ART-774 / ART-790; updated_at untouched |
| 3 | main, follow-up | PASS, score 5 | fix confirmed; attacks on the repair (schema nullability, state, chronology, task purpose, predicate scope, concealed answer) all failed; 34 base Slack messages and 42 #builds posts on the path rechecked, no other past-clock or self-contradicting value; reviewer withdrew the clock-bound reading for other SC-22 records (Eval 0 Check C L240–244: a cached duration need not be measured at the clock) | — |

## Settled forks (UGT), with the record that settles each

- Sheet as the whole scope → Frederick's Trello comment `68dc65a0f2d7fb28743f5860` (Julia's 4:5 static, "count it in") and his note `cmt_art831_2` (end card "Not on the live creatives sheet yet").
- Archived creatives → the sheet's Read me ("Paused or retired creatives move to Archive"); ART-836 … ART-839 Canceled.
- App icon Reuse of Martin's Sep 17 concept → Robert's reply `C08R8CHB0QL/1758127951.679146` ("not for the app icon").
- Icon around Oct 24 → Arthur's calendar `f_fdd6d2d2f4a4d2f5b908fb` (merge cut Thu Oct 16 12:00 PT; icon in the Nov 6 clean-up).
- All store sizes exported → the Store folder `d_74a7c95c28097dd9777e01` (iPhone ×5, Play ×6, no iPad).
- Ads due Oct 17 / four campaigns → Frederick's Sep 30 mail (`…<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>`: "Wed Oct 15, not the 17th"; skip "anything that only runs there").
- Every cheer fastcouch export Reuse → Marcus's reply `D05V2N6PZNU/1759166437.080255` ("both 9:16 and 16:9"); ART-851 is a Halloween version.
- Re-captures → the deck's newest-capture rule; ART-795 / 797 / 805 / 808 / 816 and the exports ART-851 … ART-854.
- ART-831 (Jul 29) current → Android #1450 vs the deck's #1452 threshold.
- Historical makers (Julia, Frederick) as assignees → Leonard's split ("Martin has the icon and the stills, Marcus has video and end cards").
- Reuse ads assigned / given no date → "the ones that need new work"; both date readings accepted.
- ART-774 / 790 / 792 as existing coverage for the new store art → none is Halloween work; a new ticket (or linking them as context) accepted.
- Sharing audience → the review `evt_d947bf7cd910549b674b1f` (seven attendees, Arthur included); commenter or writer accepted, viewer not.

## State after the fixes

All five local gates PASS with 0 warnings on prompt `63d7c0713c3b` and SQL `29bc98c6e28b`: scenario, injection, error-async, prompt-writing, prompt-check. Next: paste the SQL into `/injection` and the prompt into `/prompt` on the platform (task date Oct 1, 2025, synth-cut), then `/create-humantime`.
