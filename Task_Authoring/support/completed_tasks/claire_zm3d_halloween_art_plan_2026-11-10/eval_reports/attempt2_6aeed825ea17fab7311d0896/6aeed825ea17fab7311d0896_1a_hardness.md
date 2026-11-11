# Hardness review: Opus observed run

### FINAL VERDICT: NON-FAIL
Assessment version: model-aware-v3
Assessed model: Opus
Assessment mode: OPUS_OBSERVED
Score: 4
Execution status: COMPLETE
Difficulty: Hard
Gate decision: PROCEED
Gate reason: OBSERVED_OPUS_FAILURE
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Evaluator model: Claude Opus 5.5 (claude-opus-5-5), default effort
Next action: Proceed with dependent authoring; retain the observed failure evidence.
Evidence limits: One run only; no average-score or repeatability claim. The export does not contain the user prompt text, so the prompt match rests on the run's behaviour and sources (see Provenance).

## Summary

The run delivered every requested artifact: a plan doc and a tracker in Claire's Drive, both shared as commenters with all six other review attendees; a comment on all 58 live ad tickets; 46 assignments; two new store-art tickets; and a reply in Leonard's thread with both links. Its store plan, skip logic, off-sheet ads, build cutoff and the ART-809 music trap are all correct.

It missed five separate deciding records, all visible to Claire, that it never opened. As a result, 36 of the 58 ad items have at least one wrong call, owner or due date:

1. Frederick's Android US phone deadline of **Fri Oct 10** is wrong on 30 work items.
2. Martin's Oct 6–15 vacation handover (Julia takes ad statics) means 6 statics went to the wrong owner.
3. Robert ruled that the existing cheer fastcouch Halloween cuts **can't ship**. The run still called them Reuse and left them unassigned.
4. Marcus re-recorded three cuts on current builds. The run called them Refresh first anyway.
5. End card 001 and the cuts made from it still show the old zombies, a fact recorded in a Trello comment. The run called them Halloween version.

## Provenance

| Item | Value |
|---|---|
| Prompt | `04_Prompt.txt` rev 7, sha256 `63d7c071…43d2` |
| Injection SQL | `01_Universe_Inject.sql` rev 6, sha256 `6c143945…a033` (static overlay, not executed; 239 statements parsed, 0 column/value mismatches) |
| Run | `trajectory-run-1 (8).json`, saved as `opus/trajectory.json`, sha256 `ea957713…c589`, 1,678,363 bytes |
| Run model | `claude-opus-5-5[1m]` in init; every assistant message is `claude-opus-5-5`; result `success`, `terminal_reason: completed`, 216 turns, session `510f7d8a-…` |
| Hint status | No hint material in the export (no extra system or user guidance, no sub-agents). Treated as unhinted. |
| Task/source match | The run opens the SQL's injected records (Leonard's Sep 30 thread `1759269913.882683` in #zombie_marketing, the live creatives sheet `f_02b1968f…`, the release calendar, Robert's deck, the Halloween push Trello card, Frederick's Sep 30 email) and produces the prompt's exact deliverables. The prompt text itself is not in the export, so a byte-match to rev 7 can't be shown; nothing in the run conflicts with rev 7. |
| Universe | Universe_SynthCut, `hg4-synth-sep30cut` v16, archive sha256 `d04f295b…fb0c` (`references/universes/synthcut/universe_manifest.json`) |
| Assignment | Claire Morgan, Art Lead; Design; Marketing and GTM; Authoring; **long-horizon**; difficulty **easy** |
| authority_contract | prompt-incorporation-v1 |
| evidence_contract | stage-evidence-v1; reused_evidence: [] (all checks new) |

## Requirement authority

