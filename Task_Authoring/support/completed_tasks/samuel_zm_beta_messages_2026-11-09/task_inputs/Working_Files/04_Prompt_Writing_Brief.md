# Prompt Brief — samuel_zm_beta_messages · prep
> Built 2026-11-05 from 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql (sha256 6d162cfd1032, rev6), 01_Scenario_Design.md, 01_Hardness_Manifest.json, 03_Error_Async_Config.txt (Friction: none). No reference files. Persona view verified: all
> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human.
> **Clock:** 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Samuel's today is Wed Oct 1, 2025. The latest seeded event is Leonard's DM D06L58XCVKK/1759264851.763895 (2025-09-30T20:40:51Z, Tue Sep 30, 1:40 PM PT). Seed bound 2025-10-01T00:00:00Z.

## 1 · Assignment fit

Raw assignment: Business Function Design · Persona Samuel Turner, Role: Game Designer · Competency Marketing and GTM · Task Skill Retrieval · Task Type long-horizon · Difficulty Mode medium · Universe Date Oct 1, 2025.

| Axis | Assigned value | What it requires here (cited) |
|---|---|---|
| Business function | Design → Product & Design (`Evals/references/rules/task_categories.md`: product decisions, gameplay and design requirements) | a designer's call on what the game says to players, by the rule Leonard wrote; the requirement decisions are the plan's Call and Audience columns |
| Persona / role | Samuel Turner, samuel.turner@harmonygames.co, Game Designer (roster `samuel_turner`) | Voice: an ordinary colleague request, clean spelling. Remit: Leonard sent him the sheet (D06L58XCVKK/1750138057.452159), the roadmap card reads '[Feature] Push Notifications - Samuel + Leonard' (6851a769c65dc0017a227bb7), he authored harmonygames-Games/match3d#248. Read scope: DMs with Leonard, Vincent, Robert, Arthur; #zombie-match3d C0880U9751A, #zombie-bugs C08R27X0EAH, #zombie-art C08R8CHB0QL, #company-internal C05KNDCHAAG; not #executives C07C2866011 |
| Competency | Marketing and GTM (taxonomy screen 7: demand and retention, GTM, communications; outputs: memos, spreadsheets, emails) | the job is what players hear and when, to protect D1 and D7 before more money goes behind beta (D06L58XCVKK/1759264851.763895): a retention communications plan plus a team note with the warehouse baseline; a Designer is a listed typical persona. Open risk: most writes are on Linear |
| Task skill | Retrieval (find and return specific information across connectors, extracting structured values) | each message's facts come from the sheet, its ticket and comments, the roadmap lists, PR #248 and Slack, assembled into the plan; stacked: Analysis and Synthesis (the rule's ordered tests), Actions (ticket comments and moves, checklist, emails) |
| Task type / tier | long-horizon → Long Horizon 100–500+; requester bar: over 130 counted calls per run, corrected average under 80% | 12 services carry weight; volumes: 32 message tickets each read and written, 36 plan rows, 8 emails; manifest call budget 202 (01_Hardness_Manifest.json), `HARDNESS GATE (extreme): PASS` in the dossier |
| Difficulty mode / date | medium (cap 85%); Oct 1, 2025 | nothing on or after Wed Oct 1 00:00 PT may be described as done |

## 2 · Situation

| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |
|---|---|---|---|
| Leonard wants one straight answer on what the game actually says to players before more money goes behind beta, and doesn't trust the sheet's six Ready | Samuel, in his DM with Leonard | D06L58XCVKK/1759264851.763895 | — |
| The sheet's two status columns are from June and disagree on four of 14 rows | Samuel, on the PN sheet | f_a325dd4af80afc5994d5dc (tab PNs Beta, last changed 2025-06-23T07:02:43Z) | — |
| Tickets for the messages sit under one parent, six Done and the rest In Review, and people have added asks | Samuel, in Linear | DES-314 | — |
| A readiness deck and a channel post both repeat the six | Samuel | f_de7a1ae20201816a67750d, C0880U9751A/1758909739.853209 | — |
| The iOS prompt debate of Sep 23 | not Samuel | #executives C07C2866011/1758659424.324079 | Samuel is not a member; his visible records are C08R27X0EAH/1758265279.763959 and the Sep 29 post with its reply |

No cause belongs in the situation. Why the obvious reading is wrong is discovery-only (§5, never in the prompt).

## 3 · Investigation → action

Questions to resolve (no answers here):
1. What is on the list: every sheet row and every ask for a new phone message filed on a ticket or card, and what stays off?
2. For each message, which of the rule's ordered tests does it pass, and where does it stop?
3. What does the client actually schedule, and on which days?
4. What counts as reaching a player and as Vincent having seen it?
5. What is the latest line for each message that goes, and does the client ship it?
6. Who is each message for?
7. Which ask already has a ticket under another name, and which has none?
8. What happens to a ticket after its call, and has that rule changed?
9. What were D1 and D7 for the Sep 15 cohort week on each platform, which lapsed reminders does the client schedule by day, and what is in the client but still on Hold?

Writes they feed: W1 plan sheet (1–7) → W2 team note (3, 4, 9) → W3 ticket comments (2, 7) → W4 ticket moves (2, 8) → W5 new tickets (5, 7) → W6 checklist (2) → W7 emails to askers (1, 2) → W8 counts to Leonard (W1). No write is a bolt-on: Leonard's DM asks for each.

## 4 · Pinned final state (UGT anchor)

| Deliverable | Required contents (requirements) | Destination (exact) | Recipient(s) (exact) | Catalog write (reference only; never in the prompt) | Fed by |
|---|---|---|---|---|---|
| W1 plan sheet | one row per message, 36 rows; columns Message, Ticket, Call, What's missing, Audience, Final headline, String change; Go 2, Hold 28, Drop 6 | Samuel's Drive folder d_caafeec2804b3a67ce46aa | — | gsheets_create_spreadsheet, gsheets_values_update, gdrive_move_file if needed | D06L58XCVKK/1759264851.763895, f_dc45e0e5a8b8635c1b82b2, f_a325dd4af80afc5994d5dc |
| W2 team note | one page: D1 and D7 for the Sep 15 cohort week, iOS and Android separately; the lapsed reminders the client schedules by day; anything the client already schedules that's still a Hold and why | next to the plan in d_caafeec2804b3a67ce46aa | the team | gdocs_create_document | D06L58XCVKK/1759264851.763895, wh_USER_COHORT_RETENTION, harmonygames-Games/match3d#248 |
| W3 ticket comments | the call as a comment on each of the 32 message tickets, Go ones included | DES-313, DES-315 to DES-345 | — | linear_create_comment | D06L58XCVKK/1759264851.763895, f_dc45e0e5a8b8635c1b82b2 |
| W4 ticket moves | Drop to Canceled (6); Hold to Backlog, unassigned (24 with tickets); Go stay as they are (2) | the same tickets | — | linear_update_issue | f_dc45e0e5a8b8635c1b82b2, 68dae8c7d95e24b55b69bf80 |
| W5 new tickets | one for each of the four asks with no ticket; one string ticket for the changed line, under DES-314 | Linear team_DES | — | linear_create_issue | D06L58XCVKK/1759264851.763895, f_dc45e0e5a8b8635c1b82b2, cmt_f1b8a109dfa70cdc4565, cmt_2b519285937e7fa79453, cmt_eabac5435f2b3a575aad, cmt_e2e2926a2080ca53c4ea, evt_f2c03e69f50acf62c9d1c3 |
| W6 checklist | a checklist with the 2 Go messages | the push notifications card 6851a769c65dc0017a227bb7 | Vincent ticks it | trello_create_checklist, trello_create_check_item | D06L58XCVKK/1759264851.763895 |
| W7 emails | one email per person who asked, saying what happened to their asks | mail | brian.foster@harmonygames.co, calvin.price@harmonygames.co, douglas@harmonygames.co, julia.lawson@harmonygames.co, martin.walsh@harmonygames.co, oliver.brooks@harmonygames.co, owen.baker@harmonygames.co, robert@harmonygames.co | gmail_send_message | D06L58XCVKK/1759264851.763895 |
| W8 counts | how many Go, Hold and Drop | Leonard's DM D06L58XCVKK | leonard.hayes@harmonygames.co | slack_send_message or slack_conversations_add_message | D06L58XCVKK/1759264851.763895 |

