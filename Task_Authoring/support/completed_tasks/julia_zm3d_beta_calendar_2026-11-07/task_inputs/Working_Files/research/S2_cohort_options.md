# S2 — Natural populations of ≥ 40 records for the cohort gate (synth-cut)

Written by the build session from the S2 worker's findings (it ran out of steps before filling its skeleton) plus the
build session's own checks (marked BUILD). Locators unchanged.

| # | Population | Count (scope) | Per-record surfaces | Bulk shortcut? | Julia-visible? | Verdict |
|---|---|---|---|---|---|---|
| 1 | Zombie Lane reward nodes | node table lives in a linked Excel; Julia owns only `f_dc0254e04bfd48cc4ee8ab` "DO NOT USE OLD Zombie Lane Rewards" (stale); ZOM-398 says nodes stop after level 54 | none per node | one sheet read | live node sheet not visible (2 hidden + 2 UNVERIFIED hits, BUILD `persona_view search`) | no |
| 2 | Season Pass 30 × 2 reward tiers | 60 | none per tier | one sheet read | NO — `f_c0518ab5dacb03dcc8a144`, `f_89aebb6083dc44501666c7` (S4 §7) | no |
| 3 | Quests | quest list not found; 6 tickets (ZOM-323/355/357/399/534/557) | — | — | — | no |
| 4 | Event reward lines (Endless milestones/ranks in `f_9956263905ddb43d1500ff`, Plague Race stages, Boss Arena milestones, daily login) | ~25 Julia-visible lines (BUILD: Endless doc 3 daily + 8 weekly rows) | doc table only | one doc read | partly | no |
| 5 | Push-notification catalogue `f_a325dd4af80afc5994d5dc` | PNs 7 (Domino-era), PNs Beta 14, PN BETA Translated 16 × 10 languages, Deep Links 8 | none per row | one sheet read returns every row | YES | no (as a cohort); yes as a decision surface |
| 6 | Julia-owned docs/sheets | Event Icon System doc, Zombie Lane doc, `FTUE Catalogue`, `ZM Bundles` (75 rows, May 2025, BUILD) | none per row | one read | YES | no |
| 7 | ZM ROADMAP Trello cards | 79 (BETA: Oct 10 = 19, Jun 30th 14, Backlog 12, July 18 9, Oct 21 8, Jul 24 7, Jun 18th 5, July 30 5) | only 10 cards have comments (56 comments board-wide), 23 descriptions, 9 checklists | board read | YES | weak; SC-13/SC-14 sit on it |
| 8 | Snowflake STORE_REVIEWS / APP_STORE_REVIEWS (ZM3D) | 236 ZM3D rows (Apr–Sep 2025; Sep 33) — BUILD | none (one query) | one query | YES (unscoped) | no — templated generic text ("Reasonable ad frequency …") |
| 9 | ZM3D levels | VariantC `C_0001`–`C_0275` (275 `.asset`), `PR_0004`–`PR_0103` ladder (100), `Level_117–121`, `MF`/`MFv2` 35 each, Endless/Infinite levels; PRs match3d#439 (4,078 files) and #464 (2,288 files) | per-level asset file (GitHub), level threads in `#zombie-design` | none for asset content | YES (GitHub unscoped) | viable as a population, but level design is not Marketing & GTM work |
| 10 | Live-ops ZOM issues (BUILD) | 56 ZOM issues on live-ops features, open at the clock or closed in Sep 2025 (Done 24, Todo 12, Backlog 8, In Progress 6, In Validation 3, Canceled 2, Duplicate 1) | description and state come from the list call; **base Linear comments: 0 of 3,687 issues** (S2 cache: 1,955 attachments, 0 comments); PR links rare (1 of 66 Sep match3d PRs names a Linear id); Slack bot posts in `#zombie-bugs` | yes, unless per-issue comments are seeded | YES (Linear unscoped) | viable only with seeded per-issue notes (playbook S2 necessity rule) — see the analysis §8 |
| 11 | GitHub match3d PRs (Aug–Sep) | 121 merged Aug–Sep, 66 in Sep | files, reviews, comments, `#zombie-prs` mirror | per PR | YES | engineering population; review comments are CodeRabbit (66 of 67 Sep PR comments) |

Other: "Video Capture Requests for UA" `f_b5fb884dc96261846b6c2c` 25 rows (2024); "Playtestcloud learnings" `f_151b8f3952d3101dd82174`
95/44/18/20 rows (Domino Delights, 2024).

Cross-candidate inconsistencies noted: the push sheet's "PNs" tab is the Domino-era copy and "PNs Beta" the beta copy
(never conflate); Trello flags (SC-14); Linear has no base comments at all, so any "Linear comment" evidence is seeded.
