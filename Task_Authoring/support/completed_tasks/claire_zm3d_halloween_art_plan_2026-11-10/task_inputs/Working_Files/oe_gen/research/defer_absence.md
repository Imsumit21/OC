# Act-vs-defer search and absence checks: Claire Morgan, Halloween task

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Persona: `claire_morgan` (claire.morgan@harmonygames.co, Art Lead / Design, usable in tasks).
Overlay: `01_Universe_Inject.sql` read as data from `Working_Files/oe_gen/sql_rows.json` (238 rows). "L123" means the SQL line. No SQL was executed.

## Bottom line

- **Part A:** no record says to hold, defer or skip any of the six write families. Every family's population finished. Nothing is UNRESOLVED.
- Eight overlay records narrow what a write may say or who gets it (section 3). The two that change the write count are Frederick's Sep 30 email (10 tickets get a Skip call and no assignment) and the Archive tab (ART-836..839 get no comment).
- **Part B:** seven of the eight checks match what you expected. Three additions:
  - B2: a second attachment sits on Martin's icon post, and it is a concept, not a store file.
  - B3: 5 Slack messages and 1 calendar copy that Claire can see are dated after Frederick's reply. None touches a date.
  - B7: the name "Marcus" is **not unique** in Linear or Slack. Marcus Lee exists in both.
- Claire cannot see #executives, which holds relevant UA talk. It holds nothing back from these writes (section 7).

## 1. How the search ran

**Scoped services.** `persona_view.py search claire_morgan <svc> <term> --limit 500000 --no-hidden --json`, across slack, gmail, gcal, gdrive, gdocs, gslides and gsheets. That was 756 calls: 72 terms in the first sweep and 36 in the second, over 7 services.

**Unscoped services.** `hg.py search search-many`, limit 200000 per query, on `linear/data.json`, `trello/data.json`, `github/data.json`, `confluence/confluence_working.json` and `contacts/contacts.json`. Snowflake got one `halloween` search: 0 hits, scan complete. It holds analytics and governs none of these writes.

**Overlay.** Every sweep term was matched against all 238 rows.

**Direct reads, not only term matches.**
- Every Slack message in Claire's channels from Sep 1 to the clock, read with `hg.py search get` (see the table below).
- All 846 threads in her mailbox, listed.
- All her calendar events from Sep 1 on.
- ZM ROADMAP: all 79 cards and 499 actions pulled; cards active since Jul 15 and every action since Sep 1 read.
- All 597 base ART issues pulled; every ticket from May 2025 on, plus all keyword matches, read.
- All 184 Drive records she can see, listed.

**Pagination.** Finished everywhere.
- persona_view: `visible_total == len(visible)` on all 756 calls. Largest result 2,045, limit 500,000.
- search-many: every query `scan_complete: true`, no errors, `files_completed == files_selected`. Largest result 390, limit 200,000.
- Slack `get`: 18 files, 1 page each, `truncated: false`, 3,478 messages.

**Terms.**
- Requested: halloween, defer, hold off, not yet, wait, as-is, accept, freeze, pause, postpone, cancel.
- Added: as is, on hold, delay, push back, scrap, 40 identifier, creative-name and store fragments, topic words, Oct date literals and leave words. Also Turkish `cadılar`, `ertele`, `iptal`, `reklam`, because Claire's DMs are partly Turkish.

**Window.** ART tickets were created from Sep 8, so the window read from Sep 1 to the clock. Term sweeps covered full history.

### Slack coverage, Sep 1 to clock (base; 78 visible channels, 16 active)

| Depth | Channels | Messages |
|---|---|---|
| Read every message | zombie_marketing 12, company-internal 40, zombie-ops 28, random 13, zombie-art 271, six DMs 175 | 539 |
| Term sweep plus topic filter (ads, UA, creative, marketing, campaign, store, listing, capture, end card, submit, leave words) | zombie-match3d 473, zombie-bugs 1,097, zm-animations 203 | 1,773 |
| Term sweep only (bot feeds) | builds 1,137, engineering-bots 29 | 1,166 |

The 16 overlay Slack rows are all YES for Claire in `check-sql` and were read in full.

### Term counts (Claire-visible, or unscoped; Slack and Gmail show all time / since Sep 1)