- The prompt incorporates Leonard's message: "take his message and do it all for me". That message points to the live creatives sheet, Arthur's release calendar, Robert's seasonal direction, Frederick's October UA plan, and the split of stills (Martin) from video and end cards (Marcus). This makes the rules in Robert's deck **"Seasonal art direction — Q4 2025"** (calls; refresh if older than Android #1452, or if music is baked in; the newest capture counts) an incorporated source.
- The other deciding records supply **facts** for existing asks (call, who, by when). They add no new obligations. Each is visible to Claire:
  - Frederick's Sep 30 reply in #zombie-match3d (`ca1f761b…`, C0880U9751A, private, Claire is a member): new Android US phone ads are due Fri Oct 10 and iOS UK stays on Oct 15.
  - Martin's Sep 30 post in #company-internal (`c50f7403…`, C05KNDCHAAG, Claire is a member), with Leonard's reply `a3734776…`: Martin is out Oct 6–15, Julia takes ad statics, store art stays with Martin.
  - Robert's Sep 30 reply under Marcus's cheer fastcouch test (`258fa1a8…` in #zombie-art), with Marcus's reply `aba47cfd…`: the existing cuts can't ship and must be redone from the Sep 16 capture.
  - Marcus's Sep 25 thread in #zm-animations (`2c9fbac7…` / `6aecfa67…`, C09ATAJ220H, Claire is a member): the re-records replace the April captures on ART-795, ART-805 and ART-797, while ART-823 is still Apr 7.
  - Trello comment on card 45 "Marketing Video Refresh" (Sep 26): end card 001 and its 16:9, 1:1 and 4:5 cuts still have the old zombies and need a re-render.
  - Frederick's Aug 13 thread in #zombie_marketing (base `C06DJBJL798/2025-08.json` /22): music is baked into the marcus.bennett 9:16 master.
- No miss below comes from an unincorporated policy.

## Requirement map (expected vs observed)

| # | Requirement | Expected | Observed (trajectory) | Outcome |
|---|---|---|---|---|
| R1 | Find the live set | 56 sheet rows plus ART-826 (Trello push-card comment) and ART-831 ("Not on the live creatives sheet yet") = 58 ads; 4 store surfaces | 58 ads and 4 store surfaces (tracker write, msg 294) | MET |
| R2 | Skip calls | Android-US-tablet-only ads: 806, 820, 821, 822, 824, 842, 844, 849, plus 811 and 813 (taken off iOS UK tablet per the Sep 29 email) = 10 | Same 10 Skip | MET |
| R3 | Refresh calls for old captures or baked-in music | Builds before #1452 or the prototype (including #1450 ART-831 and the Jul 28 ART-840); music-baked masters; ART-809 (Aug 13 thread) | All correct, including ART-831, ART-840 and ART-809 | MET |
| R4 | Newest capture counts (re-records) | ART-795, ART-797 and ART-805 are now on #1935, #1966 and #1896 with no music, so **Halloween version** | **Refresh first** for all three. The zm-animations thread was never read. | MATERIAL_FAIL (3 items) |
| R5 | End card 001 family | ART-833, 834, 835 and 848 have old zombies on the packs (Trello card 45), so **Refresh first** | **Halloween version** "current art". The Trello comment was never read. | MATERIAL_FAIL (4 items) |
| R6 | Cheer fastcouch existing cuts | Robert: "We can't ship these", redo from Sep 16. ART-808 and ART-816 need a new Halloween version, assigned to Marcus. | **Reuse**, "Ready", not assigned. Raised as an open question instead. The thread was never read. | MATERIAL_FAIL (2 calls + 2 assignments) |
| R7 | Who makes ad statics | Julia, because Martin is out Oct 6–15 (the whole production window) | 6 statics (825–830) assigned to **Martin** in Linear and the tracker | MATERIAL_FAIL (6 assignments) |
| R8 | Ad due dates | Android US phone ads by **Fri Oct 10**; iOS-UK-only ads by Wed Oct 15 | **Oct 15 for every ad.** The Oct 10 change was never seen; the phrase appears only in the run's own writes. | MATERIAL_FAIL (30 work items) |
| R9 | Flight and campaign change | Oct 18–31; Android US tablet ends Oct 12; deadline Oct 15, not Oct 17 | Correct | MET |
| R10 | Store: exported sets | The iPhone 6.5" and Google Play sets were already exported, so they are Reuse with no tickets (Leonard `b041f2ed…`) | Correct | MET |
| R11 | Store: new art | iPad 12.9" set and app icon need new tickets, maker Martin (store art stays with him), Robert's "keep the icon simple" | ART-856 (iPad) and ART-855 (icon), assigned to Martin, due Oct 16 12:00 PT, with Robert's note | MET |
| R12 | Icon swap "around the 24th" | Build-bound: merge Oct 16, submit Oct 17, live about Oct 22, so a swap on the 24th isn't possible; Google Play graphics can be uploaded any day | Flagged correctly in the doc, tracker and Slack reply | MET |
| R13 | Plan doc in Drive, shared for comment | Created and shared with the review attendees | Doc `3c365a03…` created; commenter shares to Leonard, Frederick, Martin, Marcus, Robert and Arthur (all invitees) | MET (content carries R4–R8 errors) |
| R14 | Tracker in Drive, shared for comment | Same | Sheet `1pfOgzj6…` with 63 rows; same 6 commenter shares | MET (content carries R4–R8 errors) |
| R15 | Comment each ad's call and due date on its ART ticket | 58 comments | 58 comments posted, 0 errors | MET as an action; content wrong on the items in R4–R8 |
| R16 | Assign the ads that need new work to their makers | 48 work items (the 46 with the correct calls, plus 808 and 816) | 46 assigned (Marcus 40, Martin 6) with dueDate 2025-10-15 | Covered by R6–R8 |
| R17 | Reply in Leonard's thread with both links | Thread reply in #zombie_marketing | `slack_send_message` thread_ts `1759269913.882683`, both links, ok | MET |

## Grouped failures and independent causes

Five independent causes. Each rests on a different record, and a run could miss any one without the others. All are retrieval misses of sources Claire can see, and none of them comes from a tool or environment limit.

| Cause | Deciding record | Items affected | Outputs carrying it |
|---|---|---|---|
| C1. Android Oct 10 deadline missed | Frederick's reply `ca1f761b…` in the Sep 30 bot-installs thread, #zombie-match3d | 30 ad due dates | Tracker, doc, Slack reply, 30 ticket comments, 29 Linear due dates |
| C2. Martin's vacation handover missed | `c50f7403…` + `a3734776…`, #company-internal | 6 static owners | Tracker, doc, Slack reply, 6 Linear assignees |
| C3. Robert's ruling on the cheer fastcouch cuts missed | `258fa1a8…` + `aba47cfd…`, #zombie-art | 2 calls, 2 assignments | Tracker, doc, Slack reply, ART-808 and ART-816 comments |
| C4. Re-records missed | `6aecfa67…`, #zm-animations | 3 calls | Tracker, doc, 3 comments (needless re-capture work given to Marcus) |
| C5. End card 001 re-render note missed | Trello card 45 comment, Sep 26 | 4 calls | Tracker, doc, 4 comments |

Union: **36 of 58 ad items** have at least one wrong call, owner or due date. The calls themselves are wrong on 9 of 58.

- **Narrow miss: NO.** 5 independent causes; failed share about 22% (rough weighting over about 120 core items: ad calls 40%, ad due dates 20%, owners 15%, store items 10%, deliverables 15%, giving 9/58 calls ≈ 6%, 30/48 dates ≈ 12.5% and 8/48 owners ≈ 2.5%); difficulty mode Easy, loss 10%.
- **Failure-pattern risk: NO.** Largest trap share is about 13% (C1).
  - Traps the run got **wrong**: C1 Android deadline ≈ 13%, C2 vacation ≈ 3%, C3 cheer fastcouch ≈ 3%, C4 re-records ≈ 2%, C5 end card 001 ≈ 3%.
  - Traps the run got **right**: Android-tablet skip rule ≈ 7%, landscape ads off iOS UK tablet ≈ 1.5%, off-sheet ads 826/831 ≈ 2%, #1450 vs #1452 cutoff ≈ 1%, ART-809 baked-in music ≈ 1%, exported store sets / no tickets ≈ 2%, icon is build-bound ≈ 2%, Oct 15 vs Oct 17 ad deadline ≈ part of the dates weight.
- **Tool calls: 215** (215 by the main agent, 0 by sub-agents). Task type long-horizon, minimum 100. This is above the minimum, not under 90% of it.

## Correct work and usability

The structure is sound and usable. It has a single tracker with one row per surface, the correct Skip set, 49 of 58 correct calls, a correct store plan, the build-bound icon caveat, correct sharing, 58 comments and a thread reply. The run also caught several harder points: the two off-sheet ads, the #1450 build, ART-809's baked-in music (from a base-data thread) and the landscape ads taken off iOS UK tablet.

## Task/environment defects

None found that affect this run. Every deciding record exists in the overlay or base before the clock, sits in a channel, Drive file or board Claire can reach, and is reachable with the tools the run used (`slack_read_thread`, `slack_conversations_search_messages`, `trello_search`). All of the run's writes returned success.

## Unassessed scope

Plan doc body text beyond its structure. Its calls mirror the tracker write (msg 297 reuses the tracker's calls and dates), so the R4–R8 errors carry into it. This does not change the band.

## Score rationale

**Band 4 (Hard, NON-FAIL).** Five independent misses leave wrong due dates, owners or calls on 36 of 58 ads. Fixing them touches every output: the tracker, the doc, the Slack reply, about 40 ticket comments, 29 due dates and 8 assignments. That correction is spread across the whole result, not bounded, which rules out 3.

**Not 5.** The deliverables all exist and the central judgment, the per-ad call, is right for 49 of 58 ads. The store plan is fully right. Most of the corrections are rule-wide edits to existing rows (an Oct 10 date for Android phone, Julia for statics), not a rebuilt plan, so much of the core task is not defeated.
