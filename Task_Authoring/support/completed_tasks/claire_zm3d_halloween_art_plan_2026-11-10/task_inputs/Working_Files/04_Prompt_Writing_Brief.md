# Prompt Brief — claire-zm3d-halloween-art-plan · prep

> Built 2026-11-06 from `00_Assigments.md`, `Working_Files/00_Task_Context.json`, `Working_Files/01_Grounding_Dossier.md` (incl. Facts for the human), `01_Universe_Inject.sql` (sha256 0a08dedecd60, revision rev3: 233 INSERT, 5 UPDATE), `03_Error_Async_Config.txt` (Friction: none), `Working_Files/01a_Hardening_Report.md` (§10, §11, S0r outcome), `Working_Files/scenario_gen/apply_rev3.py`, `Working_Files/solver/truth.json`, `Working_Files/01_Scenario_Design.md`, `Working_Files/01_Hardness_Manifest.json`, `Working_Files/scenario_gen/rubric_only_facts.json`, `Evals/references/tools/catalog.json` · Persona view verified: all (check-sql PASS, 0 load-bearing rows not visible; base records can-see YES) · no reference files (`02_Reference_Files/` holds only its README)
> Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) · seed bound 2025-10-01T00:00:00Z · persona today Wed Oct 1, 2025
> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human.

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
| --- | --- | --- |
| Business function | Design | `task_categories.md` nearest of the six: creative / design production. The work is art production planning for marketing surfaces (icon, store screens, UA video and statics), owned by the Art Lead; Leonard asks her to "own the art side" (`C06DJBJL798/1759269913.882683`). Spend, budgets and media buying stay with Frederick (UA) and are never asked. |
| Persona | Claire Morgan · claire.morgan@harmonygames.co · Art Lead (Design) · Slack EMPLOYEE_0009_SLACK_ID · Linear usr_7fe31e7ec8199618 | Voice: a busy art lead delegating to her assistant in plain colleague English; remit: she leads the art side of the push (the ask's owner split: Martin Walsh icon and stills, Marcus Bennett video and end cards; Julia Lawson takes the ad statics while Martin is out, `C05KNDCHAAG/1759243286.478812`, `C05KNDCHAAG/1759275107.322377`) and reacted to Martin's Halloween icon concept (`C08R8CHB0QL/1758121809.236839`, ghost + jack_o_lantern reactions). Read scope: member of #zombie_marketing `C06DJBJL798`, #zombie-art `C08R8CHB0QL`, #zombie-match3d `C0880U9751A`, #zm-animations `C09ATAJ220H`, #company-internal `C05KNDCHAAG`, #builds `C05433XK267`, her IM with Marcus `D05V2N6PZNU`; her own mailbox and calendar; Drive files shared with her. |
| Competency | Marketing and GTM | Focus: seasonal go-to-market for Zombie Match 3D — every store surface and every running UA ad gets a Halloween call, a maker and a hand-off date against the store submission cut and the UA flight. Outputs: a plan and a tracker the team reviews, tickets and assignments that let UA queue uploads. Remit: Leonard (CEO) assigns her the art side of the push in the marketing channel. |
| Task skill | Authoring | The plan doc (an authored artifact: calls by surface type, ship route and dates, reuse, owners) and the tracker; supporting writes: 58 ticket comments, 48 assignments, new store-art tickets, the thread reply. |
| Task type | long-horizon (Long Horizon) | Tier 100–500+ counted calls. Services carrying a deciding fact (measured from the SQL): Linear 62 seeded library tickets + 75 comments (58 per-ticket reads, 58 comments, 48 assignments), Slack (14 seeded messages over #zombie_marketing, #zombie-art, #zombie-match3d, #zm-animations, #company-internal and the IM, plus base threads such as `C06DJBJL798/1755114007.441789`), Sheets (4 tabs: Store 4 rows, Unity 56, Archive 4; 62 serving surfaces with the 2 off-sheet tickets), Docs (calendar), Slides (4-slide deck), Gmail (3 Frederick mails + the vendor quote in Claire's mailbox), Drive (3 folders, 13 files), Trello (2 comments on 2 cards), GCal (review). Conditional reads only: Contacts, GitHub, Confluence, Snowflake. Call budget: unconditional floor 197 / planned 218 (`01_Hardness_Manifest.json` call_budget; volume_exception call_budget_floor 181 at the requester's "over 180 tool calls in each run"); the prompt states no count, step list or service list. |
| Difficulty mode | medium (cap < 85 %; requester target < 80 %, < 70 % preferred) | Assigned mode is never switched; difficulty comes from the eleven mechanism rules in records (`01_Hardness_Manifest.json` mechanism_portfolio), six of them rev3's moves off the swept path (R_TEST_TURNED_DOWN, R_REVIEW_WINDOW, R_RECAPTURE_NOTE, R_STATICS_COVER, R_TABLET_TRIM, R_OLD_PACKS), never from the prompt. |
| Freeze and clock | October 1, 2025 07:00 → freeze 2025-10-01T00:00:00Z, synth-cut | Every seeded event ≤ the seed bound (latest: Frederick's reply `C0880U9751A/1759275738.984915`, 2025-09-30T23:42:18Z); the review (`evt_d947bf7cd910549b674b1f`, Thu Oct 2 16:00Z) and the plan dates are future plan fields. No shutdown rule applies (synth-cut). |

## 2 · Situation

| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |
| --- | --- | --- | --- |
| Leonard wants everything players see of Zombie Match 3D to look like Halloween for late October and asked Claire, yesterday, to own the art side: a call per live store surface and ad, makers and dates, a plan doc and a tracker, ticket follow-through, links before Thursday's review. Nothing exists yet: no plan, no tracker, no ticket comments. | Claire (she is @-mentioned) | `C06DJBJL798/1759269913.882683` (#zombie_marketing, Tue Sep 30 15:05 PT); the review `evt_d947bf7cd910549b674b1f` on her calendar ("Claire walks us through the Halloween plan and tracker. I'm in LA Thursday so I'll dial in for this one.") | Recipient copies of Frederick's three mails in Leonard's, Frederick's, Marcus's and Martin's mailboxes (12 rows; Claire holds her own copy of each, including `claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>`); none is needed. |

## 3 · Investigation → action

Questions to resolve (answers live only in records; never in the prompt):

1. What is live today — which store surfaces and which ads, and which ones the obvious list leaves out or should not carry?
2. For each surface, which call applies under the seasonal art direction, and what already exists that can be reused?
3. For each ad, which campaigns it runs on today, what it was captured or rendered from, how its master was mixed, and what has changed since its ticket note?
4. Which campaign changes and hand-off dates hold for October, on which campaigns, and which earlier plan or date they replace?
5. When must store and in-app pieces be merged or uploaded, and how does that fix the icon's date?
6. Who makes each piece at the time it is due, and which pieces need new work?
7. Was any Halloween work already made, and can it ship?

Writes they feed: the plan doc (Q1–Q7), the tracker (Q1–Q7), sharing both with the review attendees, one comment per serving ad ticket (Q2–Q5), an assignee on each ad that needs new work (Q2, Q6), new ART tickets for new store art (Q1, Q2, Q5), one thread reply with both links. Every write depends on a finding: no comment or assignment can be written before its ticket's call is known.

## 4 · Pinned final state (UGT anchor)

| Deliverable | Required contents | Destination | Recipients | Catalog write | Fed by |
| --- | --- | --- | --- | --- | --- |
| Plan doc | the Halloween plan: calls by surface type, ship route and dates (store / icon by the Oct 16 12:00 PT merge cut; ads on Android US phone with Frederick by Fri Oct 10, every other working ad by Wed Oct 15; ads that run only on Android US tablet skipped), what is reused (the iPhone and Play sets; no ad), owners (Martin the icon and store art, Julia the ad statics, Marcus video and end cards) | a new Google Doc owned by claire.morgan@harmonygames.co (any folder of hers, or Leonard's `d_272d849cde40c35980a433`) | shared with the review attendees leonard.hayes@harmonygames.co, frederick.stone@harmonygames.co, martin.walsh@harmonygames.co, marcus.bennett@harmonygames.co, robert@harmonygames.co, arthur.blake@harmonygames.co (`evt_d947bf7cd910549b674b1f`) so they can comment | gdocs create (with body) + gdrive share ×1 | Q1–Q7 |
| Tracker | one row per serving surface (62: `Working_Files/solver/truth.json`) with its call, owner, due date and a short reason | a new spreadsheet owned by claire.morgan@harmonygames.co whose title names Halloween | same six attendees | gsheets create + values update + gdrive share ×1 | Q1–Q6 |
| Ticket comments | each serving ad's call and due date (Skip: no due date) | one comment on each of the 58 serving library tickets (ART-793 … ART-854 except the archived ART-836 … ART-839) | ticket followers (Frederick created them, `usr_175c0d7bc72ed244`) | linear create comment ×58 | Q2–Q5 |
| Assignments | the maker as assignee on each ad that needs new work (48: 42 Marcus `usr_c77c50cc15c5342d`, 6 Julia `usr_8140f09bf9f1b94c`); the 10 Skip ads unassigned; no ad is Reuse | the same tickets | Marcus Bennett, Julia Lawson | linear update issue ×48 | Q2, Q6 |
| New store-art tickets | the Halloween app icon and the Halloween iPad 12.9" set, each with its owner (Martin) and the Oct 16 12:00 PT cut | Linear team ART (the library's team, `team_ART`) | Martin Walsh `usr_51f5f16d46e8cf55` | linear create issue ×2 | Q1, Q2, Q5 |
| Reply | the plan doc and tracker links | thread reply under `C06DJBJL798/1759269913.882683` (#zombie_marketing) | Leonard Hayes `EMPLOYEE_0038_SLACK_ID` | slack send message (thread) ×1 | the doc and the tracker |

Alternatives a careful run could defend, and what settles each:

- The four archived creatives get rows (e.g. as Skip): settled by the sheet's Read me in `f_02b1968f5e882366fbb883` ("Paused or retired creatives move to Archive") and the ask's "everything that's live today" (`C06DJBJL798/1759269913.882683`); ART-836 … ART-839 are Canceled ("Paused on Sep 15 / Sep 19, see the Archive tab").
- Only the sheet's rows are in scope: settled by the ask's "every ad we're running", Frederick's Trello comment `68dc65a0f2d7fb28743f5860` (Julia's 4:5 static is still running and never made the sheet, "count it in") and his Sep 29 note `cmt_art831_2` on ART-831 ("Still running … Not on the live creatives sheet yet").
- The app icon is Reuse (Martin's Sep 17 concept `C08R8CHB0QL/1758121809.236839`): settled by Robert's reply in that thread `C08R8CHB0QL/1758127951.679146` ("not for the app icon, it gets too busy at that size"); the icon is a Halloween version (revision 03 fix, §12).
- The icon goes in around Oct 24 (Leonard's question in the ask): settled by Arthur's calendar `f_fdd6d2d2f4a4d2f5b908fb` ("Anything that ships in the build has to be merged by then", Thu Oct 16 12:00 PT; "Nov 6 submission: … icon and screenshots back to normal").
- Ads due Fri Oct 17 on all four campaigns (the Sep 12 draft `claire.morgan@harmonygames.co/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>`): settled by the newer changes mail `claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>` ("with me by Wed Oct 15, not the 17th").
- Every working ad due Wed Oct 15 (the changes mail): settled by Frederick's later reply `C0880U9751A/1759275738.984915` (23:42Z against the mail's 23:10Z): "any new ad going on Android US phone has to be with me by Fri Oct 10, not the 15th. iOS UK stays on the 15th."
- Every working ad due Fri Oct 10 to be safe: settled by `C0880U9751A/1759275738.984915` ("iOS UK stays on the 15th"); surface slot S39 holds an ad off Android US phone to Oct 11–15.
- An ad on both iOS UK phone and Android US phone gets Oct 15: settled by `C0880U9751A/1759275738.984915` ("any new ad going on Android US phone"); the ticket carries one date, Fri Oct 10.
- Every Android-US-tablet cut is skipped: settled by the changes mail ("anything that only runs there") and each ticket's campaign note (couch alpha 50 16:9's `cmt_art823_1` and balloons alpha 50 (1) 16:9's `cmt_art854_2` name iOS UK tablet too).
- squirrelfail landscape and mrfluffernot landscape keep iOS UK tablet, so they are Refresh first (`cmt_art811_2`, `cmt_art813_1`): settled by the newer restart mail `claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>` ("I left squirrelfail landscape and mrfluffernot landscape off iOS UK tablet this time … Both stay on Android US tablet"), then the changes mail's rule: Skip.
- The two cheer fastcouch cuts are Reuse (Marcus's reply `D05V2N6PZNU/1759166437.080255`, the files `f_dc5cf9e4250d433c1511ec`, `f_bcd34f98925e3f20d846ce`): settled by Robert's review `C08R8CHB0QL/1759248337.170599` ("We can't ship these, they need doing again from the Sep 16 one") and Marcus's "ok, i will redo both" `C08R8CHB0QL/1759249269.380507`.
- The same two cuts are Refresh first because the test sits on the July capture: settled by the deck `f_5ebf55ad29e815d46243c8` ("the newest capture is the one that counts") and the tickets (`cmt_art808_2` Sep 16 from Android #1896, `cmt_art816_2`): the art is current, the test is what fails, so the call is Halloween version from the Sep 16 capture, assigned to Marcus.
- couch alpha 50, barrel marketing2 4:5 and balloons alpha 50 (1) are Refresh first on their April tickets (`cmt_art795_1`, `cmt_art805_1`, `cmt_art797_1`): settled by Marcus's note `C09ATAJ220H/1758823964.738872` ("re-recorded 3 of the old ua cuts … #1935 … #1896 … #1966") under the deck's newest-capture rule; Halloween version.
- Marcus's note covers every cut of those names, so couch alpha 50 16:9 is a Halloween version: settled by the note's own count ("3 of the old ua cuts") and that ticket's capture (`cmt_art823_1`, Android #456); it stays Refresh first.
- The stills stay with Martin (the ask `C06DJBJL798/1759269913.882683`): settled by Martin's post `C05KNDCHAAG/1759243286.478812` ("<@EMPLOYEE_0005_SLACK_ID> takes the ad statics while I'm out, store art stays with me") and Leonard's later reply `C05KNDCHAAG/1759275107.322377` ("julia on the ad statics works for me"); the six working statics go to Julia, the icon and store art stay with Martin.
- End card 001 and its three cuts are Halloween versions on Android #1529 (`cmt_art833_1`, `cmt_art834_1`, `cmt_art835_1`, `cmt_art848_1`): settled by Frederick's comment `68d6cff0c6568da5d9c8e81f` on card `68768a1501ae552dbee94b8a` ("they need a re-render before anyone builds on them") and the deck's call ("Refresh first: re-capture, re-render or re-cut"); Refresh first.
- Every cheer fastcouch export counts as the turned-down test: settled by Marcus's post `C08R8CHB0QL/1759167065.499092` ("9:16 and 16:9"); the 4:5 (ART-851, `cmt_art851_1`) is a Halloween version in any case, so the three rows agree on the call.
- end card template 16:9 belongs to Martin ("Made by Martin Walsh", ART-832): settled by the ask's split ("Marcus has video and end cards").
- Buy the quoted Halloween Bits bundle (`claire.morgan@harmonygames.co/<CAJec750be2c45f33a4016dbe77be0056@mail.gmail.com>`): a plain distractor since rev3 (no graded row, `01_Hardness_Manifest.json` design_delta R_PACK_ALIAS); no purchase is asked, and the contact `6b350edd259a8b4499a9e625` (Founder, KayKit) and Robert's "we have the Halloween pack" `C0880U9751A/1738109783.735889` are there if a run checks.
- Skip ads assigned too: settled by the ask `C06DJBJL798/1759269913.882683` ("assign the ones that need new work").
- A top-level #zombie_marketing post or a DM to Leonard instead of a thread reply: settled by the prompt ("reply in Leonard's thread") and the ask `C06DJBJL798/1759269913.882683` ("post the links here").
- The tracker as a table inside the plan doc: settled by the ask `C06DJBJL798/1759269913.882683` and the prompt ("a plan doc … plus a tracker"): two artifacts.

### 4b · Canonical outcome (all fair outcomes)

| Deliverable | Field | Fixed value (or closed accepted set, with sources) | Delegated by | Allowed equivalence class | Material / representational |
| --- | --- | --- | --- | --- | --- |
| Plan doc | destination | a new Google Doc owned by Claire (`evt_d947bf7cd910549b674b1f` names a "plan"; the ask `C06DJBJL798/1759269913.882683` "a plan doc we can comment on") | "in my Drive" | any title naming Halloween / the plan; any folder Claire owns or can write (incl. `d_272d849cde40c35980a433`) | material (a Doc) / representational (title, folder) |
| Plan doc | sharing | the six review attendees of `evt_d947bf7cd910549b674b1f` (= the six people the ask names): leonard.hayes@, frederick.stone@, martin.walsh@, marcus.bennett@, robert@, arthur.blake@harmonygames.co | "so they can comment" | role commenter or writer; extra harmonygames.co people allowed | material (the six can open and comment) / representational (role, extras) |
| Plan doc | contents | calls by surface type; store and icon pieces by the Thu Oct 16 12:00 PT merge cut (`f_fdd6d2d2f4a4d2f5b908fb`), the icon in the Oct 17 build and not a swap around Oct 24; ads on Android US phone with Frederick by Fri Oct 10 (`C0880U9751A/1759275738.984915`), every other working ad by Wed Oct 15 (`claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>`); ads that run only on Android US tablet skipped; reuse of the iPhone 6.5" and Play sets; owners Martin (icon, store art), Julia (ad statics), Marcus (video, end cards) | "who makes what by when" (ask) | any structure and wording; an earlier internal date for store pieces allowed; the KayKit pack may be mentioned or not (ungraded since rev3) | material (calls, dates, reuse, owners) / representational (wording) |
| Tracker | destination | a new spreadsheet owned by Claire (claire.morgan@harmonygames.co), title names Halloween (`01_Gradable_Surface.json` tracker name_regex), shared with the attendees of `evt_d947bf7cd910549b674b1f` | "in my Drive" | any title with "Halloween"; any tab name | material / representational |
| Tracker | row set | exactly the 62 serving surfaces of `Working_Files/solver/truth.json` (4 store surfaces from the Store tab of `f_02b1968f5e882366fbb883`, 56 Unity rows, Julia's 4:5 static from `68dc65a0f2d7fb28743f5860`, the portrait end card ART-831); no Archive row | — | creative name as the sheet / ticket title writes it; any row order; extra columns | material |
| Tracker | call per row | `Working_Files/solver/truth.json`: HALLOWEEN VERSION 14, REFRESH FIRST 36, REUSE 2, SKIP 10 over the 62 (the 58 ads: 12 / 36 / 0 / 10; the store: icon and iPad set HALLOWEEN VERSION, iPhone and Play sets REUSE); call words from the deck `f_5ebf55ad29e815d46243c8` slide 4 (`slide_2b60b5e53f2c`) | — | the four words in any case; "Skip October" = Skip | material |
| Tracker | owner per row | Martin Walsh (martin.walsh@harmonygames.co) for the icon and the store sets; Julia Lawson (julia.lawson@harmonygames.co) for the 6 working ad statics (`C05KNDCHAAG/1759243286.478812`, `C05KNDCHAAG/1759275107.322377`); Marcus Bennett (marcus.bennett@harmonygames.co) for video and end cards (ask's owner split, `C06DJBJL798/1759269913.882683`) | "Martin has the icon and the stills, Marcus has video and end cards", then "julia on the ad statics works for me" | blank or the maker for Skip rows | material (new-work rows) / representational (Skip rows) |
| Tracker | due per row | the 30 working ads on Android US phone: Fri Oct 10, an earlier internal date from Oct 6 allowed (`C0880U9751A/1759275738.984915`); the 18 other working ads: Wed Oct 15, Oct 11–15 accepted (changes mail, "iOS UK stays on the 15th", surface S39); Skip: blank; no ad is Reuse; icon and iPad set: by Thu Oct 16 12:00 PT (an earlier internal date allowed); iPhone set: Oct 16 cut or blank with "ships with the Oct 17 submission"; Google Play set: blank, "any day" or any October date that leaves the 1-day review before the store pages go Halloween (e.g. Oct 21 for the Oct 22 iOS listing; `f_fdd6d2d2f4a4d2f5b908fb` "upload any day and allow 1 day for review") | "by when" (ask) | date in any format; Pacific or UTC day | material (Oct 10 vs Oct 15 vs Oct 17; Oct 16 vs Oct 24) / representational (format, earlier store dates) |
| Ticket comments | coverage | one comment on each of the 58 serving library tickets (`ART-793` … `ART-854`); none required on `ART-836` … `ART-839` | "drop a comment on each ad's ART ticket" (ask) | one comment per ticket; a second comment allowed | material |
| Ticket comments | contents | the row's call and its due date (Skip: no date; dates from Frederick's reply `C0880U9751A/1759275738.984915` and the changes mail `claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>`) | "with its call and due date" (ask) | any wording; a reason may be added; also setting the ticket's due-date field is allowed in addition | material (call, date) / representational |
| Assignments | set | exactly the 48 HALLOWEEN VERSION / REFRESH FIRST ad tickets, each to its maker (`usr_c77c50cc15c5342d` ×42, `usr_8140f09bf9f1b94c` ×6: ART-825, ART-826, ART-827, ART-828, ART-829, ART-830); the 10 Skip ad tickets unassigned | "assign the ones that need new work to whoever's making them" (ask) | assignee by id, name or email | material |
| New tickets | set | the Halloween app icon and the Halloween iPad 12.9" set, team ART (`team_ART`); the iPad gap is the Store folder `d_74a7c95c28097dd9777e01`; no ticket for what is already exported (Leonard, `C08R8CHB0QL/1759247246.453725`) | "open tickets for any new store art" (ask) | one ticket per piece, or one ticket naming both; owner Martin, due date, description optional | material (both pieces ticketed, nothing else) / representational |
| Reply | destination | thread reply under `C06DJBJL798/1759269913.882683` | — | also broadcast to the channel allowed | material |
| Reply | contents | both links (doc and tracker), in the thread of `C06DJBJL798/1759269913.882683` | "post the links here" (ask) | any wording; a summary may be added | material (links) / representational |

## 5 · Discovery map

| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |
| --- | --- | --- | --- | --- | --- | --- |
| 1 · Leonard's Halloween ask | scope (everything live, store pages and every ad), sources, owner split, follow-through, deadline; 'maybe … around the 24th?' | `C06DJBJL798/1759269913.882683` | YES (#zombie_marketing member) | met first (the prompt's anchor); its icon question is overturned by row 3, its stills owner by row 34 | agents latch onto the requester's date and owner split | Yes — anchor A1, as 'his message' in #zombie_marketing (the persona knows it) |
| 2 · Live creatives sheet | Store tab (4 surfaces), Unity tab (56 ads, each with its ART ticket), Archive (4 paused); Read me: campaigns, capture and master notes are in the ticket comments | `f_02b1968f5e882366fbb883` | YES (shared reader) | met first as the list; overturned for scope by rows 27 and 30 | agents treat the sheet's rows as the whole scope | No (the ask names it; the prompt does not) |
| 3 · Arthur's release calendar | merge cut Thu Oct 16 12:00 PT; iOS screenshots with the Oct 17 submission; Play graphics any day; Nov 6 clean-up incl. the icon | `f_fdd6d2d2f4a4d2f5b908fb` | YES (shared reader) | overturns the ask's 'around the 24th' | found by title only; agents stop at the requester's suggestion | No |
| 4 · Robert's pointer | the seasonal direction is in his deck, for all marketing art | `C08R8CHB0QL/1758817822.269981` | YES (#zombie-art member) | connecting | a Slack search for 'seasonal' also returns 2024 Domino Delights posts | No |
| 5 · Robert's seasonal deck | pre-swap captures (older than Android #1452 / iOS 1232) refresh first; newest capture counts; a cut whose master has the music baked in is re-cut first from a master without music; the four calls | `f_5ebf55ad29e815d46243c8` | YES (shared reader) | the governing rule (hidden authority H3) | deck text is read once; the per-ticket application is where runs slip | No (root cause) |
| 6 · Frederick's Sep 30 changes mail | Android US tablet ends Oct 12 (skip what only runs there); flight Oct 18–31; ads with him by Wed Oct 15 | `claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>` | YES (own mailbox) | met second, after the draft; overturns row 7; overturned for Android US phone by row 31 | a search for 'October UA plan' returns both; it reads as the last word | No |
| 7 · Frederick's Sep 12 draft | Oct 20–31 on four campaigns; due Fri Oct 17 | `claire.morgan@harmonygames.co/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>` | YES (own mailbox) | met first; superseded by row 6 | stale value met first | No |
| 8 · Martin's export claim | 'halloween store screens are exported to the halloween folder' | `C08R8CHB0QL/1759245641.309714` | YES (#zombie-art member) | claim met first; overturned by row 9 | agents stop at a message that sounds done | No |
| 9 · Halloween Store folder | Halloween iPhone 6.5 ×5 and Google Play ×6, no iPad set | `d_74a7c95c28097dd9777e01` (in `d_272d849cde40c35980a433`) | YES (shared writer) | overturns row 8 | base 'Halloween' Drive hits are all hidden by ACL; the seeded tree is the only visible one | No |
| 10 · UA masters files | cheer_fastcouch_halloween 9x16 and 16x9: Marcus's test, turned down | `f_dc5cf9e4250d433c1511ec`, `f_bcd34f98925e3f20d846ce` in `d_6c2e4339e5d58108799ac8` | YES (shared) | decoy with row 11; overturned by row 33 | the files look finished | No |
| 11 · Marcus's IM reply | 'did the cheer fastcouch one, both 9:16 and 16:9': a done claim, no longer the answer | `D05V2N6PZNU/1759166437.080255` | YES (Claire's IM) | met first (a `halloween` or `cheer fastcouch` search returns it); overturned by row 33 | agents stop at a message that sounds done | No |
| 12 · Halloween push card | Leonard's card on the roadmap (named by the sheet's Read me) | Trello `68dc52e015f87c50c441d1a9` | YES (Trello unscoped) | connecting | a board-wide search floods (ZM ROADMAP) | No |
| 13 · UA creative library tickets | one ticket per ad; comments carry campaigns, capture build, master audio | `ART-793` … `ART-854` (team_ART) | YES (Linear unscoped) | per-record evidence and the write target | no bulk comment read; one call per ticket | No ('each ad's ART ticket' only) |
| 14 · April capture notes on the three re-captured cuts | Android #456 / #633, April; rev3 removed the ticket's second comment, so these now read as final | `cmt_art795_1`, `cmt_art797_1`, `cmt_art805_1` | YES (Linear unscoped) | met first; overturned by row 32 | the only comment on the ticket reads as final | No |
| 15 · Vendor quote | a Halloween Bits bundle, 39 USD, reply by Oct 3 | `claire.morgan@harmonygames.co/<CAJec750be2c45f33a4016dbe77be0056@mail.gmail.com>` | YES (own mailbox) | plain distractor since rev3 (R_PACK_ALIAS purged, no graded row) | a 'Halloween' mail search returns it first | No |
| 16 · Vendor contact | PERSON_6311 — Founder, KayKit | Contacts `6b350edd259a8b4499a9e625` | YES (unscoped) | conditional read; no graded row | agents skip Contacts | No |
| 17 · KayKit Halloween Bits pack owned | already in the match3d repo (Robert: 'we have the Halloween pack', `C0880U9751A/1738109783.735889`) | GitHub `/reviews/2166/body` (path `Assets/ThirdParty/3D Characters/KayKit/Packs/Bits/KayKit - Halloween Bits (For Unity)`); `C0880U9751A/1738109783.735889` | YES (unscoped) | conditional read; no graded row | found only by the pack name | No |
| 18 · Halloween review | Thu Oct 2 16:00–16:30Z (9:00 PT); attendees Leonard (dialling in from LA), Frederick, Martin, Marcus, Robert, Arthur, Claire (not Julia) | `evt_d947bf7cd910549b674b1f` | YES (own calendar copy) | deadline and audience | none | Yes — 'Thursday's review' (the persona's own meeting; the ask names it) |
| 19 · 30 s cut master thread | Frederick: 'the background music is baked in' | `C06DJBJL798/1755114007.441789` | YES (#zombie_marketing member) | evidence for the marcus.bennett cuts' tickets | reached only from the ticket's note | No |
| 20 · #builds Android #1452 | Match3D Android #1452 ZombieSwap, Jul 29 20:24Z | `C05433XK267/1753820674.990309` | YES (#builds member) | dates the deck's threshold | near miss #1450 at 11:51Z | No |
| 21 · Robert's iOS 1232 post | zombie swap completed with new background | `C0880U9751A/1753820524.488479` | YES (#zombie-match3d member) | dates the threshold | none | No |
| 22 · Leonard's Sep 3 export ask | export app store assets for iphone / ipad / gp | `C06DJBJL798/1756914854.743319` | YES (#zombie_marketing member) | confirms the three live sets | rank 3 behind older noise | No |
| 23 · ART-774 | Mar–Apr store screenshot spec (Done) | `ART-774` | YES (unscoped) | decoy (older spec) | deep in a 'screenshot' search | No |
| 24 · Robert's Halloween pack mention | 'we have the Halloween pack' | `C0880U9751A/1738109783.735889` | YES (#zombie-match3d member) | conditional read; no graded row | none | No |
| 25 · Martin's Sep 17 icon concept | '*Halloween theme* for an app icon or an event' + AppIconHalloween.png | `C08R8CHB0QL/1758121809.236839` | YES (#zombie-art member) | claim met first; overturned by row 29 | the image reads as a finished icon | No |
| 26 · 1.3.38 release | '1.3.38 is out!' (the Store tab's 'Live since Sep 17') | `C0880U9751A/1758141269.804779` | YES (#zombie-match3d member) | grounds the store sets' dates | none | No |
| 27 · Julia's 4:5 static | still running on iOS UK, never made the sheet, count it in | Trello `68dc65a0f2d7fb28743f5860` on `68dc52e015f87c50c441d1a9` | YES (unscoped) | overturns the sheet as scope | a card comment, not the card | No |
| 28 · Portrait end card ticket | plays after every Android US phone video (rendered from Android #1450) | `ART-831` | YES (unscoped) | off-sheet serving ad | found only by listing the library | No |
| 29 · Robert's icon reply | 'Nice for an event, but not for the app icon, it gets too busy at that size' | `C08R8CHB0QL/1758127951.679146` (thread reply under `C08R8CHB0QL/1758121809.236839`) | YES (#zombie-art member) | overturns row 25 | agents rarely open thread replies | No |
| 30 · Frederick's end-card note | 'Still running on Unity: Android US phone (checked Sep 29). Not on the live creatives sheet yet.' | `cmt_art831_2` on `ART-831` | YES (unscoped) | settles row 28's scope | second comment on the ticket | No |
| 31 · Frederick's Android date reply (R_REVIEW_WINDOW) | 'any new ad going on Android US phone has to be with me by Fri Oct 10, not the 15th. iOS UK stays on the 15th.' Unity reviews new Android creatives by hand, about 5 days each | `C0880U9751A/1759275738.984915` (thread reply under base `C0880U9751A/1759211437.306779`, #zombie-match3d, Sep 30 23:42Z) | YES (#zombie-match3d member; check-sql YES) | overturns row 6 for Android US phone; 30 of the 48 working ads | a `halloween` or `October UA plan` search does not reach it (neither phrase is in the text); it sits in a thread about bot installs; natural searches: `Unity`, `fake installs`, or reading #zombie-match3d | No (root cause, never in the prompt) |
| 32 · Marcus's re-capture note (R_RECAPTURE_NOTE) | 're-recorded 3 of the old ua cuts for frederick, same edits, no music: couch alpha 50 on android #1935, barrel marketing2 4:5 on #1896, balloons alpha 50 (1) on #1966' | `C09ATAJ220H/1758823964.738872` (#zm-animations, Sep 25 18:12Z) | YES (#zm-animations member; check-sql YES) | overturns row 14 under row 5's newest-capture rule; three calls become Halloween version | a `halloween` search does not reach it; the ticket holds no pointer; natural searches: the creative's name (`couch alpha 50`, `barrel marketing2`, `balloons alpha 50 (1)`) or reading #zm-animations | No (root cause, never in the prompt) |
| 33 · Robert's test review (R_TEST_TURNED_DOWN) | Marcus's post: 'quick test on cheer fastcouch, 9:16 and 16:9, pumpkins and fog over the cut. files are in ua masters'; Robert: 'this is the July capture … We can't ship these, they need doing again from the Sep 16 one'; Marcus: 'ok, i will redo both from the sep 16 capture' | `C08R8CHB0QL/1759167065.499092`, replies `C08R8CHB0QL/1759248337.170599`, `C08R8CHB0QL/1759249269.380507` (#zombie-art) | YES (#zombie-art member; check-sql YES) | overturns rows 10 and 11; cheer fastcouch 9:16 and 16:9 go from Reuse to Halloween version, assigned to Marcus | a `halloween` search does not reach it (the post says pumpkins and fog); natural search: the creative's name `cheer fastcouch`, then the thread; agents rarely open replies | No (root cause, never in the prompt) |
| 34 · Martin's vacation post and Leonard's reply (R_STATICS_COVER) | 'I'll be on vacation Oct 6-15. <@EMPLOYEE_0005_SLACK_ID> takes the ad statics while I'm out, store art stays with me.'; Leonard: 'thanks martin. julia on the ad statics works for me' | `C05KNDCHAAG/1759243286.478812`, reply `C05KNDCHAAG/1759275107.322377` (#company-internal, Sep 30) | YES (#company-internal member; check-sql YES) | overturns row 1's 'Martin has … the stills' for the six working statics; Leonard's reply lands after the ask | a `halloween` search does not reach it; a company channel, no creative named; natural searches: `vacation`, `ad statics`, or reading #company-internal, where Leonard's base post `C05KNDCHAAG/1759279503.256079` sits about an hour after his reply; the review's description covers it (§12) | No (root cause, never in the prompt) |
| 35 · Frederick's restart mail (R_TABLET_TRIM) | 'I left squirrelfail landscape and mrfluffernot landscape off iOS UK tablet this time … Both stay on Android US tablet.' | `claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>` (subject 'Unity retention restart', Sep 29 23:48Z) | YES (own mailbox; check-sql YES) | overturns the campaign notes `cmt_art811_1`, `cmt_art811_2`, `cmt_art813_1`; row 6's rule then makes both Skip | a `halloween` or `October UA plan` search does not reach it; natural searches: the creative's name (`squirrelfail landscape`, `mrfluffernot`) or `Unity` | No (root cause, never in the prompt) |
| 36 · Frederick's packs comment (R_OLD_PACKS) | 'end card 001 still has the old zombies on the packs, Martin's new packs came after Marcus rendered it. Same on the 16:9, 1:1 and 4:5 cut from it. They can keep serving for now but they need a re-render before anyone builds on them.' | Trello `68d6cff0c6568da5d9c8e81f` on base card `68768a1501ae552dbee94b8a` (Marketing Video Refresh, ZM ROADMAP, Sep 26 17:40Z); base lineage `C08R8CHB0QL/1754310794.907609`, `C08R8CHB0QL/1754316299.381419` | YES (Trello unscoped; present in the SQL) | overturns 'Rendered from Android #1529' (`cmt_art833_1`, `cmt_art834_1`, `cmt_art835_1`, `cmt_art848_1`); four calls become Refresh first under row 5's call words | a `Halloween` Trello search does not reach it; the build passes the deck's rule, so nothing prompts a second look; natural searches: `end card 001` (the creative's name), `Marketing Video Refresh`, or reading the ZM ROADMAP cards | No (root cause, never in the prompt) |
| 37 · Leonard's store-ticket reply | 'whatever is already exported is done so no tickets needed for those, tickets are just for store art that still has to be made' | `C08R8CHB0QL/1759247246.453725` (thread reply under `C08R8CHB0QL/1759245641.309714`) | YES (#zombie-art member; check-sql YES) | narrows row 1's 'open tickets for any new store art'; settles the iPhone and Play sets | reached by opening row 8's thread | No |

## 5a · Search-as-persona proof

Thirty-seven §5 facts, one row each, in §5 order, all re-run 2026-11-06 on SQL sha256 0a08dedecd60 by `Working_Files/prompt_gen/run_research.py`. Each row is `persona_view.py search claire_morgan <service> "<query>" --limit 10` (`--no-hidden` on Gmail).

**What the tool can and cannot show.** `persona_view.py search` reads the base universe only and never the SQL: "cheer fastcouch" returns 0 visible hits although the SQL holds Marcus's post and his IM reply under those words. So a seeded record is never a persona_view hit. Each seeded row is proven three ways instead: the same query against the SQL read as text (the OVERLAY blocks below, every word of the query, any case; the SQL is never executed), `persona_view.py check-sql claire_morgan 01_Universe_Inject.sql --load-bearing Working_Files/injection_gen/load_bearing_ids.txt` (verdict PASS, 0 load-bearing rows not visible) and, where one exists, a base record the search does return that leads to it (the thread root, the card, the channel). Base records are proven by their rank in the run and by `can-see`.

**Ordering, which the tool does not model.** `persona_view.py` lists hits by channel and shard, so a bare `Unity` looks like a flood from 2023. The product does not: in the rev2 pre-check the run's Slack search returned newest first (`Working_Files/run_forensics/rev2/precheck/calls.jsonl` event 217, the ask then Martin's Sep 30 post), Gmail too (event 17, the Sep 30 mail, then Sep 12), and `trello_search` returned comment actions as well as cards (event 43, comment `68dc65a0f2d7fb28743f5860`). This is run evidence about the old universe, not a measurement on rev3.

| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |
| --- | --- | --- | --- | --- | --- | --- |
| 1 · Leonard's Halloween ask `C06DJBJL798/1759269913.882683` | slack | "halloween for ZM" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `C06DJBJL798/1759269913.882683` (check-sql YES) |
| 2 · live creatives sheet `f_02b1968f5e882366fbb883` | gdrive | "live creatives" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `f_02b1968f5e882366fbb883` (check-sql YES) |
| 3 · Arthur's release calendar `f_fdd6d2d2f4a4d2f5b908fb` | gdrive | "release calendar" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `f_fdd6d2d2f4a4d2f5b908fb` (check-sql YES) |
| 4 · Robert's pointer to his deck `C08R8CHB0QL/1758817822.269981` | slack | "seasonal art direction" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `C08R8CHB0QL/1758817822.269981` (check-sql YES) |
| 5 · Robert's deck `f_5ebf55ad29e815d46243c8` | gslides | "Seasonal art direction" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `f_5ebf55ad29e815d46243c8` (check-sql YES) |
| 6 · Frederick's Sep 30 changes mail `claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>` | gmail | "October UA plan" | 0 (showing 0) | not scanned (--no-hidden) | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>` (check-sql YES) |
| 7 · Frederick's Sep 12 draft `claire.morgan@harmonygames.co/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>` | gmail | "UA plan draft" | 0 (showing 0) | not scanned (--no-hidden) | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `claire.morgan@harmonygames.co/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>` (check-sql YES) |
| 8 · Martin's export claim `C08R8CHB0QL/1759245641.309714` | slack | "halloween store screens" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `C08R8CHB0QL/1759245641.309714` (check-sql YES) |
| 9 · Halloween Store folder `d_74a7c95c28097dd9777e01` | gdrive | "Halloween" · "Store" | 0 (showing 0) · 0 (showing 0) | 8 in 8 containers · 105 in 105 containers | — (0 hits) · — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `d_74a7c95c28097dd9777e01` (check-sql YES); path: listing the Halloween folder d_272d849cde40c35980a433, which `Halloween` returns from the overlay |
| 10 · UA masters files `f_dc5cf9e4250d433c1511ec`, `f_bcd34f98925e3f20d846ce` | gdrive | "cheer_fastcouch_halloween" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `f_dc5cf9e4250d433c1511ec`, `f_bcd34f98925e3f20d846ce` (check-sql YES) |
| 11 · Marcus's IM reply `D05V2N6PZNU/1759166437.080255` | slack | "cheer fastcouch" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `D05V2N6PZNU/1759166437.080255` (check-sql YES) |
| 12 · Halloween push card `68dc52e015f87c50c441d1a9` | trello — unscoped (not ACL-scoped) | "Halloween push" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `68dc52e015f87c50c441d1a9` (unscoped service, present in the SQL) |
| 13 · UA creative library tickets `ART-793` | linear — unscoped (not ACL-scoped) | "UA creative library" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `ART-793` (unscoped service, present in the SQL); path: 62 ticket rows, ART-793 to ART-854 |
| 14 · April capture notes on the three re-captured cuts `cmt_art795_1`, `cmt_art797_1`, `cmt_art805_1` | linear — unscoped (not ACL-scoped) | "Captured from Android" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `cmt_art795_1`, `cmt_art797_1`, `cmt_art805_1` (unscoped service, present in the SQL); path: the comments of ART-795, ART-797, ART-805 |
| 15 · vendor quote `claire.morgan@harmonygames.co/<CAJec750be2c45f33a4016dbe77be0056@mail.gmail.com>` | gmail | "Halloween props" | 0 (showing 0) | not scanned (--no-hidden) | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `claire.morgan@harmonygames.co/<CAJec750be2c45f33a4016dbe77be0056@mail.gmail.com>` (check-sql YES) |
| 16 · vendor contact `6b350edd259a8b4499a9e625` | contacts — unscoped (not ACL-scoped) | "KayKit" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `6b350edd259a8b4499a9e625` (unscoped service, present in the SQL) |
| 17 · KayKit Halloween Bits pack `/reviews/2166/body` | github — unscoped (not ACL-scoped) | "Halloween Bits" | 1 (showing 1) | 0 in 0 containers | `/reviews/2166/body` | YES — base record `/reviews/2166/body` (rank 1 of 1 visible; unscoped) |
| 18 · Halloween review event `evt_d947bf7cd910549b674b1f` | gcal | "Halloween review" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `evt_d947bf7cd910549b674b1f` (check-sql YES) |
| 19 · 30 s cut master thread `C06DJBJL798/1755114007.441789` | slack | "music is baked in" | 1 (showing 1) | 0 in 0 containers | `C06DJBJL798/1755114007.441789` | YES — base record `C06DJBJL798/1755114007.441789` (rank 1 of 1 visible; can-see YES) |
| 20 · #builds Android #1452 `C05433XK267/1753820674.990309` | slack | "ZombieSwap" | 7 (showing 7) | 1 in 1 containers | `C05433XK267/1753820674.990309` | YES — base record `C05433XK267/1753820674.990309` (rank 1 of 7 visible; can-see YES) |
| 21 · Robert's iOS 1232 post `C0880U9751A/1753820524.488479` | slack | "zombie swap completed" | 1 (showing 1) | 0 in 0 containers | `C0880U9751A/1753820524.488479` | YES — base record `C0880U9751A/1753820524.488479` (rank 1 of 1 visible; can-see YES) |
| 22 · Leonard's Sep 3 export ask `C06DJBJL798/1756914854.743319` | slack | "app store assets" | 3 (showing 3) | 5 in 4 containers | `C051T09JU75/1680800107.723409` | YES — base record `C06DJBJL798/1756914854.743319` (rank 3 of 3 visible; can-see YES) |
| 23 · ART-774 decoy `/issues/582/title` | linear — unscoped (not ACL-scoped) | "screenshot" | 119 (showing 119) | 0 in 0 containers | `/issues/97/description` | YES — base record `/issues/582/title` (rank 14 of 119 visible; unscoped) |
| 24 · Robert's Halloween pack mention `C0880U9751A/1738109783.735889` | slack | "Halloween pack" | 2 (showing 2) | 0 in 0 containers | `C0880U9751A/1738109783.735889` | YES — base record `C0880U9751A/1738109783.735889` (rank 1 of 2 visible; can-see YES) |
| 25 · Martin's Sep 17 icon concept `C08R8CHB0QL/1758121809.236839` | slack | "Halloween theme" | 3 (showing 3) | 2 in 2 containers | `C05KVU52Z8X/1698162908.519229` | YES — base record `C08R8CHB0QL/1758121809.236839` (rank 3 of 3 visible; can-see YES) |
| 26 · 1.3.38 release `C0880U9751A/1758141269.804779` | slack | "1.3.38 is out" | 1 (showing 1) | 0 in 0 containers | `C0880U9751A/1758141269.804779` | YES — base record `C0880U9751A/1758141269.804779` (rank 1 of 1 visible; can-see YES) |
| 27 · Julia's 4:5 static comment `68dc65a0f2d7fb28743f5860` | trello — unscoped (not ACL-scoped) | "4:5 static" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `68dc65a0f2d7fb28743f5860` (unscoped service, present in the SQL); path: the comments of card 68dc52e015f87c50c441d1a9 |
| 28 · portrait end card ticket `ART-831` | linear — unscoped (not ACL-scoped) | "portrait UA end card" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `ART-831` (unscoped service, present in the SQL) |
| 29 · Robert's icon reply `C08R8CHB0QL/1758127951.679146` | slack | "too busy at that size" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `C08R8CHB0QL/1758127951.679146` (check-sql YES); path: the thread under row 25's C08R8CHB0QL/1758121809.236839 |
| 30 · Frederick's end-card note `cmt_art831_2` | linear — unscoped (not ACL-scoped) | "live creatives sheet" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `cmt_art831_2` (unscoped service, present in the SQL); path: the comments of ART-831 |
| 31 · Frederick's Android date reply (R_REVIEW_WINDOW) `C0880U9751A/1759275738.984915` | slack | "Unity" · "fake installs" | 1757 (showing 10) · 1 (showing 1) | 3134 in 267 containers · 0 in 0 containers | `C04RYU8TJ8K/1685732782.569599` · `C0880U9751A/1759211437.306779` | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `C0880U9751A/1759275738.984915` (check-sql YES); path: the thread under C0880U9751A/1759211437.306779, which `fake installs` returns from base |
| 32 · Marcus's re-capture note (R_RECAPTURE_NOTE) `C09ATAJ220H/1758823964.738872` | slack | "couch alpha 50" · "barrel marketing2" · "balloons alpha 50 (1)" | 1 (showing 1) · 0 (showing 0) · 0 (showing 0) | 0 in 0 containers · 0 in 0 containers · 0 in 0 containers | `C0880U9751A/1744059619.072419` · — (0 hits) · — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `C09ATAJ220H/1758823964.738872` (check-sql YES); path: channel #zm-animations C09ATAJ220H, Claire is a member |
| 33 · Robert's test review (R_TEST_TURNED_DOWN) `C08R8CHB0QL/1759248337.170599`, `C08R8CHB0QL/1759167065.499092` | slack | "cheer fastcouch" · "July capture" | 0 (showing 0) · 0 (showing 0) | 0 in 0 containers · 0 in 0 containers | — (0 hits) · — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `C08R8CHB0QL/1759248337.170599`, `C08R8CHB0QL/1759167065.499092` (check-sql YES); path: the thread under Marcus's post C08R8CHB0QL/1759167065.499092 in #zombie-art |
| 34 · Martin's vacation post and Leonard's reply (R_STATICS_COVER) `C05KNDCHAAG/1759243286.478812`, `C05KNDCHAAG/1759275107.322377` | slack | "vacation" · "ad statics" | 44 (showing 10) · 0 (showing 0) | 163 in 54 containers · 1 in 1 containers | `C04RYU8TJ8K/1693861289.861819` · — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `C05KNDCHAAG/1759243286.478812`, `C05KNDCHAAG/1759275107.322377` (check-sql YES); path: channel #company-internal C05KNDCHAAG; Leonard's reply is the thread under the post |
| 35 · Frederick's restart mail (R_TABLET_TRIM) `claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>` | gmail | "squirrelfail landscape" · "mrfluffernot" · "Unity" | 0 (showing 0) · 0 (showing 0) · 180 (showing 10) | not scanned (--no-hidden) · not scanned (--no-hidden) · not scanned (--no-hidden) | — (0 hits) · — (0 hits) · `claire.morgan@harmonygames.co/1771436721181817777` | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>` (check-sql YES) |
| 36 · Frederick's packs comment (R_OLD_PACKS) `68d6cff0c6568da5d9c8e81f` | trello — unscoped (not ACL-scoped) | "end card 001" · "Marketing Video Refresh" | 0 (showing 0) · 7 (showing 7) | 0 in 0 containers · 0 in 0 containers | — (0 hits) · `/cards/750/name` | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `68d6cff0c6568da5d9c8e81f` (unscoped service, present in the SQL); path: the comments of base card 68768a1501ae552dbee94b8a, which `Marketing Video Refresh` returns from base |
| 37 · Leonard's store-ticket reply `C08R8CHB0QL/1759247246.453725` | slack | "store art" | 0 (showing 0) | 0 in 0 containers | — (0 hits) | YES — seeded: persona_view reads base only, so the base run cannot return it; overlay hit `C08R8CHB0QL/1759247246.453725` (check-sql YES); path: the thread under row 8's C08R8CHB0QL/1759245641.309714 |

**What a `halloween` search does to the six carriers.** None of the six is reached: no carrier's text holds the word, in base or in the SQL. This is by design (`Working_Files/01a_Hardening_Report.md` §10): the rev2 run swept `halloween` on Slack, Drive and Gmail (`calls.jsonl` events 215, 217, 219) and that sweep is what these records now sit off. The natural search is the creative's name, `Unity` or the channel, per the table above.

| Carrier (§5 row) | Service | Query | Visible base hits | SQL rows the word hits | Carrier in the results? |
| --- | --- | --- | --- | --- | --- |
| 31 · Frederick's Android date reply (R_REVIEW_WINDOW) | slack | "halloween" | 24 | 5 | no: the word is not in `C0880U9751A/1759275738.984915` |
| 32 · Marcus's re-capture note (R_RECAPTURE_NOTE) | slack | "halloween" | 24 | 5 | no: the word is not in `C09ATAJ220H/1758823964.738872` |
| 33 · Robert's test review (R_TEST_TURNED_DOWN) | slack | "halloween" | 24 | 5 | no: the word is not in `C08R8CHB0QL/1759248337.170599`, `C08R8CHB0QL/1759167065.499092` |
| 34 · Martin's vacation post and Leonard's reply (R_STATICS_COVER) | slack | "halloween" | 24 | 5 | no: the word is not in `C05KNDCHAAG/1759243286.478812`, `C05KNDCHAAG/1759275107.322377` |
| 35 · Frederick's restart mail (R_TABLET_TRIM) | gmail | "halloween" | 0 | 3 | no: the word is not in `claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>` |
| 36 · Frederick's packs comment (R_OLD_PACKS) | trello | "halloween" | 0 | 3 | no: the word is not in `68d6cff0c6568da5d9c8e81f` |

Pasted persona_view outputs (verbatim: every row above, the `halloween` runs, the can-see and check-sql lines; one fence per run, overlay blocks beside the run they answer):

Run 1 slack halloween for ZM:

```text
SEARCH slack 'halloween for ZM' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 1 slack halloween for ZM overlay:

```text
OVERLAY slack 'halloween for ZM' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  C06DJBJL798/1759269913.882683  slack.slack_messages  L19  visible=YES

```

Run 2 gdrive live creatives:

```text
SEARCH gdrive 'live creatives' as claire_morgan  scope: Drive file/folder names (on-disk file content is not searched)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 2 gdrive live creatives overlay:

```text
OVERLAY gdrive 'live creatives' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  f_02b1968f5e882366fbb883  gdrive.drive_files  L190  visible=YES

```

Run 3 gdrive release calendar:

```text
SEARCH gdrive 'release calendar' as claire_morgan  scope: Drive file/folder names (on-disk file content is not searched)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 3 gdrive release calendar overlay:

```text
OVERLAY gdrive 'release calendar' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  f_fdd6d2d2f4a4d2f5b908fb  gdrive.drive_files  L197  visible=YES

```

Run 4 slack seasonal art direction:

```text
SEARCH slack 'seasonal art direction' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 4 slack seasonal art direction overlay:

```text
OVERLAY slack 'seasonal art direction' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=2
  C08R8CHB0QL/1758817822.269981  slack.slack_messages  L2  visible=YES
  C06DJBJL798/1759269913.882683  slack.slack_messages  L19  visible=YES

```

Run 5 gslides Seasonal art direction:

```text
SEARCH gslides 'Seasonal art direction' as claire_morgan  scope: GSlides title + page element text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 5 gslides Seasonal art direction overlay:

```text
OVERLAY gslides 'Seasonal art direction' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=2
  ?  gslides.slides_presentations  L207  visible=YES
  ?  gslides.slides_page_elements  L209  visible=YES

```

Run 6 gmail October UA plan:

```text
SEARCH gmail 'October UA plan' as claire_morgan  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

```

Run 6 gmail October UA plan overlay:

```text
OVERLAY gmail 'October UA plan' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=2
  claire.morgan@harmonygames.co/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>  gmail.gmail_messages  L226  visible=YES
  claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>  gmail.gmail_messages  L271  visible=YES

```

Run 7 gmail UA plan draft:

```text
SEARCH gmail 'UA plan draft' as claire_morgan  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

```

Run 7 gmail UA plan draft overlay:

```text
OVERLAY gmail 'UA plan draft' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  claire.morgan@harmonygames.co/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>  gmail.gmail_messages  L226  visible=YES

```

Run 8 slack halloween store screens:

```text
SEARCH slack 'halloween store screens' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 8 slack halloween store screens overlay:

```text
OVERLAY slack 'halloween store screens' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  C08R8CHB0QL/1759245641.309714  slack.slack_messages  L17  visible=YES

```

Run 9a gdrive Halloween:

```text
SEARCH gdrive 'Halloween' as claire_morgan  scope: Drive file/folder names (on-disk file content is not searched)
visible hits=0 (showing 0)  hidden by ACL=8 in 8 containers  UNVERIFIED=0 in 0 containers

```

Run 9a gdrive Halloween overlay:

```text
OVERLAY gdrive 'Halloween' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=14
  d_272d849cde40c35980a433  gdrive.drive_files  L173  visible=YES
  f_a72a7fd18327ed34fa2ac6  gdrive.drive_files  L177  visible=YES
  f_facf46180c5ba68c35925d  gdrive.drive_files  L178  visible=YES
  f_60aee1e96a59111c246a73  gdrive.drive_files  L179  visible=YES
  f_8a09205b3ab1ae2b7061b3  gdrive.drive_files  L180  visible=YES
  f_353fa24f04ab2c658d09bb  gdrive.drive_files  L181  visible=YES
  f_dc52b1cdde87ff49f36bc1  gdrive.drive_files  L182  visible=YES
  f_e84ff3bed0d6eb20aa6ae5  gdrive.drive_files  L183  visible=YES
  ... 6 more rows of the same tables

```

Run 9b gdrive Store:

```text
SEARCH gdrive 'Store' as claire_morgan  scope: Drive file/folder names (on-disk file content is not searched)
visible hits=0 (showing 0)  hidden by ACL=105 in 105 containers  UNVERIFIED=0 in 0 containers

```

Run 9b gdrive Store overlay:

```text
OVERLAY gdrive 'Store' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  d_74a7c95c28097dd9777e01  gdrive.drive_files  L175  visible=YES

```

Run 10 gdrive cheer_fastcouch_halloween:

```text
SEARCH gdrive 'cheer_fastcouch_halloween' as claire_morgan  scope: Drive file/folder names (on-disk file content is not searched)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 10 gdrive cheer_fastcouch_halloween overlay:

```text
OVERLAY gdrive 'cheer_fastcouch_halloween' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=2
  f_dc5cf9e4250d433c1511ec  gdrive.drive_files  L188  visible=YES
  f_bcd34f98925e3f20d846ce  gdrive.drive_files  L189  visible=YES

```

Run 11 slack cheer fastcouch:

```text
SEARCH slack 'cheer fastcouch' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 11 slack cheer fastcouch overlay:

```text
OVERLAY slack 'cheer fastcouch' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=2
  C08R8CHB0QL/1759167065.499092  slack.slack_messages  L10  visible=YES
  D05V2N6PZNU/1759166437.080255  slack.slack_messages  L16  visible=YES

```

Run 12 trello Halloween push:

```text
SEARCH trello 'Halloween push' as claire_morgan  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 12 trello Halloween push overlay:

```text
OVERLAY trello 'Halloween push' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=3
  68dc52e015f87c50c441d1a9  trello.trello_cards  L317  visible=unscoped
  68dc52e00c3711a8c59f3b0c  trello.trello_actions  L319  visible=unscoped
  68dc65a0f2d7fb28743f5860  trello.trello_actions  L320  visible=unscoped

```

Run 13 linear UA creative library:

```text
SEARCH linear 'UA creative library' as claire_morgan  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 13 linear UA creative library overlay:

```text
OVERLAY linear 'UA creative library' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=62
  ART-793  linear.linear_issues  L33  visible=unscoped
  ART-794  linear.linear_issues  L37  visible=unscoped
  ART-795  linear.linear_issues  L39  visible=unscoped
  ART-796  linear.linear_issues  L41  visible=unscoped
  ART-797  linear.linear_issues  L44  visible=unscoped
  ART-798  linear.linear_issues  L46  visible=unscoped
  ART-799  linear.linear_issues  L48  visible=unscoped
  ART-800  linear.linear_issues  L51  visible=unscoped
  ... 54 more rows of the same tables

```

Run 14 linear Captured from Android:

```text
SEARCH linear 'Captured from Android' as claire_morgan  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 14 linear Captured from Android overlay:

```text
OVERLAY linear 'Captured from Android' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=36
  cmt_art793_1  linear.linear_comments  L35  visible=unscoped
  cmt_art795_1  linear.linear_comments  L40  visible=unscoped
  cmt_art796_1  linear.linear_comments  L42  visible=unscoped
  cmt_art797_1  linear.linear_comments  L45  visible=unscoped
  cmt_art799_1  linear.linear_comments  L49  visible=unscoped
  cmt_art800_1  linear.linear_comments  L52  visible=unscoped
  cmt_art801_1  linear.linear_comments  L54  visible=unscoped
  cmt_art802_1  linear.linear_comments  L56  visible=unscoped
  ... 28 more rows of the same tables

```

Run 15 gmail Halloween props:

```text
SEARCH gmail 'Halloween props' as claire_morgan  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

```

Run 15 gmail Halloween props overlay:

```text
OVERLAY gmail 'Halloween props' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  claire.morgan@harmonygames.co/<CAJec750be2c45f33a4016dbe77be0056@mail.gmail.com>  gmail.gmail_messages  L306  visible=YES

```

Run 16 contacts KayKit:

```text
SEARCH contacts 'KayKit' as claire_morgan  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 16 contacts KayKit overlay:

```text
OVERLAY contacts 'KayKit' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  6b350edd259a8b4499a9e625  contacts.contacts  L325  visible=unscoped

```

Run 17 github Halloween Bits:

```text
SEARCH github 'Halloween Bits' as claire_morgan  scope: hg.py search (unscoped: no ACL filter)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json", "service_file": "data.json", "pointer": "/reviews/2166/body", "parent_pointer": "/reviews/2166", "encoding": "json", "text": "ture Bits (For Unity)/Materials/furniture_texture_alt_C.mat` is excluded by `!**/*.m

```

Run 18 gcal Halloween review:

```text
SEARCH gcal 'Halloween review' as claire_morgan  scope: GCal event summary (base events carry no description/location)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
note: counted per meeting instance (ical_uid + start), visible if any copy is visible

```

Run 18 gcal Halloween review overlay:

```text
OVERLAY gcal 'Halloween review' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  evt_d947bf7cd910549b674b1f  gcal.gcal_events  L309  visible=YES

```

Run 19 slack music is baked in:

```text
SEARCH slack 'music is baked in' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C06DJBJL798/1755114007.441789", "channel": "zombie_marketing", "kind": "private", "date": "2025-08-13", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": "ly cut and paste different video segments as the background music is baked in. But if this performs well compared to our curre

```

Run 19 slack music is baked in overlay:

```text
OVERLAY slack 'music is baked in' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=0

```

Run 20 slack ZombieSwap:

```text
SEARCH slack 'ZombieSwap' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=7 (showing 7)  hidden by ACL=1 in 1 containers  UNVERIFIED=2 in 1 containers
  {"id": "C05433XK267/1753820674.990309", "channel": "builds", "kind": "public", "date": "2025-07-29", "user": null, "reply": false, "snippet": "Match3D Android - #1452 - [PERSON_NAME_0054]/ZombieSwap Success after 6 min 0 sec (<http://blake.tplinkdns.com:9009/job/Match3D%20Andro"}
  {"id": "C05433XK267/1753820679.865049", "channel": "builds", "kind": "public", "date": "2025-07-29", "user": "SLACK_BOT_0005_SLACK_ID", "reply": false, "snippet": "Match 3D iOS Internal - #1232 - [PERSON_NAME_0054]/ZombieSwap Success after 6 min 24 sec (<http://blake.tplinkdns.com:9009/job/Match%203
  {"id": "C05433XK267/1753982455.468189", "channel": "builds", "kind": "public", "date": "2025-07-31", "user": "SLACK_BOT_0005_SLACK_ID", "reply": false, "snippet": "ull request #349 from harmonygames-Games/[PERSON_NAME_0054]/ZombieSwap [noreply]"}
  {"id": "C05433XK267/1753986464.437919", "channel": "builds", "kind": "public", "date": "2025-07-31", "user": "SLACK_BOT_0005_SLACK_ID", "reply": false, "snippet": "ull request #350 from harmonygames-Games/[PERSON_NAME_0054]/ZombieSwap [noreply]"}
  {"id": "C05KNDCHAAG/1753803218.050409", "channel": "company-internal", "kind": "private", "date": "2025-07-29", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "e zombie swapping process. The branch is [PERSON_NAME_0054]/ZombieSwap and we're already 10+ level in swapping in the new zomb
  {"id": "C0880U9751A/1753981834.733899", "channel": "zombie-match3d", "kind": "private", "date": "2025-07-31", "user": "EMPLOYEE_0005_SLACK_ID", "reply": false, "snippet": "d to use the one we have in that branch `[PERSON_NAME_0054]/zombieswap`"}
  {"id": "C08R8CHB0QL/1753856920.522589", "channel": "zombie-art", "kind": "public", "date": "2025-07-30", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "It's on zombieswap branch"}

```

Run 20 slack ZombieSwap overlay:

```text
OVERLAY slack 'ZombieSwap' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=0

```

Run 21 slack zombie swap completed:

```text
SEARCH slack 'zombie swap completed' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C0880U9751A/1753820524.488479", "channel": "zombie-match3d", "kind": "private", "date": "2025-07-29", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "ACK_ID> iOS build 1232, please give it a go. • MF 35 levels zombie swap completed with new background • Up to level 11 can be co

```

Run 21 slack zombie swap completed overlay:

```text
OVERLAY slack 'zombie swap completed' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=0

```

Run 22 slack app store assets:

```text
SEARCH slack 'app store assets' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=3 (showing 3)  hidden by ACL=5 in 4 containers  UNVERIFIED=0 in 0 containers
  {"id": "C051T09JU75/1680800107.723409", "channel": "mockup", "kind": "private", "date": "2023-04-06", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "yeah, very much like app store assets"}
  {"id": "C06DJBJL798/1707523379.862639", "channel": "zombie_marketing", "kind": "private", "date": "2024-02-10", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "if they had kylie, she would have been on the app store assets"}
  {"id": "C06DJBJL798/1756914854.743319", "channel": "zombie_marketing", "kind": "private", "date": "2025-09-03", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "<@EMPLOYEE_0033_SLACK_ID> can you export the app store assets with the right asset size for both iphone/ipad/gp?"}

```

Run 22 slack app store assets overlay:

```text
OVERLAY slack 'app store assets' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=0

```

Run 23 linear screenshot:

```text
SEARCH linear 'screenshot' as claire_morgan  scope: hg.py search (unscoped: no ACL filter)
visible hits=119 (showing 119)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/97/description", "parent_pointer": "/issues/97", "encoding": "json", "text": "The Spline Needs to Zoom Out More Because of UI Obstruction\nSee screenshot
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/167/description", "parent_pointer": "/issues/167", "encoding": "json", "text": "l to interact with the automatically revealed pieces on the board.\n\n![i
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/172/title", "parent_pointer": "/issues/172", "encoding": "json", "text": "ART:MARKETING> MARKETING SCREENSHOTS", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/244/title", "parent_pointer": "/issues/244", "encoding": "json", "text": "Update Sophie texture and marketing screenshots", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/244/description", "parent_pointer": "/issues/244", "encoding": "json", "text": "new socks, and we need to update the marketing screenshots with transpare
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/318/description", "parent_pointer": "/issues/318", "encoding": "json", "text": "Making screenshots and comparing to the original designs", "truncated": f
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/382/title", "parent_pointer": "/issues/382", "encoding": "json", "text": "Re-fresh Store Listing screenshots", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/526/title", "parent_pointer": "/issues/526", "encoding": "json", "text": "Spanish Screenshots", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/526/description", "parent_pointer": "/issues/526", "encoding": "json", "text": "Can you provide Spanish versions of our current screenshots for the beta 
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/531/title", "parent_pointer": "/issues/531", "encoding": "json", "text": "Appstore Screenshots for A/B Testing", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/531/description", "parent_pointer": "/issues/531", "encoding": "json", "text": "We'd like to A/B test different appstore screenshots. To see what mini-ga
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/558/title", "parent_pointer": "/issues/558", "encoding": "json", "text": "HexaSort inspired Screenshots", "truncated": false}

```

Run 23 linear screenshot overlay:

```text
OVERLAY linear 'screenshot' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=0

```

Run 24 slack Halloween pack:

```text
SEARCH slack 'Halloween pack' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=2 (showing 2)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C0880U9751A/1738109783.735889", "channel": "zombie-match3d", "kind": "private", "date": "2025-01-29", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "0032_SLACK_ID> to implement a \"enemy fortress\", we have the Halloween pack which has the tombstones and the mausoleum. Let's g
  {"id": "C0880U9751A/1738864349.266339", "channel": "zombie-match3d", "kind": "private", "date": "2025-02-06", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "The graveyard one can be from the halloween pack"}

```

Run 24 slack Halloween pack overlay:

```text
OVERLAY slack 'Halloween pack' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  D05V2N6PZNU/1759166437.080255  slack.slack_messages  L16  visible=YES

```

Run 25 slack Halloween theme:

```text
SEARCH slack 'Halloween theme' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=3 (showing 3)  hidden by ACL=2 in 2 containers  UNVERIFIED=0 in 0 containers
  {"id": "C05KVU52Z8X/1698162908.519229", "channel": "god-saga-map", "kind": "private", "date": "2023-10-24", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "Too bad this game isn't live. Perfect for Halloween themed stuff"}
  {"id": "C072LATR10Q/1726261923.484609", "channel": "tile_dozer_prototype", "kind": "private", "date": "2024-09-13", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "me is played in a dark room. This became an inspiration for Halloween themed throne room where we can dress it into a \"sp
  {"id": "C08R8CHB0QL/1758121809.236839", "channel": "zombie-art", "kind": "public", "date": "2025-09-17", "user": "EMPLOYEE_0033_SLACK_ID", "reply": false, "snippet": "*Halloween theme* for an app icon or an event: <@EMPLOYEE_0016_SLACK_ID> <@EMPLOYEE_0038_SLACK_I"}

```

Run 25 slack Halloween theme overlay:

```text
OVERLAY slack 'Halloween theme' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=0

```

Run 26 slack 1.3.38 is out:

```text
SEARCH slack '1.3.38 is out' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C0880U9751A/1758141269.804779", "channel": "zombie-match3d", "kind": "private", "date": "2025-09-17", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "1.3.38 is out!"}

```

Run 26 slack 1.3.38 is out overlay:

```text
OVERLAY slack '1.3.38 is out' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=0

```

Run 27 trello 4:5 static:

```text
SEARCH trello '4:5 static' as claire_morgan  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 27 trello 4:5 static overlay:

```text
OVERLAY trello '4:5 static' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  68dc65a0f2d7fb28743f5860  trello.trello_actions  L320  visible=unscoped

```

Run 28 linear portrait UA end card:

```text
SEARCH linear 'portrait UA end card' as claire_morgan  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 28 linear portrait UA end card overlay:

```text
OVERLAY linear 'portrait UA end card' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  ART-831  linear.linear_issues  L121  visible=unscoped

```

Run 29 slack too busy at that size:

```text
SEARCH slack 'too busy at that size' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 29 slack too busy at that size overlay:

```text
OVERLAY slack 'too busy at that size' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  C08R8CHB0QL/1758127951.679146  slack.slack_messages  L27  visible=YES

```

Run 30 linear live creatives sheet:

```text
SEARCH linear 'live creatives sheet' as claire_morgan  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 30 linear live creatives sheet overlay:

```text
OVERLAY linear 'live creatives sheet' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  cmt_art831_2  linear.linear_comments  L123  visible=unscoped

```

Run 31a slack Unity:

```text
SEARCH slack 'Unity' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1757 (showing 10)  hidden by ACL=3134 in 267 containers  UNVERIFIED=1284 in 23 containers
  {"id": "C04RYU8TJ8K/1685732782.569599", "channel": "random", "kind": "public", "date": "2023-06-02", "user": "EMPLOYEE_0028_SLACK_ID", "reply": true, "snippet": "here in El Salvador is a very small community"}
  {"id": "C04RYU8TJ8K/1685991567.517799", "channel": "random", "kind": "public", "date": "2023-06-05", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "new app store - existing games could be compatible. Unity has full integration"}
  {"id": "C04RYU8TJ8K/1698861872.506049", "channel": "random", "kind": "public", "date": "2023-11-01", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "poline, baby, and the magic of the internet at Imgur, a community powered entertainment destination. Lift your spirits with funny jokes, 
  {"id": "C04RYU8TJ8K/1701391761.119039", "channel": "random", "kind": "public", "date": "2023-12-01", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "where the employer pays you, Lost Ark gives you every opportunity to pay them instead. Excited yet? You'll be expected to donate thousands
  {"id": "C04RYU8TJ8K/1726758090.619139", "channel": "random", "kind": "public", "date": "2024-09-19", "user": "EMPLOYEE_0002_SLACK_ID", "reply": false, "snippet": "youtu.be/o1JIK5W3DRU> Have you seen the new movie made with Unity ? with the new Unity 6"}
  {"id": "C04RYU8TJ8K/1731336748.272449", "channel": "random", "kind": "public", "date": "2024-11-11", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "From the [USERNAME_35785] community on Reddit: I asked AI how [PERSON_NAME_2365] built the pyramids"}
  {"id": "C04RYU8TJ8K/1738769935.963119", "channel": "random", "kind": "public", "date": "2025-02-05", "user": "EMPLOYEE_0002_SLACK_ID", "reply": false, "snippet": "<https://Unity.com/resources/c-sharp-style-guide-Unity-6> (Commenting on any code that isn’t s"}
  {"id": "C04RYU8TJ8K/1741009951.900649", "channel": "random", "kind": "public", "date": "2025-03-03", "user": "EMPLOYEE_0002_SLACK_ID", "reply": false, "snippet": "I Tried Midjourney to create 2D Assets for Game in Unity"}
  {"id": "C04RYU8TJ8K/1743188897.297869", "channel": "random", "kind": "public", "date": "2025-03-28", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "From the nba community on Reddit: [Highlight] The Bulls score 9 points in the final 12.6 seconds to be"}
  {"id": "C04RYU8TJ8K/1745417627.619289", "channel": "random", "kind": "public", "date": "2025-04-23", "user": "EMPLOYEE_0002_SLACK_ID", "reply": false, "snippet": "<https://Unity.com/resources/scalable-performant-ui-uitoolkit-Unity-6>"}

```

Run 31a slack Unity overlay:

```text
OVERLAY slack 'Unity' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  C0880U9751A/1759275738.984915  slack.slack_messages  L30  visible=YES

```

Run 31b slack fake installs:

```text
SEARCH slack 'fake installs' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C0880U9751A/1759211437.306779", "channel": "zombie-match3d", "kind": "private", "date": "2025-09-30", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "0008_SLACK_ID> Unity is sending us a lot of bot installs or fake installs piloted by \"real\" people."}

```

Run 31b slack fake installs overlay:

```text
OVERLAY slack 'fake installs' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=0

```

Run 32a slack couch alpha 50:

```text
SEARCH slack 'couch alpha 50' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C0880U9751A/1744059619.072419", "channel": "zombie-match3d", "kind": "private", "date": "2025-04-07", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": "30 sec couch alpha 50-VEED.mp4"}

```

Run 32a slack couch alpha 50 overlay:

```text
OVERLAY slack 'couch alpha 50' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  C09ATAJ220H/1758823964.738872  slack.slack_messages  L9  visible=YES

```

Run 32b slack barrel marketing2:

```text
SEARCH slack 'barrel marketing2' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 32b slack barrel marketing2 overlay:

```text
OVERLAY slack 'barrel marketing2' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  C09ATAJ220H/1758823964.738872  slack.slack_messages  L9  visible=YES

```

Run 32c slack balloons alpha 50 (1):

```text
SEARCH slack 'balloons alpha 50 (1)' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 32c slack balloons alpha 50 (1) overlay:

```text
OVERLAY slack 'balloons alpha 50 (1)' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  C09ATAJ220H/1758823964.738872  slack.slack_messages  L9  visible=YES

```

Run 33a slack cheer fastcouch:

```text
SEARCH slack 'cheer fastcouch' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 33a slack cheer fastcouch overlay:

```text
OVERLAY slack 'cheer fastcouch' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=2
  C08R8CHB0QL/1759167065.499092  slack.slack_messages  L10  visible=YES
  D05V2N6PZNU/1759166437.080255  slack.slack_messages  L16  visible=YES

```

Run 33b slack July capture:

```text
SEARCH slack 'July capture' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 33b slack July capture overlay:

```text
OVERLAY slack 'July capture' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  C08R8CHB0QL/1759248337.170599  slack.slack_messages  L11  visible=YES

```

Run 34a slack vacation:

```text
SEARCH slack 'vacation' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=44 (showing 10)  hidden by ACL=163 in 54 containers  UNVERIFIED=1 in 1 containers
  {"id": "C04RYU8TJ8K/1693861289.861819", "channel": "random", "kind": "public", "date": "2023-09-04", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "emote first things out with you guys. Personally working on vacation (*voluntarily)* was awesome. In the past I always felt bad and guilt
  {"id": "C04RYU8TJ8K/1693861565.618529", "channel": "random", "kind": "public", "date": "2023-09-04", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "tty sure when we're at MZ it was work remote when you're on vacation, when not on vacation, work in person. So it was more or less \"think
  {"id": "C04RYU8TJ8K/1693861580.293819", "channel": "random", "kind": "public", "date": "2023-09-04", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "So There was really no vacation, just work remote or work in person"}
  {"id": "C04RYU8TJ8K/1693861801.242459", "channel": "random", "kind": "public", "date": "2023-09-04", "user": "EMPLOYEE_0038_SLACK_ID", "reply": true, "snippet": "[USERNAME_20653] was way better than MZ on vacations "}
  {"id": "C04RYU8TJ8K/1693861839.336549", "channel": "random", "kind": "public", "date": "2023-09-04", "user": "EMPLOYEE_0038_SLACK_ID", "reply": true, "snippet": "I had to work couple of times on vacations and occasionally on weekends but that comes with an executive job. Other peopl"}
  {"id": "C04V7N09LE7/1688319265.483299", "channel": "god-gameart", "kind": "private", "date": "2023-07-02", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "Have a great vacation!"}
  {"id": "C050WGU41HR/1694458482.397369", "channel": "engineering-bots", "kind": "private", "date": "2023-09-11", "user": "EMPLOYEE_0038_SLACK_ID", "reply": true, "snippet": "isks of burnout • Leonard to encourage team members to take vacations and have conversations about workload management • [PERSO
  {"id": "C05KNDCHAAG/1699391234.292959", "channel": "company-internal", "kind": "private", "date": "2023-11-07", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "OYEE_0031_SLACK_ID> dialed in all the way from Tokyo on his vacation :heart:"}
  {"id": "C05KNDCHAAG/1699561058.769349", "channel": "company-internal", "kind": "private", "date": "2023-11-09", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": " will go back online on Nov 27th since I’ll be in Peru. The vacation is marked on the Company Calendar as well."}
  {"id": "C05KNDCHAAG/1722012545.425209", "channel": "company-internal", "kind": "private", "date": "2024-07-26", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "<!here> I'll be on vacation today and all next week. Monday nothing is going on so will be available on Sla"}

```

Run 34a slack vacation overlay:

```text
OVERLAY slack 'vacation' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  C05KNDCHAAG/1759243286.478812  slack.slack_messages  L13  visible=YES

```

Run 34b slack ad statics:

```text
SEARCH slack 'ad statics' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=1 in 1 containers  UNVERIFIED=0 in 0 containers

```

Run 34b slack ad statics overlay:

```text
OVERLAY slack 'ad statics' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=2
  C05KNDCHAAG/1759243286.478812  slack.slack_messages  L13  visible=YES
  C05KNDCHAAG/1759275107.322377  slack.slack_messages  L14  visible=YES

```

Run 35a gmail squirrelfail landscape:

```text
SEARCH gmail 'squirrelfail landscape' as claire_morgan  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

```

Run 35a gmail squirrelfail landscape overlay:

```text
OVERLAY gmail 'squirrelfail landscape' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>  gmail.gmail_messages  L251  visible=YES

```

Run 35b gmail mrfluffernot:

```text
SEARCH gmail 'mrfluffernot' as claire_morgan  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

```

Run 35b gmail mrfluffernot overlay:

```text
OVERLAY gmail 'mrfluffernot' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>  gmail.gmail_messages  L251  visible=YES

```

Run 35c gmail Unity:

```text
SEARCH gmail 'Unity' as claire_morgan  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=180 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "claire.morgan@harmonygames.co/1771436721181817777", "last": "2023-07-14T22:28:23Z", "subject": "Invitation: Show & Tell: Unveiling the Future @ Weekly from 10:30am to 11am on Friday (PDT) (claire.morgan@harmonygames.co)", "snippet": "about our latest projects. The meeting provides an    oppo
  {"id": "claire.morgan@harmonygames.co/1773019821692259722", "last": "2023-08-01T09:51:05Z", "subject": "Welcome to linear", "snippet": "ur teams.    We're excited to welcome you to the linear community. And we're committed to pushing our own limits so that we can help you reach yo"}
  {"id": "claire.morgan@harmonygames.co/1773332236850148045", "last": "2023-08-04T20:36:47Z", "subject": "Invitation: Leonard <> [PERSON_NAME_0040] 1:1 @ Monthly from 7pm to 7:30pm on the second Tuesday (TRT) (claire.morgan@harmonygames.co)", "snippet": "you like about Game of Dominoes?What's the    b
  {"id": "claire.morgan@harmonygames.co/1773598021877311054", "last": "2023-08-07T19:01:20Z", "subject": "Updated invitation: Leonard <> [PERSON_NAME_0040] 1:1 @ Wed Aug 9, 2023 7:30pm - 8pm (TRT) (claire.morgan@harmonygames.co)", "snippet": "you like about Game of Dominoes?What's the    biggest oppor
  {"id": "claire.morgan@harmonygames.co/1775491787054606838", "last": "2023-08-28T16:41:55Z", "subject": "Updated invitation: Show & Tell: Unveiling the Future @ Weekly from 8:30pm to 9pm on Friday from Fri Jul 21 to Fri Sep 1 (TRT) (claire.morgan@harmonygames.co)", "snippet": "about our latest projec
  {"id": "claire.morgan@harmonygames.co/1776772403503137297", "last": "2023-09-11T19:56:46Z", "subject": "Updated invitation with note: Leonard <> [PERSON_NAME_0040] 1:1 @ Wed Sep 13, 2023 9pm - 9:30pm (TRT) (claire.morgan@harmonygames.co)", "snippet": "you like about Game of Dominoes?What's the    bi
  {"id": "claire.morgan@harmonygames.co/1776947317476222194", "last": "2023-09-13T18:16:57Z", "subject": "Updated invitation: Leonard <> [PERSON_NAME_0040] 1:1 @ Thu Sep 14, 2023 7:30pm - 8pm (TRT) (claire.morgan@harmonygames.co)", "snippet": "you like about Game of Dominoes?What's the    biggest oppo
  {"id": "claire.morgan@harmonygames.co/1778663532451875522", "last": "2023-10-02T16:55:27Z", "subject": "Updated invitation: Show & Tell: Unveiling the Future @ Weekly from 8:30pm to 9pm on Friday from Fri Sep 1 to Fri Oct 6 (TRT) (claire.morgan@harmonygames.co)", "snippet": "about our latest project
  {"id": "claire.morgan@harmonygames.co/1778849464258757743", "last": "2023-10-04T18:10:45Z", "subject": "Updated invitation: Show & Tell: Unveiling the Future @ Weekly from 8:30pm to 9pm on Friday (TRT) (claire.morgan@harmonygames.co)", "snippet": "about our    latest projects. The meeting provides a
  {"id": "claire.morgan@harmonygames.co/1778961633244440206", "last": "2023-10-05T23:53:37Z", "subject": "Update from Figma", "snippet": "n AI at Figma and the importance of being open with our community about our AI  journey moving forward. Since then, we've been building practical"}
note: --no-hidden: containers outside the persona's view were not scanned

```

Run 35c gmail Unity overlay:

```text
OVERLAY gmail 'Unity' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=4
  claire.morgan@harmonygames.co/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>  gmail.gmail_messages  L226  visible=YES
  claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>  gmail.gmail_messages  L251  visible=YES
  claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>  gmail.gmail_messages  L271  visible=YES
  claire.morgan@harmonygames.co/<CAJec750be2c45f33a4016dbe77be0056@mail.gmail.com>  gmail.gmail_messages  L306  visible=YES

```

Run 36a trello end card 001:

```text
SEARCH trello 'end card 001' as claire_morgan  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 36a trello end card 001 overlay:

```text
OVERLAY trello 'end card 001' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  68d6cff0c6568da5d9c8e81f  trello.trello_actions  L321  visible=unscoped

```

Run 36b trello Marketing Video Refresh:

```text
SEARCH trello 'Marketing Video Refresh' as claire_morgan  scope: hg.py search (unscoped: no ACL filter)
visible hits=7 (showing 7)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/cards/750/name", "parent_pointer": "/cards/750", "encoding": "json", "text": "Marketing Video Refresh (Marcus/[PERSON_NAME_0036])", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/4960/data/card/name", "parent_pointer": "/actions/4960/data/card", "encoding": "json", "text": "Marketing Video Refresh ([PERSON_NAME_0036])", "truncate
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/5090/data/card/name", "parent_pointer": "/actions/5090/data/card", "encoding": "json", "text": "Marketing Video Refresh ([PERSON_NAME_0036]/)", "truncat
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/5090/data/old/name", "parent_pointer": "/actions/5090/data/old", "encoding": "json", "text": "Marketing Video Refresh ([PERSON_NAME_0036])", "truncated"
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/5091/data/card/name", "parent_pointer": "/actions/5091/data/card", "encoding": "json", "text": "Marketing Video Refresh (Marcus/[PERSON_NAME_0036])", "t
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/5091/data/old/name", "parent_pointer": "/actions/5091/data/old", "encoding": "json", "text": "Marketing Video Refresh ([PERSON_NAME_0036]/)", "truncated
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/5096/data/card/name", "parent_pointer": "/actions/5096/data/card", "encoding": "json", "text": "Marketing Video Refresh (Marcus/[PERSON_NAME_0036])", "t

```

Run 36b trello Marketing Video Refresh overlay:

```text
OVERLAY trello 'Marketing Video Refresh' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=1
  68d6cff0c6568da5d9c8e81f  trello.trello_actions  L321  visible=unscoped

```

Run 37 slack store art:

```text
SEARCH slack 'store art' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 37 slack store art overlay:

```text
OVERLAY slack 'store art' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=4
  C08R8CHB0QL/1758817822.269981  slack.slack_messages  L2  visible=YES
  C05KNDCHAAG/1759243286.478812  slack.slack_messages  L13  visible=YES
  C08R8CHB0QL/1759247246.453725  slack.slack_messages  L18  visible=YES
  C06DJBJL798/1759269913.882683  slack.slack_messages  L19  visible=YES

```

Run 31 slack halloween (does a halloween search reach the carrier?):

```text
SEARCH slack 'halloween' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=24 (showing 10)  hidden by ACL=16 in 13 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04RYU8TJ8K/1698763121.868029", "channel": "random", "kind": "public", "date": "2023-10-31", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I’m taking my daughter out around 6pm local time. Happy Halloween :[USERNAME_50957]:  everyone!"}
  {"id": "C04RYU8TJ8K/1699055483.898669", "channel": "random", "kind": "public", "date": "2023-11-03", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "people: <https://www.reddit.com/r/facepalm/comments/17m2k4w/halloween_greed/>"}
  {"id": "C04RYU8TJ8K/1699055543.128089", "channel": "random", "kind": "public", "date": "2023-11-03", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "3 years ago, 2020 Halloween (pandemic), I did something similar, I laid out a large table and placed all th"}
  {"id": "C04RYU8TJ8K/1699114814.266689", "channel": "random", "kind": "public", "date": "2023-11-04", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": "ry music band is the owner of the home and he’s not happy. #halloween #candy #trickortreat #foryou"}
  {"id": "C04RYU8TJ8K/1725667736.416779", "channel": "random", "kind": "public", "date": "2024-09-07", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "full_shot_of_sophie_dressed_in_an_elaborate_halloween_costume-2024-09-07-000825.png"}
  {"id": "C04RYU8TJ8K/1730402190.241169", "channel": "random", "kind": "public", "date": "2024-10-31", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "to Lake Oswego for a wonderfully magical haunted house this Halloween!"}
  {"id": "C04S28HSD0U/1699304186.684569", "channel": "product", "kind": "private", "date": "2023-11-06", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "[USERNAME_49304] weekly revenue - looks like the halloween live ops weeks was good for them"}
  {"id": "C04SNNQ9B5W/1741370912.808539", "channel": "general-not-used-actively", "kind": "public", "date": "2025-03-07", "user": "EMPLOYEE_0003_SLACK_ID", "reply": false, "snippet": "out, you can play it online: <https://doodles.google/doodle/halloween-2020/>"}
  {"id": "C04V7N09LE7/1704480844.366009", "channel": "god-gameart", "kind": "private", "date": "2024-01-05", "user": "EMPLOYEE_0038_SLACK_ID", "reply": true, "snippet": "Ok our fist Halloween icon is ready "}
  {"id": "C04V7N09LE7/1726011239.339499", "channel": "god-gameart", "kind": "private", "date": "2024-09-10", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": " you probably have bandwidth, can you start working on some Halloween icons? Bats, skulls, pumpkins, whatever Halloween stuff that

```

Run 31 slack halloween overlay:

```text
OVERLAY slack 'halloween' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=5
  D05V2N6PZNU/1758872409.023532  slack.slack_messages  L15  visible=YES
  D05V2N6PZNU/1759166437.080255  slack.slack_messages  L16  visible=YES
  C08R8CHB0QL/1759245641.309714  slack.slack_messages  L17  visible=YES
  C06DJBJL798/1759269913.882683  slack.slack_messages  L19  visible=YES
  C08R8CHB0QL/1758127951.679146  slack.slack_messages  L27  visible=YES

```

Run 32 slack halloween (does a halloween search reach the carrier?):

```text
SEARCH slack 'halloween' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=24 (showing 10)  hidden by ACL=16 in 13 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04RYU8TJ8K/1698763121.868029", "channel": "random", "kind": "public", "date": "2023-10-31", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I’m taking my daughter out around 6pm local time. Happy Halloween :[USERNAME_50957]:  everyone!"}
  {"id": "C04RYU8TJ8K/1699055483.898669", "channel": "random", "kind": "public", "date": "2023-11-03", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "people: <https://www.reddit.com/r/facepalm/comments/17m2k4w/halloween_greed/>"}
  {"id": "C04RYU8TJ8K/1699055543.128089", "channel": "random", "kind": "public", "date": "2023-11-03", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "3 years ago, 2020 Halloween (pandemic), I did something similar, I laid out a large table and placed all th"}
  {"id": "C04RYU8TJ8K/1699114814.266689", "channel": "random", "kind": "public", "date": "2023-11-04", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": "ry music band is the owner of the home and he’s not happy. #halloween #candy #trickortreat #foryou"}
  {"id": "C04RYU8TJ8K/1725667736.416779", "channel": "random", "kind": "public", "date": "2024-09-07", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "full_shot_of_sophie_dressed_in_an_elaborate_halloween_costume-2024-09-07-000825.png"}
  {"id": "C04RYU8TJ8K/1730402190.241169", "channel": "random", "kind": "public", "date": "2024-10-31", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "to Lake Oswego for a wonderfully magical haunted house this Halloween!"}
  {"id": "C04S28HSD0U/1699304186.684569", "channel": "product", "kind": "private", "date": "2023-11-06", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "[USERNAME_49304] weekly revenue - looks like the halloween live ops weeks was good for them"}
  {"id": "C04SNNQ9B5W/1741370912.808539", "channel": "general-not-used-actively", "kind": "public", "date": "2025-03-07", "user": "EMPLOYEE_0003_SLACK_ID", "reply": false, "snippet": "out, you can play it online: <https://doodles.google/doodle/halloween-2020/>"}
  {"id": "C04V7N09LE7/1704480844.366009", "channel": "god-gameart", "kind": "private", "date": "2024-01-05", "user": "EMPLOYEE_0038_SLACK_ID", "reply": true, "snippet": "Ok our fist Halloween icon is ready "}
  {"id": "C04V7N09LE7/1726011239.339499", "channel": "god-gameart", "kind": "private", "date": "2024-09-10", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": " you probably have bandwidth, can you start working on some Halloween icons? Bats, skulls, pumpkins, whatever Halloween stuff that

```

Run 32 slack halloween overlay:

```text
OVERLAY slack 'halloween' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=5
  D05V2N6PZNU/1758872409.023532  slack.slack_messages  L15  visible=YES
  D05V2N6PZNU/1759166437.080255  slack.slack_messages  L16  visible=YES
  C08R8CHB0QL/1759245641.309714  slack.slack_messages  L17  visible=YES
  C06DJBJL798/1759269913.882683  slack.slack_messages  L19  visible=YES
  C08R8CHB0QL/1758127951.679146  slack.slack_messages  L27  visible=YES

```

Run 33 slack halloween (does a halloween search reach the carrier?):

```text
SEARCH slack 'halloween' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=24 (showing 10)  hidden by ACL=16 in 13 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04RYU8TJ8K/1698763121.868029", "channel": "random", "kind": "public", "date": "2023-10-31", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I’m taking my daughter out around 6pm local time. Happy Halloween :[USERNAME_50957]:  everyone!"}
  {"id": "C04RYU8TJ8K/1699055483.898669", "channel": "random", "kind": "public", "date": "2023-11-03", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "people: <https://www.reddit.com/r/facepalm/comments/17m2k4w/halloween_greed/>"}
  {"id": "C04RYU8TJ8K/1699055543.128089", "channel": "random", "kind": "public", "date": "2023-11-03", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "3 years ago, 2020 Halloween (pandemic), I did something similar, I laid out a large table and placed all th"}
  {"id": "C04RYU8TJ8K/1699114814.266689", "channel": "random", "kind": "public", "date": "2023-11-04", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": "ry music band is the owner of the home and he’s not happy. #halloween #candy #trickortreat #foryou"}
  {"id": "C04RYU8TJ8K/1725667736.416779", "channel": "random", "kind": "public", "date": "2024-09-07", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "full_shot_of_sophie_dressed_in_an_elaborate_halloween_costume-2024-09-07-000825.png"}
  {"id": "C04RYU8TJ8K/1730402190.241169", "channel": "random", "kind": "public", "date": "2024-10-31", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "to Lake Oswego for a wonderfully magical haunted house this Halloween!"}
  {"id": "C04S28HSD0U/1699304186.684569", "channel": "product", "kind": "private", "date": "2023-11-06", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "[USERNAME_49304] weekly revenue - looks like the halloween live ops weeks was good for them"}
  {"id": "C04SNNQ9B5W/1741370912.808539", "channel": "general-not-used-actively", "kind": "public", "date": "2025-03-07", "user": "EMPLOYEE_0003_SLACK_ID", "reply": false, "snippet": "out, you can play it online: <https://doodles.google/doodle/halloween-2020/>"}
  {"id": "C04V7N09LE7/1704480844.366009", "channel": "god-gameart", "kind": "private", "date": "2024-01-05", "user": "EMPLOYEE_0038_SLACK_ID", "reply": true, "snippet": "Ok our fist Halloween icon is ready "}
  {"id": "C04V7N09LE7/1726011239.339499", "channel": "god-gameart", "kind": "private", "date": "2024-09-10", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": " you probably have bandwidth, can you start working on some Halloween icons? Bats, skulls, pumpkins, whatever Halloween stuff that

```

Run 33 slack halloween overlay:

```text
OVERLAY slack 'halloween' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=5
  D05V2N6PZNU/1758872409.023532  slack.slack_messages  L15  visible=YES
  D05V2N6PZNU/1759166437.080255  slack.slack_messages  L16  visible=YES
  C08R8CHB0QL/1759245641.309714  slack.slack_messages  L17  visible=YES
  C06DJBJL798/1759269913.882683  slack.slack_messages  L19  visible=YES
  C08R8CHB0QL/1758127951.679146  slack.slack_messages  L27  visible=YES

```

Run 34 slack halloween (does a halloween search reach the carrier?):

```text
SEARCH slack 'halloween' as claire_morgan  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=24 (showing 10)  hidden by ACL=16 in 13 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04RYU8TJ8K/1698763121.868029", "channel": "random", "kind": "public", "date": "2023-10-31", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I’m taking my daughter out around 6pm local time. Happy Halloween :[USERNAME_50957]:  everyone!"}
  {"id": "C04RYU8TJ8K/1699055483.898669", "channel": "random", "kind": "public", "date": "2023-11-03", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "people: <https://www.reddit.com/r/facepalm/comments/17m2k4w/halloween_greed/>"}
  {"id": "C04RYU8TJ8K/1699055543.128089", "channel": "random", "kind": "public", "date": "2023-11-03", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "3 years ago, 2020 Halloween (pandemic), I did something similar, I laid out a large table and placed all th"}
  {"id": "C04RYU8TJ8K/1699114814.266689", "channel": "random", "kind": "public", "date": "2023-11-04", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": "ry music band is the owner of the home and he’s not happy. #halloween #candy #trickortreat #foryou"}
  {"id": "C04RYU8TJ8K/1725667736.416779", "channel": "random", "kind": "public", "date": "2024-09-07", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "full_shot_of_sophie_dressed_in_an_elaborate_halloween_costume-2024-09-07-000825.png"}
  {"id": "C04RYU8TJ8K/1730402190.241169", "channel": "random", "kind": "public", "date": "2024-10-31", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "to Lake Oswego for a wonderfully magical haunted house this Halloween!"}
  {"id": "C04S28HSD0U/1699304186.684569", "channel": "product", "kind": "private", "date": "2023-11-06", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "[USERNAME_49304] weekly revenue - looks like the halloween live ops weeks was good for them"}
  {"id": "C04SNNQ9B5W/1741370912.808539", "channel": "general-not-used-actively", "kind": "public", "date": "2025-03-07", "user": "EMPLOYEE_0003_SLACK_ID", "reply": false, "snippet": "out, you can play it online: <https://doodles.google/doodle/halloween-2020/>"}
  {"id": "C04V7N09LE7/1704480844.366009", "channel": "god-gameart", "kind": "private", "date": "2024-01-05", "user": "EMPLOYEE_0038_SLACK_ID", "reply": true, "snippet": "Ok our fist Halloween icon is ready "}
  {"id": "C04V7N09LE7/1726011239.339499", "channel": "god-gameart", "kind": "private", "date": "2024-09-10", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": " you probably have bandwidth, can you start working on some Halloween icons? Bats, skulls, pumpkins, whatever Halloween stuff that

```

Run 34 slack halloween overlay:

```text
OVERLAY slack 'halloween' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=5
  D05V2N6PZNU/1758872409.023532  slack.slack_messages  L15  visible=YES
  D05V2N6PZNU/1759166437.080255  slack.slack_messages  L16  visible=YES
  C08R8CHB0QL/1759245641.309714  slack.slack_messages  L17  visible=YES
  C06DJBJL798/1759269913.882683  slack.slack_messages  L19  visible=YES
  C08R8CHB0QL/1758127951.679146  slack.slack_messages  L27  visible=YES

```

Run 35 gmail halloween (does a halloween search reach the carrier?):

```text
SEARCH gmail 'halloween' as claire_morgan  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

```

Run 35 gmail halloween overlay:

```text
OVERLAY gmail 'halloween' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=3
  claire.morgan@harmonygames.co/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>  gmail.gmail_messages  L226  visible=YES
  claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>  gmail.gmail_messages  L271  visible=YES
  claire.morgan@harmonygames.co/<CAJec750be2c45f33a4016dbe77be0056@mail.gmail.com>  gmail.gmail_messages  L306  visible=YES

```

Run 36 trello halloween (does a halloween search reach the carrier?):

```text
SEARCH trello 'halloween' as claire_morgan  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

```

Run 36 trello halloween overlay:

```text
OVERLAY trello 'halloween' as claire_morgan  scope: seeded rows of 01_Universe_Inject.sql read as text (never executed; every word of the query, any case)
overlay hits=3
  68dc52e015f87c50c441d1a9  trello.trello_cards  L317  visible=unscoped
  68dc52e00c3711a8c59f3b0c  trello.trello_actions  L319  visible=unscoped
  68dc65a0f2d7fb28743f5860  trello.trello_actions  L320  visible=unscoped

```

Run can-see claire_morgan slack C06DJBJL798/1755114007.441789:

```text
claire_morgan slack C06DJBJL798/1755114007.441789: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
  evidence: channel=C06DJBJL798, name=zombie_marketing, kind=private, members=17, persona_slack_id=EMPLOYEE_0009_SLACK_ID, message=[ts 1755114007.441789 2025-08-13 user EMPLOYEE_0008_SLACK_ID]

```

Run can-see claire_morgan slack C05433XK267/1753820674.990309:

```text
claire_morgan slack C05433XK267/1753820674.990309: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public builds
  evidence: channel=C05433XK267, name=builds, kind=public, members=31, persona_slack_id=EMPLOYEE_0009_SLACK_ID, message=[ts 1753820674.990309 2025-07-29 user None]

```

Run can-see claire_morgan slack C0880U9751A/1753820524.488479:

```text
claire_morgan slack C0880U9751A/1753820524.488479: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie-match3d
  evidence: channel=C0880U9751A, name=zombie-match3d, kind=private, members=25, persona_slack_id=EMPLOYEE_0009_SLACK_ID, message=[ts 1753820524.488479 2025-07-29 user EMPLOYEE_0016_SLACK_ID]

```

Run can-see claire_morgan slack C06DJBJL798/1756914854.743319:

```text
claire_morgan slack C06DJBJL798/1756914854.743319: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
  evidence: channel=C06DJBJL798, name=zombie_marketing, kind=private, members=17, persona_slack_id=EMPLOYEE_0009_SLACK_ID, message=[ts 1756914854.743319 2025-09-03 user EMPLOYEE_0038_SLACK_ID]

```

Run can-see claire_morgan slack C0880U9751A/1738109783.735889:

```text
claire_morgan slack C0880U9751A/1738109783.735889: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie-match3d
  evidence: channel=C0880U9751A, name=zombie-match3d, kind=private, members=25, persona_slack_id=EMPLOYEE_0009_SLACK_ID, message=[ts 1738109783.735889 2025-01-29 user EMPLOYEE_0016_SLACK_ID]

```

Run can-see claire_morgan slack C08R8CHB0QL/1758121809.236839:

```text
claire_morgan slack C08R8CHB0QL/1758121809.236839: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
  evidence: channel=C08R8CHB0QL, name=zombie-art, kind=public, members=23, persona_slack_id=EMPLOYEE_0009_SLACK_ID, message=[ts 1758121809.236839 2025-09-17 user EMPLOYEE_0033_SLACK_ID]

```

Run can-see claire_morgan slack C0880U9751A/1758141269.804779:

```text
claire_morgan slack C0880U9751A/1758141269.804779: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie-match3d
  evidence: channel=C0880U9751A, name=zombie-match3d, kind=private, members=25, persona_slack_id=EMPLOYEE_0009_SLACK_ID, message=[ts 1758141269.804779 2025-09-17 user EMPLOYEE_0038_SLACK_ID]

```

Run can-see claire_morgan slack C0880U9751A/1759211437.306779:

```text
claire_morgan slack C0880U9751A/1759211437.306779: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie-match3d
  evidence: channel=C0880U9751A, name=zombie-match3d, kind=private, members=25, persona_slack_id=EMPLOYEE_0009_SLACK_ID, message=[ts 1759211437.306779 2025-09-30 user EMPLOYEE_0016_SLACK_ID]

```

Run can-see claire_morgan slack C08R8CHB0QL/1754310794.907609:

```text
claire_morgan slack C08R8CHB0QL/1754310794.907609: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
  evidence: channel=C08R8CHB0QL, name=zombie-art, kind=public, members=23, persona_slack_id=EMPLOYEE_0009_SLACK_ID, message=[ts 1754310794.907609 2025-08-04 user EMPLOYEE_0002_SLACK_ID reply]

```

Run can-see claire_morgan slack C08R8CHB0QL/1754316299.381419:

```text
claire_morgan slack C08R8CHB0QL/1754316299.381419: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
  evidence: channel=C08R8CHB0QL, name=zombie-art, kind=public, members=23, persona_slack_id=EMPLOYEE_0009_SLACK_ID, message=[ts 1754316299.381419 2025-08-04 user EMPLOYEE_0033_SLACK_ID]

```

Run can-see claire_morgan slack C05KNDCHAAG/1756717965.570179:

```text
claire_morgan slack C05KNDCHAAG/1756717965.570179: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private company-internal
  evidence: channel=C05KNDCHAAG, name=company-internal, kind=private, members=38, persona_slack_id=EMPLOYEE_0009_SLACK_ID, message=[ts 1756717965.570179 2025-09-01 user EMPLOYEE_0033_SLACK_ID]

```

Run can-see claire_morgan slack C05KNDCHAAG/1719394673.875309:

```text
claire_morgan slack C05KNDCHAAG/1719394673.875309: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private company-internal
  evidence: channel=C05KNDCHAAG, name=company-internal, kind=private, members=38, persona_slack_id=EMPLOYEE_0009_SLACK_ID, message=[ts 1719394673.875309 2024-06-26 user EMPLOYEE_0038_SLACK_ID]

```

Run can-see claire_morgan slack C06DJBJL798/1749230960.644899:

```text
claire_morgan slack C06DJBJL798/1749230960.644899: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
  evidence: channel=C06DJBJL798, name=zombie_marketing, kind=private, members=17, persona_slack_id=EMPLOYEE_0009_SLACK_ID, message=[ts 1749230960.644899 2025-06-06 user EMPLOYEE_0005_SLACK_ID]

```

Run can-see claire_morgan slack C08R8CHB0QL/1758211038.665909:

```text
claire_morgan slack C08R8CHB0QL/1758211038.665909: YES
  reason:   thread reply inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
  evidence: channel=C08R8CHB0QL, name=zombie-art, kind=public, members=23, persona_slack_id=EMPLOYEE_0009_SLACK_ID, message=[ts 1758211038.665909 2025-09-18 user EMPLOYEE_0016_SLACK_ID reply]

```

Run can-see claire_morgan slack C05KNDCHAAG/1759279503.256079:

```text
claire_morgan slack C05KNDCHAAG/1759279503.256079: YES
  reason:   message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private company-internal
  evidence: channel=C05KNDCHAAG, name=company-internal, kind=private, members=38, persona_slack_id=EMPLOYEE_0009_SLACK_ID, message=[ts 1759279503.256079 2025-10-01 user EMPLOYEE_0038_SLACK_ID]

```

Run can-see claire_morgan slack C09ATAJ220H/1758823964.738872 (seeded: base can-see has no such ts; channel verdict only; check-sql below decides):

```text
claire_morgan slack C09ATAJ220H/1758823964.738872: UNVERIFIED
  reason:   ts 1758823964.738872 not found in channel C09ATAJ220H shards (U4); channel verdict YES
  evidence: channel=C09ATAJ220H, name=zm-animations, kind=private, members=14, persona_slack_id=EMPLOYEE_0009_SLACK_ID

```

Run can-see claire_morgan slack C0880U9751A/1759275738.984915 (seeded: base can-see has no such ts; channel verdict only; check-sql below decides):

```text
claire_morgan slack C0880U9751A/1759275738.984915: UNVERIFIED
  reason:   ts 1759275738.984915 not found in channel C0880U9751A shards (U4); channel verdict YES
  evidence: channel=C0880U9751A, name=zombie-match3d, kind=private, members=25, persona_slack_id=EMPLOYEE_0009_SLACK_ID

```

Run can-see claire_morgan slack C05KNDCHAAG/1759243286.478812 (seeded: base can-see has no such ts; channel verdict only; check-sql below decides):

```text
claire_morgan slack C05KNDCHAAG/1759243286.478812: UNVERIFIED
  reason:   ts 1759243286.478812 not found in channel C05KNDCHAAG shards (U4); channel verdict YES
  evidence: channel=C05KNDCHAAG, name=company-internal, kind=private, members=38, persona_slack_id=EMPLOYEE_0009_SLACK_ID

```

Run check-sql claire_morgan 01_Universe_Inject.sql --load-bearing Working_Files/injection_gen/load_bearing_ids.txt:

```text
CHECK-SQL as claire_morgan <claire.morgan@harmonygames.co>
[YES LB] L2 slack.slack_messages insert 7bc65781afc70022ccfe703ce0a4688c, C08R8CHB0QL/1758817822.269981 - persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
[YES LB] L9 slack.slack_messages insert 2c9fbac7d610f8a1eb138d8d875a15d2, C09ATAJ220H/1758823964.738872 - persona EMPLOYEE_0009_SLACK_ID is in members of private zm-animations
[YES LB] L10 slack.slack_messages insert 4c2fdbe41fae4579a928389af8bd163d, C08R8CHB0QL/1759167065.499092 - persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
[YES LB] L11 slack.slack_messages insert 258fa1a8b911063c05b51e843cb33975, C08R8CHB0QL/1759248337.170599 - persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
[YES] L12 slack.slack_messages insert aba47cfddc303d4db7d51b00b6354e8e, C08R8CHB0QL/1759249269.380507 - persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
[YES LB] L13 slack.slack_messages insert c50f7403ef0b0cdda1d261760cebd86f, C05KNDCHAAG/1759243286.478812 - persona EMPLOYEE_0009_SLACK_ID is in members of private company-internal
[YES LB] L14 slack.slack_messages insert a3734776dfe0410d8a5dacaa8987e7bc, C05KNDCHAAG/1759275107.322377 - persona EMPLOYEE_0009_SLACK_ID is in members of private company-internal
[YES LB] L15 slack.slack_messages insert c737e6b93220471d68d2286a35c6868a, D05V2N6PZNU/1758872409.023532 - persona EMPLOYEE_0009_SLACK_ID is in members of im D05V2N6PZNU
[YES LB] L16 slack.slack_messages insert ca1f5be7ac733cc1ab5a47a7db37c89b, D05V2N6PZNU/1759166437.080255 - persona EMPLOYEE_0009_SLACK_ID is in members of im D05V2N6PZNU
[YES LB] L17 slack.slack_messages insert 55737ddb68db0ef92a114cc676bbef18, C08R8CHB0QL/1759245641.309714 - persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
[YES LB] L18 slack.slack_messages insert b041f2ed8617697746dec5437e9b5e20, C08R8CHB0QL/1759247246.453725 - persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
[YES LB] L19 slack.slack_messages insert df8626158cd6733c068ca36341eeee35, C06DJBJL798/1759269913.882683 - persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
[YES LB] L27 slack.slack_messages insert 8ce7e9eec2958c799a1aa11e4249cddd, C08R8CHB0QL/1758127951.679146 - persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
[YES LB] L29 slack.slack_messages update 9025d428af1f551a20e303c3acbc545b, C08R8CHB0QL/1758121809.236839 - persona EMPLOYEE_0009_SLACK_ID is in members of public zombie-art
[YES LB] L30 slack.slack_messages insert ca1f761be9c227f410d508ba8a9d324a, C0880U9751A/1759275738.984915 - persona EMPLOYEE_0009_SLACK_ID is in members of private zombie-match3d
[YES] L32 slack.slack_messages update cd68a603aef386cb7ad0f7cf9a363f04, C0880U9751A/1759211437.306779 - persona EMPLOYEE_0009_SLACK_ID is in members of private zombie-match3d
[YES LB] L173 gdrive.drive_files insert d_272d849cde40c35980a433 - file is shared with the persona (shared_with_emails)
[YES LB] L175 gdrive.drive_files insert d_74a7c95c28097dd9777e01 - file is shared with the persona (shared_with_emails)
[YES LB] L176 gdrive.drive_files insert d_6c2e4339e5d58108799ac8 - file is shared with the persona (shared_with_emails)
[YES LB] L177 gdrive.drive_files insert f_a72a7fd18327ed34fa2ac6 - file is shared with the persona (shared_with_emails)
[YES LB] L178 gdrive.drive_files insert f_facf46180c5ba68c35925d - file is shared with the persona (shared_with_emails)
[YES LB] L179 gdrive.drive_files insert f_60aee1e96a59111c246a73 - file is shared with the persona (shared_with_emails)
[YES LB] L180 gdrive.drive_files insert f_8a09205b3ab1ae2b7061b3 - file is shared with the persona (shared_with_emails)
[YES LB] L181 gdrive.drive_files insert f_353fa24f04ab2c658d09bb - file is shared with the persona (shared_with_emails)
[YES LB] L182 gdrive.drive_files insert f_dc52b1cdde87ff49f36bc1 - file is shared with the persona (shared_with_emails)
[YES LB] L183 gdrive.drive_files insert f_e84ff3bed0d6eb20aa6ae5 - file is shared with the persona (shared_with_emails)
[YES LB] L184 gdrive.drive_files insert f_846e988c8642078ec32fd8 - file is shared with the persona (shared_with_emails)
[YES LB] L185 gdrive.drive_files insert f_ca2f05278861dc6e12ecfd - file is shared with the persona (shared_with_emails)
[YES LB] L186 gdrive.drive_files insert f_a1582de8fc89f7ab4d42e8 - file is shared with the persona (shared_with_emails)
[YES LB] L187 gdrive.drive_files insert f_fcfdf5502a68b1797fa0db - file is shared with the persona (shared_with_emails)
[YES LB] L188 gdrive.drive_files insert f_dc5cf9e4250d433c1511ec - file is shared with the persona (shared_with_emails)
[YES LB] L189 gdrive.drive_files insert f_bcd34f98925e3f20d846ce - file is shared with the persona (shared_with_emails)
[YES LB] L190 gdrive.drive_files insert f_02b1968f5e882366fbb883 - file is shared with the persona (shared_with_emails)
[YES LB] L192 gsheets.sheets_spreadsheets insert f_02b1968f5e882366fbb883 - file is shared with the persona (shared_with_emails)
[YES LB] L193 gsheets.sheets_sheets insert f_02b1968f5e882366fbb883, f_02b1968f5e882366fbb883#0 - file is shared with the persona (shared_with_emails)
[YES LB] L194 gsheets.sheets_sheets insert f_02b1968f5e882366fbb883, f_02b1968f5e882366fbb883#1 - file is shared with the persona (shared_with_emails)
[YES LB] L195 gsheets.sheets_sheets insert f_02b1968f5e882366fbb883, f_02b1968f5e882366fbb883#2 - file is shared with the persona (shared_with_emails)
[YES LB] L196 gsheets.sheets_sheets insert f_02b1968f5e882366fbb883, f_02b1968f5e882366fbb883#3 - file is shared with the persona (shared_with_emails)
[YES LB] L197 gdrive.drive_files insert f_fdd6d2d2f4a4d2f5b908fb - file is shared with the persona (shared_with_emails)
[YES LB] L199 gdocs.docs_documents insert f_fdd6d2d2f4a4d2f5b908fb - file is shared with the persona (shared_with_emails)
[YES LB] L205 gdrive.drive_files insert f_5ebf55ad29e815d46243c8 - file is shared with the persona (shared_with_emails)
[YES LB] L207 gslides.slides_presentations insert f_5ebf55ad29e815d46243c8 - file is shared with the persona (shared_with_emails)
[YES LB] L208 gslides.slides_pages insert f_5ebf55ad29e815d46243c8, slide_3094f53a92b2 - file is shared with the persona (shared_with_emails)
[YES LB] L209 gslides.slides_page_elements insert f_5ebf55ad29e815d46243c8, el_46b532d7f66d, slide_3094f53a92b2 - file is shared with the persona (shared_with_emails)
[YES LB] L210 gslides.slides_page_elements insert f_5ebf55ad29e815d46243c8, el_9006e13d1b71, slide_3094f53a92b2 - file is shared with the persona (shared_with_emails)
[YES LB] L211 gslides.slides_pages insert f_5ebf55ad29e815d46243c8, slide_2f543a88ea15 - file is shared with the persona (shared_with_emails)
[YES LB] L212 gslides.slides_page_elements insert f_5ebf55ad29e815d46243c8, el_bc403344b919, slide_2f543a88ea15 - file is shared with the persona (shared_with_emails)
[YES LB] L213 gslides.slides_page_elements insert f_5ebf55ad29e815d46243c8, el_1f12d04ad444, slide_2f543a88ea15 - file is shared with the persona (shared_with_emails)
[YES LB] L215 gslides.slides_pages insert f_5ebf55ad29e815d46243c8, slide_0655492faa5a - file is shared with the persona (shared_with_emails)
[YES LB] L216 gslides.slides_page_elements insert f_5ebf55ad29e815d46243c8, el_61ecca3f712d, slide_0655492faa5a - file is shared with the persona (shared_with_emails)
[YES LB] L217 gslides.slides_page_elements insert f_5ebf55ad29e815d46243c8, el_5925f7c037fa, slide_0655492faa5a - file is shared with the persona (shared_with_emails)
[YES LB] L218 gslides.slides_pages insert f_5ebf55ad29e815d46243c8, slide_2b60b5e53f2c - file is shared with the persona (shared_with_emails)
[YES LB] L219 gslides.slides_page_elements insert f_5ebf55ad29e815d46243c8, el_43a43bd396b4, slide_2b60b5e53f2c - file is shared with the persona (shared_with_emails)
[YES LB] L220 gslides.slides_page_elements insert f_5ebf55ad29e815d46243c8, el_b04e5ccd5706, slide_2b60b5e53f2c - file is shared with the persona (shared_with_emails)
[YES] L224 gmail.gmail_threads insert claire.morgan@harmonygames.co/1843080777036925215 - row user_email is the persona (claire.morgan@harmonygames.co)
[YES LB] L226 gmail.gmail_messages insert claire.morgan@harmonygames.co/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>, cla - row user_email is the persona (claire.morgan@harmonygames.co)
[NO] L230 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843080777478741540 - row is in mailbox frederick.stone@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L231 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>, f - row is in mailbox frederick.stone@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L235 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1843080777552218739 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L236 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>, leo - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L240 gmail.gmail_threads insert marcus.bennett@harmonygames.co/1843080777405480450 - row is in mailbox marcus.bennett@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L241 gmail.gmail_messages insert marcus.bennett@harmonygames.co/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>, ma - row is in mailbox marcus.bennett@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L245 gmail.gmail_threads insert martin.walsh@harmonygames.co/1843080777143145137 - row is in mailbox martin.walsh@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L246 gmail.gmail_messages insert martin.walsh@harmonygames.co/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>, mart - row is in mailbox martin.walsh@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[YES] L250 gmail.gmail_threads insert claire.morgan@harmonygames.co/1844644077950167516 - row user_email is the persona (claire.morgan@harmonygames.co)
[YES LB] L251 gmail.gmail_messages insert claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>, cla - row user_email is the persona (claire.morgan@harmonygames.co)
[NO] L254 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844644078464897252 - row is in mailbox frederick.stone@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L255 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>, f - row is in mailbox frederick.stone@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L258 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1844644078011653282 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L259 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>, leo - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L262 gmail.gmail_threads insert marcus.bennett@harmonygames.co/1844644078077504433 - row is in mailbox marcus.bennett@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L263 gmail.gmail_messages insert marcus.bennett@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>, ma - row is in mailbox marcus.bennett@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L266 gmail.gmail_threads insert martin.walsh@harmonygames.co/1844644078449983920 - row is in mailbox martin.walsh@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L267 gmail.gmail_messages insert martin.walsh@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>, mart - row is in mailbox martin.walsh@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[YES] L270 gmail.gmail_threads insert claire.morgan@harmonygames.co/1844732284519287777 - row user_email is the persona (claire.morgan@harmonygames.co)
[YES LB] L271 gmail.gmail_messages insert claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>, cla - row user_email is the persona (claire.morgan@harmonygames.co)
[NO] L277 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844732284882540716 - row is in mailbox frederick.stone@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L278 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>, f - row is in mailbox frederick.stone@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L284 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1844732285026565607 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L285 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>, leo - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L291 gmail.gmail_threads insert marcus.bennett@harmonygames.co/1844732284828828071 - row is in mailbox marcus.bennett@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L292 gmail.gmail_messages insert marcus.bennett@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>, ma - row is in mailbox marcus.bennett@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L298 gmail.gmail_threads insert martin.walsh@harmonygames.co/1844732284741054074 - row is in mailbox martin.walsh@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[NO] L299 gmail.gmail_messages insert martin.walsh@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>, mart - row is in mailbox martin.walsh@harmonygames.co, not the persona's (claire.morgan@harmonygames.co)
[YES] L305 gmail.gmail_threads insert claire.morgan@harmonygames.co/1844154099753384967 - row user_email is the persona (claire.morgan@harmonygames.co)
[YES LB] L306 gmail.gmail_messages insert claire.morgan@harmonygames.co/<CAJec750be2c45f33a4016dbe77be0056@mail.gmail.com>, claire.m - row user_email is the persona (claire.morgan@harmonygames.co)
[YES LB] L309 gcal.gcal_events insert evt_d947bf7cd910549b674b1f - event is on the persona's own calendar claire.morgan@harmonygames.co
[YES] L311 gcal.gcal_events insert evt_239a96845c8465f6c4099b - persona is an attendee and holds its own copy evt_d947bf7cd910549b674b1f (same ical_uid and start) on claire.morgan@harmonygames.co
[YES] L312 gcal.gcal_events insert evt_7ca595cfa2e8a51769ef28 - persona is an attendee and holds its own copy evt_d947bf7cd910549b674b1f (same ical_uid and start) on claire.morgan@harmonygames.co
[YES] L313 gcal.gcal_events insert evt_1f74e7a2684103c4644a3d - persona is an attendee and holds its own copy evt_d947bf7cd910549b674b1f (same ical_uid and start) on claire.morgan@harmonygames.co
[YES] L314 gcal.gcal_events insert evt_78fd240a7e0229f18fe246 - persona is an attendee and holds its own copy evt_d947bf7cd910549b674b1f (same ical_uid and start) on claire.morgan@harmonygames.co
[YES] L315 gcal.gcal_events insert evt_8678e073bb601ead3e686b - persona is an attendee and holds its own copy evt_d947bf7cd910549b674b1f (same ical_uid and start) on claire.morgan@harmonygames.co
[YES] L316 gcal.gcal_events insert evt_26c86d9ea1b590bf86fe70 - persona is an attendee and holds its own copy evt_d947bf7cd910549b674b1f (same ical_uid and start) on claire.morgan@harmonygames.co
[YES LB] base slack C05433XK267/1753789877.590639 - base record: message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public builds
[YES LB] base slack C05433XK267/1753820674.990309 - base record: message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of public builds
[YES LB] base slack C06DJBJL798/1753968186.965269 - base record: message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
[YES LB] base slack C06DJBJL798/1755114007.441789 - base record: message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
[YES LB] base slack C06DJBJL798/1756914854.743319 - base record: message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie_marketing
[YES LB] base slack C0880U9751A/1738109783.735889 - base record: message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie-match3d
[YES LB] base slack C0880U9751A/1753820524.488479 - base record: message inherits channel: persona EMPLOYEE_0009_SLACK_ID is in members of private zombie-match3d

summary: {'YES': 69, 'NO': 24}  unscoped rows (always visible): 145
  gcal.gcal_events: {'YES': 7}
  gdocs.docs_documents: {'YES': 1}
  gdrive.drive_files: {'YES': 19}
  gmail.gmail_messages: {'YES': 4, 'NO': 12}
  gmail.gmail_threads: {'YES': 4, 'NO': 12}
  gsheets.sheets_sheets: {'YES': 4}
  gsheets.sheets_spreadsheets: {'YES': 1}
  gslides.slides_page_elements: {'YES': 8}
  gslides.slides_pages: {'YES': 4}
  gslides.slides_presentations: {'YES': 1}
  slack.slack_messages: {'YES': 16}
verdict: PASS (0 load-bearing rows not visible)
```

## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · persona-readable · unique · instructions-not-answer) | Inferable |
| --- | --- | --- | --- | --- |
| R1 tracker scope: every serving store surface and ad, paused ones out (RO-free; surface V01, S10, S11) | the sheet `f_02b1968f5e882366fbb883`, the Trello comment `68dc65a0f2d7fb28743f5860`, `cmt_art831_2` | scope ("everything that's live today, the store pages and every ad we're running") | the ask `C06DJBJL798/1759269913.882683` · #zombie_marketing member · the one Halloween ask · names the sheet as a source, not the list | yes (requester's scope) |
| R2 call per surface (surface S03–S36) | deck `f_5ebf55ad29e815d46243c8`; ticket comments ART-793 … ART-854; Marcus's note `C09ATAJ220H/1758823964.738872`; Frederick's comment `68d6cff0c6568da5d9c8e81f` | deliverable ("the Halloween call") | the ask names "Robert has direction for seasonal art"; Robert's pointer `C08R8CHB0QL/1758817822.269981` names the deck · readable · unique title · the deck states the rule and the call words ("the newest capture is the one that counts"; "re-capture, re-render or re-cut"), never a call | yes (once the ask is followed; the note and the comment are facts the deck's rule is applied to) |
| R3 / R4 ship route and due for store and icon (RO6, RO8, RO9) | calendar `f_fdd6d2d2f4a4d2f5b908fb` | deliverable ("who makes what by when") | the ask "Arthur's release calendar has the Q4 dates" · shared with Claire · one doc by that title · states dates and rules, not the icon's due | yes |
| R5 ad due date (RO2, RO10, S37–S39) | changes mail `claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>`; Frederick's later reply `C0880U9751A/1759275738.984915` | deliverable ("by when", "comment each ad's call and due date") | the ask "Frederick is sending his october UA plan tonight" · Claire's INBOX and #zombie-match3d · the same person's later word on the same date · states the hand-off dates per campaign, not per-ad calls | yes (a dated correction by the plan's own author, not an extra rule) |
| R6 Skip for creatives that run only on Android US tablet (S08, S29, S33, S34) | the changes mail + each ticket's campaign note + the restart mail `claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>` | deliverable ("the Halloween call") | same mail · readable · unique · a rule ("anything that only runs there"); the restart mail changes the input, it adds no rule | yes |
| R7 reuse what exists and can ship (S05, S06, S24, S28) | folders `d_6c2e4339e5d58108799ac8` / `d_74a7c95c28097dd9777e01`, IM reply `D05V2N6PZNU/1759166437.080255`, Robert's review `C08R8CHB0QL/1759248337.170599` | the ask's "what we already have" (incorporated by "take his message and do it all") | the ask · readable · one message · asks the question, gives no answer | yes |
| R8 owners and assignments (RO3, S31, S32) | the ask's owner split; Martin's post `C05KNDCHAAG/1759243286.478812`, Leonard's reply `C05KNDCHAAG/1759275107.322377` | deliverable ("assign the ones that need new work to whoever's making them") | the ask "Martin has the icon and the stills, Marcus has video and end cards" · readable · unique · instruction; Leonard's own later reply updates it for the ad statics | yes |
| R9 comments and new tickets (RO1, S04, S26) | — (writes) | deliverable ("comment each ad's call and due date on its ART ticket", "open ART tickets for any new store art") | the ask (same sentences) · readable · unique · instruction; `C08R8CHB0QL/1759247246.453725` narrows "new store art" | yes |
| R10 delivery (RO7, D01, D02) | review `evt_d947bf7cd910549b674b1f` | destination + recipients ("a plan doc and a tracker in my Drive, shared with everyone on the review so they can comment"; "reply in Leonard's thread with both links before the review") | the review event on Claire's calendar (7 attendees) · own copy · one event · lists people, not content | yes |

Implicit requirements a competent assistant infers without a trigger: read each ad's ticket before commenting on it; use the sheet's creative names; one tracker row per surface. No gotcha is left without a trigger: the Reuse / Skip / Refresh rules, the dates and the scope additions all sit in records the ask points to. The six rev3 carriers add no requirement: each is a newer fact about something the ask already asks for (a date, a maker, a campaign, a capture), so each is settled by the newer-source and scope checks, not by a rule the prompt would need to carry.

Anchor-name table (carried unchanged from the dossier §6):

| Anchor | May be named |
| --- | --- |
| A1 | Leonard's Halloween message; Leonard's Halloween ask |

## 7 · Dates and constraints

| Item | Absolute date or value | Source | Past fact or deadline |
| --- | --- | --- | --- |
| Persona today | Wed Oct 1, 2025 (clock 00:00 PT = 07:00 UTC) | `Working_Files/00_Task_Context.json` universe.persona_today; the latest seeded event `C0880U9751A/1759275738.984915` (2025-09-30T23:42:18Z) precedes it | clock |
| Leonard's ask ("yesterday") | Tue Sep 30, 2025 15:05 PT (22:05:13Z) | `C06DJBJL798/1759269913.882683` | past fact |
| Halloween review ("Thursday's review") | Thu Oct 2, 2025 09:00–09:30 PT (16:00–16:30Z) | `evt_d947bf7cd910549b674b1f` | deadline (future event) |
| Ads on Android US phone with Frederick | Fri Oct 10, 2025 (30 working ads) | `C0880U9751A/1759275738.984915` (Tue Sep 30 16:42 PT) | deadline |
| Every other working ad with Frederick | Wed Oct 15, 2025 (18 working ads) | `claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>`; "iOS UK stays on the 15th" `C0880U9751A/1759275738.984915` | deadline |
| Martin's vacation | Mon Oct 6 – Wed Oct 15, 2025 | `C05KNDCHAAG/1759243286.478812` (Tue Sep 30 14:41Z); Leonard's reply `C05KNDCHAAG/1759275107.322377` (Sep 30 23:31Z) | future plan fact |
| Android US tablet campaign ends | Sun Oct 12, 2025 | `claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>` | future plan fact |
| Halloween flight | Sat Oct 18 – Fri Oct 31, 2025 (three campaigns) | `claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>` | future plan fact |
| Superseded draft dates | Fri Oct 17 hand-off; Oct 20–31 flight on four campaigns | `claire.morgan@harmonygames.co/<CANf1Nx8adc8e5aab6af2f77119eca82ab3cde@mail.gmail.com>` (Sep 12 17:40Z) | superseded |
| Merge cut / submission | Thu Oct 16, 2025 12:00 PT (19:00Z); submit Fri Oct 17; iOS listing live from about Wed Oct 22 | `f_fdd6d2d2f4a4d2f5b908fb` | deadline |
| Icon suggestion | "around the 24th" (Fri Oct 24) — a question, overruled by the cut | `C06DJBJL798/1759269913.882683` | superseded suggestion |
| Post-Halloween clean-up | Nov 6 submission | `f_fdd6d2d2f4a4d2f5b908fb` | future plan fact |
| Leonard in LA | Thu Oct 2, 2025; flies home Fri Oct 3 morning; dials in to the review | `evt_d947bf7cd910549b674b1f`; `C05KNDCHAAG/1759279503.256079` | future plan fact |
| Vendor quote reply-by | Oct 3, 2025 (decoy) | `claire.morgan@harmonygames.co/<CAJec750be2c45f33a4016dbe77be0056@mail.gmail.com>` | decoy |
| Zombie swap build | Android #1452 Jul 29, 2025 20:24Z / iOS 1232 | `C05433XK267/1753820674.990309`, `C0880U9751A/1753820524.488479` | past fact |
| Store sets live since | Sep 17, 2025 (1.3.38) | `C0880U9751A/1758141269.804779` | past fact |
| Robert's icon reply | Wed Sep 17, 2025 16:52:31Z | `C08R8CHB0QL/1758127951.679146` | past fact |
| cheer fastcouch re-capture | Tue Sep 16, 2025, Android #1896 | `cmt_art808_2` | past fact |
| Marcus's three re-captures noted | Thu Sep 25, 2025 18:12:44Z (Android #1935, #1896, #1966) | `C09ATAJ220H/1758823964.738872` | past fact |
| Frederick's packs comment | Fri Sep 26, 2025 17:40Z | Trello `68d6cff0c6568da5d9c8e81f` on `68768a1501ae552dbee94b8a` | past fact |
| Marcus's test post, Robert's review | Mon Sep 29, 2025 17:31Z; Tue Sep 30, 2025 16:05Z | `C08R8CHB0QL/1759167065.499092`, `C08R8CHB0QL/1759248337.170599` | past fact |
| Frederick's restart mail | Mon Sep 29, 2025 23:48Z | `claire.morgan@harmonygames.co/<CANf1Nx47805f8aa3d388495515d37fa274ef9@mail.gmail.com>` | past fact |

The prompt keeps "yesterday" and "Thursday's review" (relative, persona-natural; both resolve to one day each in PT and UTC) and states no other date.

## 8 · Difficulty levers

| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |
| --- | --- | --- | --- | --- |
| Ambiguity | yes | yes | the rules sit in the deck `f_5ebf55ad29e815d46243c8`, the calendar `f_fdd6d2d2f4a4d2f5b908fb`, the changes mail and each ticket's comments; the prompt names the work and the destinations only | the prompt names the start (Leonard's message, #zombie_marketing) and every destination Claire knows (her Drive, the review attendees, the ART tickets, Leonard's thread); it never says where a rule lives |
| Dynamic change | yes | yes | draft → changes mail → Frederick's reply (Fri Oct 17 → Wed Oct 15 → Fri Oct 10 on Android US phone, `C0880U9751A/1759275738.984915`); April ticket note → Marcus's note in another service (`cmt_art795_1` → `C09ATAJ220H/1758823964.738872`); the IM's done test → Robert's review (`D05V2N6PZNU/1759166437.080255` → `C08R8CHB0QL/1759248337.170599`); the ask's split → Martin's post and Leonard's reply (`C05KNDCHAAG/1759275107.322377`); ticket campaigns → the restart mail; "Rendered from Android #1529" → Frederick's packs comment `68d6cff0c6568da5d9c8e81f`; Martin's "exported" `C08R8CHB0QL/1759245641.309714` → the Store folder `d_74a7c95c28097dd9777e01`; Leonard's "24th" → the calendar; Martin's concept → Robert's reply `C08R8CHB0QL/1758127951.679146` | the prompt gives the reason to look past the first summary ("work out the Halloween call for everything that's live today") and names neither the stale record nor the correction |
| Multi-source | yes | yes | Slack, Sheets, Docs, Slides, Gmail, Linear, Drive, Trello, GCal carry a deciding fact; Contacts, GitHub, Confluence and Snowflake are conditional reads (13 services, `01_Hardness_Manifest.json` services and call_budget) | no source is named as an exact artifact; the review is named only as the audience and deadline |
| Async | no | — | `03_Error_Async_Config.txt` Friction: none | nothing to hide |
| Error recovery | no | — | Friction: none | nothing announced |
| Access control | no | — | every deciding record is visible to Claire (check-sql PASS) | no restriction is described |

## 9 · Must not appear in the prompt

- Tool and parameter vocabulary (`Evals/references/tools/catalog.json`, `Working_Files/research/prompt/catalog.md` §8): every tool name of slack, gmail, gcal, gdrive, gdocs, gsheets, gslides, linear, trello, contacts, github, confluence, snowflake (e.g. `linear_create_comment`, `gdrive_share_file`, `slack_send_message`) and their parameter names (`issueId`, `thread_ts`, `assignee`, `dueDate`, `spreadsheetId`, …); "the X tool", "MCP" (no MCP server name exists in the catalog).
- Opaque ids and filenames (dossier ledger): `C06DJBJL798/1759269913.882683` and every ts, ART-793 … ART-854, `cmt_art*`, `f_02b1968f5e882366fbb883`, `f_fdd6d2d2f4a4d2f5b908fb`, `f_5ebf55ad29e815d46243c8`, `d_272d849cde40c35980a433`, `d_74a7c95c28097dd9777e01`, `d_6c2e4339e5d58108799ac8`, `evt_d947bf7cd910549b674b1f`, Trello ids, Message-IDs, `ZM3D_Halloween_*.png`, `cheer_fastcouch_halloween_*.mp4`.
- Exact titles of the hidden authorities and evidence (§5 "No" rows): "ZM3D live creatives", "ZM3D release calendar — Q4", "Seasonal art direction — Q4 2025", "October UA plan", "Halloween push" (the Trello card), "ZM ROADMAP", "ZM3D Halloween 2025", "Store", "UA masters", "UA creative library".
- Root causes and findings (dossier §5, solver truth): the Android #1452 / iOS 1232 threshold, "newest capture", "music baked in", the Android US tablet end (Oct 12), Oct 15, Oct 16 12:00 PT, Oct 17, Oct 18–31, the missing iPad set, the two cheer fastcouch Halloween cuts, Julia's 4:5 static, the portrait end card, the KayKit / Halloween Bits pack and the vendor, Robert's verdict on Martin's icon concept, any creative name, any count (62, 58, 48, 42, 36, 30, 18, 14, 12, 10, 6, 2), the four call words as a list.
- The six rev3 rules and their words (`Working_Files/01_Hardness_Manifest.json` mechanism_portfolio):
  - R_TEST_TURNED_DOWN: "turned down", "can't ship", "test", "July capture", "Sep 16", "fog", "pumpkins", "redo".
  - R_REVIEW_WINDOW: "review window", "manual review", "Unity rep", "Unity", "fake installs", "Android", "Android US phone", "iOS UK", "Oct 10", "Fri Oct 10", "5 days".
  - R_RECAPTURE_NOTE: "re-capture", "recapture", "re-recorded", "re-record", "#zm-animations", "#1896", "#1935", "#1966", "couch alpha 50", "barrel marketing2", "balloons alpha 50".
  - R_STATICS_COVER: "vacation", "Julia", "Lawson", "statics", "static", "stills", "cover", "#company-internal", "Oct 6".
  - R_TABLET_TRIM: "tablet", "tablet trim", "iOS UK tablet", "Android US tablet", "restart", "retention", "landscape", "squirrelfail", "mrfluffernot".
  - R_OLD_PACKS: "old zombies", "old packs", "packs", "re-render", "rerender", "Marketing Video Refresh", "end card", "end card 001".
- Leonard's travel (`evt_d947bf7cd910549b674b1f`, `C05KNDCHAAG/1759279503.256079`): "LA", "dial in", "investors".
- Result of the scan: 79 words and phrases (the rev3 rule words above, the six rule ids, the rest of the dates, call words and people) scanned against `04_Prompt.txt` (sha256 63d7c0713c3b) by `Working_Files/prompt_gen/build_brief.py`, whole word, any case: 0 found.
- People-as-sources that point at hidden evidence: Frederick's plan, Marcus's DM, Robert's deck, Martin's export, Arthur's calendar (the ask already names its sources; the prompt does not repeat them).
- Friction: none configured (`03_Error_Async_Config.txt`); nothing to announce, and Unity's manual review is a story fact, not a tool wait. Reference files: none, no `/app/artifact` path.
- Form: markdown, bullets, numbered steps, column lists, per-deliverable content specs, format rules, the words First / Then / Finally (`Evals/references/rules/common_errors.md` §3 search hits), answer-key clauses, hedges ("if my date is off …").

## 10 · Entity traps

Pasted `entity.py collisions` and `entity.py resolve` output (verbatim):

Run entity.py collisions:

```text
SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <trello:c48a210d5c5a4b59231c6873>']
  martin: ['Martin Lewis <PERSON_0394_EMAIL>', 'Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]']
  thomas: ['Thomas Baker <thomas.baker@harmonygames.co>', 'Thomas <thomas@harmonygames.co> [persona thomas]']

SHARED_LAST_NAMES (5)
  baker: ['Owen Baker <owen.baker@harmonygames.co> [persona owen_baker]', 'Thomas Baker <thomas.baker@harmonygames.co>']
  bennett: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Oscar Bennett <oscar.bennett@harmonygames.co>']
  brooks: ['Lauren Brooks <lauren@harmonygames.co>', 'Oliver Brooks <oliver.brooks@harmonygames.co> [persona oliver_brooks]']
  lawson: ['Julia Lawson <julia.lawson@harmonygames.co> [persona julia_lawson]', 'Peter Lawson <peter.lawson@harmonygames.co>']
  price: ['Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]', 'Nathan Price <nathan@harmonygames.co>']

LOOKALIKE_HANDLES_AND_ALIASES (15)
  - Gmail thread files of arthur.blake@harmonygames.co are named 'blake@harmonygames.co_*'
  - Gmail thread files of brian.foster@harmonygames.co are named 'brian@harmonygames.co_*'
  - Gmail thread files of calvin.price@harmonygames.co are named 'calvin@harmonygames.co_*'
  - Gmail thread files of claire.morgan@harmonygames.co are named 'claire@harmonygames.co_*'
  - Gmail thread files of frederick.stone@harmonygames.co are named 'frederick@harmonygames.co_*'
  - Gmail thread files of julia.lawson@harmonygames.co are named 'jlawson@harmonygames.co_*'
  - Gmail thread files of leonard.hayes@harmonygames.co are named 'leonard@harmonygames.co_*'
  - Gmail thread files of oliver.brooks@harmonygames.co are named 'oliver@harmonygames.co_*'
  - Gmail thread files of owen.baker@harmonygames.co are named 'owen@harmonygames.co_*'
  - Gmail thread files of samuel.turner@harmonygames.co are named 'samuel@harmonygames.co_*'
  - Gmail thread files of simon.walker@harmonygames.co are named 'simon@harmonygames.co_*'
  - Gmail thread files of vincent.parker@harmonygames.co are named 'vincent@harmonygames.co_*'
  - Gmail thread files of felix.young@harmonygames.co are named 'felixyoung@harmonygames.co_*'
  - Gmail thread files of oscar.bennett@harmonygames.co are named 'oscar@harmonygames.co_*'
  - Slack handle 'thomas' (U05F0A0D12F) belongs to Thomas Baker <thomas.baker@harmonygames.co> but equals the mailbox local part of Thomas <thomas@harmonygames.co> [persona thomas]

LOOKALIKE_EMAIL_LOCAL_PARTS (1)
  - 'thomas@' vs 'thomas.baker@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['Thomas Baker <thomas.baker@harmonygames.co>']

TOKENS_MAPPING_TO_SEVERAL_ENTITIES (9)
  EMPLOYEE_0024: {'entities': ['scott <employee_0024@harmonygames.co>', '? <slack:EMPLOYEE_0024_SLACK_ID>', '? <trello:3d36d70154e6a715614e0d75>'], 'records': ['gcal.calendar_id=employee_0024@harmonygames.co', 'gcal.owner_email=employee_0024@harmonygames.co', 'linear.id=usr_EMPLOYEE_0024', 'linear.email=employee_0024@harmonygames.co', 'contacts.email=employee_0024@harmonygames.co', 'email.email=employee_0024@harmonygames.co', 'slack.id=EMPLOYEE_0024_SLACK_ID', 'trello.username=employee_0024']}
  EMPLOYEE_0032: {'entities': ['? <EMPLOYEE_0032_EMAIL>', 'Josh Dempsey <josh.dempsey@harmonygames.co>', '? <github:EMPLOYEE_0032_GITHUB_USERNAME>', '? <slack:EMPLOYEE_0032_SLACK_ID>'], 'records': ['confluence.id=user_EMPLOYEE_0032', 'gmail.mailbox=EMPLOYEE_0032_EMAIL', 'gdrive.email=EMPLOYEE_0032_EMAIL', 'linear.id=usr_EMPLOYEE_0032', 'linear.email=EMPLOYEE_0032_EMAIL', 'contacts.email=EMPLOYEE_0032_EMAIL', 'email.email=EMPLOYEE_0032_EMAIL', 'github.login=EMPLOYEE_0032_GITHUB_USERNAME', 'slack.id=EMPLOYEE_0032_SLACK_ID']}
  PERSON_2218: {'entities': ['? <PERSON_2218_EMAIL>', '? <github:PERSON_2218_GITHUB_USERNAME>'], 'records': ['linear.id=usr_PERSON_2218', 'linear.email=PERSON_2218_EMAIL', 'contacts.email=PERSON_2218_EMAIL', 'email.email=PERSON_2218_EMAIL', 'github.login=PERSON_2218_GITHUB_USERNAME']}
  PERSON_2360: {'entities': ['? <PERSON_2360_EMAIL>', 'Claire <github:PERSON_2360_GITHUB_USERNAME>'], 'records': ['github.login=PERSON_2360_GITHUB_USERNAME', 'email.email=PERSON_2360_EMAIL']}
  PERSON_3233: {'entities': ['? <PERSON_3233_EMAIL>', '? <github:PERSON_3233_GITHUB_USERNAME>', '? <slack:PERSON_3233_SLACK_ID>'], 'records': ['linear.id=usr_PERSON_3233', 'linear.email=PERSON_3233_EMAIL', 'contacts.email=PERSON_3233_EMAIL', 'email.email=PERSON_3233_EMAIL', 'github.login=PERSON_3233_GITHUB_USERNAME', 'slack.id=PERSON_3233_SLACK_ID']}
  PERSON_3335: {'entities': ['? <PERSON_3335_EMAIL>', '? <slack:PERSON_3335_SLACK_ID>'], 'records': ['contacts.email=PERSON_3335_EMAIL', 'email.email=PERSON_3335_EMAIL', 'slack.id=PERSON_3335_SLACK_ID']}
  PERSON_3935: {'entities': ['? <PERSON_3935_EMAIL>', '? <slack:PERSON_3935_SLACK_ID>'], 'records': ['email.email=PERSON_3935_EMAIL', 'slack.id=PERSON_3935_SLACK_ID']}
  PERSON_5275: {'entities': ['? <PERSON_5275_EMAIL>', '? <slack:PERSON_5275_SLACK_ID>'], 'records': ['contacts.email=PERSON_5275_EMAIL', 'email.email=PERSON_5275_EMAIL', 'slack.id=PERSON_5275_SLACK_ID']}
  PERSON_5360: {'entities': ['? <PERSON_5360_EMAIL>', '? <slack:PERSON_5360_SLACK_ID>'], 'records': ['email.email=PERSON_5360_EMAIL', 'slack.id=PERSON_5360_SLACK_ID']}

SEVERAL_IDS_IN_ONE_SERVICE (1)
  - Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]: 2 github identities ['PERSON_0003_GITHUB_USERNAME', 'PERSON_2137_GITHUB_USERNAME'] (joins: ['exact_email', 'exact_name'])

PERSONA_ROLE_VS_CONTACTS_JOB (5)
  - Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]: roster role 'Game Engineer (Unity VFX)' vs Contacts job 'Game Engineer (Unity/VFX)'
  - Frederick Stone <frederick.stone@harmonygames.co> [persona frederick_stone]: roster role 'Co-founder' vs Contacts job 'Commercial Lead, Marketing & Business Development'
  - Leonard Hayes <leonard.hayes@harmonygames.co> [persona leonard_hayes]: roster role 'Co-founder & Creative Director' vs Contacts job 'Co-founder & CEO'
  - Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]: roster role 'Artist' vs Contacts job 'Artist (VFX & Animation)'
  - Robert <robert@harmonygames.co> [persona robert]: roster role 'Co-Founder & Creative Director' vs Contacts job 'Co-founder & Chief Product Officer'

SHARED_CONTACT_JOB_TITLES (5)
  Game Designer: ['Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]', 'Samuel Turner <samuel.turner@harmonygames.co> [persona samuel_turner]']
  Game Developer: ['Thomas <thomas@harmonygames.co> [persona thomas]', 'Lucas <lucas@harmonygames.co>']
  Game Engineer: ['Brian Foster <brian.foster@harmonygames.co> [persona brian_foster]', 'Victor Barnes <victor.barnes@harmonygames.co> [persona victor_barnes]']
  General Counsel: ['Michelle Carter <michelle.carter@harmonygames.co>', 'Thomas Baker <thomas.baker@harmonygames.co>']
  User Acquisition Manager: ['George Miller <george.miller@harmonygames.co>', 'Megan Wilson <megan.wilson@harmonygames.co>', 'Victoria Lane <victoria.lane@harmonygames.co>']

UNRESOLVED (11)
  [ambiguous_name] github: mononym 'Claire' is an exact name of [] and the first name of ['email:claire.morgan@harmonygames.co'] -> candidates ['email:claire.morgan@harmonygames.co']
  [ambiguous_name] trello: mononym 'Marcus' is an exact name of [] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co'] -> candidates ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']
  [token_link] EMPLOYEE_0024: same token number across services but no shared exact email/name: not joined -> candidates ['email:employee_0024@harmonygames.co', 'slack:EMPLOYEE_0024_SLACK_ID', 'trello:3d36d70154e6a715614e0d75']
  [token_link] EMPLOYEE_0032: same token number across services but no shared exact email/name: not joined -> candidates ['email:EMPLOYEE_0032_EMAIL', 'email:josh.dempsey@harmonygames.co', 'github:EMPLOYEE_0032_GITHUB_USERNAME', 'slack:EMPLOYEE_0032_SLACK_ID']
  [token_link] PERSON_2218: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_2218_EMAIL', 'github:PERSON_2218_GITHUB_USERNAME']
  [token_link] PERSON_2360: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_2360_EMAIL', 'github:PERSON_2360_GITHUB_USERNAME']
  [token_link] PERSON_3233: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3233_EMAIL', 'github:PERSON_3233_GITHUB_USERNAME', 'slack:PERSON_3233_SLACK_ID']
  [token_link] PERSON_3335: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3335_EMAIL', 'slack:PERSON_3335_SLACK_ID']
  [token_link] PERSON_3935: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3935_EMAIL', 'slack:PERSON_3935_SLACK_ID']
  [token_link] PERSON_5275: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_5275_EMAIL', 'slack:PERSON_5275_SLACK_ID']
  [token_link] PERSON_5360: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_5360_EMAIL', 'slack:PERSON_5360_SLACK_ID']

INTEGRITY FLAGS (2)
  {'type': 'id_with_space', 'service': 'linear', 'id': 'usr_Victor Barnes'}
  {'type': 'name_mismatch_on_email_join', 'service': 'github', 'id': 'PERSON_2314_GITHUB_USERNAME', 'detail': "GitHub PERSON_2314_GITHUB_USERNAME joined by email but shows name 'Ryan' (entity is Frederick Stone)"}

```

Run entity.py resolve "Leonard":

```text
no exact match for 'Leonard'
  candidate: email:leonard.hayes@harmonygames.co  Leonard Hayes  ['leonard.hayes@harmonygames.co']

```

Run entity.py resolve "Frederick":

```text
no exact match for 'Frederick'
  candidate: email:frederick.stone@harmonygames.co  Frederick Stone  ['frederick.stone@harmonygames.co']

```

Run entity.py resolve "Martin":

```text
no exact match for 'Martin'
  candidate: email:martin.walsh@harmonygames.co  Martin Walsh  ['martin.walsh@harmonygames.co']
  candidate: email:PERSON_0394_EMAIL  Martin Lewis  ['PERSON_0394_EMAIL']

```

Run entity.py resolve "Marcus":

```text
ENTITY trello:c48a210d5c5a4b59231c6873  name=Marcus  kind=person  emails=[]
  trello     id=c48a210d5c5a4b59231c6873, username=marcus, fullName=Marcus   [join: own_record (ambiguous name)]
  absent from: slack, gmail, gcal, gdrive, linear, github, confluence, contacts
  last activity: -
  UNRESOLVED (ambiguous_name): mononym 'Marcus' is an exact name of [] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']

```

Run entity.py resolve "Robert":

```text
ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
  persona: robert - Co-Founder & Creative Director / Executive
  slack      id=EMPLOYEE_0016_SLACK_ID, name=Robert, real_name=Robert, email=robert@harmonygames.co, is_bot=False, deleted=False, messages=110334, first_post=2023-03-15, last_post=2025-10-01   [join: exact_email]
  gmail      mailbox=robert@harmonygames.co, threads=14813, messages=17363, first=2023-03-15, last=2025-10-01   [join: exact_email]
  gcal       calendar_id=robert@harmonygames.co, owner_email=robert@harmonygames.co, summary=Robert — primary, events=1133, last_event_before_clock=2025-09-30   [join: exact_email]
  gdrive     id=user_9f7ba94f7526, email=robert@harmonygames.co, display_name=Robert, root_folders=['d_9f7ba94f7526d54d8482ba'], owned_items=190, last_modified=2025-09-25, files_shared_with=412   [join: exact_email]
  linear     id=usr_Robert, email=robert@harmonygames.co, name=Robert, is_active=True, last_activity=2025-09-30   [join: exact_email]
  github     login=EMPLOYEE_0016_GITHUB_USERNAME, name=Robert, email=robert@harmonygames.co, type=User, last_activity=2025-09-29   [join: exact_email]
  trello     id=3d06b73654d0c8940792514c, username=robert, fullName=Robert   [join: exact_name]
  confluence id=user_EMPLOYEE_0016, account_id=acct_EMPLOYEE_0016, email=robert@harmonygames.co, display_name=Robert, is_active=True, last_activity=2025-09-30   [join: exact_email]
  contacts   contact_id=5f647df33ba6e92fbd56b05b, name=Robert, email=robert@harmonygames.co, job=Co-founder & Chief Product Officer, is_user=True   [join: exact_email]
  last activity: {'slack': '2025-10-01', 'gmail': '2025-10-01', 'gcal': '2025-09-30', 'gdrive': '2025-09-25', 'linear': '2025-09-30', 'github': '2025-09-29', 'confluence': '2025-09-30'}

```

Run entity.py resolve "Arthur":

```text
no exact match for 'Arthur'
  candidate: email:arthur.blake@harmonygames.co  Arthur Blake  ['arthur.blake@harmonygames.co']

```

Run entity.py resolve "Julia":

```text
no exact match for 'Julia'
  candidate: email:julia.lawson@harmonygames.co  Julia Lawson  ['julia.lawson@harmonygames.co']

```

Run entity.py resolve "Claire":

```text
ENTITY github:PERSON_2360_GITHUB_USERNAME  name=Claire  kind=unidentified  emails=[]
  github     login=PERSON_2360_GITHUB_USERNAME, name=Claire, type=User, last_activity=2025-09-25   [join: own_record (ambiguous name)]
  absent from: slack, gmail, gcal, gdrive, linear, trello, confluence, contacts
  last activity: {'github': '2025-09-25'}
  UNRESOLVED (ambiguous_name): mononym 'Claire' is an exact name of [] and the first name of ['email:claire.morgan@harmonygames.co']
  UNRESOLVED (token_link): same token number across services but no shared exact email/name: not joined  records=['email.email=PERSON_2360_EMAIL', 'github.login=PERSON_2360_GITHUB_USERNAME']

```

Run entity.py resolve "Marcus Bennett":

```text
ENTITY email:marcus.bennett@harmonygames.co  name=Marcus Bennett  kind=person  emails=['marcus.bennett@harmonygames.co']
  persona: marcus_bennett - Artist / Design
  slack      id=EMPLOYEE_0002_SLACK_ID, name=Marcus Bennett, real_name=Marcus Bennett, email=marcus.bennett@harmonygames.co, is_bot=False, deleted=False, messages=25786, first_post=2023-09-28, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=marcus.bennett@harmonygames.co, threads=4219, messages=4245, first=2023-09-28, last=2025-09-29, thread_filename_alias=['marcus.bennett@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=marcus.bennett@harmonygames.co, owner_email=marcus.bennett@harmonygames.co, summary=Marcus Bennett — primary, events=604, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_c77c50cc15c5, email=marcus.bennett@harmonygames.co, display_name=marcus.bennett@harmonygames.co, root_folders=['d_c77c50cc15c5342d638ebb'], owned_items=47335, last_modified=2025-09-10, files_shared_with=132   [join: exact_email]
  linear     id=usr_c77c50cc15c5342d, email=marcus.bennett@harmonygames.co, name=marcus.bennett@harmonygames.co, is_active=True, last_activity=2025-09-25   [join: exact_email]
  github     login=PERSON_0396_GITHUB_USERNAME, name=Marcus Bennett, email=marcus.bennett@harmonygames.co, type=User, last_activity=2025-09-30   [join: exact_email]
  trello     id=7a20445f698bc5871ffd17f5, username=marcus.bennett, fullName=Marcus Bennett   [join: exact_name]
  confluence id=user_EMPLOYEE_0002, account_id=acct_EMPLOYEE_0002, email=marcus.bennett@harmonygames.co, display_name=Marcus Bennett, is_active=True   [join: exact_email]
  contacts   contact_id=c77c50cc15c5342d638ebb21, name=Marcus Bennett, email=marcus.bennett@harmonygames.co, job=Artist (VFX & Animation), is_user=False   [join: exact_email]
  last activity: {'slack': '2025-09-30', 'gmail': '2025-09-29', 'gcal': '2025-09-29', 'gdrive': '2025-09-10', 'linear': '2025-09-25', 'github': '2025-09-30'}
  UNRESOLVED (ambiguous_name): mononym 'Marcus' is an exact name of [] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']

```

Run entity.py resolve "Martin Walsh":

```text
ENTITY email:martin.walsh@harmonygames.co  name=Martin Walsh  kind=person  emails=['martin.walsh@harmonygames.co']
  persona: martin_walsh - Game Designer / Design
  slack      id=EMPLOYEE_0033_SLACK_ID, name=Martin Walsh, real_name=Martin Walsh, email=martin.walsh@harmonygames.co, is_bot=False, deleted=False, messages=7527, first_post=2023-08-28, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=martin.walsh@harmonygames.co, threads=4356, messages=4618, first=2023-08-27, last=2025-10-01, thread_filename_alias=['martin.walsh@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=martin.walsh@harmonygames.co, owner_email=martin.walsh@harmonygames.co, summary=Martin Walsh — primary, events=581, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_51f5f16d46e8, email=martin.walsh@harmonygames.co, display_name=martin.walsh@harmonygames.co, root_folders=['d_51f5f16d46e8cf55f5ee33'], owned_items=30, last_modified=2024-02-16, files_shared_with=136   [join: exact_email]
  linear     id=usr_51f5f16d46e8cf55, email=martin.walsh@harmonygames.co, name=martin.walsh@harmonygames.co, is_active=True, last_activity=2025-09-30   [join: exact_email]
  trello     id=ba9cc333cefad99228d6757d, username=martin.walsh, fullName=Martin Walsh   [join: exact_name]
  confluence id=user_EMPLOYEE_0033, account_id=acct_EMPLOYEE_0033, email=martin.walsh@harmonygames.co, display_name=Martin Walsh, is_active=True   [join: exact_email]
  contacts   contact_id=51f5f16d46e8cf55f5ee337b, name=Martin Walsh, email=martin.walsh@harmonygames.co, job=Game Designer, is_user=False   [join: exact_email]
  absent from: github
  last activity: {'slack': '2025-09-30', 'gmail': '2025-10-01', 'gcal': '2025-09-29', 'gdrive': '2024-02-16', 'linear': '2025-09-30'}

```

Run entity.py resolve "Julia Lawson":

```text
ENTITY email:julia.lawson@harmonygames.co  name=Julia Lawson  kind=person  emails=['julia.lawson@harmonygames.co']
  persona: julia_lawson - Product Manager / Product
  slack      id=EMPLOYEE_0005_SLACK_ID, name=Julia Lawson, real_name=Julia Lawson, email=julia.lawson@harmonygames.co, is_bot=False, deleted=False, messages=31848, first_post=2023-07-16, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=julia.lawson@harmonygames.co, threads=253, messages=304, first=2023-07-16, last=2025-09-17, thread_filename_alias=['jlawson@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=julia.lawson@harmonygames.co, owner_email=julia.lawson@harmonygames.co, summary=Julia Lawson — primary, events=748, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_8140f09bf9f1, email=julia.lawson@harmonygames.co, display_name=julia.lawson@harmonygames.co, root_folders=['d_8140f09bf9f1b94cb8ee2d'], owned_items=28, last_modified=2025-09-11, files_shared_with=158   [join: exact_email]
  linear     id=usr_8140f09bf9f1b94c, email=julia.lawson@harmonygames.co, name=julia.lawson@harmonygames.co, is_active=True, last_activity=2025-09-23   [join: exact_email]
  github     login=PERSON_0005_GITHUB_USERNAME, name=Julia Lawson, email=julia.lawson@harmonygames.co, type=User, last_activity=2025-09-29   [join: exact_email]
  trello     id=793af7ca6940bf18eb516c75, username=julia.lawson, fullName=Julia Lawson   [join: exact_name]
  confluence id=user_EMPLOYEE_0005, account_id=acct_EMPLOYEE_0005, email=julia.lawson@harmonygames.co, display_name=Julia Lawson, is_active=True, last_activity=2025-09-21   [join: exact_email]
  contacts   contact_id=8140f09bf9f1b94cb8ee2dd7, name=Julia Lawson, email=julia.lawson@harmonygames.co, job=Product Manager, is_user=False   [join: exact_email]
  last activity: {'slack': '2025-09-30', 'gmail': '2025-09-17', 'gcal': '2025-09-29', 'gdrive': '2025-09-11', 'linear': '2025-09-23', 'github': '2025-09-29', 'confluence': '2025-09-21'}

```

Run entity.py resolve "Marcus Lee":

```text
ENTITY email:marcus.lee@harmonygames.co  name=Marcus Lee  kind=person  emails=['marcus.lee@harmonygames.co']
  slack      id=PERSON_2705_SLACK_ID, name=Marcus Lee, real_name=Marcus Lee, email=marcus.lee@harmonygames.co, is_bot=False, deleted=False, messages=181, first_post=2023-12-19, last_post=2025-06-18   [join: exact_email]
  gcal       calendar_id=marcus.lee@harmonygames.co, owner_email=marcus.lee@harmonygames.co, summary=Marcus Lee — primary, events=3, last_event_before_clock=2024-09-26   [join: exact_email]
  linear     id=usr_b501f018a4c5319f, email=marcus.lee@harmonygames.co, name=marcus.lee@harmonygames.co, is_active=True   [join: exact_email]
  trello     id=54b24ad13c96c74bd0376532, username=marcus.lee, fullName=Marcus Lee   [join: exact_name]
  confluence id=user_STAFF_5, account_id=acct_STAFF_5, email=marcus.lee@harmonygames.co, display_name=Marcus Lee, is_active=True   [join: exact_email]
  contacts   contact_id=c7b13b5c524387cbef98ab8d, name=Marcus Lee, email=marcus.lee@harmonygames.co, job=AppLovin Business Development (UA partner, not an employee), is_user=False   [join: exact_email]
  absent from: gmail, gdrive, github
  last activity: {'slack': '2025-06-18', 'gcal': '2024-09-26'}
  UNRESOLVED (ambiguous_name): mononym 'Marcus' is an exact name of [] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']

```

Run entity.py resolve "Martin Lewis":

```text
ENTITY email:PERSON_0394_EMAIL  name=Martin Lewis  kind=person  emails=['PERSON_0394_EMAIL']
  contacts   contact_id=42869c73053b8c1b750ca3b6, name=Martin Lewis, email=PERSON_0394_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gmail, gcal, gdrive, linear, github, trello, confluence
  last activity: -

```

Run entity.py resolve "Peter Lawson":

```text
ENTITY email:peter.lawson@harmonygames.co  name=Peter Lawson  kind=person  emails=['peter.lawson@harmonygames.co']
  gcal       calendar_id=peter.lawson@harmonygames.co, owner_email=peter.lawson@harmonygames.co, summary=Peter Lawson — primary, events=2, last_event_before_clock=2023-05-01   [join: exact_email]
  gdrive     share_recipient=peter.lawson@harmonygames.co, files_shared_with=1   [join: exact_email]
  trello     id=bb244f7044cf0c4ca186f816, username=peter.lawson, fullName=Peter Lawson   [join: exact_name]
  contacts   contact_id=9e426d1ad2ba15c877071a89, name=Peter Lawson, email=peter.lawson@harmonygames.co, job=Product / Design Consultant (Contract), is_user=False   [join: exact_email]
  absent from: slack, gmail, linear, github, confluence
  last activity: {'gcal': '2023-05-01'}
```

| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |
| --- | --- | --- | --- |
| Marcus Bennett, video and end cards, Claire's IM partner, assignee ×42 | Marcus Lee (UA); Trello-only "Marcus"; the `marcus@harmonygames.co` mailbox (trap P03); Oscar Bennett for "Bennett" | the maker is the IM partner in `D05V2N6PZNU` and the author of every UA cut and of the #zm-animations note; Linear assignee `usr_c77c50cc15c5342d`; Marcus Lee is a separate Linear user `usr_b501f018a4c5319f` | marcus.bennett@harmonygames.co; marcus.lee@harmonygames.co; oscar.bennett@harmonygames.co; Trello `c48a210d5c5a4b59231c6873` |
| Martin Walsh, icon and store art (no longer the working ad statics) | Martin Lewis (external token) | only Martin Walsh is in #zombie-art and on the Linear team; Slack `EMPLOYEE_0033_SLACK_ID`, assignee `usr_51f5f16d46e8cf55` on the new store-art tickets if a run assigns them | martin.walsh@harmonygames.co; PERSON_0394_EMAIL |
| Julia Lawson, the ad statics while Martin is out, assignee ×6 | Peter Lawson; Martin Walsh (the ask's "stills") | named only as a mention token in Martin's post (`<@EMPLOYEE_0005_SLACK_ID>`, `C05KNDCHAAG/1759243286.478812`) and as "julia" in Leonard's reply; the static tickets write "Made by Julia Lawson"; roster role Product Manager, not an artist, yet she made the June statics; Linear `usr_8140f09bf9f1b94c`, active, member of `team_ART` (`tmem_team_ART_usr_8140f09bf9f1b94c`); not a review attendee | julia.lawson@harmonygames.co; peter.lawson@harmonygames.co |
| Claire Morgan (persona) | GitHub "Claire" `PERSON_2360_GITHUB_USERNAME` | unjoined GitHub token; the persona is EMPLOYEE_0009_SLACK_ID / usr_7fe31e7ec8199618 | claire.morgan@harmonygames.co |
| ART-831 (portrait end card), ART-793 … ART-854 | ENG-831, ENG-793 … (trap N01: shared numbers across teams) | the library is team_ART; the prompt says "ART ticket" | `ART-831`, `team_ART` |
| #zombie_marketing `C06DJBJL798` | #zombie-art `C08R8CHB0QL`, #zombie-match3d `C0880U9751A` | the ask and the reply thread are in #zombie_marketing | `C06DJBJL798/1759269913.882683` |
| The live creatives sheet `f_02b1968f5e882366fbb883` | Domino Delights "Video Capture Requests for UA" `f_b5fb884dc96261846b6c2c` (trap T10) | the 2024 sheet is another game's capture list | `f_02b1968f5e882366fbb883` |
| #zombie-match3d `C0880U9751A` (Frederick's date reply), #zm-animations `C09ATAJ220H` (Marcus's note), #company-internal `C05KNDCHAAG` (Martin's post) | each other, and #zombie_marketing `C06DJBJL798` | three private channels Claire is in; each holds one carrier, none is named in the ask | `C0880U9751A/1759275738.984915`, `C09ATAJ220H/1758823964.738872`, `C05KNDCHAAG/1759243286.478812` |
| "Marketing Video Refresh" card `68768a1501ae552dbee94b8a` (base, list Jul 24) | "Halloween push" card `68dc52e015f87c50c441d1a9` | same board ZM ROADMAP; Frederick comments on both | Trello `68d6cff0c6568da5d9c8e81f`, `68dc65a0f2d7fb28743f5860` |
| The KayKit Halloween Bits pack the studio owns | the vendor's "Halloween Bits bundle" quote | same product; a plain distractor since rev3, nothing graded | `6b350edd259a8b4499a9e625`; `C0880U9751A/1738109783.735889` |
| Zombie Match 3D (current name since Jul 24) | Puzzles vs Zombies, Match 3D (trap K02) | the prompt writes "Zombie Match 3D" | `f_fdd6d2d2f4a4d2f5b908fb` ("Zombie Match 3D store submissions") |

## 11 · Pre-submit checklist

- [ ] Written in Claire's voice; reads as a quick delegation, not a document.
- [ ] Names no tool, MCP server or parameter, and has no search hit (`linear_`, `gmail_`, `slack_`, `MCP`, `tool`, `First`, `Then`, `Finally`; `Evals/references/rules/common_errors.md` §3).
- [ ] States no root cause, no rule, no count and no creative.
- [ ] Every sentence is load-bearing.
- [ ] Every date resolves before Feb 14, 2026 and against Wed Oct 1, 2025 ("yesterday" = Sep 30, "Thursday's review" = Oct 2).
- [ ] Every name, channel and ID was checked in this run (§5a, §10).
- [ ] Plausible for Claire Morgan, Art Lead, in Marketing and GTM.
- [ ] Two or more services carry weight; investigation feeds writes.
- [ ] Two careful runs end in the same final state (§4b).
- [ ] Destinations named the way Claire knows them: her Drive, everyone on the review, each ad's ART ticket, Leonard's thread.
- [ ] The ask is incorporated as "his message" (anchor A1) and nothing in §9 appears, the rev3 rule words included.
- [ ] `04_Prompt.txt` is unchanged: sha256 starts 63d7c0713c3b.
- [ ] No carrier, channel, date or person from §5 rows 31–36 is hinted at (no Julia, no Unity, no vacation, no Android date, no re-capture, no packs).
- [ ] No "Halloween push", no sheet / calendar / deck / mail title, no build number.
- [ ] `/prompt` returns PASS (red-team emulation, then the platform).

## 12 · Blockers and routed defects

Nothing is routed open. No §5a fact needs routing: every seeded carrier is in the SQL and visible to Claire.

Closed earlier, kept for the record (scenario revision 03, `Working_Files/scenario_gen/redteam_dispositions.md` PW1 / PW2):

- PW1 (UGT fork, icon): Martin's base concept `C08R8CHB0QL/1758121809.236839` let the icon read as already made. Fixed with Robert's thread reply `C08R8CHB0QL/1758127951.679146`.
- PW2 (scope fork, end card): ART-831 was off the sheet with only its description saying it plays. Fixed with Frederick's note `cmt_art831_2`, which keeps its "Not on the live creatives sheet yet." sentence at rev3 (S0r declined the proposed cut).

Rev3 (`/create-hardening` MODE B moves 1–6, `Working_Files/01a_Hardening_Report.md` §10, §11, S0r outcome; `Working_Files/scenario_gen/apply_rev3.py`): the universe changed, not the prompt. The report found no prompt-side defect, and `04_Prompt.txt` stays byte-identical (sha256 63d7c071…). Scenario, injection, hardening and error-async gates PASS on SQL sha256 0a08dedecd60.

Evidence limits closed since the last brief: `gdrive_share_file` took `role: "commenter"` 12 times and `linear_update_issue` took an assignee email 48 times in the rev2 pre-check (`Working_Files/run_forensics/rev2/precheck/calls.jsonl`, 0 failed calls). No run has yet assigned a ticket to `julia.lawson@harmonygames.co`; she is an active `team_ART` member like the other two, so nothing is expected to differ.

Closed by the universe, re-tested at the prompt check: Leonard's base post `C05KNDCHAAG/1759279503.256079` (Oct 1 00:45Z: "won't attend internal meeting tomorrow and Thu") sat beside the seeded review he organized (`evt_d947bf7cd910549b674b1f`, Thu Oct 2), and rev3's R_STATICS_COVER path reads that channel. The review's description now says "I'm in LA Thursday so I'll dial in for this one." The argument and verdict are in `Working_Files/04_Prompt_Check.md` (C22 re-test); no write changes either way and the invite stays the sharing list.

## 13 · Self-review

1. Re-read as the eval (`Evals/1_Prompt_Eval.md` Phases 1–3) against this brief: persona and role (§1), competency and skill (§1), complexity levers (§8), seeding (rules in records, §6), fair readings (§4, §4b), feasibility and ACL (§5a, `Working_Files/research/prompt/catalog.md`), truthfulness of every premise the prompt will carry (§7, §10), coherence (§12).

| Area | Counter to a PASS | Resolution (evidence) | Verdict |
| --- | --- | --- | --- |
| Fair readings (accepted outcomes) | Strongest counter: Martin's Sep 17 Halloween icon is "what we already have", so the icon is Reuse and needs no ticket; a second fair outcome the rubric would reject | Robert's reply `C08R8CHB0QL/1758127951.679146` turns the concept down for the app icon; the deck `f_5ebf55ad29e815d46243c8` defines Reuse as "it already has a seasonal version" — the icon has none approved; §4b keeps the icon as Halloween version | holds (fixed upstream, PW1) |
| Fair readings (accepted outcomes) | Strongest counter: the Sep 30 mail says every Halloween ad is due Oct 15, and a reply in a bot-installs thread is not the plan, so Oct 15 for all stays fair | same author, same issue, 32 minutes later, and it names the date it replaces: "has to be with me by Fri Oct 10, not the 15th" (`C0880U9751A/1759275738.984915`); the newer-source check settles it (Eval 1 §2.1), both records are visible to Claire | holds |
| Fair readings (accepted outcomes) | Strongest counter: the cheer fastcouch test sits on the July capture, so the two cuts are Refresh first, not Halloween version | the tickets already carry the Sep 16 capture (`cmt_art808_2`, `cmt_art816_2`), the deck says "the newest capture is the one that counts" (`f_5ebf55ad29e815d46243c8`) and defines Halloween version as "dress it from the current art"; Robert's "doing again from the Sep 16 one" (`C08R8CHB0QL/1759248337.170599`) is exactly that | holds |
| Fair readings (accepted outcomes) | Strongest counter: Martin is only out Oct 6–15, so a run could leave the statics with him before he goes | his post hands them over outright and Leonard confirms it (`C05KNDCHAAG/1759243286.478812`, `C05KNDCHAAG/1759275107.322377`); the statics are due Oct 10 and Oct 15, inside his leave | holds |
| Clarity | Strongest counter: "comment each ad's call and due date on its ART ticket" could mean editing the ticket's due-date field instead of a comment | the ask `C06DJBJL798/1759269913.882683` says "drop a comment"; §4b allows the field in addition, never instead | holds |
| Clarity | Strongest counter: "share with everyone on the review" leaves the role open (view vs comment) | the prompt adds "so they can comment"; §4b accepts commenter or writer (representational) | holds |
| Incorporation | Strongest counter: "take his message and do it all" incorporates every bullet, including "maybe we swap the icon around the 24th?" as an instruction | the bullet is a question; Arthur's calendar `f_fdd6d2d2f4a4d2f5b908fb`, which the same message names for the Q4 dates, governs the date; Leonard's message asks for a plan "we can comment on", so overriding his suggestion with a cited cut is in scope | holds |
| Incorporation | Strongest counter: the pointed-to message hands over the answer | it names sources and owners only (no call, date or list); every call needs the deck, the mails and each ticket (§6) | holds |
| Incorporation | Strongest counter: the prompt incorporates only Leonard's message, so a Slack reply in another channel or a Trello comment adds no obligation and grading it is unauthorized (`prompt-incorporation-v1`) | the carriers add no rule; each is a newer fact on an asked field. Leonard's message asks for "who makes what by when" and names Frederick's plan and the owner split; `C0880U9751A/1759275738.984915` and `C05KNDCHAAG/1759275107.322377` are their own authors updating those statements (Eval 1 §2.1 newer source); `68d6cff0c6568da5d9c8e81f` and `C09ATAJ220H/1758823964.738872` are inputs to the deck's incorporated rule | holds |
| Truthfulness | Strongest counter: "I'm walking everyone through it at Thursday's review" is an unsupported narrative claim | the review's description reads "Claire walks us through the Halloween plan and tracker. I'm in LA Thursday so I'll dial in for this one." (`evt_d947bf7cd910549b674b1f`, Leonard, updated 2025-09-30T22:10:00Z) | holds |
| Truthfulness | Strongest counter: "yesterday" could be Sep 29 or Oct 1 in UTC | the ask is Sep 30 22:05:13Z = Sep 30 15:05 PT; both calendars give Sep 30 against Wed Oct 1 | holds |
| Feasibility / ACL | Strongest counter: a required read sits outside Claire's view (the other mailboxes' mail copies, the review's other copies, the three private channels rev3 added) | Claire holds her own copy of each mail and the event; she is a member of #zm-animations, #company-internal and #zombie-match3d (check-sql PASS: 0 load-bearing rows not visible, `C09ATAJ220H/1758823964.738872` YES); every base record is can-see YES (§5a) | holds |
| Feasibility / ACL | Strongest counter: Julia is not on the art team, so she cannot be assigned | `usr_8140f09bf9f1b94c` is active and has `tmem_team_ART_usr_8140f09bf9f1b94c` (linear data.json via `Task_Authoring/tools/hg.py`); `linear_update_issue` took an assignee email in the pre-check (`Working_Files/run_forensics/rev2/precheck/calls.jsonl`) | holds |
| Feasibility / ACL | Strongest counter: "so they can comment" needs a comment role the catalog may not support | `gdrive_share_file` took `role: "commenter"` 12 of 12 times in the pre-check (`Working_Files/run_forensics/rev2/precheck/calls.jsonl`); writer is also accepted (§4b) | holds |
| Contrived register | Strongest counter: listing five writes in one sentence reads as a deliverable spec sheet, or a "Then" reads as a step list | the writes are the requester's own list (the ask `C06DJBJL798/1759269913.882683`), one destination each, no column, wording or rule; no First / Then / Finally word (`Evals/references/rules/common_errors.md` §3; draft v1's "Then" removed) | holds |
| Contrived register | Strongest counter: "everything that's live today" hints at the off-sheet creatives | it is Leonard's own scope ("go through everything that's live today", `C06DJBJL798/1759269913.882683`) and names no item or source (`prompt_qc_cases.json` control-symptom) | holds |
| Contrived register | Strongest counter: with rev3 the prompt must now hint at the carriers or the task is a riddle; or, it already does through "whoever's making them" | the words were there before rev3 and name a field, not a person; §9's scan finds none of the rule words; the hardening report found no prompt-side defect (`Working_Files/01a_Hardening_Report.md` §11) | holds |

2. Mechanics: every §2, §4, §5, §7 and §10 row carries a locator; the root cause appears only in §5; the persona search outputs are pasted; the fixes are routed, not worked around.

Unresolved: none for the brief. Evidence limit: no run has yet assigned a ticket to Julia Lawson's account (§12); the search ordering in §5a is rev2 run evidence, not a rev3 measurement.

```
STAGE GATE prompt-writing: PASS — Task_Authoring/task_inputsN2 · 04_Prompt_Writing_Brief.md#95dd25fe8fd3 · 00_Assigments.md#6a3ab458705a · 01_Grounding_Dossier.md#c6af9569529d · 01_Universe_Inject.sql#0a08dedecd60 · 03_Error_Async_Config.txt#f93796afbb9e · 01a_Hardening_Report.md#b39c57050122 · __context__#215120f48d25 · __assignment__#fb0a0d31ccbc · __policy__#dc4ab5df3cdd · __gate_policy__#f8638415ca2c · __review__#623705ef238d · blocking 0 · warnings 0 · checks 24
[PASS] assignment.v3_context: Claire Morgan / Art Lead; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Writing_Brief.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql, 03_Error_Async_Config.txt, 01a_Hardening_Report.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#0a08dedecd60, 01_Hardness_Manifest.json#a1d69c31fa21, 01_Grounding_Dossier.md#c6af9569529d, solver/solver.py#debf4347f85a, 01c_Dispositions.json#1e36d090cbb4, 01c_Preflight_Report.json#c050112218fe, 00_Assigments.md#6a3ab458705a, 01_Scenario_Design.md#220b3403cb4c, 01_Hardness_Manifest.draft.json#014850c608bc, 01_Gradable_Surface.json#054fd42a239c, __context__#215120f48d25, __assignment__#fb0a0d31ccbc, __policy__#dc4ab5df3cdd, __gate_policy__#f8638415ca2c, __review__#98dc80681d27)
[PASS] chain.error-async: upstream 'error-async' PASS pasted and current (03_Error_Async_Config.txt#f93796afbb9e, 00_Assigments.md#6a3ab458705a, 01_Grounding_Dossier.md#c6af9569529d, 01_Universe_Inject.sql#0a08dedecd60, __context__#215120f48d25, __assignment__#fb0a0d31ccbc, __policy__#dc4ab5df3cdd, __gate_policy__#f8638415ca2c, __review__#98dc80681d27)
[PASS] structure.sections: 14 required sections present and non-empty (04_Prompt_Writing_Brief.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Writing_Brief.md
[PASS] evidence.situation: 1/1 items carry a source pointer (min 100%)
[PASS] evidence.final_state: 42/42 items carry a source pointer (min 100%)
[PASS] evidence.discovery_map: 37/37 items carry a source pointer (min 100%)
[PASS] evidence.dates: 22/22 items carry a source pointer (min 100%)
[PASS] evidence.entity_traps: 11/11 items carry a source pointer (min 100%)
[PASS] tool.search_as_persona: 43 facts proven findable by persona_view search as claire_morgan
[PASS] reach.brief: 57 scoped load-bearing ids YES for claire_morgan
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] structure.accepted_outcomes: V3 accepts multiple fair outcomes; see v3.fair_outcomes_review
[PASS] boundary.anchor_naming: 1 anchor-naming entry, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 16 evidenced counter-readings (of 17 found; need ≥ 6) in 04_Prompt_Writing_Brief.md
[PASS] review.coverage: self-review addresses all 6 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.fair_outcomes_review: current accepted outcomes and considered alternatives recorded; multiple fair outcomes are allowed
[PASS] handoff.pasted: pasted into the Self-review by --paste
```
