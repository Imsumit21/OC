# P2 deep recheck: services, data and access

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Pass: P2, blind. SQL sha256 edae63f3e83852f212c19892a9c9cf7304404b80db3178f92a470f301a598e13, read only, never executed.

**Result: 0 fail-level, 0 low-impact, 6 advisory.** The two changed sentences add no finding. The six advisories are unchanged from the previous hash (1f2175a2...). No State / Lifecycle or Quantitative item. Nothing here fails or lowers Cross-Service Coherence, Feasibility, Persona access, Data exists or Tool use.

**Checked:** 6 of 6 prompt sentences. All 111 SQL statements (81 inserts, 30 updates): 12 Slack inserts and 8 updates, 6 Gmail messages in 6 threads, 4 GCal rows, 4 Drive files, 1 Doc, 7 Slides rows, 3 Sheets rows, 5 GitHub rows, 32 Linear comments on 22 tickets, 21 Linear issue updates, 2 Trello rows. `hg.py lint` on this hash: FAIL 0, CHECK 0, INFO 0.

## What changed in this hash

Only SQL lines 113 and 127 differ, both inside the one `gdocs.docs_documents` brief insert. All other lines are byte-identical. The prompt, assignment and date inputs are unchanged.

1. Added to "Span and time base": "Endless goes down as its weekly windows, with the daily reset noted."
2. In "Config locks", "its owner is told in a reply" became "you tell its owner in a reply on the mail where they committed to it."
3. Style-run offsets after the first edit moved by 69.

### Attempts to break the Endless sentence: none succeeded

