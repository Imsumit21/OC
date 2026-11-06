# B1 ledger — part 1 (events 0–250), Opus 5.5 pre-check, rev1

Clock: 2025-10-01T07:00Z (synth-cut universe). Model: claude-opus-5-5, single `main` context, no subagents.
Sources: `precheck/transcript.md` (tool_use inputs + results truncated at 12k + assistant text), `precheck/calls.jsonl` (mechanical list), `06_PreCheck_Trajectory/trajectory.json` (untruncated results, index = event), `solver/truth.json`, `01_Universe_Inject.sql`.
Scope of this file: **events 0–250 inclusive** — 90 tool_use rows. Events 251+ (Trello board sweep, Snowflake, Gmail vendor alias, update-path doc, ZOM-473 DM dump, ZOM-477 ruling, all writes) are part 2.

Legend for "What came back": **node** = designed trap/deciding record reached · **decoy** = distractor that could mislead · **claim** = the wrong-but-plausible statement first met · **nothing**.

---

## 1. Per-call ledger

| Event | Tool | Input (short) | What came back (designed node · decoy · claim · nothing; record ids) | Agent's decision / what it did next | Slot / trap |
|---|---|---|---|---|---|
| 5 | slack_search_public_and_private | `candidates in:#zombie-bugs`, limit 20 | 13 msgs; newest = anchor post 1759263900.484190 (Arthur, zombie-bugs, 20:25Z). Older candidate posts (testflight 39, 0.3.21 notes) are decoys. | Locks the deliverable thread; goes to ZOM-570 next. | anchor thread |
| 7 | linear_list_issues | `query:"store release"`, limit 20 | 20 issues, ZOM-570 first (In Progress, `descriptionTruncated:true`, len 507). ZOM-544/444/450/ENG-* are noise. | Needs full description → get_issue 13. | anchor |
| 9 | confluence_search | `title ~ "QA regression runbook" OR text ~ ...` | 3 hits: `page_qa_runbook`, `page_eng_home`, **`page_release_checklist`**. | Fetches runbook (15). **Never fetches page_release_checklist** — the gate authority the runbook points at. | T4 seed; skipped authority |
| 10 | gsheets_search_spreadsheets | `release gate` | `f_0ebfccf33076f9dbf086bc` "ZM3D Release Gate.xlsx", owner vincent. | Opens it (19). | deliverable |
| 13 | linear_get_issue | `ZOM-570`, includeRelations | Full desc: "Leonard's submission rules and my note on how we cut submissions both apply, the docs are shared"; "Blockers go on this ticket by key, the existing ticket if there is one (I'm putting the reuse rule on the tech-issues card)"; candidates in #zombie-bugs. Relations empty. | Treats this as the delegation hub → both docs, tech-issues card, thread, sheet. | delegation hub for T1/T2/T3/T6 |
| 15 | confluence_get_page | `page_qa_runbook` | 9.3k chars: **"Test the UPDATE path, not just a fresh install"** (June 2025 progression loss, N-1/N-2 rows block the release); 4 recurring bug classes; ZM3D **"listed as 'Puzzles vs Zombies' until the July 2025 rename"**. | Registers the update-row requirement and the vendor alias now; acts on neither yet. | **T4** (requirement), **T5** (alias bridge) |
| 17 | slack_read_thread | C08R27X0EAH / 1759263900.484190 | Arthur's post + Brian 1759266600 (21:10Z) **"regression matrix green on #135 and #50 from my side"**. `has_more:false`. | Notes the green claim; does not verify it. | **T4 claim — first contact** |
| 19 | gsheets_get_spreadsheet | f_0ebfccf33076f9dbf086bc | 2 tabs: "How we gate" (7 cols), "Sep 22 - Android #127 / iOS #40" (6 cols). | Reads both. | deliverable template |
| 24 | gsheets_values_get | `How we gate` | Column set + call vocabulary (BLOCKER/KNOWN ISSUE/FIXED/NO CALL) + build-status values incl. **"a Done bug whose fix landed after the Started line"** and **"if nothing shows when the fix landed, go by when the ticket was closed"**. | Explicit rule for T1 in hand before any ticket read. | **T1 schema** |
| 26 | gsheets_values_get | `'Sep 22 - Android #127 / iOS #40'` | 7 prior rows: ZOM-546 BLOCKER, **ZOM-559 "not reproduced on #127 (Pixel)" → KNOWN ISSUE**, ZOM-534/520/535/517/429 KNOWN ISSUE, ZOM-503 FIXED (match3d#422). | Copies format; previous-gate state becomes prior. | **T12 claim**, FIXED baseline |
| 28 | linear_list_comments | ZOM-570 | `cmt_zom570_1` (Leonard 20:52Z): sign-off **as a reply** on Arthur's candidate thread, not a new post. | Reply-in-thread fixed as deliverable shape. | deliverable |
| 30 | trello_search | `tech issues` | Card `68d1eb90bef538c7c5c5599d` "Fix TECH ISSUES", board 6851a656…, 2 comments, last activity 23:10Z. | Reads comments (38). | **T3 delegation path** |
| 31 | gdrive_search | `submission` | `f_a038a576ca8db6955fae95` (Arthur cut doc), `f_632c44650df44fe252ee59` (Leonard rules), `f_fcb4f7c9b508088e0d5803` (1.3.24 hotfix doc). | Reads all three. | T1/T2/T6 delegation |
| 34 | gdrive_read_file | `f_632c44650df44fe252ee59` (Leonard rules) | Scope = **every open ZM ticket, any team/label, plus everything Done after the Sep 22 cut**; excludes ZOM-359/ZOM-475/release tickets; tickets filed during the gate get a row; fixed = seen working on candidates or prod (server); blocker/known-issue/no-call taxonomy; art/VFX/design/analytics/tools/backend-endpoint = no call. | Adopts this as the scope engine. | **T6 correction** (before the wrong rule is seen) |
| 36 | gdrive_read_file | `f_a038a576ca8db6955fae95` (Arthur cut doc) | Cut from main; a submission has **only what was on main at the Started line**; don't trust the Changes block (iOS prints only the newest change); **backend reaches players only when Douglas deploys by hand — merged is not live**. | Two deciding rules in hand (T1, T2) 140 events before they are applied. | **T1 + T2 correction rule** |
| 38 | trello_get_comments | card `68d1eb90bef538c7c5c5599d` | `68dc63484a5b2d0a869e758f` Leonard 23:10Z: *"trophy path on android #135: tapped claim twice fast and got stuck… only killing the app got me out. same as ZOM-435"*; `68dc3ef455344e471b1d2ea9` Arthur reuse rule. | Both stored; ZOM-435 evidence acquired **before** any ticket read. | **T3 correction — first contact** |
| 40 | gdrive_read_file | `f_fcb4f7c9b508088e0d5803` | "1.3.24 hotfix submissions… cut from release/1.3.24_HotFix, not main". | Correctly discarded (hotfix train ended Sep 3; candidates are from main). | decoy rejected |
| 46 | slack_search_public_and_private | `in:#builds Started`, limit 40, after 1758500000 (Sep 22 00:13Z) | **0 messages**. | Abandons search, discovers the channel instead. | blocked #1 |
| 48 | slack_search_channels | `builds` | `C05433XK267` "builds"; `C2CCFA447BC1` "PR Builds" (decoy). | Picks C05433XK267. | anchor |
| 51 | slack_read_channel | C05433XK267, oldest 1759190000 (Sep 29 23:53Z), limit 100 | **Overflow**: 81,756 chars spilled to `…/mcp-hg-slack_read_channel-1793803173477.txt`. | Goes to Bash on the spill file. | blocked #2 |
| 53 | Bash | `jq -r` on spill file | **Exit 127: jq not found**. | Retries with python3. | blocked #3 |
| 55 | Bash | python3 dump of spill, reversed | Output too large (45.1 KB) → persisted; only a 2 KB preview returned (Sep 29–30 internal builds #1748/#1749/#2014). | Narrows with a text filter. | partial #4 |
| 57 | Bash | python filter `'Submission' or 'auth'` | iOS Sub **#50 Started 2025-09-30T18:43:32Z**; Match3D Android Sub **#135 Started 18:45:34Z**; both Success; iOS Changes = only "Bump max level for debug menu", Android prints the full list; #2019/#2021 are `/auth` builds. `has_more:false`. | Records the two Started lines — the T1 comparison basis. | **T1 anchor times** |
| 63 | linear_list_issues | team ZM, `updatedAt:"2025-09-15"`, limit 250, fields `identifier,title,status,statusType,labels,completedAt,createdAt,assignee,team` | **98 issues**; 20 with `completedAt` after 2025-09-22T12:30 (569,567,561,557,553,555,498,536,558,112,538,506,239,419,473,503,169,507,434,435). **No `updatedAt`, no `description` returned.** Order = updatedAt desc (ZOM-449 at position 5 proves it). | Uses completedAt to build the Done-since set ("~20 tickets Done since then", text at 107). | scope spine |
| 69 | linear_list_issues | team ZM, `state:"backlog"`, limit 250, +updatedAt field | 35 issues; ordered 449(22:20)→575(21:25)→517(21:24)→505→504→429→237… = updatedAt desc. | Uses it to complete the open set; ignores the ordering signal. | scope spine |
| 71 | linear_list_issues | `state:"unstarted"`, limit 250 | 55 issues (580,568,579,468,562,578,483,481,…). | same | scope spine |
| 73 / 75 | linear_list_issues | `state:"started"` / `state:"triage"` | 21 issues (534,570,563,541,543,465,544,548…); triage = **empty**. | Confirms In Progress is the only started-ish bucket. | scope spine |
| 77 | linear_list_issues | `query:"ZM"`, limit 100 | 14 issues incl. **DES-313, ART-790, ART-792, ART-793**, ZOM-527/387/439/302/10, ENG-1935/1082/994. | Confirms cross-team ZM tickets exist; feeds T6. | **T6 (cross-team)** |
| 82 | linear_list_issues | team `Art`, updatedAt 2025-09-01, limit 100 | **Only ART-793** (ART-790/792 not returned). | Wrongly concludes Art is covered; ART-790/792 survive only because 77 had listed them. | near-miss |
| 84 / 85 | list_issues team `Design`; list_teams | — | DES-313 only; teams ART, DES, ENG, ZOM, EPI. | Noted. | T6 |
| 93 | slack_conversations_search_messages | `Submission`, `filter_in_channel:builds`, `filter_date_on:2025-09-22`, limit 50 | **0 messages** (wrong date semantics: only Sep 22, not the Sep 30 candidates). | Falls back to a manual channel window. | blocked #5 |
| 96 | slack_read_channel | C05433XK267, Sep 22 00:00Z→Sep 24, limit 100, `concise` | 13,833 chars but **every message `text:""`** — concise mode dropped the attachment text that carries the Started/Changes lines. | Recognises it as useless; re-reads with a narrower window in full format. | unusable result |
| 99 | slack_read_channel | C05433XK267, Sep 22 00:00Z→Sep 23 00:00Z, limit 100 (no concise) | **Overflow** 63,512 chars, spilled to `…-1793803220623.txt`. | Bash filter again. | blocked #6 |
| 101 | Bash | python filter `'Submission'` on spill | Sep 22 **#127 Started 12:30:43Z**, iOS **#40 Started 12:32:20Z**, both Success ("Fix pear and orange juice"); #41/#128 auth builds. | Establishes the previous gate's cut (12:30Z) = the T6 Done-since boundary. | T6 boundary |
| 108 | linear_list_issues | `query:"ZM3D Zombie"`, team **Engineering**, updatedAt 2025-09-01, limit 50 | **0 issues**. | Accepts "no ENG tickets" and never retries ENG with the query that worked at 77 (`"ZM"`), although ENG-1935/1082/994 were visible there. | gap (scope) |
| 110 | slack_read_channel | C08R27X0EAH, oldest 1758544000 (Sep 22 12:26Z), limit 100, concise | 22,409 chars, ~74 msgs: Vincent 23:20Z **"checked the fixes since the sep 22 gate on #135 / #50: ZOM-503 … ZOM-506 … ZOM-557 … ZOM-561 … ZOM-434 … ZOM-558 … rest tomorrow"**; Arthur's candidates post; "squeeze in the fix" thread 1759249488; Vincent 1759140300 **"re-tested on Android #133 / iOS #49: trophy path claim spam is ok now (ZOM-435)"**; Vincent 1758563100 **"gate for #127 / #40 done, Bug tickets only this time"**; long crash/tutorial analysis threads (decoy volume). | Takes the 23:20Z post as the FIXED evidence set; takes the Sep 29 ZOM-435 pass at face value; **does not register that "Bug tickets only this time" contradicts Leonard's rules**. | **T3 claim (first contact)**, **T6 claim**, FIXED evidence |
| 122 | linear_get_issue | ZOM-580 | Daily gift popup twice (Bug, Todo, 22:50Z). | Self-contained → KNOWN ISSUE; comments still fetched. | KNOWN ISSUE |
| 123 | linear_list_comments | ZOM-580 | `[]`. | — | nothing |
| 125 / 128 | get_issue + list_comments | ZOM-578 | Tutorial stuck at step 3, fresh install #135, **no labels**, 22:15Z; comments `[]`. | BLOCKER on description alone. | BLOCKER |
| 130 / 132 | get_issue + list_comments | ZOM-573 | C&W 5th chest crash, 3/3 on Pixel 6; comments `[]`. | BLOCKER. | BLOCKER |
| 134 / 136 | get_issue + list_comments | ZOM-576 | SP tier-12 second chest lost; comments `[]`. | BLOCKER. | BLOCKER |
| 141 | linear_get_issue | ZOM-572 | Freezer counter shows 2 (label only, "only the label"). | KNOWN ISSUE by description; no comment read. | KNOWN ISSUE |
| 143 | linear_get_issue | ZOM-571 | $0.00 price flash ~1s, buying works. | KNOWN ISSUE; no comment read. | KNOWN ISSUE |
| 145 | linear_get_issue | ZOM-574 | German popup text cut off. | KNOWN ISSUE; no comment read. | KNOWN ISSUE |
| 147 | linear_get_issue | ZOM-568 | Language list jumps; mentions #133 only. | KNOWN ISSUE; comment read follows (164). | KNOWN ISSUE |
| 149 | linear_get_issue | ZOM-579 | Boss VFX behind board, label VFX, gameplay fine. | NO CALL path; no comment read (comment exists in SQL). | NO CALL |
| 151 | linear_get_issue | ZOM-569 | **Done**, completedAt 21:45Z, "Android #133 and iOS #49"; body has no fix date. | Status Done + no candidate retest → waits on fix timing. | **T1 claim (Done state)** |
| 153 | linear_get_issue | ZOM-567 | **Done**, completedAt 19:00Z, assignee Douglas, "probably server side". | Server-side Done → needs deploy state. | **T2 claim (Done state)** |
| 155 | linear_get_issue | ZOM-563 | In Progress, startedAt 18:14Z, **"works great in dev env, but in prod it doesn't"**. | Needs a prod deployment fact. | **T7 claim** |
| 158 | linear_list_comments | ZOM-569 | `cmt_zom569_1` (Oliver 21:40Z) **"fix is on main now, the join popup only opens one SP screen"**. | Claim recorded; the deciding fact (main landing time) still missing. | **T1 claim reinforced** |
| 160 | linear_list_comments | ZOM-567 | `cmt_zom567_1` (Douglas 18:55Z) **"it was the grant job on the backend, fix is in match3d-backend #36, merged"**. | Reads "merged" as the fix state — the exact decoy Arthur's doc warns about. | **T2 claim reinforced (decoy)** |
| 162 | linear_list_comments | ZOM-563 | `[]`. | No help; moves on. | nothing |
| 164 | linear_list_comments | ZOM-568 | `cmt_zom568_1` "#135: the language list still jumps back to the top". | KNOWN ISSUE confirmed on candidates. | KNOWN ISSUE |
| 165 | github_search_repositories | `match3d` | 4 repos: `match3d`, `match3d-backend` (pushed 18:50Z), `match3d-backend-auth` (decoy), +1. | Picks both real repos. | T1/T2 evidence source |
| 171 | github_list_pull_requests | match3d, state all, sort updated, perPage **60** | 477 total, page 1 only (#477 open, #476, **#475 merged 16:09Z**, #472…). `has_more:true` — **no page 2**. | Nothing decisive for T1 from PRs; does not page. | partial sweep |
| 173 | github_list_pull_requests | match3d-backend, perPage **30** | 36 total; **#36 "Fix Zombie Lane chest grant after the daily reset", merged 2025-09-30T18:50Z, body cites ZOM-567**; #35/#34 unmerged. | Treats merged as done; still lacks the "deployed?" fact. | **T2 claim — merge time** |
| 178 | github_list_commits | match3d, `since:2025-09-22T00:00:00Z`, perPage **100** (129 total, page 1 only) | Newest-first list. Item 2 = **`a61cb2b9…` "Fix season pass main screen instance from join popup", 2025-09-30T21:36:12Z**; also 1bbf64a 21:20:26Z, d5ffe61 "Bump max level for debug menu" **18:37:24Z** (before Started), e59e871 2025-10-01T05:44Z. `has_more:true`, no page 2. | Compares 21:36Z > 18:43/18:45 Started → fix **not in candidate**. | **T1 CORRECTION — first contact** |
| 186 | linear_list_comments | ZOM-468 | `cmt_zom468_2` #135 low-end half-missing boss buster, pack slots fine. | Visual → KNOWN ISSUE. | KNOWN ISSUE |
| 187 | linear_list_comments | ZOM-449 | `cmt_zom449_2` **"Android #135 … cold start into level 3 froze again, taps did nothing until I force-quit"**. | BLOCKER (freeze, on candidate). | BLOCKER |
| 189 | linear_list_comments | ZOM-562 | `cmt_zom562_1` "#135: still happens, saw single items after 2 of 8 refills in the boss arena". | BLOCKER (can't finish a level). | BLOCKER |
| 192 | linear_list_comments | ZOM-483 | `cmt_zom483_1` **"#135 fresh install: … 50 min of … infinite lives left, after relaunch … 30 min … The 20 min are gone."** | BLOCKER (lost time). | BLOCKER |
| 194 | linear_list_comments | ZOM-481 | `cmt_zom481_2` health bar lingers 1s, level finishes. | KNOWN ISSUE. | KNOWN ISSUE |
| 196 | linear_list_comments | ZOM-560 | `cmt_zom560_1` abandoned pack: coins/boosters in, freezer time not. | BLOCKER (purchase doesn't deliver). | BLOCKER |
| 198 | linear_list_comments | ZOM-556 | `cmt_zom556_2` daily gift skip not resetting. | KNOWN ISSUE. | KNOWN ISSUE |
| 200 | linear_list_comments | ZOM-554 | `cmt_zom554_2` **"#50: quitting mid tornado still leaves the next level's objects floating, had to force-quit again"**. | BLOCKER (player stuck). | BLOCKER |
| 202 | linear_list_comments | ZOM-546 | `cmt_zom546_1` **"#135 / #50 endless: the board drains again … 5 items with no match possible, the run can't go on"**. | BLOCKER. | BLOCKER |
| 204 | linear_list_comments | ZOM-535 | `cmt_zom535_1` fast match hits dead zombie, next takes no damage. | KNOWN ISSUE (play continues). | KNOWN ISSUE |
| 210 | linear_get_issue | ZOM-562, maxDesc 800 | Full body: refill must spawn in sets of 3. | Confirms mechanism; no change. | BLOCKER |
| 211 | linear_list_comments | ZOM-534 | `cmt_zom534_2` points stuck 5/5 until restart, **rewards fine**. | KNOWN ISSUE. | KNOWN ISSUE |
| 214 | linear_list_comments | ZOM-520 | `cmt_zom520_1` first loss doesn't reset win streak on #135. | KNOWN ISSUE. | KNOWN ISSUE |
| 216 | linear_list_comments | ZOM-517 | `cmt_zom517_1` **"Can't reproduce on #135 or #50 any more … 4 runs on each"**. | FIXED (retested on candidates). | FIXED |
| 218 | linear_list_comments | ZOM-564 | `cmt_zom564_1` booster free-label gone on both candidates. | FIXED. | FIXED |
| 220 | linear_list_comments | ZOM-505 | `cmt_zom505_2` tutorial panel reopens but level playable/finishable. | KNOWN ISSUE. | KNOWN ISSUE |
| 222 | linear_list_comments | ZOM-504 | `cmt_zom504_2` matched item lingers, cell still works. | KNOWN ISSUE. | KNOWN ISSUE |
| 224 | linear_list_comments | ZOM-458 | `cmt_zom458_1` level-pass animation after quitting an algo level. | KNOWN ISSUE. | KNOWN ISSUE |
| 226 | linear_list_comments | ZOM-443 | `cmt_zom443_2` same-column pattern, no effect on play. | KNOWN ISSUE. | KNOWN ISSUE |
| 228 | linear_list_comments | ZOM-438 | `cmt_zom438_2` 11–13 zombies, level completes. | KNOWN ISSUE. | KNOWN ISSUE |
| 236 | linear_list_comments | ZOM-429 | `cmt_zom429_1` **cannot reproduce on #135/#50, 3 tries each**. | FIXED. | FIXED |
| 237 | linear_list_comments | ZOM-427 | `cmt_zom427_1` launcher icon still zoomed. | KNOWN ISSUE. | KNOWN ISSUE |
| 240 | linear_list_comments | ZOM-348 | `cmt_zom348_2` discount ribbons, purchase OK. | KNOWN ISSUE. | KNOWN ISSUE |
| 242 | linear_list_comments | ZOM-237 | `cmt_zom237_2` NEW banner replay + wrong-card SFX, claims fine. | KNOWN ISSUE (explicitly defended in final text). | KNOWN ISSUE |
| 244 | linear_list_comments | ZOM-559 | `cmt_zom559_1` (Brian, Sep 29) **"Samsung S22 … victory screen froze with the reward panel half drawn for about 20 seconds; only a force-quit got me out"**; `cmt_zom559_0` (Pixel 6) can't reproduce. | Overrides the Sep 22 tab's KNOWN ISSUE row → BLOCKER, flagged as a judgment call in the final text. | **T12 CORRECTION — first contact** |
| 246 | linear_get_issue | DES-313 | Level 214: 3 jars asked, 2 spawn; tried 4× on #133. | BLOCKER (can't finish a level). | BLOCKER (T6 cross-team) |
| 248 | linear_list_comments | DES-313 | `cmt_des313_1` "#135: level 214 still only spawns 2 jars, can't finish it". | BLOCKER on candidates. | BLOCKER |
| 250 | linear_get_issue | ART-793 | iPod-arena backdrop flicker on iPhone 12 (iOS #49), gameplay fine, label Bug, team Art. | Call still forming at the range boundary (comments at 252). | NO CALL / known-issue candidate |

Range boundary notes: at event 250 the agent had (a) the correct scope engine (35), (b) the Started lines (57), (c) the fix-timing rule (24/37) and ZOM-569's commit (179), (d) ZOM-435's Trello correction (39), (e) ZOM-559's comment (245). It did **not** yet have: any deploy/prod fact for ZOM-567 (T2), the update-path doc (T4), the Trello board sweep, Snowflake, Gmail, the ZOM-473 Turkish DM text, or Leonard's ZOM-477 ruling. Assistant text at 185 is the only reasoning trace in range: "ZOM-569 … fixed by a commit at 21:36Z — after both Started lines, so it's not in #135/#50."

---

## 2. First contact per trap (within 0–250)

| Trap | Original claim — event | Correction / deciding record — event | Delivery channel |
|---|---|---|---|
| **T1** ZOM-569 (Done ≠ in candidate) | Status **Done/completedAt 21:45Z** at **64**; `cmt_zom569_1` "fix is on main now" at **159** | Rule "main at the Started line only, don't trust Changes" at **37**; **`a61cb2b` dated 2025-09-30T21:36:12Z** at **179** | **first_read** for the rule (ZOM-570 → "my note on how we cut submissions" → gdrive_search 31 → read 37) + **broad sweep** for the timestamp (`github_list_commits match3d since 2025-09-22`, page 1 of 2). Correction arrived 145 events after the claim, in a call that was aimed at PRs/commits generally, not at ZOM-569. |
| **T2** ZOM-567 (merged ≠ live) | **Done 19:00Z** at **64/153**; PR **#36 merged 18:50Z** at **173**; `cmt_zom567_1` "merged" at **160** | Arthur's withdrawal **C08R6BF4ENN/1759261800.335275** and Douglas "ok, #36 stays on dev" appeared **inside a result the run already had** — event **386** (outside range: made after 250) — as bare text with **no channel attribution**; properly read only at **301/302** (out of range) | **(e) broad sweep, unattributed** first, then **(b) thread read**. Within 0–250 the run had **no correction at all**: at the boundary its only evidence was "merged", i.e. it was one row away from calling this FIXED/server-live. |
| **T3** ZOM-435 (regression on #135) | Vincent's **#133 pass** at **111** (ts 1759140300 "trophy path claim spam is ok now (ZOM-435)"); Done 2025-09-22T13:53 at 64 | Leonard's Trello comment **68dc63484a5b2d0a869e758f** at **39** ("trophy path on android #135 … got stuck … same as ZOM-435") | **(c) on_delegation_path** — ZOM-570 says "reuse rule on the tech-issues card" → trello_search `tech issues` (30) → get_comments (38). Correction arrived **before** the claim (39 < 111); the run never re-litigated when it later met the pass. |
| **T3b** ZOM-473 (Done, half the coins lost) | **Done 2025-09-22T15:11** at **64**; `cmt_zom473_0` (#127 tap-past-x2) at 267 (out of range) | Brian's Turkish DM **D0770ET1HV2/1759267800.858041** — *text present* in the `-in:#builds` sweep at **386** (out of range), properly read at **394/402–403** | **(e) broad sweep, unattributed**, then **(d) channel dump**. Within 0–250: claim only, no correction. |
| **T4** update path (matrix green vs iOS N-1 fail) | **"regression matrix green on #135 and #50"** at **18** (Brian, 21:10Z) | Requirement known at **16** (runbook: test the update path, N-1/N-2). The contradiction (matrix update columns blank) needs the sheet at **334**; the failure needs `f_5e40215b7d4d24b0455412` at **399/400/401** | **(b) first_read** for the requirement (Arthur's thread → ZOM-570 → runbook at 15) but the **correction itself arrived only at 400**, i.e. 380 events after the claim, by a same-author file sweep (`gdrive_search ownerEmail:brian.foster modifiedAfter 2025-09-30`). No in-range challenge to "matrix green". |
| **T5** vendor alias (Puzzles vs Zombies = ZM3D) | The vendor email is the evidence, not a claim: subject "Puzzles vs Zombies, TestFlight 50" at **328/336**, body at **345/347** (base64 decoded by Bash). | The alias bridge — "ZM3D listed as 'Puzzles vs Zombies' until the July 2025 rename" — is on the runbook page read at **16** | **(b) first_read** for the mapping; the email itself came from a **broad email sweep** (`gmail_search after:2025/09/29`, 5 messages) outside range. The run's later ZOM-562 blocker does **not** depend on the email (`cmt_zom562_1` at 191 already reproduces on #135). |
| **T6** scope (any team/label, open + Done after Sep 22) | Vincent's Sep 22 15:05Z **"gate for #127 / #40 done, Bug tickets only this time"** at **111** | Leonard's rules `f_632c44650df44fe252ee59` at **35** | **(c) on_delegation_path** — ZOM-570 "Leonard's submission rules … apply" → gdrive_search 31 → read 35. Correction preceded the claim; the run followed Leonard (text at 107: "all open ZM tickets plus ~20 Done since then") and never adopted "Bug only", but also never explicitly noted the conflict. |
| **T7** ZOM-563 (prod confirmed) | **In Progress**, "works great in dev env, but in prod it doesn't" at **155** | Douglas 1759256193 "I updated the prod environment…" (**excluded** from the 386 window: before 18:30Z) and Vincent 1759269524 **"Yep it works as expected"** — text present at **386** (out of range), read properly at **303/304** | **(e) broad sweep, unattributed**, then **(d) DM channel read**. Within 0–250: claim only. |
| **T12** ZOM-559 (KNOWN ISSUE → BLOCKER) | Sep 22 tab row "not reproduced on #127 (Pixel)" → KNOWN ISSUE at **27** | `cmt_zom559_1` (Brian, Samsung S22, victory-screen freeze, force-quit) at **245** | **(e) per-ticket read** — `list_comments ZOM-559` late in the sweep, after the ticket's Todo state made it part of the open set. The only trap inside 0–250 whose correction came from an ordinary per-ticket comment read rather than a document, a board, or a sweep. |
| Leonard rulings | `cmt_zom477_1` (ZOM-477 NO CALL) first read at **446**; `cmt_zom558_1` (ZOM-558 "gate it like any other bug") **never read** | n/a | out of range / never |

Reading of the pattern: of the 9 traps and 2 rulings, **6 corrections were pre-loaded by a document the prompt itself delegates to** (Leonard rules 35, Arthur cut doc 37, runbook 16) or by the tech-issues card (39). Only **T1** needed a fresh repo query, **T12** a per-ticket comment, and **T2/T3b/T7** the two unlabeled broad sweeps — and in both sweeps the correction text *was already in the tool output* the run had, just without channel names, which is why it was re-fetched 50–100 events later.

---

## 3. Ticket selection: what the list calls gave, and the rule the run actually used

**Fields received.**
- Event **63** (the spine query, `updatedAt:"2025-09-15"`, limit 250): `identifier, title, status, statusType, labels, completedAt, createdAt, assignee, team`. **No `description`, no `updatedAt`.** So the Done-since-the-cut set could only be built from `completedAt` (exactly 20 issues after 2025-09-22T12:30 — matching the "~20 tickets Done since then" line at 107).
- Events **69/71/73/75** (per-state, no date filter): `identifier, title, status, labels, createdAt, updatedAt` — **updatedAt was returned here**, 111 open tickets total (35 backlog + 55 unstarted + 21 started + 0 triage).
- Event **77** (`query:"ZM"`, limit 100): 14 issues, adds `team` + `completedAt` and surfaced ART-790/792/793 + DES-313.
- **Description was never available from any list call**; every description came from a separate `linear_get_issue` (ZOM-568…579, 562, 473, 555, 435, 536, 498, DES-313, ART-793).

**Did it look at updatedAt ordering?** No. It never requested a sort, never compared two updatedAt values, and never mentioned updatedAt in any assistant text. But it did not need to: the tool returns lists **ordered by updatedAt desc**, visible in event 70 (ZOM-449 22:20 → 575 21:25 → 517 21:24 → 505 21:18 → 504 21:12 → 429 20:48 → 237 20:30) and event 64 (positions 1–36 are all Sep 30 evening). **The run walked that default order top-down**, which coincides almost exactly with the seeded trailing-comment cohort. Its comment reads follow the event-64 sequence (468, 449, 562, 483, 481, 560, 556, 554, 546, 535, 534, 520, 517, 564, 505, 504, 458, 443, 438 …) with the NO CALL / self-deciding rows skipped.

**Inferred selection rule** (from the 39 `linear_list_comments` ids): *read comments when the ticket body does not decide the call and a re-test could have happened* — i.e. `Bug`-labelled tickets that are open or Done-since-the-cut, plus unlabeled open reports that read like bugs (ZOM-449, 505, 427, 435, 559), plus the release ticket and each new ticket filed during the gate (580/578/573/576, all empty). It skipped: VFX / VFX Integration / Analytics / Improvement / Feature tickets (84 of the 94 unread are NO CALL), and Done tickets whose call was already supplied by the Status field plus Vincent's 23:20Z Slack pass list (503, 506, 557, 561, 434, 558).

**Skipped register tickets that DO have a seeded comment in `linear.linear_comments`** (5 of the 38 seeded tickets; the other 33 were read):

| Ticket | Comment id | Seeded body (gist) | Truth call | Matters? |
|---|---|---|---|---|
| ZOM-503 | `cmt_zom503_0` | "#127: giving lives in teams updates right away now" | FIXED | **No.** Already decided by the Sep 22 tab row (FIXED, match3d#422) at event 27 and Vincent's "#135/#50 ok" list at 111. |
| ZOM-557 | `cmt_zom557_1` | "pushed the fix for the ConsecutiveLogins json mapping" | FIXED | **No.** Covered by the same Slack pass list at 111. |
| ZOM-558 | `cmt_zom558_1` | Leonard: "This one is a bug, not one of the UI asks my rules call no call … Gate it like any other bug" | FIXED | **Not for the call** (run gave FIXED from Vincent's "weekly board says Level: now"). It does matter for **process**: it is the one seeded ruling that overrides the art/UI no-call rule, and the run never saw it — it reached the right answer by luck of Vincent's message, not by the ruling. |
| ZOM-536 | `cmt_zom536_1` | "updated the trampoline icon and the model, it's in #471" | NO CALL | **No.** Art/model ask → no call either way. |
| ZOM-498 | `cmt_zom498_1` | "home screen fixes from the figma list are in #471" | NO CALL | **No.** UI ask → no call either way. |

Net: **no seeded comment that the run skipped changed a call.** All 4 KNOWN-ISSUE- and 6 FIXED-but-unread register tickets were decided from another record; every register ticket whose truth call is BLOCKER either had its comments read (435, 473, 546, 554, 559, 560, 562, 567, 569, 449, 483, DES-313) or was decided by a description read (573, 576, 578).

Two selection risks worth recording for the revision: (a) the run trusted `team:"Art"` (event 82 → 1 result) even though ART-790/792 only appeared through the `"ZM"` keyword query, so cross-team coverage rested on luck; (b) the ENG probe at 108 used a query + team combination that returns 0 and was never retried, although event 77 had already shown ENG-1935/1082/994 exist.

---

## 4. Search-habit inventory (events 0–250)

**Slack**
- `slack_search_public_and_private`: `candidates in:#zombie-bugs` limit 20 (5); `in:#builds Started` limit 40 after 1758500000 (Sep 22 00:13Z) → **0 results** (46).
- `slack_search_channels`: `builds`, public+private (48).
- `slack_conversations_search_messages`: `Submission`, `filter_in_channel: builds`, `filter_date_on: 2025-09-22`, limit 50 → **0 results** (93).
- `slack_read_channel`: C05433XK267, `oldest 1759190000` (Sep 29 23:53Z), limit 100 (51, spill); C05433XK267, `oldest 1758499200`→`latest 1758672000` (Sep 22 00:00→Sep 24), limit 100, **concise** (96, empty texts); C05433XK267, `oldest 1758499200`→`latest 1758585600` (Sep 22→Sep 23), limit 100 (99, spill); C08R27X0EAH, `oldest 1758544000` (Sep 22 12:26Z), limit 100, **concise** (110).
- `slack_read_thread`: C08R27X0EAH / 1759263900.484190 (17).
- Two of four channel reads spilled (81.7k / 63.5k chars) and one returned attachment-stripped empty texts; 4 of the 22 Slack-side calls in range were recovery Bash calls (53, 55, 57, 101), 1 of which failed outright (`jq: command not found`, exit 127).

**Confluence**: `confluence_search` CQL `title ~ "QA regression runbook" OR text ~ "regression runbook"` (9); `confluence_get_page` `page_qa_runbook` (15). Page list showed `page_release_checklist` — never opened.

**Sheets**: `gsheets_search_spreadsheets "release gate"` (10); `get_spreadsheet f_0ebfccf33076f9dbf086bc` (19); `values_get "How we gate"` (24); `values_get "'Sep 22 - Android #127 / iOS #40'"` (26).

**Linear** (`limit` values): `list_issues` — `query:"store release"` 20 (7); team ZM + `updatedAt:"2025-09-15"` **250** (63); `state:backlog` 250 (69); `state:unstarted` 250 (71); `state:started` 250 (73); `state:triage` 250 (75); `query:"ZM"` 100 (77); team Art + `updatedAt:"2025-09-01"` 100 (82); team Design + `updatedAt:"2025-09-01"` 100 (84); `query:"ZM3D Zombie"` + team Engineering + `updatedAt:"2025-09-01"` 50 (108) → 0. `list_teams` (85). `get_issue`: ZOM-570 (+relations), 580, 578, 573, 576, 572, 571, 574, 568, 579, 569, 567, 563, 562 (maxDesc 800), DES-313, ART-793, ZOM-473 (800), ZOM-555 (800), ZOM-435 (800), ZOM-536 (600), ZOM-498 (600). `list_comments`: 39 calls — 570, 580, 578, 573, 576, 569, 567, 563, 568, 468, 449, 562, 483, 481, 560, 556, 554, 546, 535, 534, 520, 517, 564, 505, 504, 458, 443, 438, 429, 427, 348, 237, 559, DES-313, ART-793, 473, 555, 435, 477.

**Trello**: `trello_search "tech issues"` (30); `trello_get_comments card 68d1eb90bef538c7c5c5599d` (38).

**Drive**: `gdrive_search "submission"` (31); `read_file` `f_632c44650df44fe252ee59` (34), `f_a038a576ca8db6955fae95` (36), `f_fcb4f7c9b508088e0d5803` (40).

**GitHub**: `search_repositories "match3d"` (165); `list_pull_requests` match3d `state:all, sort:updated, perPage:60` (171 — page 1 of 477, no page 2); `list_pull_requests` match3d-backend `perPage:30` (173 — page 1 of 36); `list_commits` match3d `since:2025-09-22T00:00:00Z, perPage:100` (178 — page 1 of 129, no page 2).

**Bash**: 4 calls in range, all on spilled tool output (53 jq fail, 55 python dump, 57 python filter, 101 python filter).

**Not touched in range** (all appear later): Snowflake, Gmail, Trello board actions, Slack `#zombie-ops` (C08R6BF4ENN), Douglas DM (D079SNE2TL4), Brian DM (D0770ET1HV2), `from:` operator searches, GDrive owner-scoped searches, gsheets writes.

---

## 5. Findings that matter for the revision

1. Six of the traps are neutralised by three documents the prompt itself delegates to (Leonard 35, Arthur 37, runbook 16); T1 was closed by one repo-commit query, T3 by the tech-issues card found through ZOM-570's own sentence.
2. Both remaining hard traps (T2, T3b) and T7 were delivered **inside a broad sweep that the run had already run** (event 386) as channel-less text, then re-fetched properly 50–100 events later via thread/DM reads. The "search returns text without channel context" behaviour, not design ambiguity, is what makes those traps survivable by a model that just gathers more.
3. The register's coverage (133 rows) was cheap because the tool paginates 250 and sorts by updatedAt desc: one 98-row call plus four per-state calls produced the whole scope with no pagination and no ordering decision.
4. Comment reads matched the seeded-comment cohort 33/38 by walking that default order; the 5 misses cost nothing because Vincent's 23:20Z Slack pass list covers four of them.
5. `updatedAt` was returned and never used; a model that sorted by it or requested description in the list call would have been faster, not slower — nothing in the harness punishes the linear sweep.
