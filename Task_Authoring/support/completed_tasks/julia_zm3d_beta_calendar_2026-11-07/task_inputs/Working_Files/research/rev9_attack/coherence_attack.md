# Coherence attack on revision 9 (sha 892f7edd...)

Clock: 2025-10-01 00:00 PT (07:00 UTC). Standard: Eval 1 §3.2 and Eval 0 Check C. Times are UTC unless marked.

## Result

No fail-level item on its own: no lifecycle or sum defect, no broken convention, and no new claim that the base flatly disproves.

Two items are low-impact. **Two low-impact items fail §3.2, so a reviewer who digs into both scores this FAIL.** Both are one-sentence text edits on injected rows (F1, F2). Fix them before review. The rest are cosmetic, plus one Unique Ground Truth watch item that is not a coherence defect.

| # | Record | Label | Short form |
|---|---|---|---|
| F1 | Leonard's S23 reply | Low-impact | "remote device list": the only such service he is on record using is BrowserStack, and he cancelled it on Aug 7 |
| F2 | Brian's ZOM-566 note | Low-impact | "analytics first ... can follow", 63 minutes after his own "Analytics and name changes first" |
| F3 | Leonard's S23 reply | Cosmetic | Posted during his VC call |
| F4 | Leonard's ZOM-534 note | Cosmetic | Lands 2 seconds after a line in a live DM conversation |
| F5 | Vincent's ZOM-563 note | Cosmetic | "the update" is unscoped, and sits near Arthur's "next backend release" |
| F6 | SQL comment, dossier | Cosmetic | "21 cohort issues" is now 22; one stale dossier row |
| W1 | Oliver's shader reply | UGT watch, SCOPE_GAP | True, but it states that a flagged art fix has not gone out |

## Findings

### F1. Low-impact: "the remote device list" (fb870fca..., 2025-09-29T21:41:37Z)

Injected: "Ran this again on an S23 Ultra from the remote device list, live Android build".

Base on the other side:
- Arthur, #executives, Jul 30 18:08: "I'm going to get [PERSON_NAME_0050] "browser stack" which lets you virtually rent services so you can run your game on it to test".
- Leonard, DM to Arthur D04UGG61DUM, Jul 30 21:37:51: "This is galaxy s23 ultra - I downloaded from Netherlands play store and it looks good". Same DM, 22:14:37: "but most samsung ones are There".
- Leonard, #admin_foundersonly C04UEQVDVB7, Aug 7 22:32:40: "I canceled BrowserStack, just to make sure we don't get hit by another $49 for a service that I won't personally use every month".
- Leonard, #executives, Sep 28 02:10:20: "I tried a samsung simulator same problem - I tried on a real device oneplus and I didn't have this problem". His tools the day before the injected reply are BlueStacks and a OnePlus.

