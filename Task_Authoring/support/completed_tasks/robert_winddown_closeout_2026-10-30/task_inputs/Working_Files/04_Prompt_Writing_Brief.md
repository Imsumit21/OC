# Prompt Brief — rb-winddown-closeout · prep
> Built 2026-10-28 from 00_Assigments.md, 01_Universe_Inject.sql (sha256 fc9bc388ee2a, /injection PASS — Audit-Report/0_injection_PASS.md), Working_Files/01_Grounding_Dossier.md, 01_Scenario_Design.md, 01_Hardness_Manifest.json · 03_Error_Async_Config.txt is the blank template (Friction: none — no error-async stage run) · no 02_Reference_Files_Manifest.md (no attachments) · Persona view verified: all load-bearing records YES for robert (check-sql PASS, dossier §1.E); the Leonard/Arthur mailbox copies are not needed.
> 04_Prompt.txt may be drafted by Claude (`/create-prompt-writing draft`) or written by the human.
> **Clock:** 2026-02-14T00:00:00Z (Saturday). The latest seeded event is Robert's own Linear comment 2026-02-13T20:51Z; Leonard's ask is 2026-02-13T17:21Z (Fri 9:21 AM PT). The review call (Mar 12) and every deadline are future.

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
|---|---|---|
| Business function | Executive → Founders / Exec / Strategy (`Evals/references/rules/task_categories.md`) | a co-founder's wind-down decision work in the founders-only #winddown (C0ADGSZKR3R) |
| Persona / role | Robert, robert@harmonygames.co, Co-Founder & Creative Director (roster `robert`, Executive) | Voice: short, lowercase, direct (C0ADGSZKR3R/1770839322.836779 'Soundly canceled'; C0ADGSZKR3R/1770859313.592649 'Our Figma is good until September 11th'). Read scope: #winddown, #executives, #admin_foundersonly member; own mailbox (billing mail); Wind Down files shared with him (f_31115ddb6ed866f2b10d60) |
| Competency | Corporate Ops | account/subscription close-out during the shutdown; Leonard hands Robert the register (C0ADGSZKR3R/1771003267.448213); the Task List row 'Cancel or move all software subscriptions' is unowned (f_31115ddb6ed866f2b10d60) |
| Task skill | Planning and decision support | decide per account what happens (Cancel / Keep / Move / Hold), where it stands, by when, who acts, what it costs, and surface the clashes with earlier decisions (C0ADGSZKR3R/1771003267.448213); stacked: Actions (Linear settling, sharing, the reply) |
| Task type / tier | Long Horizon (100–500+; author target > 150 calls every run, average < 80%) | 10 services carry weight; 28 Linear issues × comments + settling, vendor words outside Linear (rule 5); manifest budget 122; `HARDNESS GATE (long): PASS` in dossier §13 |
| Difficulty mode / date | easy (recorded); Feb 14, 2026 | nothing on/after Sat Feb 14 00:00Z may be described as done |

## 2 · Situation

| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |
|---|---|---|---|
| Leonard asks Robert to own the account close-out register before he archives anything on Google: one sheet of every account (what we do, where it stands, by when, who, monthly cost), shared with him and Arthur as editors; settle each Linear issue with a line on each; reply with the two monthly totals and any clashes | Robert, in #winddown | C0ADGSZKR3R/1771003267.448213 (Fri Feb 13, 9:21 AM PT) | — |
| Leonard said the P&L covers everything | Robert, #winddown | C0ADGSZKR3R/1770933999.157259 | — |
| Arthur put the accounts into a Linear project | Robert (Linear, unscoped) | project 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a 'Shutdown – accounts' (ENG-2438…ENG-2483) | — |
| The vendors' own billing mail for Arthur's and Leonard's accounts | — | blake@harmonygames.co_1856962040028188034.json, leonard@harmonygames.co_1856958213684823393.json | Leonard's and Arthur's mailboxes; the account holders relay what matters in their Linear comments |

No cause belongs in the situation. Why the obvious list is wrong (missing accounts, the Sunset hold and its correction, the card closure, the amended keep list, unconfirmed cancellations) is discovery-only (§5, never in the prompt).

## 3 · Investigation → action

