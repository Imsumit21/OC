# Prompt Brief — jl-zm-difficulty-baseline · prep
> Built 2026-10-30 from 00_Assigments.md, 01_Universe_Inject.sql (sha256 dd7536cdea3f, hardening round 4: Leonard's reply in the thread under Julia's Sep 29 DM question, plus the PR #401 updated_at fix; round 3: Blake's 'not tiers' review on match3d#265 and Leonard's card attachment; earlier 52c581f442c1, rule 5 build clause limited to the starting tier after /prompt attempt 7; revision after /prompt attempt 2 (6adfee3ef9092601a61245bb_1_prompt (1).md); local injection gate PASS; previous SQL 37a8c7ab3444 passed /injection — Audit-Report/0_injection_PASS.md), Working_Files/01_Grounding_Dossier.md, 01_Scenario_Design.md (v5), 01_Hardness_Manifest.json · 03_Error_Async_Config.txt: Friction: none (error-async gate PASS) · no 02_Reference_Files_Manifest.md (no attachments) · Persona view verified: all load-bearing records YES for julia_lawson (check-sql PASS, dossier §1.E); Android 0.3.133's base store post sits in #executives, which Julia is not in; it is not needed (Blake's mail states the build).
> 04_Prompt.txt may be drafted by Claude (`/create-prompt-writing draft`) or written by the human.
> **Clock:** 2025-10-01T00:00:00Z (Wednesday). The latest seeded event is Leonard's ask D05HB64NMQU/1759261706.530914 (2025-09-30T19:48:26Z, Tue 12:48 PM PT). The tuning session (Mon 2025-10-06 17:00Z, evt_91674a9c23d012a9ac34da) is future.

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
|---|---|---|
| Business function | Product → Product & Design (`Evals/references/rules/task_categories.md`) | a PM's pre-tuning baseline for the Zombie Match 3D difficulty system, asked by Leonard in his DM with Julia (D05HB64NMQU/1759261706.530914) |
| Persona / role | Julia Lawson, julia.lawson@harmonygames.co, Product Manager (roster `julia_lawson`, Product) | Voice: plain, short, lowercase-ok (C090N54TG79/1757610131.672669 "I prefer the difficulty increase to come from monsters primarily"; C090N54TG79/1758689839.300009 "I will stop level making at 300"). Read scope: #zombie-design (C090N54TG79), #zombie-match3d (C0880U9751A), #zombie-bugs (C08R27X0EAH) member; own mailbox; ZM Difficulty folder writer (d_96489e1e00a56685625939); Linear/Trello/GitHub unscoped |
| Competency | Engineering Ops | release-state retrieval: what in the difficulty tickets players actually have in the store builds vs tooling-only, replaced or never shipped, and where ticket text and the build disagree (julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>); remit: Julia set the per-monster enrage values (C08R27X0EAH/1756922765.033199) and adjusted the level difficulty labels (match3d commits 737e0278, 37aaef73) |
| Task skill | Retrieval | 109 candidate ZOM tickets × their Linear notes, the rules card + amendment (68daca5871dba40417a00383, 68dbfa4362a051efb5e0ae45), the build mail + reply, the enrage sheet (f_0ba93ae0238d9ed4178212), the deck (f_048bf5e69f8e7f1a659a5c), ZOM-42, PRs #243/#265/#401, assembled into a register; stacked: Actions (the sheet, shares, the reply, two ticket comments) |
| Task type / tier | Long Horizon (100–500+; author target ≥ 120 calls every run, average < 75%) | 10 services carry weight (Linear, Slack, Trello, Gmail, Sheets, Slides, Docs, Drive, Calendar, GitHub); 109 per-ticket comment reads; manifest budget 147 (01_Hardness_Manifest.json call_budget); `HARDNESS GATE (long): PASS` in the dossier self-review |
| Difficulty mode / date | medium (recorded); October 1, 2025 07:00 | nothing on/after Wed Oct 1 00:00Z may be described as done |

## 2 · Situation

| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |
|---|---|---|---|
| Leonard wants a baseline of the difficulty system before Monday's tuning session, not from memory: every difficulty ticket since ZM started, whether players have it in the store builds, the tier and enrage numbers as they are today; rules on the difficulty baseline card; reply with the counts when it's in the folder | Julia, in her DM with Leonard | D05HB64NMQU/1759261706.530914 (Tue Sep 30, 12:48 PM PT) | — |
| Brian's recap for Monday says everything incl. the editor bits shipped and enrage is +50% for every monster | Julia, #zombie-design | C090N54TG79/1759185077.402611 | — |
| Vincent asks for the list in #zombie-design | Julia, #zombie-design | C090N54TG79/1759248760.118527 | — |
| Android 0.3.133's store post | — | C07C2866011/1759075866.111309 | #executives (Julia not a member); Blake's mail states the build julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> |

No cause belongs in the situation. Why the obvious list is wrong (tag-only members, the attack-power amendment, stripped tooling, the > 90 check, the replaced blunder mechanic, per-monster enrage) is discovery-only (§5, never in the prompt).

## 3 · Investigation → action

Questions to resolve (no answers here):
1. Which tickets belong on the register (the card's scope, its amendment, the closing-note tag, the window, duplicates)?
2. Which of them players actually have in today's store builds, which are tooling only, which were replaced and by what, which never shipped?
3. How the starting tier, promotion, demotion (and the level drop after one) and enrage work in the store builds today?
4. Which tickets say something the builds don't do, and which got replaced?
5. Where the register goes and who gets which access?

Writes they feed: W1 register (1–3) → W2 placement + shares (5) → W3 Linear comments (4) → W4 reply in Leonard's DM (counts from W1). No write is a bolt-on: each is named by the ask or the card it names.

## 4 · Pinned final state (UGT anchor)

| Deliverable | Required contents (requirements) | Destination (exact) | Recipient(s) (exact) | Catalog write (reference only; never in the prompt) | Fed by |
|---|---|---|---|---|---|
| W1 register | Tickets tab: 24 rows (ticket, title, Linear state as found, status, replaced-by for Replaced) — 16 Live (incl. ZOM-281, tagged by Blake's note though assigned to someone else), 4 Editor only, 3 Not shipped, 1 Replaced (ZOM-254 → ZOM-282); ZOM-30, 49, 50, 161, 262, 275 left off (Leonard's thread reply D05HB64NMQU/1759262838.442871); ZOM-312 left off (Blake's 'not tiers' inline comment on match3d#265, harmonygames-Games/match3d#265#rc_7, under rule 1); ZOM-258 left off (Leonard's 'notes for monday' doc, attached to the card); ZOM-162, 163, 201, 250 left off (Leonard's reply in the thread under Julia's Sep 29 DM question, D05HB64NMQU/1759267002.665190); Rules in force tab: starting tier (when a new player's 10th game ends, wins and losses both counting, avg CPM > 90 → tier 1, else tier 0; card rule 5 'go by the build', TierManager.cs totalGames == 10), promotion (80%+ over up to the last 10; tier -2 promotes after 1 win), demotion (4 losses in a row, or ≤ 50% over up to the last 10; record resets after each move), level drop after a demotion (yes, ZOM-303), enrage (speed and damage per monster from the Live tab, no HP) | a Google Sheet in the ZM Difficulty folder d_96489e1e00a56685625939 | — | gsheets_create_spreadsheet + gsheets_values_update (+ gdrive_move_file) | 68daca5871dba40417a00383; f_9ec79682ff351aa466364a; truth in support/task_work/jl_difficulty/truth.json |
| W2 shares | Robert can edit; Brian and Leonard can comment (Leonard's later reply D05HB64NMQU/1759267002.665190 takes back the checklist's 'Brian gets edit'); Arthur can view (Leonard's notes doc f_f494073fc667097c3c2c6b) | the register file | robert@harmonygames.co (writer); brian.foster@harmonygames.co, leonard.hayes@harmonygames.co (commenter); arthur.blake@harmonygames.co (reader) | gdrive_share_file | 68daca5871dba40417a00383 rule 7; checklist 68dc033bf7d24e86b8a9cc67 "rule 7 change"; evt_91674a9c23d012a9ac34da attendees |
| W3 Linear comments | ZOM-199: the build checks CPM > 90, not >= 90 (90 exactly stays on tier 0); ZOM-254: replaced by ZOM-282; each of the 4 Editor only (ZOM-173, 200, 277, 315) and 3 Not shipped (ZOM-202, 280, 293) tickets: the change isn't in the store builds; none on ZOM-162, 163, 201, 250 | 9 existing issues (no new issues) | — | linear_create_comment | julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>; 68daca5871dba40417a00383 rule 6; checklist 68dc033bf7d24e86b8a9cc67 "rule 6 change" |
| W4 reply | the register is in the folder; 24 tickets: 16 Live, 4 Editor only, 3 Not shipped, 1 Replaced; ZOM-254 was replaced by ZOM-282 (Leonard's notes doc f_f494073fc667097c3c2c6b); a new player gets the starting tier after their first 10 games, won or lost (match3d TierManager.cs totalGames == 10; card rule 5 "go by the build"), not after level 10; the Not shipped keys (ZOM-202, 280, 293) and the Editor only keys (ZOM-173, 200, 277, 315) | DM D05HB64NMQU (Leonard ↔ Julia) | Leonard (EMPLOYEE_0038_SLACK_ID) | slack_send_message | D05HB64NMQU/1759261706.530914 "reply here" |

| Decision-ambiguity risk | Alternative a careful run could take | What pins it |
|---|---|---|
| reply place | post in #zombie-design (Vincent's request) | the ask says "reply here" (D05HB64NMQU/1759261706.530914); Vincent's post is not from the requester (C090N54TG79/1759248760.118527) |
| which rules card | the Domino Delights "Difficulty baseline" card | the ask names "the difficulty baseline card on the zm roadmap board" (D05HB64NMQU/1759261706.530914); the DD card is on another board for another game (683dbef4e319167a802bd888) |
| share list | Robert only (the one named on the card) | card rule 7 "everyone on the tuning session invite" (68daca5871dba40417a00383); the invite lists Leonard, Julia, Robert, Arthur, Brian (evt_91674a9c23d012a9ac34da) |
| register location | Julia's own Drive root | card rule 7 "The register goes in the ZM Difficulty folder" (68daca5871dba40417a00383); Julia is writer on d_96489e1e00a56685625939 |
| layout | one tab or a doc | card rule 2 "Layout as in the session agenda" → "One sheet with two tabs, Tickets and Rules in force" (f_9ec79682ff351aa466364a) |
| comment vs new ticket | a new Linear issue for the > 90 finding, or a comment on ZOM-42 / ZOM-200 | card rule 6 "comment on it … Same tickets, no new ones" (68daca5871dba40417a00383); the reply names ZOM-199 (julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>) |
| rule 6 and 7 as written vs the checklist | no comments on Editor only / Not shipped; Brian as commenter | the card's checklist 68dc033bf7d24e86b8a9cc67 (addChecklistToCard 2025-09-30T16:20:11Z) says "rule 6 change" and "rule 7 change" explicitly |
| scope as written vs the thread reply | keep ZOM-30, 49, 50, 161, 262, 275 (35 rows) | Leonard's thread reply under the ask (D05HB64NMQU/1759262838.442871, after the ask) names the six to leave off |
| extra ticket comments | comments on ZOM-42 ("6-7 levels"), ZOM-275 (tutorial text), ZOM-282 ("+50%") | card rule 6 allows only tickets Blake's mail or reply says are wrong (ZOM-199, julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>) and Replaced ones (ZOM-254); "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included" (68daca5871dba40417a00383) |
| Replaced set | ZOM-282 Replaced by match3d#401; ZOM-250 Replaced by ZOM-277; ZOM-246 by ZOM-263; ZOM-274 by ZOM-295; ZOM-262 by ZOM-275 | card rule 4 "Replaced: only when another ticket's closing note says it replaces this one … a ticket players never had stays Editor only or Not shipped" (68daca5871dba40417a00383); only ZOM-282's note says it replaces a ticket (ZOM-254); harmonygames-Games/match3d#401#c_2 says #401 only splits the value |
| ZOM-271 "ATK POWER" | count it as attack power (36 tickets) | Leonard's card comment "attack power in the title counts too, written out (ATK on its own doesn't)" (68dbfa4362a051efb5e0ae45); a scan of every ZOM title up to Aug 31 finds no other near-miss form |
| window edge | Apr 21 read in Pacific time drops ZOM-23 and ZOM-30 | card rule 1 "created up to Aug 31 (so everything since we started ZM)" (68daca5871dba40417a00383); no title match before ZOM-23 and none Aug 30 – Sep 2 (linear data, first ZOM ticket 2025-04-18) |
| persona vs agent | "I'll share it" in the prompt | §11: every write is asked of the assistant (D05HB64NMQU/1759261706.530914 asks Julia) |

### 4b · Canonical outcome (one acceptance class)

| Deliverable | Field | Fixed value (pinned, with locator) | Delegated by | Allowed equivalence class | Material / representational |
|---|---|---|---|---|---|
| W1 | kind/location | a Google Sheet in d_96489e1e00a56685625939 (68daca5871dba40417a00383 rule 7; f_9ec79682ff351aa466364a "one sheet") | — | created there or moved there | material |
| W1 | title | — (68daca5871dba40417a00383 names none) | the card and the agenda name no title (f_9ec79682ff351aa466364a) | any title | representational |
| W1 | tabs | Tickets; Rules in force (f_9ec79682ff351aa466364a) | — | those names or clear equivalents, two tabs | material |
| W1 | row set | the 24 members (truth.json; incl. tag-only ZOM-221/300/305/378 via cmt_735d60b29ce006b58217 and ZOM-281 via cmt_df69e4a92767cbff0000 and attack-power ZOM-246/263/277/315 via 68dbfa4362a051efb5e0ae45; without ZOM-30, 49, 50, 161, 262, 275 per D05HB64NMQU/1759262838.442871, ZOM-162, 163, 201, 250 per D05HB64NMQU/1759267002.665190, ZOM-258 per f_f494073fc667097c3c2c6b, ZOM-312 per harmonygames-Games/match3d#265#rc_7) | — | any order; dropped tickets may be named in a separate note, never as register rows | material |
| W1 | status | per truth.json: 16 Live, 4 Editor only (ZOM-173, 200, 277, 315 — ZOM-315 is the editor stats-panel total, Assets/Scripts/LevelEditor/UI/StatsPanel.cs), 3 Not shipped (ZOM-202, 280, 293), 1 Replaced (ZOM-254) (68daca5871dba40417a00383 rule 3) | — | the four words or clear synonyms | material |
| W1 | replaced by | ZOM-254 → ZOM-282 (68daca5871dba40417a00383 rule 4; ZOM-282's closing note "this replaces the blunder 2.0 boost from ZOM-254") | — | ZOM-282 by key or title | material |
| W1 | Linear state | as found at the clock (Done except ZOM-202 In Progress, ZOM-280 Canceled, ZOM-293 Todo; ZOM-42 base data) | — | state names as Linear shows them | material |
| W1 | title column / column order / formatting | — (68daca5871dba40417a00383 rule 2 lists columns, not a layout) | the card lists the columns only (68daca5871dba40417a00383) | any | representational |
| W1 | starting tier | when a new player's 10th game ends (wins and losses both count), avg CPM > 90 → tier 1, else tier 0 (card 68daca5871dba40417a00383 rule 5 'go by the build'; TierManager.cs totalGames == 10; julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>) | — | "10 games" or "10 levels played" (/prompt r12); "> 90", "above 90", "90 exactly stays on tier 0" | material |
| W1 | promotion | win rate ≥ 80% over up to the last 10 attempts; tier -2 promotes after one win (ZOM-42) | — | any wording carrying both parts | material |
| W1 | demotion | 4 losses in a row, or ≤ 50% over up to the last 10; record resets after a move (ZOM-42) | — | any wording carrying both triggers | material |
| W1 | level drop after demotion | yes: the current level loads one tier down (ZOM-303) | — | yes / the level drops | material |
| W1 | enrage | per monster, speed and damage only, values from the Live tab, 10 rows matching the per-monster values committed to main before the Sep 26 cut (Bikekid 0.25/0.25, Boxer 0.5/0.4, Cheerleader 0.6/0.4, Chef 0.5/0.5, FootballPlayer 0.6/0.4, Karen 0.4/0.4, Magician 0.2/0.2, Mayor1 0.5/0.5, Plumber 0.3/0.3, MonsterBase base prefab 0.8/0.8; plus the row Mailman, Mayor2, PartyGirl "not copied yet", copied as is — card rule 5 "Copy its Live tab as it stands: a monster it hasn't copied yet goes on the tab as not copied yet, don't work numbers out from anywhere else"; values for those three are never graded), no HP (f_0ba93ae0238d9ed4178212; C090N54TG79/1756912929.304417) | — | the values listed or a pointer to the sheet's Live tab with "per monster, no HP" | material |
| W2 | grantees + role | robert@harmonygames.co writer; brian.foster@harmonygames.co and leonard.hayes@harmonygames.co commenter (Leonard's reply D05HB64NMQU/1759267002.665190 takes back the checklist's 'Brian gets edit'); arthur.blake@harmonygames.co reader (Leonard's notes doc f_f494073fc667097c3c2c6b); (68daca5871dba40417a00383 rule 7; checklist 68dc033bf7d24e86b8a9cc67; evt_91674a9c23d012a9ac34da) | — | direct shares; Leonard's existing folder-owner access also satisfies his row | material |
| W3 | ZOM-199 comment | the build checks > 90, not >= 90 (julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>) | — | any wording carrying "> 90" vs ">= 90" | material |
| W3 | ZOM-254 comment | replaced by ZOM-282 (68daca5871dba40417a00383 rule 6) | — | names ZOM-282 | material |
| W3 | Editor only and Not shipped comments | one on each of the 7: Editor only ZOM-173, 200, 277, 315 and Not shipped ZOM-202, 280, 293 (checklist 68dc033bf7d24e86b8a9cc67 "rule 6 change"); none on ZOM-162, 163, 201, 250 (D05HB64NMQU/1759267002.665190 'no comments on them either') | — | any wording saying the change isn't in the store builds | material |
| W3 | other comments | none; no new issues (68daca5871dba40417a00383 rule 6) | — | no comment on any other ticket | material |
| W4 | counts | 24; 16 Live, 4 Editor only, 3 Not shipped, 1 Replaced (D05HB64NMQU/1759261706.530914; D05HB64NMQU/1759262838.442871; D05HB64NMQU/1759267002.665190) | — | any wording | material |
| W4 | starting tier timing | after a new player's first 10 games, won or lost (D05HB64NMQU/1759261706.530914 asks; card 68daca5871dba40417a00383 rule 5 "for when a new player gets their starting tier … go by the build"; TierManager.cs totalGames == 10, WinHistory.GetTotalGames = wins + losses) | — | any wording that says 10 games/plays/attempts incl. losses; "10 levels" or "level 10" is wrong | material |
| W4 | keys | Not shipped ZOM-202, 280, 293; Editor only ZOM-173, 200, 277, 315 (D05HB64NMQU/1759262838.442871 asks for the keys; the register's set after D05HB64NMQU/1759267002.665190) | — | keys in any order or format | material |
| W4 | place | DM D05HB64NMQU (D05HB64NMQU/1759261706.530914 "reply here") | — | a thread reply or a DM message | material |
| W4 | wording | — (D05HB64NMQU/1759261706.530914) | the ask asks only for the counts (D05HB64NMQU/1759261706.530914) | any | representational |

Rule for 08/09: two runs reach the same final state when every material field matches within its class.

## 5 · Discovery map

| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |
|---|---|---|---|---|---|---|
| F1 the ask (LB) | baseline before Monday; rules on the card; reply with counts | D05HB64NMQU/1759261706.530914 | YES (DM member) | met first | none | Yes — as "Leonard's difficulty baseline ask" (anchor A1) |
| F2 rules card (LB authority) | rules 1–7 | trello 68daca5871dba40417a00383 | YES (unscoped) | decoy DD card 683dbef4e319167a802bd888 | Trello rarely opened | No — the ask names it |
| F3 card comment (LB) | attack power in the title counts too | trello 68dbfa4362a051efb5e0ae45 | YES | amends F2 rule 1 | comments under the description | No |
| F4 store builds mail (LB authority) | iOS 0.3.49 / Android 0.3.133; editor, Editor folders, debug menu stripped | julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> | YES (own mailbox) | overturns Brian's recap C090N54TG79/1759185077.402611 | #zombie-design hit first | No — the card names it |
| F5 Blake's reply (LB) | the build checks cpm > 90, not >= 90 | julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> | YES | overturns ZOM-199 and the deck | second message of the thread | No |
| F6 enrage sheet (LB authority) | Live per-monster speed/damage, hp 0 | gsheets f_0ba93ae0238d9ed4178212 | YES (owner) | decoy f_34f0950581934de1278969; Next pass tab | Next pass copied | No — the card names it |
| F7 Robert's deck | tier rules "90 or more"; +25% blunder line | gslides f_048bf5e69f8e7f1a659a5c | YES (shared) | overturned by F5, F8 | slide text read as current | No |
| F8 Blake's correction (LB) | the deck's blunder part is old: speed and damage per monster, no hp | C090N54TG79/1756912929.304417 | YES (member) | overturns F7 | outside the card's sources | No |
| F9 tuning invite (LB) | attendees Leonard, Julia, Robert, Arthur, Brian | evt_91674a9c23d012a9ac34da | YES (own calendar) | only via F2 rule 7 | Calendar rarely opened | Yes — as "monday's tuning invite": Julia is an attendee and knows it; the attendee list stays undiscovered |
| F10 agenda (LB) | one sheet, tabs Tickets and Rules in force | gdocs f_9ec79682ff351aa466364a | YES (shared) | only via F2 rule 2 | — | No |
| F11 ZM Difficulty folder (LB) | write target | gdrive d_96489e1e00a56685625939 | YES (writer) | — | — | Yes — as "the zm difficulty folder": Julia's own enrage sheet sits in it (f_0ba93ae0238d9ed4178212) |
| F12 ZOM-42 (LB authority) | full tier spec (> 90; 80% over up to 10; 4 losses or ≤ 50%; record resets) | linear ZOM-42 | YES (unscoped) | the deck's 4-loss-only line | list truncates descriptions | No |
| F13 Linear notes (LB) | decisive per ticket; "tiers:" tag on ZOM-221/300/305/378 | linear cmt_735d60b29ce006b58217 (+108 more, minted_ids.json LIN_NOTES) | YES (unscoped) | titles mislead (ZOM-45, ZOM-277) | no list call returns comments | No |
| F14 Brian's recap (trap) | editor bits shipped; +50% for every monster | C090N54TG79/1759185077.402611 | YES | overturned by F4, F6 | conclusion stop | No |
| F15 Vincent's request (distractor) | drop the list in #zombie-design | C090N54TG79/1759248760.118527 | YES | not the requester | — | No |
| F16 DD sheet (decoy) | Domino Delights parameters | gsheets f_34f0950581934de1278969 | YES | scope: other game | "parameter" search | No |
| F17 PR #401 comment (LB) | #401 gives enrage speed and damage separate values (they shared one since ZOM-282); drops the unused EnrageHealth method | harmonygames-Games/match3d#401#c_2 | YES (unscoped) | follows ZOM-282's note cmt_912bdd42ad5c8d51521f; agrees with commit b511fcbcd5 (hp off 2025-06-19) | bot-free PR comment | No |
| F18 iOS release (context) | 0.3.49 released Sep 29 | C0880U9751A/1759182908.627389 | YES (member) | older 0.3.38 C08R27X0EAH/1758081917.318539 | — | No |
| F19 ZOM-199 (LB) | ">= 90" text, the comment target | linear ZOM-199 | YES | overturned by F5 | — | No |
| F20 per-monster enrage remark (context) | "Every monster will enrage differently" | C08R27X0EAH/1756922765.033199 | YES (member) | supports F6 | reply in a thread | No |
| F21 Leonard's thread reply (LB, hardening L1) | leave ZOM-30, 49, 50, 161, 262, 275 off; reply lists the Not shipped and Editor only keys | D05HB64NMQU/1759262838.442871 | YES (DM member) | after the ask; overrides rule 1 for six tickets | thread replies rarely opened (Hardness_Mastery A14) | No |
| F22 card checklist (LB, hardening L2) | rule 6 change (comments on Editor only and Not shipped); rule 7 change (Brian edits) | trello 68dc033bf7d24e86b8a9cc67 | YES (unscoped) | after rule edit and comment; overrides rules 6 and 7 | not in the search or comments result | No |
| F23 ZOM-281 tag (LB, hardening L3) | Blake's "tiers:" note on a ticket assigned to EMPLOYEE_0032 with no card word | linear cmt_df69e4a92767cbff0000 | YES (unscoped) | only via the full comment scan rule 1 asks for | a scan limited to keyword and Blake-assigned tickets misses it | No |
| F24 starting-tier timing (LB, hardening L4) | after the first 10 games, won or lost | match3d Assets/Scripts/DynamicDifficulty/TierManager.cs; Assets/Scripts/Player/WinHistory.cs (GetTotalGames) | YES (unscoped) | ZOM-42, ZOM-199 and the deck say "10 levels" first | the written sources read first | No |

## 5a · Search-as-persona proof

`persona_view.py search` reads only the base export, so seeded rows return 0 there; seeded reach is the dossier's check-sql PASS for julia_lawson (§1.E). Visible hits below are base counts.

| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |
|---|---|---|---|---|---|---|
| F1 | slack | baseline of the difficulty system | base 0; seeded 1 | 0 | D05HB64NMQU/1759261706.530914 | YES (seeded; check-sql YES) |
| F2 | trello | difficulty baseline | base 0; seeded 2 cards | 0 | 68daca5871dba40417a00383 | YES (seeded; unscoped) |
| F3 | trello | attack power | 3 base + seeded comment | 0 | 68dbfa4362a051efb5e0ae45 | YES (seeded; unscoped) |
| F4 | gmail | store builds | base 0; seeded thread | 62 (other mailboxes) | julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> | YES (seeded; own copy) |
| F5 | gmail | store builds (thread) | base 0; seeded 2nd message | 0 | julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> | YES (seeded) |
| F6 | gsheets | monster enrage | base 0; seeded 1 | 0 | f_0ba93ae0238d9ed4178212 | YES (seeded; owner) |
| F7 | gslides | dynamic difficulty | base 0; seeded 1 | 22 | f_048bf5e69f8e7f1a659a5c | YES (seeded; shared) |
| F8 | slack | blunder line | base 0; seeded 1 | 0 | C090N54TG79/1756912929.304417 | YES (seeded; member) |
| F9 | gcal | ZM difficulty tuning | base 0; seeded 1 (own copy) | 0 | evt_91674a9c23d012a9ac34da | YES (seeded) |
| F10 | gdocs | ZM difficulty tuning | base 0; seeded 1 | 0 | f_9ec79682ff351aa466364a | YES (seeded; shared) |
| F11 | gdrive | ZM Difficulty | base 0; seeded folder | 0 | d_96489e1e00a56685625939 | YES (seeded; writer) |
| F12 | linear | Dynamic Difficulty | 3 shown (other games first) + ZOM-42 | 0 | ZOM-42 | YES (unscoped; list ZOM issues) |
| F13 | linear | tiers | 3 base titles; seeded notes via comments | 0 | cmt_735d60b29ce006b58217 | YES (seeded; per-issue comments) |
| F14 | slack | dynamic difficulty push | base 0; seeded 1 | 0 | C090N54TG79/1759185077.402611 | YES (seeded; member) |
| F15 | slack | difficulty list | base 0; seeded 1 | 0 | C090N54TG79/1759248760.118527 | YES (seeded; member) |
| F16 | gsheets | Parameter Optimization | 1 | 0 | f_34f0950581934de1278969 | YES |
| F17 | github | Split enrage | 2 | 0 | harmonygames-Games/match3d#401 | YES (unscoped; seeded #c_2) |
| F18 | slack | 0.3.49 | 2 | 7 | C0880U9751A/1759182908.627389 | YES |
| F19 | linear | Conduct difficulty tier assignment | 1 | 0 | ZOM-199 | YES |
| F20 | slack | enrage differently | 1 | 0 | C08R27X0EAH/1756922765.033199 | YES |
| F21 | slack | difficulty baseline (thread of the ask) | base 0; seeded 1 reply | 0 | D05HB64NMQU/1759262838.442871 | YES (seeded; DM member, check-sql YES) |
| F22 | trello | difficulty baseline (card checklist) | base 0; seeded checklist | 0 | 68dc033bf7d24e86b8a9cc67 | YES (seeded; unscoped) |
| F23 | linear | tiers | 3 base titles; seeded note on ZOM-281 via comments | 0 | cmt_df69e4a92767cbff0000 | YES (seeded; unscoped) |
| F24 | github | totalGames | base code hit | 0 | harmonygames-Games/match3d TierManager.cs | YES (unscoped) |

```
SEARCH slack 'baseline of the difficulty system' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH trello 'difficulty baseline' as julia_lawson  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gmail 'store builds' as julia_lawson  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=62 in 4 containers  UNVERIFIED=0 in 0 containers

SEARCH gsheets 'monster enrage' as julia_lawson  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gslides 'dynamic difficulty' as julia_lawson  scope: GSlides title + page element text
visible hits=0 (showing 0)  hidden by ACL=22 in 22 containers  UNVERIFIED=8 in 8 containers

SEARCH gsheets 'Parameter Optimization' as julia_lawson  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_34f0950581934de1278969", "name": "Parameter Optimization.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Parameter Optimization"}

SEARCH github 'Split enrage' as julia_lawson  scope: hg.py search (unscoped: no ACL filter)
visible hits=2 (showing 2)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH slack '0.3.49' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=2 (showing 2)  hidden by ACL=7 in 1 containers  UNVERIFIED=0 in 0 containers
  {"id": "C0880U9751A/1759182908.627389", "channel": "zombie-match3d", "kind": "private", "date": "2025-09-29", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I just released 0.3.49 on IOS"}

SEARCH linear 'Conduct difficulty tier assignment' as julia_lawson  scope: hg.py search (unscoped: no ACL filter)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH slack 'enrage differently' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C08R27X0EAH/1756922765.033199", "channel": "zombie-bugs", "kind": "private", "date": "2025-09-03", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "And she also change how monsters enrage. Every monster will enrage differently in terms of"}
```

Note: base hit C090N54TG79/1759774021.190659 for "0.3.49" is dated 2025-10-06, after the clock; it does not exist at run time and is not cited.

## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · readable · unique · instructions-not-answer) | Inferable |
|---|---|---|---|---|
| R1–R4 register membership, status, replaced-by, rules tab | 68daca5871dba40417a00383, julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>, f_0ba93ae0238d9ed4178212 | deliverable: the baseline Leonard asked for | D05HB64NMQU/1759261706.530914 · YES · names the card by board · states where the rules are, not the answers | no — needs the anchor |
| R5 folder placement | d_96489e1e00a56685625939 | via the anchor ("when it's in the folder") | 68daca5871dba40417a00383 rule 7 · YES · unique | no |
| R6 reply with counts | D05HB64NMQU/1759261706.530914 | deliverable: the reply to Leonard | D05HB64NMQU/1759261706.530914 · YES · asks, doesn't answer | no — needs the anchor |
| R7 ticket comments | ZOM-199, ZOM-254 | scope via the card | 68daca5871dba40417a00383 rule 6 · YES · unique · states the rule, not the tickets | no |
| R8 shares | evt_91674a9c23d012a9ac34da | recipients via the card | 68daca5871dba40417a00383 rule 7 · YES | no |
| R9 two-tab layout | f_9ec79682ff351aa466364a | format via the card | 68daca5871dba40417a00383 rule 2 · YES | no |

| Anchor | May be named |
|---|---|
| A1 | Leonard's difficulty baseline ask; Leonard's DM; Monday's tuning session |

## 7 · Dates and constraints

| Item | Absolute date or value | Source | Past fact or deadline |
|---|---|---|---|
| Leonard's ask | 2025-09-30T19:48:26Z | D05HB64NMQU/1759261706.530914 | past |
| Store builds cut | 2025-09-26 (iOS 0.3.49 released 2025-09-29) | julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>; C0880U9751A/1759182908.627389 | past |
| Ticket window | created up to 2025-08-31 (first ZOM ticket 2025-04-18) | 68daca5871dba40417a00383 rule 1 | constraint |
| Tuning session | 2025-10-06T17:00Z (Mon) | evt_91674a9c23d012a9ac34da | future (the deadline) |
| Clock | 2025-10-01T00:00:00Z (Wed) | GEN_EXECUTION §3; latest seed D05HB64NMQU/1759261706.530914 | now |

## 8 · Difficulty levers

| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |
|---|---|---|---|---|
| Ambiguity | yes | yes | which tickets count (tag, amendment, window), what "shipped" means, which rules card | the prompt points at the ask only; destination pinned by the card (68daca5871dba40417a00383) |
| Dynamic change | yes | yes | Brian's recap → Blake's mail; deck → reply / Blake's message; ZOM-282 note → #401 comment → sheet | the prompt names neither the recap nor the corrections |
| Multi-source | yes | yes | 10 services (Linear, Slack, Trello, Gmail, Sheets, Slides, Docs, Drive, Calendar, GitHub) | no source named as an exact artifact beyond the anchor |
| Async | no | — | — | — |
| Error recovery | no | — | Friction: none (03_Error_Async_Config.txt) | — |
| Access control | yes (minor) | no | Android's store post in #executives (C07C2866011/1759075866.111309) is not visible; the mail states the build | the prompt does not mention it |

## 9 · Must not appear in the prompt

- Tool / server names: gsheets_*, gdrive_*, linear_*, slack_*, gmail_*, trello_*, gcal_*, gslides_*, gdocs_*, github_*, any MCP server name.
- Ids: D05HB64NMQU, 68daca5871dba40417a00383, 68dbfa4362a051efb5e0ae45, f_0ba93ae0238d9ed4178212, f_048bf5e69f8e7f1a659a5c, f_9ec79682ff351aa466364a, d_96489e1e00a56685625939, evt_91674a9c23d012a9ac34da, any ZOM key, any PR number, any message id.
- Hidden authorities and their contents: the card's rules, the amendment, Blake's mail or reply, the build versions, the enrage sheet, the deck, Blake's #zombie-design correction, the invite's attendee list, the agenda's two tabs. (The ZM Difficulty folder and Monday's tuning invite may be named: Julia knows both — /prompt attempt 6adfee3ef9092601a61245bb_1 finding 4.)
- Findings: any ticket, count or status, the "tiers:" tag, the > 90 check, the replaced ticket, the share roles.
- Root causes: stripped tooling, the attack-power amendment, per-monster enrage, the ZOM-199 / build disagreement.
- Form: markdown, numbered steps, column lists, format rules.

## 10 · Entity traps

```
SHARED_LAST_NAMES (5)
  baker: ['Owen Baker <owen.baker@harmonygames.co> [persona owen_baker]', 'Thomas Baker <thomas.baker@harmonygames.co>']
  bennett: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Oscar Bennett <oscar.bennett@harmonygames.co>']
  brooks: ['Lauren Brooks <lauren@harmonygames.co>', 'Oliver Brooks <oliver.brooks@harmonygames.co> [persona oliver_brooks]']
  lawson: ['Julia Lawson <julia.lawson@harmonygames.co> [persona julia_lawson]', 'Peter Lawson <peter.lawson@harmonygames.co>']
  price: ['Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]', 'Nathan Price <nathan@harmonygames.co>']

LOOKALIKE_HANDLES_AND_ALIASES (15)
  - Gmail thread files of arthur.blake@harmonygames.co are named 'blake@harmonygames.co_*'
  - Gmail thread files of brian.foster@harmonygames.co are named 'brian@harmonygames.co_*'
  - Gmail thread files of julia.lawson@harmonygames.co are named 'jlawson@harmonygames.co_*'
  - Gmail thread files of leonard.hayes@harmonygames.co are named 'leonard@harmonygames.co_*'
  - Gmail thread files of vincent.parker@harmonygames.co are named 'vincent@harmonygames.co_*'
ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
  persona: leonard_hayes - Co-founder & Creative Director / Executive
  slack      id=EMPLOYEE_0038_SLACK_ID, name=Leonard Hayes, real_name=Leonard Hayes, email=leonard.hayes@harmonygames.co, is_bot=False, deleted=False, messages=143292, first_post=2023-03-15, last_post=2026-02-13   [join: exact_email]
ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
  persona: arthur_blake - Co-founder & CTO / Executive
  slack      id=EMPLOYEE_0025_SLACK_ID, name=Arthur Blake, real_name=Arthur Blake, email=arthur.blake@harmonygames.co, is_bot=False, deleted=False, messages=38591, first_post=2023-03-20, last_post=2026-02-12   [join: exact_email]
ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
  persona: robert - Co-Founder & Creative Director / Executive
  slack      id=EMPLOYEE_0016_SLACK_ID, name=Robert, real_name=Robert, email=robert@harmonygames.co, is_bot=False, deleted=False, messages=129939, first_post=2023-03-15, last_post=2026-02-13   [join: exact_email]
ENTITY email:brian.foster@harmonygames.co  name=Brian Foster  kind=person  emails=['brian.foster@harmonygames.co']
  persona: brian_foster - Game Engineer / Engineering
  slack      id=EMPLOYEE_0026_SLACK_ID, name=Brian Foster, real_name=Brian Foster, email=brian.foster@harmonygames.co, is_bot=False, deleted=False, messages=33142, first_post=2024-06-06, last_post=2026-02-12   [join: exact_email]
ENTITY email:julia.lawson@harmonygames.co  name=Julia Lawson  kind=person  emails=['julia.lawson@harmonygames.co']
  persona: julia_lawson - Product Manager / Product
  slack      id=EMPLOYEE_0005_SLACK_ID, name=Julia Lawson, real_name=Julia Lawson, email=julia.lawson@harmonygames.co, is_bot=False, deleted=False, messages=34047, first_post=2023-07-16, last_post=2026-02-12   [join: exact_email]
ENTITY email:vincent.parker@harmonygames.co  name=Vincent Parker  kind=person  emails=['vincent.parker@harmonygames.co']
  persona: vincent_parker - Game Systems Engineer / Engineering
  slack      id=EMPLOYEE_0012_SLACK_ID, name=Vincent Parker, real_name=Vincent Parker, email=vincent.parker@harmonygames.co, is_bot=False, deleted=False, messages=44802, first_post=2023-08-30, last_post=2025-11-23   [join: exact_email]
```

| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |
|---|---|---|---|
| Julia Lawson julia.lawson@harmonygames.co | Peter Lawson peter.lawson@harmonygames.co; "lawson40" level pack in C090N54TG79/1756751169.213249 | different person / not a person | julia.lawson@harmonygames.co |
| Arthur Blake arthur.blake@harmonygames.co ("Blake") | mailbox files `blake@…` | alias only | arthur.blake@harmonygames.co |
| Brian Foster brian.foster@harmonygames.co | mailbox files `brian@…` | alias only | brian.foster@harmonygames.co |
| Leonard Hayes leonard.hayes@harmonygames.co | mailbox files `leonard@…` | alias only | leonard.hayes@harmonygames.co |
| ZOM-199 (Zombie Match 3D) | ENG-199 twin (trap_catalog N01) | team prefix | ZOM-199 |
| match3d PR #243 / #244 | ZOM-243 / ZOM-244 issues | PR vs ticket number | harmonygames-Games/match3d#243 |
| ZM ROADMAP "Difficulty baseline (Julia)" card | Domino Delights "Difficulty baseline" card | board and game | 68daca5871dba40417a00383 vs 683dbef4e319167a802bd888 |

## 11 · Pre-submit checklist

- [ ] Julia's voice: plain, short, lowercase-ok; no spec sheet or markdown
- [ ] names the anchor in plain words (Leonard's difficulty baseline ask / his DM) and nothing else by exact title or id
- [ ] asks the assistant (not "I'll") to build the register, put it in the zm difficulty folder, share it with everyone on monday's tuning invite, update the tickets and reply
- [ ] says it's due before Monday's tuning session
- [ ] no ticket, rule, build, count, status or share role from §9
- [ ] no tool or server name; no numbered steps
- [ ] 20–4,000 words (aim 60–150)

## 12 · Blockers and routed defects

None blocking. Hardening round 1 (01a_Hardening_Report.md): the L1 thread reply D05HB64NMQU/1759262838.442871 and the L2 card checklist 68dc033bf7d24e86b8a9cc67 were added. The final state is now 29 rows, 14 comments, Brian as writer and the keys in the reply. Round 2 then added the ZOM-281 tag (L3) and the starting-tier question (L4): 30 rows (17 Live), and the reply also says when a new player gets the starting tier (after the first 10 games). The prompt is unchanged. Advisories carried from /injection (Audit-Report/0_injection_PASS.md): A2 slides columns, A3 DD card list, A4 — no change. Platform follow-ups from the dossier: Linear comments render via list comments; slide text renders. /prompt attempt 6adfee3ef9092601a61245bb_1 (FAIL 2): all five findings fixed (01_Scenario_Design.md §13 v6 table); ZOM-315 corrected to Editor only. /prompt attempt 2 (FAIL 2): rule 4 made record-based (closes ZOM-250/277 and every similar pair); hp texts match commit b511fcbcd5. /prompt attempt 3 (FAIL 2, every prompt dimension 5): Cross-Service Coherence only — the Mailman, Mayor2 and PartyGirl rows had values no match3d commit before the cut set (commits 6a4d8ba57e, 476a02949b); the rows are removed and MonsterBase 0.8/0.8 covers them. Card rule 4 says "another ticket's closing note" (injection advisory A6). Also: never grade per-monster values for Mailman, Mayor2 or PartyGirl. Rubric cautions from that review: never grade whether enrage damage stacks across blunders (Monster.cs applies the single-step damage value), and never grade "first 10 levels" vs "first 10 games" (the code counts attempts).

## 13 · Self-review

Walked `Evals/1_Prompt_Eval.md` Phases 1–3 against this brief (§1.1 persona, §1.5 competency/skill/complexity, §2.1 UGT, §2.2 feasibility/ACL, §2.3 truthfulness, §2.6 clarity, §2.7 contrived register, §3.2 coherence).

| Area | Counter-reading | Resolution (evidence) |
|---|---|---|
| UGT | the checklist's unchecked items could read as not yet decided, and the thread reply as optional | each checklist item states a rule change in Leonard's words ("rule 6 change: …", "rule 7 change: …", 68dc033bf7d24e86b8a9cc67) on the card he owns; the thread reply is the asker's own later instruction under his ask (D05HB64NMQU/1759262838.442871) and names the six tickets — one acceptance class |
| UGT | the reply could go to #zombie-design (Vincent) instead of the DM | the ask says "reply here" (D05HB64NMQU/1759261706.530914); Vincent is not the requester (C090N54TG79/1759248760.118527) — §4b W4 |
| UGT | any later ticket that touched a member (ZOM-277 on ZOM-250, ZOM-263 on ZOM-246, #401 on ZOM-282) could make it Replaced | card rule 4 makes only another ticket's closing note saying so count (68daca5871dba40417a00383); only ZOM-282's note (cmt_912bdd42ad5c8d51521f) says it replaces ZOM-254 — one Replaced row |
| UGT | a run may comment on ZOM-42, ZOM-275 or ZOM-282 where the code differs from the text | card rule 6 limits comments to tickets Blake's mail or reply calls wrong plus Replaced ones and says every other ticket stays as it is (68daca5871dba40417a00383); one comment set {ZOM-199, ZOM-254} |
| Clarity | "whether players actually have it" could mean merged to main | the card defines shipped by Blake's store builds mail (68daca5871dba40417a00383 rule 3; julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>) |
| Incorporation | the card's rule sources might not be incorporated | the ask names the card by board (D05HB64NMQU/1759261706.530914); the card names the mail, the sheet, the deck, ZOM-42, the agenda, the folder and the invite (68daca5871dba40417a00383); each is readable (check-sql YES) and states rules, not answers |
| Truthfulness | a premise like "Leonard asked yesterday" could be off | the ask is Tue Sep 30 19:48Z, the clock Wed Oct 1 00:00Z — the prompt should say "Leonard's ask" or "Tuesday", not a relative day (D05HB64NMQU/1759261706.530914) |
| Feasibility / ACL | Julia may need Android's #executives post | Blake's mail in her mailbox states Android 0.3.133 (julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>); writes: gsheets create/update, gdrive move/share, linear create comment, slack send exist in Evals/references/tools/catalog.json; Julia is writer on d_96489e1e00a56685625939 |
| Contrived register | listing the tabs or columns in the prompt reads as a spec sheet | the layout lives in the card and the agenda (68daca5871dba40417a00383; f_9ec79682ff351aa466364a); the prompt only points at the ask |
| Contrived register | hiding a destination and audience the persona knows reads as a riddle | the prompt names the ZM Difficulty folder (d_96489e1e00a56685625939, Julia's own sheet f_0ba93ae0238d9ed4178212 sits in it) and Monday's tuning invite (evt_91674a9c23d012a9ac34da, Julia an attendee); the share roles and attendee names stay in the card and the invite |

Unresolved: none.

```
STAGE GATE prompt-writing: PASS — Task_Authoring-2/task_inputs · 04_Prompt_Writing_Brief.md#382253dc20c2 · blocking 0 · warnings 0 · checks 21
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Writing_Brief.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql, 03_Error_Async_Config.txt, 01a_Hardening_Report.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#dd7536cdea3f, 01_Hardness_Manifest.json#741e6e29d5bc, 01_Grounding_Dossier.md#00dd277180d2)
[PASS] chain.error-async: upstream 'error-async' PASS pasted and current (03_Error_Async_Config.txt#5a647d2055f6)
[PASS] structure.sections: 14 required sections present and non-empty (04_Prompt_Writing_Brief.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Writing_Brief.md
[PASS] evidence.situation: 4/4 items carry a source pointer (min 100%)
[PASS] evidence.final_state: 40/40 items carry a source pointer (min 100%)
[PASS] evidence.discovery_map: 24/24 items carry a source pointer (min 100%)
[PASS] evidence.dates: 5/5 items carry a source pointer (min 100%)
[PASS] evidence.entity_traps: 7/7 items carry a source pointer (min 100%)
[PASS] tool.search_as_persona: 24 facts proven findable by persona_view search as julia_lawson
[PASS] reach.brief: 17 scoped load-bearing ids YES for julia_lawson
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] structure.canonical_outcome: canonical outcome table: 23 field(s), each fixed or delegated
[PASS] boundary.anchor_naming: 1 anchor-naming entry, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 10 evidenced counter-readings (of 10 found; need ≥ 6) in 04_Prompt_Writing_Brief.md
[PASS] review.coverage: self-review addresses all 6 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```




















