# 01b Design Review (final, independent)

Reviewer: independent subagent, standing in for the dual red team (RED TEAM FALLBACK). This is not the tool's two-reviewer run. Base values below were read through `hg.py` this session. Seeds do not exist yet, so seed-text findings are about planned wording. Times are UTC. No prompt, OE or criterion text.

## Blocker

**B1. The planned device-rule limiter forks the answer and flips the decision.**
Evidence: section 10 and the notes limit the rule to "device groups with an open stability report". Base has other open reports: ZOM-475 Todo "causes crash on android", ZOM-468 Todo "Low-end devices rendering issues", ZOM-449 Backlog "low-end android device", ZOM-359 Regression "Phone heating up". ZOM-475 reaches all Android. Dropping the 6 clean Android sessions (ZOM-598, 601, 606, 620, 623, 625) leaves casual 7, RPG 4. RPG falls under the minimum of 6, so there is no clear lead and the action becomes keep. ZOM-475 is also card SC-8 (fixed or not is ungradable, 17 FAILs), so a rule that touches it cannot be settled. Learnings section 21.
Repair: drop the "open report" limiter. The gate Doc names Samsung as the one group on this gate, listing the model families, and says every other group needs no pass. Same Doc, no new record.

**B2. Known session defect, class confirmed at 3 of 60.**
Evidence: the sweep finds only ZOM-570 (Pixel 8), ZOM-573 (Redmi Note 13), ZOM-576 (Pixel 7) with 0.3.38. 0.3.127 is not a safe swap: these sessions are Sep 22, and 0.3.127 was "just published" at Sep 22 21:04Z (`C07C2866011/1758575080.472629`), with required versions set on Sep 23 16:02Z (`C0880U9751A/1758643365.607149`). The Android twin of iOS 0.3.38 is 0.3.122 (D05QQF7V404 "Android 0.3.122 iOS 0.3.38"; Android Submission #122, Sep 17).
Repair: change the three devices to iPhones and keep 0.3.38. This keeps three ordinary ids. K4 does not depend on device.

## Major

**M1. No session carries an age, so the "25-45" clause applies to nothing.**
Evidence: `planned_records.sessions`, forms and the field map have no age field. "Ages in band" could not be swept. R1 settles the clause as an age band, then no record lets a run apply it. Learnings section 22.
Repair: add an age to each notes Doc (a field, not a row) and to `sessions`, all 25-45.

**M2. K4 leaks from its own wrong source, and its join field is unplanned.**
Evidence: "work friends", written by someone who works at a game studio, already points at the industry rule without the DM. Brian's visible Sep 22 19:47Z post, the same day as his sessions, cites "an artist friend from Cypher Games" (`C090N54TG79/1758570425.654109`). Sessions have no relation field, so the 51 other relation lines are undefined and could also read as colleagues.
Repair: add `relation` to `sessions` with a closed list. Give Brian's batch a neutral group nickname and use the same nickname in the Turkish line. No other line may imply work or studio.

**M3. Rating alone separates counted from not counted, 60 of 60.**
Evidence: clean 3-4, K1 and K4 4.5-5, K3 and K5 2-2.5, with no overlap. Every block is single-label. One histogram or per-observer mean invites the audit brief section 2 forbids. The design accepts this as open.
Repair (proved here, truth unchanged): ZOM-588 to 3, ZOM-594 to 3.5, ZOM-579 to 3, ZOM-584 to 3.5, ZOM-608 to 4, ZOM-614 to 4, ZOM-570 to 4. All 15 miss combinations stay RPG; smallest wrong gap 0.270 (K5), then K4 0.284, K1 0.333, K3 0.350. The slack is thin, so re-run the flip proof after any other rating change.

**M4. K5 is not a real block as built; its odds misread the calibration.**
Evidence: `00_Carrier_Calibration.md` figures are miss rates. Slack channel thread reply is 4/18 missed, so about 78 % found against the design's .40. Section S5a quotes them as "measured carrier rates" with no direction. 1943 sits among 0.3.x strings on 10 of 60 Docs, next to a store-builds rule, and one search reaches `Match3D Android - #1943 - main` (Julia YES). Submission jobs track the version (Sub #127 = 0.3.127), so a non-Submission job shows itself. The ask also sends runs to Robert, who wrote both K5 and F one day apart, so an author-scoped search returns both records.
Repair: use one shape for every id, as base Crashlytics writes it (`0.3.38 (38)`): `0.3.127 (127)`, `0.3.40 (40)`, and for K5 `0.3.127 (1943)`. The reply keeps naming 1943. Move the K5 author to Leonard (brief's second choice; reply_users_count 2 to 3). Rewrite the find odds as find rates.

**M5. Gate Doc chronology and the F-LIMIT sentence do not fit base git.**
Evidence: Doc dated Sep 23 18:30Z. First Vision Bot job starts Sep 23 23:10:42Z (`C05433XK267/1758669042.879369`), and the first success lands Sep 24 00:23Z. #476 opens Sep 30 18:54:32Z, so run #15 (Sep 25) tested the branch, and no PR existed: "the PR it tested" is false for the one pass it governs. "Tool owner Arthur": the CLI and editor-flow commits (708a2475, 9b1b71d3) are Samuel Turner's. Arthur owns the PR and started the job. Learnings sections 17, 49; `base_claims.py` is blocking.
Repair: date the Doc about Sep 24 15:30Z and R2b 15:40Z (after Bot #8, before R3 at 17:00Z). Word it as the PR for the branch the job ran on. Call Arthur the job's owner, not the tool's author.

**M6. The device rule is silent on timing, and K3 sessions predate the pass.**
Evidence: K3 dates are Sep 23 (3), Sep 24 (6), Sep 25 (2). Run #15 is Sep 25 12:31Z. A reader can drop 9 as uncleared when played, with no PR read, and leave 2 undecided. Calvin's form is 14:18Z, and the session time is unknown. That is a right verdict for the wrong reason, or a fork on 2 tickets. Learnings section 22.
Repair: one clause in the gate Doc: a pass, when valid, clears the group's sessions whatever day they ran.

**M7. Retention: the KPI value is impossible on its date, "mature" forks, and the slot rejects the right number.**
Evidence, recomputed from `/tables/10/rows`: 242 rows, 51 ZM, 47 with a D14 figure. Weighted D7 over the 47 is 9.0885, so 9.09 is verified. 8.79 is verified only as the simple mean over 49 rows (8.7857), not over the mature 47 (8.6885). Those 49 include cohort 09-22, whose D7 cannot exist on the KPI Sheet's Sep 24 date. Cohort 09-15 has a D14 figure, but its window closes Oct 5, so "D14 window closed" literally gives 45 rows and 9.05. S-E1's regex `9\.1` fails on 9.09 and passes the wrong 9.15 (all 49 rows, weighted).
Repair: KPI value 8.63, the simple mean of the 45 rows through cohort 09-08, which fits Sep 24. Define mature in R5 as cohorts that have a D14 figure. Change S-E1 to accept 9.09 and 9.1 only.

**M8. K3 fairness carries the whole run, and the half-weight margin is 1 point.**
Evidence: 35/77 and 38/77 (49.4 %) verified. 38/76 is exactly half, so losing one neutral weight in rubric drafting hits the limit. K3 is also the likeliest miss, so it could be over half of failing runs (failure-pattern limit), and it is the only block a reviewer could call an inference: Arthur never names Samsung. A defect ruling there voids S-H1, S-G1, S-G2 and the writes, not just K3's 8.
Repair: seed "covers a device only if it ran on that device" so "no phone in the loop" answers the rule directly. Keep S-F1 as presence, not the exact 21, so K3 and K5 stay at 35/77 (45.5 %).

## Minor

- **m1. T-S23 points at the wrong record.** `C090N54TG79/1758646127.950749` has no Samsung or S23 text, and no files, so its discovery claim is false. Distractors sit at exactly 6. Repoint to `C08R27X0EAH/1758420497.482989` (Julia YES).
- **m2. rc_27 shape.** All 26 base rows have `line`, `position` and `commit_id` null, and the schema snapshot has 11 columns with no `side` or `subject_type`. The plan seeds line 1, a commit, side RIGHT and subject_type line. Drop the last two (lint `unknown_column`) and match the base row shape.
- **m3. K5 time.** 11:20Z falls in Robert's dead hours: no posts from 09:00 to 13:59Z in four channels this month. Moot if M4 moves the author; otherwise post about 15:00Z.
- **m4. Ticket cadence.** All 60 tickets are exactly 150 s apart. Add jitter.
- **m5. Deck labels.** "What makes a session casual or RPG" could imply re-deriving labels with no data. State that the observer's label stands.
- **m6. KPI owner.** T-RET says shared with Julia; section 11 says Julia owns it. Pick one.
- **m7. Linear comments.** Base has none, so `linear_list_comments` on injected rows carries 60 devices and Vincent's line unproven. Add it to the pre-run tests.

## Check log

1. **Values.** Verified through `hg.py`: every Slack id in the notes list (text, thread, rc), including K5 root rc 15, users 2, 16 rows; F root rc 1; run #15 at row 916; D076RBM29JS Sep 23 count 23, last 1758640673.917619; users map; 51 ZM rows; 9.09. 8.79 verified with the caveat in M7. All 13 mailboxes (12 observers plus Leonard) exist in gmail `users.json`. "No base ZM KPI tab" is only partly re-verified: the "KPI" and "retention" searches hit their limit of 15, so they are incomplete. Hits read are a Firebase data dictionary, an A/B calculator and Competitor Data, none a ZM KPI tab.
2. **Sessions.** 60 rows, 17 counted, casual 9 at 3.833, RPG 8 at 3.375, gap 0.458. 15 of 15 miss combinations give RPG past 0.25 (0.314 to 1.717). Samsung set is exactly K3 (11, all model codes Samsung). 1943 is exactly K5, all Android. Martin only Sep 29. Form counts and dates match; no form predates its session; Claire's form Sep 26 21:00Z precedes K1. iOS 0.3.40 sessions start Sep 25, after release. Only B2 is a platform defect. Ages and relation absent (M1, M2).
3. **Rules.** Apply to every class after B1, M1, M6 and m5. Pixel and iPhone are spared only once B1 lands. The older-iPhone thread (`C08R27X0EAH/1758642623.835409`, iPhone 7) touches no session device; oldest is iPhone 12. Keep/hold mapping is complete and all three outcomes are stated. Store-build and device rules do not collide: groups are disjoint.
4. **Fairness.** K1, K4, K5, F reachable and tied to one block. K1 depends on final mail text. K3 per M8. No trap reads as unmentioned policy once M1 and M6 land.
5. **Injection and prompt.** No contradiction found for: Brian's tutorial and level-order work (Julia assigned both, `C090N54TG79/1759173180.192809`, `1759173247.603649`); Leonard's reopening (he agreed the lean, not a ship); ask at 21:10Z after his last post; Vincent's line (a claim; the crash thread stops Sep 23 with no repro record); Arthur's note (`#if UNITY_EDITOR`, commit text "exit Play Mode"); Claire's gathering (Turkish DMs through Sep 24, nothing against Sep 26); R0 relay (Julia is a member of `C0880U9751A`). All seeded Slack authors are channel members. K4 line: the DM has 14 messages after that slot, so page 1; Sep 29 base DM talk of "sektör" concerns Brian's own job case, so the seed must not read as that.
6. **Leak.** #476: c_1 says "Added Editor window ... in Play mode; added CLI entry to run plans headlessly", the path holds `/Editor/`, and rev_2 mentions Play Mode. The design discloses only "Play mode"; "headlessly" is stronger. It helps only a run already on the PR, so the real gate is opening #476, and the gate Doc sentence points there. Measured inline miss is 70 % overall but 3/12 on Julia tasks. K3 find about .50-.60 (judgement), not .35-.40. K1 about .50: Julia's mail stops Sep 17, so 18 seeded mails sit together and `from:claire` returns both. 1943 stands out (M4). Comment read is about 285K characters, so spill stays a confound risk. One call revealing two records: Robert author search (M4).
7. **Fit.** Audience call fits a PM under Marketing and GTM, and Julia's voice supports it. GTM is thin, though: the output is a session register. The 60 retro tickets and the device/build field split look engineered, and base ZOM is a bug tracker, so 2.7 is exposed. Evidence reads are 123; 183 needs the writes. The log note should state why tickets exist. Leonard's ask has 10 delegations, heavy for a founder's message, but it is a record, not the prompt.

## Verdict

**Do not start /create-injection until B1 and B2 are fixed; fix M1-M8 in the same pass.** All are edits to planned values or wording: no rows, steps or prompt rules. Then proceed.

Predicted /hardness (judgement, uncalibrated): **4, range 3-5, confidence low-moderate.** Any one miss gives RPG and keep, which can support 5, but the register stays largely right, which argues 4. As designed, P(all four caught, score 1-2) about .25; after repairs about .10-.15. Main fail route is a defect ruling on K3, not Opus finding everything.
