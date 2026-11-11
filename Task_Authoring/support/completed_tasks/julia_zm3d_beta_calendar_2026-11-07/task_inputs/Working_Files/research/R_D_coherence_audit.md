# R-D — Coherence audit over the scope (synth-cut, clock 2025-10-01 00:00 PT)

The build session wrote this from the R-D worker's final report (the worker ran out of steps after its probes and
before writing). Locators unchanged; the build session completes §1, §4 and §5 in `01_Scenario_Design.md` §1a.

## 2 · coherence_hazards.json

Six categories, 59 emitted hazards (T08, R02, R05, R09, L01, L07, Q01, Q03, Q04, Q09 have count 0). Direct example-id
hits in scope: none in the window read. Closest: Q02 (`reply_users_count` vs distinct repliers) on
`C0880U9751A/1750724624.203279` (July, outside the Sep 22–30 window). T04/S01 examples match3d#327/#330/#375/#379/#382
and L03 examples (ZOM-292→#267, ZOM-387→#319) sit outside the cited PR/issue sets. Rules that still apply to the scope:
T01 (`reviewed` timeline events have null `created_at` and an empty actor — never date a review from the timeline), I01
(raw-shaped Slack rows: 218 in D05GU6L0XFH, 222 without `id` — cosmetic), I10 (non-`usr_<16hex>` Linear ids
`usr_Robert`, `usr_EMPLOYEE_0032`), L09/L10 (merged PRs with no human APPROVED — fair, ~574 base-wide).

## 3 · Seven QC categories (probe results)

- **Slack**: `reply_count` vs replies in the dump — 0 mismatches across the 9 scope files; `id != sha256(channel|ts)` —
  0; no strikethrough retractions in cited messages.
- **Linear** (13 issues): ZOM-471 Todo / priority 3 vs a Slack bot "high" (SC-71) — **real**; ZOM-429 (Backlog) and ZOM-534
  (In Progress) while Slack says the leaderboard is "working fine" and quests fixed — SC-16 / L03-style state-vs-activity,
  **real** (handled by design: ZOM-429's later prod check; ZOM-534 treated as a known issue); no `updated_at <
  completed_at`; no `completed_at` outside Done.
- **GitHub**: all 22 scope PRs merged, #477 open (SC-18: CodeRabbit says "closed"); PRs cite no Linear keys (S01 note); no
  human APPROVED on #356/#360/#370/#396/#397/#420 (fair).
- **Trello**: SC-14 mismatches only on the four BETA-list cards (68c451141c69fb8af1b4568e, 68c1b79b91ef53c5c5beed58,
  68c44d42651fc25b07722d86, 68c457c45f9e302837332bf4); no T06 (action after `dateLastActivity`) on the 8 scope cards.
- **Push sheet** f_a325dd4af80afc5994d5dc: **13 internal Status vs "Status (NA, WIP, LIVE)" contradictions in "PNs Beta"**
  (Not Ready + LIVE ×3, Ready + WIP ×4 among them); the spreadsheet title "Push Notifications Zombie Match" while its
  translated tab holds two other games' copy; `content_path` `Design/Domino Delights/…`; owner `Resource:
  -6481757892984311338`. "PN BETA Translated" is 4 rows short of "PNs Beta" with rows 3–7 from three other games
  (Tiledozer/Luckydrop R03, Domino Adventures R04–R07, River Rush R11 vs Plague Race), and "Puzzles vs Zombies" appears in
  its R10 body_en (Treasure Hunt). "PNs Beta" names "Puzzles vs Zombies" in R04 (1-day lapse) and R06 (D0-1 FTUE).

## Consequence (build session)

The push sheet carries live, same-artifact contradictions (Status vs Status(NA/WIP/LIVE); title vs content). A design
that **requires** the sheet must explain both columns with a dated owner statement, or keep the contradictory column off
the path. Treated in `01_Scenario_Design.md` §1a.
