# P2 deep recheck, rerun on the revised SQL

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
SQL sha256: 1348d287ac4a105c41b9f0bf511c6664e306adcc3cf42406688a228fd4b684e7 (matches; previous file matches ffbac458...; prompt unchanged; `hg.py lint` returns 0 FAIL, 0 CHECK)

## Result

**No fail-level finding and no low-impact finding on this revision.** There are 9 advisories, and none of them is an inconsistency in the data. They are unsupported single-source claims, wording, or known base issues, so none should count toward the two-item line.

- All three rev10 low-impact findings (DR1, DR2, DR3) are closed. I retested each fix against the base.
- The new claims hold. Brian's ZOM-465 note, Douglas's reply, the brief's new sentences and the deck lines all survived attempts to contradict them.
- One limit: Season Pass PNGs in the export are Git LFS pointers (130 bytes), so I could not open the art. The strip claim cannot be tested either way (DR9).

Diff scope: 18 changed spots, including 2 new records (Douglas's reply, Brian's note) and 1 new state change (ZOM-542). That makes 54 injected records. All other rows are byte-identical to rev10, so my rev10 claim table still stands for them.

Paths: `OS` = `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data`. `GH` = `Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github`. `M3D` = `GH/root/harmonygames-Games/match3d`. All times are UTC.

## What happened to DR1 to DR9

| DR | Rev10 | Now | Why |
|---|---|---|---|
| DR1 ZOM-542 "Regression" | Low-impact | **Closed** | SQL sets `state_id = 'Todo'`, which fits `started_at` null and "Picking this up after the bug list." No Slack bot post or other record names its state. |
| DR2 ZOM-521 icon row ticked | Low-impact | **Closed** | The row stays [X], but `cmt_zom465_3` now explains it on the record: "the master VFX list was written before that event came in." ZOM-521 dates from 09-02 and #468 merged 09-29, so that holds. |
| DR3 deck spend | Low-impact | **Closed** | Slide 2 now reads "any scale-up comes after the pivot call", matching slide 3's "hold the spend there until the pivot call". The title no longer says "Scaled". |
| DR4 ZOM-344 Done | Advisory | **Stands, advisory** | Unchanged. |
| DR5 "next backend release" | Advisory | **Stands, advisory** | `#470#rc_10`, the calendar and Douglas's base message are unchanged. The injected ZOM-563 echo ("after Douglas's teams update") is gone. |
| DR6 beta date | Advisory | **Stands, advisory** | Base-only. The Trello action no longer carries a list name, so it no longer touches SC-13 directly. |
| DR7 phrasing | Advisory | **Half closed, advisory** | "beta weeks" and "the cut" are gone. The refrain remains and grew by one. |
| DR8 `#468#ev_6` order | Advisory | **Stands, advisory** | Unchanged. |
| DR9 strip and vial owners | Advisory | **Stands, advisory, reworded** | "art" removes my point about server-driven dates, but the claim is still single-source and now cannot be tested. |

## Findings

Format: DR# | pass | checklist section | injected record quote | record path, id and quoted value | Eval dimension or issue type | severity

**DR4** | P2 | §3.2 State / Lifecycle | SQL `cmt_zom344_1`, Marcus, 2025-09-16, state Done: "Quest box open and close animation reuses the endless chest curve and reads well on the quest screen." | Slack `CF4EDAF93359`, Vincent, 2025-09-30 13:29:35: "and the timing is off. Especially in the quest chests. It should be opened first, then the reward should be visible." | Cross-Service Coherence | **Advisory**
- No Marcus commit touched a Quest-named file from 2025-07-03 to 2025-09-17. The later bug is about reward timing, not the box animation, so this is unsupported rather than contradicted.

**DR5** | P2 | §3.2 Temporal | SQL `#470#rc_10`, 2025-09-30T15:51:06Z: "they reach prod with the next backend release" | Slack `D079SNE2TL4`, Douglas, 2025-09-30 18:16:33: "Ok, I updated the prod environment with the latest teams/social changes" | Cross-Service Coherence | **Advisory**
- The reading that windows went live Sep 30 is ruled out by Douglas's scope ("teams/social") and the Oct 8 calendar text: "The server windows that are still on the DEV stack go live with this release".

