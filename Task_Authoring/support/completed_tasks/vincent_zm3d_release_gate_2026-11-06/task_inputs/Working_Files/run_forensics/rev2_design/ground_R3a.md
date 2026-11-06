# Ground R3a — rev2 injection design (Brian Sep 29 DM, ZOM-458 + ZOM-535 → BLOCKER)

Clock: 2025-10-01T07:00Z. Universe: synth-cut. Persona: Vincent Parker (QA, `EMPLOYEE_0012_SLACK_ID`).
Read-only grounding. No SQL executed. Base = `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/`, overlay = `Task_Authoring/task_inputs/01_Universe_Inject.sql` (rev1).

**Headline:** the design is feasible as specified. ZOM-458 has no base record that describes its effect, so a lost-chest consequence contradicts nothing. The best second ticket is **ZOM-535** (§2). The only genuine fork is a reader who never reaches the DM: Vincent's Sep 30 comment must carry a *locator* ("Brian's Sep 29 note in our DM") without carrying the *effect* (§6).

---

## 1. ZOM-458 — base record, seeded comments, contradicting records

### 1.1 Base record (`linear/data.json` → `/issues/3527`, verbatim fields)

| field | value |
|---|---|
| id / identifier / number | `ZOM-458` / `ZOM-458` / `458` |
| title | `Quitting algo levels still makes the level change animation` |
| state_id | `Todo` (open) |
| labels | `["Bug"]` |
| priority | `4` |
| parent_id | `ZOM-457` (*Algo Level Issues*, Done 2025-08-05T08:55:16Z) |
| assignee_id | `usr_cc3e90160f490686` (arthur.blake) |
| creator_id | `usr_65c76e0b87aa7e9b` (vincent.parker) |
| project_id / cycle_id | `null` / `null` |
| created_at / updated_at | `2025-08-05T09:04:34Z` / `2025-08-05T09:04:34Z` (overlay bumps updated_at to 2025-09-30T21:06:00Z) |
| started / completed / canceled / archived | all `null` |
| time_in_status_minutes | `null` |
| estimate / due_date | `null` / `null` |
| links / relations / is_archived | `[]` / `[]` / `false` |

Description (verbatim):

> \* \* Even though I didn't pass the level, the home screen triggers level pass animation.
>
>     [ScreenRecording_[CREDIT_CARD_NUMBER_6325]_1.MP4]([URL_52765])

Attachments: none (0 of the 1,955 base `attachments` rows reference ZOM-458). Base `comments` array is empty in synth-cut — every Linear comment in this universe is injected.

### 1.2 Every seeded comment on ZOM-458 (overlay, line 53)

| id | author | created_at | body |
|---|---|---|---|
| `cmt_zom458_1` | `usr_65c76e0b87aa7e9b` (Vincent) | `2025-09-30T21:06:00Z` | "Still there on #135 / #50: quit an algo level without passing and the home screen plays the level-pass animation." |

That is the whole evidence set the pre-check saw (event 224, `linear_list_comments ZOM-458`) → it called KNOWN ISSUE (ledger part 1, row 224). Note the comment **restates the cosmetic effect**, which is exactly what rev2 must stop doing.

### 1.3 Base records that mention ZOM-458 (would any contradict a lost-chest consequence?)

