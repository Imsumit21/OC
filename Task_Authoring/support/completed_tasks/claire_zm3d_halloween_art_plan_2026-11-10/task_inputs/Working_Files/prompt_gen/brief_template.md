# Prompt Brief — claire-zm3d-halloween-art-plan · prep

> Built 2026-11-06 from `00_Assigments.md`, `Working_Files/00_Task_Context.json`, `Working_Files/01_Grounding_Dossier.md` (incl. Facts for the human), `01_Universe_Inject.sql` (sha256 @@SQL_SHA@@, revision rev3: 233 INSERT, 5 UPDATE), `03_Error_Async_Config.txt` (Friction: none), `Working_Files/01a_Hardening_Report.md` (§10, §11, S0r outcome), `Working_Files/scenario_gen/apply_rev3.py`, `Working_Files/solver/truth.json`, `Working_Files/01_Scenario_Design.md`, `Working_Files/01_Hardness_Manifest.json`, `Working_Files/scenario_gen/rubric_only_facts.json`, `Evals/references/tools/catalog.json` · Persona view verified: all (check-sql PASS, 0 load-bearing rows not visible; base records can-see YES) · no reference files (`02_Reference_Files/` holds only its README)
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

@@DISCOVERY_MAP@@

## 5a · Search-as-persona proof

Thirty-seven §5 facts, one row each, in §5 order, all re-run 2026-11-06 on SQL sha256 @@SQL_SHA@@ by `Working_Files/prompt_gen/run_research.py`. Each row is `persona_view.py search claire_morgan <service> "<query>" --limit 10` (`--no-hidden` on Gmail).

**What the tool can and cannot show.** `persona_view.py search` reads the base universe only and never the SQL: "cheer fastcouch" returns 0 visible hits although the SQL holds Marcus's post and his IM reply under those words. So a seeded record is never a persona_view hit. Each seeded row is proven three ways instead: the same query against the SQL read as text (the OVERLAY blocks below, every word of the query, any case; the SQL is never executed), `persona_view.py check-sql claire_morgan 01_Universe_Inject.sql --load-bearing Working_Files/injection_gen/load_bearing_ids.txt` (verdict @@CHECK_SQL@@, 0 load-bearing rows not visible) and, where one exists, a base record the search does return that leads to it (the thread root, the card, the channel). Base records are proven by their rank in the run and by `can-see`.

**Ordering, which the tool does not model.** `persona_view.py` lists hits by channel and shard, so a bare `Unity` looks like a flood from 2023. The product does not: in the rev2 pre-check the run's Slack search returned newest first (`Working_Files/run_forensics/rev2/precheck/calls.jsonl` event 217, the ask then Martin's Sep 30 post), Gmail too (event 17, the Sep 30 mail, then Sep 12), and `trello_search` returned comment actions as well as cards (event 43, comment `68dc65a0f2d7fb28743f5860`). This is run evidence about the old universe, not a measurement on rev3.

@@SAP_TABLE@@

**What a `halloween` search does to the six carriers.** None of the six is reached: no carrier's text holds the word, in base or in the SQL. This is by design (`Working_Files/01a_Hardening_Report.md` §10): the rev2 run swept `halloween` on Slack, Drive and Gmail (`calls.jsonl` events 215, 217, 219) and that sweep is what these records now sit off. The natural search is the creative's name, `Unity` or the channel, per the table above.

@@SAP_HALLOWEEN@@

Pasted persona_view outputs (verbatim: every row above, the `halloween` runs, the can-see and check-sql lines; one fence per run, overlay blocks beside the run they answer):

@@SAP_RAW@@

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
- Result of the scan: @@MUST_NOT@@
- People-as-sources that point at hidden evidence: Frederick's plan, Marcus's DM, Robert's deck, Martin's export, Arthur's calendar (the ask already names its sources; the prompt does not repeat them).
- Friction: none configured (`03_Error_Async_Config.txt`); nothing to announce, and Unity's manual review is a story fact, not a tool wait. Reference files: none, no `/app/artifact` path.
- Form: markdown, bullets, numbered steps, column lists, per-deliverable content specs, format rules, the words First / Then / Finally (`Evals/references/rules/common_errors.md` §3 search hits), answer-key clauses, hedges ("if my date is off …").

## 10 · Entity traps

Pasted `entity.py collisions` and `entity.py resolve` output (verbatim):

@@ENTITY_RAW@@

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

Rev3 (`/create-hardening` MODE B moves 1–6, `Working_Files/01a_Hardening_Report.md` §10, §11, S0r outcome; `Working_Files/scenario_gen/apply_rev3.py`): the universe changed, not the prompt. The report found no prompt-side defect, and `04_Prompt.txt` stays byte-identical (sha256 63d7c071…). Scenario, injection, hardening and error-async gates PASS on SQL sha256 @@SQL_SHA@@.

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
