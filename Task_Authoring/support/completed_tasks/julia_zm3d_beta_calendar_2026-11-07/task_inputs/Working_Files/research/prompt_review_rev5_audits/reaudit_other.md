# Re-audit of the non-Linear injected records

- **Input:** `review_rev5/inputs/01_Universe_Inject.sql`, 59,504 bytes, 103 statements, sha256 `2e0dc42c656556d0e92f06cc6a3c9aa13d0da9a9016f603e4c4c7db282b81cac`. Not executed.
- **Clock:** 2025-10-01 07:00 UTC. Universe: `Universe_SynthCut`.
- **Scope:** every injected record that is not a Linear comment (GitHub, #zombie-prs mirrors, Slack, Gmail, GCal, Drive, Docs, Slides, Sheets, Trello).
- **Path shorthand:** `S/` = `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data`, `G/` = `…/SynthCut_HarmonyGames_GitHub/Services_Data/github`, `M/` = `…/SynthCut_HarmonyGames_Gmail/Services_Data/gmail`. `/N` after a file is the array index.

## 1. Result

No statement in this slice is contradicted by base content, including base data the persona cannot read. Most claims are confirmed by a base record; the rest are uncontradicted. One sentence in the UA deck is in soft conflict with base timing.

What does break is format and placement. Seven items are ones a strict reviewer could score; the rest are cosmetic.

| # | Problem | Records | Scoreable? |
|---|---|---|---|
| 1 | Slack `ts` ends in a digit no base message uses | all 9 Slack rows | Yes, format |
| 2 | Calendar sheet `content_path` omits its folder | `f_e4a17c90…` | Yes, format |
| 3 | PR "opened" cards not updated (Comments count, Reviewers) | 3 parent UPDATEs | Yes, coherence |
| 4 | Notes written on merged PRs, later than any base precedent | #470, #471 (and #473) | Yes, placement |
| 5 | Gmail Message-ID is the wrong length and prefix | 6 Gmail messages | Yes, format |
| 6 | `Reply-To` header on received copies only, with empty `reply_to_json` | 4 Gmail messages | Yes, internal inconsistency |
| 7 | Deck says retention campaigns were "already running" on Sep 23 | slide 3 | Possibly, timing |
| 8–20 | Cosmetic items | various | No |

## 2. Problems, ranked, with the smallest fix

### 2.1 Scoreable

**1. Slack `ts` last digit (all 9 injected Slack rows).**
Base: 610,445 of 610,468 messages have a `ts` ending in `9`; the other 23 end in `0`. None ends in 3, 4, 5, 7 or 8 (2025-09 alone: 21,652 of 21,657 end in `9`). The injected values end in 7, 7, 3, 4, 7, 7, 7, 5, 8.
Fix: set the last digit to `9`, recompute the id, and update `created_at`, `thread_parent_id`, `thread_ts_legacy` and the parents' `latest_reply`. None of the replacements collides with a base `ts` or id.

| Record | Channel | New `ts` | New id |
|---|---|---|---|
| Frederick ask | D05SD5QLG94 | `1759263600.418209` | `02c5ebdd0b2dde6a043d168cd6f7b1b0` |
| Frederick reply | D05SD5QLG94 | `1759263878.305129` | `890dc27f56e8501bd7590ffdfc231057` |
| Robert approval | C08R8CHB0QL | `1758213600.552919` | `e97c4083377036b59598158e27b54c26` |
| Robert retraction | D05GU6L0XFH | `1759270200.638119` | `1b8d9ecd2be488ef0c08763969bc7947` |
| Vincent re-test | C0880U9751A | `1759265412.481909` | `b5f2955c2e154efc6835946ecfe1758e` |
| #470 mirror | C093LEZGF6J | `1759257682.404979` | `1ec9e5cfae7b876289f425b034b7f72e` |
| #468 mirror | C093LEZGF6J | `1759160203.669699` | `6913312c7db76e465621395144ddb3fa` |
| #473 mirror | C093LEZGF6J | `1759248995.072069` | `4e271a4498d3c5a191a42bbf0c26d241` |
| #471 mirror | C093LEZGF6J | `1759266448.880539` | `57edcea2b72af43ed69f5eab871dac58` |

Invisible to the solver, but it is an absolute base convention (0 of 610,468).

**2. Calendar sheet `content_path` omits the folder.**
Base: in 30,242 of 30,242 Drive files with a `content_path`, the path is `<root name>/<every ancestor folder>/<name>` (segment count = ancestors + 1); 123 of 123 spreadsheets inside a sub-folder include the folder. The sheet's parent is `ZM Live Ops` (`d_5f2c8e1b…`), but its path is `julia.lawson@harmonygames.co/ZM3D Beta Live-Ops Calendar.xlsx`.
Fix: `julia.lawson@harmonygames.co/ZM Live Ops/ZM3D Beta Live-Ops Calendar.xlsx`.
Related risk, not a base contradiction: the brief's and the sheet's `content_path` point at bytes that do not exist under `S/gdrive/root`. The lint accepts this because the Docs and Sheets rows exist, but a Drive byte download would fail. Worth one dry-run read.

**3. PR "opened" cards in #zombie-prs are left stale.**
- *Comments field.* Base: in 218 of 218 parents that carry the field, `Comments` equals the PR's conversation-comment count, including human comments added a day after opening (#262 and #332, both 3). After the SQL, the #473 card (`S/slack/messages/C093LEZGF6J/2025-09.json /605`) still says `1` with 2 comments, and the #471 card (`/583`) still says `2` with 3.
- *Reviewers field.* Base: a comment-only review adds the reviewer to the card (Arthur 5 of 5 PRs: #265, #281, #317, #390, #395; all humans 8 of 9). The #468 card (`/530`) lists only CodeRabbit after Arthur's `rev_3`. The #470 card already lists him.
Fix: add `attachments_json` to the three parent UPDATEs: Comments `"2"` on `d05a2f8a…`, `"3"` on `da3fe08c…`, and `, <@EMPLOYEE_0025_SLACK_ID>` appended to Reviewers on `4b7c4127…`.

**4. Notes on merged PRs, later than base precedent.**

| Note | PR merged | Note time | After merge | Base pattern for that record type |
|---|---|---|---|---|
| #468 `rc_38` (inline) | 09-29 16:13:50Z | 09-29 15:36:41Z | 37 min before | pre-merge, normal |
| #473 `c_2` (conversation) | 09-30 15:41:20Z | 16:16:33Z | 35 min | 2 of 92 human PR comments are post-merge: 9 min and 40 min |
| #470 `rc_10` (inline) | 09-30 15:51:15Z | 18:41:19Z | 2 h 50 min | 3 of 547 human inline comments are post-merge: 8 s, 10 s, 61 s |
| #471 `c_3` (conversation) | 09-30 15:52:24Z | 21:07:26Z | 5 h 15 min | same 2 of 92, max 40 min |

In match3d specifically, 0 of 23 human inline comments and 0 of 4 human conversation comments are post-merge. The only long precedent is a bodiless approval: `GameOfDominoes#1578#rev_2` by Arthur, 6 h 17 min after merge.
All three post-merge notes sit on closed, merged records. #473 is inside the base range; #470 and #471 are outside it. Both are forced late by their own text: "the prod update from today" follows Douglas's 18:16:33Z message, and "iOS 50 and Android 135" follows the 20:13:09Z build result.
Fixes, cheapest first:
- #470: move to about 15:50Z on Sep 30 (a comment review just before Arthur's base approval at 15:51:06Z) and drop the clause "the prod update from today carried the teams/social changes only". Carry that clause elsewhere if it is needed.
- #471: either accept it with the #1578 precedent, or move the build confirmation to a Slack reply and keep a short PR comment within 40 minutes of the merge.
- #473: leave.

**5. Gmail Message-ID shape.**
Base: all 4,337 internal Gmail-web messages have a 51-character local part, and each sender has a fixed 7-character prefix plus one varying character. Brian Foster's two human mails start `CAPT--p4` (`M/threads/brian@harmonygames.co_1822687189419018831.json`, `…_1822693237981026750.json`). The injected ids are 32 characters and start `CAH4q9Z`.
Fix: use 51-character ids with his prefix, for example `<CAPT--p4sBC8XnaA7qBDMtZkWqJPiXP0MT3deOQGPusOZhHF+vo@mail.gmail.com>` and `<CAPT--p4a5fY9wd6vr+8JtjFXfffkxQOCEUYsuqSPy9HbQJu3Fs@mail.gmail.com>`, in the message `id` and the `Message-ID` header of all three copies.

**6. `Reply-To` header against `reply_to_json`.**
The four received copies carry `Reply-To: Brian Foster <…>`; the two sent copies do not, and `reply_to_json` is `[]` everywhere. Base: 0 of 199 internal human mails in the three mailboxes have the header; across all Gmail it appears in 7 of 4,337, and in all 7 the `reply_to` field is set too.
Fix: delete the `Reply-To` header from the four received copies.

**7. Deck, slide 3: "The small retention campaigns already running" (deck dated Sep 23).**
Base: on 09-19 20:19:57Z Leonard set the Unity campaign budget to $1 "instead of turning them off completely" (`S/slack/messages/C07C2866011/2025-09.json /819`). Android was funded again on 09-27 00:39Z and iOS on 09-29 22:48Z, where he writes it "was set to $1 to effectively pause" (`/1166`). So on Sep 23 the retention campaigns were effectively paused.
Fix: reword to "The Unity retention campaigns are a separate budget and are not part of these buys."

### 2.2 Cosmetic

8. **Em dash in human GitHub comments** (`#473#c_2`, `#471#c_3`, and their mirrors). Base: 0 of 92 human PR comments and 0 of 547 human inline comments contain `—`; Samuel uses it in 0 of 1,510 Slack messages. Fix: replace ` — ` with a full stop or comma.
9. **Other Gmail header deviations.**
   - No `Content-Type` header (base: 118 of 118 sent, 199 of 199 received). Add `multipart/alternative; boundary="000000000000<12 hex>"` as the last header.
   - `To`/`Cc` display names `Julia Lawson` and `Frederick Stone` (base: `julia` 29 or bare address 19; `frederick stone` 350 or bare 110; the capitalised forms 0).
   - Date offset `+0000` (Brian Foster's two base mails use `+0300`; the alias as a whole uses `+0000` in 0 of 21).
   - `mbox_from` has no trailing `\r` (base 6,085 of 6,085) and repeats the Date second on the received copies. Base: its second equals the thread-id arrival second in 4,912 of 4,931 single-message threads, so Julia's copies should read `:02` and Frederick's `:02` and `:03`.
   - Received copies lack the delivery chain (`Received`, `ARC-*`, `DKIM-Signature`…; base 191 of 192). Not practical to fake.
10. **#468 review has no `reviewed` timeline event, #470's has one.** In match3d, standalone review comments by a non-author have events (3 of 3 PRs: #303, #317, #332) and reply-type ones do not (7 PRs, including #470's own four). Adding `#468#ev_6` would number a pre-merge review after `closed`, so leaving it out is the lesser evil.
11. **No GitHub notification mail for `#473#c_2` in Oliver's mailbox.** Base: 15 of 15 events by others on his Aug 15–Sep 30 match3d PRs have one, including #473's CodeRabbit comment at 15:41:35Z. Not persona-visible. No mail is expected for #471 (own comment) or #468/#470 (Owen's mailbox has none in base).
12. **Folder `ZM Live Ops` modified 06:30:00, its only child created 06:35:00.** Base: 18,640 of 19,003 folders have `modified_time` at or after the latest child's `created_time`. Fix: folder `modified_time` ≥ 06:35.
13. **Deck row has a NULL description and no PDF sibling.** Base: 132 of 132 presentation rows carry "Reconstructed Google Slides sibling from Drive PDF f_…". Faking one would be worse; leave.
14. **Whole-minute timestamps.** Slack human messages: 3 of 5 at `:00` (base 1.67%). Gmail: 2 of 2 (base 1.5%). GCal created and updated: both (base 1.6% and 0.7%). Drive: 7 of 7 (base 1.6–2.9%). Fix: give them seconds.
15. **Frederick threads the follow-up under his own DM.** Base 2025: 1 of 781 of his DM messages is a reply to his own parent. Fix: make it a second top-level message.
16. **Vincent's re-test is top-level in #zombie-match3d.** Base September: 4 top-level posts there (all Sep 9) against 21 in #zombie-bugs.
17. **Arthur's #468 review at 09-29 15:36:41Z.** He answered a DM at 15:12:11Z, then nothing until 17:48:54Z; at 17:49:40Z "I'll be back to the office tonight" and at 18:00:09Z "Will review when I get home tonight" (about PR #469; `S/slack/messages/D06477JGUKT/2025-09.json /194`). Soft; a text note from a phone is plausible.
18. **Wording with no base precedent.** "DEV stack" (0 Slack mentions in 2025; base says "dev server", "dev env", "on dev"), "premium strip" (0; the assets are "golden stripe"), "pivot call". Also on Sep 30 the next season is October, so "move to the November range rather than the current one" skips a month and reads ambiguously.
19. **First names in free text.** Base text shows Julia, Frederick, Claire and Oliver only as redaction tokens (`[PERSON_NAME_0040]`, `[PERSON_NAME_0036]`, `[PERSON_NAME_0022]`); since June 2025 the plain names appear 4, 0, 1 and 0 times. Do not change this; tokens would read worse.
20. **Minor.**
    - Robert says "one of the beta weeks" on Sep 18, five days before the deck defines the buy weeks.
    - The Trello payload spells the card "(Leonard/Douglas)" as the cards table does, while the card's last base action spells "(Leonard/douglas)"; that is a base inconsistency.
    - Discussion id `r2388843617` implies about 80k ids/h on a Monday afternoon against about 183k/h measured on Tuesday; it is still monotonic.
    - GCal has no Meet link (base: 267 of 10,395 lack one).

## 3. Verdict table

### (a) GitHub

| Record | Claim or field | Verdict | Evidence |
|---|---|---|---|
| `#470#rc_10` | C&W server windows still on DEV only | UNCONTRADICTED, supported | Douglas 09-26 20:48:47Z "Ese merge con main significa que debo deployar a prod?"; Owen "no va para release ahora… creeria que no": `S/slack/messages/D05SG9H1CFM/2025-09.json /405–/408`. Confluence `page_liveops_calendar` (updated 09-29): "not yet live". Snowflake `LIVE_EVENT_PERFORMANCE` has no ZM3D Collect & Win run |
| `#470#rc_10` | "prod update from today carried the teams/social changes" | CONFIRMED ("only" is inference) | Douglas 09-30 18:16:33Z "I updated the prod environment with the latest teams/social changes": `S/slack/messages/D079SNE2TL4/2025-09.json /263` |
| `#470#rc_10` | Plague Race, leagues, Endless, Season Pass schedules on prod | CONFIRMED | `G/root/harmonygames-Games/match3d-backend/zombies-game-cdk/lib/zombies-game-cdk-stack.ts` lines 136–189; Confluence calendar rows "Live"; Season Pass spec "Reached production in the week of September 22-29"; Snowflake `EVT-0527` |
| `#470#rc_10` | path, shape, numbering | CONFIRMED | path is in the PR (`rc_7`–`rc_9`); empty `diff_hunk` with null line is the base file-comment shape (53 of 1,387, Arthur 26 of 154); `rev_10`/`rc_10` follow `rev_9`/`rc_9` |
| `#470#rc_10` | author active at 18:41:19Z | CONFIRMED | Arthur push 18:37:50Z, Slack "pushed" 18:38:24Z, starts Submission #50 at 18:43:32Z: `S/slack/messages/C05433XK267/2025-09.json /1117–/1122` |
| `#470#rc_10` | 2 h 50 min after merge | TIMING, FORMAT | problem 4 |
| `#470#ev_9` | `reviewed`, actor `''`, null date, head commit | CONFIRMED | same shape as 2,116 of 2,116 base reviewed events; commit `4935e948…` is the head (`G/data.json /pull_requests/2375`) |
| `#468#rc_38` | vials are first-pass models, final ones missing, Claire has them | UNCONTRADICTED, supported | Claire commit `235e49e2` 08-08 "Collect&Win Items Potion bottles Added" (PR #370); Martin 08-11 "wants to change the icon on the bottle... I'll send you when it's done" (`S/slack/messages/D05PV7UMRUL/2025-08.json /24`, last message); no later Claire commit names the bottle |
| `#468#rc_38` | anchored on `GameLoader.cs` | CONFIRMED | file spawns `collectAndWinVial` (lines 179–202); base `rc_1` uses the same path |
| `#468#rev_3` | no timeline event | FORMAT, cosmetic | problem 10 |
| `#468` | no `updated_at` bump | CONFIRMED | base 16:13:50Z is later than the review |
| `#473#c_2` | premium strip to November range, Oliver | UNCONTRADICTED, ambiguous | Oliver authored #473; Season Pass resets monthly on the 1st; "premium strip" has no base term |
| `#473#c_2`, `ev_5`, bump | ids, shape, 35 min after merge | CONFIRMED | `c_2` follows `c_1`; event shape as base; inside the 40 min base maximum |
| `#471#c_3` | frame went out with this PR | UNCONTRADICTED, partly supported | commit `f0bb8b48` "update header image"; `rc_2` path `Daily Gift/img - DailyGift.png.meta`. Samuel's own change list (`S/slack/messages/D06UFE81RF0/2025-09.json /31`) lists only font and alignment for Daily Gift |
| `#471#c_3` | in iOS 50 and Android 135 from today | CONFIRMED | `S/slack/messages/C05433XK267/2025-09.json /1123` (19:15:49Z) and `/1124` (20:13:09Z, lists "Fixing UI Elements on Daily Gift") |
| `#471#c_3` | 5 h 15 min after merge; em dash | TIMING, FORMAT | problems 4 and 8 |
| PR `updated_at` ×3 | forward, equal to the note | CONFIRMED | base: `updated_at` ≥ latest note in 1,957 of 1,957 PRs |

### (b) #zombie-prs mirrors

| Record | Claim or field | Verdict | Evidence |
|---|---|---|---|
| 4 mirrors | text equals the GitHub body with `&` → `&amp;` | CONFIRMED | checked programmatically; base keeps `—` unescaped (224 mirrors) |
| 4 mirrors | author handle, anchor type, title, fallback, key set, `subtype` null | CONFIRMED | 949 of 956 base comment mirrors have the same 10 keys |
| 4 mirrors | lag 3.40, 2.67, 2.07, 2.88 s | CONFIRMED | base range 1.91–335.6 s, median 4.27 s; all four in the lowest quartile |
| 4 mirrors | link ids | CONFIRMED | monotonic against all 290 discussion and 70 issue-comment ids in both mirror channels for Sep–Oct |
| 4 mirrors | thread parent, id hash, uniqueness | CONFIRMED | each parent is the PR's "opened" card; sha256 matches; no collision in 610,468 messages |
| 4 mirrors | `ts` last digit | FORMAT | problem 1 |
| Parent UPDATEs | `reply_count` 17, 42, 3, 8; `latest_reply` | CONFIRMED | base counts 16, 41, 2, 7; #468 correctly keeps the later merge broadcast |
| Parent UPDATEs | card fields not updated | FORMAT, coherence | problem 3 |

### (c) Slack

| Record | Claim or field | Verdict | Evidence |
|---|---|---|---|
| Frederick ask | placement, author active | CONFIRMED | DM members are Julia and Frederick; last base DM message is 09-18; Frederick posts in #executives at 20:27:30Z |
| Frederick ask | "pivot call" | UNCONTRADICTED, supported | Leonard 09-22 "in 15-20 days, we'll decide: either iterate or pivot" (`S/slack/messages/C090N54TG79/2025-09.json /537`); Frederick 09-29 19:42Z on a "substantial pivot" |
| Frederick ask | calendar ticket | CONFIRMED | ZOM-78 "Event Calendar For Zombie Match 3D", Backlog, created by Julia |
| Frederick reply | four rows exist on PNs Beta | CONFIRMED | `S/gsheets/data.json /sheets_spreadsheets/220/sheets/1` rows 2, 8, 10, 11 |
| Frederick reply | those four are not in the beta | CONFIRMED | Brian 09-22 16:22:44Z "postpone Axe Arena for the beta release" (`S/slack/messages/C05KNDCHAAG/2025-09.json /31`); the other three are Domino Delights events |
| Frederick reply | Zombie Lane is permanent | CONFIRMED | Confluence calendar: "Permanent (level-gated reward track)" |
| Robert approval | placement, author active | CONFIRMED | parent `S/slack/messages/C08R8CHB0QL/2025-09.json /121` had 0 replies; Robert posts in the channel at 16:25:31Z and 16:49:17Z |
| Robert approval | content | UNCONTRADICTED | Confluence: one-offs "should never displace a recurring slot without documented Product approval"; contacts list Robert as Chief Product Officer |
| Robert retraction | placement, author active | CONFIRMED | top-level after Julia's 20:46:05Z message; Robert posts at 21:26:55Z and 22:25:11Z |
| Vincent re-test | week boundary | CONFIRMED | `LEAGUES_SCHEDULE` prod `0 0 * * 1` (Monday 00:00 UTC); Sep 30 is a Tuesday |
| Vincent re-test | "still does not start a new week" after a restart | UNCONTRADICTED | base ZOM-429 (July) says a restart helps; this is a later test |
| Vincent re-test | author active | CONFIRMED | Vincent writes to Douglas at 21:58:44Z |
| All 5 | `ts` last digit | FORMAT | problem 1 |

### (d) Gmail

| Record | Claim or field | Verdict | Evidence |
|---|---|---|---|
| 6 threads | id >> 20 | CONFIRMED | arrival +0.4, +2.1, +2.9 s and +0.3, +2.2, +3.1 s; base median 1.2 s; ids absent from all 81,404 thread files |
| 6 messages | labels and `X-Gmail-Labels` | CONFIRMED | every combination exists in base; Julia's mailbox never uses `UNREAD` (0 of 304), unopened is `INBOX, CATEGORY_PERSONAL` (41) |
| 6 messages | snippet | CONFIRMED | equals the first 175 characters of the collapsed body |
| 6 messages | `internal_date` | CONFIRMED | equals the Date header, as in 6,078 of 6,085 base messages |
| Sep 26 mail | a mail of its own | CONFIRMED | no reply headers, own thread ids, new subject |
| Bodies | November season opens Sat Nov 1 | CONFIRMED | Season Pass spec and `SEASON_PASS_SCHEDULE` `0 0 1 * *` |
| Bodies | reward tiers, quest tables, premium track; agreed with Product | UNCONTRADICTED, supported | spec: 30 tiers, free and premium tracks, `daily_quest` points, "Owner: Robert (Product). Design partner: Julia Lawson" |
| Bodies | weekdays | CONFIRMED | Oct 29 Wed, Oct 31 Fri, Nov 1 Sat |
| Bodies | handoff dates, "September handoff" | UNCONTRADICTED | no base mail on the topic (0 hits for four phrases across all thread files) |
| 6 messages | Message-ID | FORMAT | problem 5 |
| 4 messages | Reply-To | FORMAT | problem 6 |
| 6 messages | other headers, `mbox_from` | FORMAT, cosmetic | problem 9 |

### (e) GCal, Drive, Docs, Slides, Sheets

| Record | Claim or field | Verdict | Evidence |
|---|---|---|---|
| GCal ×4 | ids, copies, attendee shape, self flags, sequence | CONFIRMED | base: one copy per internal attendee in 746 of 796 events; organizer copy self and accepted in 1,595 of 1,611 |
| GCal ×4 | no conflict, 15:00Z = 18:00 Istanbul | CONFIRMED | no base event in the four calendars on Oct 8 14:30–16:30Z |
| GCal ×4 | organizer active | CONFIRMED | Douglas posts 09-24 16:07–16:20Z and 09-26 16:06Z |
| Folder | parent, shape, name | CONFIRMED | Julia's root `d_8140f09b…`; no name clash; she is on Slack 08-11 07:29Z |
| Brief (Drive) | name, size, `content_path`, parent, times | CONFIRMED | base docs: `.docx` name, size and path never null (595 of 595) |
| Brief (Docs) | heading offsets | CONFIRMED | all 9 runs are line-exact with exclusive ends; heading-only run sets occur in 124 of 315 base docs with headings |
| Brief | C&W windows Mon-Tue, Wed-Thu, Fri-Sun at 00:00 UTC | CONFIRMED | `G/root/harmonygames-Games/match3d-backend/lib/zombies_game/win_and_collect.ex` lines 62–84; Brian's spec `f_7989a718…` |
| Brief | seasons open on the 1st at 00:00 UTC; config lock | CONFIRMED | Season Pass spec: "locked 24h before each season opens" |
| Brief | one-off rule, Product approval | CONFIRMED | Confluence calendar info box |
| Brief | Login Calendar row; Ready and LIVE columns; translated tab is the Domino set | CONFIRMED | PNs Beta row 12 and both status columns; `/sheets/2` has 44 "Domino" and 0 "Zombie" |
| Brief | Boss Arena off, hold rules, English-only | UNCONTRADICTED | rules of the brief; no base rule against them |
| Deck (Drive, Slides) | shapes, ids, null size and path | CONFIRMED | base slides: `BLANK`, one `TEXT_BOX` at 9144000×5143500, `slide_`/`el_` + 12 hex |
| Deck | weekdays of the four weeks | CONFIRMED | all eight labels correct |
| Deck | "UK and US first" | UNCONTRADICTED | base buys are UK only so far ("they are all UK", 09-19) |
| Deck | retention campaigns "already running" | TIMING CONFLICT, soft | problem 7 |
| Sheet (Drive) | `content_path` | FORMAT | problem 2 |
| Sheets rows | tabs, counts, headers | CONFIRMED | `sheet_id` = index; column count equals header length |

### (f) Trello

| Record | Claim or field | Verdict | Evidence |
|---|---|---|---|
| Card #61 | open, not completed | CONFIRMED | `closed` false, `dueComplete` false, badge false; Leonard completed other cards on 09-30 16:40Z but not this one |
| Action | id encodes its time | CONFIRMED | `68dac820` = 2025-09-29T17:55:44Z; base 5,203 of 5,252 |
| Action | payload | CONFIRMED | key set and order as the board's 12 base comments; `idShort` 61, `viBYIjSG`, `HSqnngwQ` |
| Action | list name "BETA: Sep 30" | CONFIRMED | 71 of 71 base actions from 09-12 16:42Z to 09-30 17:09Z carry it; the lists table says "BETA: Oct 10" (known issue SC-13) |
| Action | author | CONFIRMED | `PERSON_6094` is Leonard Hayes, a card owner; 23 base comments; on Slack 17:33–17:45Z |
| Action | Mon Oct 13 rollover | CONFIRMED | `G/root/harmonygames-Games/match3d-quests/lib/quests-stack.ts`: weekly cron `weekDay: 'MON'`, hour 0 |
| Action | new set not in yet | UNCONTRADICTED, supported | push sheet row 1 "Revisit once new quests roll out", Not Ready |
| Card UPDATE | badges, `dateLastActivity` | CONFIRMED | comments 0 → 1; other keys identical; board activity 09-30 17:09Z is later |

## 4. Records with no finding beyond shared cosmetic items

- Trello comment action and card UPDATE.
- GCal event, all four copies.
- Docs brief row, including all nine heading offsets, and its Drive row.
- Slides presentation, pages and elements; Sheets spreadsheet and both tabs.
- `ZM Live Ops` folder row, apart from item 12.
- `#470#ev_9`, `#473#ev_5`, `#471#ev_8` and the three PR `updated_at` bumps.
- The four mirrors on text, author, escaping, lag, link ids, parents and counts. Only the `ts` digit is wrong.
- The content of every Slack message, Gmail body, GitHub note and the Trello comment.

## 5. Searches run

- **SQL:** quote-aware parse of all 103 statements; per-row cross-checks.
- **Slack:** full scan of 4,840 files and 610,468 messages for `ts` format, id and `ts` collisions and thread conventions. Full reads of both DMs, #zombie-art Sep 15–20, #zombie-match3d and #executives Sep 26–Oct 1, #builds Sep 29–Oct 1, #zm-collect-win, #zombie-bugs Sep 30, #company-internal, and the Douglas, Arthur, Samuel and Martin–Claire DMs. Keyword sweeps over Sep–Oct 2025 for Halloween; vial, bottle and potion; Season Pass and November; prod and deploy; campaign, UA and geo; Axe Arena, Streak Fever, Hourly Coins and Treasure Hunt; quests. Per-author activity around each timestamp, and hour histograms.
- **#zombie-prs:** all 2,123 messages: 956 comment mirrors, 220 "opened" cards, lag distribution, id ordering across both mirror channels.
- **GitHub:** all reviews (2,230), review comments (1,387), PR comments (687) and timeline events (11,406) for shapes, numbering and post-merge latency; the four PRs in full; commits and PR lists. Repo trees of match3d, match3d-backend, match3d-quests and ZM-Liveops-Docs.
- **Gmail:** every message in the brian@, jlawson@ and frederick@ mailboxes (6,085); two byte scans of all 81,404 thread files for collisions, Brian's mail and topic phrases; one parsed scan for Message-ID, timezone and Reply-To conventions; GitHub notification coverage in Oliver's mailbox.
- **GCal:** all 10,395 events and 38 calendars.
- **Drive, Docs, Slides, Sheets:** all 53,631 Drive rows, 595 docs, 132 decks and 356 spreadsheets; the push sheet in full.
- **Trello:** all 5,252 actions, the board's lists, cards and members.
- **Confluence:** `page_liveops_calendar` and `page_season_pass_spec` in full.
- **Snowflake:** table list; `LIVE_EVENT_PERFORMANCE`, `PUSH_NOTIFICATION_STATS` and the UA spend mart for Sep–Nov 2025.
- **Reference:** contacts, persona roster, known-issue cards SC-13, SC-14 and SC-38.

## 6. Limits

- The base export has no Gmail `snippet` or `size_estimate`, no GCal description, and no GitHub `seq`, `pull_request_review_id` or `subject_type`. Those fields were checked for internal consistency only.
- `shared_roles_json` and `visibility_role` on Drive rows have no export counterpart.
- Linear comments and issue UPDATEs were not reviewed, except ZOM-78, ZOM-429 and ZOM-432 as context.
- Nothing was executed; whether a Drive read of the two files with a `content_path` succeeds needs a live check.
