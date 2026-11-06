# Coherence audit — working notes (scenario stage)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Source: subagent audit (step limit reached before writing) plus the design session's own checks. The dispositioned tables live in `01_Scenario_Design.md` §1a.

## Hazards by category (coherence_hazards.json)

- Temporal: T02 (thread message order in the vincent@/blake@/leonard@ thread files), T04 (ZOM-450 completed before match3d#375 merged), T06 (card 68d1eb90bef538c7c5c5599d dateLastActivity 2025-09-23T00:36:35Z = last action; seeded comments must bump it).
- Semantic: S01 (match3d PRs #327/#330/#375/#379/#382 cite ENG-414/420/450/470/472; branches samuel.turner/ENG-…), S03 ("Submission Blocker" is one label among 243).
- Cross-service referential: R01 (no Sep 2025 message in the scoped channels cites a missing ZOM key), R04 (Slack→Drive links use Google-native ids), R06/R07 (match3d human PR comments 0 % mirrored; bot 83 %; COMMENTED reviews 99.4 %), R08 (seed GCal row and invite mail together or neither).
- Quantitative: Q01/Q03 clean in base, seeded replies must update reply_count / reply_users_count / latest_reply; Q04 (1,526 raw-shaped parents without counters); Q10 (copies differ between mailboxes — quote Vincent's own copy only).
- State/lifecycle: L03 ZOM-292 and ZOM-387 open with merged PRs (match3d#267, match3d#319); L06 open children with Done parents ZOM-16, ZOM-293, ZOM-317, ZOM-453, ZOM-458; L08 touches ART only (oscar.bennett, rachel).
- Identifier/format: I03 (blake@, leonard@, vincent@ thread-file aliases), I05 (token mailboxes unreadable), I08 (EMPLOYEE_0025_GITHUB_USERNAME → arthur.blake, PERSON_5760 → douglas, PERSON_5877 → owen.baker, PERSON_0180 → brian.foster), I11/I12/I13 (GCal copies), I17 (Trello list "BETA: Oct 10" live name; redacted list/member tokens).

## Pre-existing inconsistencies found

1. SC-13: ZM ROADMAP board 6851a6569f3bf818760632ab, list 6851a674975da1fe76e70d93 named "BETA: Oct 10"; rename actions read "BETA: Sep 30" on 2025-09-12T16:42:21Z (earlier "BETA: Aug 30" 07-30, "BETA: Aug 15" 07-13).
2. match3d-backend has 35 PRs, max #35 ("Other players profile", closed unmerged 2025-08-13); #36 is free.
3. match3d: max PR #477; #476 (vision bot) merged in the timeline but merged=false in the export; #477 unmerged (SC-18).
4. Linear: max ZOM-566; ZOM-567…580, ART-793, DES-313 absent. ZOM-563 quoted in Slack only in D079SNE2TL4 and C08R8CHB0QL.
5. C08R6BF4ENN (#zombie-ops) private, created 2025-05-07, 28 Sep messages; C08R27X0EAH private, 1,097 Sep messages; D079SNE2TL4 and D0770ET1HV2 are is_im with 5 members.
6. release/1.3.24_HotFix exists (head 4225a7c4ce); vincent.parker/hotfix0910 also exists.
7. SC-8 (ZOM-475) and SC-16 (ZOM-564 / ZOM-563 / ZOM-513 / ZOM-514) sit inside the scope — ZOM-475 excluded; SC-16 tickets graded only on the safer evidence.
8. SC-19: store builds are 0.3.x / 1.3.x in Slack, RAW_EVENTS 0.1.5xx / 0.601 — never matched.
9. Q10 / X04: EMPLOYEE_0011_EMAIL vs arthur.blake copies differ (23 pairs < 0.80).

## People (activity.json status_at_clock)

All of Vincent Parker, Arthur Blake, Leonard Hayes, Brian Foster, Douglas, Oliver Brooks, Claire Morgan, Julia Lawson, Robert, Calvin Price, Owen Baker, Samuel Turner: `active_sep_2025_quiet_in_oct`. Arthur, Robert, Leonard, Owen and Brian have a 2025-10-01 Slack post at or before the 07:00Z clock; nothing is seeded on Oct 1.

## Integrations relevant to seeded services

INT-01 (GitHub→Slack; match3d mirror window 2025-06-30T21:35:55Z → 2025-09-30T22:33:40Z), INT-03 (linear[bot] on keyed PRs, 76 % of 428), INT-04 (Linear Slack app; only 26 in #zombie-bugs), INT-05 (Linear mail digests), INT-06 (Jenkins #builds; a seeded build needs Started + result), INT-07 (Firebase tester mails), INT-08 (TestFlight app-name drift: "Puzzles vs Zombies" 1,194 mails 2025-03-21 → 2025-07-14, "Zombie Match 3D" 70 mails from 2025-07-24), INT-09, INT-10 (299 Crashlytics digests to Vincent), INT-11 (invites match a GCal row 87.1 %), INT-12, INT-13, INT-21 (no Trello→Slack), INT-22, INT-23 (CodeRabbit).

## Cohort and catalog ids

- cohorts.json LIN-OPEN-ZOM: team_ZOM, state not Done/Canceled/Duplicate, count 99; hazards inside: parent-Done-child-open 5, Todo-but-PR-merged 2.
- trap_catalog: P01/P02 name collisions, P04 GitHub tokens, N01 ZOM/ENG twins, N02 PR # vs issue #, D01/D02 lookalike Drive files, D04/D05 stale versions, D06 page_qa_runbook has 2 versions, C01/C02/C03 overturned-in-replies, B01/B03/B04 bot noise and Jenkins Unknown, X01/X02/X04 redaction tokens, K01 canvas pseudo-channels, K02 app-name lineage.
- timeline: 2025-09-01 win-streak port (C08R27X0EAH/1756753899.413789, match3d#411); 09-02 ZOM-556/527 tuning; 09-11 PR #408, ZOM-493 closes; 09-15 Season Pass PR #438; 09-16 ZOM-549; 09-17 ZOM-436, ZOM-552/526; 09-19 ZOM-554 (C08R27X0EAH/1758311440.897499); 09-25 vision bot (match3d#476).

## Sibling sweep

- Works on dev, not prod: ZOM-534 (In Progress, 2025-09-08), ZOM-563 (In Progress, 2025-09-23), ZOM-353 (Done, 2025-07-07).
- "Puzzles vs Zombies": 0 hits in vincent.parker@harmonygames.co.
- Card 68d1eb90bef538c7c5c5599d: comments 0, 2 actions — seeded comments are net-new.
- Design-session additions: Android #2027 (start 21:21Z) lacks the season pass fix and #2028 (start 21:36:41Z) carries it; ENG-2258 / ENG-2360 are Domino Delights tickets; DES-304…312 carry the Cookie label (another game).