| Decision-ambiguity risk | Alternative a careful run could take | What pins it |
|---|---|---|
| which tab | PNs or PN BETA Translated as well | the DM names the PNs Beta tab (D06L58XCVKK/1759264851.763895); the others hold Domino copy (f_a325dd4af80afc5994d5dc) |
| which sheet | Push Notifications Domino Adventure, which also has a PNs Beta tab | the DM's sheet is the Zombie Match one with six Ready; f_351b98dfb06f61fb8357d0 has no Ready column |
| what counts as an ask | Slack asks too, or red dots and in-game popups | the DM says filed on a ticket or a card; the rule doc defines a message as what reaches a closed phone (f_dc45e0e5a8b8635c1b82b2) |
| a second ticket for Win & Collect | file a new one because no child of the parent has that name | the DM's 'under whatever name'; page_liveops_calendar maps the names; DES-313 carries it |
| Done tickets on Hold rows | leave them Done | the rule doc says Hold tickets move (f_dc45e0e5a8b8635c1b82b2); only Go tickets stay as they are |
| Hold state | Todo, as the rule doc's last sentence says | the doc's 'unless the roadmap says otherwise' and Leonard's later card note 68dae8c7d95e24b55b69bf80 |
| base tickets holding the asks | move ZOM-542 or ZOM-556, or leave the call there | they are not message tickets; the new tickets take the call (DM: 'Anything with no ticket gets one') |
| who gets email | Leonard too, or one group mail | the DM says 'Email each person who asked for something, apart from me' (D06L58XCVKK/1759264851.763895); he hears on Slack |
| the note's scope | every message still in the client, a total count, or the warehouse's server campaigns | the DM asks for the lapsed reminders the client schedules by day and the Holds already in the client (D06L58XCVKK/1759264851.763895); no total is graded, and nothing in the note reads the push stats table |
| where counts go | a channel, or the sheet only | 'tell me here' in D06L58XCVKK/1759264851.763895 |

### 4b · Canonical outcome (all fair outcomes)