So the rev9 route (the census's "Best honest route") is the service he had cancelled seven weeks earlier, and nothing re-subscribes it. The census table did not record the cancellation.

Why it is not fail-level: the reply does not name BrowserStack, and another referent exists. Confluence page_qa_runbook, which Julia can read, says "We keep a small physical lab plus a cloud device farm for the long tail." Arthur, Jan 2 2025, says of the AWS device farm: "we have used the device farm a good bit". Also, "remote device list" appears nowhere in the base.

Smallest fix, use the runbook's term: "Ran this again on an S23 Ultra in the cloud device farm, live Android build, a few endless runs with the airstrike. Could not get it to freeze, so I am leaving this one." Do F3 in the same edit.

### F2. Low-impact: Brian's ZOM-566 note against his own line (cmt_zom566_1, 2025-09-30T17:53:19Z)

Injected: "Owen, analytics first. The header title and the info screen text can follow with it. The event runs fine with the current text, so they do not have to land before the beta."

Base on the other side, same day, same person, same list:
- #zm-collect-win 16:49:10, Owen: "got it, I'll try to squeeze analytics events first then".
- 16:50:02, Brian: "Analytics and name changes first".
- DM D0770ET1HV2 08:47:55, Brian: "evet isim gerek" (yes, it needs a name). 15:23:57: "Energy Raid Energy Chase". 15:24:16, Vincent: "raid daha iyi bence de".
- Owen's real commit order has text before analytics: c7d3bc6f "Change text on Collect And Win info screen" 21:34:44; 31ee4178 analytics 22:23:02; 9dc995cb header 22:24:09.

So 63 minutes after ranking name changes level with analytics, Brian demotes them, gives no reason, and the work then goes the other way. It reads as a later correction, which Eval 0 allows, but nothing in the record explains it.

Is "the event runs fine with the current text" true to the base? Yes, as a functional claim. Vincent, #zm-collect-win 16:47:38: "none of them blockers and doesn't affect the submission so it's up to you guys". Vincent also said that morning that strings need fixing and "Token çok sırıtıyo" (the word Token sticks out), so "fine" means working, not finished. The note makes no naming claim, and it should not: "Energy Raid" lives only in that DM. "With it" fits the single PR #477, and the #477 files (MainScreenCollectAndWin.prefab, InfoScreenCollectAndWin.prefab) match "header title" and "info screen text".

Smallest fix, keeps the settling sentence and matches both base lines: "Owen, analytics and the name changes are first on the list, but none of it is a blocker. The event runs fine with the current text, so the header title and the info screen text do not have to land before the beta."

### F3. Cosmetic: the S23 reply sits inside a VC call

Leonard, #executives 21:06:17: "waiting for the Turkish VC to show up". 21:49:58: "ok talked to her". His calendar has "Leonard Hayes and PERSON_5748_NAME" 21:00-21:30. He posts nothing anywhere from 21:06:37 to 21:49:58 except this injected reply at 21:41:37. Not incompatible (Eval 0: implausibility alone is no defect), and the hour is normal for him.

Since F1 rewrites the row, move it. Suggested ts `1759187861.318279`, created_at `2025-09-29T23:17:41.318279Z`, id `e343557b2e94a1701251ebd079e6f0ce`, and the parent's latest_reply to the same ts. He is silent 22:48:10 to 01:14:46 and has no calendar entry then.

### F4. Cosmetic: ZOM-534 note timing (cmt_zom534_2, 2025-09-30T01:22:46Z)

Leonard's DM with Robert, D04UP2L3E3S: 01:22:06 "I think if we get no traction from fundraising in the next week or so it's time to get ready for downsizing". 01:22:44 "Blake wants one engineer and let everyone else go". 01:23:12 next line. The Linear note lands 2 seconds after the second line. Suggested: `2025-09-30T01:09:52Z` on created_at, updated_at and the issue's updated_at. That is before the DM starts at 01:14:46 and still 18:09 PDT, so "tonight" holds.

### F5. Cosmetic: "the update" in Vincent's ZOM-563 note

The base update is Douglas, DM 18:16:33: "I updated the prod environment with the latest teams/social changes". Julia cannot see that DM, so she reads "Checked on prod after the update" about six hours after Arthur's #470 line (15:51:06) "they reach prod with the next backend release". The GCal Oct 8 entry settles the release, and teams run on Nakama (Architecture Overview), so nothing breaks. Smallest fix: "Checked on prod after Douglas's teams update: teams' lives, golden frames and names all work as expected. Closing."

### F6. Cosmetic: bookkeeping

- SQL section header says "Linear per-issue comments (21 cohort issues)". There are now 22 with ZOM-563.
- 01_Grounding_Dossier.md line 730 still ties `cmt_zom566_1` to Owen's "Wiring both..." quote. Not in the universe. solver.py has already moved to `cmt_zom566_2`.

### W1. UGT watch, not coherence: Oliver's reply (31b154fc..., 2025-09-30T21:24:52Z)

Injected: "it goes out with the next build and nothing waits on it."

The reply is true (table below), but it states on the record that a fix flagged after the brief, for player-facing art, has not gone out. The commit (21:20:26) follows both Sep 30 submission builds (18:43, 18:45), and the UA deck starts the buy "once the stores approve the Sep 30 builds". So bought users start without it.

Brief: "what has been flagged for that beat as not done since this brief (prod deploy, config or player-facing art)". "Polish nobody flagged" does not exclude it, because Vincent flagged it. "Nothing waits on it" is the owner's own claim (SCOPE_GAP). What rules the other reading out is "for that beat": no one names a beat, and the box is the shared reward box (weeklyContest animator, RewardScreen.prefab). That holds, but a reviewer could still list it under Quests or Endless.

Optional hardening: "It is only that sweep on the shared reward box, no event is tied to it, it goes out with the next build."

## Claim by claim

| Claim | Result | Evidence |
|---|---|---|
| S23: "live Android build" | True | 0.3.133 published Sep 27 15:51:47, "this is the latest Android - 0.3.133" Sep 28 16:11:06 |
| S23: "airstrike" in endless | True | Parent's masked word plus Vincent Sep 22 "the airstrike freeze"; Robert Sep 22 "air strike in endless mode"; EndlessModeBar.cs SpawnNuke uses `airStrikeVfx` |
| S23: nothing says otherwise | Holds | No freeze or S23 report after Sep 29 in any channel. Robert Sep 24 fits: "had to restart his app", then the log continued. Vincent Sep 22 fits: Samsung-specific, could not reproduce |
| Shader: commit 25c6c66b6b | True | Oliver, 21:20:26. Adds `SKINNED_SPRITE` to lightSweep Box Variant.mat, which answers Marcus's "doesnt deform". The commit subject is about popups, and it changes 9 files |
| Shader: "next build" | True | Not in Submission #50 / #135. Internal builds #2027 and #1758 had already started at 21:21:06 and 21:22:39, so it can only mean the next store build |
| Shader: reply order | Clean | Base replies end 17:42:42, none after. reply_count 4 to 5, users stay 3 (Oliver already replied at 17:41:38) |
| ZOM-534: "store build" | True on each store | iOS 0.3.49 released Sep 29 21:55:08 (#zombie-match3d, Julia is a member). Android 0.3.133. Both are main builds of Sep 26 and contain 47c65623e7 (`merge-base --is-ancestor` passes); the only later quest change on main (d376fab4c8) does not revert it |
| ZOM-534: "00:00 UTC reset" | True | Confluence: "daily at 00:00 UTC" |
| ZOM-534: online then | No conflict | Slack silent 22:48:10 to 01:14:46 |
| ZOM-534: "my report" | True | #zombie-bugs Sep 8 00:03:45; the ticket quotes "@Leonard said" |
| ZOM-534: reset working | Nothing contradicts | Leonard Sep 11, #executives: "my quest points are reset". Vincent's Sep 30 "quest point not found" is about logs on claim, not the reset |
| ZOM-534: stays In Progress | Explained | Douglas: "keeping this open" |
| Douglas: "went out in the client builds" | True on Sep 25 | Fix reached main by Sep 11; Android 0.3.127 (Sep 22) and iOS 0.3.40 (Sep 23) were live |
| ZOM-566: order | Clean | created 16:26:02, started 17:20:13, Brian 17:53:19 seq 1, Owen 19:40:47 seq 2, updated_at 19:40:47 |
| ZOM-563: DM and close | Clean | "Yep it works as expected" 21:58:44; note 22:04:33; Douglas "Go to sleep" 22:05:03 |
| ZOM-563: fields after UPDATE | Clean | created Sep 23 < started 18:14:25 < completed = updated 22:04:33. No later activity in Slack, Gmail, Linear or backend git. Also clears SC-16 for this ticket. time_in_status stays NULL (same as SC-22) |
| Trello note | Clean | Card title matches; Oct 13 is a Monday; author Leonard; badge comments 1; dateLastActivity matches. List name is SC-13, unchanged |
| Brian's Sep 22 mail, 3 copies | Clean | All three changed. Snippet ends before the sentence. Sep 26 "Same contents ... premium track" fits. Spec: "tiers, rewards, theme". No "quest tables" left |
| Pushes headers | Clean | 7 headers, column_count 7 |
| Robert's withdrawal | Clean | Martin wrote the parent; Robert's approval says "one themed prop set only" |

## Conventions

- Slack id: both rows equal sha256("channel|ts")[:32]; base sample 174,403 of 174,408. No id or ts collision.
- Slack ts: both end in 9 (610,445 of 610,468 in base) and match created_at.
- Threads: thread_parent_id and thread_ts_legacy correct; replies carry 0/0/NULL. S23 parent 1/1/reply ts, same as the base self-reply thread 1758746963.720009. Both authors are channel members.
- Linear: sequences follow time; issue updated_at equals the latest comment; every author is in team_ZOM; base has 0 comments, so no sequence clash. state_history_json is not touched (same as ZOM-432/344; not in the export, so not checkable).
- Author hours: Leonard 21Z and 01Z, Oliver 21Z, Brian 17Z, Robert 22Z are all normal. Vincent 22Z is rare but backed by his 21:58 DM.
- Apostrophes doubled. Brief style-run offsets all land on their headings. `hg.py lint`: 0 FAIL, 0 CHECK, 0 INFO.
- Bot mirrors: none needed. Status mirrors appear on 13 tickets, all created by Robert or Leonard; ZOM-563 and ZOM-566 have none. Base unfurls of both predate the changes and show the then-current Todo. No permalink to either parent.

## Scanned and not scanned

Scanned: full rev8/rev9 diff; all 610,468 Slack messages including channels and DMs Julia cannot read; Linear, Trello, GCal, Confluence; targeted Gmail threads; GitHub data and git history for match3d, match3d-backend, match3d-quests; a text grep of the other services for the three ticket ids.

Not scanned or not possible:
- #477's four commits are not in the local git, so their diffs are unread. I used commit metadata and the CodeRabbit file list. Prefab text past 10 KB is cut in SynthCut, so the current header string is unconfirmed.
- Many base lines are masked ([USERNAME_...]); Turkish lines are my translation.
- Slack canvas F09BZ9R1NFM has no content in the export.
- Snowflake was covered by that text grep only.
- Did not re-run Eval 1 UGT on the whole brief; W1 is the only fork I raise.