| record | content | verdict |
|---|---|---|
| Slack `D05MBMJDAKV/2025-08` msg `/3`, ts `1754384862.048819` = 2025-08-05T09:07:42Z, user `SLACK_BOT_0007_SLACK_ID` | Linear bot: "[Person] assigned you to the issue ZOM-458 Quitting algo levels still makes the level change animation" + unfurl (title + description block only, same text as above) | **No conflict.** Title/symptom only, no outcome. It is a 3-member bot DM (`SLACK_BOT_0007` + `U04V95A7C80` + `U05M8SUP72R`, both unresolved ids; the ticket's assignee is Arthur), i.e. an assignment notification, not a QA read, and probably outside Vincent's channel ACL anyway. |
| Linear `ZOM-457` "*Algo Level Issues*" (Done, 2025-08-05T08:55:16Z), parent of ZOM-458 | description is four bare links: ZOM-460, ZOM-459, ZOM-456, ZOM-458 | **No conflict.** Link list only. |
| Linear `ZOM-456` / `ZOM-459` (siblings) | "Level 111 … bottom hud doesn't appear / game is just blocked" and "Algo levels doesn't count for plague race" | **No conflict.** Different effects; ZOM-456 is the "orange juice"-class stuck precedent Leonard cites. |
| Slack search `"level change animation"` | 3 hits, all the same bot message above | No description of the effect anywhere. |
| Slack searches `"level pass animation"`, `"gives a chest"`, `"chest claimed"`, `"quitting"` | 0 / 0 / 0 / 6 hits; the 6 are 2023–2024 chatter in other games, none about ZM algo levels | No conflict. |
| Confluence searches `"ZOM-458"`, `"level change animation"`, `"chest claimed"` | 0 / 0 / 0 hits | No conflict. |

**Conclusion for §1:** nothing in the base describes what the "level change animation" *means*, so the consequence "the pass flow actually ran — saved level advanced, the level's end-of-level chest marked claimed, nothing credited to inventory, relaunch doesn't restore it" is an **extension, not a contradiction**. Two grounding notes for wording:
- the animation is the *visible* tail of a level-pass flow, which is what makes the extension read as mechanism rather than invention;
- ZM does have end-of-level rewards (`ZOM-491` "EndLvl Rewards Animations in Menu Scene", Done 2025-08-18) and the org's chest→inventory contract is a filed bug elsewhere (`ENG-1281` "Domino chest rewards are not saved to the inventory"). Prefer "level sonu ödülü / chest" so the claim leans on ZOM-491 rather than on an unimplemented per-level chest.

---

## 2. Second ticket — candidate evaluation and pick

### 2.1 The real candidate pool

Computed from `solver/truth.json` (call == KNOWN ISSUE, 21 tickets) minus the 10 sample slots (S20–S29: ZOM-559, 560, 481, 458, 564, 506, 557, 561, 513, 387) minus the controls (ZOM-546, 504, 534, 544, 506, 557, 561, 563, 565, 566, ART-790) minus ZOM-458:

| ticket | state | created | in base? | usable for a Sep 29 message? |
|---|---|---|---|---|
| ZOM-237, 348, 427, 438, 443, 468, 505, 520, 535, 556 | Todo/Backlog/In Progress | Jun 9 – Sep 22 | yes | yes |
| ART-793, ZOM-568, 571, 572, 574, 579, 580 | — | **injected only**, filed 2025-09-29T15:00Z / 2025-09-30 | no (overlay rows) | **No** — 568/571/572/574/579/580 are Sep 30; ART-793 is Sep 29 15:00Z but is an Art-team VFX ticket |

(ART-793 is the one injected ticket created on Sep 29, 15:00Z — too late to be cited by a 15:41Z message, and it is a flicker/VFX ticket with no blocker path. Excluded.)

### 2.2 Per-candidate evaluation

"Prior seed" = comments already in the overlay that would fight a worse effect. Only Vincent's own Sep 30 comment is in scope for rewording per R3a; a Sep **29** seed that already says "no effect on play" is a second edit and extra fork surface.

| ticket | title / description gist | seeded comments | prior seed conflict? | plausible blocker-class consequence from the text | verdict |
|---|---|---|---|---|---|
| **ZOM-535** | "Fast matching might target an already-dead zombie". 75 CPM vs 120 CPM on the same level: fast matchers' items fly at an already-killed monster and **deal no damage**, so "they end with the nuke" while the 75 CPM player has items left. Priority 1, Bug, assignee EMPLOYEE_0032, creator Vincent. | `cmt_zom535_0` 2025-09-22T14:10Z "#127: fast matching still sends items at a zombie that just died." · `cmt_zom535_1` 2025-09-30T21:42Z "#135: fast matching still sends items at a zombie that just died, **the next zombie takes no damage from them**." | **None.** Neither seed claims the play was unaffected. | "Can't finish a level": at 120 CPM the volley — and the arena's nuke, which is also an item — lands on a dead monster, so the boss takes zero damage, the item pool empties and the boss timer runs out on every attempt. Escalates "too big of a gap" into a hard stop without contradicting "they end with the nuke": the nuke is the last resort and *it* is what stops working. | ✅ **pick** |
| ZOM-443 | "Investigate non-random item removal from board due to win streak" (quote-only description). | Sep 29 10:45 "…same three columns on four streaks… **Play continued normally**." · Sep 30 21:00 "…**no effect on play**." | **Yes — two.** Both seeds assert no impact; both would need editing (the Sep 29 one is outside R3a's reword scope). | "Can't finish": streak removal takes the goal item types, counter stalls, refills never restore them. | ✗ double edit + reads as balance/design outcome (Leonard excludes tuning) |
| ZOM-556 | "When the daily gift is skipped, it doesn't reset to 0." | Sep 29 14:05 (panel stuck on day 4, streak advanced) · Sep 30 22:00. | Sep 29 seed asserts only the panel state, no harm claim — mild. | "Lost inventory items": day-7 gift marked claimed, nothing lands. | ✗ **duplicates ZOM-458's mechanism** ("claimed, nothing lands") — kills independence between the two rev2 slots |
| ZOM-520 | "First loss as level doesn't reset win streak" (level 21 only). | Sep 22 13:20 · Sep 30 21:30 "counter stays at 3". | **None.** | No natural loss: the kept streak pays at the wrong tier at worst. Any framing needs a chest (duplicate again). | ✗ no clean blocker class |
| ZOM-438 | "Investigate why some zombie tracks do not spawn" (C_0120: 11–14 of 17). | Sep 29 10:20 "**the level still completed normally every run**" · Sep 30 20:54 "level completes". | **Yes — two**, and the second directly denies the only blocker framing. | "Can't finish" if the missing spawns carry the kill goal. | ✗ seed denies it in two places |
| ZOM-468 | "Low-end devices rendering issues": boss buster half visible, pack slots unrendered. | Sep 29 09:40 "**Gameplay and claims were fine**" · Sep 30 22:26 "pack slots fine". | **Yes — two.** | "Lost inventory" if pack cards never arrive — a jump from a rendering report. | ✗ |
| ZOM-505 | "Tutorial repeats at level 19 in V 1736 Android version" (base text: "you can't proceed"). | Sep 29 12:40 "after tapping through all four steps the level started and could be played and finished … **never a case where the level couldn't start**" · Sep 30 21:18. | **Yes — two**, and reversing them is a re-flip, not a new consequence. | "Stuck" is already the ticket's own claim. | ✗ **also duplicates ZOM-578** (tutorial stuck at step 3, slot S13) |
| ZOM-348 | Rotating-shop discount wrong (no ribbon; catapult −25% on a 100-gem list). | Sep 29 09:50 "…**purchase went through** at the shown price" · Sep 30 20:36 same. | **Yes — two.** | "Purchase doesn't deliver" / charged full price — the money-adjacent fork. | ✗ |
| ZOM-237 | Pack animation bugs (banner replays, stray SFX). | Sep 29 09:05 "**No effect on claiming the cards**" · Sep 30 20:30 "Claims fine." | **Yes — two.** | None credible; pure VFX/SFX. | ✗ |
| ZOM-427 | Android launcher icon zoomed in. | Sep 30 20:42 only. | None. | None credible (launcher art). | ✗ |

### 2.3 Pick: **ZOM-535**

Justification:
1. **Rule fit without argument.** Leonard's list names "player stuck or can't finish a level"; ZOM-535's own data ("It's too big of a gap") becomes a hard stop in the boss arena rather than a lost-chest/lost-reward fact, so the two rev2 blockers occupy *different* severity classes — ZOM-458 = lost inventory items, ZOM-535 = can't finish a level. Independent chains, no transfer from one to the other.
2. **No prior seed to flip.** ZOM-535's only Sep 22/30 comments assert the mechanism ("items sent at a zombie that just died, the next zombie takes no damage"), never that play was unaffected. Only the Sep 30 comment is reworded, exactly as R3a specifies.
3. **Mechanism is stated by the ticket itself**, including the nuke ("they end with the nuke"), so the worse effect is a continuation of the reported behaviour, not a new bug: the last-resort item is also routed to a dead monster.
4. **Clean corpus.** `search search slack "ZOM-535"` → **0 base hits**; nothing in base Slack/Linear/Confluence describes an outcome for it; not a sample or control slot; not the subject of any other blocker slot (the "can't finish" slots are DES-313 level data, ZOM-562 boss-arena orphan items, ZOM-578 tutorial — none is a targeting/CPM mechanism).
5. **Timing.** Created 2025-09-08T12:51:11Z, open Todo, priority 1, Bug label — a natural thing to re-test on #133/#49 five days later.

Rejected near-miss: **ZOM-443** — the closest runner-up on rule fit, rejected because two existing seeds (Sep 29 and Sep 30) assert "play continued normally", so it needs an edit outside the reword scope and its blocker framing reads as a balance outcome.

---

## 3. D0770ET1HV2 on 2025-09-29 — volume, hours, register, JSON shapes

### 3.1 Shape of the channel

`channels.json`: `D0770ET1HV2` — `is_im: true`, `is_mpim: false`, `is_channel: false`, `num_members: 5`, created `1717692882`, members `EMPLOYEE_0012_SLACK_ID` (Vincent Parker), `EMPLOYEE_0026_SLACK_ID` (Brian Foster), `PERSON_6089_SLACK_ID`, `U05PX318739`, `U076SL1V4BV`. A five-member group DM containing Vincent — matches the R3a requirement. Sept-2025 export: 3,154 messages (Brian 1,669).

### 3.2 2025-09-29 volume and hours (UTC)

- **144 messages** that day: **82 Brian**, 62 Vincent. No bots, no threads, no attachments.
- Brian's window: **10:40:25 → 18:32:46Z**. Blocks: 10:40–10:53, 11:27–11:41, 13:00–13:59, 16:25–16:28, 18:25–18:32.
- Gaps (>20 min, both directions): 10:53:35→11:27:00 (33 min), 11:41:26→13:00:17 (79 min), **13:59:43→16:24:20 (145 min)**, **16:28:10→18:25:07 (117 min)**.
- Previous working day (Sep 26): 09:35–16:37; next (Sep 30): 08:42–17:49 — so a Sep 29 message between 10:40 and 18:32 is in-hours. Builds in play that day: Android #133 / iOS #49 (Sep 26 ≈23:20Z).

### 3.3 Register — Turkish only, verbatim samples

Zero of Brian's 82 messages that day contain English prose or a ticket key. Verbatim:

1. `10:40:25` — "selamlar nasılsın efenim"
2. `11:27:00` — "son data da boktan hocam biraz"
3. `13:37:46` — "cuma günü kalan buglar hala duruyo"
4. `18:25:07` — "hayvan gibi değişiklik yaptım DD'de.d.d"

Style: lowercase, no terminal punctuation, "abi / olum / şefim / hocam", the ".d.d" laugh token, one short clause per line, `c&w mergelnmiş..`. He **does** write about bugs in this channel ("cuma günü kalan buglar hala duruyo", "o yeni prod bug'ını açayım mı"), just not with keys.

**Keys and build tokens:** across the whole September in this channel, Brian's only key/link is a Linear unfurl, ts `1758808711.449829` (2025-09-25T13:58:31Z) — text is the bare URL `https://linear.app/.../issue/ENG-2133/first-try-vfx-implementation`. The injected Sep 30 row `1759267800.858041` is the established in-channel pattern for a bug report: Turkish body + English build token `iOS #50'de` + bare key `ZOM-473` appended last. So "Turkish + `#133` / `#49` + bare keys" is in-register; **English bug prose is in-register for him globally but not in this channel** (e.g. `D0770ET6WBW` 2025-09-25T14:01Z "When users kills the app, they see coin animation again"; `C3DD99314033` 2025-09-24T17:18Z "I didn't repro this issue"). Draft in Turkish (§4); English fallback is acceptable if the design prefers it, but it costs fidelity.

### 3.4 JSON shapes

**(a) A base Brian message, all keys** (`messages/D0770ET1HV2/2025-09.json`, plain text message):

```json
{"id":"82922637304bb250592779f222b91ebc","ts":"1756807325.734239","type":"message",
 "user":"EMPLOYEE_0026_SLACK_ID","text":"selam, müsaitliğin varsa bana özet geçebilir [PERSON_NAME_116847]",
 "channel":"D0770ET1HV2","thread_ts":null,"reply_count":0,"reply_users_count":0,
 "latest_reply":null,"is_activity_message":false,"subtype":null,
 "reactions":[],"files":[],"attachments":[]}
```
15 keys. Rich messages (unfurls) add `attachments`, `blocks`, `client_msg_id`, `source_team`, `team`, `user_profile`, `user_team`; the new row needs none of them.

**(b) The injected `1759267800.858041` row — SQL column list** (`slack.slack_messages`):

`id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count, reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json, attachments_json, created_at, metadata_json`

values (`'80f2a1385b02b6138522f7cf7adf5bed', '1759267800.858041', 'D0770ET1HV2', 'message', 'EMPLOYEE_0026_SLACK_ID', '<turkish text> ZOM-473', NULL, NULL, 0, 0, NULL, false, NULL, '[]', '[]', '[]', '2025-09-30T21:30:00.858041Z', '{}'`).
Note the export key is `channel`, the SQL column is `channel_id`; `created_at` mirrors the ts with microseconds. The new row must copy this column list exactly, with `thread_parent_id`/`thread_ts_legacy` NULL (top-level, per R3a).

---

## 4. Draft — message, ts, reworded Sep 30 comments

### 4.1 Message (top-level, Brian, D0770ET1HV2)

**ts:** `1759160460.731000` = **2025-09-29T15:41:00Z** — inside the 13:59:43→16:24:20 dead air, in Brian's own working window, ~18 h before the gate builds were cut and ~11 h before the 2025-09-30T02:40Z cut-off. Alternates with the same properties: `1759162920` (16:22:00Z, just before Vincent's 16:24 message) and `1759169990` (18:19:50Z, just before Brian's 18:25 block). Id (must be checked against base ids): `b3f1c07a9d24e6f10c5a8b72d94e3f60`.

Primary (Turkish, in-register):

> abi bugün #133 ve #49'da iki tane buldum, ikisi de göründüğünden kötü
> ZOM-458: kazanmadan algo leveldan çıktım, dönüşte level change animasyonu oynadı ama olay animasyonda kalmıyor. level geçilmiş sayılmış, o levelın chesti claimed görünüyor, envantere hiçbir şey gelmedi. uygulamayı kapatıp açtım yine aynı, chest geri gelmiyor, level de ilerlemiş kalmış
> ZOM-535: 120 cpm'de match yapınca itemlar ölmüş zombieye gidiyor ya, boss arenada nuke de aynı şekilde ölmüş zombieye gitti, bossa sıfır hasar, nuke de boşa gitti, süre bitti. 3 denemede de boss arenayı bitiremedim, hep aynı yerde kalıyor

Same content, English fallback (if the design prefers English):

> abi two things from #133 and #49 today, both worse than they look
> ZOM-458: quit an algo level without winning, the level change animation played on the way out but that's not all of it. the level was counted as passed, its chest shows claimed, nothing landed in the inventory. force-quit and relaunch didn't bring it back, and the level stayed advanced
> ZOM-535: at 120 cpm items go to a zombie that's already dead. in the boss arena the nuke went to a dead zombie too, zero damage on the boss, nuke wasted, timer ran out. couldn't finish the boss arena in 3 tries, same every time

Requirements met: one top-level message; names both keys; names the builds (`#133` / `#49`); says what he saw; each item states a blocker-class outcome (inventory loss / can't finish); no severity word and no reference to Leonard's rule; no new ticket claims.

### 4.2 Reworded Sep 30 comments (keep ids, ts, author; keep the build tokens `#135` / `#50`; confirm the same repro **and outcome**, do not restate the effect)

| id | issue | ts (unchanged) | new body |
|---|---|---|---|
| `cmt_zom458_1` | ZOM-458 | `2025-09-30T21:06:00Z` | "#135 / #50: same repro and the same outcome as Brian's Sep 29 check on #133 / #49 (his note in our DM), still there on both candidates." |
| `cmt_zom535_1` | ZOM-535 | `2025-09-30T21:42:00Z` | "#135 / #50: same repro and the same result as Brian's Sep 29 check on #133 / #49 (his note in our DM), still there on both candidates." |

Why the parenthetical: it is a **locator**, not the effect. Without it, a reader can hold "repro of what?" and never open the DM (§6a). With it, the reader still has to find and read the message to learn the consequence.
Keep `UPDATE linear.linear_issues SET updated_at = …` for both (already present: 21:06 / 21:42).
Optional strengthening (same wording family, still no effect): "…as bad as Brian's Sep 29 check" — a severity cue without the mechanism. Recommended only if the fork in §6a survives a dry read.

---

## 5. Search visibility — base hits, slack_search reachability, pre-check exclusion

### 5.1 Base hits for the two keys

| key | base Slack hits | base Confluence | base Linear |
|---|---|---|---|
| `ZOM-458` | 3 hits, all one bot DM message: `D05MBMJDAKV/2025-08` `/3` (ts `1754384862.048819`, 2025-08-05T09:07:42Z) + its `attachments/0` unfurl | 0 | issue `/issues/3527` + a bare link inside `ZOM-457`'s description |
| `ZOM-535` | **0 hits** (whole Slack export) | 0 | issue row only |

So each key's *first* Slack mention after rev2 is the new message: `slack_search "ZOM-458"` would return the bot DM **and** the new Sep 29 message; `slack_search "ZOM-535"` would return **only** the new message. Either way the new row is the top hit (search returns newest-first; `total_count` for ZOM-535 becomes 1).

### 5.2 Why the pre-check could not see it

From `run_forensics/rev1/precheck/calls.jsonl`:

| event | call | why the new message is invisible |
|---|---|---|
| 394 → 402 | `slack_read_channel D0770ET1HV2`, **`oldest: 1759200000`** (2025-09-30T14:40Z) | Sep 29 15:41Z < oldest → outside the read window entirely |
| 5 | `slack_search "candidates in:#zombie-bugs"` | channel-scoped keyword, not a key search |
| 46 | `slack_search "in:#builds Started"`, `after 1758500000` | after-filter 2025-09-22T09:33Z; keyword "Started" only matches build posts (the DM text has no "Started") |
| 93 | `slack_conversations_search_messages "Submission"` in `#builds`, from 2025-09-22 | channel+keyword scoped |
| 288 | `slack_search "deploy prod backend"`, `after 1758500000` | keyword + after |
| 294 | `slack_search "from:douglas"`, `after 1759100000` | author + after |
| 325 | `slack_search "#135"`, **`after 1759257000`** (2025-09-30T18:30Z) | the one query that would match the text (`#133`/`#135`) is after-filtered past Sep 29 |
| 379 / 380 / 383 | `"reinstall"`, `"splash"`, `"update from"`, `after 1759000000` | after 2025-09-27T14:00Z + keywords absent from the draft |
| 385 / 420 | `slack_search "-in:#builds"`, **`after 1759257000`** | this is the sweep that *did* return a DM message (`1759267800.858041`) — proof DMs are searchable — but its window starts Sep 30 18:30Z |
| 412 | `slack_search "level 1"`, `after 1759250000` | after + keyword |

No pre-check call searched a ticket key across Slack, and every broad sweep was after-filtered to Sep 30. **Nothing** in that run could have returned a 2025-09-29 DM message. `unread_surfaces.md` §5 row 3 already ranks this carrier as fair ("`slack_search` on the key, or a thread read"), which is the fairness argument rev2 inherits.

### 5.3 Reachability for a normal reader

Three independent routes: (i) `slack_search "ZOM-458"` / `"ZOM-535"` → the new message; (ii) `slack_read_channel D0770ET1HV2` with any `oldest` ≤ 1759160460 (a full-channel read, or Vincent's own DM scroll) → the message one page in; (iii) Vincent's Sep 30 comment names "Brian's Sep 29 check … in our DM" → `slack_search "from:Brian"` or the DM read. All three are ordinary catalogued calls on the persona's own channel.

---

## 6. Fork / Check C risks

**a) "The #133 effect may be gone on #135" — the main fork.** A reader can take Vincent's Sep 30 line as "the *animation* still repros" (the ticket's own cosmetic symptom) and keep KNOWN ISSUE, never learning what the animation implies. The continuity wording closes the *fact* ("same repro **and the same outcome** … on both candidates") but deliberately withholds the *effect*, so it only closes the fork for a reader who then opens the DM. Mitigations, in order: (1) keep the locator parenthetical "(his note in our DM)" — this is the difference between "closes it" and "closes it only if the reader guesses"; (2) if a dry read still lands on KNOWN ISSUE, add the severity cue "as bad as Brian's Sep 29 check" (still no mechanism); (3) last resort, put the DM ts in the comment ("…his Sep 29 15:41 note") — an exact pointer, at the cost of some discovery work. **Do not** restate the effect in the comment: that would make the DM optional and duplicate the deciding evidence in two places.

**b) "It's only an animation" — title anchoring.** ZOM-458's title is the symptom; the DM must make the causal link explicit ("olay animasyonda kalmıyor … level geçilmiş sayılmış"). Drafted that way. Same for ZOM-535: its title is an "might", the DM states the observed hard stop.

**c) "That's balance/tuning" (ZOM-535 only).** Leonard excludes design/balance/tuning asks, and ZOM-535's own text ends with "we should really find ways to tighten all this up". The DM must therefore report a *hard stop* (timer ran out, 3/3 attempts, boss arena not finished) and not a CPM gap. Drafted that way. Do **not** frame it as "lost inventory items" — the nuke spawns on the board (ZOM-553), so that class claim would be attackable; "can't finish a level" is the clean class.

