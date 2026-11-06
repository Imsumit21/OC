# Prompt Brief — robert_llc_takeover · prep
> Built 2026-11-05 from 00_Assigments.md, Working_Files/00_Task_Context.json, 01_Grounding_Dossier.md (injection rev2, SQL sha256 edf1fd903611, platform /injection PASS twice), 01_Universe_Inject.sql, 03_Error_Async_Config.txt (Friction: none), 01_Scenario_Design.md, 01_Hardness_Manifest.json · Persona view verified: all (check-sql PASS on every seeded load-bearing record; base records by persona_view search, §5a) · Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) · Robert's today: Saturday Feb 14, 2026.
> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human. No 02_Reference_Files_Manifest.md (no attachment) and no 01a_Hardening_Report.md (no run yet).

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
|---|---|---|
| Business function | Executive | Founders / Exec / Strategy in `Evals/references/rules/task_categories.md` (strategic decisions, executive coordination). The work also sits in Finance / Legal / HR / Ops (the competency): a founders' decision on what the new LLC takes, its three-month running cost and each founder's share. |
| Persona | Robert · robert@harmonygames.co · Co-founder & Creative Director (roster.json persona_key robert, department Executive) | Voice: short, plain, first person to his assistant, lower-key than Leonard (base posts e.g. C09UHHN6PFZ/1770865575.541589 'Daily challenges has 14 levels now'). Remit: one of three founders running the wind-down in #winddown (C0ADGSZKR3R/1770839322.836779 'Soundly canceled'); Combo Fighter is his game and he wants it self-sustaining (C07C2866011/1770084297.911029). Read scope: member of D04UP2L3E3S (Leonard DM), D04V95AAAHW (Arthur DM), C0ADGSZKR3R, C07C2866011, C09UHHN6PFZ, C05433XK267, C04UEQVDVB7, C09SWTHEMEW; his own mailbox and calendar; Drive files he owns or that are shared with him; Linear, GitHub, Trello, Confluence, Snowflake unscoped. |
| Competency | Finance | Budget and cost planning for the founders' LLC: monthly running cost of what it takes (March–May), who carries which bill, each founder's cash share (split email robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com>). Expected outputs: a cost plan sheet and the decision record on each candidate item. |
| Task skill | Planning and decision support | Exercised by: the take/stay/carried decision per item under the ground rules (f_1e468a9d69ea0f0a2001f5), the three-month plan sheet, and the recommendation with per-founder monthly cost in the reply to Leonard. Authoring: the plan sheet is an authored artifact. |
| Task type | long-horizon (Long Horizon; difficulty mode easy, V3 cap < 90 %; requester target < 85 % average, > 130 counted calls per run) | Services carrying weight: Slack (hub, Arthur's DM reply, #prototype status, #winddown lists, #executives posts, #admin_foundersonly 2023 posts, Jenkins #builds), Linear (37 issues, 37 notes, 74 per-issue writes), Gmail (split, billing, App Review), Drive/Docs/Sheets/Slides (ground rules, notes doc, draft, deck, the new sheet), Snowflake (REVENUE_DAILY, 2,284 rows), Trello (the moving rule), GitHub (#1917), GCal (Monday's call), Confluence (page_aws_infra). call_budget 190 (01_Hardness_Manifest.json); hardness_gate (extreme): PASS in the dossier. |

## 2 · Situation

| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |
|---|---|---|---|
| Leonard asks Robert, on Thursday night (Feb 12 21:40 PT), to decide what the founders' LLC takes from HG to keep Combo Fighter going, what it costs March–May and who pays, and to reply before Monday's call. | Robert (DM recipient) | D04UP2L3E3S/1770961200.890407 (row 6257a3c4456db0bd2aeb872619d7a364) | Arthur's own Kapwing notice (blake@harmonygames.co_1856962040028188034.json) and receipts; none is needed (each is restated in a Robert-visible note) |
| Leonard's candidate list is a Linear project with one issue per item, each with an owner note; the issues carry titles and short descriptions only. | Robert (Linear, unscoped) | 0fa95761-d59b-4ff4-a8a3-15df3210ca6e; ENG-2438…ENG-2474 | — |
| The monthly figures Robert meets first in #winddown, the notes doc and the draft are older than what the item owners say now. | Robert | C0ADGSZKR3R/1770680984.725779, C0ADGSZKR3R/1770933903.645709, f_a7af6f358dd5648c11a608, f_d996e4c434ce160dc52596 | — |

## 3 · Investigation → action