| Term | Slack | Gmail | Drive names | Docs | Sheets | Slides | Linear | Trello | GitHub | Confluence | Overlay rows |
|---|---|---|---|---|---|---|---|---|---|---|---|
| halloween | 24 / 2 | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 45 |
| defer | 3 / 0 | 1 / 0 | 0 | 0 | 0 | 0 | 1 | 0 | 14 | 0 | 0 |
| hold off | 12 / 0 | 0 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| not yet | 57 / 0 | 2 / 0 | 0 | 0 | 0 | 0 | 1 | 0 | 13 | 5 | 0 |
| wait | 841 / 36 | 55 / 10 | 0 | 2 | 4 | 0 | 88 | 9 | 390 | 0 | 0 |
| as-is | 23 / 0 | 1 / 0 | 0 | 0 | 0 | 0 | 5 | 0 | 12 | 0 | 0 |
| as is | 107 / 7 | 4 / 0 | 0 | 0 | 1 | 0 | 5 | 0 | 56 | 3 | 0 |
| accept | 117 / 4 | 33 / 3 | 0 | 2 | 0 | 0 | 24 | 5 | 69 | 0 | 7 |
| freeze | 122 / 21 | 2 / 1 | 0 | 0 | 2 | 0 | 14 | 12 | 43 | 10 | 0 |
| pause | 73 / 3 | 16 / 0 | 0 | 1 | 1 | 0 | 11 | 0 | 191 | 0 | 6 |
| postpone | 27 / 3 | 1 / 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 0 | 0 |
| cancel | 314 / 2 | 81 / 2 | 0 | 0 | 3 | 0 | 385 | 11 | 43 | 0 | 62 |
| on hold | 4 / 0 | 2 / 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| delay | 505 / 1 | 11 / 0 | 0 | 0 | 2 | 0 | 41 | 0 | 247 | 0 | 0 |
| push back | 16 / 0 | 0 / 0 | 0 | 0 | 0 | 0 | 1 | 0 | 5 | 0 | 0 |
| scrap | 12 / 0 | 5 / 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |

Calendar: `persona_view` matches event summaries only, so I also ran `hg` over the whole gcal JSON for halloween, defer, hold off, not yet, wait, as-is, freeze, pause, postpone, vacation, out of office and ZM3D. All 0.

Reading the overlay column:
- `accept` is `responseStatus: accepted` on the 7 calendar copies.
- `cancel` is the column name `canceled_at` on all 62 Linear rows. Only ART-836..839 are actually Canceled.
- `pause` is ART-836..839 and two sheet tabs.
- The overlay has no human text using defer, hold off, not yet, wait, as-is, freeze or postpone.

What the hits turned out to be:
- The two in-window `halloween` Slack hits are C20 and a Sep 19 list of game object ideas. The 36 `wait` hits and the other in-window hits are game logic, code review, bot text or the Sep 22 Axe Arena postponement. None holds an ad or store art.
- The in-window Gmail hits are newsletters, PR notifications, meeting notes and award spam.
- Full-history Slack hits from Dec 2024 to Aug 2025 (46 for the strong terms, leaving out bot feeds and the two old god- channels) include "Hold off on UA due to bug?" on May 14 and "we paused tablet traffic" on Jul 10. Both are about older tests, predate every ticket, and the live sheet supersedes them.
- Noise terms in Linear, GitHub and Trello were accepted on the Eval 2.6 rule that a candidate must name the target or the decision. Identifier and creative-name searches were run separately (Family 1).

## 2. Candidate register (all Claire-visible)

