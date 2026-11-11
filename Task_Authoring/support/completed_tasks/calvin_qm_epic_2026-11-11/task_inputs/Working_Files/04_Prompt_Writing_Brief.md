# Prompt Brief — calvin_qm_epic · prep
> Built 2026-11-10 from 00_Assigments.md, Working_Files/00_Task_Context.json, 01_Grounding_Dossier.md (injection rev3, sha256 479b8441f52e, built after six baseline runs on the second revision averaged about 79 %; the first two revisions passed the platform /injection and /prompt, rev3 has not been reviewed there yet), 01_Scenario_Design.md, 01_Hardness_Manifest.json, solver/truth.json, 03_Error_Async_Config.txt (Friction: none) · Persona view verified: all (check-sql PASS, §5a)
> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human. No 02_Reference_Files: the scenario needs no attachment.
> Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
|---|---|---|
| Business function | Engineering | Engineering & Live-Ops in `Evals/references/rules/task_categories.md` (engineering delivery, releases, incidents, live game operations): the ZM home screen queue manager and the QA reports against it. |
| Persona | Calvin Price · calvin.price@harmonygames.co · Game Engineer (Unity VFX) (roster.json persona_key calvin_price, department Engineering) | Voice: a working engineer writing to his assistant, first person, short and plain; judged against the role only. Remit: he is the assignee of ZOM-543 (Queue Manager, In Progress), opened harmonygames-Games/match3d#465 and #472, Brian asked him to take the queue manager on (D0770ET6WBW/1758730948.999939) and QA reports to him directly (D06UPGF5PQV/1758806199.381319). Read scope: his DMs D0770ET6WBW (Brian), D06UPGF5PQV (Vincent), D05U73FNDDL (Marcus), D05HYDTG5TJ (Julia), channels C08R27X0EAH (#zombie-bugs), C0880U9751A (#zombie-match3d), C093LEZGF6J (#zombie-prs), C05433XK267 (#builds), his mailbox, calendar and Drive. |
| Competency | Engineering Ops | Epic and task management: one ticket becomes an epic with a child per area, every QA report gets its line under the right child, and ticket states are brought in line. Brian asks him because the ticket is his (hub D0770ET6WBW/1759264805.214409). |
| Task skill | Analysis and synthesis | Exercised by deciding the status of 39 reports from the pass sheet, build posts, PR reviews and later chat reports, and by the stock-take sheet, the slide and the five numbers that sum it up. Retrieval and the Linear writes stack under it. |
| Task type | long-horizon (Long Horizon; difficulty mode hard, V3 cap < 70 %; requester targets: average < 60 %, > 130 counted calls per run, largest failure pattern < 50 %) | Services carrying weight: Linear (ZOM-543, 22 existing tickets, 32 notes, about 72 writes), Sheets (38 rows of f_cb40955893624e1acb8500), Slack (4 DMs, 4 channels, 15 build posts), GitHub (4 PRs, 2 review comments, 1 PR comment), Docs (legend, rule doc, decoy), Trello (the review card and its 4 actions), Gmail (2 invitations, 2 review mails), Calendar (1 event, 6 attendees), Drive (folder, shares), Slides (deck). Call budget floor 180 (01_Hardness_Manifest.json); the prompt states no count. |

## 2 · Situation

| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |
|---|---|---|---|
| The queue manager is one ticket while QA's home screen flow pass lives in a sheet of its own; Brian wants it turned into a real epic before Thursday's flow review. | Calvin (DM recipient) | D0770ET6WBW/1759264805.214409 | — |
| Brian left a note on the ticket saying how he wants the epic. | Calvin (Linear, unscoped) | comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 | — |
| Vincent's flow pass sheet has 38 rows with tickets, fixes and re-tests as he knew them. | Calvin (sheet shared with him) | f_cb40955893624e1acb8500 | — |
| Brian also wants a stock-take sheet in Calvin's folder, shared with the review's people, one slide in Calvin's deck and five numbers back in the DM. | Calvin | d_36cdb0374c4aad3b8bf741; f_637e63ae6c1b4a7eb016aa; evt_342a813cb7765d4a6fce8d | the other attendees' calendar copies and invitation mails (not needed: Calvin's own copy evt_342a813cb7765d4a6fce8d lists every attendee) |

## 3 · Investigation → action

Questions to resolve (no answers here):
- How does Brian want the epic laid out, and which areas get a child?
- Which reports are in the list, and which things stay out of it?
- What does each re-test code in the pass sheet mean, and on which build was each re-test done?
- Which builds count for a QA pass on this game?
- Did anyone say later that something came back, and on which build?
- For each report that is not passed, is its fix really merged?
- Does a ticket already hold the report, perhaps under another name?
- Does each ticket's state match where its report stands?
- Which areas does the review cover now, and who is on it?
- Where do the stock-take sheet and the slide go?

Writes those answers feed: ten child issues under the epic, a sub-issue for every report with no ticket, a move, a note and where needed a state change on every existing ticket, the stock-take sheet and its sharing, one slide, and the reply to Brian. Every write depends on the investigation.

## 4 · Pinned final state (UGT anchor)

| Deliverable | Required contents | Destination | Recipients | Catalog write | Fed by |
|---|---|---|---|---|---|
| Area children | one child per area named in Brian's note comment_faaa792418a942cd40be046d8d217a7d, state by whether the area is clear | Linear team ZOM, parent ZOM-543 | — | linear_create_issue | the areas and each area's reports |
| New sub-issues | one per report no ticket holds, title the report, state by status, no priority, no assignee (comment_faaa792418a942cd40be046d8d217a7d) | under the area's child of ZOM-543 | — | linear_create_issue | status of each report; ticket lookup |
| Existing tickets | moved under the area's child, a note with the status and why, state changed where it does not match (comment_faaa792418a942cd40be046d8d217a7d) | ZOM-556, ZOM-560, ZOM-567 to ZOM-584 | — | linear_update_issue, linear_create_comment | status of each report; ticket lookup |
| Stock-take sheet | tab Reports (Report, Area, Status, Ticket, Review list, Why) and tab Areas (Area, Status, Open reports), per comment_faaa792418a942cd40be046d8d217a7d | Calvin's folder d_36cdb0374c4aad3b8bf741 | brian.foster@harmonygames.co, leonard.hayes@harmonygames.co, arthur.blake@harmonygames.co, julia.lawson@harmonygames.co, vincent.parker@harmonygames.co (attendees of evt_342a813cb7765d4a6fce8d) | gsheets_create_spreadsheet, gsheets_batch_update, gsheets_values_update, gdrive_move_file, gdrive_share_file | every status |
| Slide | the five numbers | Calvin's deck f_637e63ae6c1b4a7eb016aa | — | gslides_batch_update | the five counts |
| Reply to Brian | reports passed, waiting on QA, waiting on a fix, areas clear, reports on the review list | Brian's DM D0770ET6WBW (hub D0770ET6WBW/1759264805.214409) | brian.foster@harmonygames.co | slack_send_message | the five counts |

Alternatives a careful run could defend are settled or accepted in §4b. The forks two blind sweeps found, and how each was closed, are in plan/sweeps/fork_sweep_inj.md and the dossier's Self-review; the design's two-reading table (01_Scenario_Design.md §10) lists the record that settles each one.

### 4b · Canonical outcome (all fair outcomes)

| Deliverable | Field | Fixed value (or closed accepted set, with sources) | Delegated by (quoted span, or —) | Allowed equivalence class | Material / representational | Source |
|---|---|---|---|---|---|---|
| Area children | count and names | 10: Tutorials, Level-end rewards, Daily Gift, Season Pass, Collect & Win, Win Streak, Zombie Lane, Boss Arena, Endless Mode, Card packs | — | title is the area name; a prefix such as 'Queue Manager:' is fine | material (areas) / representational (prefix) | comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 |
| Area children | team, parent, assignee | ZOM, ZOM-543, none | — | — | material | comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 |
| Area children | state | Todo for all ten (no area is Clear) | — | — | material | comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 |
| Reports | population | 39: the 38 rows of the pass sheet plus the pass icon glow Marcus reported | — | — | material | f_cb40955893624e1acb8500; D05U73FNDDL/1759252212.611349 |
| Reports | status | 10 Passed, 9 Waiting on QA, 20 Waiting on a fix; per report in the table below | — | — | material | comment_faaa792418a942cd40be046d8d217a7d on ZOM-543; f_6d0326fa006b136f1bbf82 |
| New sub-issues | count and parent | 17, each under its area's child | — | — | material | comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 |
| New sub-issues | title | the report as the pass sheet words it; for Marcus's report, wording that names the pass icon glow staying on | note: 'make a sub-issue under the child with the report as the title' | case and end punctuation free; Marcus's line may be reworded | material (which report) / representational (wording) | comment_faaa792418a942cd40be046d8d217a7d on ZOM-543; D05U73FNDDL/1759252212.611349 |
| New sub-issues | state | Done for Passed, In Validation for Waiting on QA, Todo for Waiting on a fix | — | — | material | comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 |
| New sub-issues | priority and assignee | none | — | — | material | comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 |
| Existing tickets | which | 22: ZOM-567 to ZOM-584, plus ZOM-556 for the day counter row and ZOM-560 for the freezer row | — | — | material | comment_b3c560833d151268202546002e7613cf; comment_9f28b3d8d66bd04e3f7fc46bc6ed1ea9 |
| Existing tickets | parent | the child of the report's area | — | — | material | comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 |
| Existing tickets | state | ZOM-571 to Todo, ZOM-581 to Todo, ZOM-572 to In Validation; the other 17 keep their state | — | — | material | harmonygames-Games/match3d#472#rc_1; harmonygames-Games/match3d#475#rc_1; harmonygames-Games/match3d#473#c_2 |
| Existing tickets | note | one on each of the 20, giving the status and why | note: 'leave a note with the status and why' | wording free | material (presence, status) / representational (wording) | comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 |
| Existing tickets | priority and assignee | left as found | — | — | representational | comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 |
| Sheet | location | in d_36cdb0374c4aad3b8bf741 | — | — | material | D0770ET6WBW/1759264805.214409 |
| Sheet | title | — | hub: 'put a stock-take sheet in your ZM queue manager folder' | any title | representational | D0770ET6WBW/1759264805.214409 |
| Sheet | tab Reports | columns Report, Area, Status, Ticket, Review list, Why; 39 rows | — | column order free; Ticket holds the key of the existing ticket or of the new sub-issue; Review list as Yes/No or the like | material | comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 |
| Sheet | tab Areas | columns Area, Status, Open reports; 10 rows; all ten Open; open counts per the area table below | — | column order free | material | comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 |
| Sheet | sharing | Brian, Leonard, Arthur, Julia, Vincent | hub: 'share it with everyone on the review invite, Leonard too' | any role | material (people) / representational (role) | evt_342a813cb7765d4a6fce8d |
| Slide | location and count | one new slide in f_637e63ae6c1b4a7eb016aa | — | any layout, any position | material (deck, one slide) / representational (layout) | D0770ET6WBW/1759264805.214409 |
| Slide | numbers | 10 passed, 9 waiting on QA, 20 waiting on a fix, 0 area clear, 7 on the review list | — | labels free; '1 of 10' is fine | material | comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 |
| Reply | destination | Brian's DM D0770ET6WBW | hub: 'tell me here' | a new message in the DM or a reply in the thread of D0770ET6WBW/1759264805.214409 | material (the DM) / representational (thread or not) | D0770ET6WBW/1759264805.214409 |
| Reply | numbers | 10, 9, 20, 0, 7 | — | extra detail may be added | material | D0770ET6WBW/1759264805.214409 |
| Review list | membership | 7 reports: those not Passed in Collect & Win or Level-end rewards | — | — | material | 68daad83bacf52c6ea7e1593 (changed by 68dc11dceb76ad640995fd98) |

Areas (solver/truth.json):

| Area | Reports | Open reports | Status | Source |
|---|---|---|---|---|
| Tutorials | 5 | 3 | Open | f_cb40955893624e1acb8500 |
| Level-end rewards | 5 | 3 | Open | f_cb40955893624e1acb8500 |
| Daily Gift | 3 | 3 | Open | f_cb40955893624e1acb8500 |
| Season Pass | 5 | 5 | Open | f_cb40955893624e1acb8500 |
| Collect & Win | 4 | 4 | Open | f_cb40955893624e1acb8500 |
| Win Streak | 3 | 3 | Open | f_cb40955893624e1acb8500 |
| Zombie Lane | 3 | 1 | Open | f_cb40955893624e1acb8500 |
| Boss Arena | 3 | 1 | Open | f_cb40955893624e1acb8500 |
| Endless Mode | 4 | 4 | Open | f_cb40955893624e1acb8500 |
| Card packs | 4 | 2 | Open | f_cb40955893624e1acb8500 |

Reports (solver/truth.json; the row number is the pass sheet's # column):

| Report | Area | Status | Ticket | Review list | Ticket state (as found → to set) | Source |
|---|---|---|---|---|---|---|
| Back to back tutorials at level 16-17 only play the first one | Tutorials | Waiting on QA | new sub-issue | No | — → In Validation | f_cb40955893624e1acb8500 row 1 |
| Card upgrade tutorial never shows after the Zombie Lane one | Tutorials | Waiting on QA | new sub-issue | No | — → In Validation | f_cb40955893624e1acb8500 row 2 |
| Quest tutorial arrow points at the wrong tab after the last panel closes | Tutorials | Passed | new sub-issue | No | — → Done | f_cb40955893624e1acb8500 row 3 |
| Win streak tutorial at level 20 freezes the home screen | Tutorials | Waiting on a fix | ZOM-567 | No | Todo → Todo | f_cb40955893624e1acb8500 row 4 |
| Coin animation plays again after killing and reopening the app | Level-end rewards | Passed | new sub-issue | No | — → Done | f_cb40955893624e1acb8500 row 5 |
| Level-end coins fly while the pre-level panel is already open | Level-end rewards | Waiting on QA | ZOM-568 | Yes | Todo → In Validation | f_cb40955893624e1acb8500 row 6 |
| Reward count-up is skipped when tapping fast on play | Level-end rewards | Passed | new sub-issue | No | — → Done | f_cb40955893624e1acb8500 row 7 |
| Stars from the level fly to the wrong corner on tablets | Level-end rewards | Waiting on a fix | ZOM-569 | Yes | Todo → Todo | f_cb40955893624e1acb8500 row 8 |
| Season pass popup comes up on top of the daily gift when both are due | Daily Gift | Waiting on a fix | new sub-issue | No | — → Todo | f_cb40955893624e1acb8500 row 9 |
| Daily gift calendar opens before the level-end coins finish | Daily Gift | Waiting on a fix | ZOM-570 | No | Todo → Todo | f_cb40955893624e1acb8500 row 10 |
| Daily gift day counter keeps going after a skipped day | Daily Gift | Waiting on a fix | ZOM-556 | No | Todo → Todo | f_cb40955893624e1acb8500 row 11 |
| Season pass icon animation restarts every time a panel closes | Season Pass | Waiting on a fix | ZOM-571 | No | In Validation → Todo | f_cb40955893624e1acb8500 row 12 |
| Season pass start popup shows again after every level until it is claimed | Season Pass | Waiting on QA | ZOM-572 | No | Todo → In Validation | f_cb40955893624e1acb8500 row 13 |
| Season pass reward claim animation plays twice when coming back from the shop | Season Pass | Waiting on QA | ZOM-573 | No | Todo → In Validation | f_cb40955893624e1acb8500 row 14 |
| Event bar starts filling while the daily gift popup is still open | Collect & Win | Waiting on a fix | ZOM-574 | Yes | In Validation → Todo | f_cb40955893624e1acb8500 row 15 |
| Endless unlock banner shows again after coming back from a level | Endless Mode | Waiting on a fix | ZOM-575 | No | Todo → Todo | f_cb40955893624e1acb8500 row 16 |
| Reward animation waits too long before the event bar fills | Collect & Win | Waiting on a fix | ZOM-585 | Yes | In Validation → Todo | f_cb40955893624e1acb8500 row 17 |
| Event panel opens over the level-end rewards on first unlock | Collect & Win | Waiting on QA | ZOM-576 | Yes | In Validation → In Validation | f_cb40955893624e1acb8500 row 18 |
| Event progress popup opens before the level-end coins finish | Collect & Win | Waiting on a fix | ZOM-577 | Yes | Todo → Todo | f_cb40955893624e1acb8500 row 19 |
| Win streak freezer from the abandoned pack never shows up on the home screen | Win Streak | Waiting on a fix | ZOM-560 | No | Todo → Todo | f_cb40955893624e1acb8500 row 20 |
| Streak counter jumps by two after a win when other panels are waiting | Win Streak | Waiting on a fix | ZOM-578 | No | Todo → Todo | f_cb40955893624e1acb8500 row 21 |
| Zombie Lane reward animation plays under the home buttons | Zombie Lane | Passed | new sub-issue | No | — → Done | f_cb40955893624e1acb8500 row 22 |
| Zombie Lane panel opens twice after claiming | Zombie Lane | Passed | new sub-issue | No | — → Done | f_cb40955893624e1acb8500 row 23 |
| Lane progress bar animates from zero every time | Zombie Lane | Waiting on a fix | ZOM-586 | No | Todo → Todo | f_cb40955893624e1acb8500 row 24 |
| Boss arena tutorial does not play when another tutorial is queued before it | Boss Arena | Waiting on QA | new sub-issue | No | — → In Validation | f_cb40955893624e1acb8500 row 25 |
| Boss arena unlock popup shows behind the level-end rewards | Boss Arena | Passed | new sub-issue | No | — → Done | f_cb40955893624e1acb8500 row 26 |
| Arena entry button can be tapped during the reward animation | Boss Arena | Passed | new sub-issue | No | — → Done | f_cb40955893624e1acb8500 row 27 |
| Endless unlock banner overlaps the daily gift | Endless Mode | Waiting on a fix | ZOM-579 | No | Todo → Todo | f_cb40955893624e1acb8500 row 28 |
| Coming back from Endless replays the home intro animation | Endless Mode | Waiting on a fix | new sub-issue | No | — → Todo | f_cb40955893624e1acb8500 row 29 |
| Endless reward chest opens before the coins land | Endless Mode | Waiting on a fix | ZOM-580 | No | Todo → Todo | f_cb40955893624e1acb8500 row 30 |
| Tap to collect prompt is missing when a pack opens after a level | Card packs | Passed | new sub-issue | No | — → Done | f_cb40955893624e1acb8500 row 31 |
| Pack opening sound keeps playing on the home screen after the pack closes | Card packs | Waiting on a fix | ZOM-581 | No | In Validation → Todo | f_cb40955893624e1acb8500 row 32 |
| Last pack does not show its cards before closing | Card packs | Passed | new sub-issue | No | — → Done | f_cb40955893624e1acb8500 row 33 |
| Pack count on the home button only updates after a restart | Card packs | Waiting on a fix | ZOM-582 | No | Todo → Todo | f_cb40955893624e1acb8500 row 34 |
| Tutorial hand stays on screen after the last panel closes | Tutorials | Passed | new sub-issue | No | — → Done | f_cb40955893624e1acb8500 row 35 |
| Level-end rewards do not show at all right after an app update | Level-end rewards | Waiting on a fix | ZOM-583 | Yes | Todo → Todo | f_cb40955893624e1acb8500 row 36 |
| Win streak freezer popup opens behind the season pass popup | Win Streak | Waiting on QA | ZOM-584 | No | Todo → In Validation | f_cb40955893624e1acb8500 row 37 |
| Pass progress bar fills before the tokens arrive | Season Pass | Waiting on QA | new sub-issue | No | — → In Validation | f_cb40955893624e1acb8500 row 38 |
| Pass icon glow stays on after everything is claimed | Season Pass | Waiting on a fix | new sub-issue | No | — → Todo | D05U73FNDDL/1759252212.611349 |

## 5 · Discovery map

Root causes and findings appear only here and never in the prompt.

| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |
|---|---|---|---|---|---|---|
| F1 Brian's ask | the epic, the stock-take sheet, the share, the slide, five numbers back | D0770ET6WBW/1759264805.214409 | YES (DM member) | met first (the anchor) | — | Yes (anchor AN1) |
| F2 Brian's note on the ticket | areas, what counts as a report, the three statuses, the ticket rule, states, Clear and Open, the review list, the tabs | comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 | YES (Linear unscoped) | named by the hub ('I left a note on the ticket') | comments need their own read | Yes for the ticket (anchor AN2); the note's content No |
| F3 Vincent's flow pass sheet | 38 rows: #, Area, What happens, Found on, Ticket, Fix, Re-test | f_cb40955893624e1acb8500 | YES (shared with Calvin) | named by the hub and the note; its cells are the claims met first | a sheet, not a chat | No |
| F4 pass sheet legend | ok, nr, again, 'ok, chat'; Fix is the PR he was told | f_d3a1aa5976285aac98ffda | YES (shared with Calvin) | the sheet's own note points at it | a second doc to open | No |
| F5 Arthur's rule for QA passes | a pass only counts on a build of the main branch | f_6d0326fa006b136f1bbf82 | YES (shared with Calvin) | named by role in the note ('Arthur's rule for QA passes'); the decoy f_ea7517885d11570b54bf13 sits beside it | a search for QA passes also returns the other game's doc | No |
| F6 DD hotfix doc (decoy) | a branch-build pass is enough, for DD hotfixes | f_ea7517885d11570b54bf13 | YES (shared with Calvin) | decoy for F5 | title names DD | No |
| F7 Leonard's review card | Thu Oct 2; Collect & Win and Level-end rewards | 68daad83bacf52c6ea7e1593 (changed by 68dc11dceb76ad640995fd98) | YES (Trello unscoped) | Brian's earlier line D0770ET6WBW/1759164072.337219 and the first invitation first; overturned by the changed card | the card is off the DM path | No |
| F8 Brian's earlier line | Friday; collect&win and daily gift first | D0770ET6WBW/1759164072.337219 | YES (DM member) | met first, in the same DM as the hub | reads as the agenda | No |
| F9 first invitation | Fri Oct 3; Collect & Win and Daily Gift | calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com> | YES (Calvin's mailbox) | met first | older mail on the same meeting | No |
| F10 updated invitation | Thu Oct 2; agenda changed on the card | calvin.price@harmonygames.co/<calendar-f2b39cd5-884e-2def-a4d7-d41d80d4c55b@google.com> | YES (Calvin's mailbox) | after F9 | says the card changed, not what to | No |
| F11 the review event | Thu Oct 2 18:00 UTC; Leonard, Brian, Arthur, Julia, Vincent, Calvin | evt_342a813cb7765d4a6fce8d | YES (Calvin's calendar) | named by the hub ('everyone on the review invite') | — | No |
| F12 review comment on #472 | the season pass icon restart is not in that diff | harmonygames-Games/match3d#472#rc_1 | YES (GitHub unscoped) | the sheet's Fix cell and ZOM-571 In Validation first; overturned by Arthur's comment | the review body is empty; the comment is inline | No |
| F13 review comment on #475 | the pack sound stop is not in it | harmonygames-Games/match3d#475#rc_1 | YES (GitHub unscoped) | the sheet's Fix cell and ZOM-581 In Validation first; overturned by Arthur's comment | same | No |
| F14 Oliver's comment on his PR | #473 also has the pass start popup fix and the bar fill fix | harmonygames-Games/match3d#473#c_2 | YES (GitHub unscoped) | blank Fix cells and ZOM-572 Todo first; overturned by the comment | no sheet cell points at #473 | No |
| F15 GitHub app copies in #zombie-prs | the same three comments | 8e02c1142dfdd380c577a14bc366ee1d; 69700214ac2e727feec1d08d2b873218; 66dd5332dde5b7312c0ae201c285a323 | YES (channel member) | a second route to F12 to F14 | thread replies under bot posts | No |
| F16 pass popup came back | on Android Submission 135 the pass popup came up on top of the gift again | C08R27X0EAH/1759267212.418339 | YES (channel member) | nr on row 9 first; overturned by Vincent's later reply | a reply under a Sep 15 thread; the root is outside a recent-history read | No |
| F17 home intro came back | on Android Submission 135 the home intro played again after Endless | C08R27X0EAH/1759268652.552719 | YES (channel member) | ok on row 29 first; overturned by Robert's reply under his Sep 10 endless thread | a reply under a three-week-old thread; the root is outside a recent-history read | No |
| F18 Marcus's report | the pass icon glow stays on after everything is claimed | D05U73FNDDL/1759252212.611349 | YES (DM member) | the sheet reads as the whole list first | a DM no anchor names | No |
| F19 day counter row's ticket | ZOM-556 | comment_b3c560833d151268202546002e7613cf on ZOM-556 | YES (Linear unscoped) | no key in the sheet first; the tie is Vincent's note | the ticket's title uses other words | No |
| F20 freezer row's ticket | ZOM-560 | comment_9f28b3d8d66bd04e3f7fc46bc6ed1ea9 on ZOM-560 | YES (Linear unscoped) | no key in the sheet first; the tie is Vincent's note | the ticket's title uses other words | No |
| F21 Vincent's 18 tickets | ZOM-567 to ZOM-584; ZOM-571, ZOM-576, ZOM-581 In Validation, the rest Todo | ZOM-567 | YES (Linear unscoped) | keys are in the sheet | states are claims, not facts | No |
| F22 Calvin's folder | ZM queue manager | d_36cdb0374c4aad3b8bf741 | YES (Calvin owns it) | named by the hub | — | Yes, by its plain name if needed |
| F23 Calvin's deck | ZM queue manager, four slides | f_637e63ae6c1b4a7eb016aa | YES (Calvin owns it) | named by the hub | — | Yes, by its plain name if needed |
| F24 which build 'ok, chat' was on | Calvin's line naming iOS Internal #1718 | D06UPGF5PQV/1758817744.353289 | YES (DM member) | Vincent's ok D06UPGF5PQV/1758820544.160399 first | the build number is in the line before the ok | No |
| F25 where #1718 was built from | Calvin's QueueManager branch | C05433XK267/1758817549.151639 | YES (channel member) | overturns 'ok, chat' on rows 1, 2 and 25 | the branch is in the bot post's text | No |
| F26 Android Submission #135 | a main build, Sep 30 20:13 UTC | C05433XK267/1759263189.219529 | YES (channel member) | dates F16 and F17 after the passes | a busy channel | No |
| F27 PR #465 | merged Sep 25; coin replay and queued tutorials | harmonygames-Games/match3d#465 | YES (GitHub unscoped) | the Fix cell of rows 1, 2, 5, 25 | — | No |
| F28 the parked input blocker | Brian: not a problem right now | D0770ET6WBW/1758808795.588519 | YES (DM member) | could read as a report; the note keeps it off | — | No |
| F29 Julia's point about Calvin's tickets | why no priority or assignee on the new ones | D05HYDTG5TJ/1756838837.147599 | YES (DM member) | the note states the rule itself | — | No |
| F30 Vincent's Bug Checklist canvas | left as it is | C08R27X0EAH/1755139050.519009 | YES (channel member) | could read as more reports; the note keeps it out | a canvas next to the list | No |
| F31 Oliver's skip tutorial exceptions | stay off the list | C08R27X0EAH/1758903616.346579 | YES (channel member) | could read as reports; the note keeps them off | — | No |

## 5a · Search-as-persona proof

`persona_view.py search calvin_price <service> "<query>" --limit 3 --no-hidden` reads base data; seeded rows Calvin can see are counted from the SQL overlay (check-sql PASS for every scoped seeded record, dossier 1.E). For a base fact the hit id is the target record among the visible hits. Outputs verbatim below the table.

| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |
|---|---|---|---|---|---|---|
| F1 | slack | flow review | 0 base + 2 seeded | n/a (--no-hidden) | D0770ET6WBW/1759264805.214409 | YES (seeded; check-sql YES) |
| F2 | linear | Queue Manager | 3 base + 0 seeded | 0 | comment_faaa792418a942cd40be046d8d217a7d | YES (base hit on the parent record; the seeded comment sits on it, unscoped) |
| F3 | gsheets | flow pass | 0 base + 2 seeded | 0 | f_cb40955893624e1acb8500 | YES (seeded; check-sql YES) |
| F4 | gdocs | pass sheets | 0 base + 1 seeded | 0 | f_d3a1aa5976285aac98ffda | YES (seeded; check-sql YES) |
| F5 | gdocs | QA passes | 0 base + 2 seeded | 0 | f_6d0326fa006b136f1bbf82 | YES (seeded; check-sql YES) |
| F6 | gdocs | hotfix builds | 0 base + 1 seeded | 0 | f_ea7517885d11570b54bf13 | YES (seeded; check-sql YES) |
| F7 | trello | flow review | 0 base + 5 seeded | 0 | 68daad83bacf52c6ea7e1593 | YES (seeded; unscoped) |
| F8 | slack | daily gift first | 0 base + 1 seeded | n/a (--no-hidden) | D0770ET6WBW/1759164072.337219 | YES (seeded; check-sql YES) |
| F9 | gmail | flow review | 0 base + 15 seeded | n/a (--no-hidden) | calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com> | YES (seeded; check-sql YES) |
| F10 | gmail | Updated invitation | 164 base + 5 seeded | n/a (--no-hidden) | calvin.price@harmonygames.co/<calendar-f2b39cd5-884e-2def-a4d7-d41d80d4c55b@google.com> | YES (seeded; check-sql YES) |
| F11 | gcal | flow review | 0 base + 6 seeded | 0 | evt_342a813cb7765d4a6fce8d | YES (seeded; check-sql YES) |
| F12 | github | Win&Collect into Queue Manager | 3 base + 1 seeded | 0 | harmonygames-Games/match3d#472#rc_1 | YES (base hit on the parent record; the seeded comment sits on it, unscoped) |
| F13 | github | animated icons | 3 base + 0 seeded | 0 | harmonygames-Games/match3d#475#rc_1 | YES (base hit on the parent record; the seeded comment sits on it, unscoped) |
| F14 | github | Addressables/sp | 3 base + 0 seeded | 0 | harmonygames-Games/match3d#473#c_2 | YES (base hit on the parent record; the seeded comment sits on it, unscoped) |
| F15 | slack | season pass icon | 22 base + 1 seeded | n/a (--no-hidden) | 8e02c1142dfdd380c577a14bc366ee1d | YES (seeded; check-sql YES) |
| F16 | slack | pass popup | 9 base + 2 seeded | n/a (--no-hidden) | C08R27X0EAH/1759267212.418339 | YES (seeded; check-sql YES) |
| F17 | slack | home intro | 0 base + 1 seeded | n/a (--no-hidden) | C08R27X0EAH/1759268652.552719 | YES (seeded; check-sql YES) |
| F18 | slack | icon glow | 0 base + 1 seeded | n/a (--no-hidden) | D05U73FNDDL/1759252212.611349 | YES (seeded; check-sql YES) |
| F19 | linear | daily gift is skipped | 1 base + 0 seeded | 0 | comment_b3c560833d151268202546002e7613cf | YES (base hit on the parent record; the seeded comment sits on it, unscoped) |
| F20 | linear | win streak freezer | 2 base + 1 seeded | 0 | comment_9f28b3d8d66bd04e3f7fc46bc6ed1ea9 | YES (base hit on the parent record; the seeded comment sits on it, unscoped) |
| F21 | linear | Season pass icon | 0 base + 1 seeded | 0 | ZOM-567 | YES (seeded; unscoped) |
| F22 | gdrive | queue manager | 0 base + 2 seeded | 0 | d_36cdb0374c4aad3b8bf741 | YES (seeded; check-sql YES) |
| F23 | gslides | queue manager | 0 base + 2 seeded | 0 | f_637e63ae6c1b4a7eb016aa | YES (seeded; check-sql YES) |
| F24 | slack | already tested | 8 base + 0 seeded | n/a (--no-hidden) | D06UPGF5PQV/1758817744.353289 | YES (base hit) |
| F25 | slack | Internal - #1718 | 3 base + 0 seeded | n/a (--no-hidden) | C05433XK267/1758817549.151639 | YES (base hit) |
| F26 | slack | Android Submission | 1175 base + 2 seeded | n/a (--no-hidden) | C05433XK267/1759263189.219529 | YES (base hit) |
| F27 | github | queue manager | 3 base + 1 seeded | 0 | harmonygames-Games/match3d#465 | YES (base hit) |
| F28 | slack | input blocker | 117 base + 0 seeded | n/a (--no-hidden) | D0770ET6WBW/1758808795.588519 | YES (base hit) |
| F29 | slack | tickets | 251 base + 0 seeded | n/a (--no-hidden) | D05HYDTG5TJ/1756838837.147599 | YES (base hit) |
| F30 | slack | Bug Checklist | 5 base + 0 seeded | n/a (--no-hidden) | C08R27X0EAH/1755139050.519009 | YES (base hit) |
| F31 | slack | skip tutorial | 16 base + 0 seeded | n/a (--no-hidden) | C08R27X0EAH/1758903616.346579 | YES (base hit) |

```
SEARCH slack 'flow review' as calvin_price  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned
SEARCH linear 'Queue Manager' as calvin_price  scope: hg.py search (unscoped: no ACL filter)
visible hits=3 (showing 3)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/1961/title", "parent_pointer": "/issues/1961", "encoding": "json", "text": "Reward animation and queue manager issues", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/1979/description", "parent_pointer": "/issues/1979", "encoding": "json", "text": "'@julia.lawson to fill up \n\nThe Icon Management System in very simple
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/1983/description", "parent_pointer": "/issues/1983", "encoding": "json", "text": "uld automatically appear when it's first introduced or in any other day
SEARCH gsheets 'flow pass' as calvin_price  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gdocs 'pass sheets' as calvin_price  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gdocs 'QA passes' as calvin_price  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gdocs 'hotfix builds' as calvin_price  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH trello 'flow review' as calvin_price  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH slack 'daily gift first' as calvin_price  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned
SEARCH gmail 'flow review' as calvin_price  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned
SEARCH gmail 'Updated invitation' as calvin_price  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=164 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "calvin.price@harmonygames.co/1761735700542994345", "last": "2023-03-29T20:34:49Z", "subject": "Updated invitation: [PERSON_NAME_0099] & [PERSON_NAME_0029] Welcome @ Mon Apr 3, 2023 1pm - 1:20pm (EDT) (calvin.price@harmonygames.co)", "snippet": "Updated invitation: [PERSON_NAME_0099] & [PERSO
  {"id": "calvin.price@harmonygames.co/1765666268644423422", "last": "2023-05-12T05:49:31Z", "subject": "Updated invitation: Company Stand Up @ Weekly from 11am to 11:30am on Monday, Wednesday, Friday from Fri Apr 7 to Thu May 11 (CST) (calvin.price@harmonygames.co)", "snippet": "Updated invitation: C
  {"id": "calvin.price@harmonygames.co/1766270289551787118", "last": "2023-05-18T21:50:10Z", "subject": "Updated invitation: Company Stand Up @ Fri May 19, 2023 10am - 10:15am (CST) (calvin.price@harmonygames.co)", "snippet": "Updated invitation: Company Stand Up @ Fri May 19, 2023 10am - 10:15am (CST
note: --no-hidden: containers outside the persona's view were not scanned
SEARCH gcal 'flow review' as calvin_price  scope: GCal event summary (base events carry no description/location)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
note: counted per meeting instance (ical_uid + start), visible if any copy is visible
SEARCH github 'Win&Collect into Queue Manager' as calvin_price  scope: hg.py search (unscoped: no ACL filter)
visible hits=3 (showing 3)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json", "service_file": "data.json", "pointer": "/commits/1393/message", "parent_pointer": "/commits/1393", "encoding": "json", "text": "Implement Win&Collect into Queue Manager\n\nImplement Win&Collect into Queue Mana
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json", "service_file": "data.json", "pointer": "/pull_requests/2377/title", "parent_pointer": "/pull_requests/2377", "encoding": "json", "text": "Implement Win&Collect into Queue Manager", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json", "service_file": "data.json", "pointer": "/pull_requests/2377/body", "parent_pointer": "/pull_requests/2377", "encoding": "json", "text": "Implement Win&Collect into Queue Manager\n\n<!-- This is an auto-generat
SEARCH github 'animated icons' as calvin_price  scope: hg.py search (unscoped: no ACL filter)
visible hits=3 (showing 3)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json", "service_file": "data.json", "pointer": "/pull_requests/2357/title", "parent_pointer": "/pull_requests/2357", "encoding": "json", "text": "Marcus/animated icons", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json", "service_file": "data.json", "pointer": "/pull_requests/2357/body", "parent_pointer": "/pull_requests/2357", "encoding": "json", "text": "\n\n<!-- This is an auto-generated comment: release notes by coderabbit.
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json", "service_file": "data.json", "pointer": "/pull_requests/2359/title", "parent_pointer": "/pull_requests/2359", "encoding": "json", "text": "[PERSON_NAME_0029]/animated icons", "truncated": false}
SEARCH github 'Addressables/sp' as calvin_price  scope: hg.py search (unscoped: no ACL filter)
visible hits=3 (showing 3)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json", "service_file": "data.json", "pointer": "/commits/4428/message", "parent_pointer": "/commits/4428", "encoding": "json", "text": "Merge branch 'main' into addressables/sp", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json", "service_file": "data.json", "pointer": "/pull_requests/2378/title", "parent_pointer": "/pull_requests/2378", "encoding": "json", "text": "Addressables/sp", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json", "service_file": "data.json", "pointer": "/pull_requests/2378/head_ref", "parent_pointer": "/pull_requests/2378", "encoding": "json", "text": "addressables/sp", "truncated": false}
SEARCH slack 'season pass icon' as calvin_price  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=22 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=1 in 1 containers
  {"id": "C050WGU41HR/1745901316.093169", "channel": "engineering-bots", "kind": "private", "date": "2025-04-29", "user": "SLACK_BOT_0004_SLACK_ID", "reply": false, "snippet": "ce, if player exit, it no longer displays even clicking the season pass Icon."}
  {"id": "C05433XK267/1742860575.471419", "channel": "builds", "kind": "public", "date": "2025-03-24", "user": "SLACK_BOT_0005_SLACK_ID", "reply": false, "snippet": "n>) DD iOS - #1322 - feature/seasonpass Changes: - enabling season pass icon on world map ui [[PERSON_NAME_0022]]"}
  {"id": "C05433XK267/1742911791.791009", "channel": "builds", "kind": "public", "date": "2025-03-25", "user": null, "reply": false, "snippet": " getting event from backend [[PERSON_NAME_0022]] - enabling season pass icon on world map ui [[PERSON_NAME_0022]] - Adding print blob on debug option and re"
note: --no-hidden: containers outside the persona's view were not scanned
SEARCH slack 'pass popup' as calvin_price  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=9 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C050WGU41HR/1745620875.509049", "channel": "engineering-bots", "kind": "private", "date": "2025-04-25", "user": "SLACK_BOT_0004_SLACK_ID", "reply": false, "snippet": "Season Pass Popup should only display once per season.   First Try Event should only display once"}
  {"id": "C050WGU41HR/1745901316.093169", "channel": "engineering-bots", "kind": "private", "date": "2025-04-29", "user": "SLACK_BOT_0004_SLACK_ID", "reply": false, "snippet": "abel but clicking on it disappears the event icon.   Season Pass PopUp was showing once, if player exit, it no longer display
  {"id": "C05433XK267/1745707115.226189", "channel": "builds", "kind": "public", "date": "2025-04-26", "user": null, "reply": false, "snippet": " event. [Calvin Price] - Fix Queue manager , display season pass popup after streak fever poup [Calvin Price] - Fix queue manager and Win&amp;Collect "}
note: --no-hidden: containers outside the persona's view were not scanned
SEARCH slack 'home intro' as calvin_price  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned
SEARCH slack 'icon glow' as calvin_price  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned
SEARCH linear 'daily gift is skipped' as calvin_price  scope: hg.py search (unscoped: no ACL filter)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/3632/title", "parent_pointer": "/issues/3632", "encoding": "json", "text": "When the daily gift is skipped, it doesn't reset to 0.", "truncated": false}
SEARCH linear 'win streak freezer' as calvin_price  scope: hg.py search (unscoped: no ACL filter)
visible hits=2 (showing 2)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/3637/title", "parent_pointer": "/issues/3637", "encoding": "json", "text": "The abandoned pack win streak freezer reward is not granted.", "truncated": f
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/3637/description", "parent_pointer": "/issues/3637", "encoding": "json", "text": "The other packs have the right components and everything works fine. \n
SEARCH linear 'Season pass icon' as calvin_price  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gdrive 'queue manager' as calvin_price  scope: Drive file/folder names (on-disk file content is not searched)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH gslides 'queue manager' as calvin_price  scope: GSlides title + page element text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
SEARCH slack 'already tested' as calvin_price  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=8 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=1 in 1 containers
  {"id": "C050WGU41HR/1727280932.458309", "channel": "engineering-bots", "kind": "private", "date": "2024-09-25", "user": "SLACK_BOT_0004_SLACK_ID", "reply": false, "snippet": "les that are moving into the hand pile.  [PERSON_NAME_0050] already tested the branch."}
  {"id": "C050WGU41HR/1727528518.606969", "channel": "engineering-bots", "kind": "private", "date": "2024-09-28", "user": "SLACK_BOT_0004_SLACK_ID", "reply": false, "snippet": "onfusion and had to change the names in There as well. I've already tested it and works and now i think it looks more visibil
  {"id": "C050WGU41HR/1727532647.383229", "channel": "engineering-bots", "kind": "private", "date": "2024-09-28", "user": "SLACK_BOT_0004_SLACK_ID", "reply": false, "snippet": "onfusion and had to change the names in There as well. I've already tested it and works and now i think it looks more visibil
note: --no-hidden: containers outside the persona's view were not scanned
SEARCH slack 'Internal - #1718' as calvin_price  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=3 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C05433XK267/1758817262.251429", "channel": "builds", "kind": "public", "date": "2025-09-25", "user": "SLACK_BOT_0005_SLACK_ID", "reply": false, "snippet": "Match 3D iOS Internal - #1718 Started by user Calvin Price (<http://blake.tplinkdns.com:9009/job/Match%203D%2"}
  {"id": "C05433XK267/1758817549.151639", "channel": "builds", "kind": "public", "date": "2025-09-25", "user": "SLACK_BOT_0005_SLACK_ID", "reply": false, "snippet": "Match 3D iOS Internal - #1718 - [PERSON_NAME_0029]/QueueManager Success after 5 min 2 sec (<http://blake.tpli"}
  {"id": "D06UPGF5PQV/1758817744.353289", "channel": "D06UPGF5PQV", "kind": "im", "date": "2025-09-25", "user": "EMPLOYEE_0006_SLACK_ID", "reply": false, "snippet": "I think I may have fixed the tutorial stuffs. Match 3D iOS Internal - #1718 already tested"}
note: --no-hidden: containers outside the persona's view were not scanned
SEARCH slack 'Android Submission' as calvin_price  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1175 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C050WGU41HR/1705185805.160009", "channel": "engineering-bots", "kind": "private", "date": "2024-01-13", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "Yeah. I'm making an android submission so we can use internal testing to verify"}
  {"id": "C050WGU41HR/1739481156.117169", "channel": "engineering-bots", "kind": "private", "date": "2025-02-13", "user": "SLACK_BOT_0004_SLACK_ID", "reply": true, "snippet": "leted by spamming the \"collect\" button.>   Version or date: android submission 135  *Description:*  Normally, the reward scr
  {"id": "C050WGU41HR/1741301980.858409", "channel": "engineering-bots", "kind": "private", "date": "2025-03-06", "user": "SLACK_BOT_0004_SLACK_ID", "reply": true, "snippet": " is always on when a new session starts>   Version or date: android submission 149  ### Description:  The vibration preference
note: --no-hidden: containers outside the persona's view were not scanned
SEARCH github 'queue manager' as calvin_price  scope: hg.py search (unscoped: no ACL filter)
visible hits=3 (showing 3)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json", "service_file": "data.json", "pointer": "/commits/479/message", "parent_pointer": "/commits/479", "encoding": "json", "text": "Fixing queue manager flow", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json", "service_file": "data.json", "pointer": "/commits/872/message", "parent_pointer": "/commits/872", "encoding": "json", "text": "Update season pass VFX, queue order\n\nUpdate season Pass VFX to not bleed through 
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json", "service_file": "data.json", "pointer": "/commits/1107/message", "parent_pointer": "/commits/1107", "encoding": "json", "text": "Added queue manager to boot scene", "truncated": false}
SEARCH slack 'input blocker' as calvin_price  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=117 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=6 in 2 containers
  {"id": "C050WGU41HR/1713484390.358199", "channel": "engineering-bots", "kind": "private", "date": "2024-04-18", "user": "SLACK_BOT_0004_SLACK_ID", "reply": false, "snippet": "0397efa>` - Fix for 2nd event fade issue + added delay with input blocker"}
  {"id": "C050WGU41HR/1713538514.304129", "channel": "engineering-bots", "kind": "private", "date": "2024-04-19", "user": "SLACK_BOT_0004_SLACK_ID", "reply": false, "snippet": "2587cd9c5f6cc58e0cb0616d363c9bf0c33|b5ecf258>` - Streak bar input blocker duration descreased"}
  {"id": "C050WGU41HR/1713543229.279279", "channel": "engineering-bots", "kind": "private", "date": "2024-04-19", "user": "SLACK_BOT_0004_SLACK_ID", "reply": false, "snippet": "2fafaa6eed2cd1105c422410ab16b7279bd38f1|42fafaa6>` - Adding input blocker to megatile tutorial because [PERSON_NAME_0050] dem
note: --no-hidden: containers outside the persona's view were not scanned
SEARCH slack 'tickets' as calvin_price  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=251 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=4 in 3 containers
  {"id": "C04RYU8TJ8K/1696632924.195809", "channel": "random", "kind": "public", "date": "2023-10-06", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "my new favorite linear view as I’m assigning tickets to Blake :[USERNAME_42656]:"}
  {"id": "C04RYU8TJ8K/1701127974.031629", "channel": "random", "kind": "public", "date": "2023-11-27", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "Given how airplane tickets is not a fixed price good, I be hesitant on buying airline credits"}
  {"id": "C04RYU8TJ8K/1705351797.234189", "channel": "random", "kind": "public", "date": "2024-01-15", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "[PERSON_NAME_20559] lives in Ohio now but he has season tickets to the Buffalo Bills"}
note: --no-hidden: containers outside the persona's view were not scanned
SEARCH slack 'Bug Checklist' as calvin_price  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=5 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=1 in 1 containers
  {"id": "C08R27X0EAH/1755139050.519009", "channel": "zombie-bugs", "kind": "private", "date": "2025-08-14", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Bug Checklist – v0"}
  {"id": "C08R27X0EAH/1755140754.370399", "channel": "zombie-bugs", "kind": "private", "date": "2025-08-14", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Bug Checklist – v0"}
  {"id": "C08R27X0EAH/1756222021.289149", "channel": "zombie-bugs", "kind": "private", "date": "2025-08-26", "user": "EMPLOYEE_0012_SLACK_ID", "reply": false, "snippet": "Bug Checklist"}
note: --no-hidden: containers outside the persona's view were not scanned
SEARCH slack 'skip tutorial' as calvin_price  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=16 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C050WGU41HR/1721842160.962409", "channel": "engineering-bots", "kind": "private", "date": "2024-07-24", "user": "EMPLOYEE_0021_SLACK_ID", "reply": false, "snippet": "SON_3233_SLACK_ID> in the debug panel, There are options to skip tutorials, if you are stuck in characters tutorial, scroll do
  {"id": "C050WGU41HR/1737015919.210499", "channel": "engineering-bots", "kind": "private", "date": "2025-01-16", "user": "SLACK_BOT_0004_SLACK_ID", "reply": false, "snippet": "specific level to trigger?  With this changes, if you don't skip tutorials/reload the game.. everything seems to work fine.  
  {"id": "C050WGU41HR/1741000515.307309", "channel": "engineering-bots", "kind": "private", "date": "2025-03-03", "user": "EMPLOYEE_0002_SLACK_ID", "reply": false, "snippet": "evel doesnt load up. Back in the day i had to play a bit to skip tutorials and stuff and then the board scene would have work.
note: --no-hidden: containers outside the persona's view were not scanned
```

## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · persona-readable · unique · instructions-not-answer) | Inferable |
|---|---|---|---|---|
| ten area children under the epic | comment_faaa792418a942cd40be046d8d217a7d | deliverable (Brian's ask) | hub D0770ET6WBW/1759264805.214409 'I left a note on the ticket about how I want it' · YES · one note by Brian on ZOM-543 · rules, no answers | yes, once the hub is followed |
| which reports are in the list | comment_faaa792418a942cd40be046d8d217a7d | scope | comment_faaa792418a942cd40be046d8d217a7d · YES · unique · a scope sentence, no list | yes |
| status of each report | comment_faaa792418a942cd40be046d8d217a7d | scope | comment_faaa792418a942cd40be046d8d217a7d names 'Arthur's rule for QA passes' · YES · f_6d0326fa006b136f1bbf82 is the one ZM doc with that subject · rule, no answers | yes, through the note |
| ticket reuse, move, note and state | comment_faaa792418a942cd40be046d8d217a7d | none | comment_faaa792418a942cd40be046d8d217a7d · YES · unique · instruction | gotcha with a record trigger |
| no priority and no assignee on new ones | comment_faaa792418a942cd40be046d8d217a7d | none | comment_faaa792418a942cd40be046d8d217a7d · YES · unique · instruction | gotcha with a record trigger |
| review list | comment_faaa792418a942cd40be046d8d217a7d | none | comment_faaa792418a942cd40be046d8d217a7d 'in an area on the agenda of Thursday's review' · YES · one card 68daad83bacf52c6ea7e1593 · names areas, not reports | gotcha with a record trigger |
| stock-take sheet in the folder, shared with the review's people | D0770ET6WBW/1759264805.214409 | destination + recipients | hub 'share it with everyone on the review invite, Leonard too' · YES · one event evt_342a813cb7765d4a6fce8d · names people, no answers | yes |
| tabs and columns | comment_faaa792418a942cd40be046d8d217a7d | none | comment_faaa792418a942cd40be046d8d217a7d · YES · unique · instruction | gotcha with a record trigger |
| one slide with the numbers | D0770ET6WBW/1759264805.214409 | deliverable | hub · YES · one deck f_637e63ae6c1b4a7eb016aa in Calvin's Drive · instruction | yes |
| five numbers back to Brian | D0770ET6WBW/1759264805.214409 | deliverable | hub 'tell me here' · YES · DM D0770ET6WBW · instruction | yes |

Anchor-name table (noun phrases of at most 6 words; `;` separates synonyms):

| Anchor | May be named |
|---|---|
| AN1 | Brian's message from yesterday; Brian's DM |
| AN2 | the Queue Manager ticket; ZOM-543 |

## 7 · Dates and constraints

| Item | Absolute date or value | Source | Past fact or deadline |
|---|---|---|---|
| Calvin's today | Wednesday Oct 1, 2025 (clock 2025-10-01 00:00 PT = 07:00 UTC) | 00_Task_Context.json universe.persona_today; last hub record D0770ET6WBW/1759264805.214409 | — |
| Brian's ask | Tue Sep 30, 2025 13:40 PT (20:40 UTC): 'yesterday' for Calvin | D0770ET6WBW/1759264805.214409 | past fact |
| Brian's note on the ticket | Tue Sep 30, 2025 13:25 PT (20:25 UTC) | comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 | past fact |
| Vincent's pass started | Fri Sep 26, 2025 (sheet created 03:12 PT, 10:12 UTC) | f_cb40955893624e1acb8500 | past fact |
| pass sheet last changed | Tue Sep 30, 2025 12:30 PT (19:30 UTC) | f_cb40955893624e1acb8500 | past fact |
| review card changed | Tue Sep 30, 2025 10:22 PT (17:22 UTC) | 68dc11dceb76ad640995fd98 | past fact |
| first invitation | Mon Sep 29, 2025 09:05 PT (16:05 UTC), for Fri Oct 3 | calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com> | past fact |
| updated invitation | Tue Sep 30, 2025 10:24 PT (17:24 UTC), for Thu Oct 2 | calvin.price@harmonygames.co/<calendar-f2b39cd5-884e-2def-a4d7-d41d80d4c55b@google.com> | past fact |
| the flow review | Thu Oct 2, 2025 11:00 to 11:30 PT (18:00 to 18:30 UTC; 12pm CST on Calvin's invitation): 'Thursday' or 'tomorrow' | evt_342a813cb7765d4a6fce8d | deadline (future event); no deadline is graded |
| Android Submission #135 | Tue Sep 30, 2025 13:13 PT (20:13 UTC) | C05433XK267/1759263189.219529 | past fact |
| latest seeded record | Tue Sep 30, 2025 14:44 PT (21:44 UTC), before the clock | C08R27X0EAH/1759268652.552719 | past fact |

## 8 · Difficulty levers

| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |
|---|---|---|---|---|
| Ambiguity | yes | yes | what decides a report's status is spread over the note, the legend, the rule doc, build posts and PRs (F2 to F5, F24 to F27) | the prompt names the two anchors only, never where an answer lives |
| Dynamic change | yes | yes | sheet cells, ticket states and the first invitation are met first and overturned later (F7, F12 to F14, F16, F17) | the prompt names neither a first reading nor what corrects it |
| Multi-source | yes | yes | Linear, Sheets, Slack, GitHub, Docs, Trello, Gmail, Calendar, Drive, Slides | no source named as an exact artifact beyond the two anchors |
| Async | no | no | Friction: none (03_Error_Async_Config.txt) | — |
| Error recovery | no | no | Friction: none | — |
| Access control | no | no | every load-bearing record is Calvin-visible (check-sql PASS) | no ask to read someone else's scoped data |

## 9 · Must not appear in the prompt

- **Tool and server names (catalog.json):** linear_create_issue, linear_update_issue, linear_create_comment, linear_list_issues, linear_list_comments, slack_send_message, slack_read_thread, slack_search_public_and_private, slack_conversations_history, github_get_pull_request_comments, github_get_pull_request_reviews, gsheets_create_spreadsheet, gsheets_values_update, gsheets_batch_update, gdrive_share_file, gdrive_move_file, gslides_batch_update, gmail_search_messages, gcal_list_events, trello_search, any MCP server name.
- **Opaque ids and filenames:** f_cb40955893624e1acb8500, f_d3a1aa5976285aac98ffda, f_6d0326fa006b136f1bbf82, f_ea7517885d11570b54bf13, d_36cdb0374c4aad3b8bf741, f_637e63ae6c1b4a7eb016aa, evt_342a813cb7765d4a6fce8d, 68daad83bacf52c6ea7e1593, D0770ET6WBW, D06UPGF5PQV, D05U73FNDDL, C08R27X0EAH, C0880U9751A, C093LEZGF6J, C05433XK267, every ZOM key other than ZOM-543.
- **Findings and root causes:** any status, any count (10, 9, 20, 0, 7, 39, 38, 19, 20, 10), any area name, #builds or any build number (#1718, 135), the QueueManager branch, any PR number (#465, #472, #473, #475) or review comment, Vincent's thread reply, Robert's post, Oliver's comment, Marcus or his report, ZOM-556, ZOM-560, ZOM-571, ZOM-572, ZOM-581.
- **Hidden authorities and rules:** Brian's note's content or any of its sentences, the three statuses, the state mapping, Clear and Open, the review list rule, the tabs and columns, the pass sheet's legend, Arthur's doc or its rule, the DD doc, Leonard's card or Trello, the invitation mails, the review having moved, Julia's point.
- **Format and choreography:** markdown, numbered steps, a per-column content list, a service list, a call count, 'first … then …'.
- **Friction and files:** none configured; no reference files or /app/artifact paths.

## 10 · Entity traps

`entity.py collisions` and `entity.py resolve` for every name the prompt could use, verbatim:
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
  EMPLOYEE_0024: {'entities': ['scott <employee_0024@harmonygames.co>', '? <slack:EMPLOYEE_0024_SLACK_ID>', '? <trello:3d36d70154e6a715614e0d75>'], 'records': ['gcal.calendar_id=employee_0024@harmonygames.co', 'gcal.owner_email=employee_0024@harmonygames.co', 'linear.id=usr_EMPLOYEE_0024', 'linear.email=employee_0024@harmonygames.co', 'contacts.email=employee_0024@harmonygames.co', 'email.email=employee_0024@harmonyg
  EMPLOYEE_0032: {'entities': ['? <EMPLOYEE_0032_EMAIL>', 'Josh Dempsey <josh.dempsey@harmonygames.co>', '? <github:EMPLOYEE_0032_GITHUB_USERNAME>', '? <slack:EMPLOYEE_0032_SLACK_ID>'], 'records': ['confluence.id=user_EMPLOYEE_0032', 'gmail.mailbox=EMPLOYEE_0032_EMAIL', 'gdrive.email=EMPLOYEE_0032_EMAIL', 'linear.id=usr_EMPLOYEE_0032', 'linear.email=EMPLOYEE_0032_EMAIL', 'contacts.email=EMPLOYEE_0032_EMAIL', 'email.e
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
== resolve Brian
no exact match for 'Brian'
  candidate: email:brian.foster@harmonygames.co  Brian Foster  ['brian.foster@harmonygames.co']
== resolve Vincent
no exact match for 'Vincent'
  candidate: email:vincent.parker@harmonygames.co  Vincent Parker  ['vincent.parker@harmonygames.co']
== resolve Leonard
no exact match for 'Leonard'
  candidate: email:leonard.hayes@harmonygames.co  Leonard Hayes  ['leonard.hayes@harmonygames.co']
== resolve Arthur
no exact match for 'Arthur'
  candidate: email:arthur.blake@harmonygames.co  Arthur Blake  ['arthur.blake@harmonygames.co']
== resolve Julia
no exact match for 'Julia'
  candidate: email:julia.lawson@harmonygames.co  Julia Lawson  ['julia.lawson@harmonygames.co']
== resolve Marcus
ENTITY trello:c48a210d5c5a4b59231c6873  name=Marcus  kind=person  emails=[]
  trello     id=c48a210d5c5a4b59231c6873, username=marcus, fullName=Marcus   [join: own_record (ambiguous name)]
  absent from: slack, gmail, gcal, gdrive, linear, github, confluence, contacts
  last activity: -
  UNRESOLVED (ambiguous_name): mononym 'Marcus' is an exact name of [] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']
== resolve Robert
ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
  persona: robert - Co-Founder & Creative Director / Executive
  slack      id=EMPLOYEE_0016_SLACK_ID, name=Robert, real_name=Robert, email=robert@harmonygames.co, is_bot=False, deleted=False, messages=110334, first_post=2023-03-15, last_post=2025-10-01   [join: exact_email]
  gmail      mailbox=robert@harmonygames.co, threads=14813, messages=17363, first=2023-03-15, last=2025-10-01   [join: exact_email]
  gcal       calendar_id=robert@harmonygames.co, owner_email=robert@harmonygames.co, summary=Robert — primary, events=1133, last_event_before_clock=2025-09-30   [join: exact_email]
  gdrive     id=user_9f7ba94f7526, email=robert@harmonygames.co, display_name=Robert, root_folders=['d_9f7ba94f7526d54d8482ba'], owned_items=190, last_modified=2025-09-25, files_shared_with=412   [join: exact_email]
  linear     id=usr_Robert, email=robert@harmonygames.co, name=Robert, is_active=True, last_activity=2025-09-30   [join: exact_email]
  github     login=EMPLOYEE_0016_GITHUB_USERNAME, name=Robert, email=robert@harmonygames.co, type=User, last_activity=2025-09-29   [join: exact_email]
== resolve Oliver
no exact match for 'Oliver'
  candidate: email:oliver.brooks@harmonygames.co  Oliver Brooks  ['oliver.brooks@harmonygames.co']
== resolve Calvin
no exact match for 'Calvin'
  candidate: email:calvin.price@harmonygames.co  Calvin Price  ['calvin.price@harmonygames.co']
```

| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |
|---|---|---|---|
| Brian Foster | none by first name | the requester; Calvin's DM partner in D0770ET6WBW | brian.foster@harmonygames.co |
| Vincent Parker | none by first name | QA; owner of the pass sheet | vincent.parker@harmonygames.co |
| Arthur Blake | 'Blake' in base talk; mail thread files named blake@ | one person | arthur.blake@harmonygames.co |
| Leonard Hayes | none | organizer of the review | leonard.hayes@harmonygames.co |
| Julia Lawson | Peter Lawson | Julia is on the invite | julia.lawson@harmonygames.co |
| Marcus Bennett | Marcus Lee, Oscar Bennett, github and trello 'Marcus' | Calvin's DM partner is Bennett; the prompt must not name him | marcus.bennett@harmonygames.co |
| Robert (one name) | none | co-founder; posts in #zombie-match3d and #zombie-bugs | robert@harmonygames.co |
| Oliver Brooks | Lauren Brooks | Oliver wrote and merged #473 | oliver.brooks@harmonygames.co |
| Calvin Price | Nathan Price; two GitHub identities for Calvin | the persona | calvin.price@harmonygames.co |
| ZOM tickets | ENG tickets (DD) | ZM is on ZOM; the decoy doc f_ea7517885d11570b54bf13 is about DD | ZOM-543 |
| the Queue Manager ticket | 'Reward animation and queue manager issues' and other tickets that mention a queue manager | ZOM-543 is titled Queue Manager and is Calvin's | ZOM-543 |

## 11 · Pre-submit checklist

- [ ] Persona voice: Calvin, first person, plain; no spec-sheet layout
- [ ] Names only the two anchors (§6 table); no §9 item
- [ ] States the deliverables at the level Brian's DM does, or simply points at it; destination named
- [ ] No tool or server name; no step list; no count; no area name
- [ ] No word that the review moved, that a pass may not count, or that something came back
- [ ] 'yesterday' for Brian's message and 'Thursday' for the review are the only dates, if any
- [ ] Clean spelling and punctuation; no riddle, hint, hedge or if-chain
- [ ] 20–4,000 words
- [ ] Run `/create-prompt-writing check` before `/prompt`

## 12 · Blockers and routed defects

None blocking. No fact is routed to /create-injection: every §5 fact is found by a natural search or reached by reading an anchor's DM, ticket, sheet or card (§5a). rev3 (sha256 479b8441f52e) needs its own platform /injection before /prompt; the prompt text is the one /prompt scored 5 on rev1.

Open, not blocking: the fixes made after the two blind sweeps of the SQL were not swept again; the pre-check must confirm that Slack tools return the attachment text of the #builds posts (C05433XK267/1758817549.151639) and of the #zombie-prs copies; no independent red team ran (fallback recorded in the scenario design, section 13). The under-60 % requester target stays at risk until the pre-check run.

## 13 · Self-review

| Area | Counter-reading (strongest argument it fails) | Evidence that resolves it | Verdict |
|---|---|---|---|
| Fair readings (C6) | Rows 1, 2 and 25 are Passed: Vincent said ok in the chat. | f_6d0326fa006b136f1bbf82 counts only main builds; C05433XK267/1758817549.151639 shows #1718 came from Calvin's QueueManager branch; harmonygames-Games/match3d#465 is merged, so Waiting on QA | settled |
| Fair readings (C6) | Row 12 is Waiting on QA: #472 is merged and ZOM-571 is In Validation. | comment_faaa792418a942cd40be046d8d217a7d 'a fix for it is in main'; harmonygames-Games/match3d#472#rc_1 | settled |
| Fair readings (C6) | Rows 13 and 38 are Waiting on a fix: the sheet names no PR. | comment_faaa792418a942cd40be046d8d217a7d 'a fix for it is in main that QA has not tried on a main build yet'; harmonygames-Games/match3d#473#c_2 | settled |
| Fair readings (C6) | Row 9 stays Passed: Vincent's reply is about another thread's topic. | f_6d0326fa006b136f1bbf82 'A pass stands until somebody sees the bug again on a main build made after the one it passed on'; C08R27X0EAH/1759267212.418339 names Android Submission 135, C05433XK267/1759263189.219529 | settled |
| Fair readings (C6) | Row 29 stays Passed: Robert is not QA. | the note says 'somebody'; C08R27X0EAH/1759268652.552719 | settled |
| Fair readings (C6) | Daily Gift is on the review list: Brian said so on Sep 29. | the note names the review's agenda and the updated invitation puts it on the roadmap card; 68dc11dceb76ad640995fd98 is later than D0770ET6WBW/1759164072.337219 and calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com> | settled |
| Fair readings (C6) | Marcus's line is not a report: it is a chat remark. | comment_faaa792418a942cd40be046d8d217a7d 'any bug somebody else on the team saw in a build and told you about in a DM since Vincent started his pass on the 26th'; D05U73FNDDL/1759252212.611349 | settled |
| Fair readings (C6) | Rows 11 and 20 get new sub-issues: the sheet has no key. | comment_faaa792418a942cd40be046d8d217a7d 'if a ticket already has the report, move that ticket'; comment_b3c560833d151268202546002e7613cf; comment_9f28b3d8d66bd04e3f7fc46bc6ed1ea9 | settled |
| Clarity (C7) | 'tell me here' could be a thread reply or a new DM message. | §4b accepts both, in D0770ET6WBW (D0770ET6WBW/1759264805.214409) | accepted outcomes |
| Clarity (C7) | The share leaves the role open, and the sheet's title is not given. | §4b accepts any role for the five attendees of evt_342a813cb7765d4a6fce8d and any title | accepted outcomes |
| Incorporation (C8) | The note might not be reached: the prompt names only the DM. | hub D0770ET6WBW/1759264805.214409 says 'I left a note on the ticket about how I want it'; comment_faaa792418a942cd40be046d8d217a7d is Brian's only note on ZOM-543 and Linear is unscoped | incorporated |
| Incorporation (C8) | 'Arthur's rule for QA passes' could be the DD doc. | f_6d0326fa006b136f1bbf82 is titled 'ZM builds and QA passes'; f_ea7517885d11570b54bf13 is titled for DD hotfixes | unique |
| Truthfulness (C17) | 'yesterday' could be the wrong day for Brian's message. | D0770ET6WBW/1759264805.214409 is Tue Sep 30 13:40 PT and Calvin's today is Wed Oct 1 (00_Task_Context.json) | true |
| Truthfulness (C17) | Calvin might not own the ticket or the folder. | ZOM-543 is assigned to Calvin (base); d_36cdb0374c4aad3b8bf741 and f_637e63ae6c1b4a7eb016aa are owned by calvin.price@harmonygames.co in the SQL | true |
| Feasibility / ACL (C18–C19) | The sheet must sit in Calvin's folder with two tabs and be shared; a new sheet lands in his root with one tab. | gsheets_create_spreadsheet, gsheets_batch_update to add the tab, gdrive_move_file to d_36cdb0374c4aad3b8bf741, gdrive_share_file; Calvin owns the folder | feasible |
| Feasibility / ACL (C18–C19) | Calvin cannot read the other attendees' invitations. | his own event copy evt_342a813cb7765d4a6fce8d lists all six attendees, and calvin.price@harmonygames.co/<calendar-f2b39cd5-884e-2def-a4d7-d41d80d4c55b@google.com> is in his mailbox | feasible |
| Feasibility / ACL (C18–C19) | States or parents might not be settable. | Todo, In Validation and Done are states on base ZOM tickets (ZOM-556 Todo); linear_create_issue and linear_update_issue take state and parentId | feasible |
| Contrived register (C15–C16) | Pointing at Brian's DM could read as hiding the destination. | the prompt names the DM and the ticket, and the DM itself names the folder, the deck and where to answer (D0770ET6WBW/1759264805.214409); prompt_qc_cases hidden_destination | ordinary |
| Contrived register (C15–C16) | Listing what Brian wants could read as a command list. | deliverables and who to tell are the screen-24 skeleton, not sequenced method steps; ZOM-543 stays named as an anchor only | ordinary |

Fair readings, clarity, incorporation, truthfulness, feasibility / ACL and the contrived register are each addressed above with evidence. Unresolved: the prompt is not yet written, and check mode re-tests every point on the actual text.

```
STAGE GATE prompt-writing: PASS — Task_Authoring/task_inputs · 04_Prompt_Writing_Brief.md#b42cfa5ecf15 · 00_Assigments.md#a8cc00ce24ff · 01_Grounding_Dossier.md#88526f435b5f · 01_Universe_Inject.sql#479b8441f52e · 03_Error_Async_Config.txt#52b2d02d66d3 · 01a_Hardening_Report.md#35ccd8634d0f · __context__#7be566a0936c · __assignment__#d644f7ef43f6 · __policy__#dc4ab5df3cdd · __gate_policy__#cc68bf5564ff · __review__#fd6a51a31848 · blocking 0 · warnings 0 · checks 25
[PASS] assignment.v3_context: Calvin Price / Game Engineer (Unity VFX); hard cap <70%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Writing_Brief.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql, 03_Error_Async_Config.txt, 01a_Hardening_Report.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#479b8441f52e, 01_Hardness_Manifest.json#bffb088156a7, 01_Grounding_Dossier.md#88526f435b5f, solver/solver.py#337c6a63f446, 01c_Dispositions.json#818f309bd758, 01c_Preflight_Report.json#6bb345bafeb1, 00_Assigments.md#a8cc00ce24ff, 01_Scenario_Design.md#cd79a4e0e490, 01_Hardness_Manifest.draft.json#b79d491b46aa, 01_Gradable_Surface.json#e2392bcc269e, __context__#7be566a0936c, __assignment__#d644f7ef43f6, __policy__#dc4ab5df3cdd, __gate_policy__#5b7d4d20094d, __review__#e8f09c674b67)
[PASS] chain.error-async: upstream 'error-async' PASS pasted and current (03_Error_Async_Config.txt#52b2d02d66d3, 00_Assigments.md#a8cc00ce24ff, 01_Grounding_Dossier.md#88526f435b5f, 01_Universe_Inject.sql#479b8441f52e, __context__#7be566a0936c, __assignment__#d644f7ef43f6, __policy__#dc4ab5df3cdd, __gate_policy__#cc68bf5564ff, __review__#15d71f843716)
[PASS] structure.sections: 14 required sections present and non-empty (04_Prompt_Writing_Brief.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Writing_Brief.md
[PASS] evidence.situation: 4/4 items carry a source pointer (min 100%)
[PASS] evidence.final_state: 79/79 items carry a source pointer (min 100%)
[PASS] evidence.discovery_map: 31/31 items carry a source pointer (min 100%)
[PASS] evidence.dates: 11/11 items carry a source pointer (min 100%)
[PASS] evidence.entity_traps: 11/11 items carry a source pointer (min 100%)
[PASS] tool.search_as_persona: 31 facts proven findable by persona_view search as calvin_price
[PASS] reach.brief: 22 scoped load-bearing ids YES for calvin_price
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] structure.accepted_outcomes: V3 accepts multiple fair outcomes; see v3.fair_outcomes_review
[PASS] boundary.anchor_naming: 2 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 19 evidenced counter-readings (of 19 found; need ≥ 6) in 04_Prompt_Writing_Brief.md
[PASS] review.coverage: self-review addresses all 6 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.fair_outcomes_review: current accepted outcomes and considered alternatives recorded; multiple fair outcomes are allowed
[PASS] readiness.context: explicit task/revision and current upstream evidence verified
[PASS] handoff.pasted: pasted into the Self-review by --paste
```


