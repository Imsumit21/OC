# Prompt Brief — owen_dd_bug_carryover · prep
> Built 2026-11-08 from 00_Assigments.md, Working_Files/00_Task_Context.json, 01_Grounding_Dossier.md (injection rev7; rev2 and rev4 failed /prompt on data findings, rev3 failed /injection on two join rows, rev5 passed both, rev6 added second carriers for four corrections and failed /prompt on the tooltips thread, rev7 closed that thread and passed /prompt 5 but failed /hardness 1, rev8 removed Brian's Apple line and failed /hardness 2, rev9 removes his Tavern line and moves his Daily Gift note into his DM), 01_Scenario_Design.md, 01_Hardness_Manifest.json, 03_Error_Async_Config.txt (Friction: none) · Persona view verified: all (check-sql PASS, §5a)
> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human. No 02_Reference_Files: the scenario needs no attachment.

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
|---|---|---|
| Business function | Engineering | Engineering & Live-Ops in `Evals/references/rules/task_categories.md` (engineering delivery, releases, incidents, live game operations): Domino Delights' bug record and its live build. |
| Persona | Owen Baker · owen.baker@harmonygames.co · Game Engineer (Unity) (roster.json persona_key owen_baker, department Engineering) | Voice: short and plain, first person to his assistant, as in CE156FDFB428/1763549617.765149 'Should be fixed now'. Remit: he holds 16 of the 28 UI children (ENG-2417, ENG-2432), fixed canvas lines himself and owns the flicker and music threads (C05V5FNLB9V/1764659550.713509). Read scope: his DMs D05S1S2AB5M, D05USBTQY1F, D07E9PSQB6W, the group DM C9CA62B5180A, channels CE156FDFB428, C05V5FNLB9V, C05433XK267, C09Q4S613CN, C09SWTHEMEW, his mailbox, calendar and Drive. |
| Competency | Engineering Ops | Epic and task management: the bug record moves into the tracker and the ENG-2401 tree is closed out. Arthur asks him because he worked the list (hub D05S1S2AB5M/1770937805.214409). |
| Task skill | Actions | Exercised by 68 new tickets, 2 notes on reused tickets, 14 child moves, 28 child notes, the sheet, its sharing and the reply. Retrieval and reconciliation stack under it. |
| Task type | long-horizon (Long Horizon; difficulty mode medium, V3 cap < 85 %; requester target < 80 % average, > 130 counted calls per run) | Services carrying weight: Slack (63 canvas lines, 7 later posts, corrections), Linear (28 children, 13 notes, every write), GitHub (10 PRs, 2 inline comments), Docs (rule doc, economy doc), Drive, Sheets, Slides, Trello, Gmail, Calendar. Call budget 285 (01_Hardness_Manifest.json); the prompt states no count. |

## 2 · Situation

| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |
|---|---|---|---|
| Slack is about to drop to the free plan and take DD's bug history with it; Arthur asks Owen to move the whole list into Linear. | Owen (DM recipient) | D05S1S2AB5M/1770937805.214409 | — |
| The list lives as a Slack canvas comment channel and later posts, with ticks that may not match where each bug stands today. | Owen | CE156FDFB428/1763041126.468099; C05V5FNLB9V/1764256187.655299 | — |
| The UI Changes tree never got closed out: children sit in PR, Validation or In Progress long after the work ended. | Owen (Linear, unscoped) | ENG-2401; ENG-2417 | — |
| Only one record names the public build by number, and Owen can't see it. | Arthur, Leonard | the rule doc names 0.3.310 for Owen: f_3ca9e15d7b20f4e681ad52 | D04UGG61DUM/1770846601.876869 (not needed: the rule doc is the authority) |

## 3 · Investigation → action

Questions to resolve (no answers here):
- Which lines and posts are in scope, and which channels stay out?
- Which outcome does each bug get under the carry-over notes' first-fit order, going by the build players have?
- Does any later record, in any channel, DM or mailbox, change what a tick or an open thread says?
- Which fixes actually reached that build?
- Is any line already covered by an open ticket?
- Which open UI children have part of their screen missing from that build?
- What does each child's note have to say?
- Who is on Sunday's review?
- Has anything changed since the notes were written?

Writes those answers feed: one Linear record per bug, a note on any reused ticket, a state and a line on each child, the sheet and its sharing, the reply. Every write depends on the investigation.

## 4 · Pinned final state (UGT anchor)

| Deliverable | Required contents | Destination | Recipients | Catalog write | Fed by |
|---|---|---|---|---|---|
| New tickets | one per bug that gets a new record, fields per f_3ca9e15d7b20f4e681ad52 and comment_49b5ac4788465f72ddf245e34f2b7034 | Linear team_ENG, parent ENG-2401 | — | linear_create_issue | outcome of each line |
| Notes on reused tickets | the canvas wording | ENG-2073, ENG-2363 | — | linear_create_comment | ties to open tickets |
| Child moves | open children whose screen is all in the build go Done | children of ENG-2403, ENG-2404, ENG-2405 | — | linear_update_issue | tree question |
| A line on every child | where it landed, naming the build (690b29bc3c7d2e51b0f86a47) | all 28 children, ENG-2409 to ENG-2437 | — | linear_create_comment | tree question |
| Sheet | columns Bug, Outcome, Ticket, Why; one row per bug | Owen's folder d_9b41e7c2a05d36f8e1c7a4 | arthur.blake@harmonygames.co, robert@harmonygames.co, oliver.brooks@harmonygames.co (evt_6e2c91d4b07f3a58c1d2e4) | gsheets_create_spreadsheet, gsheets_values_update, gdrive_move_file, gdrive_share_file | every outcome |
| Reply to Arthur | how many are still broken, how many new tickets, how many of the 28 children are Done | thread of D05S1S2AB5M/1770937805.214409 | arthur.blake@harmonygames.co | slack_send_message | the three counts |

Alternatives a careful run could defend are settled or accepted in §4b. The forks a blind sweep found, and how each was closed, are in plan/out/sweep_dispositions.md.

### 4b · Canonical outcome (all fair outcomes)

| Deliverable | Field | Fixed value (or closed accepted set, with sources) | Delegated by (quoted span, or —) | Allowed equivalence class | Material / representational | Source |
|---|---|---|---|---|---|---|
| New tickets | count | 68: 58 Fixed, 3 Gone, 7 Broken (solver/truth.json) | — | — | material | f_3ca9e15d7b20f4e681ad52 |
| New tickets | team, label, parent, assignee | Engineering, Bug, ENG-2401, none | — | — | material | f_3ca9e15d7b20f4e681ad52 |
| New tickets | title | [2231] then the line without its tick box, or the first line of the post, as written | — | emoji codes and mentions kept or dropped; trailing spaces free | material (prefix, wording) / representational (codes) | ENG-2401 note comment_49b5ac4788465f72ddf245e34f2b7034; the bottom bar bug takes the first line of its first post, C05V5FNLB9V/1766415211.386389 |
| New tickets | state | Done for Fixed, Canceled for Gone, Bugs for Broken | — | — | material | f_3ca9e15d7b20f4e681ad52 |
| New tickets | description | empty | — | — | material | f_3ca9e15d7b20f4e681ad52 |
| Reused tickets | note | on ENG-2073 for the Apple line, on ENG-2363 for the manual sign-in line, carrying the canvas wording | — | wording around it free | material | owen.baker@harmonygames.co/1849333980856689601 |
| Children | state | 23 of 28 Done: 9 already plus 14 moved; ENG-2424, ENG-2426, ENG-2428, ENG-2434, ENG-2437 stay in their current state; masters untouched | — | — | material | f_3ca9e15d7b20f4e681ad52 |
| Children | line on each | where it landed, on all 28 | hub: 'leave a line on every child saying where it landed' | wording free | material (presence) / representational (wording) | D05S1S2AB5M/1770937805.214409 |
| Children | build in the note | 0.3.310 on all 28 lines: Brian's rule asks for the current public build, and the doc says that is 0.3.310 | — | '0.3.310' or 'build 0.3.310' | material | 690b29bc3c7d2e51b0f86a47 |
| Sheet | location | in d_9b41e7c2a05d36f8e1c7a4 | — | — | material | D05S1S2AB5M/1770937805.214409 |
| Sheet | title | — | hub: 'Put a sheet in your DD bug carry-over folder' | any title | representational | D05S1S2AB5M/1770937805.214409 |
| Sheet | columns | Bug, Outcome, Ticket, Why | — | order free | material | f_3ca9e15d7b20f4e681ad52 |
| Sheet | rows | 70: 58 Fixed, 7 Broken, 3 Gone, 2 Covered | — | Outcome may read as the state (Done, Bugs, Canceled) | material | f_3ca9e15d7b20f4e681ad52 |
| Sheet | sharing | Arthur, Robert, Oliver | — | any role | material (people) / representational (role) | evt_6e2c91d4b07f3a58c1d2e4 |
| Reply | destination | thread of D05S1S2AB5M/1770937805.214409 | — | — | material | D05S1S2AB5M/1770937805.214409 |
| Reply | still broken | 9 (Broken plus Covered) | — | may also give the 7 and 2 split | material | f_3ca9e15d7b20f4e681ad52 |
| Reply | new tickets | 68 | — | — | material | D05S1S2AB5M/1770937805.214409 |
| Reply | children Done | 23 of 28 | — | — | material | D05S1S2AB5M/1770937805.214409 |

## 5 · Discovery map

Root cause and findings appear only here and never in the prompt.

| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |
|---|---|---|---|---|---|---|
| F1 Arthur's ask | hub text | D05S1S2AB5M/1770937805.214409 | YES (DM member) | met first (the anchor) | — | Yes (anchor AN1) |
| F2 carry-over notes | scope, outcomes, what counts, ticket fields, tree rule, columns | f_3ca9e15d7b20f4e681ad52 | YES (shared with Owen) | named by the hub; the decoy f_72e0b4c3d91a5f68c2b7e4 sits beside it | a search for bug notes also returns the ZM doc | No |
| F3 change note on the master ticket | every filed title starts [2231] | ENG-2401 comment_49b5ac4788465f72ddf245e34f2b7034 | YES (Linear unscoped) | after the rule doc, which points at the master ticket | comments need their own read | Yes (anchor AN2), the note itself No |
| F4 Brian's closing rule | each close-out note names the current public build | 690b29bc3c7d2e51b0f86a47 on 690b27282f4c1b7a6e93d512 | YES (Trello unscoped) | named by role in the rule doc; decoy 68d284b84b7e9a3c5d16e208 | the card is off the named path | No |
| F5 canvas lines | 63 lines | CE156FDFB428/1763041126.468099 | YES (channel member) | met first | channel history, not search | No |
| F6 later bug posts | 7 posts | C05V5FNLB9V/1764256187.655299 | YES (channel member) | after the canvas | the population comes from the rule doc | No |
| F7 shop icons came back | Broken | C09Q4S613CN/1764606918.318209 | YES (channel member) | the tick CE156FDFB428/1763549455.195819 first; overturned by Brian's reply under a gems post | a reply under an unrelated root | No |
| F8 Tavern frame went again | Broken | D05USBTQY1F/1765452012.418229 | YES (DM member) | the tick and Brian's fix first; overturned by Marcus's DM | a DM no anchor names | No |
| F9 lives removed | three lines Gone | C09SWTHEMEW/1764659626.614679 | YES (channel member) | the unticked lines first | the removal is in another channel | No |
| F10 economy doc | no-lives economy | f_948768f5a462e7037d17c9 | YES (shared with Owen) | after the lines | a doc, not a chat | No |
| F11 Win & Collect off | ENG-2424 stays | C9CA62B5180A/1765927876.696389 | YES (group DM member) | the child reads as finished first; the doc's switched-off clause decides it | a group DM | No |
| F12 window fix never shipped | Broken | harmonygames-Games/GameOfDominoes#1913 | YES (GitHub unscoped) | Marcus's reply first; overturned by the open PR | agents stop at a conclusion | No |
| F13 Marcus's fix claim | claim met first | C05V5FNLB9V/1764329192.159229 | YES (channel member) | met first | reads as closed | No |
| F14 flicker closed | Fixed: Robert says both flickers are gone | C09Q4S613CN/1766164222.418229 | YES (channel member) | the thread ends at testing; closed by Robert's reply under his sub-250 report, with the fix on the economy line | a reply in another channel | No |
| F15 music and acid sorted | Fixed | D07E9PSQB6W/1765206644.602119 | YES (DM member) | the threads have no closing line; closed by Brian's DM | a DM | No |
| F16 bottom bar closed | Fixed | C05V5FNLB9V/1767021345.207719 | YES (channel member) | a long thread; the last reply closes it | the thread is 61 replies long | No |
| F17 Apple line tie | ENG-2073 | owen.baker@harmonygames.co/1849333980856689601 | YES (Owen's mailbox) | titles use other words | mail is not in the anchor chain | No |
| F18 ENG-2073 open | Bugs | ENG-2073 | YES (Linear unscoped) | — | — | No |
| F19 manual sign-in tie | ENG-2363 | ENG-2363 comment_7ab5299cbb609d95ba12249d315daedc | YES (Linear unscoped) | titles use other words | comments need their own read | No |
| F20 Tile Dozer popup held | ENG-2434 stays | harmonygames-Games/GameOfDominoes#1905#rc_1 | YES (GitHub unscoped) | the merged PR and Owen's comment first; overturned by the inline comment | review body is empty | No |
| F21 Axe Arena popup held | ENG-2426 stays | harmonygames-Games/GameOfDominoes#1908#rc_1 | YES (GitHub unscoped) | the merged PR first; overturned by the inline comment | review body is empty | No |
| F22 Season Pass reward track | ENG-2428 stays | ENG-2428 comment_d6aee2099bd71050facc422ccef8f809 | YES (Linear unscoped) | the deck first; overturned by Oliver's note | comments need their own read | No |
| F23 Daily Gift last pass | ENG-2437 stays | D07E9PSQB6W/1765471651.208713 | YES (Owen is in the DM) | the deck first; overturned by Brian's DM line on Dec 11 | read only by runs that look through Brian's messages | No |
| F24 wrap deck | stale claim | f_d15a8c70e3f2b94a61c8d3 | YES (shared with Owen) | met before the notes | — | No |
| F25 UI pass tracker | stale list | f_a9ba8abc7d5189babcb378 | YES (shared with Owen) | met before the notes | — | No |
| F26 screen checklist | 27 of 28 ticked | 690b27282f4c1b7a6e93d512 | YES (Trello unscoped) | a claim the inline comments overturn | — | No |
| F27 ZM notes decoy | other game | f_72e0b4c3d91a5f68c2b7e4 | YES (shared with Owen) | decoy for F2 | title names the game | No |
| F28 ZM close-out decoy | other game | 68d284b84b7e9a3c5d16e208 | YES (Trello unscoped) | decoy for F4 | card title names ZM | No |
| F29 Sunday's review | Arthur, Robert, Oliver, Owen | evt_6e2c91d4b07f3a58c1d2e4 | YES (Owen's calendar) | named by the hub | — | No |
| F30 Owen's folder | destination | d_9b41e7c2a05d36f8e1c7a4 | YES (Owen owns it) | named by the hub | — | Yes, by its plain name if needed |
| F31 train line stays open | Broken | CE156FDFB428/1763845212.507119 | YES (channel member) | commit 4189eca5 first; overturned by Vincent's reply | reply in a long thread | No |
| F32 team line stays open | Broken | CE156FDFB428/1763742012.611229 | YES (channel member) | commit 100612a7 first; overturned by Vincent's reply | reply in a thread | No |
| F33 lives lines not fixed | reply says the same after the change | CE156FDFB428/1763845812.703339 | YES (channel member) | commit 3646982c first; overturned by Vincent's replies | — | No |
| F34 public build post | Leonard's post that a new build went out | C09SWTHEMEW/1770926214.816149 | YES (channel member) | the rule doc gives the number | — | No |
| F35 sub-250 reports | out of scope | C09Q4S613CN/1764013026.858409 | YES (channel member) | the rule doc leaves them out | near a bug list | No |

## 5a · Search-as-persona proof

`persona_view.py search owen_baker <service> "<query>"` reads base data; seeded rows Owen can see are counted from the SQL overlay (check-sql PASS for every scoped seeded record, dossier 1.E). Outputs verbatim below the table.

| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |
|---|---|---|---|---|---|---|
| F1 | slack | BoomBit sync | 0 base + 1 seeded | n/a (--no-hidden) | D05S1S2AB5M/1770937805.214409 | YES (seeded; check-sql YES) |
| F2 | gdocs | carry-over notes | 0 base + 1 seeded | 0 | f_3ca9e15d7b20f4e681ad52 | YES (seeded; check-sql YES) |
| F3 | linear | UI Changes Master Ticket | 1 base + 1 seeded | 0 | ENG-2401 | YES (seeded; unscoped) |
| F4 | trello | UI optimization | 0 base + 2 seeded | 0 | 690b27282f4c1b7a6e93d512 | YES (seeded; unscoped) |
| F5 | slack | train level backgrounds | 10 base + 0 seeded | n/a (--no-hidden) | CE156FDFB428/1763394823.486369 | YES (base hit) |
| F6 | slack | mega tile | 223 base + 0 seeded | n/a (--no-hidden) | C05V5FNLB9V/1764256187.655299 | YES (base hit) |
| F7 | slack | shop icons | 4 base + 1 seeded | n/a (--no-hidden) | C09Q4S613CN/1764606918.318209 | YES (seeded; check-sql YES) |
| F8 | slack | Tavern buttons | 1 base + 1 seeded | n/a (--no-hidden) | D05USBTQY1F/1765452012.418229 | YES (seeded; check-sql YES) |
| F9 | slack | no lives | 15 base + 0 seeded | n/a (--no-hidden) | C09SWTHEMEW/1764659626.614679 | YES (base hit) |
| F10 | gdocs | economy | 6 base + 0 seeded | 74 | f_948768f5a462e7037d17c9 | YES (base hit) |
| F11 | slack | Win & Collect | 10 base + 0 seeded | n/a (--no-hidden) | C9CA62B5180A/1765927876.696389 | YES (base hit) |
| F12 | github | Fixing window in tile dozer | 2 base + 0 seeded | 0 | harmonygames-Games/GameOfDominoes#1913 | YES (base hit) |
| F13 | slack | did a PR | 44 base + 0 seeded | n/a (--no-hidden) | C05V5FNLB9V/1764329192.159229 | YES (base hit) |
| F14 | slack | flickering | 40 base + 1 seeded | n/a (--no-hidden) | C09Q4S613CN/1766164222.418229 | YES (seeded; check-sql YES) |
| F15 | slack | acid | 39 base + 1 seeded | n/a (--no-hidden) | D07E9PSQB6W/1765206644.602119 | YES (seeded; check-sql YES) |
| F16 | slack | bottom bar | 70 base + 1 seeded | n/a (--no-hidden) | C05V5FNLB9V/1767021345.207719 | YES (seeded; check-sql YES) |
| F17 | gmail | sign in | 13 base + 1 seeded | n/a (--no-hidden) | owen.baker@harmonygames.co/1849333980856689601 | YES (seeded; check-sql YES) |
| F18 | linear | Sign-In Account | 1 base + 0 seeded | 0 | ENG-2073 | YES (base hit) |
| F19 | linear | stuck at splash | 3 base + 1 seeded | 0 | ENG-2363 | YES (seeded; unscoped) |
| F20 | github | Mini-Games UI Optimization | 2 base + 1 seeded | 0 | harmonygames-Games/GameOfDominoes#1905 | YES (seeded; unscoped) |
| F21 | github | Axe Arena - UI Optimization | 2 base + 1 seeded | 0 | harmonygames-Games/GameOfDominoes#1908 | YES (seeded; unscoped) |
| F22 | linear | Season Pass - UI Optimization | 1 base + 1 seeded | 0 | ENG-2428 | YES (seeded; unscoped) |
| F23 | linear | Daily Gift UI Optimization | 1 base + 1 seeded | 0 | ENG-2437 | YES (seeded; check-sql YES) |
| F24 | gslides | UI optimization | 0 base + 1 seeded | 2 | f_d15a8c70e3f2b94a61c8d3 | YES (seeded; check-sql YES) |
| F25 | gsheets | UI pass | 0 base + 1 seeded | 0 | f_a9ba8abc7d5189babcb378 | YES (seeded; check-sql YES) |
| F26 | trello | Screens checked | 0 base + 1 seeded | 0 | 690b27282f4c1b7a6e93d512 | YES (seeded; unscoped) |
| F27 | gdocs | bug list notes | 0 base + 1 seeded | 0 | f_72e0b4c3d91a5f68c2b7e4 | YES (seeded; check-sql YES) |
| F28 | trello | close-outs | 0 base + 1 seeded | 0 | 68d284b84b7e9a3c5d16e208 | YES (seeded; unscoped) |
| F29 | gcal | bug review | 11 base + 1 seeded | 0 | evt_6e2c91d4b07f3a58c1d2e4 | YES (seeded; check-sql YES) |
| F30 | gdrive | carry-over | 0 base + 1 seeded | 0 | d_9b41e7c2a05d36f8e1c7a4 | YES (seeded; check-sql YES) |
| F31 | slack | snow train | 1 base + 1 seeded | n/a (--no-hidden) | CE156FDFB428/1763845212.507119 | YES (seeded; check-sql YES) |
| F32 | slack | navigation bar | 105 base + 1 seeded | n/a (--no-hidden) | CE156FDFB428/1763742012.611229 | YES (seeded; check-sql YES) |
| F33 | slack | lives are not decreased | 1 base + 2 seeded | n/a (--no-hidden) | CE156FDFB428/1763845812.703339 | YES (seeded; check-sql YES) |
| F34 | slack | published a new build | 1 base + 0 seeded | n/a (--no-hidden) | C09SWTHEMEW/1770926214.816149 | YES (base hit) |
| F35 | slack | 250 mb | 27 base + 0 seeded | n/a (--no-hidden) | C09Q4S613CN/1764013026.858409 | YES (base hit) |

```
SEARCH slack 'BoomBit sync' as owen_baker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned
SEARCH gdocs 'carry-over notes' as owen_baker  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH linear 'UI Changes Master Ticket' as owen_baker  scope: hg.py search (unscoped: no ACL filter)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/2338/title", "parent_pointer": "/issues/2338", "encoding": "json", "text": "UI Change
SEARCH trello 'UI optimization' as owen_baker  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH slack 'train level backgrounds' as owen_baker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=10 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C050WGU41HR/1733765990.040729", "channel": "engineering-bots", "kind": "private", "date": "2024-12-09", "user": "SLACK_BOT_0004_SLACK_ID", "reply": false, "snippet": "om/harmonygames-Games/GameOfDominoes/pull/1537|#1537 
SEARCH slack 'mega tile' as owen_baker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=223 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=2 in 2 containers
  {"id": "C04S28HSD0U/1678249982.593689", "channel": "product", "kind": "private", "date": "2023-03-08", "user": "PERSON_6047_SLACK_ID", "reply": false, "snippet": "There is the mega tile, not really trick, but it's a giant 4 squa
SEARCH slack 'shop icons' as owen_baker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=4 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C05KVU52Z8X/1704902571.440649", "channel": "god-saga-map", "kind": "private", "date": "2024-01-10", "user": "EMPLOYEE_0007_SLACK_ID", "reply": false, "snippet": "progress on the concepts and shop icons and some miscellan
SEARCH slack 'Tavern buttons' as owen_baker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "CE156FDFB428/1763642831.967359", "channel": "FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025", "kind": "public", "date": "2025-11-20", "user": "PERSON_6089_SLACK_ID", "reply": false, "snippet": "☑ Tavern buttons lost its 
SEARCH slack 'no lives' as owen_baker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=15 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=3 in 1 containers
  {"id": "C05433XK267/1754956435.728189", "channel": "builds", "kind": "public", "date": "2025-08-11", "user": null, "reply": false, "snippet": "ON_NAME_0068]] - Added disabled button to MoreLives UI when no lives in bank [[PERSON
SEARCH gdocs 'economy' as owen_baker  scope: GDocs title + body_text
visible hits=6 (showing 3)  hidden by ACL=74 in 74 containers  UNVERIFIED=6 in 6 containers
  {"id": "f_948768f5a462e7037d17c9", "name": "Economy Changes for Domino Delights.docx", "mime": "application/vnd.google-apps.document", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Economy Changes fo
SEARCH slack 'Win & Collect' as owen_baker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=10 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=1 in 1 containers
  {"id": "C05433XK267/1737421636.921309", "channel": "builds", "kind": "public", "date": "2025-01-21", "user": "PERSON_6065_SLACK_ID", "reply": true, "snippet": "ENG-2068 Win & Collect Event pop up doesn't appear."}
SEARCH github 'Fixing window in tile dozer' as owen_baker  scope: hg.py search (unscoped: no ACL filter)
visible hits=2 (showing 2)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_Normal/Normal_HarmonyGames_GitHub/Services_Data/github/data.json", "service_file": "data.json", "pointer": "/commits/3893/message", "parent_pointer": "/commits/3893", "encoding": "json", "text": "Fixing window
SEARCH slack 'did a PR' as owen_baker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=44 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04V7N09LE7/1713965319.074429", "channel": "god-gameart", "kind": "private", "date": "2024-04-24", "user": "EMPLOYEE_0002_SLACK_ID", "reply": false, "snippet": ":slightly_smiling_face: but then you get used to it. I also
SEARCH slack 'flickering' as owen_baker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=40 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=4 in 1 containers
  {"id": "C050WGU41HR/1710447097.535639", "channel": "engineering-bots", "kind": "private", "date": "2024-03-14", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "to draw cards really really fast, then you'd have the t
SEARCH slack 'acid' as owen_baker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=39 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C050WGU41HR/1717622949.413249", "channel": "engineering-bots", "kind": "private", "date": "2024-06-05", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "be \"dissolve\" the tile, like vanishing tile style, b
SEARCH slack 'bottom bar' as owen_baker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=70 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C050WGU41HR/1689700344.451789", "channel": "engineering-bots", "kind": "private", "date": "2023-07-18", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "Well the default option was either a button at the bot
SEARCH gmail 'sign in' as owen_baker  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=13 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "owen.baker@harmonygames.co/1777123429617449470", "last": "2023-09-15T16:56:10Z", "subject": "[PERSON_NAME_0038] just joined your workspace!", "snippet": "rkspace name: [SOURCE_ORG_0001]  Workspace URL: [URL_3601]  Sign I
SEARCH linear 'Sign-In Account' as owen_baker  scope: hg.py search (unscoped: no ACL filter)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/1989/title", "parent_pointer": "/issues/1989", "encoding": "json", "text": "Sign-In A
SEARCH linear 'stuck at splash' as owen_baker  scope: hg.py search (unscoped: no ACL filter)
visible hits=3 (showing 3)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/1539/title", "parent_pointer": "/issues/1539", "encoding": "json", "text": "The game 
SEARCH github 'Mini-Games UI Optimization' as owen_baker  scope: hg.py search (unscoped: no ACL filter)
visible hits=2 (showing 2)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_Normal/Normal_HarmonyGames_GitHub/Services_Data/github/data.json", "service_file": "data.json", "pointer": "/pull_requests/1034/title", "parent_pointer": "/pull_requests/1034", "encoding": "json", "text": "ENG
SEARCH github 'Axe Arena - UI Optimization' as owen_baker  scope: hg.py search (unscoped: no ACL filter)
visible hits=2 (showing 2)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_Normal/Normal_HarmonyGames_GitHub/Services_Data/github/data.json", "service_file": "data.json", "pointer": "/pull_requests/1037/title", "parent_pointer": "/pull_requests/1037", "encoding": "json", "text": "ENG
SEARCH linear 'Season Pass - UI Optimization' as owen_baker  scope: hg.py search (unscoped: no ACL filter)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/2367/title", "parent_pointer": "/issues/2367", "encoding": "json", "text": "Season Pa
SEARCH linear 'Daily Gift UI Optimization' as owen_baker  scope: hg.py search (unscoped: no ACL filter)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/2377/title", "parent_pointer": "/issues/2377", "encoding": "json", "text": "Daily Gif
SEARCH gslides 'UI optimization' as owen_baker  scope: GSlides title + page element text
visible hits=0 (showing 0)  hidden by ACL=2 in 2 containers  UNVERIFIED=0 in 0 containers
SEARCH gsheets 'UI pass' as owen_baker  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH trello 'Screens checked' as owen_baker  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gdocs 'bug list notes' as owen_baker  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH trello 'close-outs' as owen_baker  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gcal 'bug review' as owen_baker  scope: GCal event summary (base events carry no description/location)
visible hits=11 (showing 3)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "evt_26a0aba4879f285c50e9f9", "calendar": "owen.baker@harmonygames.co", "start": "2024-08-13T15:00:00Z", "summary": "Bug Review", "status": "confirmed"}
SEARCH gdrive 'carry-over' as owen_baker  scope: Drive file/folder names (on-disk file content is not searched)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH slack 'snow train' as owen_baker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "CE156FDFB428/1763737300.402439", "channel": "FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025", "kind": "public", "date": "2025-11-21", "user": "EMPLOYEE_0012_SLACK_ID", "reply": true, "snippet": "tally creates visually mi
SEARCH slack 'navigation bar' as owen_baker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=105 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C050WGU41HR/1696874215.133569", "channel": "engineering-bots", "kind": "private", "date": "2023-10-09", "user": "SLACK_BOT_0004_SLACK_ID", "reply": false, "snippet": "• Disabled Navigation Bar Buttons Child Images Raycas
SEARCH slack 'lives are not decreased' as owen_baker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "CE156FDFB428/1763548856.943389", "channel": "FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025", "kind": "public", "date": "2025-11-19", "user": "PERSON_6089_SLACK_ID", "reply": false, "snippet": "☐ P.S I found the issue, l
SEARCH slack 'published a new build' as owen_baker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C09SWTHEMEW/1770926214.816149", "channel": "publishing-ext-[SOURCE_ORG_0001]-nbp7547", "kind": "private", "date": "2026-02-12", "user": "EMPLOYEE_0038_SLACK_ID", "reply": true, "snippet": "We were able to fix this proble
SEARCH slack '250 mb' as owen_baker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=27 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C05433XK267/1707507575.539909", "channel": "builds", "kind": "public", "date": "2024-02-09", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "btw - this apk is 250 mb?"}
```

## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · persona-readable · unique · instructions-not-answer) | Inferable |
|---|---|---|---|---|
| outcome of each bug | f_3ca9e15d7b20f4e681ad52 | scope (Arthur's ask) | hub D05S1S2AB5M/1770937805.214409 names 'the carry-over notes doc' · YES · one doc with that title · rules, no answers | yes, once the hub is followed |
| population: canvas lines and later posts | f_3ca9e15d7b20f4e681ad52 | scope | f_3ca9e15d7b20f4e681ad52 · YES · unique · scope sentence, no list | yes |
| ticket fields | f_3ca9e15d7b20f4e681ad52 | none | f_3ca9e15d7b20f4e681ad52 · YES · unique · instruction | gotcha with a record trigger |
| title prefix | comment_49b5ac4788465f72ddf245e34f2b7034 | none | f_3ca9e15d7b20f4e681ad52 'If anything changes after this I'll put it on the master ticket' · YES · ENG-2401 · instruction | gotcha with a record trigger |
| build in each child note | 690b29bc3c7d2e51b0f86a47 | none | f_3ca9e15d7b20f4e681ad52 'Brian's closing rule from the UI work applies to the line on every child, Done or not' · YES · one card comment · rule, no answers | gotcha with a record trigger |
| a line on every child | D05S1S2AB5M/1770937805.214409 | deliverable | hub · YES · — · instruction | yes |
| sheet in the folder, shared with the review | D05S1S2AB5M/1770937805.214409 | destination + recipients | hub 'share it with everyone on Sunday's bug review' · YES · one event evt_6e2c91d4b07f3a58c1d2e4 · names people, no answers | yes |
| three counts in the reply | D05S1S2AB5M/1770937805.214409 | deliverable | hub · YES · thread of D05S1S2AB5M/1770937805.214409 · instruction | yes |

Anchor-name table (noun phrases of at most 6 words; `;` separates synonyms):

| Anchor | May be named |
|---|---|
| AN1 | Arthur's DM from Thursday |
| AN2 | the UI Changes master ticket |

## 7 · Dates and constraints

| Item | Absolute date or value | Source | Past fact or deadline |
|---|---|---|---|
| Owen's today | Saturday Feb 14, 2026 (clock 2026-02-14T00:00Z = Fri Feb 13 16:00 PT) | 00_Task_Context.json universe.persona_today; last hub record D05S1S2AB5M/1770937805.214409 | — |
| Arthur's ask | Thu Feb 12, 2026 15:10 PT (23:10Z) | D05S1S2AB5M/1770937805.214409 | past fact |
| carry-over notes | Thu Feb 12, 2026 14:48 PT (22:48Z) | f_3ca9e15d7b20f4e681ad52 | past fact |
| title note | Thu Feb 12, 2026 16:40 PT (Feb 13 00:40Z) | ENG-2401 comment_49b5ac4788465f72ddf245e34f2b7034 | past fact |
| Sunday's bug review | Sun Feb 15, 2026 09:00–09:30 PT (17:00–17:30Z) | evt_6e2c91d4b07f3a58c1d2e4 | deadline (future event) |
| shutdown premise | decided Feb 9–11, 2026; wind-down acknowledged, no business as usual | C09UHHN6PFZ/1770842566.250369 | past fact |

## 8 · Difficulty levers

| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |
|---|---|---|---|---|
| Ambiguity | yes | yes | outcomes live across Slack, Linear, GitHub, Gmail and Docs (F7 to F23) | the prompt names the anchors only, never where an answer lives |
| Dynamic change | yes | yes | ticks, merged PRs and the deck are met first and overturned later (F7, F8, F20 to F23) | the prompt names neither the summary nor the correction |
| Multi-source | yes | yes | Slack, Linear, GitHub, Docs, Drive, Sheets, Slides, Trello, Gmail, Calendar | no source named as an exact artifact beyond the two anchors |
| Async | no | no | Friction: none (03_Error_Async_Config.txt) | — |
| Error recovery | no | no | Friction: none | — |
| Access control | no | no | every load-bearing record is Owen-visible (check-sql PASS) | no ask to read someone else's scoped data |

## 9 · Must not appear in the prompt

- **Tool and server names (catalog.json):** linear_create_issue, linear_update_issue, linear_create_comment, linear_list_issues, linear_list_comments, slack_send_message, slack_read_thread, slack_search_public_and_private, github_get_pull_request_comments, github_get_pull_request_reviews, gsheets_create_spreadsheet, gsheets_values_update, gdrive_share_file, gdrive_move_file, gmail_search_messages, gcal_list_events, trello tools, any MCP server name.
- **Opaque ids and filenames:** f_3ca9e15d7b20f4e681ad52, d_9b41e7c2a05d36f8e1c7a4, evt_6e2c91d4b07f3a58c1d2e4, 690b27282f4c1b7a6e93d512, CE156FDFB428, C05V5FNLB9V, D05USBTQY1F, D07E9PSQB6W, every ENG key (the master ticket goes by its name).
- **Findings and root causes:** any outcome, any count (9, 68, 23, 58, 7, 3, 2, 70, 63), the build 0.3.310, the [2231] prefix, the Tavern, shop icons, train, team, lives or window lines, #1913, the inline comments, the popups, Win & Collect being off, the Season Pass and Daily Gift notes, ENG-2073, ENG-2363.
- **Hidden authorities and rules:** the four outcomes, the first-fit order, what counts, the ticket fields, the tree rule, the sheet columns, Brian's closing rule, the Trello card, Vincent's mail or note, Marcus's DM, Brian's reply and DM, the economy doc, the wrap deck, the tracker.
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

UNRESOLVED (12)
  [ambiguous_name] github: mononym 'Marcus' is an exact name of [] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co'] -> candidates ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']
  [ambiguous_name] github: mononym 'Claire' is an exact name of [] and the first name of ['email:claire.morgan@harmonygames.co'] -> candidates ['email:claire.morgan@harmonygames.co']
  [ambiguous_name] trello: mononym 'Marcus' is an exact name of ['github:PERSON_0396_GITHUB_USERNAME'] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co'] -> candidates ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co', 'github:PERSON_0396_GITHUB_USERNAME']
  [token_link] EMPLOYEE_0024: same token number across services but no shared exact email/name: not joined -> candidates ['email:employee_0024@harmonygames.co', 'slack:EMPLOYEE_0024_SLACK_ID', 'trello:3d36d70154e6a715614e0d75']
  [token_link] EMPLOYEE_0032: same token number across services but no shared exact email/name: not joined -> candidates ['email:EMPLOYEE_0032_EMAIL', 'email:josh.dempsey@harmonygames.co', 'github:EMPLOYEE_0032_GITHUB_USERNAME', 'slack:EMPLOYEE_0032_SLACK_ID']
  [token_link] PERSON_2218: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_2218_EMAIL', 'github:PERSON_2218_GITHUB_USERNAME']
  [token_link] PERSON_2360: same token n