| ID | Record | Locator | Date (UTC) | Status at the clock |
|---|---|---|---|---|
| C1 | Leonard's ask | Slack C06DJBJL798 ts 1759269913.882683 (L19) | Sep 30 22:05:13 | Governs the ask; stills maker narrowed by C19 |
| C2 | Frederick, "October UA plan (draft)" | Gmail .../1843080777036925215 (L224, L226) | Sep 12 17:40 | **Superseded** by C4 |
| C3 | Frederick, "Unity retention restart" | Gmail .../1844644077950167516 (L250, L251) | Sep 29 23:48 | Governs placements of ART-811, ART-813 over their ticket comments |
| C4 | Frederick, "October UA plan - changes" | Gmail .../1844732284519287777 (L270, L271) | Sep 30 23:10 | Governs flight, tablet end; Oct 15 date narrowed by C5 |
| C5 | Frederick's Unity reply | Slack C0880U9751A thread 1759211437.306779, ts 1759275738.984915 (L30) | Sep 30 23:42:18 | **Latest date authority.** Android US phone Oct 10, iOS UK stays Oct 15 |
| C6 | ZM3D live creatives sheet | f_02b1968f5e882366fbb883 (L190, L192-196) | modified Sep 30 22:30 | One version; governs the live list except C23 and ART-831 |
| C7 | ZM3D release calendar, Q4 | f_fdd6d2d2f4a4d2f5b908fb (L197, L199), rev dc309c94e6 | modified Sep 30 22:40 | One version; governs store dates, overrides C1's "around the 24th" |
| C8 | Seasonal art direction, Q4 2025 | f_5ebf55ad29e815d46243c8 (L205-220), rev 09590bf741 | Sep 25 16:10 | One version; governs call rules |
| C9 | Robert's pointer to C8 | Slack C08R8CHB0QL ts 1758817822.269981 (L2) | Sep 25 16:30 | Governs |
| C10 | Marcus re-recorded 3 cuts | Slack C09ATAJ220H ts 1758823964.738872 (L9) | Sep 25 18:12 | Governs capture of ART-795, 805, 797 over their comments |
| C11, C12 | Claire asks Marcus for a test; Marcus reply | Slack D05V2N6PZNU (L15, L16) | Sep 26 07:40; Sep 29 17:20 | C12's file superseded by C14 |
| C13-C15 | Marcus test post; Robert rejects; Marcus will redo | Slack C08R8CHB0QL thread 1759167065.499092 (L10-12) | Sep 29 17:31; Sep 30 16:05; 16:21 | **C14 and C15 govern** |
| C16, C17 | Martin exported store screens; Leonard reply | Slack C08R8CHB0QL thread 1759245641.309714 (L17, L18) | Sep 30 15:20; 15:47 | C17 governs |
| C18, C19 | Martin's leave post; Leonard's reply | Slack C05KNDCHAAG thread 1759243286.478812 (L13, L14) | Sep 30 14:41; 23:31 | **Govern.** C19 is later than C1, so Julia makes statics |
| C20, C21 | Martin's icon concept; Robert's reply | Slack C08R8CHB0QL ts 1758121809.236839 (base `messages/C08R8CHB0QL/2025-09.json` /121) and L27 | Sep 17 15:10; 16:52 | C21 governs |
| C22 | Trello "Halloween push" card | 68dc52e015f87c50c441d1a9 (L317, L319), list "Oct 21" | Sep 30 22:00 | One version |
| C23 | Frederick on C22: Julia's 4:5 | Trello action 68dc65a0f2d7fb28743f5860 (L320) | Sep 30 23:20 | Governs over C6 for ART-826 |
| C24 | Frederick on end card 001 | Trello action 68d6cff0c6568da5d9c8e81f (L321), card 68768a1501ae552dbee94b8a | Sep 26 17:40 | Governs |
| C25 | ZM3D Halloween review | Calendar evt_d947bf7cd910549b674b1f (L309) | created Sep 30 22:10; meets Oct 2 16:00 | One version, sequence 0, confirmed |
| C26 | 62 ART tickets, 75 comments | Overlay L33-L170 | Sep 8 to Sep 29 | Newest comment per ticket, then C3 and C10 |
| C27 | Halloween Drive folders, 11 PNGs, 2 test MP4s | L173-189 | Sep 29, Sep 30 | MP4s rejected by C14 |
| C28 | Base ART-790, ART-792 (open, Martin) | `linear/data.json` /issues/590, /591 | Jul 9, Aug 26 | Non-Halloween A/B screenshot work; no conflict |
| C29 | KayKit Halloween Bits offer | Gmail .../1844154099753384967 (L305, L306) | Sep 24 14:00 | Unrelated to the writes |
| C30 | Leonard flying to LA | Slack C05KNDCHAAG ts 1759279503.256079 (base `2025-10.json` /0) | Oct 1 00:45 | Agrees with C25's note; no effect |

SQL L171 updates base ART-792 only to clear `time_in_status_minutes`. It changes no content.