Questions to resolve (no answers here):
- Which candidates does the LLC take, which does a founder already carry, and which stay with HG, under the ground rules' tests and the keep-or-cancel decisions in #winddown?
- Does each of Domino Delights and Zombie Match pass the take test (January income from the warehouse's daily revenue table against what its hosting bills now)?
- What does each taken item bill per month now, going by whoever runs it — and is any monthly charge for a taken game missing from the project?
- What does each founder already pay personally, and what is each founder's monthly cash under Leonard's split email?
- Which items are claimed done but still owe a step, and what date does each step carry under the moving rule (own deadline, the sale, or March 1)?
- Is anything that looks like the founders' own actually a Harmony Games asset that goes through Sunset's sale?

Writes those answers feed: the plan sheet (rows, costs, payers, steps, owners, dates, the per-month shares); a call and a state on each project issue; a new issue for any plan line the project lacks; the reply to Leonard (recommendation, monthly cost each, link). Every write depends on the investigation.

## 4 · Pinned final state (UGT anchor)

| Deliverable | Required contents | Destination | Recipients | Catalog write | Fed by |
|---|---|---|---|---|---|
| Plan sheet (Google Sheet) (layout from f_d996e4c434ce160dc52596) | one row per item (the 37 issues + any missing monthly line) with Item, Game, Decision, Monthly cost, Paid by, Next step, Owner, By (the draft's columns, f_d996e4c434ce160dc52596); the three founders' shares per month | Robert's Drive root d_9f7ba94f7526d54d8482ba | shared with leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co | gsheets create + values update; gdrive move/share | every §3 question |
| Call on each issue | a comment with the decision (and why) on each of ENG-2438…ENG-2474; the state per the project description (Todo + assignee / Done / Canceled) | Linear project 0fa95761-d59b-4ff4-a8a3-15df3210ca6e | — (Leonard and Arthur read the project) | linear comment + issue update ×37 | decisions |
| Missing plan line | a new issue for any monthly line on the plan that the project lacks | Linear project 0fa95761-d59b-4ff4-a8a3-15df3210ca6e (team_ENG) | — | linear create issue | scope question |
| Reply to Leonard | what Robert would do and what it costs each founder a month; a link to the sheet | thread of D04UP2L3E3S/1770961200.890407 (thread_ts 1770961200.890407) in D04UP2L3E3S | Leonard (leonard.hayes@harmonygames.co) | slack send message (thread reply) | decisions, totals, the sheet |

Alternatives a careful run could defend (settled or accepted in §4b): a new top-level DM message instead of a thread reply (settled by the prompt: 'in that thread'); shares as the even third ($1,150) vs cash after carried costs (both accepted); GitHub's Linear state Done vs Canceled (both accepted; Arthur pays, the org stays HG's, robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com>); share role writer vs commenter/reader (delegated: 'share it with Blake and me'); one combined Metabase + dbt row (draft layout) vs two rows (both accepted).

### 4b · Canonical outcome (all fair outcomes)

| Deliverable | Field | Fixed value (or closed accepted set, with sources) | Delegated by (quoted span, or —) | Allowed equivalence class | Material / representational | Source |
|---|---|---|---|---|---|---|
| Plan sheet | location | in Robert's Drive root d_9f7ba94f7526d54d8482ba | 'keep it in your drive' (hub) | any subfolder of his root is not accepted; the root itself | material | D04UP2L3E3S/1770961200.890407 |
| Plan sheet | title | — | hub: 'lay the sheet out like my draft' | any title (e.g. 'LLC 90 days', 'LLC plan') | representational | D04UP2L3E3S/1770961200.890407 |
| Plan sheet | columns | Item · Game · Decision · Monthly cost · Paid by · Next step · Owner · By | hub: 'like my draft from Tuesday' | same columns; order and extra columns free | material (columns) / representational (order) | f_d996e4c434ce160dc52596 |
| Plan sheet | rows | 38 items: ENG-2438…ENG-2474 by title + the CF VO campaign | — | Metabase + dbt as one combined row also accepted (draft layout); non-charges (BoomBit test, CrazyGames licence) may appear as $0 HG lines | material | ENG-2438 |
| Plan sheet | Decision per row | LLC 7 · Founder 3 · HG 28 (solver/truth.json) | — | labels LLC / founder (Arthur) / HG or 'stays with HG' / 'Sunset's sale' | material | f_1e468a9d69ea0f0a2001f5 |
| Plan sheet | Monthly cost | DD prod account 140 · CF backend and auth stacks 62 · CF VO campaign 3,000 · Metabase 100 · dbt 100 · GitHub 48 · every other row 0 | — | $-formatted or plain; 3000 / 3,000 (the cap); Metabase + dbt combined 200 | material | D04V95AAAHW/1770952200.665739 |
| Plan sheet | Paid by | LLC for the three LLC-billed lines; Arthur for Metabase, dbt, GitHub; HG or blank for HG rows | — | 'the LLC', 'Arthur (Kub card)', 'HG' | material | robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> |
| Plan sheet | Next step / By | DD player support: get a support build approved and released before Helpshift stops (by Feb 28); layer.ai: export CF's art before access ends Mar 3; GitHub: repos transfer after the data is sold/delivered; CF and DD: through Sunset's sale, when it closes; LLC billing moves: by Mar 1 | Trello card 698e6548aa9516b76c4ab475 (moving rule) | any Feb 15–28 date for support; Mar 1–3 or 'before Mar 3' for layer.ai; 'when the sale closes' or a date tied to it for CF/DD | material (support, layer, GitHub) / representational (others) | 698e6548aa9516b76c4ab475 |
| Plan sheet | Owner | — | Trello: 'Whoever runs an item today moves it' | any defensible owner per that rule (e.g. Robert or Leonard for CF/DD; Arthur for AWS lines) | representational | 698e6548aa9516b76c4ab475 |
| Plan sheet | shares per month | total $3,450 (LLC cash $3,202 + Arthur's carried $248); third $1,150; cash Leonard $1,150, Robert $1,150, Arthur $902 | split email robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> | per-month figures, optionally with Mar–May totals (×3); any placement on the sheet | material | robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> |
| Plan sheet | sharing | leonard.hayes@harmonygames.co, arthur.blake@harmonygames.co | 'share it with Blake and me' (hub) | writer or commenter/reader | material (people) / representational (role) | D04UP2L3E3S/1770961200.890407 |
| Issue calls | comment per issue | the row's decision with a reason, on each of the 37 issues | 'leave your call on each issue too' (hub) | wording free | material (decision) / representational (wording) | D04UP2L3E3S/1770961200.890407 |
| Issue calls | state per issue | Todo + assignee for LLC rows; Done for Founder rows; Canceled for HG rows (project description) | — | GitHub: Done or Canceled; Calm Play LLC: Canceled (stays with HG) | material | ENG-2438 |
| Missing plan line | new issue | one issue for the CF VO campaign in 0fa95761-d59b-4ff4-a8a3-15df3210ca6e | prompt: the project matches the sheet | title naming the VO/Meta campaign or CF ads; any team_ENG state | material | team_ENG |
| Reply | destination | thread reply under D04UP2L3E3S/1770961200.890407 (D04UP2L3E3S, thread_ts 1770961200.890407) | prompt: 'in that thread' | — | material | D04UP2L3E3S/1770961200.890407 |
| Reply | monthly cost each | third $1,150 each and/or cash $1,150 / $1,150 / $902 (Leonard / Robert / Arthur); LLC cash $3,202 a month | hub: 'what it costs each of us a month' | either or both share readings | material | robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> |
| Reply | what Robert would do | DD comes over, ZM stays; the campaign is most of the cost; the support build still has to ship before Feb 28 | hub: 'what you'd do' | wording free; extra items fine | material (calls) / representational (wording) | D04UP2L3E3S/1770961200.890407 |
| Reply | link | a link to (or the name of) the plan sheet | hub: 'share it… tell me here' | a Drive link or the sheet's title | representational | D04UP2L3E3S/1770961200.890407 |

## 5 · Discovery map

Root cause and findings appear only here and never in the prompt.

| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |
|---|---|---|---|---|---|---|
| F1 Leonard's ask (scope, the ground rules, layout, Drive, split email, reply) | hub text | D04UP2L3E3S/1770961200.890407 | YES (DM member) | met first (the anchor) | — | Yes (anchor AN1: 'Leonard's DM') |
| F2 the candidate list | 37 issues ENG-2438…ENG-2474 | 0fa95761-d59b-4ff4-a8a3-15df3210ca6e | YES (unscoped) | met first | agents list issues but must open each issue's comments | Yes (anchor AN2: 'the LLC project in Linear') |
| F3 the rules: vehicle, window, take test, costing, keep/cancel, pay out, monthly only | ground rules | f_1e468a9d69ea0f0a2001f5 | YES (shared) | named by the hub | the older notes doc F4 also matches 'LLC' | No (hub incorporates it) |
| F4 older notes ('DD and ZM come with CF', '$1k') | superseded | f_a7af6f358dd5648c11a608 | YES (shared) | met first by a Drive 'LLC' search / overturned by F3 | stops at a conclusion-sounding note | No |
| F5 the layout (8 columns) | draft rows ~1000/300 (stale) | f_d996e4c434ce160dc52596 | YES (shared) | named by the hub ('my draft from Tuesday') | numbers copied as truth | No |
| F6 the split rule | a third each; carried costs count; shares per month | robert@harmonygames.co/1856989298688559716 | YES (INBOX) | named by the hub ('I'll email you') | — | No |
| F7 the moving rule (owner, own deadline, sale close, Mar 1) | Trello card | 698e6548aa9516b76c4ab475 | YES (unscoped) | named by the ground rules | Trello rarely opened | No |
| F8 Monday's call | Mon Feb 16 18:00–18:45Z | evt_f5f279f282d20ec86bb8e5 | YES (own calendar) | — | — | No (the prompt may say 'Monday's call') |
| F9 DD prod account $140 a month (never in the prompt) | $140 | D04V95AAAHW/1770952200.665739 | YES (DM member) | overturns C0ADGSZKR3R/1770680984.725779 (~$1k), C0ADGSZKR3R/1770682219.100789 (300), ENG-2441 note | reply under an unrelated Feb 2 root | No |
| F10 January income per game (never in the prompt) | DD 183.11 · CF 7.36 · ZM 0.00 | snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY | YES (unscoped) | decoy C09SWTHEMEW/1770725775.479449 (BoomBit's test view) | Snowflake rarely opened; sum the grain rows | No |
| F11 Arthur carries $248 (never in the prompt) | Metabase 100 · dbt 100 · GitHub 48 | robert@harmonygames.co/1856975772058401508 | YES (INBOX) | overturns C0ADGSZKR3R/1770933903.645709 (~$300) and ENG-2447 note | mail searched by tool name | No |
| F12 the VO campaign at $3,000 a month cap, moves to the LLC (never in the prompt) | $3,000 | C09UHHN6PFZ/1770938400.370665 | YES (#prototype member) | overturns C07C2866011/1770489896.754049 (both live) | outside every list; a thread reply | No |
| F13 Robert's deck (campaign rate) | ~$3k a month | f_7d2c9e7822e87b92a11759 | YES (owner) | supports F12 | — | No |
| F14 App Review rejection (never in the prompt) | email-draft support does nothing without a mail account | robert@harmonygames.co/1856994331853686118 | YES (INBOX) | overturns ENG-2462 'done' note | buried among App Store mail | No |
| F15 the 'done' claim on DD player support | Arthur's note | ENG-2462 | YES (unscoped) | met first / overturned by F14 | stops at 'done' | No |
| F16 PR #1917 merged | Replace Helpshift with support email | harmonygames-Games/GameOfDominoes#1917 | YES (unscoped) | supports the claim | merge read as release | No |
| F17 Jenkins DD iOS Submission #218 with the change | #218 | C05433XK267/1770932970.616709 | YES (#builds member) | ties F14 to the change | — | No |
| F18 Calm Play is HG's subsidiary (never in the prompt) | fully owned by Harmony Games | C04UEQVDVB7/1701383740.580749 | YES (#admin_foundersonly member) | overturns the ENG-2472 note | an older-channel search | No |
| F19 Calm Play note 'could just be our LLC' | claim | ENG-2472 | YES (unscoped) | met first / overturned by F18 | face value | No |
| F20 layer.ai access until March 3rd | Mar 3 | C09UHHN6PFZ/1770837702.167889 | YES (#prototype member) | own deadline beats Mar 1 | dated everything Mar 1 | No |
| F21 the subscription checklist (GitHub after data sold; Slack 3; Google Feb 15) | checklist | C0ADGSZKR3R/1770933450.410449 | YES (#winddown member) | — | — | No |
| F22 Helpshift stops; DD/ZM off before Feb 28 | Feb 28 | C0ADGSZKR3R/1770789534.434749 | YES (#winddown member) | the support item's deadline | NB-5 vendor date never used | No |
| F23 Arthur moves github, dbt, Metabase to his KubLLC card | payer | C0ADGSZKR3R/1770937232.664809 | YES (#winddown member) | connects F11 | — | No |
| F24 the lifestyle-route post | route | C07C2866011/1770612982.268919 | YES (#executives member) | cited by the ground rules | — | No |
| F25 IP to auction; the LLC buys what is left | vehicle | C07C2866011/1770850800.723979 | YES (#executives member) | cited by the ground rules | — | No |
| F26 AWS account layout (DD dev/prod, ZM one account, analytics) | layout | confluence:page_aws_infra | YES (unscoped) | — | Confluence rarely opened | No |
| F27 CF backend and auth stacks $62 (control) | $62 | ENG-2445 | YES (unscoped) | — | — | No |
| F28 Sunset liquidates laptops and build machines | HG asset | C07C2866011/1770839126.382429 | YES (#executives member) | with Arthur's ENG-2446 note | — | No |
| F29 Figma prepaid to Sep 11 | HG | C0ADGSZKR3R/1770859313.592649 | YES (#winddown member) | overturns the draft's Figma LLC row | — | No |
| F30 AppsFlyer free up to 15K installs | $0 | C0ADGSZKR3R/1770932709.222409 | YES (#winddown member) | with Leonard's ENG-2451 note | — | No |
| F31 the Unity Ads $100 (one-off) | one-off | C09UHHN6PFZ/1770845002.610529 | YES (#prototype member) | control (not monthly) | added as monthly | No |

## 5a · Search-as-persona proof

`persona_view.py search robert <service> "<query>"` reads base data; seeded rows Robert can see are counted from the SQL overlay (check-sql PASS for every scoped seeded record, dossier 1.E). Outputs verbatim below the table.

| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |
|---|---|---|---|---|---|---|
| F1 | slack | LLC | 283 base + 2 seeded | n/a (--no-hidden) | D04UP2L3E3S/1770961200.890407 | YES (seeded; check-sql YES) |
| F2 | linear | LLC take-over | 0 base + 1 seeded | 0 | 0fa95761-d59b-4ff4-a8a3-15df3210ca6e | YES (seeded; unscoped) |
| F3 | gdocs | ground rules | 0 base + 1 seeded | 1 | f_1e468a9d69ea0f0a2001f5 | YES (seeded; check-sql YES) |
| F4 | gdocs | LLC notes | 0 base + 1 seeded | 0 | f_a7af6f358dd5648c11a608 | YES (seeded; check-sql YES) |
| F5 | gsheets | LLC 90 days | 0 base + 1 seeded | 0 | f_d996e4c434ce160dc52596 | YES (seeded; check-sql YES) |
| F6 | gmail | LLC money | 0 base + 1 seeded | n/a (--no-hidden) | robert@harmonygames.co/1856989298688559716 | YES (seeded; check-sql YES) |
| F7 | trello | LLC | 9 base + 1 seeded | 0 | 698e6548aa9516b76c4ab475 | YES (seeded; unscoped) |
| F8 | gcal | LLC | 1 base + 1 seeded | 0 | evt_f5f279f282d20ec86bb8e5 | YES (seeded; check-sql YES) |
| F9 | slack | prod account | 0 base + 1 seeded | n/a (--no-hidden) | D04V95AAAHW/1770952200.665739 | YES (seeded; check-sql YES) |
| F10 | snowflake | REVENUE_DAILY | 10 base + 0 seeded | 0 | ANALYTICS.MONETIZATION.REVENUE_DAILY | YES (base hit) |
| F11 | gmail | metabase | 16 base + 1 seeded | n/a (--no-hidden) | robert@harmonygames.co/1856975772058401508 | YES (seeded; check-sql YES) |
| F12 | slack | meta campaigns | 10 base + 1 seeded | n/a (--no-hidden) | C09UHHN6PFZ/1770938400.370665 | YES (seeded; check-sql YES) |
| F13 | gslides | VO campaign | 0 base + 1 seeded | 0 | f_7d2c9e7822e87b92a11759 | YES (seeded; check-sql YES) |
| F14 | gmail | noticed an issue | 16 base + 1 seeded | n/a (--no-hidden) | robert@harmonygames.co/1856994331853686118 | YES (seeded; check-sql YES) |
| F15 | linear | player support | 0 base + 2 seeded | 0 | ENG-2462 | YES (seeded; unscoped) |
| F16 | github | Replace Helpshift | 0 base + 1 seeded | 0 | harmonygames-Games/GameOfDominoes#1917 | YES (seeded; unscoped) |
| F17 | slack | DD iOS Submission | 391 base + 2 seeded | n/a (--no-hidden) | C05433XK267/1770932970.616709 | YES (seeded; check-sql YES) |
| F18 | slack | calm play | 66 base + 0 seeded | n/a (--no-hidden) | C04UEQVDVB7/1701383740.580749 | YES (base hit) |
| F19 | linear | Calm Play | 1 base + 2 seeded | 0 | ENG-2472 | YES (seeded; unscoped) |
| F20 | slack | access until March | 1 base + 0 seeded | n/a (--no-hidden) | C09UHHN6PFZ/1770837702.167889 | YES (base hit) |
| F21 | slack | subscriptions | 21 base + 0 seeded | n/a (--no-hidden) | C0ADGSZKR3R/1770933450.410449 | YES (base hit) |
| F22 | slack | off Helpshift | 1 base + 0 seeded | n/a (--no-hidden) | C0ADGSZKR3R/1770789534.434749 | YES (base hit) |
| F23 | slack | KubLLC | 2 base + 0 seeded | n/a (--no-hidden) | C0ADGSZKR3R/1770937232.664809 | YES (base hit) |
| F24 | slack | lifestyle | 24 base + 0 seeded | n/a (--no-hidden) | C07C2866011/1770612982.268919 | YES (base hit) |
| F25 | slack | auction | 12 base + 0 seeded | n/a (--no-hidden) | C07C2866011/1770850800.723979 | YES (base hit) |
| F26 | confluence | AWS Infrastructure Guide | 10 base + 0 seeded | 0 | /pages/2/title | YES (base hits; target page_aws_infra reached by reading the hit's thread/table) |
| F27 | linear | backend and auth stacks | 0 base + 1 seeded | 0 | ENG-2445 | YES (seeded; unscoped) |
| F28 | slack | build machines | 12 base + 0 seeded | n/a (--no-hidden) | C07C2866011/1770839126.382429 | YES (base hit) |
| F29 | slack | Figma is good | 2 base + 0 seeded | n/a (--no-hidden) | C0ADGSZKR3R/1770859313.592649 | YES (base hit) |
| F30 | slack | 15K installs | 3 base + 0 seeded | n/a (--no-hidden) | C0ADGSZKR3R/1770932709.222409 | YES (base hit) |
| F31 | slack | $100 we have | 1 base + 0 seeded | n/a (--no-hidden) | C09UHHN6PFZ/1770845002.610529 | YES (base hit) |

```
SEARCH slack 'LLC' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=283 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=35 in 1 containers
  {"id": "C04RYU8TJ8K/1692814375.992619", "channel": "random", "kind": "public", "date": "2023-08-23", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "ards back in the 90s. You can read about that <http://baseballcardpedia.com/index.php/Hot_Pack|HERE> 2. We can have a meter that builds u
  {"id": "C04UEQVDVB7/1680118948.417789", "channel": "admin_foundersonly", "kind": "private", "date": "2023-03-29", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I sent invites to their llc account"}
  {"id": "C04UEQVDVB7/1680890962.773979", "channel": "admin_foundersonly", "kind": "private", "date": "2023-04-07", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": " we answered your question on whether we should pay to your LLC vs to [PERSON_NAME_0099] and [PERSON_NAME_0027] directly. Wh
  {"id": "C04UEQVDVB7/1681861642.621279", "channel": "admin_foundersonly", "kind": "private", "date": "2023-04-18", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "I think we had to do that for a multi person llc I did before"}
  {"id": "C04UEQVDVB7/1684894524.689149", "channel": "admin_foundersonly", "kind": "private", "date": "2023-05-24", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "lending for at least 3 months. I'm juggling payroll at Blakellc right now as we transition some of the team to a new contrac
  {"id": "C04UEQVDVB7/1684895469.212409", "channel": "admin_foundersonly", "kind": "private", "date": "2023-05-24", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "-5 months) Harmony Games could take him on as intern, Blake LLC could pay his wages. Then down the road Blake LLC would have
  {"id": "C04UEQVDVB7/1684895582.070269", "channel": "admin_foundersonly", "kind": "private", "date": "2023-05-24", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "maybe we can share the cost between the LLC and HG"}
  {"id": "C04UEQVDVB7/1684895678.238739", "channel": "admin_foundersonly", "kind": "private", "date": "2023-05-24", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": " at Unity you/we can decide whether we want him FT on HG or LLC"}
  {"id": "C04UEQVDVB7/1690583365.090569", "channel": "admin_foundersonly", "kind": "private", "date": "2023-07-28", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "its not clear if i enabled it just for Kub LLC"}
  {"id": "C04UEQVDVB7/1691110103.263179", "channel": "admin_foundersonly", "kind": "private", "date": "2023-08-04", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "shit is for all of my accounts. So all of my payments at KubLLC failed."}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH linear 'LLC take-over' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gdocs 'ground rules' as robert  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=1 in 1 containers  UNVERIFIED=0 in 0 containers

SEARCH gdocs 'LLC notes' as robert  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gsheets 'LLC 90 days' as robert  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gmail 'LLC money' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH trello 'LLC' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=9 (showing 9)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/cards/248/name", "parent_pointer": "/cards/248", "encoding": "json", "text": "Follow up with Michelle on LLC", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/cards/248/url", "parent_pointer": "/cards/248", "encoding": "json", "text": "https://PERSON_6092_TRELLO_USERNAME.com/c/SnCf8ZCz/234-follow-up-with-anne-on-llc", "tr
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/1345/data/card/name", "parent_pointer": "/actions/1345/data/card", "encoding": "json", "text": "Follow up with Michelle on LLC", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/1372/data/card/name", "parent_pointer": "/actions/1372/data/card", "encoding": "json", "text": "Follow up with Michelle on LLC", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/1373/data/card/name", "parent_pointer": "/actions/1373/data/card", "encoding": "json", "text": "Follow up with Michelle on LLC", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/1374/data/card/name", "parent_pointer": "/actions/1374/data/card", "encoding": "json", "text": "Follow up with Michelle on LLC", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/1375/data/card/name", "parent_pointer": "/actions/1375/data/card", "encoding": "json", "text": "Follow up with Michelle on LLC", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/1376/data/card/name", "parent_pointer": "/actions/1376/data/card", "encoding": "json", "text": "Follow up with Michelle on LLC", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/1549/data/card/name", "parent_pointer": "/actions/1549/data/card", "encoding": "json", "text": "Follow up with Michelle on LLC", "truncated": false}

SEARCH gcal 'LLC' as robert  scope: GCal event summary (base events carry no description/location)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "evt_40a22ce27369e2090178ac", "calendar": "robert@harmonygames.co", "start": "2024-05-29T12:00:00Z", "summary": "Franchise Tax to Delaware CalmPlay LLC", "status": "confirmed"}
note: counted per meeting instance (ical_uid + start), visible if any copy is visible

SEARCH slack 'prod account' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH snowflake 'REVENUE_DAILY' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=10 (showing 10)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/12/name", "parent_pointer": "/tables/12", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/12/id", "parent_pointer": "/tables/12", "encoding": "json", "text": "ANALYTICS.MONETIZATION.REVENUE_DAILY", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/name", "parent_pointer": "/tables/13", "encoding": "json", "text": "REVENUE_DAILY_V2", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/id", "parent_pointer": "/tables/13", "encoding": "json", "text": "ANALYTICS.MONETIZATION.REVENUE_DAILY_V2", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/rows/0/source_table", "parent_pointer": "/tables/13/rows/0", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/rows/1/source_table", "parent_pointer": "/tables/13/rows/1", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/rows/2/source_table", "parent_pointer": "/tables/13/rows/2", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/rows/3/source_table", "parent_pointer": "/tables/13/rows/3", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/rows/4/source_table", "parent_pointer": "/tables/13/rows/4", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/rows/5/source_table", "parent_pointer": "/tables/13/rows/5", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}

SEARCH gmail 'metabase' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=16 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1788727767998296782", "last": "2024-01-21T19:02:11Z", "subject": "You're invited to join Analytics's Metabase", "snippet": "You're invited to join Analytics's Metabase"}
  {"id": "robert@harmonygames.co/1788897102511219489", "last": "2024-01-23T15:53:40Z", "subject": "So you’ve got Metabase access. Now what?", "snippet": "So you’ve got Metabase access. Now what?"}
  {"id": "robert@harmonygames.co/1789078298591146308", "last": "2024-01-25T15:53:42Z", "subject": "Click your way to better analyses in Metabase", "snippet": "Click your way to better analyses in Metabase"}
  {"id": "robert@harmonygames.co/1789377175456507756", "last": "2024-01-28T23:00:11Z", "subject": "Asking a question in Metabase (with training wheels)", "snippet": "Asking a question in Metabase (with training wheels)"}
  {"id": "robert@harmonygames.co/1789558227616530284", "last": "2024-01-30T23:00:08Z", "subject": "Get your Metabase insights to come to you 💌 📊💫", "snippet": "Get your Metabase insights to come to you 💌 📊💫"}
  {"id": "robert@harmonygames.co/1789740637624362876", "last": "2024-02-01T23:21:18Z", "subject": "We've Noticed a New Metabase Login, [PERSON_NAME_0054]", "snippet": "We've Noticed a New Metabase Login, [PERSON_NAME_0054]"}
  {"id": "robert@harmonygames.co/1804483357332384538", "last": "2024-07-13T16:50:31Z", "subject": "We've Noticed a New Metabase Login, [PERSON_NAME_0054]", "snippet": "We've Noticed a New Metabase Login, [PERSON_NAME_0054]"}
  {"id": "robert@harmonygames.co/1810124385403073294", "last": "2024-09-19T17:02:58Z", "subject": "Re: Google cloud next steps", "snippet": "is no >>>>> cost or commitment obligation to you in year 1. Metabase is an open source, >>>>> under supported tool that will not scale as you grow, "}
  {"id": "robert@harmonygames.co/1812029960932351700", "last": "2024-10-05T00:00:33Z", "subject": "We've Noticed a New Metabase Login, [PERSON_NAME_0054]", "snippet": "We've Noticed a New Metabase Login, [PERSON_NAME_0054]"}
  {"id": "robert@harmonygames.co/1819525130937892848", "last": "2024-12-26T17:33:05Z", "subject": "We've Noticed a New Metabase Login, [PERSON_NAME_0054]", "snippet": "We've Noticed a New Metabase Login, [PERSON_NAME_0054]"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'meta campaigns' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=10 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UTBZL6AX/1683734312.616269", "channel": "founders", "kind": "private", "date": "2023-05-10", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "yeah, what do you call the meta campaigns, [USERNAME_50856]?"}
  {"id": "C07C2866011/1731364093.778039", "channel": "executives", "kind": "private", "date": "2024-11-11", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": "Looks like both the meta campaigns had roughly the same 1_5 completion."}
  {"id": "C07C2866011/1768265943.581399", "channel": "executives", "kind": "private", "date": "2026-01-13", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": " playtime, ~53 mins average daily playtime, ~4 CPI on broad meta campaigns • D1 retention is soft at 30% but we have clear levers: s
  {"id": "C07C2866011/1768266187.662249", "channel": "executives", "kind": "private", "date": "2026-01-13", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": " playtime, ~53 mins average daily playtime, ~4 CPI on broad meta campaigns • D1 retention is soft at 30% but we have clear levers: s
  {"id": "C07C2866011/1768266587.810349", "channel": "executives", "kind": "private", "date": "2026-01-13", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": " playtime, ~53 mins average daily playtime, ~4 CPI on broad meta campaigns • D1 retention is soft at 30%, but we’re addressing it th
  {"id": "C08MCEP1B9B/1728590927.786729", "channel": "node-[SOURCE_ORG_0001]-external", "kind": "private", "date": "2024-10-10", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": "any reason to wait for the app to be live before setting up meta campaigns in au, NZ, and CA? If not, you could
  {"id": "C08MCEP1B9B/1732037352.119439", "channel": "node-[SOURCE_ORG_0001]-external", "kind": "private", "date": "2024-11-19", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": "e in the Nordics is low so far. But it's worth getting some meta campaigns live in the Nordics as well to see i
  {"id": "C08MCEP1B9B/1732041535.736699", "channel": "node-[SOURCE_ORG_0001]-external", "kind": "private", "date": "2024-11-19", "user": "PERSON_0498_SLACK_ID", "reply": false, "snippet": "we are launching Google and meta campaigns in DK-FI-SW for $500/day  $200 - Google ads $300 - meta ads (split int
  {"id": "C08MCEP1B9B/1732228299.448739", "channel": "node-[SOURCE_ORG_0001]-external", "kind": "private", "date": "2024-11-21", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": " from Leonard we just set live on Unity. Can you add to our meta campaigns? It's less high octane than Leonard'
  {"id": "C08MCEP1B9B/1732742347.056739", "channel": "node-[SOURCE_ORG_0001]-external", "kind": "private", "date": "2024-11-27", "user": "EMPLOYEE_0008_SLACK_ID", "reply": false, "snippet": " for 250 daily Android installs. I unpaused the DK-SW-FI-NL meta campaigns and upped daily spend cap on Unity."
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gslides 'VO campaign' as robert  scope: GSlides title + page element text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gmail 'noticed an issue' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=16 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1786350758801586632", "last": "2023-12-26T13:20:37Z", "subject": "We noticed an issue with your submission.", "snippet": "We noticed an issue with your submission."}
  {"id": "robert@harmonygames.co/1788110939477958521", "last": "2024-01-14T23:37:56Z", "subject": "We noticed an issue with your submission.", "snippet": "We noticed an issue with your submission."}
  {"id": "robert@harmonygames.co/1788251073213806721", "last": "2024-01-16T12:45:18Z", "subject": "We noticed an issue with your submission.", "snippet": "We noticed an issue with your submission."}
  {"id": "robert@harmonygames.co/1811882996967331212", "last": "2024-10-03T09:04:37Z", "subject": "We noticed an issue with your submission.", "snippet": "We noticed an issue with your submission."}
  {"id": "robert@harmonygames.co/1811952781746959978", "last": "2024-10-04T03:33:49Z", "subject": "We noticed an issue with your submission.", "snippet": "We noticed an issue with your submission."}
  {"id": "robert@harmonygames.co/1813797589179151398", "last": "2024-10-24T12:16:15Z", "subject": "We noticed an issue with your submission.", "snippet": "We noticed an issue with your submission."}
  {"id": "robert@harmonygames.co/1829023437798416759", "last": "2025-04-10T13:44:35Z", "subject": "We noticed an issue with your submission.", "snippet": "We noticed an issue with your submission."}
  {"id": "robert@harmonygames.co/1829097434490129345", "last": "2025-04-11T09:20:44Z", "subject": "We noticed an issue with your submission.", "snippet": "We noticed an issue with your submission."}
  {"id": "robert@harmonygames.co/1833172857386240172", "last": "2025-05-26T08:57:50Z", "subject": "We noticed an issue with your submission.", "snippet": "We noticed an issue with your submission."}
  {"id": "robert@harmonygames.co/1836972401494127045", "last": "2025-07-07T07:29:57Z", "subject": "We noticed an issue with your submission.", "snippet": "We noticed an issue with your submission."}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH linear 'player support' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH github 'Replace Helpshift' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH slack 'DD iOS Submission' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=391 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C05433XK267/1727814307.024419", "channel": "builds", "kind": "public", "date": "2024-10-01", "user": "SLACK_BOT_0005_SLACK_ID", "reply": false, "snippet": "DD iOS Submission - #1 Started by user Arthur Blake (<http://blake.tplinkdns.com:9009/job/DD%20iO"}
  {"id": "C05433XK267/1727814751.496499", "channel": "builds", "kind": "public", "date": "2024-10-01", "user": "SLACK_BOT_0005_SLACK_ID", "reply": false, "snippet": "DD iOS Submission - #1 - Blake/switchToHarmony Failure after 16 min (<http://blake.tplinkdns.com:"}
  {"id": "C05433XK267/1727816143.508729", "channel": "builds", "kind": "public", "date": "2024-10-01", "user": "SLACK_BOT_0005_SLACK_ID", "reply": false, "snippet": "DD iOS Submission - #2 Started by user Arthur Blake (<http://blake.tplinkdns.com:9009/job/DD%20iO"}
  {"id": "C05433XK267/1727820305.497539", "channel": "builds", "kind": "public", "date": "2024-10-01", "user": "SLACK_BOT_0005_SLACK_ID", "reply": false, "snippet": "DD iOS Submission - #3 Started by user Arthur Blake (<http://blake.tplinkdns.com:9009/job/DD%20iO"}
  {"id": "C05433XK267/1727835659.610459", "channel": "builds", "kind": "public", "date": "2024-10-02", "user": "SLACK_BOT_0005_SLACK_ID", "reply": false, "snippet": "DD iOS Submission - #4 Started by user Arthur Blake (<http://blake.tplinkdns.com:9009/job/DD%20iO"}
  {"id": "C05433XK267/1727835987.799449", "channel": "builds", "kind": "public", "date": "2024-10-02", "user": "SLACK_BOT_0005_SLACK_ID", "reply": false, "snippet": "DD iOS Submission - #5 Unknown after 11 sec and counting (<http://blake.tplinkdns.com:9009/job/DD"}
  {"id": "C05433XK267/1727922367.809679", "channel": "builds", "kind": "public", "date": "2024-10-03", "user": "SLACK_BOT_0005_SLACK_ID", "reply": false, "snippet": "DD iOS Submission - #6 Started by user Arthur Blake (<http://blake.tplinkdns.com:9009/job/DD%20iO"}
  {"id": "C05433XK267/1727922699.991419", "channel": "builds", "kind": "public", "date": "2024-10-03", "user": "SLACK_BOT_0005_SLACK_ID", "reply": false, "snippet": "DD iOS Submission - #7 Started by changes from Arthur Blake (991 file(s) changed) (<http://blake."}
  {"id": "C05433XK267/1727925604.941589", "channel": "builds", "kind": "public", "date": "2024-10-03", "user": "SLACK_BOT_0005_SLACK_ID", "reply": false, "snippet": "DD iOS Submission - #8 Started by user Arthur Blake (<http://blake.tplinkdns.com:9009/job/DD%20iO"}
  {"id": "C05433XK267/1727960620.700819", "channel": "builds", "kind": "public", "date": "2024-10-03", "user": "SLACK_BOT_0005_SLACK_ID", "reply": false, "snippet": "DD iOS Submission - #9 Started by user Arthur Blake (<http://blake.tplinkdns.com:9009/job/DD%20iO"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'calm play' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=66 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UEQVDVB7/1701383740.580749", "channel": "admin_foundersonly", "kind": "private", "date": "2023-11-30", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "ing agreement to use Harmony Games IP. The stealth company, Calm Play LLC, will accomplish a couple of things • We will cont
  {"id": "C04UEQVDVB7/1701456721.772959", "channel": "admin_foundersonly", "kind": "private", "date": "2023-12-01", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "CALM PLAY LLC - De - Department of State_ Division Of Corporations - Formation Filing - L"}
  {"id": "C04UEQVDVB7/1701471874.741269", "channel": "admin_foundersonly", "kind": "private", "date": "2023-12-01", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "EIN number for Calm Play LLC in da house!!! *[SSN_16904]*"}
  {"id": "C04UEQVDVB7/1702067409.999069", "channel": "admin_foundersonly", "kind": "private", "date": "2023-12-08", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Calm Play LLC Privacy Policy"}
  {"id": "C04UEQVDVB7/1702067942.457799", "channel": "admin_foundersonly", "kind": "private", "date": "2023-12-08", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Calm Play LLC Terms of Serice"}
  {"id": "C04UEQVDVB7/1702068005.394379", "channel": "admin_foundersonly", "kind": "private", "date": "2023-12-08", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "ervices proudly adopted from dream games and cleaned up for Calm Play LLC lol"}
  {"id": "C04UEQVDVB7/1703492086.341779", "channel": "admin_foundersonly", "kind": "private", "date": "2023-12-25", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Paying the calm play llc invoice to [PERSON_NAME_104591]"}
  {"id": "C04UEQVDVB7/1703492127.063049", "channel": "admin_foundersonly", "kind": "private", "date": "2023-12-25", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": " couple more things on top of the regular LLC setup to make calm play full subsidiary of Harmony Games and can generate reve
  {"id": "C04UEQVDVB7/1710173103.244119", "channel": "admin_foundersonly", "kind": "private", "date": "2024-03-11", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "can you take care of calm play llc as well?"}
  {"id": "C04UEQVDVB7/1711748296.609699", "channel": "admin_foundersonly", "kind": "private", "date": "2024-03-29", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "<@EMPLOYEE_0025_SLACK_ID> to look into calm play llc tax thingy"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH linear 'Calm Play' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/3335/title", "parent_pointer": "/issues/3335", "encoding": "json", "text": "Migrate Zombie Match from Calm Play to Harmony Games", "truncated": false}

SEARCH slack 'access until March' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C09UHHN6PFZ/1770837702.167889", "channel": "prototype", "kind": "private", "date": "2026-02-11", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "er.ai|layer.ai> account <@EMPLOYEE_0033_SLACK_ID> - we have access until March 3rd"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'subscriptions' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=21 (showing 21)  hidden by ACL=None in 0 containers  UNVERIFIED=6 in 1 containers
  {"id": "C04S28HSD0U/1683122769.686439", "channel": "product", "kind": "private", "date": "2023-05-03", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "most season passes in games are just regular IAP instead of subscriptions?"}
  {"id": "C04S28HSD0U/1683124401.123719", "channel": "product", "kind": "private", "date": "2023-05-03", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "A couple reasons. 1- There is a bit of stigma on subscriptions among the gamers. You need to cancel them to stop paying and you can’t c
  {"id": "C04UEQVDVB7/1680203087.063829", "channel": "admin_foundersonly", "kind": "private", "date": "2023-03-30", "user": "EMPLOYEE_0038_SLACK_ID", "reply": true, "snippet": "Manage your subscriptions &amp; global settings - Google Groups Help"}
  {"id": "C04UEQVDVB7/1690515747.497039", "channel": "admin_foundersonly", "kind": "private", "date": "2023-07-28", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "ting reimbursed right? Some upwork stuff, laptops, and some subscriptions right?"}
  {"id": "C04UEQVDVB7/1690516955.800009", "channel": "admin_foundersonly", "kind": "private", "date": "2023-07-28", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Yeah. We need to move subscriptions over. "}
  {"id": "C04UTBZL6AX/1705263510.798269", "channel": "founders", "kind": "private", "date": "2024-01-14", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "ing consumable and non-consumable purchases, auto-renewable subscriptions, and free trials.  9. **Check for Common Issues**: If you en
  {"id": "C04UTBZL6AX/1705266501.850339", "channel": "founders", "kind": "private", "date": "2024-01-14", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "ou’ll be selling (like content, functionality, services, or subscriptions) and using AssetBundles for downloadable content if necessar
  {"id": "C050C9EPYKW/1693428360.106149", "channel": "teambuilding-foundersonly-archived", "kind": "private", "date": "2023-08-30", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "Might be better value than some of our software subscriptions"}
  {"id": "C050WGU41HR/1705702137.649979", "channel": "engineering-bots", "kind": "private", "date": "2024-01-19", "user": "SLACK_BOT_0004_SLACK_ID", "reply": false, "snippet": "a556adc48f1789a48612eab95a39c38583|7fe468a5>` - Adding ResetSubscriptions on startup since static vars are not always reset i
  {"id": "C05433XK267/1705702528.899219", "channel": "builds", "kind": "public", "date": "2024-01-19", "user": null, "reply": false, "snippet": "es Android Freestyle - #358 - master Changes: - Adding ResetSubscriptions on startup since static vars are not always reset in Unity right now. [Arthur B"}
  {"id": "C05433XK267/1705760401.866679", "channel": "builds", "kind": "public", "date": "2024-01-20", "user": "SLACK_BOT_0005_SLACK_ID", "reply": false, "snippet": "zles if level is not completed [Arthur Blake] - Adding ResetSubscriptions on startup since static vars are not always reset in Unity rig
  {"id": "C05433XK267/1705855245.399409", "channel": "builds", "kind": "public", "date": "2024-01-21", "user": null, "reply": false, "snippet": " Highlighting all of hand pile [Arthur Blake] - Adding ResetSubscriptions on startup since static vars are not always reset in Unity right now. [Arthur B"}
  {"id": "C05433XK267/1759863061.678629", "channel": "builds", "kind": "public", "date": "2025-10-07", "user": null, "reply": false, "snippet": "awned in endless mode [[PERSON_NAME_0068]] - Removed lambda subscriptions to prevent memory leaks on enable/disable [Calvin Price] - Stop tornado booster"}
  {"id": "C05433XK267/1759943637.607419", "channel": "builds", "kind": "public", "date": "2025-10-08", "user": null, "reply": false, "snippet": "rwriting whistle fix. [[PERSON_NAME_0055]] - Removed lambda subscriptions to prevent memory leaks on enable/disable [Calvin Price] - Update sorting layer"}
  {"id": "C05433XK267/1760025582.963369", "channel": "builds", "kind": "public", "date": "2025-10-09", "user": null, "reply": false, "snippet": "- #147 - [PERSON_NAME_0120]/auth  Changes: - Removed lambda subscriptions to prevent memory leaks on enable/disable [Calvin Price] - Logs [[PERSON_NAME_0"}
  {"id": "C05433XK267/1760026437.808949", "channel": "builds", "kind": "public", "date": "2025-10-09", "user": null, "reply": false, "snippet": "Android Submission - #148 - main  Changes: - Removed lambda subscriptions to prevent memory leaks on enable/disable [Calvin Price] - Update sorting layer"}
  {"id": "C07C2866011/1752552007.682869", "channel": "executives", "kind": "private", "date": "2025-07-15", "user": "EMPLOYEE_0038_SLACK_ID", "reply": true, "snippet": "ransferred, all users, statistics, data, comments, ratings, subscriptions, etc. that are related to the app are also transferred. We 
  {"id": "C0ADGSZKR3R/1770933450.410449", "channel": "winddown", "kind": "private", "date": "2026-02-12", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "latest and greatest on subscriptions"}
  {"id": "C0ADGSZKR3R/1770933601.686309", "channel": "winddown", "kind": "private", "date": "2026-02-12", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": " shutdown, let’s keep Deel, gusto, Intuit. I canceled other subscriptions under mine. Figma won’t be able to charge us by the time it’
  {"id": "C3C507EA71D6/1728276140.127629", "channel": "mpdm-robert--frederick.stone--leonard.hayes-1", "kind": "mpim", "date": "2024-10-07", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "ecret** is used when your app is integrated with iTunes for subscriptions and in-app purchases. You
  {"id": "D05UDNCCFEW/1705339175.681569", "channel": "D05UDNCCFEW", "kind": "im", "date": "2024-01-15", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "And you can manage all your various streaming subscriptions, and you can download iTunes games and play on TV"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'off Helpshift' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C0ADGSZKR3R/1770789534.434749", "channel": "winddown", "kind": "private", "date": "2026-02-11", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": " more to go. We gotta move domino delights and zombie match off Helpshift before Feb 28th. We can just open up the email app and let p
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'KubLLC' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=2 (showing 2)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UEQVDVB7/1691110103.263179", "channel": "admin_foundersonly", "kind": "private", "date": "2023-08-04", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "ullshit is for all of my accounts. So all of my payments at KubLLC failed."}
  {"id": "C0ADGSZKR3R/1770937232.664809", "channel": "winddown", "kind": "private", "date": "2026-02-12", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "I'll be moving github, [USERNAME_30019], and Metabase to my KubLLC card."}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'lifestyle' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=24 (showing 24)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UEQVDVB7/1681870011.424539", "channel": "admin_foundersonly", "kind": "private", "date": "2023-04-19", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "LA = lifestyle people, not serious workers but want cali pay"}
  {"id": "C04UTBZL6AX/1679620238.429969", "channel": "founders", "kind": "private", "date": "2023-03-24", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "Lifestyle companies as [PERSON_NAME_0036] calls it"}
  {"id": "C04UTBZL6AX/1682444722.353559", "channel": "founders", "kind": "private", "date": "2023-04-25", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "Probably would suit your lifestyle"}
  {"id": "C04UTBZL6AX/1692402311.442989", "channel": "founders", "kind": "private", "date": "2023-08-18", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "nd evolve in marketing or just the packaging, like \"healthy lifestyle\""}
  {"id": "C04UTBZL6AX/1699547874.178249", "channel": "founders", "kind": "private", "date": "2023-11-09", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "ng might be good for body but I don’t know if I will make a lifestyle out of it - as I said based on what I’ve read / listened / watch
  {"id": "C04UTBZL6AX/1706149035.136109", "channel": "founders", "kind": "private", "date": "2024-01-25", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "nvestorlife #dealmaker #lifebydesign #millionaire #mindset #lifestyle | [PERSON_NAME_134002] | Common · 1999 (Instrumental)"}
  {"id": "C050C9EPYKW/1690576240.442539", "channel": "teambuilding-foundersonly-archived", "kind": "private", "date": "2023-07-28", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "So I think he's probably hoping to match his current lifestyle"}
  {"id": "C050C9EPYKW/1690577246.559379", "channel": "teambuilding-foundersonly-archived", "kind": "private", "date": "2023-07-28", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "ean he tells us how much delta There is between his current lifestyle and what we offer"}
  {"id": "C050C9EPYKW/1692200784.514879", "channel": "teambuilding-foundersonly-archived", "kind": "private", "date": "2023-08-16", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "I wonder what lifestyle he has"}
  {"id": "C050C9EPYKW/1705020202.369549", "channel": "teambuilding-foundersonly-archived", "kind": "private", "date": "2024-01-12", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": " The man was brilliant, but he led an extremely destructive lifestyle.  He was known for destroying hotel ro
  {"id": "C050C9EPYKW/1721946319.595799", "channel": "teambuilding-foundersonly-archived", "kind": "private", "date": "2024-07-25", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "ding however he said he needs $150K to maintain his current lifestyle until the family likely moves to Orego
  {"id": "C050C9EPYKW/1723682796.290109", "channel": "teambuilding-foundersonly-archived", "kind": "private", "date": "2024-08-15", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "he is considering a more digital nomad lifestyle and getting away from Istanbul"}
  {"id": "C05KNDCHAAG/1764095181.719039", "channel": "company-internal", "kind": "private", "date": "2025-11-25", "user": "EMPLOYEE_0005_SLACK_ID", "reply": true, "snippet": "uld love to but Barbie is a drama-free, carefree beach type lifestyle brand. The most scandalous thing would be your shoe losin
  {"id": "C07C2866011/1739480541.508719", "channel": "executives", "kind": "private", "date": "2025-02-13", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Spykes is lifestyle for their founding team, they work hard but they don’t really have the speed or"}
  {"id": "C07C2866011/1765564977.275499", "channel": "executives", "kind": "private", "date": "2025-12-12", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "it sounds like a lifestyle biz idea. I think it may do OK. I personally don’t care about any physical phot"}
  {"id": "C07C2866011/1768337740.338379", "channel": "executives", "kind": "private", "date": "2026-01-13", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "new lifestyle I’m gonna embrace with Blake: <https://YouTube.com/shorts/1csTS0DUH9I?si=yTfFLt"}
  {"id": "C07C2866011/1768342512.143639", "channel": "executives", "kind": "private", "date": "2026-01-13", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "What is the lifestyle? It just seems like having lots of money"}
  {"id": "C07C2866011/1770237731.670189", "channel": "executives", "kind": "private", "date": "2026-02-04", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "s like [PERSON_NAME_5466] and I are willing to explore the “lifestyle biz” path if we can take out our assets and figure out if we c
  {"id": "C07C2866011/1770612982.268919", "channel": "executives", "kind": "private", "date": "2026-02-09", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "uss if you guys are ready to shut down and want to explore “lifestyle biz” route by shutting down Harmony Games and buying its asset
  {"id": "C09QDMC3UL9/1764867270.291679", "channel": "mattel_proposal", "kind": "private", "date": "2025-12-04", "user": "EMPLOYEE_0005_SLACK_ID", "reply": true, "snippet": "quely Barbie? • How does this respond to current cozy-sim / lifestyle trends?"}
  {"id": "C09QDMC3UL9/1764867488.235769", "channel": "mattel_proposal", "kind": "private", "date": "2025-12-04", "user": "EMPLOYEE_0005_SLACK_ID", "reply": true, "snippet": "ve beyond launch? • Could this evolve into a broader Barbie lifestyle platform? • How do you see the community interacting with 
  {"id": "C09QDMC3UL9/1765213543.355689", "channel": "mattel_proposal", "kind": "private", "date": "2025-12-08", "user": "EMPLOYEE_0038_SLACK_ID", "reply": true, "snippet": " • Strong overlap with players of fashion, home design, and lifestyle sim titles. • Comfortable with deeper collection, progress
  {"id": "C09QDMC3UL9/1765214562.505549", "channel": "mattel_proposal", "kind": "private", "date": "2025-12-08", "user": "EMPLOYEE_0038_SLACK_ID", "reply": true, "snippet": "Cats &amp; Soup and similar “watch your world run” games. • Lifestyle and decor titles in the home design and fashion space. The
  {"id": "D05GU6L0XFH/1744151048.527629", "channel": "D05GU6L0XFH", "kind": "im", "date": "2025-04-08", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "not... all these alternative lifestyle folks"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'auction' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=12 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04RYU8TJ8K/1685649654.886989", "channel": "random", "kind": "public", "date": "2023-06-01", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "I'm going to spend all of my time in the auction house"}
  {"id": "C04RYU8TJ8K/1701391761.119039", "channel": "random", "kind": "public", "date": "2023-12-01", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "ters to ensure you can get gold. What is gold good for? The Auction House. Upgrade items and gear. Perhaps more importantly, you can conve
  {"id": "C04UTBZL6AX/1683166802.506409", "channel": "founders", "kind": "private", "date": "2023-05-04", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "Fucking d3 auction house on blockchain"}
  {"id": "C04UTBZL6AX/1683734352.047129", "channel": "founders", "kind": "private", "date": "2023-05-10", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "ng strategies. These are automated bid strategies that use “auction-time bidding”—meaning Google will optimize for conversion or conve
  {"id": "C04UTBZL6AX/1701910693.722569", "channel": "founders", "kind": "private", "date": "2023-12-07", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "hauls back a couple pieces and auctions it off"}
  {"id": "C05M9QYMZUN/1696547881.840679", "channel": "industry-news", "kind": "public", "date": "2023-10-05", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "thesis here is either: 1. Has already been tested (Diablo 3 auction house), except he wouldn't know because he wasn't There to live
  {"id": "C05M9QYMZUN/1696547954.240609", "channel": "industry-news", "kind": "public", "date": "2023-10-05", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "And it's not just Diablo 3 Real money auction house, you can observe the digital goods economy if you once played World of Wa"}
  {"id": "C07C2866011/1759449301.151039", "channel": "executives", "kind": "private", "date": "2025-10-02", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": ". Even for aream it’s 1M+ min. Also bankers are good for an auction process.  For something like an acquihire they’re best done thro
  {"id": "C07C2866011/1770850800.723979", "channel": "executives", "kind": "private", "date": "2026-02-11", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "ich will cover majority of our costs • we wil put our IP to auction and if no one buys it we can buy via our LLC "}
  {"id": "C7442B7CD94B/1758316286.242589", "channel": "mpdm-leonard.hayes--person_r004--robert--frederick.stone-1", "kind": "mpim", "date": "2025-09-19", "user": "PERSON_3935_SLACK_ID", "reply": false, "snippet": "You’ll get penalized on the auction side"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH confluence 'AWS Infrastructure Guide' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=10 (showing 10)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json", "service_file": "confluence_working.json", "pointer": "/pages/1/body", "parent_pointer": "/pages/1", "encoding": "json", "text": ">AWS CDK (v2, TypeScript)</strong> - there is no click-ops
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json", "service_file": "confluence_working.json", "pointer": "/pages/2/title", "parent_pointer": "/pages/2", "encoding": "json", "text": "AWS Infrastructure Guide", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json", "service_file": "confluence_working.json", "pointer": "/pages/3/body", "parent_pointer": "/pages/3", "encoding": "json", "text": "ecture Overview\"/><ac:link-body>Architecture Overview</ac
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json", "service_file": "confluence_working.json", "pointer": "/pages/11/body", "parent_pointer": "/pages/11", "encoding": "json", "text": "ition game-api:317 --force-new-deployment]]></ac:plain-t
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json", "service_file": "confluence_working.json", "pointer": "/pages/12/body", "parent_pointer": "/pages/12", "encoding": "json", "text": " do not solo a database change during an incident.</p></
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json", "service_file": "confluence_working.json", "pointer": "/page_versions/10/body", "parent_pointer": "/page_versions/10", "encoding": "json", "text": "DK (v2, TypeScript)</strong> &mdash; the
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json", "service_file": "confluence_working.json", "pointer": "/page_versions/11/body", "parent_pointer": "/page_versions/11", "encoding": "json", "text": ">AWS CDK (v2, TypeScript)</strong> — the
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json", "service_file": "confluence_working.json", "pointer": "/page_versions/12/body", "parent_pointer": "/page_versions/12", "encoding": "json", "text": ">AWS CDK (v2, TypeScript)</strong> - the
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json", "service_file": "confluence_working.json", "pointer": "/page_versions/13/title", "parent_pointer": "/page_versions/13", "encoding": "json", "text": "AWS Infrastructure Guide", "truncated":
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json", "service_file": "confluence_working.json", "pointer": "/page_versions/14/title", "parent_pointer": "/page_versions/14", "encoding": "json", "text": "AWS Infrastructure Guide", "truncated":

SEARCH linear 'backend and auth stacks' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH slack 'build machines' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=12 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UEQVDVB7/1702667030.110309", "channel": "admin_foundersonly", "kind": "private", "date": "2023-12-15", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "you need to build the app with different config on your build machines you said, right?"}
  {"id": "C04UEQVDVB7/1712953203.606199", "channel": "admin_foundersonly", "kind": "private", "date": "2024-04-12", "user": "EMPLOYEE_0025_SLACK_ID", "reply": true, "snippet": "on't pay for crash tracking I added another license for the build machines so it went up a bit  Unity $1,665.00 / month githu
  {"id": "C04UEQVDVB7/1712956733.052449", "channel": "admin_foundersonly", "kind": "private", "date": "2024-04-12", "user": "EMPLOYEE_0025_SLACK_ID", "reply": true, "snippet": "Started the build machines on April 9th. [PERSON_NAME_24716] pays for his own. Samuel has a license. [PERS"}
  {"id": "C050WGU41HR/1723227691.998809", "channel": "engineering-bots", "kind": "private", "date": "2024-08-09", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "on the team will have to update at the same time (including build machines). The build system will also need some settings cha
  {"id": "C05V5FNLB9V/1746459179.836409", "channel": "god-bugs", "kind": "private", "date": "2025-05-05", "user": "EMPLOYEE_0025_SLACK_ID", "reply": true, "snippet": " had time to figure out the network setup to use it for the build machines."}
  {"id": "C07C2866011/1727120112.715749", "channel": "executives", "kind": "private", "date": "2024-09-23", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "are unblocked if you want to start working on reconfiguring build machines and shit lol"}
  {"id": "C07C2866011/1756846060.000679", "channel": "executives", "kind": "private", "date": "2025-09-02", "user": "EMPLOYEE_0025_SLACK_ID", "reply": true, "snippet": "t up. i just went outside to see what was going on when the build machines went down. i see the split cable just poking out of the gr
  {"id": "C07C2866011/1756911724.303409", "channel": "executives", "kind": "private", "date": "2025-09-03", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "fixing another thing on build machines"}
  {"id": "C07C2866011/1770839126.382429", "channel": "executives", "kind": "private", "date": "2026-02-11", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "they will liquidify all the assets including laptops build machines etc as well as IP"}
  {"id": "C08R27X0EAH/1759497680.776399", "channel": "zombie-bugs", "kind": "private", "date": "2025-10-03", "user": "EMPLOYEE_0032_SLACK_ID", "reply": true, "snippet": "hen we all switch to it and i guess we must to change it on build machines too <@EMPLOYEE_0025_SLACK_ID>"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'Figma is good' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=2 (showing 2)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C05H8KVNU67/1701369991.291769", "channel": "game-design", "kind": "private", "date": "2023-11-30", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "yeah, being good in Figma is good - will enable others"}
  {"id": "C0ADGSZKR3R/1770859313.592649", "channel": "winddown", "kind": "private", "date": "2026-02-12", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "Our Figma is good until September 11th"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack '15K installs' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=3 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UEQVDVB7/1713227957.407129", "channel": "admin_foundersonly", "kind": "private", "date": "2024-04-16", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "They are let us gonna exceed 15k installs "}
  {"id": "C069FF9Q57S/1710874378.412549", "channel": "analytics", "kind": "private", "date": "2024-03-19", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "e careful about <@EMPLOYEE_0016_SLACK_ID> is that after our 15K installs are over, Singular doesn’t have pay-as-you-go tiers it sound
  {"id": "C0ADGSZKR3R/1770932709.222409", "channel": "winddown", "kind": "private", "date": "2026-02-12", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "o another solution provider that offers data for free up to 15K installs"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack '$100 we have' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C09UHHN6PFZ/1770845002.610529", "channel": "prototype", "kind": "private", "date": "2026-02-11", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I am not gonna put $1K into this lol but happy to spend $100 we have on this"}
note: --no-hidden: containers outside the persona's view were not scanned
```

## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · persona-readable · unique · instructions-not-answer) | Inferable |
|---|---|---|---|---|
| decide each candidate under the ground rules | f_1e468a9d69ea0f0a2001f5 | scope (the LLC project; Leonard's ask) | hub D04UP2L3E3S/1770961200.890407 names 'the ground rules doc' · YES · one doc titled 'LLC ground rules' · rules, no answers | yes, once the hub is followed |
| the take test from the warehouse | snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY | none in the prompt (the ground rules name 'the warehouse's daily revenue table') | f_1e468a9d69ea0f0a2001f5 · YES · one daily revenue table (REVENUE_DAILY_V2 agrees) · names the table, not the sums | gotcha with a record trigger |
| cost each item at what it bills now, by its runner | ground rules | none | f_1e468a9d69ea0f0a2001f5 · YES · unique · rule only | gotcha with a record trigger |
| the split (a third each; carried counts) | robert@harmonygames.co/1856989298688559716 | deliverable (what it costs each of us a month) | hub 'I'll email you how we split the money' · YES · one mail 'LLC money' · rule, no figures | yes |
| owners and dates (own deadline, sale, Mar 1) | 698e6548aa9516b76c4ab475 | none | ground rules 'How things move is on the LLC card on our board' · YES · one card · rule only | gotcha with a record trigger |
| sheet layout | f_d996e4c434ce160dc52596 | deliverable (the sheet, like the draft) | hub 'lay the sheet out like my draft from Tuesday' · YES · one draft · layout (its numbers are stale) | yes |
| sheet in Robert's Drive, shared with Leonard and Arthur | hub | destination + recipients | hub · YES · — · instruction | yes (prompt restates it) |
| a call and a state on each issue | 0fa95761-d59b-4ff4-a8a3-15df3210ca6e description | deliverable (leave the call on each issue) | project description · YES · one project · state mapping only | yes |
| a new issue for the missing line | — | deliverable: the project ends up matching the sheet (prompt) | prompt sentence (no record names the campaign as missing) | needs the prompt trigger |
| reply in Leonard's thread with the per-founder cost | hub | destination (that thread) + content | hub 'tell me here' · YES · thread 1770961200.890407 · instruction | yes (prompt pins the thread) |

Anchor-name table (noun phrases of at most 6 words; `;` separates synonyms):

| Anchor | May be named |
|---|---|
| AN1 | Leonard's DM; Leonard's message from Thursday night |
| AN2 | the LLC project in Linear; the LLC take-over project |

## 7 · Dates and constraints

| Item | Absolute date or value | Source | Past fact or deadline |
|---|---|---|---|
| Robert's today | Saturday Feb 14, 2026 (clock 2026-02-14T00:00Z = Fri Feb 13 16:00 PT) | 00_Task_Context.json universe.persona_today; last #winddown post before the clock C0ADGSZKR3R/1770937460.360699 | — |
| Leonard's ask | Thu Feb 12, 2026 21:40 PT (2026-02-13T05:40Z) | D04UP2L3E3S/1770961200.890407 | past fact |
| the draft 'from Tuesday' | Tue Feb 10, 2026 10:30 PT (2026-02-10T18:30Z) | f_d996e4c434ce160dc52596 | past fact |
| Monday's call | Mon Feb 16, 2026 10:00–10:45 PT (18:00–18:45Z) | evt_f5f279f282d20ec86bb8e5 | deadline (future event) |
| the plan window | Mar 1 – May 31, 2026 | f_1e468a9d69ea0f0a2001f5 | plan field |
| Helpshift stops | before Feb 28, 2026 | C0ADGSZKR3R/1770789534.434749 | deadline |
| layer.ai access ends | Mar 3, 2026 | C09UHHN6PFZ/1770837702.167889 | deadline |
| Kapwing Pro ends | Feb 25, 2026 | ENG-2456 note comment_8c69b5b90f9f6c03a0a168d25e6b75bd | past decision / plan field |
| Figma prepaid | to Sep 11, 2026 | C0ADGSZKR3R/1770859313.592649 | plan field |
| shutdown premise | decided Feb 9–11, 2026; Sunset signed Feb 12 (wind-down acknowledged, no business as usual) | C0ADGSZKR3R/1770931777.561519 | past fact |

## 8 · Difficulty levers

| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |
|---|---|---|---|---|
| Ambiguity | yes | yes | the plan's population and figures live across Linear notes, Slack, Gmail, Snowflake (F9–F14) | the prompt names the anchors only, never where an answer lives |
| Dynamic change | yes | yes | older figures met first (#winddown, notes doc, draft, issue notes) and overturned later (F9, F11, F12, F14) | the prompt names neither the summary nor the correction |
| Multi-source | yes | yes | Slack, Linear, Gmail, Drive family, Snowflake, Trello, GitHub, Confluence | no source named as an exact artifact beyond the two anchors |
| Async | no | no | Friction: none (03_Error_Async_Config.txt) | — |
| Error recovery | no | no | Friction: none | — |
| Access control | no | no | every load-bearing record is Robert-visible (check-sql PASS) | no ask to read someone else's scoped data |

## 9 · Must not appear in the prompt

- **Tool and server names (catalog.json):** slack_send_message, slack_read_thread, slack_search_public_and_private, linear_list_issues, linear_list_comments, linear_create_comment, linear_update_issue, linear_create_issue, gsheets_create_spreadsheet, gsheets_values_update, gdrive_share_file, gdrive_move_file, gmail_search_messages, snowflake_execute_query, snowflake_list_tables, trello_get_card, github_get_pull_request, confluence_get_page, gcal_list_events; any MCP server name; 'the X tool'.
- **Opaque ids and filenames:** f_1e468a9d69ea0f0a2001f5, f_a7af6f358dd5648c11a608, f_d996e4c434ce160dc52596, f_7d2c9e7822e87b92a11759, 698e6548aa9516b76c4ab475, 0fa95761-d59b-4ff4-a8a3-15df3210ca6e, ENG-2438…ENG-2474, D04UP2L3E3S/1770961200.890407, D04V95AAAHW, C09UHHN6PFZ, robert@harmonygames.co/1856989298688559716, robert@harmonygames.co/1856975772058401508, robert@harmonygames.co/1856994331853686118, harmonygames-Games/GameOfDominoes#1917, #218, REVENUE_DAILY, page_aws_infra.
- **Findings and root causes (01 dossier):** DD's $140; DD's $183.11 January income; ZM's $0.00; Arthur's $248 and its parts; the VO campaign or any ad spend; the $3,000 cap; the App Store rejection or that support is not done; Calm Play's subsidiary status; layer.ai's Mar 3; GitHub after the data sale; every decision, total, share ($3,202, $3,450, $1,150, $902) or count (7/3/28).
- **Hidden authorities and rules:** the ground rules' contents (take test, costing rule, vehicle rule, window, pay out, monthly only), the warehouse or 'revenue table', the split rule, the Trello card or its moving rule, Arthur's DM or mail, Leonard's #prototype status, the Jenkins build.
- **Format and choreography:** markdown, numbered steps, a per-column content list, a service list, a call count, 'first … then …'.
- **Friction and files:** none configured; no reference files or /app/artifact paths.

## 10 · Entity traps

`entity.py collisions` and `entity.py resolve` for every name the prompt could use, verbatim:
```

SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <github:PERSON_0396_GITHUB_USERNAME>', 'Marcus <trello:c48a210d5c5a4b59231c6873>']
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

LOOKALIKE_EMAIL_LOCAL_PARTS (2)
  - 'thomas@' vs 'thomas.baker@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['Thomas Baker <thomas.baker@harmonygames.co>']
  - 'thomas@' vs 'thomaslee@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['? <thomaslee@harmonygames.co>']

TOKENS_MAPPING_TO_SEVERAL_ENTITIES (9)
  EMPLOYEE_0024: {'entities': ['scott <employee_0024@harmonygames.co>', '? <slack:EMPLOYEE_0024_SLACK_ID>', '? <trello:3d36d70154e6a715614e0d75>'], 'records': ['gcal.calendar_id=employee_0024@harmonygames.co', 'gcal.owner_email=employee_0024@harmonygames.co', 'linear.id=usr_EMPLOYEE_0024', 'linear.email=employee_0024@harmonygames.co', 'contacts.email=employee_0024@harmonygames.co', 'email.email=employee_0024@harmonygames.co', 'slack.id=EMPLOYEE_0024_SLACK_ID', 'trello.username=employee_0024']}
  EMPLOYEE_0032: {'entities': ['? <EMPLOYEE_0032_EMAIL>', 'Josh Dempsey <josh.dempsey@harmonygames.co>', '? <github:EMPLOYEE_0032_GITHUB_USERNAME>', '? <slack:EMPLOYEE_0032_SLACK_ID>'], 'records': ['confluence.id=user_EMPLOYEE_0032', 'gmail.mailbox=EMPLOYEE_0032_EMAIL', 'gdrive.email=EMPLOYEE_0032_EMAIL', 'linear.id=usr_EMPLOYEE_0032', 'linear.email=EMPLOYEE_0032_EMAIL', 'contacts.email=EMPLOYEE_0032_EMAIL', 'email.email=EMPLOYEE_0032_EMAIL', 'github.login=EMPLOYEE_0032_GITHUB_USERNAME', 'slack.id=EMPLOYEE_0032_SLACK_ID']}
  PERSON_2218: {'entities': ['? <PERSON_2218_EMAIL>', '? <github:PERSON_2218_GITHUB_USERNAME>'], 'records': ['linear.id=usr_PERSON_2218', 'linear.email=PERSON_2218_EMAIL', 'contacts.email=PERSON_2218_EMAIL', 'email.email=PERSON_2218_EMAIL', 'github.login=PERSON_2218_GITHUB_USERNAME']}
  PERSON_2360: {'entities': ['? <PERSON_2360_EMAIL>', 'Claire <github:PERSON_2360_GITHUB_USERNAME>'], 'records': ['github.login=PERSON_2360_GITHUB_USERNAME', 'email.email=PERSON_2360_EMAIL']}
### resolve Leonard
no exact match for 'Leonard'
  candidate: email:leonard.hayes@harmonygames.co  Leonard Hayes  ['leonard.hayes@harmonygames.co']
### resolve Blake
no exact match for 'Blake'
  candidate: email:arthur.blake@harmonygames.co  Arthur Blake  ['arthur.blake@harmonygames.co']
### resolve Arthur
no exact match for 'Arthur'
  candidate: email:arthur.blake@harmonygames.co  Arthur Blake  ['arthur.blake@harmonygames.co']
### resolve Robert
ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
  persona: robert - Co-Founder & Creative Director / Executive
  slack      id=EMPLOYEE_0016_SLACK_ID, name=Robert, real_name=Robert, email=robert@harmonygames.co, is_bot=False, deleted=False, messages=129939, first_post=2023-03-15, last_post=2026-02-13   [join: exact_email]
  gmail      mailbox=robert@harmonygames.co, threads=16233, messages=19169, first=2023-03-15, last=2026-02-13   [join: exact_email]
  gcal       calendar_id=robert@harmonygames.co, owner_email=robert@harmonygames.co, summary=Robert — primary, events=1229, last_event_before_clock=2026-02-12   [join: exact_email]
  gdrive     id=user_9f7ba94f7526, email=robert@harmonygames.co, display_name=Robert, root_folders=['d_9f7ba94f7526d54d8482ba'], owned_items=223, last_modified=2026-02-12, files_shared_with=464   [join: exact_email]
  linear     id=usr_Robert, email=robert@harmonygames.co, name=Robert, is_active=True, last_activity=2025-10-27   [join: exact_email]
  github     login=EMPLOYEE_0016_GITHUB_USERNAME, name=Robert, email=robert@harmonygames.co, type=User, last_activity=2026-01-16   [join: exact_email]
  trello     id=3d06b73654d0c8940792514c, username=robert, fullName=Robert   [join: exact_name]
  confluence id=user_EMPLOYEE_0016, account_id=acct_EMPLOYEE_0016, email=robert@harmonygames.co, display_name=Robert, is_active=True, last_activity=2026-02-12   [join: exact_email]
  contacts   contact_id=5f647df33ba6e92fbd56b05b, name=Robert, email=robert@harmonygames.co, job=Co-founder & Chief Product Officer, is_user=True   [join: exact_email]
  last activity: {'slack': '2026-02-13', 'gmail': '2026-02-13', 'gcal': '2026-02-12', 'gdrive': '2026-02-12', 'linear': '2025-10-27', 'github': '2026-01-16', 'confluence': '2026-02-12'}
### resolve Sunset
no exact match for 'Sunset'
```
| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |
|---|---|---|---|
| Leonard Hayes | 'Leonard' alone (no other Leonard) | co-founder; the hub's sender | leonard.hayes@harmonygames.co |
| Arthur Blake ('Blake') | 'Blake' used in Slack and docs; GitHub token EMPLOYEE_0025_GITHUB_USERNAME; mailbox alias blake@ (I03) | one person | arthur.blake@harmonygames.co |
| Robert | Linear id usr_Robert (I10) | the persona | robert@harmonygames.co |
| the LLC project | base projects 'GoD - Beta', 'Zombie Match 3D' | the only project named LLC | 0fa95761-d59b-4ff4-a8a3-15df3210ca6e (ENG-2438…ENG-2474, team_ENG) |
| LLC ground rules (doc) | 'LLC notes (Monday)' (older) | the hub names the ground rules | f_1e468a9d69ea0f0a2001f5 |
| Calm Play LLC | 'the LLC' (the founders' new one) | Calm Play is HG's subsidiary (C04UEQVDVB7/1701383740.580749) | ENG-2472 |
| ENG-2438…ENG-2474 | ZOM-### series (ZM team) | the project's issues are ENG | 0fa95761-d59b-4ff4-a8a3-15df3210ca6e |

## 11 · Pre-submit checklist

- [ ] Persona voice: Robert, first person, plain; no spec-sheet layout
- [ ] Names only the two anchors (§6 table); no §9 item
- [ ] States the deliverables: the sheet in his Drive like Leonard's draft, shared with Leonard and Blake; the call on each issue; the project matching the sheet; a reply in Leonard's thread
- [ ] No tool or server name; no step list; no count
- [ ] Wind-down acknowledged (no business as usual); Monday's call as the deadline
- [ ] Clean spelling and punctuation; no riddle, hint, hedge or if-chain
- [ ] 20–4,000 words
- [ ] Run `/create-prompt-writing check` before `/prompt`

## 12 · Blockers and routed defects

None blocking. No fact is routed to /create-injection: every §5 fact is found by a natural search or reached by reading the anchor's thread, table or project (§5a). Unverified: none. The platform /injection review of rev2 left A-4/A-5/A-6 for /prompt; each is settled by a dated record (dossier, Platform review section).

## 13 · Self-review

| Area | Counter-reading (strongest argument it fails) | Evidence that resolves it | Verdict |
|---|---|---|---|
| Fair readings (C6) | Reading B leaves the campaign off (it is Leonard's, not in the project). | C09UHHN6PFZ/1770938400.370665 'moves to the LLC from March … so count it in what the LLC costs'; the hub asks 'what it costs us March through May'; §4b fixes it as a row | settled |
| Fair readings (C6) | GitHub is HG (the org stays HG's) rather than Founder. | robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> 'I'm just paying the bill, so count it as mine like the other two'; §4b accepts Done or Canceled for the state | accepted outcomes |
| Clarity (C7) | 'tell me here' could be a new DM message, not a thread reply. | the prompt says 'in that thread' (§4b destination); thread_ts 1770961200.890407 | settled |
| Clarity (C7) | 'share it with Blake and me' leaves the share role open. | §4b: writer or reader accepted (representational) | accepted outcomes |
| Incorporation (C8) | the ground rules doc could be confused with the older notes doc. | one doc titled 'LLC ground rules' (f_1e468a9d69ea0f0a2001f5); the notes doc is 'LLC notes (Monday)' (f_a7af6f358dd5648c11a608) and older | unique |
| Incorporation (C8) | the new-issue requirement has no record trigger. | the prompt carries it as 'the project ends up matching the sheet' (§6); no record states the campaign is missing | trigger in the prompt |
| Truthfulness (C17) | 'Thursday night' or 'Tuesday' could be the wrong day. | hub D04UP2L3E3S/1770961200.890407 = Thu Feb 12 21:40 PT; draft f_d996e4c434ce160dc52596 = Tue Feb 10 10:30 PT | true |
| Truthfulness (C17) | naming 'Blake' could resolve to someone else. | entity.py resolve 'Blake' → arthur.blake@harmonygames.co only (§10) | true |
| Feasibility / ACL (C18–C19) | the sheet must be in Robert's Drive root and shared; a copy of Leonard's draft would be owned by Leonard. | gsheets create (owner = Robert) + gdrive move to d_9f7ba94f7526d54d8482ba + gdrive share; never edit Leonard's draft | feasible |
| Feasibility / ACL (C18–C19) | a deciding fact could sit in a mailbox Robert cannot read. | check-sql PASS (dossier 1.E): the split, billing and App Review mails are Robert's INBOX copies | feasible |
| Contrived register (C15–C16) | 'make sure the project matches the sheet' could read as a hint that something is missing. | it is a completeness instruction for a deliverable (the project is the decision record), names no item, cause or count (prompt_qc_cases trap_hint_or_riddle: naming a symptom or a deliverable is fine) | ordinary |
| Contrived register (C15–C16) | listing four deliverables could read as a command list. | deliverables and who to tell are the screen-24 skeleton, not sequenced method steps (C15) | ordinary |

Fair readings, clarity, incorporation, truthfulness, feasibility / ACL and the contrived register are each addressed above with evidence. Unresolved: none; the prompt is not yet written (draft or human), and check mode re-tests every point on the actual text.

```
STAGE GATE prompt-writing: PASS — Task_Authoring/task_inputs · 04_Prompt_Writing_Brief.md#75df2d4fffd6 · 00_Assigments.md#97be9960492b · 01_Grounding_Dossier.md#b5ecaa709bea · 01_Universe_Inject.sql#edf1fd903611 · 03_Error_Async_Config.txt#08fb87a4b11f · __context__#226493b2011a · __assignment__#b4220a529c0a · __policy__#dc4ab5df3cdd · __gate_policy__#115714063000 · __review__#65afaa257571 · blocking 0 · warnings 0 · checks 24
[PASS] assignment.v3_context: Robert / Co-founder & Creative Director; easy cap <90%; freeze 2026-02-14T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe normal; KB bound; clock Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Writing_Brief.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql, 03_Error_Async_Config.txt)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#edf1fd903611, 01_Hardness_Manifest.json#e3aef693644d, 01_Grounding_Dossier.md#b5ecaa709bea, solver/solver.py#1f7bb0a502ad, 01c_Dispositions.json#9849267e3b62, 01c_Preflight_Report.json#4759139c2a6f, 00_Assigments.md#97be9960492b, 01_Scenario_Design.md#fbd6167fad15, 01_Hardness_Manifest.draft.json#a0c1e6ecaa00, 01_Gradable_Surface.json#ba791eaea9ec, __context__#226493b2011a, __assignment__#b4220a529c0a, __policy__#dc4ab5df3cdd, __gate_policy__#115714063000, __review__#ee46d7814b64)
[PASS] chain.error-async: upstream 'error-async' PASS pasted and current (03_Error_Async_Config.txt#08fb87a4b11f, 00_Assigments.md#97be9960492b, 01_Grounding_Dossier.md#b5ecaa709bea, 01_Universe_Inject.sql#edf1fd903611, __context__#226493b2011a, __assignment__#b4220a529c0a, __policy__#dc4ab5df3cdd, __gate_policy__#115714063000, __review__#ee46d7814b64)
[PASS] structure.sections: 14 required sections present and non-empty (04_Prompt_Writing_Brief.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Writing_Brief.md
[PASS] evidence.situation: 3/3 items carry a source pointer (min 100%)
[PASS] evidence.final_state: 22/22 items carry a source pointer (min 100%)
[PASS] evidence.discovery_map: 31/31 items carry a source pointer (min 100%)
[PASS] evidence.dates: 10/10 items carry a source pointer (min 100%)
[PASS] evidence.entity_traps: 7/7 items carry a source pointer (min 100%)
[PASS] tool.search_as_persona: 31 facts proven findable by persona_view search as robert
[PASS] reach.brief: 28 scoped load-bearing ids YES for robert
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] structure.accepted_outcomes: V3 accepts multiple fair outcomes; see v3.fair_outcomes_review
[PASS] boundary.anchor_naming: 2 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 12 evidenced counter-readings (of 12 found; need ≥ 6) in 04_Prompt_Writing_Brief.md
[PASS] review.coverage: self-review addresses all 6 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.fair_outcomes_review: current accepted outcomes and considered alternatives recorded; multiple fair outcomes are allowed
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