**DR6** | P2 | §3.2 Referential, SC-13 | SQL Slack `bca784379e7dbca9e64e79a64dfefbba`: "the beta buy we start Mon Oct 6 through Sun Nov 2" | Slack `D04UP2L3E3S`, Leonard, 2025-09-25 05:15:22: "We can barely get the beta out by mid october"; `OS/trello/data.json` list `6851a674975da1fe76e70d93` name "BETA: Oct 10" | Cross-Service Coherence | **Advisory**
- Leonard's line is in a DM Julia cannot read. SC-13 says to settle the date in task data, and Frederick's records do.

**DR7** | P2 | §3.2 Temporal (phrase before its source) | SQL `cmt_zom471_1`, Samuel, 2025-09-17: "nothing here has to land for the beta" | Brief, dated Sep 24: "what still has to land before it runs for bought users" | Cross-Service Coherence | **Advisory**
- "has to land" or "not needed for the beta" now appears in 9 records by 5 authors. It reads as seeded wording but changes no fact.

**DR8** | P2 | §3.2 Temporal | SQL `#468#ev_6` "reviewed", `created_at` NULL, added after `#468#ev_4` merged and `ev_5` closed | `GH/data.json`: merged 2025-09-29T16:13:50Z; `#468#rev_3` submitted 2025-09-29T15:36:41Z | Cross-Service Coherence | **Advisory**
- The table has no sequence column and base "reviewed" rows also have NULL times, so no field conflicts. Only id order suggests it.

**DR9** | P2 | §3.2 Referential | SQL `#472#rc_1`: "the Season Pass premium strip art still shows the October range ... Oliver is taking the date change"; SQL `#468#rc_38`: "Claire has those on her list" | `M3D/Assets/Sprites/Season Pass/bg - golden stripe.png`: LFS pointer, last changed 2025-07-31; `M3D/Assets/Prefabs/Season Pass/`: text is a countdown ("2d 22h"), with no month | Data support | **Advisory**
- Nothing from Claire or Oliver backs the owner claims. The newest Season Pass sprite commit is 09-19 (icons), and no month variant exists, so nothing supports month-specific art but nothing rules it out. Oliver has committed Season Pass sprites, so him taking the change is plausible.

**DR10 (new)** | P2 | §3.2 Other, SC-57 | SQL `7d70c7753179c98b6c8b2b5457a1e5e7`, Douglas, 2025-09-26 16:22:44: "Both tables are updated." | `OS/slack/channels.json` `C09EVVCFHKR`: `is_archived` true; members do not include Julia | Cross-Service Coherence | **Advisory**
- SC-57 lists posting in this channel as "Don't grade". Base posts there run to Sep 30, so a Sep 26 reply adds no new conflict. Julia sees Brian's request and this reply together or not at all, so nothing is hidden from her in a way that matters. A graded fact should not rest on this row.

**DR11 (new)** | P2 | §3.2 Temporal | SQL brief: "each opening 00:00 UTC and closing 23:59 UTC on its last day" | `GH/root/harmonygames-Games/match3d-backend/config/runtime.exs`: `"0 0 * * 3",  # Wednesday midnight (end of Tuesday)` | Cross-Service Coherence | **Advisory**
- The server resets at the next 00:00, so the brief is one minute off the code. It is the same display convention as the brief's own "Sun Nov 2 23:59 UTC", and the brief is a rule source, so the graded value is settled.