```

| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |
|---|---|---|---|
| Arthur Blake | 'Blake' in base talk | one person | arthur.blake@harmonygames.co |
| Marcus Bennett | Marcus Lee, Oscar Bennett, github and trello 'Marcus' | Owen's DM partner is Bennett; the prompt need not name him | marcus.bennett@harmonygames.co |
| Robert (one name) | none | co-founder; on the review invite | robert@harmonygames.co |
| Oliver Brooks | Lauren Brooks | Oliver is on the invite | oliver.brooks@harmonygames.co |
| Owen Baker | Thomas Baker | the persona | owen.baker@harmonygames.co |
| ENG tickets | ZOM tickets, ZM canvases | DD is on ENG; the decoy doc f_72e0b4c3d91a5f68c2b7e4 is about ZM | ENG-2401 |

## 11 · Pre-submit checklist

- [ ] Persona voice: Owen, first person, plain; no spec-sheet layout
- [ ] Names only the two anchors (§6 table); no §9 item
- [ ] States the deliverables at the level Arthur's DM does, or simply points at it; destination named
- [ ] No tool or server name; no step list; no count
- [ ] Wind-down acknowledged (no business as usual)
- [ ] Clean spelling and punctuation; no riddle, hint, hedge or if-chain
- [ ] 20–4,000 words
- [ ] Run `/create-prompt-writing check` before `/prompt`

## 12 · Blockers and routed defects

None blocking. No fact is routed to /create-injection now. rev2's /prompt FAIL (run_forensics/rev2/1_prompt_FAIL_r2.md) came from the data, and rev3 fixes it: forks F1 to F4, NB-1, NB-14 and the inline comment dates, plus what a blind item-by-item sweep and a blind coherence audit then found (plan/out/sweep_dispositions.md). The prompt text is unchanged. Every §5 fact is found by a natural search or reached by reading the anchor's thread, ticket or card (§5a).

rev9 needs its own platform /injection before /prompt. Upload `task_inputs/01_Universe_Inject.sql`, which is identical to `Working_Files/run_forensics/rev9/01_Universe_Inject.sql`. rev8 passed /injection and /prompt 5 and failed /hardness 2; rev9 removes Brian's Tavern line and moves his Daily Gift note into his DM. rev7 passed /injection and /prompt 5, then /hardness scored 1 (the pre-check run read all of Brian's Dec messages); rev8 removes Brian's Apple line only. rev5 passed /injection and /prompt 5; its baselines failed the spread and pattern gates, so rev6 added three DM lines that repeat four corrections in Brian's DM with Owen, which some runs read and others don't. rev6 passed /injection, and /prompt failed it on the navigation bar tooltips thread, which ended at Brian's 'I'll send another fix' (Unique Ground Truth and Clarity 2); rev7 adds Vincent's Nov 22 reply there saying the second fix closed the gap. The prompt and truth are unchanged. Accepted and watched: 0.3.310 has no base record Owen can read, so the rule doc f_3ca9e15d7b20f4e681ad52 is the authority (C09SWTHEMEW/1770926214.816149 gives the post, D04UGG61DUM/1770846601.876869 the number); the masters ENG-2401 to ENG-2405 keep their states, as the rule doc says and as /prompt accepted on rev2; the Dec 22 bottom bar bug's title comes from the first of its two posts, C05V5FNLB9V/1766415211.386389.

## 13 · Self-review

| Area | Counter-reading (strongest argument it fails) | Evidence that resolves it | Verdict |
|---|---|---|---|
| Fair readings (C6) | ENG-2424 goes Done: nothing names a missing part, and the tracker says done. | f_3ca9e15d7b20f4e681ad52 'or the screen is switched off there'; C9CA62B5180A/1765927876.696389 'event disabled', with no later record turning it back on; the blind re-check closed the fork at 23 of 28 | settled |
| Fair readings (C6) | Each note names the build the child was checked on, not 0.3.310. | 690b29bc3c7d2e51b0f86a47 now says the current public build; f_3ca9e15d7b20f4e681ad52 says that is 0.3.310 and applies the rule to the line on every child, Done or not | settled |
| Fair readings (C6) | Arthur's Dec 31 no-ads post is an eighth later bug, giving 69 tickets. | C05V5FNLB9V/1767191512.428539 is a design question to Leonard; f_3ca9e15d7b20f4e681ad52 'A design question for Leonard isn't a bug post' | settled |
| Fair readings (C6) | Fragment lines or alike lines merge, giving 65 to 67 tickets. | f_3ca9e15d7b20f4e681ad52 'One Linear record per canvas line and one per bug posted after it'; CE156FDFB428/1763042493.563249 | settled |
| Fair readings (C6) | Tavern is Fixed by the Dec 5 Gacha commit. | Marcus's note D05USBTQY1F/1765452012.418229 now follows the Dec 5 commit, and H1 needs a commit named for the bug | settled |
| Fair readings (C6) | Axe Arena and Tile Dozer are Done: Brian ticked them. | harmonygames-Games/GameOfDominoes#1905#rc_1 and #1908#rc_1 name a popup; the deck and checklist now speak of main screens, so nothing later says the popups were done | settled |
| Fair readings (C6) | Robert's flicker post stays Broken: the fix names only the end-level popup. | Robert's reply C09Q4S613CN/1766164222.418229 covers both, the play button and coming out of a level | settled |
| Fair readings (C6) | Brian's two Dec 22 posts are two tickets. | f_3ca9e15d7b20f4e681ad52 'a follow-up on a bug already posted is part of that bug'; C05V5FNLB9V/1766415211.386389 | settled |
| Fair readings (C6) | Deleted canvas lines and the QA-doc post get tickets. | f_3ca9e15d7b20f4e681ad52 'A comment whose line was deleted has nothing to carry over' and 'a post that points at a QA doc isn't a bug post'; C05V5FNLB9V/1764662837.138929 | settled |
| Clarity (C7) | 'tell me here' could be a new DM message, not a thread reply. | §4b pins the thread of D05S1S2AB5M/1770937805.214409; the prompt must say so | settled by the prompt |
| Clarity (C7) | 'share it with everyone on Sunday's bug review' leaves the role open. | §4b accepts any role for Arthur, Robert and Oliver (evt_6e2c91d4b07f3a58c1d2e4) | accepted outcomes |
| Incorporation (C8) | Brian's rule might be owed only on closed tickets. | f_3ca9e15d7b20f4e681ad52 'applies to the line on every child, Done or not'; the blind re-check found every write owed through the DM or the doc | incorporated |
| Incorporation (C8) | The doc could be confused with the ZM notes. | the hub names 'the carry-over notes doc'; f_72e0b4c3d91a5f68c2b7e4 is titled 'Zombie Match bug list notes' | unique |
| Truthfulness (C17) | 'Thursday' could be the wrong day for Arthur's DM. | D05S1S2AB5M/1770937805.214409 is Thu Feb 12 15:10 PT | true |
| Truthfulness (C17) | Slack dropping to free could be a false premise after the shutdown. | it is Arthur's stated plan in the hub, and the wind-down is acknowledged, C09UHHN6PFZ/1770842566.250369 | true |
| Feasibility / ACL (C18–C19) | The sheet must sit in Owen's folder and be shared; a new sheet lands in his root. | gsheets_create_spreadsheet then gdrive_move_file to d_9b41e7c2a05d36f8e1c7a4 then gdrive_share_file; Owen owns the folder | feasible |
| Feasibility / ACL (C18–C19) | Owen left #god-bugs on Feb 11, so a read may fail (NB-1). | the hub says he is back on a paid seat (five seats, three kept: C0ADGSZKR3R/1770842395.641349), and the SQL gives him a leave on Feb 11 and a join on Feb 12 in each task channel: C05V5FNLB9V, CE156FDFB428, C09Q4S613CN, C05433XK267, C09SWTHEMEW, C050WGU41HR | feasible |
| Feasibility / ACL (C18–C19) | Labels or states might not exist. | Bug label and states Bugs, Done, Canceled are on base ENG tickets (ENG-2280); linear_create_issue takes labels, state and parentId | feasible |
| Contrived register (C15–C16) | Pointing at Arthur's DM could read as hiding the destination. | the prompt names the DM and the master ticket and says where the reply goes (prompt_qc_cases hidden_destination) | ordinary |
| Contrived register (C15–C16) | Listing the deliverables could read as a command list. | deliverables and who to tell are the screen-24 skeleton, not sequenced method steps; ENG-2401 stays named as an anchor only | ordinary |

Fair readings, clarity, incorporation, truthfulness, feasibility / ACL and the contrived register are each addressed above with evidence. Unresolved: the prompt is not yet written, and check mode re-tests every point on the actual text.

```
STAGE GATE prompt-writing: PASS — Task_Authoring/task_inputs · 04_Prompt_Writing_Brief.md#f91406518f7f · 00_Assigments.md#c039da1b9b09 · 01_Grounding_Dossier.md#9c226652d6ec · 01_Universe_Inject.sql#ea5b542897c8 · 03_Error_Async_Config.txt#3d3ae3f9720a · __context__#ba6bb23d4a12 · __assignment__#560a0d2ca2a9 · __policy__#dc4ab5df3cdd · __gate_policy__#f8638415ca2c · __review__#38f0f10cf2a0 · blocking 0 · warnings 0 · checks 24
[PASS] assignment.v3_context: Owen Baker / Game Engineer (Unity); medium cap <85%; freeze 2026-02-14T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe normal; KB bound; clock Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Writing_Brief.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql, 03_Error_Async_Config.txt)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#ea5b542897c8, 01_Hardness_Manifest.json#ec4cc1070c06, 01_Grounding_Dossier.md#9c226652d6ec, solver/solver.py#c2eca0f97c62, 01c_Dispositions.json#b86f62194ac2, 01c_Preflight_Report.json#2580b7c15c79, 00_Assigments.md#c039da1b9b09, 01_Scenario_Design.md#de755e35633e, 01_Hardness_Manifest.draft.json#459add197b56, 01_Gradable_Surface.json#6d9cd388cdbb, __context__#ba6bb23d4a12, __assignment__#560a0d2ca2a9, __policy__#dc4ab5df3cdd, __gate_policy__#f8638415ca2c, __review__#a52cce78498e)
[PASS] chain.error-async: upstream 'error-async' PASS pasted and current (03_Error_Async_Config.txt#3d3ae3f9720a, 00_Assigments.md#c039da1b9b09, 01_Grounding_Dossier.md#9c226652d6ec, 01_Universe_Inject.sql#ea5b542897c8, __context__#ba6bb23d4a12, __assignment__#560a0d2ca2a9, __policy__#dc4ab5df3cdd, __gate_policy__#f8638415ca2c, __review__#a52cce78498e)
[PASS] structure.sections: 14 required sections present and non-empty (04_Prompt_Writing_Brief.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Writing_Brief.md
[PASS] evidence.situation: 4/4 items carry a source pointer (min 100%)
[PASS] evidence.final_state: 24/24 items carry a source pointer (min 100%)
[PASS] evidence.discovery_map: 35/35 items carry a source pointer (min 100%)
[PASS] evidence.dates: 6/6 items carry a source pointer (min 100%)
[PASS] evidence.entity_traps: 6/6 items carry a source pointer (min 100%)
[PASS] tool.search_as_persona: 35 facts proven findable by persona_view search as owen_baker
[PASS] reach.brief: 27 scoped load-bearing ids YES for owen_baker
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] structure.accepted_outcomes: V3 accepts multiple fair outcomes; see v3.fair_outcomes_review
[PASS] boundary.anchor_naming: 2 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 20 evidenced counter-readings (of 20 found; need ≥ 6) in 04_Prompt_Writing_Brief.md
[PASS] review.coverage: self-review addresses all 6 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.fair_outcomes_review: current accepted outcomes and considered alternatives recorded; multiple fair outcomes are allowed
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