## 3. Records that say to hold, defer or not do something

None bars a family outright. These bar a subset or set the content.

| Record | Quote | Effect |
|---|---|---|
| **C4** | "so don't make Halloween versions of anything that only runs there." | Bars new work on Android-US-tablet-only ads. Those tickets still get a comment (Skip), with no assignment. |
| **C3** | "I left squirrelfail landscape and mrfluffernot landscape off iOS UK tablet this time" | Moves ART-811 and ART-813 into the C4 set, against their ticket comments. |
| **C6 Archive + ART-836..839** | "Paused or retired creatives move to Archive." "Paused on Sep 15/19" | No comment on these 4 Canceled tickets. |
| **C14, C15** | "We can't ship these, they need doing again from the Sep 16 one" / "ok, i will redo both from the sep 16 capture" | Bars reusing f_dc5cf9e4250d433c1511ec and f_bcd34f98925e3f20d846ce. ART-808 and ART-816 are not Reuse. |
| **C17** | "whatever is already exported is done so no tickets needed for those, tickets are just for store art that still has to be made" | Bars tickets for the iPhone 6.5 and Google Play sets. |
| **C21** | "Nice for an event, but not for the app icon, it gets too busy at that size." | Bars using Martin's concept as the icon. Supports a new ticket. |
| **C24** | "They can keep serving for now but they need a re-render before anyone builds on them." | Bars a Halloween pass on ART-833, 834, 835, 848 until re-rendered. |
| **C8 slide 2** | "redone on the current build first", music "re-cut first" | Order of work, not a hold on a write. |

Date overrides, not holds:
- C5 replaces C4's Oct 15 for Android US phone with Oct 10.
- C7 replaces C1's "maybe we swap the icon around the 24th?": Oct 16 12:00 PT cut, live from Oct 22.

## 4. Part A by write family

