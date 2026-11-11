# Injected-record audit vs base universe: Brian's mails, GCal release, brief, UA deck, Drive, Trello

Scope: slices (a)-(f) of `inputs/01_Universe_Inject.sql` against `Universe_SynthCut/` (clock 2025-10-01 07:00 UTC). SQL read only, never executed. Nothing written except this file.

Path shorthand
- `SL/<channel>/<month>.json[i]` = `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/slack/messages/<channel>/<month>.json`, array index i
- `GM/<file>` = `Universe_SynthCut/SynthCut_HarmonyGames_Gmail/Services_Data/gmail/threads/<file>`
- `CF/<page id>` = `.../confluence/confluence_working.json` page
- `TR` = `.../trello/data.json`; `GC` = `.../gcal/data.json`; `GD` = `.../gdrive/data.json`; `GS` = `.../gsheets/data.json`; `SF` = `.../snowflake/snowflake.json`
- `GH/root/...` = `Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/root/harmonygames-Games/...`

---

## 1. Headline

No injected statement in my slice is flatly contradicted by a base fact, apart from the already-known Trello placement. There are four things a strict reviewer can still pin on base data, in this order:

1. **Trello comment** (known): on a card completed 2025-06-30. Target found (card #61). Three further base mismatches come with the move: list name in the action payload, author, and the card's named owners.
2. **Gmail thread ids**: both ids decode to instants later than the mails; the Sep 26 one decodes to **2025-10-02 02:24:38 UTC (after the clock)** and is larger than every base thread id. The same numeric id is reused in three mailboxes, which base never does (0 of 61,819).
3. **"Beta buy starts Mon Oct 6" vs base beta-date signals**: Trello list is named `BETA: Oct 10`; CEO DM on Sep 25 says "We can barely get the beta out by mid october". Base also supports the injection (Confluence "end-of-September beta submission", Sep 30 submission builds #50/#135). Tension, not contradiction.
4. **Oct 8 backend release**: nothing in base gives another date, and Confluence says Collect & Win is "not yet live". But base shows Douglas updating prod on Sep 29 and Sep 30, after the event was created. Inference risk only.

Everything else is confirmed or uncontradicted, with a handful of format/plausibility deviations listed in section 4.

---

## 2. Claim table

Verdicts: CONFIRMED / UNCONTRADICTED / CONTRADICTED / TIMING CONFLICT (hard) / TENSION (soft, base statements pull the other way without stating the opposite) / FORMAT (deviates from base convention, no fact at stake).

### (a) Brian Foster's mails (Sep 22 and Sep 26, three mailboxes each)

| # | Claim | Verdict | Evidence locator |
|---|---|---|---|
| a1 | November season opens Sat Nov 1 | CONFIRMED | `CF/page_season_pass_spec`: "production seasons reset monthly on the 1st at 00:00 UTC"; `GH/root/match3d-backend/zombies-game-cdk/lib/zombies-game-cdk-stack.ts` L186-189 `SEASON_PASS_SCHEDULE ... "0 0 1 * *"`; `SL/D07GY332589/2025-09.json[311]` Douglas 2025-09-30T23:01:01Z "The event resets the very first day of the month in prod"; `SF` LIVE_EVENT_PERFORMANCE EVT-0527 Season Pass zombie_match_3d 2025-09-29..2025-09-30 completed. Nov 1 2025 is a Saturday. |
| a2 | Handoff "agreed with Product" for Wed Oct 29 | UNCONTRADICTED | No base record of any handoff date (Slack since Aug: "oct 29/31", "nov 1", "handoff", "hand over" = no relevant hit; Gmail 7 mailboxes since Aug 15 = none). "Product" = Robert is base-true: `CF/page_season_pass_spec` and `CF/page_zm3d_gdd` "Owner: Robert (Product). Design partner: Julia Lawson". Oct 29 is a Wednesday. |
| a3 | Config = reward tiers, daily and weekly quest tables, premium track | CONFIRMED (compatible) | Brian owns the live workbook: `GS` f_89aebb6083dc44501666c7 "Zombie Match Economy 1.0", owner brian.foster, tabs include `Season Pass - Free`, `Season Pass - Premium`, `Daily Quests`, `Weekly Quests`, `Daily Quest Chest`, `Weekly Quest Chest`. Spec points model: "daily_quest: 250". Spec lists season config as "(tiers, rewards, theme)"; quest tables are extra, not excluded. |
| a4 | Brian is the plausible owner | CONFIRMED | `TR` card #27 "Season Pass - ([PERSON_NAME_0092]/[PERSON_NAME_0022])" (0092 = Brian, per his mailbox "[PERSON_NAME_0092] <> Leonard 1:1"); `SL/D07GK9QQG7M/2025-08.json[128]` Brian 2025-08-19 "Here's the season pass reward tables / Free ... / Premium ..."; `SL/C08R6BF4ENN` 2025-09-04 14:35Z Vincent "up to @Brian"; Linear ZOM-552 "Season Pass Analytics" created by Brian. |
| a5 | "the September handoff" | UNCONTRADICTED | Loosely supported: reward tables shared Aug 19; 2025-09-19 15:38Z Brian DM "Can you check all the parameters in the Season Pass sheets?"; Season Pass reached production the week of Sep 22-29 (`CF/page_season_pass_spec`). No base record calls anything a "handoff". |
| a6 | "10:00 Istanbul time" | CONFIRMED | `GC` calendars: brian.foster time_zone `UTC+03:00`, julia.lawson `Europe/Istanbul`; Brian's invites render "(GMT+3)". Oct 31 10:00 Istanbul = 07:00 UTC, which is after the base lock ("locked 24h before each season opens" = Oct 31 00:00 UTC), so the designed miss holds against base. |
| a7 | To Julia, Cc Frederick | UNCONTRADICTED | Internally consistent across the six rows. |
| a8 | Thread ids 1844470925517303296 / 1844835127305531392 | **TIMING CONFLICT (format)** | Base: thread id >> 20 = arrival ms. Brian 134/134, Julia 25/25, Frederick 2,908/2,937 of 2025 threads are within 60 s. Injected ids decode to 2025-09-28T01:55:49Z and **2025-10-02T02:24:38Z**. Max base id 1844759654420061899 = 2025-10-01T06:25:02Z. |
| a9 | Same thread id in three mailboxes | FORMAT | Base: 0 numeric thread ids shared across mailboxes (61,819 mailbox-prefixed files). E.g. the same invite is 1806761895559412993 (blake), ...672218074 (douglas), ...460111598 (leonard). |
| a10 | Labels `UNREAD` / "Inbox,Category Personal,Unread" on Julia's Sep 26 copy | FORMAT | Julia's mailbox: 0 of 304 messages carry UNREAD or "Unread"; read state is `Label_b19fb8d1b3` = "Opened" (213 of 304). Same in Frederick's (0 of 5,474) and Brian's. By that convention Julia's Sep 22 copy (no "Opened") also reads as unread. |
| a11 | Sent-copy headers | FORMAT (cosmetic) | Base Sent copies carry only X-GM-THRID, X-Gmail-Labels, MIME-Version, Date, Message-ID, Subject, From, To, Content-Type (no Delivered-To, no Reply-To). Brian's two base sent mails are labelled `Archived,Sent`. His base Message-ID prefix is `CAPT--p4...`, injected `CAH4q9Z...`. |
| a12 | internal_date, Date, mbox_from, snippet | CONFIRMED | 1758532320000 = 2025-09-22T09:12:00Z; 1758872400000 = 2025-09-26T07:40:00Z; weekdays right; snippets are the 175-char body prefix; 09:12Z and 07:40Z sit in Brian's active hours (Slack Jun-Sep: 05-22 UTC). |
| a13 | SC-6 clash (Brian Cooper at brian.foster@) | UNCONTRADICTED | Julia's mailbox: no base mail from that address at all. Frederick's mailbox: 18 from "Brian Cooper <brian.foster@harmonygames.co>" (Craftsman+ CEO), latest `GM/frederick@harmonygames.co_1823332883409810377.json` 2025-09-09 "Re: Checking in", plus 1 from "Brian Foster" (2025-03-12 calendar acceptance). No content clash; the injected display name follows the majority base form. |
| a14 | Brian mails colleagues | UNCONTRADICTED (thin) | Brian's base mailbox has 2 sent mails ever (both 2025-01-30, to Vincent, empty subject). He is Slack-first (6,760 messages Jun-Sep). |

### (b) GCal "ZM3D backend release — live-ops server windows"

| # | Claim | Verdict | Evidence locator |
|---|---|---|---|
| b1 | Douglas organizes / runs the release | CONFIRMED | `SL/D079SNE2TL4/2025-09.json[58]` "I will make the deployment to prod then"; `[136]` 2025-09-16 "Deployments are done, ready for testing on both envs"; `SL/C08R27X0EAH/2025-08.json[450]` "I will check the jobs on prod after every deployment"; `CF/page_backend_services` "Owner: Douglas (Engineering)". He has organized one base event ("Quest discussion", 2024-06-05). |
| b2 | Windows still DEV-only, go live with this release | CONFIRMED (state), UNCONTRADICTED (date) | `CF/page_liveops_calendar` (v3, 2025-09-29T17:00Z): Collect & Win on ZM3D "Built for the end-of-September beta submission (QA blockers cleared 26 Sep 2025); not yet live"; "Windows are cron expressions in the CDK stack and do need a deploy to change". No ZM3D Win & Collect row in `SF` LIVE_EVENT_PERFORMANCE. |
| b3 | Date Oct 8 | UNCONTRADICTED, with TENSION | No base date for a next backend release (Slack "oct 8", "backend release", "release window", "prod deploy" since Aug = nothing; GCal has no release/deploy event at all; Linear ZOM = none; Trello = none). Fits Trello list `BETA: Oct 10`. Tension: base prod updates after the event's creation: `SL/D079SNE2TL4/2025-09.json[256]` 2025-09-29T16:47:43Z "the deployment is done" (Google login, env not named) and `[263]` 2025-09-30T18:16:33Z "I updated the prod environment with the latest teams/social changes". `GH/root/match3d-backend/lib/zombies_game/win_and_collect.ex` computes prod windows in code, so any prod deploy of `main` would carry them. Base never says that happened. |
| b4 | 15:00-16:00 UTC = 18:00-19:00 Istanbul | CONFIRMED | Istanbul is UTC+3. Oct 8 is a Wednesday. 09:00-10:00 in Douglas's zone (`America/El_Salvador`). No overlap with base recurring events for the four calendars. |
| b5 | Attendees Douglas, Frederick, Julia, Owen | UNCONTRADICTED | Owen is Douglas's Collect & Win counterpart (`SL/C09EVVCFHKR`, "[PERSON_NAME_0067]" = Owen). All four calendar ids exist; attendees alphabetical with `self` on the owner, as base. |
| b6 | Ids, uid, shape | CONFIRMED | No collision for the four `evt_` ids or the ical uid; `evt_`+22 hex and `<32 hex>@hg4` match base. Base export has no description field on any of 10,395 events, so this is the only event with a description. |
| b7 | created 2025-09-24T13:05Z, updated 2025-09-26T11:20Z | FORMAT (plausibility) | 07:05 and 05:20 in El Salvador. Douglas's Slack Jun-Sep: 0 messages at 07-10 UTC, 4 at 11, 0 at 12, 3 at 13. |

### (c) Brief "ZM3D beta live-ops calendar - working rules"

| # | Claim | Verdict | Evidence locator |
|---|---|---|---|
| c1 | Span Mon Oct 6 00:00 UTC - Sun Nov 2 23:59 UTC, "four buy weeks in my UA plan" | UNCONTRADICTED | Matches the injected deck; weekdays right. Frederick as UA owner: `CF/page_liveops_calendar` and `CF/page_product_okrs` "Owner: Frederick Stone (Growth/UA)". |
| c2 | Collect & Win runs Mon-Tue, Wed-Thu, Fri-Sun, each opening 00:00 UTC | CONFIRMED | `CF/page_liveops_calendar` table row; CDK stack L168-185; `win_and_collect.ex` L40-82 ("Monday at 00:00:00 UTC", hours 0-47 / 48-95 / 96-167). |
| c3 | Season Pass seasons open on the 1st at 00:00 UTC | CONFIRMED | As a1. |
| c4 | Daily gift = "Login Calendar" row on the push sheet | CONFIRMED (compatible) | `GS` f_a325dd4af80afc5994d5dc "Push Notifications Zombie Match", tab `PNs Beta` row 12: Event / Push Notification / "Daily/Monthly Rollover" / "Login Calendar update" / Not Ready / WIP. Base uses both "Daily Login" (ZOM-299, ZOM-412, ZOM-415) and "daily gift" (ZOM-432, ZOM-556) for the feature. |
| c5 | Boss Arena off this calendar until the pivot call | UNCONTRADICTED | A scoping instruction. Base: Boss Arena is in store builds since Sep 17 (`GM/frederick@harmonygames.co_1842285743246816270.json`, Leonard: "Boss Arena mode: do as much damage as possible to the boss"), Trello #26 complete Sep 18, and tied to pivot experiments in the same thread ("Boss mode ... game mode still WIP"). |
| c6 | "the pivot call" | UNCONTRADICTED | No base meeting by that name. Grounded: `SL/D04UP2L3E3S/2025-09.json[635]` "if the game metrics still suck by mid oct, let's ... pivot"; `SL/C08H78VJG80/2025-09.json[24]` Frederick 2025-09-29 "we are considering a pretty substantial pivot in core game play"; Board Meeting 2025-10-14 in `GC`. |
| c7 | "Aug-Sep live-ops cohort", change request outside it does not hold | UNCONTRADICTED | Only CHANGES_REQUESTED review on match3d in all of base: `harmonygames-Games/match3d#303#rev_6`, 2025-07-16, PR "Samuel/zom 349", merged. Zero in Aug-Sep, and the SQL adds only COMMENTED reviews. So the "outside" clause has exactly one base instance and the "inside does hold" clause has none. |
| c8 | Beta pushes English-only (UK and US buys) | CONFIRMED | `SL/C7442B7CD94B/2025-09.json[99]` Leonard "we didn't do localization at all and not ready technically for global launch"; `SL/C5A22E7CCFDB/2025-09.json[3]` "289 installs from UK and that's where we buy users from Unity"; `SF` AD_SPEND_DAILY Sep 2025 unity_ads installs GB 749, US 70, DK 20, SE 16, NO 12, NL 8, FI 1; `CF/page_product_okrs` "US-only from April 2025 and still a short country list in September 2025". |
| c9 | Translated tab is the old Domino set | CONFIRMED | Tab `PN BETA Translated` rows 3-8, 11: "Full Charge on Tiledozer & Luckydrop Coins!", "mini-games in Domino Adventures", "Your Domino Quest Awaits!", "River Rush Is On!" in 21 languages. |
| c10 | Game named only "Zombie Match 3D", events by ZM3D names | CONFIRMED | `CF/page_zm3d_gdd`: renamed from "Puzzles vs Zombies" on 24 July 2025; `PNs Beta` rows 4 and 6 still say "Puzzles vs Zombies"; row 7 says "Win & Collect", and `CF/page_liveops_calendar` gives the ZM3D name as "Collect & Win ... Same feature as Win & Collect on Domino Delights, under a different name". |
| c11 | One-off takes a recurring slot only with Product approval; overlap allowed | CONFIRMED | `CF/page_liveops_calendar`: one-offs "should never displace a recurring slot without documented Product approval"; "Overlapping events are normal". |
| c12 | Config locks exist | CONFIRMED | `CF/page_season_pass_spec`: "locked 24h before each season opens". `CF/page_liveops_calendar` calls it "a process control ... not a mechanism", which does not negate it. |
| c13 | Row must be "Ready and LIVE" | CONFIRMED | `PNs Beta` has both columns: "Status" (Ready / Not Ready) and "Status (NA, WIP, LIVE)". |
| c14 | Created 2025-09-24 10:15Z, modified 10:40Z | FORMAT (plausibility) | 03:15-03:40 Pacific. Frederick's Slack Jun-Sep: 0 messages in 07:00-11:59 UTC. Same day he edited "Publishing Partners" at 17:15:31Z. |
| c15 | Doc shape | CONFIRMED / FORMAT | Style-run offsets all land exactly on the title and eight headings. Drive row has `size` and `content_path` NULL; base has both non-null on 595/595 Google Docs. |

### (d) Slides "ZM3D beta UA plan"

| # | Claim | Verdict | Evidence locator |
|---|---|---|---|
| d1 | Four week ranges W1-W4 | UNCONTRADICTED | All Mondays/Sundays correct. No base buy schedule. |
| d2 | "starting once the stores approve the Sep 30 builds" | CONFIRMED (builds), mild TIMING note | Builds exist: `SL/C05433XK267/2025-09.json[1120]` "Match 3D iOS Submission - #50" 2025-09-30T18:43:32Z, `[1122]` "Match3D Android Submission - #135" 18:45:34Z. On the deck's date the roadmap list was already `BETA: Sep 30` (`TR` updateList 2025-09-12T16:42:21Z) and `SL/D04UP2L3E3S/2025-09.json[680]` 2025-09-23T00:39:08Z says "Push this out by next Wednesday as our beta launch". Note: other submission builds shipped in between (iOS #46-49, Android #129-133 on Sep 26; Android published Sep 27, iOS 0.3.49 released Sep 29), so "the Sep 30 builds" in a file last modified Sep 23 is only unambiguous in hindsight. |
| d3 | "UK and US first, English-only creative" | CONFIRMED | As c8. |
| d4 | Small retention campaigns already running, separate budget | CONFIRMED (running), UNCONTRADICTED (separate budget) | `SL/C0880U9751A/2025-09.json[472]` Frederick 2025-09-30T16:04:27Z "We are only running the retention campaigns"; `SL/C07C2866011/2025-09.json[467]` "I turned on UK Retention IOS and added $1K"; `[819]` 2025-09-19 "set the budget for Unity campaign to a $1 instead of turning them off completely"; `[823]` "Fb spend is like $20/day so I'm just gonna let it run"; `[1160]`, `[1166]` Sep 29 "turning on iOS Unity retention campaigns", "$150/campaign/day". |
| d5 | Buy at small scale, hold until the pivot call | UNCONTRADICTED | `SL/C07C2866011/2025-09.json[1191]` Frederick 2025-09-30T20:27:30Z offers to "juice it more"; Robert: "dont just throw too much money away". |
| d6 | A scaled beta buy from Oct 6 at all | **TENSION** | Against: `GM/frederick@harmonygames.co_1823332883409810377.json` Frederick 2025-09-09 "We aren't spending on UA at the moment. But we're shooting for a beta release of our second title as soon as we can get UA funding ironed out"; `SL/D04UP2L3E3S/2025-09.json[775]` Leonard 2025-09-25T05:15:22Z "We can barely get the beta out by mid october"; Leonard's Sep 17 investor mail "beta goals over the next 3-4 weeks"; `TR` list currently named `BETA: Oct 10`. For: Confluence "end-of-September beta submission", the Sep 30 submission builds, Sep 29 "do you want us to buy users". No base decision not to buy. |
| d7 | Internal consistency | note | Slide 1 "Scaled beta-cohort buy", slide 2 "scaled up week by week if the cohorts hold", slide 3 "hold the spend there until the pivot call". Not a base issue. |
| d8 | Deck shape | CONFIRMED | `slide_`/`el_`+12 hex, BLANK, TEXT_BOX, 9144000x5143500, size/content_path NULL all match base. No companion `.presentation.pdf`: base has one for 129 of 132 decks. Created 16:05Z = 09:05 Pacific. |

### (e) Julia's Drive folder and sheet

| # | Claim | Verdict | Evidence locator |
|---|---|---|---|
| e1 | Folder "ZM Live Ops" under Julia's root | UNCONTRADICTED | Parent `d_8140f09bf9f1b94cb8ee2d` is Julia's root; no id collision. Julia's base Drive has one folder ("Zombie Art") and no live-ops or calendar file. |
| e2 | Sheet "ZM3D Beta Live-Ops Calendar.xlsx", tabs Calendar / Pushes | UNCONTRADICTED / FORMAT | `.xlsx` suffix and extension-less sheet title match base. `size` and `content_path` NULL; base has both on 356/356 sheets. |
| e3 | "my live-ops calendar sheet" is unambiguous | UNCONTRADICTED (low ambiguity) | Only Julia-owned calendar file is the injected one. Similar base names she can open: `GD` f_b04156e116437611a5014a "LiveOps Event Calendar.xlsx" (shared-drive owner, domain-visible, 2025-02-05, Domino Delights weekday grid, under Design/Domino Delights/GDDs); "Live Ops Planning.xlsx" and "Live Ops.xlsx" (Leonard). Brian's "Event Calender.xlsx" is private. Confluence page "Live-Ops Event Calendar & Planning". |

### (f) Trello comment

| # | Claim | Verdict | Evidence locator |
|---|---|---|---|
| f1 | Comment on card 6851a724601a61857a1b202f | CONTRADICTED (known) | Card #4 completed 2025-06-30T16:56:34Z (`TR` action 6862c1c22b05395fb3e4c93c). Re-verified: 0 base cards have a comment after completion. |
| f2 | "Mon Oct 13 rollover" | CONFIRMED | Weekly quest reset is Monday 00:00 UTC: `GH/root/match3d-quests/lib/quests-stack.ts` L426-434 (`weekDay: 'MON'`, hour 0); `CF/page_quest_postmortem` "weekly reset on Monday at 00:00 UTC". Oct 13 is a Monday. |
| f3 | Brian as author | UNCONTRADICTED (thin) | See section 5. |

---

## 3. Contradictions and conflicts, ranked, with the smallest fix

**1. Trello comment sits on a completed card.** Move it to card #61 and fix the payload (section 5). Drop the `UPDATE` on card #4 entirely so its badges (`comments: 1`) and `dateLastActivity` (2025-06-30T16:56:34Z) stay as base.

**2. Gmail thread ids are out of convention and one postdates the clock.**
Base side: thread id >> 20 = arrival time in ms; max base id 1844759654420061899 (2025-10-01T06:25:02Z).
Injected side: 1844835127305531392 decodes to 2025-10-02T02:24:38Z; 1844470925517303296 to 2025-09-28T01:55:49Z.
Fix: one id per mailbox, derived from the send time. These six are free in base:

| Mailbox | Sep 22 mail | Sep 26 mail |
|---|---|---|
| brian.foster | 1843954786396120001 | 1844311386017777833 |
| julia.lawson | 1843954788178927143 | 1844311388009348974 |
| frederick.stone | 1843954789017368532 | 1844311388953497682 |

Change in step: `gmail_threads.id`, `gmail_messages.thread_id`, the `X-GM-THRID` header and the `mbox_from` prefix.

**3. Beta buy from Oct 6 vs base beta-date signals (tension).**
Base side: `TR` list 6851a674975da1fe76e70d93 is named `BETA: Oct 10`; `SL/D04UP2L3E3S/2025-09.json[775]` "We can barely get the beta out by mid october"; Frederick's own Sep 9 mail ties the beta release to UA funding.
Injected side: deck slide 1, brief span, Frederick's DM "the beta buy we start Mon Oct 6".
Smallest hardening, if wanted: one clause on deck slide 2, e.g. "The buy runs on the store builds; the roadmap beta milestone lands inside W1." No change is strictly required, since no base record says the buy starts later or is cancelled.

**4. Oct 8 release vs base prod updates on Sep 29 and Sep 30 (inference risk).**
Base side: `SL/D079SNE2TL4/2025-09.json[263]` 2025-09-30T18:16:33Z "I updated the prod environment with the latest teams/social changes".
Injected side: event description "The server windows that are still on the DEV stack go live with this release".
Smallest hardening: say which stack, e.g. "Prod deploy of the game API for the beta." That separates it from the teams/social (Nakama) update.

**5. Read/unread labels in Julia's mailbox.** Use the mailbox's own idiom: Sep 22 copy `["INBOX","CATEGORY_PERSONAL","Label_b19fb8d1b3"]` with header "Inbox,Opened,Category Personal"; Sep 26 copy `["INBOX","CATEGORY_PERSONAL"]` with "Inbox,Category Personal". Only matters if the read/unread difference is meant to be visible.

**6. Off-hours timestamps.** Brief: move to 2025-09-24 17:15 / 17:40 UTC. GCal: created 2025-09-24T16:05:00Z, updated 2025-09-26T17:20:00Z.

**7. "the Sep 30 builds" in a deck last modified Sep 23.** Either leave it (roadmap said `BETA: Sep 30` at the time) or reword to "the end-of-September beta builds", which mirrors Confluence.

**8. Cosmetic Gmail and Drive fields.** Drop `Delivered-To` and `Reply-To` from Brian's Sent copies; give the Doc and Sheet Drive rows a `size` and a `content_path` (`<owner>/<name>`), as every base Doc and Sheet has.

---

## 4. Other things worth knowing (not contradictions)

- **Brief's change-request rule has no in-cohort instance.** If any expected answer depends on a beat being held by a change-request blocker inside the Aug-Sep cohort, base and the SQL contain none.
- **Brian is interviewing elsewhere.** `SL/D076RBM29JS/2025-09.json[129]` 2025-09-29T10:32:50Z, Brian to Julia (Turkish): he took a case assignment from another company on Friday, nothing decided. Context for his Oct 31 commitment, nothing more.
- **Playable ad project paused.** `SL/C08H78VJG80/2025-09.json[24]` Frederick paused PlayableX "for a month or so"; `[25]` new start date November 3rd. Consistent with "English-only creative", no conflict.
- **Trello "Win and Collect" card #10 was marked complete 2025-09-30T16:40:13Z**, 36 minutes after the injected Arthur comment that says the server windows are DEV-only. Roadmap completion is not prod state; Confluence says "not yet live".
- **Plague Race cadence differs inside base** (CDK daily; Snowflake shows 5-day runs). The brief asks for no Plague Race window dates, which sidesteps it.

---

## 5. Trello recommendation (f)

### Open cards about quests, quest content or weekly rollover for ZM3D

Scanned all 803 cards on all 5 boards for quest / rollover / content set / achievement / milestone in name or description. Not completed, not archived, ZM3D:

| Board | List | Card | id | closed | dueComplete | last activity | members | comments |
|---|---|---|---|---|---|---|---|---|
| ZM ROADMAP | BETA: Oct 10 | #61 "Add more quests and balance quest rewards - (Leonard/Douglas)" | 68c452a03006277f55d9dc96 | false | false | 2025-09-12T17:31:20Z | none | 0 |
| ZM ROADMAP | BETA: Oct 10 | #58 "Minor Bugs to Fix - [PERSON_NAME_0050]" (description only: "Consecutive login quest not working") | 68c451141c69fb8af1b4568e | false | false | 2025-09-30T16:40:33Z | none | 0 |

Everything else that matched is the completed card #4 (the current target) or a Domino Delights-era card on the other two boards ("DD Product Roadmap", 2024 lists; the "Harmony Games" board's Done list, last touched 2025-04-07). No ZM ROADMAP card has any member assigned.

**Use card #61.** It is the only open card about quest content.

### Exact values

- Board `6851a6569f3bf818760632ab` "ZM ROADMAP", shortLink `HSqnngwQ`
- Card `68c452a03006277f55d9dc96`, idShort 61, shortLink `viBYIjSG` (from its url), name `Add more quests and balance quest rewards - (Leonard/Douglas)`
- List `6851a674975da1fe76e70d93`
- Current badges: `comments: 0`, `description: false`, `checkItems: 0`, `checkItemsChecked: 0`, `dueComplete: false`, `attachments: 0`. After the insert: `comments: 1`, `dateLastActivity: 2025-09-29T17:55:44Z`. Board `dateLastActivity` (2025-09-30T17:09:07Z) needs no change.
- Action id `68dac8204f1e9a3b7c2d5e61` is free and its first 8 hex digits already encode 2025-09-29T17:55:44Z.

### Three things to get right

1. **List name in the action payload must be `BETA: Sep 30`, not `BETA: Oct 10`.** The lists table says `BETA: Oct 10`, but all 71 base actions on that list from 2025-09-12T16:42:21Z to 2025-09-30T17:09:07Z carry `"name": "BETA: Sep 30"`, and no rename action to Oct 10 exists. A Sep 29 action saying Oct 10 would disagree with base actions dated the next day.
2. **Brian has no Trello footprint.** His member record exists (`d1cd0fef645a6c978ae1f068`, username `brian.foster`, fullName "Brian Foster", initials BF, memberType normal, confirmed true). But he has 0 actions on any board, is on no card, is not in the organization's `memberIds` (only PERSON_6095 and PERSON_6094), and no `addMemberToBoard` action names him. The export has no board-membership table, so membership can be neither confirmed nor refuted; the three recorded additions to ZM ROADMAP are PERSON_6095, PERSON_6096 and PERSON_6097. Related base signals: `SL/D077ALC9VK3/2025-07.json[27]` Brian asks someone else to change the roadmap; `SL/D07GMT8NVM2/2025-09.json[405]` Oliver asks for access to the Trello page. All 12 comments on this board are by PERSON_6095 (Robert's real account, by timing against his Slack), the latest on 2025-07-02; no board has a comment after that date.
3. **The card names Leonard and Douglas, not Brian.** Authors in order of base fit: Leonard Hayes (`PERSON_6094_TRELLO_USER_ID`, username `leonard.hayes`, 4,019 actions, created this card); Douglas (`1c0688ee1d9093f5b978c1db`, named on the card, no Trello activity); Brian (not named, no activity, but he owns the workbook holding the `Daily Quests` and `Weekly Quests` tabs). Keeping Brian is defensible; it is the weakest of the three.

### Base facts the note must agree with

- Weekly quest reset: Monday 00:00 UTC (`quests-stack.ts` L426-434; `CF/page_quest_postmortem`). Daily: 00:00 UTC.
- `SL/C08R27X0EAH/2025-07.json[1028]` Leonard: "forcing quest refreshes at utc midnight for both daily and weekly quests on Sundays". Same instant seen from Pacific time; worth knowing a reader may quote it as "Sunday".
- Push sheet `PNs Beta` row 1: Quests / Push Notification / Rollover / "Revisit once new quests roll out." / Not Ready / LIVE.
- Quest changes need QA and a canary: `CF/page_release_checklist` "nothing pushed straight to the live quest server"; `CF/page_quest_postmortem` "No auto-deploy to live quests without QA sign-off".
- Card #61 was created 2025-09-12 in the beta list and is not complete. Oct 13 falls three days after the list's current date; harmless on an open card.
- Linear: ZOM-534 "Quest points not resetting until app restart in production" In Progress (Douglas); ZOM-557 "Consecutive log in quest doesn't work" Done 2025-09-30; ZOM-63 quest spec by Julia, Done 2025-06-23.

---

## 6. Searches run

- **Gmail** (81,404 thread files): full pass for every message whose From contains "brian" (242); label ids, X-Gmail-Labels and header-name census for Brian's, Julia's and Frederick's mailboxes; thread-id vs internal-date check on all mailbox-prefixed threads; cross-mailbox thread-id duplicate check; keyword pass since 2025-08-15 over Julia, Frederick, Brian, Douglas, Owen, Oliver and Robert (season pass, handoff, backend release, prod deploy, UA plan, beta buy, pivot, live-ops calendar, quest set, rollover, login calendar, collect/win); list of all human mails to Julia and Frederick since Sep 15; full read of Frederick's "Checking in" thread and Leonard's Sep 17 investor mail.
- **Slack** (all channels and DMs): all of Brian's messages since Aug 2025 (3,912, keyword-filtered); full reads of #executives from Sep 17, the Leonard-Robert DM from Sep 21, #zm-collect-win, the Douglas-Vincent and Douglas-Oliver DMs for September, #zombie-ops, #zombie-match3d from Sep 28, #builds from Sep 26, all Frederick messages from Sep 19, and the September DMs among Julia, Brian, Frederick and Douglas; keyword sweeps for prod/deploy/release terms (since Aug), "beta" (since Sep), market and country terms (since Aug), the injected phrases (since Jan 2025), the injected dates (since Aug), quest content terms (since Jul), Trello/roadmap (since Jun), submission and store approval (Sep 25 on); activity-hour histograms for five people.
- **Confluence**: full read of the live-ops calendar page, Season Pass spec, ZM3D GDD, Product OKRs and the head of the release checklist; keyword grep of the other 25 pages and all 12 comments.
- **GitHub**: CDK stack, `bin/zombies-game-cdk.ts`, `config/*.exs`, `win_and_collect.ex`, match3d-quests stack and timer lambda; match3d-backend PRs and commits; review-state counts for every repo.
- **Trello**: all boards, lists, cards, members, actions (5,252); list rename history; histories of cards #4, #10, #27, #61; comment-after-completion check.
- **GCal**: all 10,395 events for organizers, release-like summaries, future events, recurring Wednesday events, id and uid collisions.
- **Drive / Docs / Sheets / Slides**: id collisions, parent folders, name and field conventions, Julia's whole Drive root, name search across 53,631 files; all four tabs of the push sheet; base "LiveOps Event Calendar" and Brian's economy workbook; Frederick's docs and decks.
- **Linear**: ZOM issues by title and description for deploy/prod, season pass, quest, calendar/push/login/boss arena/collect. Base Linear has 0 comments.
- **Snowflake**: AD_SPEND_DAILY, AD_SPEND, UA_SPEND_UNIFIED_V2, PUSH_NOTIFICATION_STATS, LIVE_EVENT_PERFORMANCE.

Not done: I did not read every Gmail body or every Slack DM in full; coverage outside the full reads above is by keyword. The Turkish-language DMs were only keyword-scanned and spot-read. `hg.py search` was not used; all scans were direct reads of the exports.