**DR12 (new)** | P2 | §3.2 Temporal | SQL `cmt_zom465_3`, Brian, 2025-09-30T18:13:41Z: "the Collect & Win icon does have to land before the beta" | Slack `C05433XK267`, 18:43:32: "Match 3D iOS Submission - #50 Started by user Arthur Blake"; SQL deck: "starting once the stores approve the Sep 30 builds" | Cross-Service Coherence | **Advisory**
- The Sep 30 builds were cut 30 minutes later without the icon, and no commit adds it by HEAD. So "before the beta" can only mean before bought users reach the event, which is how the brief words it. That needs a later client build, and only Vincent's undated "next store build" points to one. This is an open item, which is what the calendar records, not a contradiction.

## Changed and new claims

| Record | Change | Test against the base | Result |
|---|---|---|---|
| Brian, ZOM-465, 09-30 18:13 (new) | "one event icon with no animation" | `IOrderableIcon` has 6 classes (Endless, Infinite Boss, Plague Race, Quest, Season Pass, Zombie Lane), and all 6 have animated prefabs in `Assets/Prefabs/UI/MainMenu/icons`. C&W has none. The leaderboard entry is a menu button outside that set. | Holds |
| Same | "master VFX list was written before that event came in" | ZOM-521 created by Brian 09-02; #468 merged 09-29. His ZOM-526, same minute: "We will implement this together with season passes and collect&win events", so C&W was planned but not in. | Holds |
| Same | "does have to land before the beta" | Brian co-owns C&W on Trello. No clash with his 16:33 ask or his 17:53 ZOM-566 note, which covers text only. He often works past 18:00 UTC (09-29 to 19:31). | Holds; DR12 |
| Douglas, `#zm-collect-win`, 09-26 16:22 (new) | "Both tables are updated." | Parent is Brian's 15:10 ask about "each of the two reward tables". Douglas joined 09-15; he posted 16:06 that day. Reply counts 2 to 3 and users 1 to 2 are correct. No base reply exists to conflict. | Holds, single source; DR10 |
| #472 comment and mirror | "premium strip art still shows" | Art bytes not available. Both copies match. | Untestable; DR9 |
| ZOM-542 | State set to Todo | See DR1. | Holds |
| Brief | "Clip anything that starts before or runs past that to those two instants." | A rule. The October season and the Nov 1 season both cross the span, so it has real use. | Holds |
| Brief | C&W "closing 23:59 UTC" | Mon-Tue, Wed-Thu, Fri-Sun match Confluence and code. | Holds; DR11 |
| Brief | "(Login Calendar on the push sheet, same beat)" | PNs Beta row 13 "Login Calendar update". | Holds |
| Brief | "A held beat keeps its usual windows on its row, marked held." | A rule; no base fact touched. | Holds |
| Brief | "moves to any time before it" | A rule; fits Brian's "reply on this mail". | Holds |
| Brief | Heading offsets | All 9 `style_runs` land exactly on their headings in the new text. | Holds |
| Deck | "Beta-cohort buy" and "any scale-up comes after the pivot call" | Matches slide 3. Pivot call exists in Leonard's 09-22 note. Retention campaigns stay separate. | Holds |
| Frederick reply | "Two things on top of the brief." | No fact. | Holds |
| Robert approval | "one week of the beta", "lands in time" | Generic wording that needs no later record. | Holds |
| Robert retraction | Last clause removed | The brief still carries the later-word rule. | Holds |
| Vincent lightSweep | "next store build" | Commit 25c6c66b6b at 21:20 is after the submission tags on 3f5352a5b5. | Holds |
| ZOM-504 | "Re-tested: it only shows up with the bot running" | His 09-03 DM "couldn't repro without bots". | Holds |
| ZOM-563 | "Checked on prod:" | Vincent 09-30 21:58 "Yep it works as expected". | Holds |
| Trello comment | `list`, `idCard`, `textData` removed | 1 of 56 base comments has this same shape. All 12 others on this board carry the list, so it is unusual, but no claim depends on it. | Holds |

## P2 lines

Unchanged from rev10: services each change a graded fact, no hidden record, writes doable, no Snowflake read, no open-instruction scope problem, no date slips, no platform defects. All new records are before the clock and every stated weekday is correct. Known issues touched: SC-13, SC-15, SC-16, SC-38, SC-57 (new), SC-71.
