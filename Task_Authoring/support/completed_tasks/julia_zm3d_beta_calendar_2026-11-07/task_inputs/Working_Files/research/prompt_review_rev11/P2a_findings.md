# P2 deep recheck, rev11: services, data and access (blind)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
SQL reviewed: R11/inputs/01_Universe_Inject.sql, sha256 1348d287ac4a105c41b9f0bf511c6664e306adcc3cf42406688a228fd4b684e7 (read, never executed)
Compared with: R11/prev/01_Universe_Inject.rev10.sql, sha256 ffbac4586fb91842ca16263c2b76987c26623c7ed689e00d33886c63f9331bdc. Prompt is byte-identical.

## Result

| Severity | Count | Items |
|---|---|---|
| Fail-level | 0 | |
| Low-impact | 0 | |
| Advisory only | 4 | DR2, DR5 (carried); DR6, DR7 (new) |
| Closed since rev10 | 3 | DR1, DR3, DR4 |

Scope: rev11 has 110 statements (80 inserts, 30 updates) against 107. 14 statements changed, 3 are new, 0 removed, and 93 are byte-identical, so their rev10 results carry over. I tried to break all 17 touched statements against the base and the other injected records (table below).
`hg.py lint --sql`: 0 FAIL, 0 CHECK, 0 INFO.

The one item a strict reader could try to raise is DR6, because the SQL now writes into a channel on a known-issue card. The main session should open it first.

## What happened to DR1 to DR5

**DR1, premium strip: CLOSED.**
- Rev10 L160: "the Season Pass premium strip is still set to the October range."
- Rev11 L164: "the Season Pass premium strip art still shows the October range." The L166 mirror text equals L164 (checked programmatically).
- Base side, unchanged: `SeasonPassResponse.cs:8` `[JsonProperty("end_time")] public DateTime EndDate;`, and no date field in code.
- The note now speaks of art, so it no longer implies a code setting that does not exist. The sprites are 130-byte pointers, so the art stays unread. That is an evidence limit, not a finding.

**DR2, Queue Manager: STANDS, advisory, unchanged.**
- Side A: rev11 L186 `cmt_zom543_1`, 2025-09-30T16:20:37Z: "Queue manager is in progress. Adding panel-order entries as each live-ops feature lands". Post-SQL ZOM-543 is `In Progress`.
- Side B: trello/data.json card idShort 63 "Queue Manager", action 2025-09-30T16:40:22Z: `{"dueComplete": true}`.
- Both statuses are base. The comment explains the open ticket. No graded value reads either status.

**DR3, UA deck: CLOSED.**
- Rev10 slide 2: "Small scale at first, scaled up week by week if the cohorts hold." Rev10 slide 1: "Scaled beta-cohort buy".
- Rev11 L134: "Beta-cohort buy, starting once the stores approve the Sep 30 builds."
- Rev11 L141: "Small scale at first, any scale-up comes after the pivot call."
- Rev11 L144: "we start buying users at small scale and hold the spend there until the pivot call."
- All three slides now agree. A scan of the SQL finds no other scale wording.

**DR4, Trello list name: CLOSED.**
- Rev10 L253: `"list":{"id":"6851a674975da1fe76e70d93","name":"BETA: Sep 30"}`.
- Rev11 L258 has no `list` key, and "BETA: Sep 30" has 0 hits in the SQL.
- The base list row "BETA: Oct 10" against base actions remains SC-13, base only. No injected record repeats it now. The change creates the small format note DR7.

**DR5, change-request rule: STANDS, advisory, unchanged.**
- Side A: rev11 L119, brief: "An unresolved change-request review blocker on an in-scope live-ops PR from that cohort does hold it."
- Side B: github/data.json `reviews`: since 2025-06-01 only match3d-backend#4 (2025-06-06, 2025-06-10) and match3d#303 (2025-07-16) have CHANGES_REQUESTED. Both are merged, and no Aug-Sep row exists.
- The rule is inert for holds. "Aug-Sep live-ops cohort" stays undefined, which is a P1 clarity lead.

## New findings

`DR# | pass | checklist section | quoted prompt sentence | record path, id and quoted value | Eval dimension | severity`