Services searched for every family: Slack (78 channels and DMs), Gmail (Claire's mailbox), Calendar (her own), Linear, Trello, Drive, Docs, Sheets, Slides, GitHub, Confluence, plus Contacts. Pagination finished in all of them.

### Family 1: 58 Linear comments (ART-793..854 except 836..839). Result: no hold.

**Population**
- Identifier literals `ART-79`, `ART-8`: 4 Linear hits, all on ART-790 and ART-792 and outside the range. 0 in Slack, Gmail, Trello, Drive family, GitHub, Confluence.
- Overlay: 62 issues, 75 comments, 56 Unity rows, 4 Archive rows.
- Creative names: 32 Slack hits, Dec 2024 to Jul 2025, all file posts or level names. 106 end-card hits; those since Mar 2025 were read. None is a decision. GitHub: 3 branch or commit names. Trello: "End Cards" (empty, Feb 2025) and "Find playable vendors. Prioritize endcards."
- Base `/comments` in Linear is an empty array, so all 75 comments are overlay.
- Decision records: C1-C10, C13-C15, C23, C24, C26 (16 register entries).

**Governing version:** see the register. Per ticket, take the newest ticket comment, then apply C3 and C10.
- ART-808 and ART-816: the Sep 16 re-capture comments replace the Jul 28 capture.
- ART-811 and ART-813: C3 replaces the Sep 9 "Still running" comments.

**Result:** 58 = 56 sheet rows + ART-826 + ART-831. No record bars a comment on any of them.

### Family 2: 48 assignments. Result: no hold on the 48; 10 not-do tickets confirmed.

**Population:** Family 1's, plus maker records C1, C18, C19, 7 statics tickets, and all 41 Linear users.

**Count reconciles:** 58 minus 10 tablet-only = 48. The newest placement in comments gives 8 Android-US-tablet-only tickets: ART-806, 820, 821, 822, 824, 842, 844, 849. C3 adds ART-811 and ART-813. Only those 10 fall under C4.

**Governing version:** C4 over C2. C19 (23:31) over C1 (22:05) for stills, so ad statics go to Julia.

**Result:** no record says not to assign the 48. Nobody is on recorded leave for Marcus or Julia (B6). The call for each ticket is yours; I only checked that the count reconciles.

### Family 3: 2 new ART tickets. Result: no hold.

**Population:** C1, C6 Store tab, C7, C16, C17, C20, C21, C27, C28, plus `halloween` in Linear (0 base, 0 overlay Linear rows) and Trello (only C22-C23).

**Governing version:** C17 limits tickets to art still to be made. C21 keeps the icon open. B1 and B2 confirm neither file exists.

**Result:** no Halloween ART ticket exists yet, so there is no duplicate. No record defers either ticket. Planning consequence: Martin is out Oct 6-15 and "store art stays with me" (C18), and the C7 cut is Oct 16 12:00 PT.

### Family 4: plan doc and tracker. Result: no hold.

**Population:** C1, C22, C25, plus B5's ownership check.

**Governing version:** one version of each. All dated Sep 30.

**Result:** every record asks for them. Nothing exists yet that would make them duplicates.

### Family 5: sharing with six attendees. Result: no hold.

**Population:** C25's 7 copies (one per attendee), plus an extra phrase sweep over overlay and in-window Slack for "don't share", "do not share", "confidential", "internal only", "keep this", "just between", "not ready": 0 relevant.

**Governing version:** sequence 0, status confirmed, no later edit. The six are Leonard, Frederick, Martin, Marcus, Robert, Arthur.

**Result:** no record restricts sharing with any of them. Julia is not on the review (section 7).

### Family 6: reply in Leonard's thread. Result: no hold.

**Population:** C1 and its thread.

**Governing version:** `reply_count` 0, one version. See B5.

**Result:** no record says to wait. C1 asks for the links before Thursday's review. C30 changes nothing.

## 5. Part B absence checks

### B1. Store folder d_74a7c95c28097dd9777e01 holds no iPad file. Confirmed: 0 iPad files, 11 visible.

- **Method and scope:** every overlay `drive_files` row with this id in `parents_json`; `hg` search of base Drive; persona search of Drive names.
- **Queries:** `d_74a7c95c28097dd9777e01`, `iPad`, `ipad`, `12.9`, `2732`, `2048`, `tablet`.
- **Surfaces:** overlay rows; base `gdrive/data.json`; Claire's visible Drive.
- **Results:** folder id in base 0, complete. iPad-like names Claire can see 0. Base has 2 `ipad` names and 13 each for `2732` and `2048`, all hidden from her and none a Halloween file (`app store iPad screens`, 2024, a `gameplay_short_04 Ipad` caption file, and hash-named JSON whose names merely contain the digits). Overlay iPad rows 0.
- **Positive control:** the same row filter returns 5 iPhone 6.5 and 6 Google Play files. `12.9` in Slack finds Martin's base Jul 29 `iPad Pro 12.9-inch_ 2048 × 2732` posts, so the term works.

All 11 are owned by Martin, private, with Claire in `shared_with_emails`; `check-sql` gives all 19 Drive rows YES.

| Line | Id | Name | Bytes | Modified (Sep 30) |
|---|---|---|---|---|
| L177 | f_a72a7fd18327ed34fa2ac6 | ZM3D_Halloween_iPhone65_01_1242x2688.png | 2042056 | 15:12:04 |
| L178 | f_facf46180c5ba68c35925d | ZM3D_Halloween_iPhone65_02_1242x2688.png | 1886761 | 15:12:07 |
| L179 | f_60aee1e96a59111c246a73 | ZM3D_Halloween_iPhone65_03_1242x2688.png | 1948940 | 15:12:10 |
| L180 | f_8a09205b3ab1ae2b7061b3 | ZM3D_Halloween_iPhone65_04_1242x2688.png | 1939115 | 15:12:13 |
| L181 | f_353fa24f04ab2c658d09bb | ZM3D_Halloween_iPhone65_05_1242x2688.png | 2488139 | 15:12:16 |
| L182 | f_dc52b1cdde87ff49f36bc1 | ZM3D_Halloween_GooglePlay_phone_01_1080x1920.png | 2529361 | 15:12:19 |
| L183 | f_e84ff3bed0d6eb20aa6ae5 | ZM3D_Halloween_GooglePlay_phone_02_1080x1920.png | 1901730 | 15:12:22 |
| L184 | f_846e988c8642078ec32fd8 | ZM3D_Halloween_GooglePlay_phone_03_1080x1920.png | 2176966 | 15:12:25 |
| L185 | f_ca2f05278861dc6e12ecfd | ZM3D_Halloween_GooglePlay_phone_04_1080x1920.png | 2467259 | 15:12:28 |
| L186 | f_a1582de8fc89f7ab4d42e8 | ZM3D_Halloween_GooglePlay_phone_05_1080x1920.png | 2279853 | 15:12:31 |
| L187 | f_fcfdf5502a68b1797fa0db | ZM3D_Halloween_GooglePlay_phone_06_1080x1920.png | 1943242 | 15:12:34 |

### B2. No store-ready Halloween app icon Claire can see. Confirmed: 0 store-ready, 1 concept.

- **Method and scope:** persona search of every scoped service; `hg` search of unscoped services; `hg files` over blobs and attachments in 9 services; Slack `files.json`.
- **Queries:** `halloween`, `appicon`, `app_icon`, `app icon`, `app-icon`, `icon`, `F09FN3SLD9T`.
- **Results:**
  - Drive names with `halloween`: Claire 0 base, 14 overlay rows, none an icon. The 8 hidden base files are `icon_chapter1_HalloweenMansion_*` chapter art, not an app icon. Drive names with `icon`: Claire 0, plus 1 UNVERIFIED domain file (the 48 base names are folders, chapter art and a LiveOps doc; none is an app icon).
  - Slack `files.json`: 2 Halloween-named files. One is a 2024 costume image. The other is `AppIconHalloween.png`.
  - Gmail, Linear, Trello, Confluence: 0 icon files.
  - GitHub: 427 `halloween` paths, all the KayKit Halloween Bits pack in `match3d`, none with `icon` in the path. `Assets/Textures/AppIconFG.png` and `AppiconBG.png` are the current icon.
- **Only match:** `AppIconHalloween.png` (F09FN3SLD9T, 2048×2048, Martin) on his Sep 17 post. `can-see` YES, metadata only. Its sibling attachment is `image 11.png` (F09FN3YJ7D3, 1921×751). C21 rejects the concept as an app icon.
- **Hidden from Claire:** Martin and Marcus discussing the icon in DM D05TZ6N23F1 /187-/199.
- **Positive control:** `appicon` finds that file in Claire's Slack, so the route works.

### B3. Nothing after Sep 30 23:42:18Z changes Oct 10 or Oct 15. Confirmed: 0 changes.

- **Method and scope:** all overlay date fields; Claire's Slack messages after ts 1759275738.984915 up to the clock; literal `2025-09-30T23:` and `2025-10-01` in Trello, Linear, Drive, Docs, Sheets, Slides, Calendar, GitHub, Confluence, and `2025-10-02` in all of those except Sheets; Claire's mailbox list.
- **Date-text queries:** `Oct 10`, `Oct 15`, `Oct 17`, `Oct 18`, `Oct 12`, `Oct 20`, `October 10`, `October 15`, `10 Oct`, `15 Oct`.
- **Overlay:** 0 rows later than L30. Latest per service: Slack L30, Trello L320, Gmail L271.
- **Claire-visible later records (6):** company-internal C30, 4 build-bot posts (`messages/C05433XK267/2025-10.json` /0-/3), and calendar copy `/events/8858` (Mid Week Art Sync, created Oct 1 00:02:44). None touches a date. Her mailbox ends Sep 30 08:10:02 in base and 23:10:00 in the overlay.
- **Not visible to Claire:** 13 other calendar copies (Art Sync, a Dentsu meeting), 2 ENG archive stamps, and export `updated_at` stamps.
- **Base date text in window:** 0 Slack or Gmail hits for the UA dates. The only Trello hits are list names ("BETA: Oct 10", an old "Oct 15") and a Metabase card. `Final Call ... Deadline: Oct 17` is award spam.
- **Positive control:** `Oct 10` finds L30.

### B4. Other live ads off the sheet. Confirmed: 0 beyond ART-826 and ART-831.

- **Method and scope:** set comparison of overlay tickets against the sheet; all 597 base ART issues; overlay and in-window phrases.
- **Queries:** description prefix `UA creative library`; `still running`, `still serving`, `keep serving`, `never made it`, `not on the live`, `off the sheet`, `running on unity`, `Unity:`.
- **Overlay:** 62 tickets start "UA creative library" (ART-793..854). Unity tab 56, Archive 4, off both 2: ART-826 (C23) and ART-831 (comment: "Not on the live creatives sheet yet."). No duplicates or blanks; no sheet row without a ticket.
- **Base:** 597 issues, ART-70..792. None has a `Unity:` placement. 22 titles look ad-related, all production tasks from 2023 to Dec 2024 (UA Video 1-6, ART-591, ART-595, ART-743, ART-749, ART-753, ART-755 and others). ART-753 and ART-756 look like the work behind creatives already tracked as ART-810 and ART-814. 0 are serving creatives.
- **Phrases:** the only other hits are 10 "Still running" comments on sheet tickets, and C24's "keep serving" on end card 001.
- **Not live:** a playable ad is in asset collection (D076Y0SDV18 Sep 24, zm-animations Sep 26). Facebook is not in the sheet's four Unity campaigns.
- **Positive control:** the comparison finds exactly the two known off-sheet tickets.

### B5. Leonard's thread and any existing plan or tracker. Confirmed: 0 replies, 0 files.

- **Thread method:** overlay row L19, base channel files. **Queries:** `1759269913`; `thread_ts`/`thread_parent_id` references.
- **Thread results:** `reply_count` '0', `latest_reply` null. Base `messages/C06DJBJL798/*` (19 files, complete): 0 hits. No 2025-10 file. Overlay references to this ts: 1 (L19 itself).
- **Thread control:** the same fields show Frederick's thread at 5 (L32) and Martin's at 1 (L29).
- **Plan and tracker method:** Claire's 69 owned Drive records (31 folders, 37 JSON, 1 spreadsheet); all 184 visible; Docs, Sheets, Slides title and body. **Queries:** `halloween`, `tracker`, `plan doc`, `ZM3D`.
- **Plan and tracker results:** Claire owns 0 Halloween files. Her only owned spreadsheet is `Untitled spreadsheet.xlsx` (2023). `App Version Tracker.xlsx` is shared and unrelated. None of the 19 overlay Drive rows is owned by Claire: Martin 11, Leonard 3, Marcus 2, Frederick 1, Arthur 1, Robert 1.
- **Plan control:** the same filter returns all 69 owned records.

### B6. Other statics makers, and leave for Marcus or Julia. Confirmed: 0 other makers, 0 leave posts.

- **Method and scope:** all Claire-visible Slack, Gmail and her calendar; god-mode Slack Sept search and the Calendar export for Marcus and Julia, to check for records she cannot see.
- **Queries:** `statics`, `ad statics`, `static`, `takes over`, `taking over`, `cover for`, `covering`, `vacation`, `out of office`, `ooo`, `on leave`, `time off`, `day off`, `days off`, `pto`, `holiday`, `takes the`, plus each person's Sept messages.
- **Statics:**
  - Overlay hits are C18 and C19 only.
  - All 7 statics tickets say "Made by Julia Lawson".
  - Base agrees: Julia posted the 1:1 and 4:5 in zombie_marketing on Jun 6 (`2025-06.json` /3) with the "they're coming, stop them!" copy.
  - No other maker is named. C1's "Martin has the icon and the stills" is overtaken by C19 for ad statics.
- **Marcus's work:** no one takes it over. All 3 `takes over` hits and 5 `taking over` hits are unrelated.
- **Leave:**
  - Marcus: Sep 5 post for Mon Sep 8 only.
  - Julia: Sep 3 fever, back Sep 4. Sep 1 floating holiday.
  - 0 posts near October.
  - Their calendars show no out-of-office event from Sep 15 to Nov 10.
  - The Nov 24 to Dec 5 leave requests (hidden DMs) are by EMPLOYEE_0032, not either of them.
- **Positive control:** `vacation` finds Martin's Sep 1 post and C18; `out of office` finds Marcus's Sep 5 post.

### B7. Linear users. Marcus is **not unique** by first name; Julia and Martin are.

Method: full `/users` (41 records) and `/team_memberships` (76) via `hg get`; `hg.py records` on email. Linear stores the email as `name` for these users, so "Marcus Bennett" matches nothing. Match on email or id.

| Person | Id | Pointer | name field | Active | ART membership |
|---|---|---|---|---|---|
| Marcus Bennett | usr_c77c50cc15c5342d | /users/33 | marcus.bennett@harmonygames.co | true | yes, /team_memberships/13 |
| Julia Lawson | usr_8140f09bf9f1b94c | /users/18 | julia.lawson@harmonygames.co | true | yes, /team_memberships/9 |
| Martin Walsh | usr_51f5f16d46e8cf55 | /users/9 | martin.walsh@harmonygames.co | true | yes, /team_memberships/4 |
| **Marcus Lee (decoy)** | usr_b501f018a4c5319f | /users/28 | marcus.lee@harmonygames.co | true | no teams at all |

Count: `marcus` 2, `julia` 1, `martin` 1. Control: Claire resolves at /users/17 with ART membership at /team_memberships/8.

### B8. Slack ids. All seven confirmed.

Method: `hg.py records` on `slack/users.json`, field `id`; 218 records checked, complete. Each record has `is_bot: false`, `deleted: false`. Control: looking up by email returns the same seven.

| Slack id | Person | Email | Pointer |
|---|---|---|---|
| EMPLOYEE_0002_SLACK_ID | Marcus Bennett | marcus.bennett@harmonygames.co | /0 |
| EMPLOYEE_0005_SLACK_ID | Julia Lawson | julia.lawson@harmonygames.co | /3 |
| EMPLOYEE_0008_SLACK_ID | Frederick Stone | frederick.stone@harmonygames.co | /6 |
| EMPLOYEE_0009_SLACK_ID | Claire Morgan | claire.morgan@harmonygames.co | /7 |
| EMPLOYEE_0016_SLACK_ID | Robert | robert@harmonygames.co | /9 |
| EMPLOYEE_0033_SLACK_ID | Martin Walsh | martin.walsh@harmonygames.co | /20 |
| EMPLOYEE_0038_SLACK_ID | Leonard Hayes | leonard.hayes@harmonygames.co | /23 |

Sample record: `{"id": "EMPLOYEE_0005_SLACK_ID", "name": "Julia Lawson", "real_name": "Julia Lawson", "display_name": "Julia Lawson", "email": "julia.lawson@harmonygames.co", ...}`. Note PERSON_2705_SLACK_ID is Marcus Lee at /29.

## 6. Evidence limits

- Claire cannot be proved to read the 56 public channels she has not joined (UNVERIFIED) or the 108 domain-visible Drive files. Eval 2.6 limits the search to channels she belongs to. A god-mode Sept/Oct Slack search found 1 Halloween hit outside her channels (the D05TZ6N23F1 icon DM) and 0 for `hold off` or `on hold`.
- Text inside Drive JSON, text and CSV blobs, and Gmail attachments, was not searched. Only 2 of Claire's 184 Drive records were modified after Jul 15, and neither is relevant.
- Docs, Sheets and Slides comments are not in the exports.
- Turkish DMs carry anonymisation tokens that hide some words. The surrounding text is about game items, a 1:1 and a sick day.
- `can-see` needs a base id, so overlay ids were judged with `check-sql`: 69 YES, 24 NO, and all 24 NO are other people's Gmail copies.

## 7. Notes for the ledger

- **Hidden from Claire, do not cite.** #executives (C07C2866011, members 9):
  - Sep 12 /470, /477, /487: Leonard asks about killing Marcus's creatives. Frederick: "Probably not yet" and "Just not simple enough to say they are underperforming and should be paused".
  - Sep 19 /819 and Sep 29 /1166: Unity budget set to $1, then restored to $150.
  - These agree with C3 and hold nothing back.
- **Julia** is not on the review (C25) and not shared on the Halloween folders, though she would be the statics assignee. The prompt's sharing list is the review only.
- **Maker mapping is not in this report.** C1 says Marcus has video and end cards, while ART-832 says "Made by Martin Walsh" and many videos say "Made by Frederick Stone". Those are history, not assignments, but the ledger should state the rule it uses.
- **Slack "Harmony Games Calendar"** (Marcus, Sep 5) has no matching shared calendar in the export: all 38 calendars have empty sharing.

## 8. Helper scripts

All read-only, in `Working_Files/oe_gen/research/`: `defer_scan.py`, `defer_scan2.py`, `slack_window.py`. Raw results stayed in the session scratch folder.
