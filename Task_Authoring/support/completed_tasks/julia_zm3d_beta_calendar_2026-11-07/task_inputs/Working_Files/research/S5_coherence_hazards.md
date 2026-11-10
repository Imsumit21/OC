# S5 — Coherence hazards in the ZM3D beta live-ops / player-comms area (synth-cut)

Written by the build session from the S5 worker's verified findings (the worker ran out of steps before writing).
KB transcription (hazard categories, trap catalogue, integrations, conventions) is in `S5b_kb_transcription.md`.

## 1 · Self-found inconsistencies (record · category · locator · proposed disposition)

| # | Records | Category | Finding | Disposition (proposed) |
|---|---|---|---|---|
| 1 | `page_liveops_calendar` vs `LIVE_OPS.EVENTS.LIVE_EVENT_PERFORMANCE` | cross-service referential | page lists "Weekly Leaderboards — Domino Delights / Zombie Match 3D — Live"; the table's 39 Weekly Leaderboards rows are all `domino_delights` | never graded; no ZM3D leaderboard fact depends on the table |
| 2 | `page_liveops_calendar` "Leagues" ("Zombie Match 3D overlaps Plague Race, Leagues and both Endless Monster resets") | semantic | "Leagues" has no backing ZM3D record outside match3d-backend#16 "Weekly leagues fixes" | never graded |
| 3 | `page_liveops_calendar` / `page_live_ops_engine` reward import "hourly (0 * * * *)" vs CDK stack / Douglas DM "every 5 minutes" | quantitative | SC-62 | never graded |
| 4 | Sheet `f_a325dd4af80afc5994d5dc` tab "PNs Beta" copy "Puzzles vs Zombies" vs the 24 Jul 2025 rename (`page_zm3d_gdd`, `page_season_pass_spec`) | temporal / semantic | stale copy in a row marked Ready | designed work item: the copy is stale and the rename record overturns it (dated human-authored copy, not a system field) |
| 5 | Same sheet: ZM3D push row "Win & Collect event start" vs ZM3D feature "Collect & Win" (`page_liveops_calendar`: "Same feature as Win & Collect on Domino Delights, under a different name"); match3d#477 "Collect And Win Analytics and title change" OPEN | semantic | name differs by game; #477 is SC-18 | never grade the display name or #477's state |
| 6 | Trello ZM ROADMAP list `6851a674975da1fe76e70d93` "BETA: Oct 10" vs `C05KNDCHAAG/1757704290.799329` "Beta target: Sep 30" | temporal | SC-13 | never cite the list name; dates come from dated messages |
| 7 | Trello cards 54/56/58/67 (`68c1b79b91ef53c5c5beed58`, `68c44d42651fc25b07722d86`, `68c451141c69fb8af1b4568e`, `68c457c45f9e302837332bf4`) `dueComplete` ≠ `badges.dueComplete` | state/lifecycle | SC-14 | never use Trello completion flags as a deciding fact |
| 8 | Season Pass card (BETA list) dueComplete=true; `page_season_pass_spec` "production Sep 22-29" vs match3d#438 merged 2025-09-15 | temporal | SC-38 | never grade the Season Pass ship date or analytics status |

## 2 · Other verified facts

- match3d#477 open/unmerged (SC-18). `ZOM-78` "Event Calendar For Zombie Match 3D" is Backlog. `ZOM-353` "Leaderboard Rewards are not Deployed to Prod Env" Done 2025-07-09. `ZOM-552` In Progress, `ZOM-566` Todo.
- Alias records: Trello "[Live ops] Plague Race (AKA Mine Dash)" (`6851a6fde24742cce9ad7b1c`), "[Feature] Trophy Path" (`6851a72836c07bf96717ffd2`), "Win and Collect" (`6851a7abf7876721472dba99`) and a closed duplicate "Win and collect" (`686fcb6369c0fdc0b925a0ea`). The Snowflake table comment names the event "Win & Collect" for both games.
- The "PNs" tab of the push sheet is the older Domino-era copy; "PNs Beta" is the beta copy — never conflate them.

## 3 · Hazard ids the worker confirmed in scope (partial; completed in S5b)

T04 (completion vs merge: match3d#327/#330/#375 with ENG-414/420/450, ZOM-450), S01, R07 (match3d#262#c_2), L03
(ZOM-292→#267, ZOM-387→#319), I15 (`f_023c7331d7e34900bd226f`), universal T01, R06, I01–I18, L08–L10, Q01/Q04/Q11, T06, D06.

## 4 · Cohorts seen in `cohorts.json` (counts as the worker read them; relevance judged in the analysis)

LIN-S02 427, LIN-S06 45, LIN-OPEN-ZOM 99, LIN-L02 171, LIN-L04 137, LIN-L22 49, LIN-CQ12 236, LIN-DQ13 228, LIN-UPD 141,
GH-Q11 220, GH-KEYED 428, GH-CLOSED 115, SL-T11 283, SL-T19 152, SL-T28 71, SL-T31 63, SF-LEP 529, TR-B-0632ab 69 (hazards 0).