| Deliverable | Field | Fixed value (or closed accepted set, with sources) | Delegated by | Allowed equivalence class | Material / representational |
|---|---|---|---|---|---|
| W1 | location | final parent d_caafeec2804b3a67ce46aa | — | created there or moved there | material |
| W1 | name | a name about beta messages (no name set in D06L58XCVKK/1759264851.763895) | — | any name carrying beta, message, PN or player | representational |
| W1 | header | Message · Ticket · Call · What's missing · Audience · Final headline · String change (D06L58XCVKK/1759264851.763895) | — | same seven names, same order | material |
| W1 | membership | exactly these 36 (D06L58XCVKK/1759264851.763895): Achievement reward waiting; Axe Arena; Boss Arena attempts refilled; Boss Arena last hours; Boss Arena open; Comeback gift; Daily chest ready; Daily gift about to reset; Endless entries back; Endless weekly result; Finish first mission; Free shop coins ready; Hourly Coins; Infinite lives ending; Lapsed 1 day; Lapsed 14 days; Lapsed 3 days; Lapsed 30 days; Lapsed 7 days; Lives recharged; Login Calendar update; Nathan's Treasure Hunt; New levels added; Plague Race; Plague Race last hour; Plague Race result; Quests rollover; Season Pass last 48 hours; Season Pass premium nudge; Season Pass start; Streak Fever; Support reply waiting; Teammate sent lives; Weekly Leaderboard reset; Win & Collect start; Zombie Lane reward ready | — | record spelling or obvious short forms; a row may use the sheet's or the ticket's name | material |
| W1 | excluded | Cards and shop red dots; Mini-game lives ready; Mini-games discover; Permission popup; Plague Race red dot; Rate Us popup; Tiledozer and Luckydrop coins (f_dc45e0e5a8b8635c1b82b2: a message reaches a closed phone; D06L58XCVKK/1759264851.763895: the PNs Beta tab) | — | absent | material |
| W1 | Call = Go | Lapsed 1 day; Lapsed 7 days (rule: f_dc45e0e5a8b8635c1b82b2) | — | Go (D06L58XCVKK/1759264851.763895) | material |
| W1 | Call = Drop | Axe Arena; Comeback gift; Hourly Coins; Lapsed 14 days; Nathan's Treasure Hunt; Streak Fever (rule: f_dc45e0e5a8b8635c1b82b2) | — | Drop | material |
| W1 | Call = Hold | the other 28: Achievement reward waiting; Boss Arena attempts refilled; Boss Arena last hours; Boss Arena open; Daily chest ready; Daily gift about to reset; Endless entries back; Endless weekly result; Finish first mission; Free shop coins ready; Infinite lives ending; Lapsed 3 days; Lapsed 30 days; Lives recharged; Login Calendar update; New levels added; Plague Race; Plague Race last hour; Plague Race result; Quests rollover; Season Pass last 48 hours; Season Pass premium nudge; Season Pass start; Support reply waiting; Teammate sent lives; Weekly Leaderboard reset; Win & Collect start; Zombie Lane reward ready (rule: f_dc45e0e5a8b8635c1b82b2) | — | Hold | material |
| W1 | What's missing, not scheduled | Achievement reward waiting; Boss Arena attempts refilled; Boss Arena last hours; Boss Arena open; Daily chest ready; Daily gift about to reset; Endless entries back; Free shop coins ready; Infinite lives ending; Lapsed 3 days; Lapsed 30 days; Login Calendar update; Plague Race last hour; Quests rollover; Season Pass last 48 hours; Season Pass start; Win & Collect start; Zombie Lane reward ready (Arthur's notes on the tickets; harmonygames-Games/match3d#248) | — | any wording saying the client doesn't schedule it, or test 3 | material |
| W1 | What's missing, server | Endless weekly result; New levels added; Plague Race result; Season Pass premium nudge; Support reply waiting; Teammate sent lives (Arthur's notes, e.g. on DES-335) | — | any wording saying it needs a server send, or test 2 | material |
| W1 | What's missing, the four designed rows | Finish first mission: cannot reach its players (C0880U9751A/1759170096.924778); Plague Race: not seen on both platforms (D06UFE81RF0/1759174846.723833); Lives recharged: not seen on both platforms (C0880U9751A/1759245146.720608); Weekly Leaderboard reset: fires on the wrong day (harmonygames-Games/match3d#248#rc_18) | — | any wording naming that gap, with or without the test number | material |
| W1 | What's missing, covered | Lapsed 14 days names what covers it: Lapsed 7 days, the weekly batch (samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com>); other Drop rows blank or a short reason | 'then name that message' (rule doc) | either name of the message | material |
| W1 | Final headline | Go rows only (f_dc45e0e5a8b8635c1b82b2): Lapsed 1 day 'The Horde Is Growing…'; Lapsed 7 days 'Your Squad Is Waiting' (evt_f2c03e69f50acf62c9d1c3) | — | with or without the emoji (rule doc: emoji don't count); blank on other rows | material |
| W1 | String change | Lapsed 7 days Yes (evt_f2c03e69f50acf62c9d1c3); Lapsed 1 day No; blank on other rows (f_dc45e0e5a8b8635c1b82b2) | — | yes/no or true/false | material |
| W1 | Audience | who the ask says it's for, from each ticket's comment (f_dc45e0e5a8b8635c1b82b2); e.g. Boss Arena open: players past the arena unlock (DES-330); Plague Race result: players in a race (DES-335) | — | the asker's words or a plain rewording; narrowing to players who have been asked is also fair on Go rows | representational |
| W1 | Ticket | the row's ticket; Win & Collect start = DES-313 (page_liveops_calendar); the four asks with no ticket carry their new ticket's key | — | key alone or with a title | material |
| W2 | location | final parent d_caafeec2804b3a67ce46aa | — | created there or moved there | material |
| W2 | baseline | iOS D1 31.65, D7 9.28; Android D1 37.86, D7 10.68 (wh_USER_COHORT_RETENTION, cohort_week 2025-09-15, zombie_match_3d) | — | each platform on its own, because the DM says separately; rounded to one decimal, with or without % | material |
| W2 | lapsed ladder | reminders on days 1, 7, 14, 21 and 28 (harmonygames-Games/match3d#248) | — | any wording giving those days; the note may add the race and leaderboard messages as long as it marks which are lapsed reminders; either the line shipping today or the final headline | material |
| W2 | built but held | exactly four: Lives recharged, not seen on both platforms (C0880U9751A/1759245146.720608); Finish first mission, its players have not had our own ask (C0880U9751A/1759167608.326578, C0880U9751A/1759170096.924778); Plague Race, not seen on both platforms (D06UFE81RF0/1759174846.723833); Weekly Leaderboard reset, fires on the wrong day (harmonygames-Games/match3d#248#rc_18) | — | any wording naming the four with why, in step with the plan's What's missing; a caveat about the push stats table is not penalised | material |
| W3 | comments | the call on DES-313 and DES-315 to DES-345; the reason for each Hold on the four designed rows | — | any wording carrying the call | material |
| W4 | Drop | DES-324, DES-325, DES-326, DES-327, DES-344, DES-345 to Canceled (f_dc45e0e5a8b8635c1b82b2) | — | Canceled | material |
| W4 | Hold | DES-313, DES-315, DES-318, DES-319, DES-320, DES-321, DES-322, DES-323, DES-328, DES-329, DES-330, DES-331, DES-332, DES-333, DES-334, DES-335, DES-336, DES-337, DES-338, DES-339, DES-340, DES-341, DES-342, DES-343 to Backlog, unassigned (68dae8c7d95e24b55b69bf80) | — | Backlog; on the four Done Holds, Todo still shows the call was found | material |
| W4 | Go | DES-316, DES-317 stay as they are (f_dc45e0e5a8b8635c1b82b2) | — | comment only | material |
| W5 | new tickets | one per ask: Boss Arena attempts refilled (cmt_f1b8a109dfa70cdc4565); Daily gift about to reset (cmt_2b519285937e7fa79453); Teammate sent lives (cmt_eabac5435f2b3a575aad); Infinite lives ending (cmt_e2e2926a2080ca53c4ea); plus one string ticket carrying 'Your Squad Is Waiting' under DES-314 | — | any title; team DES or ZOM for the four asks; any state and assignee for the string ticket, Backlog or unset for the four asks | material |
| W6 | checklist | Lapsed 1 day, Lapsed 7 days on 6851a769c65dc0017a227bb7 | — | any checklist name; item text with the message name | material |
| W7 | recipients | brian.foster@harmonygames.co, calvin.price@harmonygames.co, douglas@harmonygames.co, julia.lawson@harmonygames.co, martin.walsh@harmonygames.co, oliver.brooks@harmonygames.co, owen.baker@harmonygames.co, robert@harmonygames.co; not Leonard (D06L58XCVKK/1759264851.763895) | — | one email each, as the DM says; a second mail to the same person is harmless | material |
| W7 | content | that person's asks and their calls: Brian: Endless entries back, Endless weekly result, Season Pass premium nudge, Comeback gift, Boss Arena attempts refilled; Calvin: Daily chest ready, Infinite lives ending, Win & Collect start; Douglas: Teammate sent lives; Julia: Plague Race last hour, Plague Race result, New levels added, Daily gift about to reset; Martin: Free shop coins ready; Oliver: Season Pass last 48 hours; Owen: Zombie Lane reward ready, Achievement reward waiting, Support reply waiting; Robert: Boss Arena open, Boss Arena last hours, Lapsed 14 days (D06L58XCVKK/1759264851.763895) | — | any wording | material |
| W8 | counts | Go 2, Hold 28, Drop 6 (D06L58XCVKK) | — | any wording with the three numbers | material |

## 5 · Discovery map

Root causes and corrections appear only here and are never in the prompt.

| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |
|---|---|---|---|---|---|---|
| F1 hub ask | scope, rule doc, plan columns, note, ticket writes, checklist, emails, counts | D06L58XCVKK/1759264851.763895 | YES (DM member) | met first | none | Yes: Leonard's DM from yesterday (A1) |
| F2 rule doc | six ordered tests; Go, Drop and Hold; audience, headline and string rules | f_dc45e0e5a8b8635c1b82b2 | YES (shared) | named by the hub; overturned in part by F9 | first-framing latch on the sheet flags | No |
| F3 GTM - Beta (decoy) | Domino Delights 2024 plan | f_ffbe775ff72a994c5d6b7c | YES (shared) | a search for beta plans; differs on the game | keyword collision | No |
| F4 PN sheet | 14 PNs Beta rows, six Ready, June copy | f_a325dd4af80afc5994d5dc | YES (shared) | met first; both status columns voided by F2 | reads as an answer | Yes: the Zombie Match PN sheet (A2) |
| F5 twin sheet (lookalike) | Domino copy with a PNs Beta tab | f_351b98dfb06f61fb8357d0 | YES (shared) | a search for 'Push Notifications'; no Ready column | near-duplicate | No |
| F6 parent ticket | the message tickets and asks | DES-314 | YES (unscoped) | named by the hub | the list looks complete | No |
| F7 QA note | seen only counts on a store build on real devices; a moved phone date is fine | samuel.turner@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com> | YES (To, INBOX) | named by the rule doc | none | No |
| F8 pass log | build behind each pass, both platforms on every row | f_8eb8c04713ff6a6ef4a265 | YES (shared) | named by the QA note; race row overturned by F16, Lives row by F44 | reads as settled | No |
| F9 the roadmap freeze | held tickets sit in Backlog, unassigned | 68dae8c7d95e24b55b69bf80 | YES (unscoped) | overturns the doc's Todo; on a card read only for its list | description of an unrelated card | No |
| F10 Minor Bugs card (decoy) | for bug tickets | 68c451141c69fb8af1b4568e | YES (unscoped) | a search for the BETA list | scope | No |
| F11 Robert's ask post | our own ask stays after level 20; the iOS popup stays | C0880U9751A/1759167608.326578 | YES (channel member) | latest of F13 to F15 | older posts come first | No |
| F12 Arthur's reply | only our own ask or the settings toggle schedules anything | C0880U9751A/1759170096.924778 | YES (channel member) | thread reply under F11 | rarely open a reply | No |
| F13 Robert, Jul 10 | move the ask to level 20 | D06KPMDV2JZ/1752162738.497679 | YES (DM member) | met first; overturned by F11 | stale | No |
| F14 variant C | pop up at level 13 on variant C | C08R27X0EAH/1755084279.518809 | YES (channel member) | met first; overturned by F11 | stale | No |
| F15 'at the beginning' | Leonard, Sep 19: PNs at the beginning on iOS | C08R27X0EAH/1758291802.756889 | YES (channel member) | met first; explained by F11 and F12 | reads as a contradiction | No |
| F16 Vincent's DM reply | that iPhone was on the timers build; on 0.3.40 it never showed up | D06UFE81RF0/1759174846.723833 | YES (DM member) | overturns cmt_fd950c410ed25c447c02 and F8 | thread reply under a build request | No |
| F17 build request root | Samuel's Android 2007 ask, the root of F16 | D06UFE81RF0/1759163970.141449 | YES (DM member) | the root a run opens | none | No |
| F18 line change | 'Your Squad Needs You Back' replaces the 'taken over' push | C08R8CHB0QL/1759169129.445834 | YES (channel member) | overturns the June line on the sheet and DES-317; overturned by F43 | reply under a theme post | No |
| F19 theme post root | Martin's desert theme post, the root of F18 | C08R8CHB0QL/1759159849.386619 | YES (channel member) | the root a run opens | none | No |
| F20 Arthur's inline comment | counts seven days from the last leave, not tied to the rollover | harmonygames-Games/match3d#248#rc_18 | YES (unscoped) | overturns Ready, Done and the approval | inline comments rarely opened | No |
| F21 PR #248 | the client schedule in its hunks, approved and merged | harmonygames-Games/match3d#248 | YES (unscoped) | named on the built tickets | approval reads as done | No |
| F22 GitHub mail thread | the notification thread, with the mail of F20 | samuel.turner@harmonygames.co/1836006988541924555 | YES (mailbox) | a second route to F20 | none | No |
| F23 cancelled ladder review | Leonard and Samuel, Sep 26, cancelled | evt_b56d5b19baa0a573da4553 | YES (own calendar) | supports F24 | reads as nothing | No |
| F24 cancellation mail | the weekly one repeats for four weeks, day 14 is already covered | samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com> | YES (INBOX) | overturns DES-344 as new work | the note is in mail only | No |
| F25 the name map | Collect & Win is Win & Collect under a different name | page_liveops_calendar | YES (unscoped) | joins row 7 to F26 | the raw search for 'Collect & Win' misses the stored '&amp;'; 'Collect' or 'under a different name' finds it | No |
| F26 the Collect & Win ticket | Calvin's ticket, no parent | DES-313 | YES (unscoped) | outside the parent's children | a name search for Win & Collect misses it | No |
| F27 Boss Arena ask | reminder once the daily attempts refill | cmt_f1b8a109dfa70cdc4565 | YES (unscoped) | one relation from DES-330 | comment on a home-screen ticket | No |
| F28 daily gift ask | reminder the evening before the streak resets | cmt_2b519285937e7fa79453 | YES (unscoped) | one relation from DES-338 | comment on a bug ticket | No |
| F29 Leonard on the comeback gift | a reward on tap is a version 2 idea | cmt_13477aa8d1468ae11c9d | YES (unscoped) | decides test 1 for DES-345 | none | No |
| F43 Leonard's copy note | 'Your Squad Is Waiting' replaces his Sep 29 line | evt_f2c03e69f50acf62c9d1c3 | YES (attendee) | overturns F18 | note on a calendar event | No |
| F44 Vincent's channel post | Full Ammo did not show on 0.3.49; he takes his tick off it | C0880U9751A/1759245146.720608 | YES (channel member) | overturns cmt_51e018b23e18c2f680cd and F8 | root post naming the headline, not the row | No |
| F45 Douglas's ask | a phone message when a teammate sends you lives; needs the server | cmt_eabac5435f2b3a575aad | YES (unscoped) | outside the parent | comment on a teams bug | No |
| F46 Calvin's ask | a reminder before infinite lives run out; local timer | cmt_e2e2926a2080ca53c4ea | YES (unscoped) | outside the parent | comment on an old lives bug | No |
| F47 list rename | BETA: Sep 30 renamed BETA: Oct 10 on Sep 30 | 68dc20c6d5fbf6ab70025295 | YES (unscoped) | agrees with the list's current name | none | No |
| F30 Leonard on the race | daily is fine, a race is always on | cmt_9338bb2c286a6c207792 | YES (unscoped) | settles test 5 for Plague Race | none | No |
| F31 readiness deck (decoy) | six Ready on the PN sheet | f_de7a1ae20201816a67750d | YES (shared) | repeats the sheet; voided by F2 | stale summary | No |
| F32 Brian's post (decoy) | send all the Ready ones | C0880U9751A/1758909739.853209 | YES (channel member) | not the rule's owner | non-authoritative | No |
| F33 in-game prompts | Rate Us and red dots are not phone messages | ZOM-397 | YES (unscoped) | keyword collisions, ruled out by F2 | over-inclusion | No |
| F34 roadmap lists | BETA, Oct 21 and Backlog lists decide test 1 | 6851a674975da1fe76e70d93 | YES (unscoped) | not on the ticket | per-feature join | No |
| F35 Axe Arena postponed | out of the beta, Sep 22 | C05KNDCHAAG/1758558164.541689 | YES (channel member) | agrees with the Oct 21 list | none | No |
| F36 beta scope post | beta scope, Sep 12 | C05KNDCHAAG/1757704290.799329 | YES (channel member) | context for F34 | none | No |
| F37 required versions | Android 0.3.127, iOS 0.3.40 | C0880U9751A/1758643365.607149 | YES (channel member) | shows the passes were on store builds | none | No |
| F38 warehouse baseline | iOS D1 31.65, D7 9.28; Android D1 37.86, D7 10.68 | wh_USER_COHORT_RETENTION (snowflake.json /tables/10) | YES (unscoped) | named by the hub; the OKR page differs (SC-28) | agent prompt does not advertise Snowflake; the hub says warehouse | No |
| F39 push notifications card | the card for the checklist, reopened Sep 24 | 6851a769c65dc0017a227bb7 | YES (unscoped) | named by the hub | none | Yes: a destination Samuel knows, in the hub's words, 'our push notifications card' |
| F40 Samuel's Drive folder | his root, writable | d_caafeec2804b3a67ce46aa | YES (owner) | named by the hub | none | Yes: my Drive folder (A3) |
| F41 askers' addresses | roster addresses, also on Linear users such as usr_fc22d5941b2aeb5c | brian.foster@harmonygames.co, usr_fc22d5941b2aeb5c | YES (unscoped) | Linear users and Contacts | none | No |

## 5a · Search-as-persona proof

`persona_view.py search` reads the base only; seeded hits are counted from the SQL rows Samuel can see, which dossier check-sql proves visible. One row per §5 fact. Scan output is in `plan/brief/search_out.txt`; decisive outputs are pasted below.

| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |
|---|---|---|---|---|---|---|
| F1 hub ask | slack | "one straight answer" | base 0; seeded 1 | n/a (--no-hidden) | D06L58XCVKK/1759264851.763895 | YES (seeded; check-sql YES) |
| F2 rule doc | gdocs | "message rule" | base 0; seeded 1 | 0 | f_dc45e0e5a8b8635c1b82b2 | YES (seeded; check-sql YES) |
| F3 GTM - Beta (decoy) | gdocs | "GTM - Beta" | base 1; seeded 0 | 0 | f_ffbe775ff72a994c5d6b7c | YES (base, hit 1 of 1) |
| F4 PN sheet | gsheets | "Push Notifications Zombie Match" | base 1; seeded 0 | 0 | f_a325dd4af80afc5994d5dc | YES (base, hit 1 of 1) |
| F5 twin sheet (lookalike) | gsheets | "Push Notifications Domino" | base 1; seeded 0 | 0 | f_351b98dfb06f61fb8357d0 | YES (base, hit 1 of 1) |
| F6 parent ticket | linear | "Beta player messages" | base 0; seeded 1 | 0 | DES-314 | YES (seeded; unscoped) |
| F7 QA note | gmail | "phone messages" | base 0; seeded 1 | n/a (--no-hidden) | samuel.turner@harmonygames.co/1843335316636662321 | YES (seeded; check-sql YES) |
| F8 pass log | gsheets | "Phone message checks" | base 0; seeded 1 | 0 | f_8eb8c04713ff6a6ef4a265 | YES (seeded; check-sql YES) |
| F9 the roadmap freeze | trello | "Held tickets" | base 0; seeded 1 | 0 | 68dae8c7d95e24b55b69bf80 | YES (seeded; unscoped) |
| F10 Minor Bugs card (decoy) | trello | "Minor Bugs to Fix" | base 10; seeded 0 | 0 | 68c451141c69fb8af1b4568e | YES (base, hit 1 of 10) |
| F11 Robert's ask post | slack | "Permission ask for beta" | base 0; seeded 1 | n/a (--no-hidden) | C0880U9751A/1759167608.326578 | YES (seeded; check-sql YES) |
| F12 Arthur's reply | slack | "switch anything on" | base 0; seeded 1 | n/a (--no-hidden) | C0880U9751A/1759170096.924778 | YES (seeded; check-sql YES) |
| F13 Robert, Jul 10 | slack | "shove it to level 20" | base 1; seeded 0 | n/a (--no-hidden) | D06KPMDV2JZ/1752162738.497679 | YES (base, hit 1 of 1) |
| F14 variant C | slack | "notification pop up is triggered at level 13" | base 2; seeded 0 | n/a (--no-hidden) | C08R27X0EAH/1755084279.518809 | YES (base, hit 2 of 2) |
| F15 'at the beginning' | slack | "PNs are at the beginning" | base 1; seeded 0 | n/a (--no-hidden) | C08R27X0EAH/1758291802.756889 | YES (base, hit 1 of 1) |
| F16 Vincent's DM reply | slack | "5-minute timers build" | base 0; seeded 1 | n/a (--no-hidden) | D06UFE81RF0/1759174846.723833 | YES (seeded; check-sql YES) |
| F17 build request root | slack | "could you help me test the build" | base 1; seeded 0 | n/a (--no-hidden) | D06UFE81RF0/1759163970.141449 | YES (base, hit 1 of 1) |
| F18 line change | slack | "taken over" | base 1; seeded 1 | n/a (--no-hidden) | C08R8CHB0QL/1759169129.445834 | YES (seeded; check-sql YES) |
| F19 theme post root | slack | "desert theme" | base 1; seeded 0 | n/a (--no-hidden) | C08R8CHB0QL/1759159849.386619 | YES (base, hit 1 of 1) |
| F20 Arthur's inline comment | github | "rollover" | base 0; seeded 1 | 0 | harmonygames-Games/match3d#248#rc_18 | YES (seeded; unscoped) |
| F21 PR #248 | github | "Push notification" | base 10; seeded 0 | 0 | harmonygames-Games/match3d#248 | YES (base, in the first 10) |
| F22 GitHub mail thread | gmail | "PR #248" | base 1; seeded 1 | n/a (--no-hidden) | samuel.turner@harmonygames.co/1836006988541924555 | YES (base thread, hit 1 of 1) |
| F23 cancelled ladder review | gcal | "ladder" | base 0; seeded 1 | 0 | evt_b56d5b19baa0a573da4553 | YES (seeded; check-sql YES) |
| F24 cancellation mail | gmail | "Lapsed ladder review" | base 0; seeded 2 | n/a (--no-hidden) | samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com> | YES (seeded; check-sql YES) |
| F25 the name map | confluence | "under a different name" | base 2; seeded 0 | 0 | page_liveops_calendar | YES (base, hit 1 of 2) |
| F26 the Collect & Win ticket | linear | "Collect" | base 10; seeded 2 | 0 | DES-313 | YES (seeded; unscoped) |
| F27 Boss Arena ask | linear | "Boss Arena" | base 10; seeded 3 | 0 | ZOM-542 | YES (seeded; unscoped) |
| F28 daily gift ask | linear | "daily gift" | base 9; seeded 2 | 0 | ZOM-556 | YES (seeded; unscoped) |
| F29 Leonard on the comeback gift | linear | "Comeback gift" | base 0; seeded 1 | 0 | DES-345 | YES (seeded; unscoped) |
| F43 Leonard's copy note | gcal | "Lapsed copy check" | base 0; seeded 1 | n/a (--no-hidden) | evt_f2c03e69f50acf62c9d1c3 | YES (seeded; check-sql YES) |
| F44 Vincent's channel post | slack | "Full Ammo" | base 0; seeded 1 | n/a (--no-hidden) | C0880U9751A/1759245146.720608 | YES (seeded; check-sql YES) |
| F45 Douglas's ask | linear | "teammate sends you lives" | base 0; seeded 1 | 0 | cmt_eabac5435f2b3a575aad | YES (seeded; unscoped) |
| F46 Calvin's ask | linear | "infinite lives are about to run out" | base 0; seeded 1 | 0 | cmt_e2e2926a2080ca53c4ea | YES (seeded; unscoped) |
| F47 list rename | trello | "BETA: Oct 10" | base 0; seeded 1 | 0 | 68dc20c6d5fbf6ab70025295 | YES (seeded; unscoped) |
| F30 Leonard on the race | linear | "Plague Race" | base 10; seeded 3 | 0 | DES-319 | YES (seeded; unscoped) |
| F31 readiness deck (decoy) | gslides | "Beta readiness" | base 0; seeded 2 | 0 | f_de7a1ae20201816a67750d | YES (seeded; check-sql YES) |
| F32 Brian's post (decoy) | slack | "send all the Ready ones" | base 0; seeded 1 | n/a (--no-hidden) | C0880U9751A/1758909739.853209 | YES (seeded; check-sql YES) |
| F33 in-game prompts | linear | "Rate us" | base 10; seeded 0 | 0 | ENG-1097 | YES (base; Domino rows come first, ZOM-397 by key) |
| F34 roadmap lists | trello | "Rewarded Ads" | base 8; seeded 0 | 0 | 68af7645b20c96f21f108ad7 | YES (base, in the first 8) |
| F35 Axe Arena postponed | slack | "postpone Axe Arena" | base 1; seeded 0 | n/a (--no-hidden) | C05KNDCHAAG/1758558164.541689 | YES (base, hit 1 of 1) |
| F36 beta scope post | slack | "Beta target" | base 1; seeded 0 | n/a (--no-hidden) | C05KNDCHAAG/1757704290.799329 | YES (base, hit 1 of 1) |
| F37 required versions | slack | "required versions" | base 1; seeded 0 | n/a (--no-hidden) | C0880U9751A/1758643365.607149 | YES (base, hit 1 of 1) |
| F38 warehouse baseline | snowflake | "USER_COHORT_RETENTION" (table list) | base 1; seeded 0 | 0 | wh_USER_COHORT_RETENTION | YES (base, read at /tables/10) |
| F39 push notifications card | trello | "Push Notifications" | base 6; seeded 2 | 0 | 6851a769c65dc0017a227bb7 | YES (base, hit 1 of 6) |
| F40 Samuel's Drive folder | gdrive | "samuel.turner" | base 1; seeded 0 | 0 | d_caafeec2804b3a67ce46aa | YES (base, own root) |
| F41 askers' addresses | contacts | "brian.foster" | base 1; seeded 0 | 0 | brian.foster@harmonygames.co | YES (base, hit 1 of 1) |

```
SEARCH gsheets 'Push Notifications Zombie Match' as samuel_turner  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_a325dd4af80afc5994d5dc", "name": "Push Notifications Zombie Match.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Push Notifications 
```

```
SEARCH gdocs 'GTM - Beta' as samuel_turner  scope: GDocs title + body_text
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_ffbe775ff72a994c5d6b7c", "name": "GTM - Beta.docx", "mime": "application/vnd.google-apps.document", "why": "file is shared with the persona (shared_with_emails)", "snippet": "GTM - Beta"}
```

```
SEARCH gdrive 'Push Notifications Zombie Match' as samuel_turner  scope: Drive file/folder names (on-disk file content is not searched)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_a325dd4af80afc5994d5dc", "name": "Push Notifications Zombie Match.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Push Notifications 
```

```
SEARCH slack 'required versions' as samuel_turner  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C0880U9751A/1758643365.607149", "channel": "zombie-match3d", "kind": "private", "date": "2025-09-23", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "<@EMPLOYEE_0031_SLACK_ID> can you update the match3d req
note: --no-hidden: containers outside the persona's view were not scanned
```

```
SEARCH slack 'desert theme' as samuel_turner  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C08R8CHB0QL/1759159849.386619", "channel": "zombie-art", "kind": "public", "date": "2025-09-29", "user": "EMPLOYEE_0033_SLACK_ID", "reply": false, "snippet": "HI guys! I'm preparing a *desert theme* for the *Endless Mode
note: --no-hidden: containers outside the persona's view were not scanned
```

```
SEARCH slack 'could you help me test the build' as samuel_turner  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "D06UFE81RF0/1759163970.141449", "channel": "D06UFE81RF0", "kind": "im", "date": "2025-09-29", "user": "EMPLOYEE_0004_SLACK_ID", "reply": false, "snippet": "Hi [PERSON_NAME_0050], could you help me test the build?  Androi
note: --no-hidden: containers outside the persona's view were not scanned
```

```
SEARCH gmail 'PR #248' as samuel_turner  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "samuel.turner@harmonygames.co/1836006988541924555", "last": "2025-06-26T21:23:53Z", "subject": "Re: [[SOURCE_ORG_0001]-Games/match3d] Push notification (PR #248)", "snippet": "Re: [[SOURCE_ORG_0001]-Games/match3d] Push n
note: --no-hidden: containers outside the persona's view were not scanned
```

```
SEARCH slack 'shove it to level 20' as samuel_turner  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "D06KPMDV2JZ/1752162738.497679", "channel": "D06KPMDV2JZ", "kind": "im", "date": "2025-07-10", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "Let's shove it to level 20"}
note: --no-hidden: containers outside the persona's view were not scanned
```

```
SEARCH slack 'PNs are at the beginning' as samuel_turner  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C08R27X0EAH/1758291802.756889", "channel": "zombie-bugs", "kind": "private", "date": "2025-09-19", "user": "EMPLOYEE_0038_SLACK_ID", "reply": true, "snippet": "Yeah PNs are at the beginning. I just downloaded from the Ap
note: --no-hidden: containers outside the persona's view were not scanned
```

## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · persona-readable · unique · instructions-not-answer) | Inferable |
|---|---|---|---|---|
| R1 population | D06L58XCVKK/1759264851.763895, f_a325dd4af80afc5994d5dc | deliverable: the plan Leonard asked for | D06L58XCVKK/1759264851.763895 · YES · the only such DM · states the scope, not the list | yes (incorporated through the hub) |
| R2 calls and audience | f_dc45e0e5a8b8635c1b82b2 | scope: do what Leonard's DM says | D06L58XCVKK/1759264851.763895 'make a call on each one using the message rule doc' · YES · one doc · rules, not answers | yes (incorporated through the hub) |
| R3 what's missing | f_dc45e0e5a8b8635c1b82b2, samuel.turner@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com> | same | f_dc45e0e5a8b8635c1b82b2 'name the test it failed'; 'What Vincent counts as seen is in his QA note' · YES · · rule only | yes (incorporated through the hub) |
| R4 final headline and string change | f_dc45e0e5a8b8635c1b82b2, C08R8CHB0QL/1759169129.445834 | same | f_dc45e0e5a8b8635c1b82b2 'the latest line I've called' · YES · · rule only | yes (incorporated through the hub) |
| R5 team note | D06L58XCVKK/1759264851.763895, wh_USER_COHORT_RETENTION | deliverable: the note | D06L58XCVKK/1759264851.763895 · YES · · names the contents, not the values | yes (incorporated through the hub) |
| R6 comments and new tickets | D06L58XCVKK/1759264851.763895, DES-313 | scope | D06L58XCVKK/1759264851.763895 'Leave the call as a comment on each ticket' · YES · · instruction | yes (incorporated through the hub) |
| R7 ticket moves | f_dc45e0e5a8b8635c1b82b2, 68dae8c7d95e24b55b69bf80 | scope | D06L58XCVKK/1759264851.763895 'move the ticket to match'; f_dc45e0e5a8b8635c1b82b2 · YES · · rule only | yes (incorporated through the hub) |
| R8 string ticket | f_dc45e0e5a8b8635c1b82b2 | scope | f_dc45e0e5a8b8635c1b82b2 'needs a string ticket under DES-314, because the strings are hard-coded, so open one when you make the call' · YES · · instruction | yes (incorporated through the hub) |
| R9 folder, checklist, emails, counts | D06L58XCVKK/1759264851.763895, 6851a769c65dc0017a227bb7 | destinations: my Drive folder, and the rest through the hub | D06L58XCVKK/1759264851.763895 · YES · · instruction | yes (incorporated through the hub) |

| Anchor | May be named (noun phrases only) | Record |
|---|---|---|
| A1 | Leonard's DM from yesterday; Leonard's DM | D06L58XCVKK/1759264851.763895 |
| A2 | the Zombie Match PN sheet; the PN sheet | f_a325dd4af80afc5994d5dc |
| A3 | my Drive folder | d_caafeec2804b3a67ce46aa |

Every graded requirement reaches the agent through A1, so the prompt only has to make Leonard's DM the job and name where the work lands. No gotcha needs its own trigger.

## 7 · Dates and constraints

| Item | Absolute date or value | Source | Past fact or deadline |
|---|---|---|---|
| Today | Wed Oct 1, 2025 | 00_Task_Context.json /universe/persona_today | clock |
| Leonard's DM | Tue Sep 30, 2025, 1:40 PM PT (2025-09-30T20:40:51Z) | D06L58XCVKK/1759264851.763895 | past fact; 'from yesterday' holds |
| Scope cut-off for asks | filed up to Sep 30, 2025 | D06L58XCVKK/1759264851.763895 | past fact |
| Cohort week | 2025-09-15 | wh_USER_COHORT_RETENTION | past fact |
| Rule doc | Sep 26, 2025 (2025-09-26T17:10:54Z) | f_dc45e0e5a8b8635c1b82b2 | past fact |
| Freeze note | Sep 29, 2025 (2025-09-29T20:15:03Z) | 68dae8c7d95e24b55b69bf80 | past fact, later than the rule doc |
| Sheet last changed | 2025-06-23T07:02:43Z | f_a325dd4af80afc5994d5dc | past fact |
| Beta date | not graded: the list reads BETA: Oct 10 and base actions read BETA: Sep 30 (SC-13) | 6851a674975da1fe76e70d93 | never name a beta date in the prompt |

## 8 · Difficulty levers

| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |
|---|---|---|---|---|
| Ambiguity | yes | yes | deciding facts sit in a PR inline comment (harmonygames-Games/match3d#248#rc_18), DM and channel thread replies (D06UFE81RF0/1759174846.723833, C08R8CHB0QL/1759169129.445834), the description of an unrelated card (68dae8c7d95e24b55b69bf80), a calendar note (evt_f2c03e69f50acf62c9d1c3), a channel post (C0880U9751A/1759245146.720608), comments on tickets about other things (cmt_f1b8a109dfa70cdc4565, cmt_2b519285937e7fa79453, cmt_eabac5435f2b3a575aad, cmt_e2e2926a2080ca53c4ea) | the prompt is clear about the ask and silent on where answers live; destinations are named |
| Dynamic change | yes | yes | superseded claims met first: the June line, the ticket pass, the doc's Todo, older ask points (T2, T4, T8, T9) | the prompt names neither the first summary's flaws nor the correction |
| Multi-source | yes | yes | 12 services (Slack, Sheets, Docs, Drive, Linear, Trello, GitHub, Gmail, Calendar, Slides, Confluence, Snowflake) | no source named as an exact artifact beyond A1 to A3 |
| Async | no | — | — | no wait configured (03_Error_Async_Config.txt: Friction: none) |
| Error recovery | no | — | — | no forced error |
| Access control | no | — | — | every deciding record is Samuel-visible (§5a); #executives C07C2866011 is not needed |

## 9 · Must not appear in the prompt

- Tool and server names (`Evals/references/tools/catalog.json`): gsheets_create_spreadsheet, gsheets_values_update, gdocs_create_document, gdrive_move_file, linear_list_issues, linear_list_comments, linear_create_comment, linear_update_issue, linear_create_issue, trello_create_checklist, trello_create_check_item, trello_get_comments, gmail_send_message, slack_send_message, slack_conversations_replies, github_get_pull_request_comments, github_get_file_contents, snowflake_execute_query; MCP server names.
- Ids and opaque names: any f_, d_ or evt_ id, thread or message id, Slack channel id or ts, DES or ZOM keys, card or list ids, cmt_ ids, PR numbers, NotificationManager.
- Root causes and findings (§5): Arthur's inline comment, Vincent's DM reply and channel post, Leonard's reply under the theme post and his calendar note, Robert's post and Arthur's reply, the freeze note, the cancelled review, the name map, the off-parent asks.
- The rules: the six tests, the Go, Hold and Drop definitions, what counts as seen, the headline, emoji and string rules, Canceled, Backlog or Todo.
- Any message name, count or value: 36 rows, Go 2, Hold 28, Drop 6, 32 tickets, 8 askers, 'Your Squad Is Waiting', the D1 and D7 figures, level 20, a beta date.
- The Snowflake table PUSH_NOTIFICATION_STATS or any wording that sends a run to it: it shows Firebase rows against Slack's 'All our PNs are local' (C08R27X0EAH/1758239520.618939), a base disagreement with no card. /prompt failed rev4 because the note asked who hears from us, so rev5's note asks nothing that table can answer. Oracle Events and rubric text for the five server rows say they fail test 2 and never say that no server push exists.
- An ask-only audience: players who switch messages on from settings also hear, so never say only asked players hear.
- The shape of sibling prompts (dataset-duplicate risk, memory prompt-dataset-duplicate-gate): 'take it off my plate', 'go through his ask and everything it points to', 'if his rules say something needs to happen on the tickets'.
- Markdown, numbered steps, per-deliverable content lists or format rules: they belong in Leonard's DM and the rule doc.

## 10 · Entity traps

```

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
  EMPLOYEE_0024: {'entities': ['scott <employee_0024@harmonygames.co>', '? <slack:EMPLOYEE_0024_SLACK_ID>', '? <trello:3d36d70154e6a715614e0d75>'], 'records': ['gcal.calendar_id=employee_0024@harmonyg
  EMPLOYEE_0032: {'entities': ['? <EMPLOYEE_0032_EMAIL>', 'Josh Dempsey <josh.dempsey@harmonygames.co>', '? <github:EMPLOYEE_0032_GITHUB_USERNAME>', '? <slack:EMPLOYEE_0032_SLACK_ID>'], 'records': ['c
  PERSON_2218: {'entities': ['? <PERSON_2218_EMAIL>', '? <github:PERSON_2218_GITHUB_USERNAME>'], 'records': ['linear.id=usr_PERSON_2218', 'linear.email=PERSON_2218_EMAIL', 'contacts.email=PERSON_2218_
  PERSON_2360: {'entities': ['? <PERSON_2360_EMAIL>', 'Claire <github:PERSON_2360_GITHUB_USERNAME>'], 'records': ['github.login=PERSON_2360_GITHUB_USERNAME', 'email.email=PERSON_2360_EMAIL']}
  PERSON_3233: {'entities': ['? <PERSON_3233_EMAIL>', '? <github:PERSON_3233_GITHUB_USERNAME>', '? <slack:PERSON_3233_SLACK_ID>'], 'records': ['linear.id=usr_PERSON_3233', 'linear.email=PERSON_3233_EM
  PERSON_3335: {'entities': ['? <PERSON_3335_EMAIL>', '? <slack:PERSON_3335_SLACK_ID>'], 'records': ['contacts.email=PERSON_3335_EMAIL', 'email.email=PERSON_3335_EMAIL', 'slack.id=PERSON_3335_SLACK_ID
  PERSON_3935: {'entities': ['? <PERSON_3935_EMAIL>', '? <slack:PERSON_3935_SLACK_ID>'], 'records': ['email.email=PERSON_3935_EMAIL', 'slack.id=PERSON_3935_SLACK_ID']}
  PERSON_5275: {'entities': ['? <PERSON_5275_EMAIL>', '? <slack:PERSON_5275_SLACK_ID>'], 'records': ['contacts.email=PERSON_5275_EMAIL', 'email.email=PERSON_5275_EMAIL', 'slack.id=PERSON_5275_SLACK_ID
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
  [ambiguous_name] github: mononym 'Claire' is an exact name of none and the first name of ['email:claire.morgan@harmonygames.co'] -> candidates ['email:claire.morgan@harmonygames.co']
  [ambiguous_name] trello: mononym 'Marcus' is an exact name of none and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co'] -> candidates ['email:marcus.benne
  [token_link] EMPLOYEE_0024: same token number across services but no shared exact email/name: not joined -> candidates ['email:employee_0024@harmonygames.co', 'slack:EMPLOYEE_0024_SLACK_ID', 'trello
  [token_link] EMPLOYEE_0032: same token number across services but no shared exact email/name: not joined -> candidates ['email:EMPLOYEE_0032_EMAIL', 'email:josh.dempsey@harmonygames.co', 'github:EMP
  [token_link] PERSON_2218: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_2218_EMAIL', 'github:PERSON_2218_GITHUB_USERNAME']
  [token_link] PERSON_2360: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_2360_EMAIL', 'github:PERSON_2360_GITHUB_USERNAME']
  [token_link] PERSON_3233: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3233_EMAIL', 'github:PERSON_3233_GITHUB_USERNAME', 'slack:PERSON_3
  [token_link] PERSON_3335: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3335_EMAIL', 'slack:PERSON_3335_SLACK_ID']
  [token_link] PERSON_3935: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3935_EMAIL', 'slack:PERSON_3935_SLACK_ID']
  [token_link] PERSON_5275: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_5275_EMAIL', 'slack:PERSON_5275_SLACK_ID']
  [token_link] PERSON_5360: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_5360_EMAIL', 'slack:PERSON_5360_SLACK_ID']

INTEGRITY FLAGS (2)
  {'type': 'id_with_space', 'service': 'linear', 'id': 'usr_Victor Barnes'}
  {'type': 'name_mismatch_on_email_join', 'service': 'github', 'id': 'PERSON_2314_GITHUB_USERNAME', 'detail': "GitHub PERSON_2314_GITHUB_USERNAME joined by email but shows name 'Ryan' (entity is Frede
ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
  persona: leonard_hayes - Co-founder & Creative Director / Executive
  slack      id=EMPLOYEE_0038_SLACK_ID, name=Leonard Hayes, real_name=Leonard Hayes, email=leonard.hayes@harmonygames.co, is_bot=False, deleted=False, messages=129898, first_post=2023-03-15, last_post
ENTITY email:vincent.parker@harmonygames.co  name=Vincent Parker  kind=person  emails=['vincent.parker@harmonygames.co']
  persona: vincent_parker - Game Systems Engineer / Engineering
  slack      id=EMPLOYEE_0012_SLACK_ID, name=Vincent Parker, real_name=Vincent Parker, email=vincent.parker@harmonygames.co, is_bot=False, deleted=False, messages=39854, first_post=2023-08-30, last_po
ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
  persona: robert - Co-Founder & Creative Director / Executive
  slack      id=EMPLOYEE_0016_SLACK_ID, name=Robert, real_name=Robert, email=robert@harmonygames.co, is_bot=False, deleted=False, messages=110334, first_post=2023-03-15, last_post=2025-10-01   [join: 
ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
  persona: arthur_blake - Co-founder & CTO / Executive
  slack      id=EMPLOYEE_0025_SLACK_ID, name=Arthur Blake, real_name=Arthur Blake, email=arthur.blake@harmonygames.co, is_bot=False, deleted=False, messages=35266, first_post=2023-03-20, last_post=202
ENTITY email:brian.foster@harmonygames.co  name=Brian Foster  kind=person  emails=['brian.foster@harmonygames.co']
  persona: brian_foster - Game Engineer / Engineering
  slack      id=EMPLOYEE_0026_SLACK_ID, name=Brian Foster, real_name=Brian Foster, email=brian.foster@harmonygames.co, is_bot=False, deleted=False, messages=28951, first_post=2024-06-06, last_post=202
ENTITY email:calvin.price@harmonygames.co  name=Calvin Price  kind=person  emails=['calvin.price@harmonygames.co']
  persona: calvin_price - Game Engineer (Unity VFX) / Engineering
  slack      id=EMPLOYEE_0006_SLACK_ID, name=Calvin Price, real_name=Calvin Price, email=calvin.price@harmonygames.co, is_bot=False, deleted=False, messages=12017, first_post=2023-03-29, last_post=202
ENTITY email:julia.lawson@harmonygames.co  name=Julia Lawson  kind=person  emails=['julia.lawson@harmonygames.co']
  persona: julia_lawson - Product Manager / Product
  slack      id=EMPLOYEE_0005_SLACK_ID, name=Julia Lawson, real_name=Julia Lawson, email=julia.lawson@harmonygames.co, is_bot=False, deleted=False, messages=31848, first_post=2023-07-16, last_post=202
ENTITY email:martin.walsh@harmonygames.co  name=Martin Walsh  kind=person  emails=['martin.walsh@harmonygames.co']
  persona: martin_walsh - Game Designer / Design
  slack      id=EMPLOYEE_0033_SLACK_ID, name=Martin Walsh, real_name=Martin Walsh, email=martin.walsh@harmonygames.co, is_bot=False, deleted=False, messages=7527, first_post=2023-08-28, last_post=2025
ENTITY email:oliver.brooks@harmonygames.co  name=Oliver Brooks  kind=person  emails=['oliver.brooks@harmonygames.co']
  persona: oliver_brooks - Senior Game Engineer / Engineering
  slack      id=EMPLOYEE_0003_SLACK_ID, name=Oliver Brooks, real_name=Oliver Brooks, email=oliver.brooks@harmonygames.co, is_bot=False, deleted=False, messages=13475, first_post=2024-08-12, last_post=
ENTITY email:owen.baker@harmonygames.co  name=Owen Baker  kind=person  emails=['owen.baker@harmonygames.co']
  persona: owen_baker - Game Engineer (Unity) / Engineering
  slack      id=EMPLOYEE_0021_SLACK_ID, name=Owen Baker, real_name=Owen Baker, email=owen.baker@harmonygames.co, is_bot=False, deleted=False, messages=14941, first_post=2023-09-15, last_post=2025-10-0
ENTITY email:samuel.turner@harmonygames.co  name=Samuel Turner  kind=person  emails=['samuel.turner@harmonygames.co']
  persona: samuel_turner - Game Designer / Design
  slack      id=EMPLOYEE_0004_SLACK_ID, name=Samuel Turner, real_name=Samuel Turner, email=samuel.turner@harmonygames.co, is_bot=False, deleted=False, messages=4586, first_post=2024-02-20, last_post=2
```

| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |
|---|---|---|---|
| Martin Walsh | Martin Lewis | Martin Lewis is an external contact; Martin Walsh filed DES-339 | martin.walsh@harmonygames.co |
| Julia Lawson | Peter Lawson | different people; Julia filed the race and levels asks | julia.lawson@harmonygames.co |
| Calvin Price | Nathan Price; Nathan's Treasure Hunt | Nathan's name survives only in a Domino event | calvin.price@harmonygames.co |
| Oliver Brooks | Lauren Brooks | different people | oliver.brooks@harmonygames.co |
| Owen Baker | Thomas Baker | different people | owen.baker@harmonygames.co |
| Push Notifications Zombie Match | Push Notifications Domino Adventure | the Domino sheet also has a PNs Beta tab but no Ready column | f_a325dd4af80afc5994d5dc |
| the PNs Beta tab | PNs; PN BETA Translated | Domino copy on the same sheet | f_a325dd4af80afc5994d5dc |
| Win & Collect start on DES-313 | Win & Collect on Domino Delights | same feature, ZM calls it Collect & Win | page_liveops_calendar |
| Boss Arena | Infinite HP Boss Mode | the board's card name for the same mode | ZOM-550 |
| ZM ROADMAP board | DD Product Roadmap; Harmony Games | other boards; the rule doc names ZM ROADMAP | 6851a769c65dc0017a227bb7 |

Task-side checks: the prompt uses first names only where the roster has one active person of that name (Leonard, Vincent); `references/universe_kb/trap_catalog.json` N01 to N03 do not apply, because no key series or lookalike channel is named in the prompt.

## 11 · Pre-submit checklist

- [ ] Persona voice: an ordinary request from Samuel to his assistant; clean spelling; no spec-sheet layout
- [ ] Names Leonard's DM from yesterday (A1) as the job, not its rules
- [ ] Names my Drive folder (A3) for the plan and the note, and our push notifications card for the checklist
- [ ] May name the Zombie Match PN sheet (A2); never a tab rule or a status
- [ ] Asks for the counts back to Leonard in that DM (R9)
- [ ] Every deliverable in §4 is reachable from the prompt or Leonard's DM
- [ ] No message name, count, value, rule, id or tool name (§9)
- [ ] No hint, riddle, hedge, if-chain or audit-form wording; no staged errors
- [ ] Not the shape of a sibling prompt (§9); `/prompt` STEP 0.6 meaning similarity stays under 0.80
- [ ] hardness_v2_check RULE_IN_PROMPT clean; word count 20 to 4,000

## 12 · Blockers and routed defects

- Routed to `/create-injection` and done: rev3 settles the forks a blind sweep of rev2 found (`plan/sweep_fork_rev2.md`), rev4 settles who files the string ticket, found by an independent read of the prompt (`plan/prompt_read_independent.md`), and rev5 takes the `/prompt` FAIL on rev4 (`run_forensics/rev4/prompt_report_FAIL.md`): the note no longer asks who hears from us and D1 and D7 are per platform. rev6 takes the `/hardness` FAIL 2 on rev5 (`run_forensics/rev5/hardness_report_FAIL_2.md`, `01a_Hardening_Report.md`) and the `/prompt` Coherence 3 on SC-13. The platform `/injection` PASS is on rev5, so `/injection` must run again on rev6.
- Surface repair (SQL unchanged): twelve slots could not pass on a correct run, because the decoder excludes ticket ids; synthetic run scores are in `plan/golden/grade.json` and are not platform evidence. X1c, X6c and X8c are local proxies by count, so the rubric must name those tickets. D1 stays strict at weight 1, because the decoder also wants a share call nothing asks for.
- Friction: `03_Error_Async_Config.txt` is set to none with its gate passed, because the blank template blocked this stage. No reference files.
- The local `/injection` review was not saved to the Evals store (it holds another task), so the platform `/injection` and `/prompt` still have to run on rev6.
- Pre-check items: relations on DES-330 and DES-338 rendering in linear_list_issues; `linear_show_data` and list `query` scope; the grader's Slack selector names slack_send_message while the catalog also has slack_conversations_add_message.
- Open risk for `/prompt`: competency fit, because most writes are on Linear; the note and the plan carry the Marketing and GTM work.
- Unverified: 27 client-code claims need repo blobs (`plan/inj_review_C2.md`); no call rests on one alone.

## 13 · Self-review

Re-read as Eval 1 Phases 1 to 3 against this brief (brief mode). Every load-bearing value above was re-read from the rev6 SQL or through `tools/hg.py` in this run (§5a, `plan/brief/search_out.txt`, the warehouse rows, can-see for the base records). Root causes appear only in §5, §9 and this review. Persona view, the assigned clock and fair-outcome acceptance hold.

| Area | Counter-reading (strongest argument it fails) | Evidence that resolves it | Verdict |
|---|---|---|---|
| Fair readings | the Go count could move: partial reach, a moved phone date, or a pass on an older iOS build | each is settled by a record: f_dc45e0e5a8b8635c1b82b2 test 4 'It fails only if none of them count'; samuel.turner@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com> on the phone date; C0880U9751A/1759245146.720608 says the lapsed ones are still coming through | holds |
| Fair readings | Audience could mean who actually hears rather than who the ticket names | f_dc45e0e5a8b8635c1b82b2: 'Audience is who the ask says it's for'; §4b also accepts narrowing on Go rows | holds |
| Fair readings | Finish first mission could pass reach on iOS, because Unity prompts at launch (C08R27X0EAH/1758291802.756889) | C0880U9751A/1759170096.924778: that popup doesn't switch anything on; f_dc45e0e5a8b8635c1b82b2: our own permission ask | holds |
| Clarity | 'one sheet in your Drive folder' could mean a subfolder, and 'next to it' could mean a tab | D06L58XCVKK/1759264851.763895 says a one-page note next to the sheet; §4b takes the final parent d_caafeec2804b3a67ce46aa; the prompt names my Drive folder (A3) | holds |
| Incorporation | the rule doc is named only by the hub, so a prompt that drops the hub loses every rule | §6: every graded requirement goes through A1 (D06L58XCVKK/1759264851.763895), which names the rule doc; f_dc45e0e5a8b8635c1b82b2 is readable, unique and states rules | holds |
| Truthfulness | 'Leonard's DM from yesterday' could be wrong in Pacific time | D06L58XCVKK/1759264851.763895 is Tue Sep 30 1:40 PM PT; today is Wed Oct 1 | holds |
| Truthfulness | the PN sheet might not be Samuel's to name | D06L58XCVKK/1750138057.452159: Leonard sent it to him; the sheet is shared with him (f_a325dd4af80afc5994d5dc) | holds |
| Feasibility / ACL | Samuel might not be able to file DES tickets, or the card might be closed | Samuel's DES membership is seeded (01_Universe_Inject.sql, tmem_team_DES_usr_caafeec2804b3a67); Leonard reopens 6851a769c65dc0017a227bb7 on Sep 24 | holds |
| Feasibility / ACL | the warehouse read may not reach the cohort rows | catalog snowflake_execute_query; wh_USER_COHORT_RETENTION rows read in this run | holds |
| Contrived register | a prompt listing every deliverable would read as a spec sheet, and one naming none would hide destinations | §6 and §11: the DM carries the contents; the prompt names A1 and A3 and asks for the counts back (D06L58XCVKK/1759264851.763895) | holds |
| Fair readings | the daily gift ask could already have a ticket, or fail test 1 while its bug is open | Julia's comment on ZOM-556 says the streak is live and it is separate from Calvin's chest ping on DES-338 | holds |
| Clarity | the String change column could be the whole of it, with no string ticket filed, and the prompt waives any check-in | the rule doc says 'so open one when you make the call'; it names the parent DES-314 | holds |
| Fair readings | the final Lapsed 7 days line could be the Sep 29 one, because that is what a search of Leonard's posts finds | the rule says the latest line he has called; his Sep 30 note on the copy check is later and says it replaces the art thread line | holds |
| Fair readings | Lives recharged could stay Go, because Vincent saw it arrive on store builds on Sep 24 | his Sep 30 post in #zombie-match3d takes his tick off it after iOS 0.3.49, and test 6 is his record | holds |

Unresolved: competency fit stays a `/prompt` risk (§12). 27 client-code claims stay unverified without repo blobs. Nothing else is open.

```
STAGE GATE prompt-writing: PASS — Task_Authoring/task_inputsK · 04_Prompt_Writing_Brief.md#2f436c545a7a · 00_Assigments.md#55f6d8057880 · 01_Grounding_Dossier.md#4aa9b3c38219 · 01_Universe_Inject.sql#6d162cfd1032 · 03_Error_Async_Config.txt#4a9d7adf67a3 · 01a_Hardening_Report.md#78482c593d15 · __context__#72168f70a409 · __assignment__#3adec6ac02d7 · __policy__#dc4ab5df3cdd · __gate_policy__#115714063000 · __review__#0d1c4d64c30c · blocking 0 · warnings 0 · checks 24
[PASS] assignment.v3_context: Samuel Turner / Game Designer; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Writing_Brief.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql, 03_Error_Async_Config.txt, 01a_Hardening_Report.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#6d162cfd1032, 01_Hardness_Manifest.json#09ddeab36568, 01_Grounding_Dossier.md#4aa9b3c38219, solver/solver.py#a1ac742c0f47, 01c_Dispositions.json#1e6cb127a339, 01c_Preflight_Report.json#d1bfc2687c65, 00_Assigments.md#55f6d8057880, 01_Scenario_Design.md#a477a8d3015e, 01_Hardness_Manifest.draft.json#ed860637b593, 01_Gradable_Surface.json#095a6e4fc9df, __context__#72168f70a409, __assignment__#3adec6ac02d7, __policy__#dc4ab5df3cdd, __gate_policy__#115714063000, __review__#95f1481dfb3c)
[PASS] chain.error-async: upstream 'error-async' PASS pasted and current (03_Error_Async_Config.txt#4a9d7adf67a3, 00_Assigments.md#55f6d8057880, 01_Grounding_Dossier.md#4aa9b3c38219, 01_Universe_Inject.sql#6d162cfd1032, __context__#72168f70a409, __assignment__#3adec6ac02d7, __policy__#dc4ab5df3cdd, __gate_policy__#115714063000, __review__#95f1481dfb3c)
[PASS] structure.sections: 14 required sections present and non-empty (04_Prompt_Writing_Brief.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Writing_Brief.md
[PASS] evidence.situation: 5/5 items carry a source pointer (min 100%)
[PASS] evidence.final_state: 47/47 items carry a source pointer (min 100%)
[PASS] evidence.discovery_map: 46/46 items carry a source pointer (min 100%)
[PASS] evidence.dates: 8/8 items carry a source pointer (min 100%)
[PASS] evidence.entity_traps: 10/10 items carry a source pointer (min 100%)
[PASS] tool.search_as_persona: 46 facts proven findable by persona_view search as samuel_turner
[PASS] reach.brief: 28 scoped load-bearing ids YES for samuel_turner
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] structure.accepted_outcomes: V3 accepts multiple fair outcomes; see v3.fair_outcomes_review
[PASS] boundary.anchor_naming: 3 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 12 evidenced counter-readings (of 14 found; need ≥ 6) in 04_Prompt_Writing_Brief.md
[PASS] review.coverage: self-review addresses all 6 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.fair_outcomes_review: current accepted outcomes and considered alternatives recorded; multiple fair outcomes are allowed
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

