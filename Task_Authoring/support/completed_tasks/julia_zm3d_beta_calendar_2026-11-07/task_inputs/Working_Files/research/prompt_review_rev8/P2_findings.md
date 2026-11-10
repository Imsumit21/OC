# Deep recheck P2, rerun on the revised SQL

SQL checked: `review_rev8/inputs/01_Universe_Inject.sql`, sha256 0e8c8ad83f3be435db1f9268f114c916f52293993eb687a55b34005015f9f815 (hash confirmed). Prompt, assignment and date files are byte-identical to the previous round. Blind pass; I opened nothing in either `out/` folder except to write this file.

## Result

- No fail-level finding and no low-impact finding remains.
- DR1, DR2, DR3 and DR4 are resolved. DR2 leaves one base-only residual, advisory only.
- A1 to A5 are unchanged and still advisory.
- Two new advisory notes: A6 (the premium-strip claim still cannot be confirmed in code, carried over from DR1) and A7 (the note now sits on an unrelated PR).

## What changed

Statement-level diff: 96 statements now (71 INSERT, 25 UPDATE), down from 98. Order of common statements is preserved.

| Kind | Statements |
|---|---|
| Changed (6) | Brief `docs_documents` (line 93 onward), sheet `drive_files` (130), `cmt_zom534_1` (180), `cmt_zom521_2` (210), `cmt_zom542_1` (220), Trello action (235) |
| New (3) | `#472#rc_1` (148), Slack mirror `65564543...` (150), parent UPDATE `61f686b8...` (152) |
| Removed (5) | `#473#c_2`, `#473#ev_5`, the #473 `updated_at` UPDATE, Slack mirror `bd1a7d0a...`, the #473 parent UPDATE |

All 14 were tested against the base and the other injected records. No remaining statement references #473. The #468 parent UPDATE looks changed in a naive diff, but it is identical.

Coverage this round: 6 of 6 prompt sentences; 38 of 38 source sentences (brief now 27); 96 of 96 statements.

## Status of earlier findings

### DR1: resolved

- Before: `#473#c_2` created 2025-09-30T16:16:33Z, against #473 `merged_at` 2025-09-30T15:41:20Z, 35 minutes after merge on a deleted branch.
- Now: line 148 `#472#rc_1`, created 2025-09-30T15:52:58Z, against #472 `merged_at` 2025-09-30T15:53:04Z. That is 6 seconds before merge.
- It shares the timestamp of the real review `#472#rev_1` (Arthur, APPROVED, `submitted_at` 2025-09-30T15:52:58Z), and `pull_request_review_id` points to it.
- Base precedent: 6 of Arthur's inline comments share a timestamp with an APPROVED review.
- All post-merge records are gone, so the §3.2 escalation no longer applies.
- The unconfirmed claim itself carries over as A6.

### DR2: resolved, base-only residual (advisory only)

- Before: "Not in the build yet: the home screen and victory score changes for endless and boss arena are still at the mockup stage."
- Now (line 220): "Picking this up after the bug list. The home screen and victory score changes for endless and boss arena are a layout refresh on screens that already work, so they are not needed for the beta."
- Other side, unchanged: `linear/data.json` ZOM-542 `state_id` "Regression", `started_at` null. Line 221 updates only `updated_at`.
- The injected text no longer asserts the work never reached a build, so it no longer contradicts the status directly.
- Residual: a ticket that has not been picked up still reads Regression. That is base data, and Regression does not imply started here: ENG-2331 also has it with null `started_at`, and ZOM-542 entered it at creation. Advisory only.

### DR3: resolved

- Before: "if anything is held and until when" and the header "Hold until (UTC)" had no dated value for the leaderboard hold, and no rule said what to write.
- Now (brief, line 103): "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date."
- The other side still holds: ZOM-429 has `due_date` null and `cycle_id` null, and no fix date exists anywhere. The new rule fits those facts and settles the cell.
- All 9 `style_runs` offsets were recomputed and land on the headings (One-offs 1831, Still to do 2039, Push copy 2268, Config locks 2594; body length 2807).

### DR4: resolved

- Before: `web_view_link` NULL on `f_e4a17c90b3d25f6a8c1d73`.
- Now (line 130): `https://drive.google.com/file/d/1oIsTl3jQeyuTuqudrlGaxEze57_FtuiMHX72lDwtDSE/view`.
- The form matches the base: 198 of 200 spreadsheet links use `file/d/<44-character id>/view`. No base file uses this link. A Drive link id that differs from the `f_` id is the base pattern.

### A1 to A5: still open, unchanged, advisory only