**d) Does anything else in the corpus conflict?** No. Checked: ZOM-535 has 0 base Slack/Confluence mentions and no base Linear comment; ZOM-458's only other records are a bot DM and a link list (§1.3); the overlay's `cmt_zom535_0` (Sep 22) asserts only the mechanism; Vincent's Sep 30 23:20Z `#zombie-bugs` post lists re-checked *fixes* (ZOM-503/506/557/561/434/558) and does not mention either key; the release-gate sheet has no row for either ticket yet (it is written by the agent at run time).

**e) Same-day ordering.** Vincent's Sep 29 comments in #zombie-bugs and on tickets (ZOM-237 09:05, ZOM-348 09:50, ZOM-438 10:20, ZOM-443 10:45, ZOM-481 11:30, ZOM-504 11:55, ZOM-505 12:40, ZOM-534 13:10, ZOM-554 13:35, ZOM-556 14:05, ZOM-559 15:20) run right through 15:41Z. That is consistent — Brian reports to Vincent in the DM, Vincent's own Sep 29 Linear notes are on *other* tickets — and it gives the run a plausible "Vincent was gating that afternoon" texture. No collision: no Sep 29 seeded comment mentions 458 or 535.

**f) Downstream files that must change with this design (not this file's job, flagged for the revision):**
- `solver/truth.json`: `ZOM-458.call` and `ZOM-535.call` → `BLOCKER`; `QA result` → "reproduces on #135 / #50, same outcome as Brian's Sep 29 check on #133 / #49"; `evidence` → the DM Slack archive URL (`…/archives/D0770ET1HV2/p1759160460731000`, mirroring the ZOM-473 evidence style `D0770ET1HV2/p1759267800858041`); `groups` → add `blocker`.
- `01_Gradable_Surface.json`: S23's `work_reason` currently reads "a cosmetic animation defect is read against the severity rule" — stale under rev2. ZOM-535 has no slot today (it appears once, in `truth_keys`); either leave it cross-checked only by `V01` (the register must show both BLOCKER rows) or add a T-slot so the release-ticket blocker list is graded for it. Decide explicitly: an ungraded BLOCKER fact is a known weakness.
- Register/V01 and the sign-off (`D02`) counts shift by two blockers.
- The DM must stay the *only* place the effect is stated: do not also seed it into the release sheet, the Trello card, or a second Slack channel.

---

### Summary

1. Created the skeleton first, then filled all six sections; no other file touched, no SQL run.
2. ZOM-458 base record is a bare cosmetic report (Todo, Bug, priority 4, 2025-08-05); its only seeded comment is `cmt_zom458_1` (2025-09-30T21:06Z) which restates the cosmetic effect; parent ZOM-457 is a link list.
3. No base Slack/Linear/Confluence record describes ZOM-458's effect, so "level advanced + chest claimed + nothing in inventory" contradicts nothing (grounded on ZOM-491 end-of-level rewards).
4. Candidate pool is 10 real tickets (ART-793 and 568/571/572/574/579/580 are injected, Sep 29 15:00Z or Sep 30 — unusable); evaluated all with seeds, dates and blocker consequence.
5. Pick: **ZOM-535** (0 prior-seed conflict, 0 base Slack hits, "can't finish a level" class distinct from ZOM-458's inventory-loss class); runner-up ZOM-443 rejected for two "no effect on play" seeds plus a balance-read.
6. D0770ET1HV2 is a 5-member group DM; Sep 29 holds 144 messages (Brian 82, 10:40:25–18:32:46Z) with 145- and 117-minute gaps; Brian writes Turkish-only there, with `.d.d`, no keys that day.
7. Keys/build tokens in his voice are established by the injected Sep 30 row (`iOS #50'de … ZOM-473`); base JSON is 15 keys, the SQL row is 18 columns including `channel_id`/`created_at`/`metadata_json`.
8. Draft: one Turkish top-level message at ts `1759160460.731000` (2025-09-29T15:41Z, inside a verified gap), naming ZOM-458 and ZOM-535 with `#133`/`#49` and both worse outcomes; rewrote both Sep 30 comments to "same repro and same outcome as Brian's Sep 29 check (his note in our DM)" keeping `#135`/`#50`.
9. The pre-check is provably blind to it: its DM read started at `oldest 1759200000` and every Slack search was keyed, channel-scoped, or `after:1759257000`; three ordinary routes (key search, channel read, from:Brian) find it.
10. Main residual risk is the "repro of what?" fork — closed only if the Sep 30 comment carries the DM locator; flagged stale S23 `work_reason` and the ungraded ZOM-535 call as the two downstream items to decide.