Questions to resolve (no answers here):
1. Which accounts belong on the register (the project, minus exclusions and the duplicate, plus accounts the project lacks)?
2. What happens to each (Leonard's keep list as amended, Arthur's LLC moves, Sunset's list as corrected)?
3. Where each Cancel account stands (vendor-confirmed or not) and by when each account needs action?
4. Who owns each account and what it costs a month; the two totals?
5. Which earlier decisions clash with the plan?

Writes they feed: W1 register (1–4) → W2 share with Leonard and Arthur → W3 Linear settling of each issue (state + comment, from W1) → W5 reply in Leonard's thread (totals from W1, clashes from 5). Rule 3 additions are register rows, not new issues. No write is a bolt-on: every one is named in the ask.

## 4 · Pinned final state (UGT anchor)

| Deliverable | Required contents (requirements) | Destination (exact) | Recipient(s) (exact) | Catalog write (reference only; never in the prompt) | Fed by |
|---|---|---|---|---|---|
| W1 register | one row per account (25): action, status (Cancel rows), deadline, owner, monthly cost; totals 6,706.49 and 1,249.04 (dossier §9.2) | a new Google Sheet in Robert's Drive (the Wind Down folder d_e5caf6a8c630421942ee59 is not writable for him) | Leonard, Arthur (W2) | gsheets_create_spreadsheet + gsheets_values_update | C0ADGSZKR3R/1771003267.448213; f_1326e66bcabfda8fd29e4a |
| W2 share | Leonard and Arthur can edit the register | the register file | leonard.hayes@harmonygames.co, arthur.blake@harmonygames.co (writer) | gdrive_share_file | C0ADGSZKR3R/1771003267.448213 |
| W3 Linear settling | Done: ENG-2438, ENG-2439, ENG-2440, ENG-2459, ENG-2460, ENG-2461, ENG-2463; Canceled: the 4 excluded issues; the rest stay open; a comment on each of the 28 issues | project 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a | — | linear_update_issue + linear_create_comment | 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a description; C0ADGSZKR3R/1771003267.448213 |
| W5 reply | the two monthly totals and the clashes: Slack downgrade to free (C0ADGSZKR3R/1770840054.486779), Slack cut to three paid seats (C0ADGSZKR3R/1770842405.931359), Google archiving after Feb 15 (C0ADGSZKR3R/1770933903.645709) vs Sunset's hold (robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>) | thread of C0ADGSZKR3R/1771003267.448213 | Leonard (EMPLOYEE_0038_SLACK_ID) | slack_post_message (thread_ts) | W1; robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> |

| Decision-ambiguity risk | Alternative a careful run could take | What pins it |
|---|---|---|
| register location | the Wind Down folder (d_e5caf6a8c630421942ee59) | Robert cannot see or write it (persona_view can-see NO); the ask says 'share it with me and Arthur as editors' (C0ADGSZKR3R/1771003267.448213), not a folder |
| which rules | Sherwood's checklist (robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com>); the Growth/UA page (page_ua_vendor_closeout) | the ask names 'Sunset's data checklist' and 'the conventions doc I just put in the Wind Down folder' (C0ADGSZKR3R/1771003267.448213); Sunset is the signed provider (robert@harmonygames.co/1856956532017091340) |
| reply place | a new #winddown message or a DM | the ask: 'reply here' (C0ADGSZKR3R/1771003267.448213); a thread reply or a channel message in #winddown both pass |
| settle vs leave | leaving all issues open until accounts close | the project description: 'Done once the account counts as closed in the register …, Canceled if it doesn't belong on the list, everything else stays open' (project of ENG-2438…ENG-2483, 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a) |
| act vs ask | cancelling accounts himself | the ask is the register, the issues and the reply; no rule asks Robert to cancel accounts on Feb 14 (C0ADGSZKR3R/1771003267.448213) |
| persona vs agent | 'I'll share it' in the prompt | §11: every write is asked of the assistant (C0ADGSZKR3R/1771003267.448213 asks Robert) |

### 4b · Canonical outcome (one acceptance class)

| Deliverable | Field | Fixed value (pinned, with locator) | Delegated by | Allowed equivalence class | Material / representational |
|---|---|---|---|---|---|
| W1 | kind/location | a spreadsheet Robert can share (C0ADGSZKR3R/1771003267.448213 'one sheet') | — | a Google Sheet (a Doc table also passes) in Robert's Drive | material |
| W1 | title | — (C0ADGSZKR3R/1771003267.448213 names none) | the ask names no title (C0ADGSZKR3R/1771003267.448213) | any title | representational |
| W1 | row set | the 25 accounts in dossier §9.2 (f_605121f4a36752645e0ac3; 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a) | — | any order; vendor-name variants (QuickBooks / Intuit QuickBooks); excluded accounts listed separately are fine | material |
| W1 | action | per dossier §9.2 (f_1326e66bcabfda8fd29e4a rule 4) | — | the four words or clear synonyms (Cancel; Keep; Move to Arthur's LLC/KubLLC card; Hold for Sunset) | material |
| W1 | status | Cancel rows only, per dossier §9.2 (f_1326e66bcabfda8fd29e4a rule 5) | — | Closed/Requested/Open or synonyms; blank or n/a on other rows | material |
| W1 | deadline | per dossier §9.2 (f_1326e66bcabfda8fd29e4a rule 6) | — | any date format; dash/blank where §9.2 has '—' | material |
| W1 | owner | per dossier §9.2 (f_1326e66bcabfda8fd29e4a rule 7) | — | first name or full name | material |
| W1 | monthly cost | per dossier §9.2 (f_1326e66bcabfda8fd29e4a rule 8) | — | to the cent, with or without $ | material |
| W1 | totals | 6,706.49 and 1,249.04 (f_1326e66bcabfda8fd29e4a rule 9) | — | to the cent; anywhere in the sheet | material |
| W1 | column order / formatting | — (C0ADGSZKR3R/1771003267.448213) | the ask lists the columns, not a layout (C0ADGSZKR3R/1771003267.448213) | any | representational |
| W2 | grantees + role | leonard.hayes@harmonygames.co, arthur.blake@harmonygames.co, editor (C0ADGSZKR3R/1771003267.448213) | — | direct share of the file | material |
| W3 | states | Done ENG-2438, ENG-2439, ENG-2440, ENG-2459, ENG-2460, ENG-2461, ENG-2463; Canceled ENG-2450, ENG-2454, ENG-2465, ENG-2466; others not Done/Canceled (3f0c6a52-ee13-4b1e-68e3-a74bcc33818a) | — | any open state (Todo, In Progress) for the rest | material |
| W3 | comment | one per issue saying what happens and by when (project description, ENG-2438…ENG-2483) | — | any wording that carries the action and the deadline | material (presence, content) |
| W5 | contents | both totals (6,706.49, 1,249.04) + exactly the three clashes under f_1326e66bcabfda8fd29e4a rule 10 (C0ADGSZKR3R/1771003267.448213) | — | any wording per clash; card moves, Oliver's Cursor request and the Gusto change are not clashes (rule 10) | material |
| W5 | wording | — (C0ADGSZKR3R/1771003267.448213) | the ask asks only for 'the two monthly totals and anything … that clashes' (C0ADGSZKR3R/1771003267.448213) | any wording | representational |

Rule for 08/09: two runs reach the same final state when every material field matches within its class. Persona approximations flagged by /injection (Typecast 'after the summer', Gusto 'on the 3rd') are not graded beyond what §9.2 states.

## 5 · Discovery map

| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |
|---|---|---|---|---|---|---|
| F1 the ask (LB) | own the register; columns; share as editors; settle issues with a line on each; reply with totals + clashes | C0ADGSZKR3R/1771003267.448213 | YES (member) | met first | none | Yes — as 'Leonard's close-out register ask' (anchor A1) |
| F2 keep list (LB) | keep Deel, gusto, Intuit; Figma; Linear | C0ADGSZKR3R/1770933601.686309 | YES | met first; amended by F3 | conclusive parent | No |
| F3 Gusto reply (LB) | gusto pulls from the bank on the 3rd; cancel before Mar 3 | C0ADGSZKR3R/1770948876.205117 | YES | overturns F2 for Gusto | replies rarely opened | No |
| F4 Leonard's subscriptions table | Kapwing, Zapier ticked, Carta 8/15, Slack down to 3 | C0ADGSZKR3R/1770933450.410449 | YES | context | table in an attachment | No |
| F5 LLC moves | github, dbt, Metabase to KubLLC | C0ADGSZKR3R/1770937232.664809 | YES | Hold wins for GitHub/dbt | redacted dbt token; comments confirm | No |
| F6 'covers everything' (trap) | P&L covers everything | C0ADGSZKR3R/1770933999.157259 | YES | overturned by F9/F12 | conclusion stop | No |
| F7 Sunset checklist (LB authority) | hold list; review call; Helpshift export | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | YES (own copy) | decoy Sherwood met first by date | Gmail rarely opened | No — the ask names it |
| F8 Sunset correction (LB) | Trello in, Metabase out, BigQuery and dbt in | robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> | YES | overturns F7 in part | second message of the thread | No |
| F9 conventions doc (LB authority) | rules 1–9 | f_1326e66bcabfda8fd29e4a | YES (shared) | decoy UA page | — | No — the ask names it |
| F10 SVB card (LB authority) | card description: closes Feb 20, move by Feb 19; Leonard's later comment on the card: closes the 18th, keep-rows off and every cancellation done by end of day the 17th | 698f48be4ba0affafbf153db + 698fa9f7f77cecfe5c7aa524 | YES (unscoped) | decoy Chase card | Trello rarely opened | No — the ask names 'SVB's card terms' |
| F11 review call (LB) | 2026-03-12 17:00Z | evt_f1d245d44ceff5a6e049c0 | YES (own calendar) | only via F7 | Calendar rarely opened | No |
| F12 costs tab (LB) | cost lines for membership; Sound and UA lines | f_605121f4a36752645e0ac3 | YES (shared) | stale December figures | copying costs from the tab | No |
| F13 founder relays of vendor confirmations (LB) | Cursor (#prototype reply to Oliver) and Unity (#executives) confirmed → Closed | C09UHHN6PFZ/1770991653.518204 + C07C2866011/1771017520.226917 | YES (member) | Leonard's AppLovin note (UA line, out of scope by rule 3) | outside #winddown and Linear | No |
| F14 Linear comments (LB) | decisive on 20 of 28 issues | 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a (e.g. cmt_bbdca23f075e9fca5cb8) | YES (unscoped) | titles/descriptions say nothing | no list call returns comments | No |
| F15 CodeRabbit notice (LB) | canceled Feb 12 | harmonygames-Games/Combo-Fighters#38#c_1 | YES (unscoped) | Arthur's 'cancelled' in Slack met first | bot comment on a PR | No |
| F16 Helpshift export (LB) | export done Feb 13 | cmt_96ae7b3689c1d073a2ff on ENG-2439 | YES (unscoped) | only via F7 | issue comments | No |
| F17 billing mail (LB) | Figma Sep 11 2026, Layer Mar 3, Pond5 ended Sep 8 2025, Soundly confirmation | robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com>; robert@harmonygames.co/<CAIoQDHYpNPHXVgnNS8DUmtr__81CmMffz7hcWJv@mail.gmail.com> | YES (own mailbox) | — | found by vendor name | No |
| F18 iPostal closed (trap) | mailbox closed Jan 16 | robert@harmonygames.co/1854432461283937829 | YES | tab still forecasts it | — | No |
| F19 ElevenLabs annual | $50, Jul 9 2025 – Jul 9 2026 | robert@harmonygames.co/1837122624854744558 | YES | — | — | No |
| F20 Singular cycle | quarterly invoices Sep 1, Dec 1; termination asks for confirmation | robert@harmonygames.co/1850283027022457279; robert@harmonygames.co/1853470745017478863 | YES | Mar 15 extension decoy | — | No |

## 5a · Search-as-persona proof

`persona_view.py search` reads only the base export, so seeded rows return 0 there; seeded reach is the dossier's check-sql PASS for robert (§1.E). Visible hits below are base counts.

| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |
|---|---|---|---|---|---|---|
| F1 | slack | close-out register | base 0; seeded 1 | 0 | C0ADGSZKR3R/1771003267.448213 | YES (seeded; check-sql YES) |
| F2 | slack | keep Deel | 1 | 0 | C0ADGSZKR3R/1770933601.686309 | YES |
| F3 | slack | gusto (thread of the keep list) | base 0; seeded 1 | 0 | C0ADGSZKR3R/1770948876.205117 | YES (seeded) |
| F4 | slack | latest and greatest on subscriptions | 1 | 0 | C0ADGSZKR3R/1770933450.410449 | YES |
| F5 | slack | KubLLC | 2 | 0 | C0ADGSZKR3R/1770937232.664809 | YES |
| F6 | slack | covers everything | 5 | 0 | C0ADGSZKR3R/1770933999.157259 (among the 5) | YES |
| F7 | gmail | data delivery checklist | base 0; seeded 1 thread | 0 | robert@harmonygames.co/1856965916492026238 | YES (seeded; own copy) |
| F8 | gmail | data delivery checklist (thread) | base 0; seeded 2nd message | 0 | robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> | YES (seeded) |
| F9 | gdocs | close-out | base 0; seeded 1 | 0 | f_1326e66bcabfda8fd29e4a | YES (seeded; shared) |
| F10 | trello | SVB | 3 base + seeded card | 0 | 698f48be4ba0affafbf153db | YES (unscoped) |
| F11 | gcal | Sunset | base 0; seeded 1 (own copy) | 0 | evt_f1d245d44ceff5a6e049c0 | YES (seeded) |
| F12 | gsheets | P&L and forecast | 7 | 8 | f_605121f4a36752645e0ac3 | YES |
| F13 | slack | cursor | 34 visible base | seeded 1 (thread reply) | C09UHHN6PFZ/1770991653.518204 | YES (member) |
| F14 | linear | Shutdown | base 0; seeded project | 0 | 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a | YES (seeded; unscoped) |
| F15 | github | coderabbit | 3 base + seeded PR comment | 0 | harmonygames-Games/Combo-Fighters#38#c_1 | YES (unscoped) |
| F16 | linear | Helpshift | 6 base + seeded issue | 0 | ENG-2439 | YES (unscoped) |
| F17 | gmail | Figma / Pond5 | Figma 78 base; Pond5 0 base + seeded | 0 | robert@harmonygames.co/<CAIoQDHYpNPHXVgnNS8DUmtr__81CmMffz7hcWJv@mail.gmail.com> | YES (own mailbox) |
| F18 | gmail | Mailbox Has Been Cancelled | 1 | 0 | robert@harmonygames.co/1854432461283937829 | YES |
| F19 | gmail | Eleven Labs | 3 | 0 | robert@harmonygames.co/1837122624854744558 | YES |
| F20 | gmail | Singular | 203 | 0 | robert@harmonygames.co/1853470745017478863 | YES |

```
SEARCH slack 'keep Deel' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C0ADGSZKR3R/1770933601.686309", "channel": "winddown", "kind": "private", "date": "2026-02-12", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "During shutdown, let’s keep Deel, gusto, Intuit. I canceled other subscriptions under mine. Figma won’t be able "}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'KubLLC' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=2 (showing 2)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UEQVDVB7/1691110103.263179", "channel": "admin_foundersonly", "kind": "private", "date": "2023-08-04", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "ullshit is for all of my accounts. So all of my payments at KubLLC failed."}
  {"id": "C0ADGSZKR3R/1770937232.664809", "channel": "winddown", "kind": "private", "date": "2026-02-12", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "I'll be moving github, [USERNAME_30019], and Metabase to my KubLLC card."}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'covers everything' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=5 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C05H8KVNU67/1732745367.787679", "channel": "game-design", "kind": "private", "date": "2024-11-27", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "But you probably got the gist of it. I think it covers everything that we discussed so far. "}
  {"id": "C07C2866011/1731376951.480519", "channel": "executives", "kind": "private", "date": "2024-11-12", "user": "EMPLOYEE_0038_SLACK_ID", "reply": true, "snippet": "I think this covers everything I wanted to say"}
  {"id": "C07C2866011/1762910093.015199", "channel": "executives", "kind": "private", "date": "2025-11-12", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "can you take a look and let me know if this covers everything we discussed with [USERNAME_21452]? <@EMPLOYEE_0016_SLACK_ID>"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'free version' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=13 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UEQVDVB7/1692659348.970159", "channel": "admin_foundersonly", "kind": "private", "date": "2023-08-21", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "Only artists, the rest of us can use free version I think"}
  {"id": "C04UTBZL6AX/1720480551.722149", "channel": "founders", "kind": "private", "date": "2024-07-08", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "I've gotten 10+ sound files from them already using free version, but out of quota now"}
  {"id": "C05H8KVNU67/1690573162.007359", "channel": "game-design", "kind": "private", "date": "2023-07-28", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "You get the free version to try out, 20 meetings a month"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'data delivery checklist' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Singular' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=203 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1780680268138518771", "last": "2023-10-24T17:00:02Z", "subject": "[ORG_NAME_0153]: This Week in Gaming 🎮", "snippet": "a is Coming to the Epic Games Store (link ([URL_13210]) ) * Singularity 6’s Cozy MMO Palia is joining the Epic Games Store for the first time as par"}
  {"id": "robert@harmonygames.co/1781207922334357403", "last": "2024-01-24T07:06:21Z", "subject": "Re: Harmony Games & Google Ads partnership", "snippet": "will populate the conversion that's already been setup, via Singular integration. You can see how this somehow magically appears b[USERNAME_35102]
  {"id": "robert@harmonygames.co/1784923294931494305", "last": "2023-12-10T19:11:40Z", "subject": "StartUp founders: Your Unfair Share of the Upswing", "snippet": "e whether IRR is measured in cash or time and then choose a Singular, quantifiable objective, be it revenue, users, retention, valuation, 
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Mailbox Has Been Cancelled' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1854432461283937829", "last": "2026-01-16T00:50:06Z", "subject": "Your Mailbox Has Been Cancelled", "snippet": "Your Mailbox Has Been Cancelled"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Eleven Labs' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=3 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1804054680638803177", "last": "2024-07-08T23:16:53Z", "subject": "[EMAIL_144452]", "snippet": " it's you  Thanks for using link on your recent purchase at Eleven Labs Inc.. To confirm it's you, please verify your email.  Verify your email : https"}
  {"id": "robert@harmonygames.co/1804054684178739572", "last": "2024-07-08T23:16:57Z", "subject": "Your receipt from Eleven Labs Inc. #2284-2469", "snippet": "Your receipt from Eleven Labs Inc. #2284-2469"}
  {"id": "robert@harmonygames.co/1837122624854744558", "last": "2025-07-08T23:17:42Z", "subject": "Your receipt from Eleven Labs Inc. #2185-9419-9007", "snippet": "Your receipt from Eleven Labs Inc. #2185-9419-9007"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Pond5' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Figma' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=78 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1761643434334829870", "last": "2023-03-28T20:08:17Z", "subject": "🔥🔥🔥 YOU DID IT 🔥🔥🔥", "snippet": "----- What’s next -----------  step 1: Install our plugins: Figma  ( https://track.bentonow.com/tracking/emails/0hMQHZO6QrX5PHDhtI4BCM2vUNqlnNZj/"}
  {"id": "robert@harmonygames.co/1762100015047284093", "last": "2023-04-02T21:05:26Z", "subject": "What did they say?", "snippet": " a few of them...    If you haven't already checked out our Figma plugin,   ( https://track.bentonow.com/tracking/emails/IB3T8c5Kn79ZKNqVDkNSZ5LI"}
  {"id": "robert@harmonygames.co/1774953681110019000", "last": "2023-08-22T18:08:52Z", "subject": "2 new notifications on Harmony Games since 5:07 PM (August 22, 2023)", "snippet": " you missed on Trello.  Leonard Hayes added you to the card Figma subscription (https://Trello.com/email/track/card?idMe
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Linear' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=400 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1761737352246507112", "last": "2023-03-29T21:01:04Z", "subject": "Arthur invited you to join Harmony Games on linear", "snippet": "Arthur invited you to join Harmony Games on linear"}
  {"id": "robert@harmonygames.co/1764981710299698577", "last": "2023-05-08T23:30:55Z", "subject": "Re: Document shared with you: \"GoD - Hero System Design\"", "snippet": "e these heroes on a progression pathway. This can be super  linear (like a leveling system) or more fuzzy. For something like [USE
  {"id": "robert@harmonygames.co/1771895396980728661", "last": "2023-07-26T22:35:42Z", "subject": "Re: Harmony Games <> PERSON_3127_NAME Sprint Planning Help", "snippet": "m on time.  We want to start with using tools like Trello + Linear but we're open to anything.  I have also CC'ed our game design 
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Soundly' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=15 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1808652468703166716", "last": "2024-08-28T17:16:45Z", "subject": "Welcome to Soundly!", "snippet": "Welcome to Soundly!"}
  {"id": "robert@harmonygames.co/1811934870143476810", "last": "2024-10-03T22:49:08Z", "subject": "We Freeze For Your Sound Effects!", "snippet": "                                                        New Soundly Pro Packages                                                                   "}
  {"id": "robert@harmonygames.co/1813817904058808447", "last": "2024-10-24T17:39:09Z", "subject": "She Possessed Us!", "snippet": "ike the legendary Wilhelm Scream, which we proudly added to Soundly not too long ago.                                  But why should Wilhelm have "}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Layer' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=727 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1763649866525949911", "last": "2023-04-20T03:34:21Z", "subject": "PERSON_3385_NAME <> [PERSON_NAME_0054] intro", "snippet": " style    *Summary*    The importance of creating a strong player experience in the gaming  industry, which involves both marketing and product 
  {"id": "robert@harmonygames.co/1763763696570067492", "last": "2023-05-23T21:50:59Z", "subject": "Re: Intros: [PERSON_NAME_0128] and PERSON_3687_NAME (Initial Capital) <> Leonard (Harmony Games)", "snippet": " aiming to achieve true AI/Designer co-creation to provide players the best possible experie
  {"id": "robert@harmonygames.co/1764276396494209330", "last": "2023-06-09T03:58:45Z", "subject": "Re: Thank You from Harmony Games!", "snippet": "d because you seem to care about the craft of game-making, player happiness, and the biz opportunity itself. We look forward to meeting the rest "}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'Unity Technologies' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=126 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1780753729824783874", "last": "2023-10-30T14:08:07Z", "subject": "Re: 2024 Headcount Planning", "snippet": "ding engineers from Google, Thoughtworks, Doordash, Reddit, Unity Technologies etc). Cheers,[PERSON_NAME_16716]: We're not a recruiting agency or a dev shop, "}
  {"id": "robert@harmonygames.co/1785096601705633362", "last": "2023-12-12T17:06:05Z", "subject": "Webinar: Maximizing your  game’s  potential with data-oriented design", "snippet": "eeing you There.   Keep creating,   The Unity team          Unity Technologies, 30 3rd Street, San Francisco, CA 94103,
  {"id": "robert@harmonygames.co/1785277436098871483", "last": "2023-12-14T17:00:42Z", "subject": "Greetings from Unity  👋🏽", "snippet": "12093a0&elqaid=35610&elqat=1&elqCampaignId=16895  Copyright Unity Technologies © 2020"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gdocs 'close-out' as robert  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gsheets 'P&L and forecast' as robert  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=7 (showing 3)  hidden by ACL=8 in 8 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_28ecc492b19f3696a19a97", "name": "Harmony Games P&L and forecast - Oct 2025.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Harmony Games P&L and forecast - Oct 2025"}
  {"id": "f_29467f8365d566d7bb2e76", "name": "Harmony Games P&L and forecast - Apr 2024.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Harmony Games P&L and forecast - Apr 2024"}
  {"id": "f_2cb4e217609f00a8ecf416", "name": "Harmony Games P&L and forecast - Oct 2024.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Harmony Games P&L and forecast - Oct 2024"}

SEARCH gsheets 'Subscriptions' as robert  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_31115ddb6ed866f2b10d60", "name": "Task List.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Cancel or move all software subscriptions"}

SEARCH gcal 'Sunset' as robert  scope: GCal event summary (base events carry no description/location)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
note: counted per meeting instance (ical_uid + start), visible if any copy is visible

SEARCH trello 'SVB' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=3 (showing 3)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/cards/162/name", "parent_pointer": "/cards/162", "encoding": "json", "text": "Reimbursement for founders - $150 for July health, also move other subscriptions to SVB", "truncated": false}
  {"file": "HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/cards/162/url", "parent_pointer": "/cards/162", "encoding": "json", "text": "https://PERSON_6092_TRELLO_USERNAME.com/c/Po9M85Ly/148-reimbursement-for-founders-150-for-july-health-also-mov
  {"file": "HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/cards/172/name", "parent_pointer": "/cards/172", "encoding": "json", "text": "SVB application", "truncated": false}

SEARCH linear 'Shutdown' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH confluence 'Helpshift' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=2 (showing 2)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json", "service_file": "confluence_working.json", "pointer": "/pages/29/body", "parent_pointer": "/pages/29", "encoding": "json", "text": "ipt and no re-link tooling.</p><ul><li>Ask whether they ever signed in with App
  {"file": "HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json", "service_file": "confluence_working.json", "pointer": "/page_versions/73/body", "parent_pointer": "/page_versions/73", "encoding": "json", "text": "ipt and no re-link tooling.</p><ul><li>Ask whether they ever si

SEARCH github 'coderabbit' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=3 (showing 3)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "HarmonyGames_GitHub/Services_Data/github/data.json", "service_file": "data.json", "pointer": "/commits/160/message", "parent_pointer": "/commits/160", "encoding": "json", "text": "Wrap debug logging in conditional compilation\n\nCo-authored-by: coderabbitai[bot] <SVC_0334_GITHUB_NOREPLY_EM
  {"file": "HarmonyGames_GitHub/Services_Data/github/data.json", "service_file": "data.json", "pointer": "/commits/338/message", "parent_pointer": "/commits/338", "encoding": "json", "text": "Fix the warning message copy-paste error.\n\nCo-authored-by: coderabbitai[bot] <SVC_0334_GITHUB_NOREPLY_EMAIL_
  {"file": "HarmonyGames_GitHub/Services_Data/github/data.json", "service_file": "data.json", "pointer": "/commits/864/message", "parent_pointer": "/commits/864", "encoding": "json", "text": "Refactor code from CodeRabbitAI suggestion\n\nRefactor code from CodeRabbitAI suggestion", "truncated": false}


SEARCH slack 'close-out register' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'latest and greatest on subscriptions' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C0ADGSZKR3R/1770933450.410449", "channel": "winddown", "kind": "private", "date": "2026-02-12", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "latest and greatest on subscriptions"}
note: --no-hidden: containers outside the persona's view were not scanned
```

## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · readable · unique · instructions-not-answer) | Inferable |
|---|---|---|---|---|
| R1–R6 register contents and rules | f_1326e66bcabfda8fd29e4a, robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>, 698f48be4ba0affafbf153db | deliverable: the register Leonard asked for | C0ADGSZKR3R/1771003267.448213 · YES · names each rule source by issuer · states rules, not cells | no — needs the anchor |
| R7 reply with totals + clashes | C0ADGSZKR3R/1771003267.448213 | deliverable: Leonard's reply | C0ADGSZKR3R/1771003267.448213 · YES · unique · asks, doesn't answer | no — needs the anchor |
| R8 share as editors | C0ADGSZKR3R/1771003267.448213 | recipients via the anchor | C0ADGSZKR3R/1771003267.448213 · YES | no |
| R9 Linear settling | 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a, f_1326e66bcabfda8fd29e4a | scope: the Linear issues in the anchor | C0ADGSZKR3R/1771003267.448213 'Settle each Linear issue as you go and leave a line on each' · YES · unique | no |

| Anchor | May be named |
|---|---|
| A1 | Leonard's close-out register ask; Leonard's #winddown request; the account close-out register |

## 7 · Dates and constraints

| Item | Absolute date or value | Source | Past fact or deadline |
|---|---|---|---|
| Leonard's ask | 2026-02-13T17:21Z | C0ADGSZKR3R/1771003267.448213 | past |
| Google accounts archived | after 2026-02-15 | C0ADGSZKR3R/1770933903.645709 | future (the register is due before it) |
| SVB card closes | 2026-02-20; moves by 2026-02-19 | 698f48be4ba0affafbf153db | future |
| Sunset review call | 2026-03-12 17:00Z | evt_f1d245d44ceff5a6e049c0 | future |
| Clock | 2026-02-14T00:00:00Z (Sat) | GEN_EXECUTION §3; latest seed ENG-2479 comment 2026-02-13T20:51Z | now |

## 8 · Difficulty levers

| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |
|---|---|---|---|---|
| Ambiguity | yes | yes | which accounts are in, which rule governs (Sunset vs Sherwood, conventions vs UA page) | the prompt points at the ask only; destination pinned by the ask (C0ADGSZKR3R/1771003267.448213) |
| Dynamic change | yes | yes | keep list → Gusto reply; checklist → correction; Slack 'cancelled' → vendor word | the prompt names neither the summary nor the correction |
| Multi-source | yes | yes | 10 services (Slack, Linear, Gmail, Trello, Docs, Sheets, Calendar, Confluence, GitHub, Drive) | no source named as an exact artifact beyond the anchor |
| Async | no | — | — | — |
| Error recovery | no | — | Friction: none | — |
| Access control | yes (minor) | no | the Wind Down folder (d_e5caf6a8c630421942ee59) is not visible; the register goes in Robert's Drive | the prompt does not ask for the folder |

## 9 · Must not appear in the prompt

- Tool / server names: gsheets_*, gdrive_share_file, linear_*, slack_*, gmail_*, trello_*, gcal_*, confluence_*, github_*, snowflake_*, any MCP server name.
- Ids: C0ADGSZKR3R/1771003267.448213, 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a, ENG-24xx keys, f_1326e66bcabfda8fd29e4a, 698f48be4ba0affafbf153db, evt_f1d245d44ceff5a6e049c0, harmonygames-Games/Combo-Fighters#38#c_1, f_605121f4a36752645e0ac3.
- Hidden authorities and their contents: Sunset's list or correction, the SVB dates, the conventions rules, the review date, the Helpshift page, CodeRabbit's notice.
- Findings: any account name, action, status, deadline, owner, cost, either total, the missing accounts, the clashes.
- Root causes: the P&L being incomplete, the Sound line, the AWS/UA exclusion, the costs-tab column, the keep-list amendment.
- Form: markdown, numbered steps, column lists beyond what Leonard asked, format rules.

## 10 · Entity traps

```

SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <marcus@harmonygames.co>', 'Marcus <github:PERSON_0396_GITHUB_USERNAME>']
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
ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
  persona: leonard_hayes - Co-founder & Creative Director / Executive
  slack      id=EMPLOYEE_0038_SLACK_ID, name=Leonard Hayes, real_name=Leonard Hayes, email=leonard.hayes@harmonygames.co, is_bot=False, deleted=False, messages=143292, first_post=2023-03-15, last_post=2026-02-13   [join: exact_email]
  gmail      mailbox=leonard.hayes@harmonygames.co, threads=17635, messages=22648, first=2023-03-15, last=2026-02-13, thread_filename_alias=['leonard@harmonygames.co']   [join: exact_email]
ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
  persona: arthur_blake - Co-founder & CTO / Executive
  slack      id=EMPLOYEE_0025_SLACK_ID, name=Arthur Blake, real_name=Arthur Blake, email=arthur.blake@harmonygames.co, is_bot=False, deleted=False, messages=38591, first_post=2023-03-20, last_post=2026-02-12   [join: exact_email]
  gmail      mailbox=arthur.blake@harmonygames.co, threads=4721, messages=6876, first=2023-03-23, last=2026-02-13, thread_filename_alias=['blake@harmonygames.co']   [join: exact_email]
ENTITY email:oliver.brooks@harmonygames.co  name=Oliver Brooks  kind=person  emails=['oliver.brooks@harmonygames.co']
  persona: oliver_brooks - Senior Game Engineer / Engineering
  slack      id=EMPLOYEE_0003_SLACK_ID, name=Oliver Brooks, real_name=Oliver Brooks, email=oliver.brooks@harmonygames.co, is_bot=False, deleted=False, messages=23993, first_post=2024-08-12, last_post=2026-02-12   [join: exact_email]
  gmail      mailbox=oliver.brooks@harmonygames.co, threads=1687, messages=2445, first=2024-08-08, last=2026-02-12, thread_filename_alias=['oliver@harmonygames.co']   [join: exact_email]
ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
  persona: robert - Co-Founder & Creative Director / Executive
  slack      id=EMPLOYEE_0016_SLACK_ID, name=Robert, real_name=Robert, email=robert@harmonygames.co, is_bot=False, deleted=False, messages=129939, first_post=2023-03-15, last_post=2026-02-13   [join: exact_email]
  gmail      mailbox=robert@harmonygames.co, threads=16233, messages=19169, first=2023-03-15, last=2026-02-13   [join: exact_email]
```

| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |
|---|---|---|---|
| Leonard Hayes leonard.hayes@harmonygames.co | — (mailbox files `leonard@…`) | alias only | leonard.hayes@harmonygames.co |
| Arthur Blake arthur.blake@harmonygames.co | 'Blake' in Leonard's table; mailbox files `blake@…` | same person | arthur.blake@harmonygames.co |
| Oliver Brooks oliver.brooks@harmonygames.co | Lauren Brooks lauren@harmonygames.co | different person | oliver.brooks@harmonygames.co |
| Sunset (provider, signed Feb 12) | Sherwood Partners (consulted); 'Sunset of Creative Reporting' mails | issuer | robert@harmonygames.co/1856956532017091340; robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com> |
| Marcus Bennett marcus.bennett@harmonygames.co | Marcus Lee, marcus@harmonygames.co | three Marcuses | marcus.bennett@harmonygames.co |

## 11 · Pre-submit checklist

- [ ] Robert's voice: short, lowercase-ok, plain; no spec-sheet layout or markdown
- [ ] names the anchor in plain words (Leonard's close-out register ask in #winddown) and nothing else by exact title or id
- [ ] asks the assistant (not 'I'll') to do the register, the sharing, the Linear settling and the reply
- [ ] says it's due before Leonard archives the Google accounts (after Feb 15)
- [ ] no account, rule, date, total or clash from §9
- [ ] no tool or server name; no numbered steps
- [ ] 20–4,000 words (aim 60–150)

## 12 · Blockers and routed defects

None blocking. Advisories carried from /injection (Audit-Report/0_injection_PASS.md): comment-only vendor facts (Cursor, Zapier, 1Password, Vercel, 'which card') must be findable — they are, in Linear comments (F14); persona approximations (Typecast, Gusto day) are not graded beyond §9.2 of the dossier.

## 13 · Self-review

Walked `Evals/1_Prompt_Eval.md` Phases 1–3 against this brief (§1.1 persona, §1.5 competency/skill/complexity, §2.1 UGT, §2.2 feasibility/ACL, §2.3 truthfulness, §2.6 clarity, §2.7 contrived register, §3.2 coherence).

| Area | Counter-reading | Resolution (evidence) |
|---|---|---|
| UGT | two destinations for the register (Wind Down folder vs own Drive) | Robert cannot see d_e5caf6a8c630421942ee59 (persona_view NO); the ask pins sharing, not a folder (C0ADGSZKR3R/1771003267.448213) — §4b W1 |
| UGT | 'reply here' could be a thread reply or a channel message | both are in #winddown and carry the same contents; §4b W5 accepts either (C0ADGSZKR3R/1771003267.448213) |
| Clarity | 'settle each Linear issue' could mean close every issue | the project description defines Done / Canceled / open (3f0c6a52-ee13-4b1e-68e3-a74bcc33818a) |
| Incorporation | the rule sources might not be incorporated | the ask names Sunset's data checklist, SVB's card terms and the conventions doc (C0ADGSZKR3R/1771003267.448213); each is readable (check-sql YES) and states rules, not answers (f_1326e66bcabfda8fd29e4a) |
| Truthfulness | a prompt premise like 'Leonard asked me yesterday' could be off | the ask is Fri Feb 13 17:21Z; clock is Sat Feb 14 00:00Z — 'yesterday'/'today' both ambiguous across time zones, so the prompt should say Friday (C0ADGSZKR3R/1770933903.645709 dates the archive plan) |
| Feasibility / ACL | the agent may need Leonard's/Arthur's billing mail | every needed fact is relayed in their Linear comments (unscoped; e.g. cmt_2238bd7d0a60d8e4f31c); writes: gsheets create, gdrive share, linear update/comment/create, slack post exist in Evals/references/tools/catalog.json |
| Contrived register | listing the register columns in the prompt reads as a spec sheet | the columns live in the ask (C0ADGSZKR3R/1771003267.448213); the prompt only points at it |

Unresolved: none.

```
STAGE GATE prompt-writing: PASS — Task_Authoring-2/task_inputs · 04_Prompt_Writing_Brief.md#4d03aef4a9b7 · blocking 0 · warnings 0 · checks 21
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Writing_Brief.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql, 03_Error_Async_Config.txt, 01a_Hardening_Report.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#fc9bc388ee2a, 01_Hardness_Manifest.json#a9e87d46b5ca, 01_Grounding_Dossier.md#fcb757f77b13)
[PASS] chain.error-async: upstream 'error-async' PASS pasted and current (03_Error_Async_Config.txt#617e2cd47eea)
[PASS] structure.sections: 14 required sections present and non-empty (04_Prompt_Writing_Brief.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Writing_Brief.md
[PASS] evidence.situation: 4/4 items carry a source pointer (min 100%)
[PASS] evidence.final_state: 25/25 items carry a source pointer (min 100%)
[PASS] evidence.discovery_map: 20/20 items carry a source pointer (min 100%)
[PASS] evidence.dates: 5/5 items carry a source pointer (min 100%)
[PASS] evidence.entity_traps: 5/5 items carry a source pointer (min 100%)
[PASS] tool.search_as_persona: 20 facts proven findable by persona_view search as robert
[PASS] reach.brief: 20 scoped load-bearing ids YES for robert
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] structure.canonical_outcome: canonical outcome table: 15 field(s), each fixed or delegated
[PASS] boundary.anchor_naming: 1 anchor-naming entry, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 6 evidenced counter-readings (of 7 found; need ≥ 6) in 04_Prompt_Writing_Brief.md
[PASS] review.coverage: self-review addresses all 6 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

