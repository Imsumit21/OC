# Prompt Brief — dg-beta-server-signoff · prep
> Built 2026-10-26 from 00_Assigments.md, 01_Universe_Inject.sql (sha256 f5a42cee0962 — revision 7: prod branch added, references swept, open-ticket comments removed (dossier §13 Revisions 3–4);
> needs a fresh `/injection` run; revision 4 99128292df92 was /injection PASS), Working_Files/01_Grounding_Dossier.md, 01_Scenario_Design.md, 01_Hardness_Manifest.json,
> 03_Error_Async_Config.txt (Friction: none, error-async gate PASS) · no 02_Reference_Files_Manifest.md (no attachments) · Persona view
> verified: all load-bearing records YES for douglas (the sender's and cc copies of the two emails sit in other mailboxes and are not needed).
> 04_Prompt.txt may be drafted by Claude (`/create-prompt-writing draft`) or written by the human.
> **Clock:** universe date Oct 1, 2025; freeze 00:00 UTC = Tue Sep 30, 2025, 5:00 PM PT (V3 §3). The latest seeded event is Arthur's ask,
> 2025-09-30T21:12:44Z (2:12 PM PT), before the freeze. The go/no-go (Thu Oct 2) and the beta (Oct 10) are future events.

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
|---|---|---|
| Business function | Engineering → Engineering & Live-Ops (`Evals/references/rules/task_categories.md`) | backend release verification for the Zombie Match 3D beta (ZM ROADMAP list "BETA: Oct 10", trello:6851a7abf7876721472dba99 sits in it) |
| Persona / role | Douglas, douglas@harmonygames.co, Software Engineer (roster `douglas`, Engineering) | Voice: short, friendly, plain, often "Ok, …" / "Done!" (D079SNE2TL4/1759164463.327349 "Ok, the deployment is done, I will inform … and Blake as well"; D05QQF7V404/1758147207.631959 "done!"). Remit: he deploys the ZM backend by hand (D079SNE2TL4/1759256193.859279) and co-owns match3d-backend with a contractor (harmonygames-Games/match3d-backend#2). Read scope: own mailbox and calendar, the DM with Arthur D05QQF7V404, the DM with Vincent D079SNE2TL4, #zombie-match3d C0880U9751A and #zombie-bugs C08R27X0EAH (member), his own Drive files and the beta folder d_69fcebc484d472907b0b5c (shared writer) |
| Role plausibility (V3 §2) | Software Engineer | the CTO asking the backend lead for the server side of a release sign-off is ordinary engineering work (D05QQF7V404/1759266764.508127) |
| Competency | Engineering Ops | deploy/release verification: which closed tickets needed a backend change and whether that change is really on prod; tickets not on prod go back to Todo (card rule 5, trello:68dabfe9bc2e8b969782e22d) |
| Task skill | Retrieval | find and gather, per ticket, the server change from 73 Linear comment threads and the deploy state from 15 PRs' comments and 13 PRs' reviews, under rules spread over a card, a comment, an email, a doc, a calendar event and a log; the register is the retrieved record (W1) |
| Task type / tier | Long Horizon (100–500+ calls; author target 130–150, minimum 130) | services carrying weight: Linear (73 comment reads), GitHub (15 comment + 13 review reads), Slack, Trello, Gmail, Docs, Calendar, Sheets, Drive, Confluence — 10 services; manifest budget 139; `HARDNESS GATE (long): PASS` is pasted in the dossier (profile `long`, profile_exception recorded) |
| Difficulty mode / date | Medium (six-rollout average strictly under 85%; author target < 75%); Oct 1, 2025 | nothing after Tue Sep 30, 5:00 PM PT may be described as done; Thursday's go/no-go is a future event |

## 2 · Situation

| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |
|---|---|---|---|
| Arthur wants the server side of the beta sign-off for Thursday's go/no-go, with a reply in the DM saying how many tickets are on prod and which aren't; the rules are on the beta card on the roadmap board | Douglas, in his DM with Arthur | D05QQF7V404/1759266764.508127 (Tue Sep 30, 2:12 PM PT) | — |
| Leonard wants the server register shared with him once it is in the beta folder | Douglas, his inbox | douglas@harmonygames.co/1844721277206562572 (Tue Sep 30, 1:15 PM PT) | — |
| QA already said on Saturday that every server fix closed since the cut is on prod | Douglas, #zombie-match3d | C0880U9751A/1758991212.775031 (Sat Sep 27, 9:40 AM PT) | — |
| Douglas pushed the latest teams changes to prod today and Vincent says it works | Douglas, his DM with Vincent | D079SNE2TL4/1759256193.859279; D079SNE2TL4/1759269524.769369 | — |

No cause belongs in the situation. Why the summaries are wrong (rollbacks, missing or late approvals, the freeze, dev-only merges, the imports, the excluded tickets) is discovery-only (§5, never in the prompt).

## 3 · Investigation → action

Questions to resolve (no answers here):
1. Which rules decide the sign-off, and what amends them (the beta card, its comment, Arthur's later email; the client card and the Domino Delights page compete)?
2. Which tickets are in scope (closed after the beta prod cut through Sep 30, fix needed a server change, no parents, minus the email's two)?
3. Which server change(s) carry each ticket (Linear comments; PRs or deploy-log imports)?
4. Is each change on prod under the deploy doc (prod: comment, rollback, prior Approve by someone else, Arthur's Approve inside the freeze), and are all of a ticket's changes on prod?
5. Where the register goes, who must see it and what happens to the tickets not on prod?

Writes they feed: W1 (register) depends on 1–4. W2 (move into the folder) and W3 (share with Leonard) place W1. W4 (DM reply) carries the count and the keys from W1. W5 (Todo + comment per not-on-prod ticket) carries W1's N rows under card rule 5. No write is a bolt-on.

## 4 · Pinned final state (UGT anchor)

| Deliverable | Required contents (requirements) | Destination (exact) | Recipient(s) (exact) | Catalog write (reference only; never in the prompt) | Fed by |
|---|---|---|---|---|---|
| W1 register | one row per in-scope ticket (17): ticket, server change(s), on prod Y/N (card rule 2, trello:68dabfe9bc2e8b969782e22d) | a Google Sheet in the folder d_69fcebc484d472907b0b5c ("ZM Beta sign-off", named on page_zm_beta_oct10) | folder members (Arthur owner; Oliver, Vincent writers) | gsheets_create_spreadsheet + gsheets_values_update (+ gdrive_move_file) or gdrive_create_file with parentId | §3 Q1–Q4 |
| W3 share | Leonard can comment on the register | the register file | leonard.hayes@harmonygames.co (commenter) | gdrive_share_file | douglas@harmonygames.co/1844721277206562572 |
| W4 DM reply | how many tickets are on prod (2) and which aren't (ZOM-336, ZOM-392, ZOM-503, ZOM-518, ZOM-550, ZOM-435, ZOM-557, ZOM-256, ZOM-487, ZOM-537, ZOM-444, ZOM-531, ZOM-459, ZOM-509, ZOM-436) | DM D05QQF7V404 (reply to D05QQF7V404/1759266764.508127) | Arthur Blake, arthur.blake@harmonygames.co | slack_send_message | W1 |
| W5 ticket updates | each of the 15 not-on-prod tickets moved to Todo with a comment naming the change still to go out | the 15 Linear tickets (team_ZOM) | ticket watchers | linear_update_issue + linear_create_comment | W1 + card rule 5 |

| Decision-ambiguity risk | Alternative a careful run could take | What pins it |
|---|---|---|
| register destination | Douglas's own Drive, or "ZM Beta sign-off - client QA" d_d71300168ca5dffa4db8b3 | card rule 6 → page_zm_beta_oct10 names Arthur's "ZM Beta sign-off" (d_69fcebc484d472907b0b5c); the prompt may name "the beta sign-off folder" (V3 §8: a destination the sender knows) |
| register membership | September only; all tickets with a PR; including ZOM-547/553; leaving out ZOM-436 (its only comment is a device test note) | card rule 1 + deploy log row 1 (f_78bedc46245090a160d2dd); comment trello:68dbf1b73eba0ba580f67a6e; Arthur's reply-all in Leonard's thread douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> |
| on-prod rule | merged = on prod (C0880U9751A/1748450537.204611); the DD page's Slack thumbs-up (page_dd_launch_server_signoff) | card rule 3 → doc f_470ae81236d5bd39045dc1 |
| tickets not on prod | In Validation (client card trello:68dac311754b38be05be7ea9) or new tickets | card rule 5 (trello:68dabfe9bc2e8b969782e22d): back to Todo, same ticket, with a comment |
| reply place | #zombie-match3d (C0880U9751A/1759253506.093318 asks for it) | the ask: "reply here" (D05QQF7V404/1759266764.508127); posting in both is not wrong |
| share | sharing the folder, or as editor | Leonard's email: "share it with me directly. Comment access please, I don't need to edit" (douglas@harmonygames.co/1844721277206562572) |
| act vs ask | asking Arthur before moving tickets | the card already says what happens (trello:68dabfe9bc2e8b969782e22d); the ask is for Thursday |
| persona vs agent | an "I'll reply to Arthur" in the prompt assigning a write to Douglas | Arthur asked Douglas (D05QQF7V404/1759266764.508127); §11: every write is asked of the assistant |

### 4b · Canonical outcome (one acceptance class)

V3 §9: every fair reading passes. Each field below is either fixed, or its equivalence class lists the fair readings the rubric must accept.

| Deliverable | Field | Fixed value (pinned, with locator) | Delegated by | Allowed equivalence class | Material / representational |
|---|---|---|---|---|---|
| W1 | destination | a file inside d_69fcebc484d472907b0b5c (named on page_zm_beta_oct10) | — | a Google Sheet (or a Doc holding the same table) directly in that folder | material |
| W1 | title | — (D05QQF7V404/1759266764.508127 names none) | the ask names no title (D05QQF7V404/1759266764.508127) | any title | representational |
| W1 | row set | ZOM-459, ZOM-509, ZOM-336, ZOM-392, ZOM-503, ZOM-518, ZOM-499, ZOM-531, ZOM-537, ZOM-444, ZOM-487, ZOM-550, ZOM-435, ZOM-557, ZOM-510, ZOM-256, ZOM-436 (dossier §9.2) | — | any order; an extra note listing excluded tickets (ZOM-547, ZOM-553, ZOM-461) is fine; those are not register rows | material |
| W1 | server change(s) | per dossier §9.2 (e.g. ZOM-503: match3d-backend#42 and #52; ZOM-510: the Zombie Lane rewards import; ZOM-487: #48 and the boss arena HP table import; ZOM-537: #46 and the economy table import; ZOM-444: #47 and the analytics events table import; ZOM-436: the analytics events table import; ZOM-531: #45 and the loadout table import; ZOM-459: #38 and the plague race table import; ZOM-509: #39 and the trophy path copy table import) | — | "#52", "match3d-backend#52", a PR link; the import named in any recognisable words | material (set), representational (form) |
| W1 | on prod | Y: ZOM-499, ZOM-510; N: ZOM-336, ZOM-392, ZOM-503, ZOM-518, ZOM-550, ZOM-435, ZOM-557, ZOM-256, ZOM-487, ZOM-537, ZOM-444, ZOM-531, ZOM-459, ZOM-509, ZOM-436 | — | Y/N, yes/no, on prod / not on prod | material |
| W3 | grantee + role | leonard.hayes@harmonygames.co, commenter (douglas@harmonygames.co/1844721277206562572) | — | a direct share of the register file | material |
| W4 | destination | DM D05QQF7V404 | — | thread reply on D05QQF7V404/1759266764.508127 or a new DM message | material |
| W4 | contents | 2 on prod (of 17); the 15 keys not on prod (ZOM-336, ZOM-392, ZOM-503, ZOM-518, ZOM-550, ZOM-435, ZOM-557, ZOM-256, ZOM-487, ZOM-537, ZOM-444, ZOM-531, ZOM-459, ZOM-509, ZOM-436) | — | the count as a number or word; keys as ZOM-n or ticket titles | material |
| W4 | wording | — (D05QQF7V404/1759266764.508127) | the ask asks only for "how many tickets are on prod and which ones aren't" (D05QQF7V404/1759266764.508127) | any wording | representational |
| W5 | state | Todo on the 15 not-on-prod tickets (card rule 5, trello:68dabfe9bc2e8b969782e22d) | — | the ZOM team's Todo state | material |
| W5 | comment | names the change still to go out (e.g. ZOM-550: match3d-backend#50; ZOM-256: the algo level pack import; ZOM-487: the boss arena HP table import; ZOM-537: the economy table import; ZOM-444 and ZOM-436: the analytics events table import; ZOM-531: the loadout table import; ZOM-459: the plague race table import; ZOM-509: the trophy path copy table import) | — | any wording naming that PR/import | material (which change), representational (wording) |
| W5 | new tickets | none (card rule 5 "Same ticket, no new ones", trello:68dabfe9bc2e8b969782e22d) | — | — | material |

Rule for 08/09: two runs reach the same final state when every material field matches within its class. Under V3 §9 one fact (a ticket's on-prod value) is graded in no more than two rows.

## 5 · Discovery map

| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |
|---|---|---|---|---|---|---|
| F1 the ask (LB) | server side of the beta sign-off; rules on the beta card on the roadmap board; reply with how many on prod and which aren't | D05QQF7V404/1759266764.508127 | YES (im member) | met first | none: the DM with Arthur | Yes — as "Arthur's beta sign-off ask" (anchor A1); not the DM id |
| F2 Leonard's request (LB) | share the register with him, comment access | douglas@harmonygames.co/1844721277206562572 | YES (own inbox) | — | Gmail rarely opened | Yes — as "Leonard's go/no-go email" (anchor A2) |
| F3 rules card (LB authority) | rules 1–6 | trello:68dabfe9bc2e8b969782e22d | YES (unscoped) | competes with the client card trello:68dac311754b38be05be7ea9 and page_dd_launch_server_signoff | same "Beta sign-off" title | No — the ask already says where |
| F4 imports comment (LB) | spreadsheet imports count as server changes | trello:68dbf1b73eba0ba580f67a6e | YES | amends rule 1 | card comments rarely read | No |
| F5 Arthur's amendment (LB) | ZOM-547, ZOM-553 off and not counted; second point: the analytics events table import is part of ZOM-444's and ZOM-436's server change, the loadout table import of ZOM-531's (log: both dev only) | douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> (reply-all inside Leonard's thread douglas@harmonygames.co/1844721277206562572) | YES (own inbox) | amends rule 1 | a sender search returns Leonard's message only; the reply needs the thread | No (the prompt's 'Leonard's go/no-go email' reaches the thread) |
| F6 deploy doc (LB authority) | prod branch; prod:/rollback: comments; Approve by someone else first; Arthur's Approve in the freeze | f_470ae81236d5bd39045dc1 | YES (owner) | overrides Oliver's May claim C0880U9751A/1748450537.204611 | — | No |
| F7 freeze instant (LB) | Fri 2025-09-26 22:00 UTC | evt_0f489eb7fb46ada9660881 | YES (own calendar) | overrides C0880U9751A/1758295268.611352 (Monday) | Calendar rarely opened | No |
| F8 cut + imports (LB) | cut 2025-08-25 11:52 UTC; Zombie Lane rewards import → prod; algo pack, plague race, trophy path copy, loadout, analytics events, economy and boss arena HP tables → dev | f_78bedc46245090a160d2dd | YES (owner) | — | the Prod deploys tab stops on Sep 10 | No |
| F9 folder name (LB) | "ZM Beta sign-off" | page_zm_beta_oct10 → d_69fcebc484d472907b0b5c | YES (unscoped; shared writer) | the client QA folder d_d71300168ca5dffa4db8b3 | two folders start the same | "the beta sign-off folder" may be named |
| F10 per-ticket server change (LB) | 19 decisive comments among 79 | e.g. ZOM-503, ZOM-336, ZOM-510 comments (sql_ids.json) | YES (unscoped) | titles suggest otherwise | no list call returns comments | No |
| F11 PR deploy records (LB) | prod:/rollback:/dev comments; reviews | harmonygames-Games/match3d-backend#38 … #54 | YES (unscoped) | Oliver's summary C0880U9751A/1758991212.775031; Douglas's claim D05QQF7V404/1758571837.284511 | wrong GitHub comment tool | No |
| F12 #50 thread reply (LB) | "go ahead on dev. i'll look at the PR before it goes to prod" | C0880U9751A/1758938751.402267 | YES (member) | the parent C0880U9751A/1758937233.118904 | replies rarely opened | No |
| F13 Sep 30 teams deploy (LB trap) | deployed and confirmed working | D079SNE2TL4/1759256193.859279; D079SNE2TL4/1759269524.769369 | YES (im member) | overturned by the freeze rule + harmonygames-Games/match3d-backend#52 reviews | the persona's own message | No |
| F14 Oliver's summary (trap) | all server fixes since the cut on prod | C0880U9751A/1758991212.775031 | YES | overturned by the PR records | newest status message | No |
| F15 Douglas's claim (trap) | trophy fix out; seeds on prod since the 3rd | D05QQF7V404/1758571837.284511 | YES | overturned by #51 dev note and #41's late approval | same DM as the ask | No |
| F16 Arthur's page reply (LB) | the boss arena HP table import is part of ZOM-487's server change (log: dev only) | comment_zm_beta_oct10_c2 (reply to comment_zm_beta_oct10_c1) on page_zm_beta_oct10; f_78bedc46245090a160d2dd | YES (unscoped) | overturns ZOM-487's '#48' comment | page comments are a separate call | No |
| F17 Arthur's inline review comment on #46 (LB) | ZOM-537 also needs the economy table import (log: dev only) | harmonygames-Games/match3d-backend#46#rc_1; f_78bedc46245090a160d2dd | YES (unscoped) | completes ZOM-537's '#46' comment | inline review comments are a separate call from reviews and PR comments | No (card rule 3 and the doc send the reader to the PRs; the comment sits on #46, which ZOM-537's comment names) |
| F18 inline review comments on #38 and #39 (LB) | ZOM-459 also needs the plague race table import; ZOM-509 the trophy path copy table import (log: dev only) | harmonygames-Games/match3d-backend#38#rc_1; harmonygames-Games/match3d-backend#39#rc_1; f_78bedc46245090a160d2dd | YES (unscoped) | completes the '#38' / '#39' ticket comments | inline review comments are a separate call | No (same path as F17) |

## 5a · Search-as-persona proof

`persona_view.py search` reads only the base export, so seeded rows return 0 there. Each row therefore gives base competition (`persona_view.py search`, verbatim below) and seeded reach (a case-insensitive count of SQL lines containing the same query, each row's `check-sql` verdict for douglas YES — dossier §1.E). Unscoped services are always YES.

| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |
|---|---|---|---|---|---|---|
| F1 | slack | "server side of the beta sign-off" | base 0; seeded 1 | 0 | D05QQF7V404/1759266764.508127 | YES (seeded, check-sql YES) |
| F2 | gmail | "go/no-go" | base 0; seeded (Douglas copy) | 0 | douglas@harmonygames.co/1844721277206562572 | YES (own mailbox) |
| F3 | trello | "beta sign-off" | base 0; seeded 2 cards | 0 | trello:68dabfe9bc2e8b969782e22d | YES (unscoped) |
| F4 | trello | "spreadsheet imports" | base 0; seeded 1 | 0 | trello:68dbf1b73eba0ba580f67a6e | YES (unscoped) |
| F5 | gmail | "go/no-go" | base 0; seeded (Douglas copy, 2 messages in one thread) | 0 | douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> | YES (own mailbox) |
| F6 | gdocs | "prod deploys" | base 0; seeded 1 | 0 | f_470ae81236d5bd39045dc1 | YES (owner) |
| F7 | gcal | "server freeze" | base 0; seeded 5 copies | 0 | evt_0f489eb7fb46ada9660881 | YES (own calendar) |
| F8 | gsheets | "deploy log" | base 0; seeded 1 | 0 | f_78bedc46245090a160d2dd | YES (owner) |
| F9 | confluence / gdrive | "ZM beta" / "ZM Beta sign-off" | base 0 / 0; seeded 1 page, 2 folders | 0 | page_zm_beta_oct10; d_69fcebc484d472907b0b5c | YES |
| F10 | linear | "match3d-backend" | base 0; seeded ~50 comments | 0 | ZOM-503 (comment) | YES (unscoped; per-ticket list) |
| F11 | github | "match3d-backend" | base 2 (repo rows); seeded 18 PRs | 0 | harmonygames-Games/match3d-backend#44 | YES (unscoped) |
| F12 | slack | "boss arena lives fix" | base 0; seeded 1 (+ replies) | 0 | C0880U9751A/1758937233.118904 | YES (member) |
| F13 | slack | "teams/social changes" | base 1 | 0 | D079SNE2TL4/1759256193.859279 | YES (can-see YES) |
| F14 | slack | "qa pass on prod" | base 0; seeded 1 | 0 | C0880U9751A/1758991212.775031 | YES (member) |
| F15 | slack | "algo seeds" | base 0; seeded 1 | 0 | D05QQF7V404/1758571837.284511 | YES (im member) |
| F16 | confluence | page comments of "ZM beta" | base 0; seeded 2 comments | 0 | comment_zm_beta_oct10_c2 | YES (unscoped) |
| F17 | github | "economy table" / inline review comments of #46 | base 2 (GameOfDominoes#1764 and its commit, another repo); seeded 1 | 0 | harmonygames-Games/match3d-backend#46#rc_1 | YES (unscoped) |
| F18 | github | "plague race table" / "trophy path copy table" | base 0 / 0; seeded 2 / 2 | 0 | harmonygames-Games/match3d-backend#38#rc_1; #39#rc_1 | YES (unscoped) |
| F5 (second point) | gmail / gsheets | "analytics events table" / "loadout table" | base 0 / 0; seeded 4 / 4 | 0 | douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> | YES (own mailbox) |

Base searches (verbatim, `python3 Task_Authoring/tools/persona_view.py search douglas <service> "<query>" --limit 2 --no-hidden`):

```
SEARCH slack 'server side of the beta sign-off' as douglas  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH slack 'algo seeds' as douglas  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH slack 'server freeze' as douglas  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH slack 'boss arena lives fix' as douglas  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH slack 'qa pass on prod' as douglas  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH slack 'teams/social changes' as douglas  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "D079SNE2TL4/1759256193.859279", "channel": "D079SNE2TL4", "kind": "im", "date": "2025-09-30", "user": "EMPLOYEE_0031_SLACK_ID", "reply": false, "snippet": "Ok, I updated the prod environment with the latest teams/social changes, let me know if you ar
SEARCH trello 'beta sign-off' as douglas  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH trello 'spreadsheet imports' as douglas  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gmail 'beta sign-off' as douglas  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gmail 'go/no-go' as douglas  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gdocs 'prod deploys' as douglas  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gsheets 'deploy log' as douglas  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gcal 'server freeze' as douglas  scope: GCal event summary (base events carry no description/location)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH confluence 'ZM beta' as douglas  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gdrive 'ZM Beta sign-off' as douglas  scope: Drive file/folder names (on-disk file content is not searched)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH linear 'match3d-backend' as douglas  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH github 'match3d-backend' as douglas  scope: hg.py search (unscoped: no ACL filter)
visible hits=2 (showing 2)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gmail 'analytics events table' as douglas  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH github 'plague race table' as douglas  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH github 'trophy path copy table' as douglas  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gsheets 'loadout table' as douglas  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

Seeded counts (lines of 01_Universe_Inject.sql containing the query, case-insensitive): "server side of the beta sign-off" 1 · "algo seeds" 1 · "server freeze" 7 · "boss arena lives fix" 1 · "qa pass on prod" 1 · "beta sign-off" 13 · "spreadsheet imports" 2 · "go/no-go" 11 · "prod deploys" 4 · "deploy log" 5 · "ZM beta" 10 · "ZM Beta sign-off" 4 · "match3d-backend#" 266 · "analytics events table" 4 · "loadout table" 4 · "plague race table" 2 · "trophy path copy table" 2.

## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · persona-readable · unique · instructions-not-answer) | Inferable |
|---|---|---|---|---|
| R1–R3 register rows (scope, server change, on prod) | trello:68dabfe9bc2e8b969782e22d, trello:68dbf1b73eba0ba580f67a6e, douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>, comment_zm_beta_oct10_c2, harmonygames-Games/match3d-backend#46#rc_1, harmonygames-Games/match3d-backend#38#rc_1, harmonygames-Games/match3d-backend#39#rc_1, f_470ae81236d5bd39045dc1, evt_0f489eb7fb46ada9660881, f_78bedc46245090a160d2dd | deliverable: the server side of the sign-off Arthur asked for | ask D05QQF7V404/1759266764.508127 · YES · one ask · it points to the card and holds no answer | gotcha → carried by the ask trigger |
| R4 register in the beta sign-off folder | d_69fcebc484d472907b0b5c via page_zm_beta_oct10 | destination | card rule 6 · YES · the Confluence page names one folder · instructions | may be named in the prompt (V3: the sender knows it) |
| R5 DM reply (count + keys) | D05QQF7V404/1759266764.508127 | destination + contents carried by the ask | ask · YES · unique DM · instructions | the prompt points at Arthur's ask; contents stay in the ask |
| R6 Todo + comment on not-on-prod tickets | card rule 5 (trello:68dabfe9bc2e8b969782e22d) | none beyond the ask (the ask incorporates the card) | card rule 5 · YES (unscoped) · one card · instructions | gotcha → triggered through the incorporated card |
| R7 share with Leonard | douglas@harmonygames.co/1844721277206562572 | recipient: Leonard's email (anchor A2) | Leonard's email · YES (own inbox) · one mail · instructions | needs the trigger (the prompt points at Leonard's email) |
| reading each record before writing | — | none | — | inferable (competent assistant) |

| Anchor | May be named |
|---|---|
| A1 | Arthur's beta sign-off ask; my DM with Arthur |
| A2 | Leonard's go/no-go email |
| destination W1 | the beta sign-off folder |

## 7 · Dates and constraints

All times Pacific, with UTC beside them where useful (V3 §10).

| Item | Absolute date or value | Source | Past fact or deadline |
|---|---|---|---|
| Oliver's merged-is-live claim | Wed May 28, 2025, 9:42 AM PT (16:42Z) | C0880U9751A/1748450537.204611 | past (superseded) |
| prod env created | Sun Jun 1, 2025 (merged 17:54Z) | harmonygames-Games/match3d-backend#2 | past |
| beta prod cut | Mon Aug 25, 2025, 4:52 AM PT (11:52Z) | f_78bedc46245090a160d2dd row 1 | past |
| freeze announced as Monday | Fri Sep 19, 2025, 8:21 AM PT (15:21Z) | C0880U9751A/1758295268.611352 | past (superseded) |
| Douglas's claim | Mon Sep 22, 2025, 1:10 PM PT (20:10Z) | D05QQF7V404/1758571837.284511 | past |
| freeze event updated | Tue Sep 23, 2025, 9:05 AM PT (16:05Z) | evt_0f489eb7fb46ada9660881 | past |
| server freeze starts | Fri Sep 26, 2025, 3:00 PM PT (22:00Z) | evt_0f489eb7fb46ada9660881 | past |
| #50 thread | Fri Sep 26, 2025, 6:40–7:07 PM PT (Sep 27 01:40–02:07Z) | C0880U9751A/1758937233.118904 | past |
| Oliver's summary | Sat Sep 27, 2025, 9:40 AM PT (16:40Z) | C0880U9751A/1758991212.775031 | past |
| #54 rollback | Sat Sep 27, 2025, 8:10 PM PT (Sep 28 03:10Z) | harmonygames-Games/match3d-backend#54 (rollback: comment) | past |
| rules card / client card | Mon Sep 29, 2025, 10:20 / 10:34 AM PT | trello:68dabfe9bc2e8b969782e22d; trello:68dac311754b38be05be7ea9 | past |
| imports comment | Tue Sep 30, 2025, 8:05 AM PT (15:05Z) | trello:68dbf1b73eba0ba580f67a6e | past |
| teams deploy / Vincent confirms | Tue Sep 30, 11:16 AM / 2:58 PM PT | D079SNE2TL4/1759256193.859279; D079SNE2TL4/1759269524.769369 | past |
| QA question / Arthur's page reply | Tue Sep 30, 2025, 3:12 / 4:03 AM PT (10:12Z / 11:03Z) | comment_zm_beta_oct10_c1; comment_zm_beta_oct10_c2 (on page_zm_beta_oct10) | past |
| Leonard's email | Tue Sep 30, 2025, 1:15 PM PT (20:15Z) | douglas@harmonygames.co/1844721277206562572 | past |
| Arthur's amendment (reply-all in Leonard's thread) | Tue Sep 30, 2025, 1:41 PM PT (20:41Z) | douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> | past |
| Arthur's ask | Tue Sep 30, 2025, 2:12 PM PT (21:12Z) | D05QQF7V404/1759266764.508127 | past; the prompt's "now" follows it |
| Arthur's inline review comment on #46 | Tue Sep 9, 2025, 12:40 PM PT (19:40Z) | harmonygames-Games/match3d-backend#46#rc_1 | past |
| reviewer's inline comment on #38 / Douglas's on #39 | Mon Aug 25, 2025, 2:20 AM PT (09:20Z) / Tue Sep 2, 2025, 8:20 AM PT (15:20Z) | harmonygames-Games/match3d-backend#38#rc_1; harmonygames-Games/match3d-backend#39#rc_1 | past |
| freeze of the universe | Tue Sep 30, 2025, 5:00 PM PT = Oct 1, 2025 00:00 UTC | 00_Assigments.md; latest seeded record before it D05QQF7V404/1759266764.508127 (the ask, 21:12:44Z) | the "now" of the prompt |
| go/no-go | Thu Oct 2, 2025 | D05QQF7V404/1759266764.508127; page_zm_beta_oct10 | future |
| beta | Fri Oct 10, 2025 | page_zm_beta_oct10; ZM ROADMAP list 6851a674975da1fe76e70d93 | future |

## 8 · Difficulty levers

| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |
|---|---|---|---|---|
| Ambiguity | yes | yes | which tickets needed a server change lives only in 73 comment threads; deploy state only in PR comments and reviews (ZOM-503; harmonygames-Games/match3d-backend#44) | the prompt says what to produce and where; never where the rules or evidence live |
| Dynamic change | yes | yes | card → comment → Arthur's reply in Leonard's thread; ticket notes → Arthur's page reply, the inline review comments on #38, #39 and #46, and the second point of Arthur's reply-all (ZOM-487, ZOM-537, ZOM-459, ZOM-509, ZOM-444, ZOM-531, ZOM-436); Slack Monday → calendar Friday; summary/claim → PR records; prod → rollback → prod (#44) (trello:68dbf1b73eba0ba580f67a6e; evt_0f489eb7fb46ada9660881) | no mention of a correction, an email from Arthur, a comment, a freeze, approvals or "the latest version" |
| Multi-source | yes | yes | 10 services (§1) | no source named as an exact artifact beyond §6 anchors and the folder |
| Async | no | — | 03_Error_Async_Config.txt: Friction: none | nothing to hide |
| Error recovery | no | — | no friction configured | nothing to announce |
| Access control | no (incidental only) | no | other mailboxes' copies of the two emails are NO and not needed | no ask to read anyone else's mail |

## 9 · Must not appear in the prompt

- **Tool and server names** (`Evals/references/tools/catalog.json`): linear_list_comments, linear_list_issues, linear_update_issue,
  linear_create_comment, github_get_issue_comments, github_get_pull_request_comments, github_get_pull_request_reviews,
  github_search_pull_requests, gcal_list_events, gsheets_create_spreadsheet, gsheets_values_update, gdrive_move_file, gdrive_share_file,
  gdrive_create_file, slack_send_message, slack_conversations_replies, trello_get_card, gmail_search_messages, gdocs_get_document,
  confluence_search; "the X tool"; any MCP server name. Natural product names ("the Linear tickets", "a sheet") are fine.
- **Ids and opaque names**: D05QQF7V404, C0880U9751A, D079SNE2TL4, any ts, f_/d_ ids, trello ids, page_ ids, evt_ ids, PR numbers
  (#37–#54), ZOM keys, task-definition names (zm-api:NN), PERSON_/EMPLOYEE_ tokens.
- **Hidden authorities and findings**: the card's title or board list, the imports comment, Arthur's reply in Leonard's thread, Arthur's
  page comment, the inline review comments on #38, #39 and #46, the economy, boss arena HP, plague race, trophy path copy, loadout and analytics events table imports, the deploy doc and
  its title, the deploy log, the freeze or its date, the Confluence pages, the client card and client QA folder, the cut time, approvals,
  rollbacks, CodeRabbit, the prod branch, "dev only", the Sep 30 teams deploy being unapproved.
- **Answers**: any ticket's on-prod value, the counts (17 rows, 2/15), the excluded tickets, ZOM-436's inclusion, which tickets need Todo.
- **V3 §8 patterns**: "don't trust Oliver's summary", "check the approvals", "Actually", answer-key clauses ("if a PR was rolled back …"),
  riddles, trap hints, spec language ("ensure", "governing").
- **Form**: Markdown, numbered steps, a column list for the register (card rule 2 has it), a prescribed reply format, staged typos.
- **No attachment or `/app/artifact` reference** (no reference files).

## 10 · Entity traps

`python3 Task_Authoring/tools/entity.py collisions` and `resolve` (verbatim excerpt):

```
SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <marcus@harmonygames.co>', 'Marcus <github:PERSON_0396_GITHUB_USERNAME>']
  martin: ['Martin Lewis <PERSON_0394_EMAIL>', 'Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]']
  thomas: ['Thomas Baker <thomas.baker@harmonygames.co>', 'Thomas <thomas@harmonygames.co> [persona thomas]']

SHARED_LAST_NAMES (5)
  baker: ['Owen Baker <owen.baker@harmonygames.co> [persona owen_baker]', 'Thomas Baker <thomas.baker@harmonygames.co>']
  brooks: ['Lauren Brooks <lauren@harmonygames.co>', 'Oliver Brooks <oliver.brooks@harmonygames.co> [persona oliver_brooks]']
ENTITY email:douglas@harmonygames.co  name=Douglas  kind=person  emails=['douglas@harmonygames.co']
ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
ENTITY email:oliver.brooks@harmonygames.co  name=Oliver Brooks  kind=person  emails=['oliver.brooks@harmonygames.co']
ENTITY email:vincent.parker@harmonygames.co  name=Vincent Parker  kind=person  emails=['vincent.parker@harmonygames.co']
```

| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |
|---|---|---|---|
| Arthur Blake, arthur.blake@harmonygames.co | "Blake" in Douglas's Slack; mailbox files blake@harmonygames.co_* | one person; author of the ask, card, comment, email, freeze | D05QQF7V404/1759266764.508127 |
| Leonard Hayes, leonard.hayes@harmonygames.co | mailbox files leonard@harmonygames.co_* | one person; the share recipient | douglas@harmonygames.co/1844721277206562572 |
| Oliver Brooks, oliver.brooks@harmonygames.co | Lauren Brooks, lauren@harmonygames.co | Oliver writes the summary and owns the client card scope | C0880U9751A/1758991212.775031 |
| match3d-backend (server repo) | match3d (client repo, mirrored to #zombie-prs) | PR numbers overlap (N02) | harmonygames-Games/match3d-backend#50 vs harmonygames-Games/match3d#438 |
| ZOM-503 etc. | ENG-503, ENG-557 (N01) | different team series | ZOM-503 |
| the server sign-off card | the client sign-off card (same list) | different scope and rules | trello:68dabfe9bc2e8b969782e22d vs trello:68dac311754b38be05be7ea9 |
| ZM Beta sign-off folder (write target) | ZM Beta sign-off - client QA (Oliver's) | Douglas is writer on the first, reader on the second | d_69fcebc484d472907b0b5c vs d_d71300168ca5dffa4db8b3 |

Name-swap test: swapping Arthur or Leonard for any other name breaks the task — the ask, the card, the comment, the amendment, the freeze and the share request are their records (D05QQF7V404/1759266764.508127; douglas@harmonygames.co/1844721277206562572). The scenario rests on real records.

## 11 · Pre-submit checklist

- [ ] Reads like Douglas writing to an assistant: short, friendly, plain (V3 §8); clean spelling is fine
- [ ] Points at Arthur's beta sign-off ask in the DM and at Leonard's go/no-go email; may name the beta sign-off folder
- [ ] Every write is asked of the assistant ("can you …"), no "I'll reply to Arthur" or "I'll share it" beside the same write
- [ ] Mentions dealing with the tickets the way the sign-off rules say, without naming Todo, comments or the card
- [ ] No Markdown, no numbered steps, no column list, no reply format
- [ ] Nothing from §9: no PR numbers, no ticket keys, no freeze, no approvals, no rollback, no "check Oliver's summary"
- [ ] No "Actually", no answer-key clause, no trap hint (V3 §8)
- [ ] Nothing after Tue Sep 30, 5:00 PM PT described as done; Thursday's go/no-go is upcoming
- [ ] Any premise stated is true (Arthur asked in the DM today; Leonard emailed today; the go/no-go is Thursday)
- [ ] 20–4,000 words; then run `/create-prompt-writing check`

## 12 · Blockers and routed defects

| Item | Status | Locator |
|---|---|---|
| `/injection` advisories (5) on f48302c6acec | FIXED; `/injection` FINAL VERDICT PASS on SQL f5a42cee0962 (revision 4) | dossier §13 Revision 2; d_d71300168ca5dffa4db8b3 |
| `linear_show_data` / `linear_list_issues(query)` bulk comment behaviour | UNVERIFIED — probe at the Opus pre-check (dossier §12) | ZOM-503 |
| conversation-comment GitHub tool | UNVERIFIED — `github_get_issue_comments` assumed (reviewer B) | harmonygames-Games/match3d-backend#44 |
| call budget 175 vs the 130–150 target | baselines measured 134–193, 163–220 and 194–228 calls; above the target, recorded as a tension (01a §6) | 01_Hardness_Manifest.json call_budget; 01a_Hardening_Report.md §6 |
| hardening round 1 (SQL c1edeb4431f4) | applied: amendment moved into Leonard's thread; ZOM-487 and ZOM-537 gain dev-only imports named by Arthur; PR #40 retitled | 01a_Hardening_Report.md §14 |
| hardening round 3 (SQL 2131bbeff16b) | applied: second point in Arthur's reply-all (ZOM-444, ZOM-531, ZOM-436); inline review comments on #38 and #39 (ZOM-459, ZOM-509); four dev-only log rows; truth 17 rows, 2 on prod, 15 not | 01a_Hardening_Report.md §11 |

## 13 · Self-review

**Eval walk (`Evals/1_Prompt_Eval.md`).** Phase 1: persona (§1.1) is Douglas, the backend lead who deploys the ZM backend himself (§1).
Naturalness (§1.2) is checked on the real text; §11 lists the V3 patterns to avoid. Anti-patterns (§1.3): no command list, no bolt-ons (W3–W5
depend on W1), no pre-solving (§9), no tool names (§9). Diversity (§1.4): five writes in four services (Sheets/Drive, Slack, Linear). Assignment
and complexity (§1.5): Engineering Ops, Retrieval, with Ambiguity, Dynamic change and Multi-source load-bearing (§8). Phase 2: UGT (§2.1) one
acceptance class per deliverable (§4b). Feasibility (§2.2): every write in the catalog, every read persona-YES (§5a). Truthfulness (§2.3): the
premises the prompt may state are in §7/§10. Cross-service (§2.4): 10 services. Investigation → action (§2.5) in §3. Clarity (§2.6) in §4.
Contrived (§2.7) in §9/§11. Today's date (§2.8) in §7. Originality (§2.9): no supplied sample; a deploy-verification register differs from the
two completed Frederick tasks (support/completed_tasks). Phase 3: universe feasibility rests on the `/injection` PASS for SQL f5a42cee0962.

**Counter-readings.**

| Area | Counter-reading | Resolution (evidence) |
|---|---|---|
| UGT | Reading B: ZOM-503 is on prod because Douglas deployed the teams changes Sep 30 and Vincent confirmed them | inside the freeze (evt_0f489eb7fb46ada9660881) a deploy counts only with Arthur's Approve; #52 has the contractor's only (harmonygames-Games/match3d-backend#52#rev_2); doc f_470ae81236d5bd39045dc1 → N |
| UGT | Reading B: ZOM-550 is on prod — Douglas approved #50 and Arthur reviewed it | freeze rule needs Arthur's Approve; his review is COMMENTED (harmonygames-Games/match3d-backend#50#rev_3) and his thread reply limits it to dev (C0880U9751A/1758938751.402267) → N |
| UGT | Reading B: ZOM-256 is out because its import went to dev only | the comment says imports on the backend count (trello:68dbf1b73eba0ba580f67a6e), with no target condition; the target decides on prod → row, N |
| UGT | Reading B: ZOM-557 stays on prod because its rollback happened inside the freeze unapproved | doc: "A rollback takes the PR off prod whenever it happens, freeze or not" (f_470ae81236d5bd39045dc1) → N |
| Clarity | if the prompt says "I'll tell Arthur", the agent may skip W4 | §11: every write asked of the assistant; check mode C7 tests it on the real text |
| Clarity | "deal with the tickets" could mean In Validation or new tickets | card rule 5 pins Todo + comment on the same ticket (trello:68dabfe9bc2e8b969782e22d); the client card's In Validation is client-scoped (trello:68dac311754b38be05be7ea9) |
| Incorporation | the prompt points to Arthur's ask, which incorporates the card — does the card hand over the answer? | the card states rules only, no ticket or value (`fact_check --no-leak` PASS, dossier §8); Arthur's reply names two excluded tickets and the page/thread replies name two server changes, which are instructions, not answers |
| Incorporation | the Todo writes and Leonard's share are not in the ask, so they look unauthorized | card rule 5 (incorporated by the ask) carries the Todo writes; anchor A2 (Leonard's email, douglas@harmonygames.co/1844721277206562572) carries the share |
| Truthfulness | a premise like "Arthur emailed me the rules" would be false | the ask is a Slack DM (D05QQF7V404/1759266764.508127); the rules are a Trello card; Arthur's only mail is his reply under Leonard's (douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>) |
| UGT | Reading B: ZOM-487 / ZOM-537 are on prod because their tickets name only #48 / #46, both on prod | card rule 4 (every change on prod, trello:68dabfe9bc2e8b969782e22d); Arthur adds the imports (comment_zm_beta_oct10_c2; harmonygames-Games/match3d-backend#46#rc_1) and the log has both on dev (f_78bedc46245090a160d2dd) → N |
| UGT | Reading B: ZOM-459 / ZOM-509 / ZOM-444 / ZOM-531 are on prod because their tickets name one PR each, all on prod with an approval first | card rule 4; the inline review comments on #38 and #39 (harmonygames-Games/match3d-backend#38#rc_1, #39#rc_1) and Arthur's reply-all (douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>) add table imports the log has on dev only (f_78bedc46245090a160d2dd) → N |
| UGT | Reading B: ZOM-436 has no row because its only comment is a device test note | card rule 1 + the imports comment (trello:68dbf1b73eba0ba580f67a6e): an import is a server change; Arthur's reply-all names the analytics events table import as ZOM-436's → row, N |
| Feasibility / ACL | can Douglas write into the folder and share the file? | folder shared with him as writer (d_69fcebc484d472907b0b5c, check-sql YES); he owns the sheet he creates; `gdrive_share_file` is in the catalog; writes are never ACL-governed |
| Feasibility / ACL | Linear and GitHub reads might not return seeded comments | unscoped services; Linear comments render (Ask_Carriers §6b); the GitHub tool is UNVERIFIED (§12), and both conversation-comment tools exist in the catalog |
| Contrived | naming the folder and two anchors could read as a spec sheet | V3 §8 asks that destinations the sender knows be named; one sentence naming them is the screen-24 skeleton (Eval 1 §2.7); the columns stay in card rule 2 |

**Re-verified this run:** the ask, claim, summaries, freeze message, thread, card, comment, emails, doc, log and page texts from
`support/task_work/dg_beta_server/planned_text.json` and the SQL rows (seeded counts above); persona reach from dossier §1.E check-sql and
`persona_view.py search` (pasted); base Slack D079SNE2TL4/1759256193.859279 from the base export; write names from `Evals/references/tools/catalog.json`;
Pacific times computed from the UTC stamps.

Unresolved: the two tool behaviours in §12 are UNVERIFIED until the Opus pre-check; the call count and the six-rollout average are unmeasured.

```
STAGE GATE prompt-writing: PASS — Task_Authoring-2/task_inputs · 04_Prompt_Writing_Brief.md#70b6632b856b · blocking 0 · warnings 0 · checks 21
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Writing_Brief.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql, 03_Error_Async_Config.txt, 01a_Hardening_Report.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#2131bbeff16b, 01_Hardness_Manifest.json#dac54299d2c5, 01_Grounding_Dossier.md#3cc21f8ed2b7)
[PASS] chain.error-async: upstream 'error-async' PASS pasted and current (03_Error_Async_Config.txt#f0acade86bfd)
[PASS] structure.sections: 14 required sections present and non-empty (04_Prompt_Writing_Brief.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Writing_Brief.md
[PASS] evidence.situation: 4/4 items carry a source pointer (min 100%)
[PASS] evidence.final_state: 24/24 items carry a source pointer (min 100%)
[PASS] evidence.discovery_map: 18/18 items carry a source pointer (min 100%)
[PASS] evidence.dates: 22/22 items carry a source pointer (min 100%)
[PASS] evidence.entity_traps: 7/7 items carry a source pointer (min 100%)
[PASS] tool.search_as_persona: 19 facts proven findable by persona_view search as douglas
[PASS] reach.brief: 16 scoped load-bearing ids YES for douglas
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] structure.canonical_outcome: canonical outcome table: 12 field(s), each fixed or delegated
[PASS] boundary.anchor_naming: 3 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 15 evidenced counter-readings (of 15 found; need ≥ 6) in 04_Prompt_Writing_Brief.md
[PASS] review.coverage: self-review addresses all 6 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```