- A1, deploy owner. `gmail/threads/frederick@harmonygames.co_1844625522638279032.json`: "[PERSON_NAME_0612] will help Leonard Hayes to deploy the win and collect to pro servers". Lines 82 to 88: organizer `douglas@harmonygames.co`, and Leonard is not an attendee. Not in Julia's mailbox; no date conflict.
- A2, Sep 30 prod update. DM D079SNE2TL4, 18:16 UTC: "I updated the prod environment with the latest teams/social changes". Line 138, 15:51:06Z: "they reach prod with the next backend release". Not a conflict: it names only teams/social, and Julia cannot read that DM.
- A3, timeline order. Line 142 `#468#ev_6` is `reviewed` with null `created_at`, sorting after `#468#ev_4` merged 2025-09-29T16:13:50Z, although `rev_3` was submitted 15:36:41Z.
- A4, UA deck. Slide 2 "scaled up week by week if the cohorts hold"; slide 3 "hold the spend there until the pivot call". They reconcile if scaling follows the call.
- A5, Queue Manager. Line 169, 16:20:37Z: "Queue manager is in progress". Trello card 63 had `dueComplete` set at 2025-09-30T16:40:22Z. Not graded.

## New

### A6: premium-strip claim unconfirmed (advisory only)

- Line 148: "the Season Pass premium strip is still set to the October range".
- No "October" or "November" string appears in `Assets/Scripts`, `Assets/Prefabs`, `Assets/Resources` or `Assets/AddressableAssetsData` of match3d at HEAD. Season Pass sprites are 130-byte LFS pointers, so a date in art cannot be inspected.
- No record contradicts the claim. It remains the only source of this still-to-do and its owner, Oliver.

### A7: the note sits on an unrelated PR (advisory only)

- Line 148: "Fine for this PR. Separately, the Season Pass premium strip ...", anchored to `Assets/RewardVFXManager.cs`.
- Other side: #472 is "Implement Win&Collect into Queue Manager", and its merge diff touches only `RewardVFXManager.cs` and `CollectAndWinProgressController.cs`.
- "Separately" makes the mismatch explicit, so the field does not misdescribe anything. The path is a real changed file.
- Findability: an agent looking only at Season Pass PRs (#438, #473) will miss it. Routes exist: `github_get_pull_request_comments` on #472, the same route as rc_10 and rc_38, and ZOM-526's comment on line 174 names #472. GitHub is unscoped. This is a difficulty point, not a feasibility defect.

## Changed and new statements that held up

- `cmt_zom534_1`, "That is on main": confirmed. Commit `47c65623e7` (2025-09-10, Oliver, "Using remaining-time endpoint to sync quests end with client") is an ancestor of HEAD. Oliver's "pushed a fix for the quests reset bug" and Leonard's "my quest points are reset" match. It is a client change, so "on main" does not hit the prod-deploy gap that Collect & Win has.
- Vincent's Sep 30 "quest point not found" in DM D0770ET1HV2 is an example of a debug log, not a bug report, so it does not undercut "nothing else has to land".
- `cmt_zom521_2`, ZOM-541: exists, "Cards Collect Vfx animation", In Progress, assignee Calvin. The comment does not claim it is a child of ZOM-521, and it is not one.
- Trello action: only the text changed. "The rollover does not wait on them" conflicts with nothing. Id timestamp, author, card and badge values are as before.
- Slack `#472` mirror:
  - Ts 1759247580.842719 matches `created_at` 15:53:00, and attachment ts 1759247578 matches 15:52:58.
  - Text equals the GitHub body exactly. Title, fallback, footer and color match the base mirror on the same thread.
  - The discussion id is in order after #470's. No id or ts collides.
  - Parent count 3 to 4 is right, and `latest_reply` stays the base 1759247586.958099.
- `#472#rc_1`: id is free (base has no review comments on #472). Empty `diff_hunk` has human precedent (all 53 base empties are human, 26 by Arthur).
- Removals: #473 and its Slack parent return to their base state, and nothing depends on the removed rows. All other injected records are unchanged from the previous round.

## Topic results

- Cross-Service Coherence: no finding. Advisories only.
- Feasibility: no finding.
- Persona access: no finding.
- Data exists: no finding.
- Tool use and cross-service: no finding.
- Hidden records: none. Julia's reach is unchanged, and the new record is in unscoped GitHub.
- Derived columns: none in the answer path.
- Open-instruction scope: none.
- Date-slip severity: no wrong date found. The latest injected record is still 2025-09-30T22:10:41Z.
- Platform defects: none.