**DR6** | P2 | Known base card SC-57 | "What he wants in it is in his message, and his working rules for building it are in the brief he shared with me."
- Side A: rev11 L35, slack_messages 7d70c775, channel C09EVVCFHKR, 2025-09-26T16:22:44Z, Douglas: "Both tables are updated."
- Side B: slack/channels.json C09EVVCFHKR (#zm-collect-win): `"is_archived": true`, `"is_private": false`. The channel has 102 base messages through 2025-09-30 16:50:02 and no channel_archive event. 85 of the 90 archived channels have one.
- SC-57 is the known card for this mismatch. The SQL now writes into the channel, so the task touches the card for the first time.
- Why it stays advisory:
  - The archive flag carries no date, and the new row sits four days before the channel's last base post, so it adds no post-archive activity.
  - The card's don't-grade item is posting there, and the task asks for no post.
  - The archive flag changes no graded value.
  - The reply and Brian's ask share one thread, so they have the same visibility: no hidden-record asymmetry.
- Limit: Julia is not a member of this public channel, and the bundled references do not settle whether non-members can read it. If they can, this reply is what closes Brian's Sep 26 reward-table ask, a post-brief config item, and the graded still-to-do set would lean on a row in an SC-57 channel. That is the case to weigh.
- Cross-Service Coherence (State / Lifecycle wording, base flag) | advisory.

**DR7** | P2 | Format, one action row | "Frederick messaged me yesterday asking for the live-ops and push calendar for the Zombie Match 3D beta"
- Side A: rev11 L258 data_json keys are `board`, `card`, `text` only.
- Side B: trello/data.json: all 12 commentCard actions on this board carry `idCard`, `list`, `text`, `textData`. Across all boards 54 of 56 carry `list` and `textData`.
- One base comment has exactly the new shape and one more adds only `embedly`, so the shape is rare but not foreign. The row's `idCard` column is set, `text` is intact, and the answer reads only `text`.
- Cross-Service Coherence (Identifier / Format) | advisory.

## Every changed and new statement

| Line | Change | Break attempt | Result |
|---|---|---|---|
| L13 | Frederick reply: "Two things on top of the brief." | Against brief and row count | Consistent. Two topics, four rows still match PNs Beta. |
| L15 | Robert: "for one week of the beta", "if it lands in time" | Against L17 and Martin's thread | Consistent. "the themed prop set I okayed in Martin's thread" still resolves. |
| L17 | Robert drops "my later word..." | Against brief One-offs | Consistent. The brief carries the rule. |
| L27 | Vincent: "rides the next store build" | Against git and #builds | Consistent. lightSweep commit 25c6c66b6b is 21:20:26Z, after iOS #50 (18:43) and Android #135 (18:45) started. No later store build exists. |
| L35 | New Douglas reply | Author, parent, order, collisions | Consistent, except DR6. Douglas is a member; parent 0069f614 exists and its text mentions him; ts equals created_at; he was active at 16:06:51; no id or ts collision. |
| L37 | Parent counts | Against base | Correct. rc 2 to 3, users 1 to 2 (Brian, Douglas), latest_reply equals the new ts. |
| L109 to L127 | Brief: Clip rule; Collect & Win closes 23:59; "same beat"; held beat keeps windows; "any time before it" | Against code, Confluence, sheet headers | Consistent. All nine style_run offsets land on their headings (body 2,992 chars). W4 Fri-Sun closes on the span end. Weekly Leaderboard's usual window exists: CDK `LEAGUES_SCHEDULE: props.production ? "0 0 * * 1"`. |
| L134, L141 | Deck wording | Against slide 3, Slack | Consistent (DR3). |
| L164, L166 | #472 note and mirror | Against code, each other | Consistent (DR1). |
| L210 | New Brian comment on ZOM-465 | Against code, Marcus's notes, ZOM-526, ZOM-565 | Consistent. Order 18:05:02 then 18:13:41. All six IOrderableIcon classes (Endless, InfiniteBoss, PlagueRace, Quest, SeasonPass, ZombieLane) have animated prefabs; Collect & Win has none. So "the one event icon with no animation" matches main. It sits on a different item from his "can follow" notes. |
| L211 | ZOM-465 updated_at 18:13:41Z | Against last comment | Correct. State stays In Progress, matching open work. |
| L222 | ZOM-504 "Re-tested:" | Against ticket | Consistent. Vincent is the creator and tester. |
| L240 | ZOM-542 Regression to Todo | Against comment, git, Slack, Trello | Consistent. It removes a state that did not fit "Picking this up after the bug list." No PR, branch or commit names ZOM-542. started_at stays null. |
| L255 | ZOM-563 comment shortened | Against base DM | Consistent. Douglas 18:16:33 prod update; Vincent 21:58:44 "Yep it works as expected". Apostrophe doubled. |
| L258 | Trello data_json trimmed | Against base shape | DR4 closed, DR7 new. Card update lines unchanged. |

One timing note, not a finding. Brian's "does have to land before the beta" (18:13:41Z) comes 30 minutes before the Sep 30 submission builds started, and those builds went without the icon. That is why the item is still to do. Vincent's "next store build" shows a later build exists, and no record rules it out before Collect & Win's first window.

## Per topic

| Topic | Result |
|---|---|
| Cross-Service Coherence | No finding at fail or low-impact level. DR2, DR6, DR7 are advisory. No status contradicts its own record's activity. |
| Feasibility | No finding. Asks and tools unchanged from rev10. No open instruction. |
| Persona access | No finding. All required scoped reads remain visible to julia.lawson@harmonygames.co. Whether she can read #zm-collect-win is open, but the ask and the reply share it (DR6). |
| Data exists | No finding. The new "usual windows" rule has data (CDK). DR5 stands. |
| Tool use and cross-service | No finding. The drop test from rev10 still holds. |
| Hidden records | None. |
| Derived columns | None. No Snowflake read. |
| Date-slip severity | No finding. No changed statement alters a date, order or window except the added closing time, which is a stated rule. |
| Platform defects | No PLATFORM:FD-2880 or FD-3785 hit. PNs Beta rows 7 and 14 still carry the source token `[PERSON_NAME_2549]`; do not score it. |

## Carried unchanged from rev10

These statements are byte-identical, so the rev10 evidence stands: Gmail (all), GCal (all), Drive rows, Sheets rows, slide structure, GitHub reviews and timeline, #468 and #470 notes and mirrors, Slack rows other than L13 to L37, all other Linear comments and updates, and the Trello card update.

## Evidence limits

- Sprite PNGs are pointers, so art content is unread (DR1).
- Prod deployment state exists only as human statements.
- Tool return rendering is unverified.
- Non-member read of a public archived channel is not settled by the bundled references (DR6).