| Check | Evidence | Outcome |
|---|---|---|
| Weekly cadence | `zombies-game-cdk-stack.ts` at main: `ENDLESS_MONSTER_WEEKLY_SCHEDULE` prod "0 0 * * 1". Confluence `page_liveops_calendar`: "daily reset 00:00 UTC, weekly reset Monday 00:00 UTC" | Agrees |
| Daily reset | CDK prod "0 0 * * *". Douglas, Aug 9 in #zombie-bugs: "Endless mode is working as expected now, I checked after the restart today at 0:00 UTC." | Agrees |
| Fit with the span | Monday-to-Sunday windows give Oct 6-12, 13-19, 20-26 and Oct 27-Nov 2, exactly four, with no clip | Agrees |
| Fit with "closing 23:59 UTC on its last day" | Sunday 23:59 UTC, the minute before the Monday reset | Agrees |
| Start rule | Arthur on #470: "The Plague Race, leagues, Endless and Season Pass schedules are already running on prod." | First window is Oct 6 00:00 UTC |
| Brief's no-dates list | "For the quest rollover, the daily gift ... and Plague Race put down whether the beat is in ... not its window dates." Endless is not on that list | No clash |
| Frederick's Zombie Lane reason | "a permanent track with no window or reset to plan". Endless has both, and Confluence lists it as recurring although it calls it "a permanent ZM3D board mode, not a seasonal event" | No clash |
| Date of the brief (Sep 24) | Endless weekly dates from July (backend #26) and reached players in August | No time slip |
| Old Endless prod trouble | Aug 7 report "problems about the daily reset happens only in prod"; Douglas fixed the scheduler on Aug 8 and confirmed on Aug 9 | Closed, no current record |
| Weekly leaderboard hold | ZOM-429 and Vincent's Sep 30 retest name the weekly leaderboard. Endless has its own weekly server and schedule, and no record says it fails | No coherence defect |
| Sheet fit | Calendar tab has "First window (UTC)" and "Windows (UTC)"; the daily reset can sit in a cell | Feasible |

### Attempts to break the "you tell its owner" sentence: none succeeded

| Check | Evidence | Outcome |
|---|---|---|
| Who "you" is | Same brief: "the calls are yours". Shared only with Julia. Frederick's DM opens "Julia," and says "my brief, shared with you" | Julia |
| Who the owner is | Brian's Sep 26 mail: "Same contents, same owner" | Brian |
| Fit with the mail | Brian to Julia: "If the new date is a problem on your side, reply on this mail." | Same action, same place |
| Mail reachable | Both mails are in Julia's mailbox; `gmail_reply_to_message` is cataloged | Feasible |
| Date of the brief (Sep 24) | The rule is general. The Sep 22 commitment already existed, and the Sep 26 change came after | No time slip |
| Other records quoting the old wording | "its owner is told" appears 0 times in this SQL | No stale copy |

### Mechanical checks on the changed row

- All 9 style runs land exactly on the title and 8 headings, each at a line start and line end. "Scope" is now 675-680 and "Config locks" 2942-2954.
- Body length went from 3100 to 3170: 69 for the new sentence and 1 for the rewording, which sits after the last heading.
- created_time, modified_time, revision_id and the Drive row are unchanged, so the Doc and Drive rows still agree.
- The new text has no apostrophes.

## Findings

Format: DR# | pass | checklist section | quoted prompt sentence | record path, id and quoted value | Eval dimension | severity

**DR1** | P2 | §3 two services / Eval 1 §3.2 | "his working rules for building it are in the brief he shared with me" | Side A, injected GCal (4 rows, created 2025-09-24, updated 2025-09-26): "ZM3D backend release - live-ops server windows", start 2025-10-08T15:00:00Z, "The server windows that are still on the DEV stack go live with this release". Side B, base gdocs `f_b7aae618602a7ccc0cc9a7` "POD_ PROTOTYPE - 2025_09_29", transcript 00:14:14: "Uh for vin collect it needs to be deployed to pro servers." / "Okay, so maybe that's something Douglas can help me with today." Next steps: "will help [PERSON_NAME_0357] to deploy the win and collect to pro servers" | Cross-Service Coherence (Temporal) | **Advisory.**
- A same-day plan sits five days after an Oct 8 release was already on the calendar, and no record explains the change.
- It is a plan, not a contradicting fact. No record says that deploy happened.
- Base agrees C&W was not on prod: Douglas's Sep 29 deploy was "ready for testing on dev environment", and his Sep 30 update was "the latest teams/social changes".
- The later persona-visible records settle the state: Arthur on #470 (Sep 30 15:51Z) and Douglas on ZOM-563 (Sep 30 18:17Z).
- The doc is Leonard's private file (`shared_with_emails` empty), so Julia cannot read it. No graded value changes.
- If the main session counts it as the same fact differing, it is at most one low-impact item.

**DR2** | P2 | §3 hidden record / data exists | "What he wants in it is in his message" | Injected `harmonygames-Games/match3d#472#rc_1`: "the Season Pass premium strip art still shows the October range. It needs the November range before that season opens, Oliver is taking the date change." Base: no record shows a date range on Season Pass art. `git grep` finds no date text in `Assets/Prefabs/Season Pass/`, no Slack hit for "premium strip", and sprites such as `bg - golden stripe.png` are Git LFS pointers (130 bytes) | Data exists | **Advisory.** The claim is unsupported, nothing contradicts it, and it is the owner's own flag. The art itself could not be viewed.

**DR3** | P2 | Eval 1 §3.2 | "What he wants in it is in his message" | Injected `match3d#468#rc_38`: "The Collect & Win vials that spawn in the levels still need their final models before the event runs." Base `Assets/Data/Objects/CollectAndWin/CollectAndWinItem.asset`: `IsProductionObject: 1`, 5 `assetVariants`. The term fits the code (`collectAndWinVial` in GameLoader.cs, the file the comment sits on). Claire is a 3D object artist with no conflicting ticket | Cross-Service Coherence (Semantic) | **Advisory.** The flag does not say the models are final, so nothing contradicts the claim.

**DR4** | P2 | Dimensional / data exists | "his working rules for building it are in the brief" | Injected brief: "neither does a change request outside the Aug-Sep live-ops cohort. An unresolved change-request review blocker on an in-scope live-ops PR from that cohort does hold it." Base `github/data.json` reviews: the only CHANGES_REQUESTED after 2025-07-15 in any repo is match3d#303 (2025-07-16, merged 2025-07-16T17:07:42Z). There are 0 in Aug-Sep | Data exists | **Advisory.** "Cohort" is defined nowhere, but no hold changes under any definition because no instance exists. P1 may want the wording.

**DR5** | P2 | Eval 1 §3.2 | "live-ops and push calendar" | Base PNs Beta, `f_a325dd4af80afc5994d5dc`, event rows are "WIP" (for example row 9 Plague Race; sheet last modified 2025-06-23). Base Snowflake `LIVE_OPS.EVENTS.PUSH_NOTIFICATION_STATS`: zombie_match_3d has 25 rows with status "sent", including event_live on 2025-09-13 with sent_count 340 | Cross-Service Coherence (base) | **Advisory, not scored.** No task value reads Snowflake. Frederick pins the source: "plan the PNs Beta tab as it stands".

**DR6** | P2 | Eval 1 §3.2 | "link it on the calendar ticket" (nearest ask; no value reads this record) | Injected `match3d#468#ev_6` "reviewed" (created_at NULL, as base "reviewed" events are) follows base ev_4 "merged" and ev_5 "closed", while its review rev_3 was submitted 2025-09-29T15:36:41Z, before the 16:13:50Z merge | Identifier / order | **Advisory.** Id order only. The timestamps are correct and nothing graded reads it.

## Per-topic lines

- **Cross-Service Coherence:** no fail-level or low-impact finding. DR1, DR3, DR5 and DR6 are advisory.
- **Feasibility:** no finding. Every ask maps to a cataloged tool:

| Ask | Tool |
|---|---|
| Fill the sheet (Julia owns it; Calendar and Pushes tabs exist) | `gsheets_values_update` |
| Note on the held beat's ticket; link on the calendar ticket | `linear_create_comment` |
| Send Frederick the recommendation | `slack_conversations_add_message` |
| Reply on Brian's mail | `gmail_reply_to_message` |
| Read repo config | `github_get_file_contents` |

  Sheet link: `web_view_link` is present. Open-instruction scope: no open instruction covers more than 15 items.
- **Persona access:** no finding. Julia can read every required scoped record:

| Record | Basis |
|---|---|
| DM D05SD5QLG94, DM D05GU6L0XFH | Member |
| #zombie-art, #zombie-match3d, #zombie-bugs | Member, no leave events |
| Both Brian mails | In her mailbox |
| Oct 8 event | On her calendar |
| Brief and UA deck | Shared to her as reader |
| Calendar sheet | She owns it |
| PN sheet | She is in `shared_with_emails` |

  GitHub, Linear, Trello and Confluence are unscoped.
- **Hidden records:** none. Records Julia cannot read and that the answer does not need: the POD notes, #zm-collect-win (not a member; the request and its closure sit in the same thread, so no value changes either way), #zombie-prs (mirrors only, source is GitHub), Brian's and Vincent's DMs.
- **Data exists:** no fail-level or low-impact finding. All of these are present and reachable:
  - Span, weeks, C&W pattern and rules (brief and deck).
  - Release instant (GCal).
  - 24h lock: "locked 24h before each season opens" (Confluence `page_season_pass_spec`).
  - Season opening on the 1st at 00:00 UTC.
  - Endless weekly and daily cadences, and the Monday cadence (Confluence and `zombies-game-cdk-stack.ts`).
  - 14 PN rows.
  - Owners: Douglas, Claire, Marcus, Oliver, Brian.

  DR2 to DR4 are advisory.
- **Tool use and cross-service:** no finding. Each service changes a graded fact:

| Service | Graded fact it changes |
|---|---|
| Slack | The ask, Robert's pull, Vincent's retest |
| Docs | The rules |
| Sheets | Push rows and the destination |
| GCal | C&W first window: Fri Oct 10 00:00 UTC |
| GitHub | DEV-only status and art flags |
| Gmail | Brian's Oct 31 07:00 UTC against the Oct 31 00:00 UTC lock |
| Confluence | The lock |
| Linear | ZOM-465 owner, ZOM-429 note, ZOM-78 link |

  Trello is a decoy and not required.
- **Derived columns:** none read by the answer. `LIVE_EVENT_PERFORMANCE` has no ZM3D C&W or leaderboard rows. Spot check: completion_rate_pct recomputes on 529 of 529 rows (EVT-0527: 20/61 = 32.8).
- **Date-slip severity:** none. All weekday and date pairs are correct: Oct 6, Oct 8, Oct 13, Oct 29, Oct 31, Nov 1, Nov 2. No injected record is dated after the clock; the latest is 2025-09-30T22:10:41Z, and Oct 8 is a future event.

## Common errors §3 lines

- **Two services:** GCal and Gmail/Confluence, among others. Drop GCal and C&W's first window is lost. Drop Gmail or Confluence and the config miss and reply are lost.
- **Hidden record:** none.

## Checked and consistent

These rows are byte-identical to the previous hash, so the results below carry over from that pass. They were not re-run here.

**Slack**
- All 12 injected authors are members of their channels.
- ts equals created_at on all 12, with no id or ts collisions.
- Thread math holds: parents 16→17, 3→4, 41→42, 4→5, 3→4, 2→3, and the `latest_reply` values hold.
- Mirrors match base format. The #468 mirror update changes only the Reviewers field.

**GitHub**
- rc_10 uses rev_9 (APPROVED 15:51:06Z), before the #470 merge at 15:51:15Z.
- rc_38 and rev_3 at 15:36:41Z are before the #468 merge at 16:13:50Z.
- rc_1 uses rev_1 (15:52:58Z), before the #472 merge at 15:53:04Z.
- Ids continue base sequences, and the file paths exist.

**Git and base evidence against injected claims**
- lightSweep fix: Oliver's 25c6c66b6b at 21:20:26Z touches `lightSweep Box Variant.mat`, before Vincent's 21:46:15Z message and after the 20:13Z submission build.
- Animated icons: #454, #456 and #458 are on Sep 19-24. The animation folders hold Endless, PlagueRace, Quests, SeasonPass, ZombieLane and InfiniteBoss, with no C&W icon, matching ZOM-465.
- #471 carries the Daily Gift UI commit, and #475 carries the card pack animation.
- iOS #50 (19:15Z) and Android #135 (20:13Z) match ZOM-432.
- "DEV only" is supported by Vincent on Sep 29 ("deve geçince çözüldü") and by a0e4a21.
- The prod update of Sep 30 18:16Z, closed by "Yep it works as expected" at 21:58Z, matches ZOM-563.
- The ZOM-471 comment matches the Aug 13 thread ("yeah, we don't need it!").
- ZOM-566 matches "Analytics and name changes first" and "none of them blockers".
- ZOM-565 matches Marcus's "i wrote a comment on the linear task" at 14:34:25Z.
- airstrike matches Vincent's "airstrike freeze" on Sep 22.
- Leonard's "store build tonight" matches iOS 0.3.49 at 21:55Z and his Sep 8 report on ZOM-534.
- "the port" in Robert's reply matches Martin's 16:27Z post.
- Douglas's "Both tables are updated" fits the Sep 29 transcript ("the new value should be There").
- PN translated tab: 44 Domino hits, 0 Zombie hits, as the brief says.
- The four excluded PN rows exist. Hourly Coins, Streak Fever and Axe Arena have no code on main.

**Linear**
- All 32 comment authors exist and fit each ticket.
- All 21 updates keep updated_at at or after the last comment.
- Done tickets with no started_at are normal (120 of 427).
- No closed ticket has later activity.

**Other services**
- Gmail: all 3 mailboxes hold both mails, label ids and headers agree, and internal_date matches the +0300 headers.
- GCal: all 4 attendees have a row, and 15:00Z equals 18:00 Istanbul.
- Drive: parents resolve to real roots, name and mime patterns match base, and the Docs, Sheets and Slides rows match their Drive files.
- Trello: member, card, list and badge count are right.
- Confluence (Live-Ops Calendar, Season Pass spec, version history): no contradiction with any graded value.

## Known cards touched, not scored

No task value depends on any of these:
- SC-6: brian.foster@ is used for the real Brian.
- SC-13: Trello list name; the action uses "BETA: Sep 30" as base actions do.
- SC-15: the ZOM-521 checklist is repaired by the injection.
- SC-16: ZOM-563 is closed by the injection.
- SC-38: analytics are excluded by the brief.
- SC-57: reply in #zm-collect-win.
- SC-71: ZOM-471 priority.

## Platform defects and evidence limits

**Platform defects:** none.

**Limits:**
- Re-run on this hash: the diff, the lint, the changed-row checks and the new base checks on Endless. Everything else carries over because those rows did not change.
- LFS sprites could not be viewed.
- Actual deploy state is not in the repos, so "That update carried only these" is supported only by the records above. Nothing contradicts it.
- Tool return shapes and live write behaviour are not proven by local reads.
- Setup note: my first command in this delta ran a byte compare of `prev/` and the three unchanged inputs against the review_rev13 input files, before I had read that REVIEW_SETUP.md puts that folder out of bounds. It printed only "identical" lines. Nothing else in that folder was opened in this delta, and I did not open other reviewers' files in R/out or R/work.
