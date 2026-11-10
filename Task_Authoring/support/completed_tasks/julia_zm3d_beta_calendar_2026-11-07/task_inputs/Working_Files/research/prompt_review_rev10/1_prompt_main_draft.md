## PROMPT EVALUATION REPORT (DRAFT, before Deep Recheck and Eval 0 merge)

### Task: Julia Lawson builds the ZM3D beta live-ops and push calendar for four buy weeks and sends Frederick a run/hold recommendation
### Assigned Persona: Julia Lawson - Product Manager (julia_lawson, julia.lawson@harmonygames.co, Product)
### Assigned Business Function: Product
### Assigned Competency: Marketing and GTM
### Assigned Task Skill: Planning and decision support
### Assigned Horizon: Long Horizon (task type long-horizon; difficulty mode medium)

Scope: chat review from R/inputs, actual review date 2026-11-06, `Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)`. Prompt sha256 in the record. SQL sha256 ffbac4586fb91842ca16263c2b76987c26623c7ed689e00d33886c63f9331bdc (read, never executed). Eval version task-quality-v1, release sha256 c5b89f4c40a7902f968001f1aa6c710d47bf203842455bbe8dbb668ec7c8943b. No reference files, error/async config or dynamic context. `authority_contract: prompt-incorporation-v1`; `evidence_contract: stage-evidence-v1`, nothing reused.

Rule sources: the prompt, Frederick's DM and thread reply, his brief. Every other record is a fact source.

TODO status: Intake DONE (R/inputs). 0.5 Injection gate: pending the separate Eval 0. 0.1 Docs: scoring.json, Eval 1 overrides, roster, ACL and catalog read; PDFs not extractable here (no pypdf or pdftotext), recorded as a limit. 0.2 Universe exploration DONE. 0.3 Example Task not read (same limit). 1.1 to 1.5, 2.1 to 2.8, 3.1, 3.2, 4.1, 4.2 DONE. 2.9 N/A. Phase 5 pending (P1 to P4 run separately).

---

### Injection Gate
- State: separate Eval 0 reviewer is running on this hash; report not yet received.
- Reviewed SQL sha256: ffbac4586fb91842ca16263c2b76987c26623c7ed689e00d33886c63f9331bdc. Eval 0 verdict: pending.
- Task-required records checked directly here: author membership for all added Slack messages (Frederick and Julia in D05SD5QLG94; Robert and Julia in D05GU6L0XFH; Vincent in C0880U9751A and C08R27X0EAH; Leonard in C08R27X0EAH; Robert in C08R8CHB0QL; bot in C093LEZGF6J), doubled apostrophes, weekday arithmetic, Gmail date headers against internal_date, Trello action id timestamp, Drive parents. All hold.

---

### Phase 1: Prompt Structure & Persona

**Persona:** PASS. Confluence `page_liveops_calendar`: "Design, led by Julia Lawson, walks the coming weeks with Frederick Stone: which recurring slots fire and whether a one-off drops on top." Spec: "Design partner: Julia Lawson." Voice fits a PM delegating. Identity matches the roster exactly.

**Assigned Competency:** PASS. A live-ops and push plan tied to UA buy weeks, UK and US creative and a go-to-market pivot call is GTM work.

**Assigned Task Skill:** PASS. "I need your call, not a list of what we have" makes planning and decision support the spine.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. PASS.
- Dynamic Change: Douglas Sep 16 "not blocking" then Vincent Sep 30 retest; Robert Sep 18 approval then Sep 30 pull; Brian Oct 29 then Oct 31.
- Multi-Source: Slack, GDocs, GSlides, GSheets, Confluence, GitHub, GCal, Gmail, Linear, Trello.
- Data seeding: PASS. 100 words; every rule lives in the DM, thread reply or brief.

**Naturalness:** PASS. First person, plain, no formatting, no connective polish, no staged errors.

| Pattern | Status |
|---|---|
| Command List | PASS ("Once the sheet's done, link it..." is a natural dependency, not a step list) |
| Bolt-On | PASS (each sentence serves the calendar: remove the ticket note and the owner hand-off is lost) |
| Pre-Solving | PASS (no beat, cause or date is given) |
| Tool Mention | PASS (hits for `linear_`, `gmail_`, `slack_`, `MCP`, `tool`, `First`, `Then`, `Finally`: none) |

Diversity: five distinct writes across four services, far beyond one Slack post.

---

### Requirement ledger

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Calendar in sheet | Prompt, DM, brief, deck, Confluence, GitHub, GCal, Linear | DM to brief to records | `gsheets_values_update` / `gsheets_values_append` | Sheet owned by Julia | Calendar tab, seven beats |
| Pushes, one line per row | Thread reply, `PNs Beta` | Sheet shared with Julia | same | Julia in `shared_with_emails` | Pushes tab, ten rows |
| Note on a held beat's ticket | Prompt, brief, ZOM-429 | Vincent post to ticket | `linear_create_comment` | Linear unscoped | Comment on ZOM-429 for Douglas |
| Link on calendar ticket | Prompt, DM, cmt_zom78_1 | Linear search | `linear_create_comment` | Unscoped | Link on ZOM-78 |
| Recommendation | Prompt, DM | DM | `slack_send_message` | Julia in DM | Run/hold call with trade-offs |
| Reply on lock miss | Brief "Config locks", Sep 26 mail, spec | Brief to mailbox and Confluence | `gmail_reply_to_message` | Julia mailbox copy | Reply to Brian: lands before Oct 31 00:00 UTC |

The Brian reply is incorporated: the prompt points to the brief, and the brief states the write. Brian's own "If the new date is a problem on your side, reply on this mail." names the thread.

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** FAIL (2)

### Unique Ground Truth comparison

Unique Ground Truth: FAIL 2

Basis: Reading B is not ruled out by any prompt sentence, rule source or third-party record: the Collect &amp; Win event icon animation rests only on its owner note, so the Still to do cell has two defensible contents.

Alternative selection: Every beat, push row, still-to-do candidate, write and destination was swept; see the decision sweep in the report. B is the only unconditional open fork.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Marcus flagged the Collect &amp; Win event icon animation since the brief, so it is a player-facing art item on the Collect &amp; Win row. Season Pass First window is the October season. | Plan seven beats on the calendar with Boss Arena, Zombie Lane and the Halloween one-off off it; hold Weekly Leaderboard until its fix is confirmed on prod; Collect &amp; Win starts late; two pushes go, eight are held. | Fill the Calendar and Pushes tabs; comment on ZOM-429; link the sheet on ZOM-78; reply to Brian on the Sep 26 mail; send Frederick the recommendation in the DM. | Julia sheet ZM3D Beta Live-Ops Calendar; Linear ZOM-429 and ZOM-78; Gmail thread of the Sep 26 mail; Slack DM D05SD5QLG94. | Collect &amp; Win Still to do: prod deploy (Douglas), final vial models (Claire), event icon animation (Marcus). Season Pass First window Oct 1 00:00 UTC. | BR\_STILL (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev10/inputs/01\_Universe\_Inject.sql pointer docs\_documents f\_7c3e91a4d2b85f60e1a9c4): "anything flagged since this brief as still needed for it (prod deploy, config or player-facing art)"; MK (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev10/inputs/01\_Universe\_Inject.sql pointer linear\_comments cmt\_zom465\_2): "The Collect &amp; Win event icon animation is still to do on my side" |
| B | The note says still to do, not still needed. Only the owner says it, nobody says it must land for bought users, and idle icon animation is the same kind of effect others ruled out for the beta, so it stays off the row. | Plan seven beats on the calendar with Boss Arena, Zombie Lane and the Halloween one-off off it; hold Weekly Leaderboard until its fix is confirmed on prod; Collect &amp; Win starts late; two pushes go, eight are held. | Fill the Calendar and Pushes tabs; comment on ZOM-429; link the sheet on ZOM-78; reply to Brian on the Sep 26 mail; send Frederick the recommendation in the DM. | Julia sheet ZM3D Beta Live-Ops Calendar; Linear ZOM-429 and ZOM-78; Gmail thread of the Sep 26 mail; Slack DM D05SD5QLG94. | Collect &amp; Win Still to do: prod deploy (Douglas), final vial models (Claire) only. Season Pass First window Oct 1 00:00 UTC. | BR\_STILL (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev10/inputs/01\_Universe\_Inject.sql pointer docs\_documents f\_7c3e91a4d2b85f60e1a9c4): "what still has to land before it runs for bought users"; Z565 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev10/inputs/01\_Universe\_Inject.sql pointer linear\_comments cmt\_zom565\_2): "so they can follow and do not have to land before the beta" |
| C | First window means the first one that opens inside the span, so Season Pass shows the November season and the October season is only noted as running. | Plan seven beats on the calendar with Boss Arena, Zombie Lane and the Halloween one-off off it; hold Weekly Leaderboard until its fix is confirmed on prod; Collect &amp; Win starts late; two pushes go, eight are held. | Fill the Calendar and Pushes tabs; comment on ZOM-429; link the sheet on ZOM-78; reply to Brian on the Sep 26 mail; send Frederick the recommendation in the DM. | Julia sheet ZM3D Beta Live-Ops Calendar; Linear ZOM-429 and ZOM-78; Gmail thread of the Sep 26 mail; Slack DM D05SD5QLG94. | Collect &amp; Win Still to do: prod deploy (Douglas), final vial models (Claire), event icon animation (Marcus). Season Pass First window Nov 1 00:00 UTC. | BR\_SPAN (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev10/inputs/01\_Universe\_Inject.sql): "The calendar covers Mon Oct 6 00:00 UTC to Sun Nov 2 23:59 UTC"; BF26 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev10/inputs/01\_Universe\_Inject.sql): "The November season still opens on Sat Nov 1." |

Explicit option inventory: The prompt has no candidate option list.
Inventory evidence: P (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev10/inputs/04\_Prompt.txt): "Can you take it on for me?"

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: B
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. The rule asks for items flagged as still needed. The only record on the icon animation is its owner saying it is still to do. No prompt sentence, rule source or third-party record says it must land before bought users or that it can follow, so the cell has two defensible contents.
Resolution evidence: MK (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev10/inputs/01\_Universe\_Inject.sql pointer linear\_comments cmt\_zom465\_2): "The Collect &amp; Win event icon animation is still to do on my side"; BR\_STILL (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev10/inputs/01\_Universe\_Inject.sql pointer docs\_documents f\_7c3e91a4d2b85f60e1a9c4): "not polish nobody flagged"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same run and hold calls. |
| writes | SAME | Same writes. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | The Still to do cell of Collect &amp; Win, and any owner list in the recommendation, differ by one item and one owner. |

Resolution relevance challenge: not polish nobody flagged shows flagged polish may go in, but it does not say an owner note counts as still needed, and the grading standard does not let an owner claim settle its own gap.
Delegation challenge: NOT_CLAIMED. Nothing delegates this choice to the Agent.
Challenge evidence: BR\_STILL (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev10/inputs/01\_Universe\_Inject.sql pointer docs\_documents f\_7c3e91a4d2b85f60e1a9c4): "anything flagged since this brief as still needed for it"

Compared alternative: C
Resolution: BOTH_FAIR_FIGURE. Only the First window date differs and nothing ranks the two.
Resolution evidence: BR\_SP (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev10/inputs/01\_Universe\_Inject.sql): "Season Pass seasons open on the 1st at 00:00 UTC."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same. |
| writes | SAME | Same. |
| destinations | SAME | Same. |
| contents | DIFFERENT | One date in one cell. |

Both-fair figure: DATE, Season Pass First window
Value for A: Oct 1 00:00 UTC. Evidence: BR\_SP (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev10/inputs/01\_Universe\_Inject.sql): "Season Pass seasons open on the 1st at 00:00 UTC."; AR472 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev10/inputs/01\_Universe\_Inject.sql pointer github\_review\_comments match3d\#472\#rc\_1): "the Season Pass premium strip is still set to the October range". Derivation: Schedules already on prod on Sep 30, so the next season to open is Oct 1 at 00:00 UTC.
Value for C: Nov 1 00:00 UTC. Evidence: BR\_SP (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev10/inputs/01\_Universe\_Inject.sql): "Season Pass seasons open on the 1st at 00:00 UTC."; BF26 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev10/inputs/01\_Universe\_Inject.sql): "The November season still opens on Sat Nov 1.". Derivation: First season that opens inside the Oct 6 to Nov 2 span.
Newer source check does not settle it: Both come from the same rule.
Authority check does not settle it: The brief does not say whether a window already open at span start is the first window.
Source identity check does not settle it: One source.
Scope check does not settle it: Both windows overlap the span.
Same material result check does not settle it: Only one cell differs; both list both seasons under Windows.
Every explicit ask: Each reading still states both seasons, weeks, push and still-to-do.
Next step unchanged: The date does not change any hold, write or owner.
Rubric must accept: Oct 1 00:00 UTC or Nov 1 00:00 UTC

Resolution relevance challenge: The rule gives the cadence, not the treatment of a window open at span start.
Delegation challenge: NOT_CLAIMED. No delegation is claimed.
Challenge evidence: BR\_SPAN (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev10/inputs/01\_Universe\_Inject.sql): "The calendar covers Mon Oct 6 00:00 UTC to Sun Nov 2 23:59 UTC"

Strongest-alternative challenge (B): B is not a strawman: three records rule comparable VFX polish out for the beta, and this one has no such record either way.
Challenge evidence: MK (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev10/inputs/01\_Universe\_Inject.sql pointer linear\_comments cmt\_zom465\_2): "The Collect &amp; Win event icon animation is still to do on my side"

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

#### Decision sweep

Basis labels: RECORD, SCOPE_GAP, SILENCE. "Rule" means Frederick's message, reply or brief.

**Beats**

| Item | Outcome | Basis | Settled by |
|---|---|---|---|
| Collect & Win | In, late start, first window Fri Oct 10 00:00 UTC, not held | RECORD | Rule "A beat whose server windows are waiting on that release starts late, it is not held."; rc_10 "still on the DEV stack only"; GCal 2025-10-08 15:00Z. Wed window opened 00:00 UTC, before the release |
| Plague Race | In, W1 to W4, no dates | RECORD | Rule; rc_10 "already running on prod" |
| Weekly Leaderboard (leagues) | Held until the fix is confirmed on prod | RECORD | Vincent Sep 30 "killed the app and reopened it twice ... Same on the second device" is newer than Douglas Sep 16 and meets the hold test. Vincent is QA, not the owner |
| Endless Monster Mode | In, W1 to W4, weekly Mon 00:00 UTC, daily 00:00 UTC | RECORD | Confluence "daily reset 00:00 UTC, weekly reset Monday 00:00 UTC"; a reset qualifies under the rule, unlike Zombie Lane |
| Season Pass | In; October season runs, November opens Nov 1 00:00 UTC | RECORD for both windows; First window cell is BOTH_FAIR_FIGURE | Rule; Brian Sep 26; rc_1 "October range" |
| Quest rollover | In, W1 to W4, no dates | RECORD | ZOM-534 Leonard (reporter) "it is good on prod now" |
| Daily gift | In, W1 to W4, no dates | RECORD | ZOM-556 Vincent "claiming works and nothing is lost"; rule "Wrong counters ... do not hold" |
| Boss Arena | Off | RECORD | Rule "off this calendar until the pivot call" |
| Zombie Lane | Off | RECORD | Reply "keep Zombie Lane off the calendar" |
| Halloween one-off | Off | RECORD | Robert Sep 30 "pulling my ok. Take it off the beta calendar"; rule "his later word is the one that counts" |
| Desert and Port themes | Not beats | RECORD | Robert Sep 30 "nothing waits on new themes" |

**Push rows (PNs Beta, sheet row number)**

| Row | Item | Status / Live col | Outcome | Basis | Settled by |
|---|---|---|---|---|---|
| 2 | Quests | Not Ready / LIVE | Hold: not Ready | RECORD | Rule |
| 3 | Hourly Coins | Not Ready / LIVE | Left off | RECORD | Reply |
| 4 | Lives recharged | Ready / LIVE | Send, no game name | RECORD | Reply "fine to go out" |
| 5 | 1 day lapsed | Ready / LIVE | Hold: copy says Puzzles vs Zombies | RECORD | Rule; spec rename 24 July 2025 |
| 6 | 7 days lapsed | Ready / LIVE | Send | RECORD | Reply |
| 7 | FTUE | Ready / LIVE | Hold: Puzzles vs Zombies | RECORD | Rule |
| 8 | Win & Collect | Not Ready / WIP | Hold: not Ready, not LIVE, wrong event name | RECORD | Rule; Confluence "under a different name" |
| 9 | Nathan's Treasure Hunt | Not Ready / WIP | Left off | RECORD | Reply |
| 10 | Plague Race | Ready / WIP | Hold: not LIVE | RECORD | Rule |
| 11 | Streak Fever | Not Ready / WIP | Left off | RECORD | Reply |
| 12 | Axe Arena | Not Ready / WIP | Left off | RECORD | Reply |
| 13 | Login Calendar | Not Ready / WIP | Hold: not Ready, not LIVE, copy says login calendar | RECORD | Rule "(the Login Calendar row on the push sheet)" shows the ZM3D name is daily gift |
| 14 | Season Pass | Not Ready / WIP | Hold: not Ready, not LIVE | RECORD | Rule |
| 15 | Weekly Leaderboard | Ready / WIP | Hold: not LIVE | RECORD | Rule |

**Still-to-do candidates flagged since the brief (Sep 24 17:15 UTC created)**

| Item | Outcome | Basis | Settled by |
|---|---|---|---|
| Collect & Win prod deploy | In, Douglas | RECORD | rc_10; GCal organizer douglas@ |
| Final vial models | In, Claire | RECORD | Arthur rc_38 (third party) |
| **Collect & Win event icon animation** | **Open: in or out** | **SCOPE_GAP** | Only Marcus, the owner: "still to do on my side". F1 |
| **Collect & Win reward tables** | **Open if the channel is visible** | **SILENCE** | Brian Sep 26 to Douglas "I Also changed 1 reward in each of the two reward tables. Could you update them?" No reply, no ticket, no later record. F2 |
| Weekly Leaderboard fix | In, Douglas | RECORD | Rule "its fix if it is held"; ZOM-429 assignee |
| November config | In, Brian, moved before Oct 31 00:00 UTC | RECORD | Spec "locked 24h before each season opens"; Oct 31 10:00 Istanbul is 07:00 UTC |
| Premium strip date | In, Oliver | RECORD | Arthur rc_1 (third party) |
| Daily gift frame ZOM-432 | Out, shipped | RECORD | Samuel; #471 commit "Fixing UI Elements on Daily Gift"; builds #50 and #135 in #builds Sep 30 |
| Quests more content, Trello #61 | Out | SCOPE_GAP, no cell | Leonard, named owner: "The weekly rollover does not wait on them". A careful reader has no ground to add it; flagged for P1 |
| lightSweep box | Out | RECORD | Vincent (reporter) "nothing has to land for the beta" |
| Airstrike freeze | Out, unverified | RECORD | Leonard (reporter) "Could not get it to freeze" |
| ZOM-526 token travel | Out | RECORD | Brian; #472 merged; rest waits on Axe Arena |
| ZOM-565 Endless VFX | Out | RECORD | Brian "do not have to land before the beta" |
| ZOM-566 and PR #477 | Out | RECORD | Rule "not analytics"; Brian on the header and info text |
| ZOM-552, 442, 549, 548 | Out | RECORD | Rule "not analytics" |
| ZOM-543 queue manager | Out | RECORD | Not deploy, config or art; #472 merged |
| ZOM-521, 528, 541 card VFX | Out | RECORD | Card pack is not a beat |
| Collect & Win Bug_Checklist canvas | Out | RECORD | Vincent "none of them blockers and doesn't affect the submission" |
| Marcus particles note Sep 24 16:58 UTC | Out | RECORD | Predates the brief's created time 17:15 UTC |
| Store approval of Sep 30 builds | Out | RECORD | Deck dated Sep 23, not flagged since the brief |

**Open PRs:** #477 analytics, out. #476 vision bot, not a beat. match3d-backend#34 draft, no review. auth-game-backend#2 and game-of-dominoes-backend#79, not ZM3D beats. **Change-request rule:** all 74 CHANGES_REQUESTED reviews checked; latest are match3d-backend#4 (June) and match3d#303 (July), none on or after Aug 1, so no beat holds under it. The undefined "Aug-Sep live-ops cohort" changes nothing.

**Writes and destinations**

| Item | Outcome | Basis | Settled by |
|---|---|---|---|
| Sheet | ZM3D Beta Live-Ops Calendar, tabs Calendar and Pushes | RECORD | DM "the calendar sheet in your ZM Live Ops folder" |
| Calendar ticket | ZOM-78, not ENG-2240 | RECORD | cmt_zom78_1 |
| Held-beat note | ZOM-429 only. A held push is not a held beat | RECORD | Rule "Hold a beat only when players provably cannot enter, score or claim" |
| Recommendation | DM D05SD5QLG94 | RECORD | DM "back here" |
| Brian reply | Sep 26 mail, in scope | RECORD | Rule; Brian "reply on this mail" |
| New date | Any instant before Oct 31 00:00 UTC | RECORD, objective boundary | Rule "lands before its lock". Later rubric must not lock one date |

**Forks**
- F1 (open, unconditional): Collect & Win Still to do. A lists the icon animation, B leaves it off. Missing: a dated record from someone other than Marcus saying whether it must land for bought users.
- F2 (open if `#zm-collect-win` is readable): reward tables. Public but archived, Julia not a member; runtime visibility unverified. Reading A omits it, Reading B lists Douglas. Confluence "re-imported from Google Sheets hourly in production" suggests it needs no action, but that is an inference, not a kill. Missing: a dated closing record.
- F3 (BOTH_FAIR_FIGURE): Season Pass First window, Oct 1 00:00 UTC or Nov 1 00:00 UTC.

---

**Feasibility:** PASS (5). Every write has a cataloged operation; all facts exist. No per-X breakdown. Numeric asks are dates only; catalog has no return schemas, so rendering is an evidence limit, not a defect.

**Persona ACL Reachability:** PASS (5). Lens 1: DM, Robert DM, #zombie-match3d, #zombie-bugs, #zombie-art by membership; brief and deck by reader share; `Push Notifications Zombie Match` by share; Julia's sheet by ownership; mail by her mailbox copies; release event on her calendar. GitHub, Linear, Trello, Confluence unscoped. #zombie-prs needs no read since GitHub holds the source. Lens 2: no ask directs an out-of-view read. No required record is hidden.

**Truthfulness:** PASS (5).

| Claim | Found | Evidence |
|---|---|---|
| Frederick messaged yesterday | Yes | ts 2025-09-30T20:20:17Z, 13:20 PT |
| Live-ops and push calendar for the ZM3D beta | Yes | "I need the live-ops and push calendar for the beta buy" |
| Four buy weeks, Monday the 6th | Yes | Deck W1 to W4; Oct 6 2025 is a Monday |
| Brief shared with Julia | Yes | reader share, Sep 24 |
| My live-ops calendar sheet | Yes | owner Julia, folder ZM Live Ops |
| Calendar ticket | Yes | ZOM-78 |
| Recommendation he asked for | Yes | "send me your recommendation back here" |

Departed people: none. Nothing after the clock is treated as done.

**Tool Use & Cross-service:** PASS (5). Graded fact per service: GitHub (which windows are on prod, vial and strip items), GCal (release instant, so Oct 10), Gmail (Oct 31 commitment), Confluence (24h lock, Endless resets), GSheets (push rows), Slack (Leaderboard hold, Halloween pull), Linear (owners, ZOM-78). Dropping any changes an answer.

**Investigation + Action:** PASS (5). Writes depend on findings.

**Clarity:** NON-FAIL (3). Intent is clear and no "I'll" statement exists. F1 and F2 vary the contents of one cell, not the writes, so this is not Action Decision Ambiguity.

**Contrived:** PASS (5). All Eval 2.7 indicators No. The destination is named; the recipient is named; a single "If" is not an if-chain; "If a beat ends up held" does not point at which beat.

**Alignment with Today's Date:** PASS (5). All relative words resolve; future dates are treated as future.

**Originality:** N/A, no samples supplied.

---

### Phase 3: Universe Feasibility

**Data Existence:** PASS (5). Entities verified 7 of 7 premises plus all sweep records. All retrievable via cataloged tools. Linear comments exist only through the SQL (base `comments` is empty); `linear_list_comments` is cataloged.

**Cross-Service Coherence:** FAIL (2). Two or more low-impact items fail under the review standard.

| # | Category | Artifacts | Evidence |
|---|---|---|---|
| C1 | Referential | Trello card #61 (task-touched) | SQL action `"name":"BETA: Sep 30"` against list record `BETA: Oct 10` for id 6851a674975da1fe76e70d93. Base origin SC-13; the SQL adds one more |
| C2 | Referential | Confluence calendar page and CDK stack | "re-imported from Google Sheets hourly in production" against `IMPORT_REWARDS_SCHEDULE ... "*/5 * * * *"`. Base origin SC-62 |
| C3 | Semantic | UA deck, SQL | Slide 2 "scaled up week by week if the cohorts hold" against slide 3 "hold the spend there until the pivot call" |

Noted, not scored: `PNs Beta` Status and Live columns disagree on sight (Not Ready / LIVE), but the brief treats them as two axes, so this is designed friction. #468 timeline ev_6 sits after `closed` with a null date (Eval 0 scope). Season Pass spec SC-38 and PR #477 SC-18 are not used by any graded fact.
- Injection SQL considered: Yes. Static integrity: direct task-relevant checks; Eval 0 pending. Sources, access and configuration: supported.

| Prompt ask / source | Static evidence | Discovery/access | Task coherence |
|---|---|---|---|
| Calendar and pushes | NEW | Supported | FAIL (C1 to C3) |
| Ticket note, link | NEW | Supported | PASS |
| Recommendation, Brian reply | NEW | Supported | PASS |

---

### Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score | Justification |
|---|---|---|---|
| Prompt | Unique Ground Truth | 2 | F1 open; F2 conditional; F3 both fair |
| Prompt | Feasibility | 5 | All asks doable |
| Prompt | Persona ACL Reachability | 5 | All required reads visible |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 3 | Same writes, one cell varies |
| Prompt | Contrived / Unnatural | 5 | Natural request |
| Prompt | Alignment with Today's Date | 5 | Resolves |
| Prompt | Originality / Sample Similarity | N/A | No samples |
| Prompt | Truthfulness | 5 | 7 of 7 premises hold |
| Prompt | Tool Use & Cross-service | 5 | Each service changes a graded fact |
| Prompt | Investigation + Action | 5 | Writes follow findings |
| Prompt | Coherence (Bolt-on) | 5 | One workflow |
| Prompt | Persona | 5 | Fits Julia |
| Prompt | Business Function | 5 | Product |
| Prompt | Assigned Competency | 5 | Marketing and GTM |
| Prompt | Assigned Task Skill | 5 | Planning and decision support |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three load-bearing |
| Universe | Data Exists | 5 | All retrievable |
| Universe | Cross-Service Coherence | 2 | C1, C2, C3 |

Draft verdict: FAIL, score 2 (final verdict block comes after the Deep Recheck).

---

### Issues Found

| # | Issue | Severity | Dimension |
|---|---|---|---|
| 1 | F1: icon animation rests only on the owner's note | Major | Unique Ground Truth |
| 2 | F2: reward tables request has no closing record | Major if the channel is readable | Unique Ground Truth |
| 3 | C1 to C3: three low-impact inconsistencies | Moderate together | Cross-Service Coherence |
| 4 | Multiple readings of "still needed" change one cell | Minor | Clarity |

### Recommended Improvements

1. F1: add one dated comment on ZOM-465 by someone other than Marcus, such as Brian who owns the VFX priority list, saying whether the Collect & Win icon animation must land for bought users.
2. F2: add a dated closing record for Brian's Sep 26 request (Douglas confirming the two tables are updated), or a visible record that it is still open.
3. C1: move Leonard's rollover note off Trello card #61 to a surface with no list-name field.
4. C3: make slide 2 agree with slide 3 on what happens to spend before the pivot call.
5. C2 is base data (SC-62). Keep the reward-import sentence out of every graded fact; it still counts as present.
6. For later stages: accept either Season Pass First window; accept any handoff date before Oct 31 00:00 UTC.

### Evidence limits
Eval 0 report pending. P1 to P4 pending. Evals/Docs PDFs and the Example Task not read (no extractor); scoring.json and Eval 1 overrides were used. Runtime visibility of non-member public Slack channels unverified. `review_context_sha256` null and full `validate_record` not run, since `start` is out of bounds; the UGT object passed `hg_prompt_ugt.validate_review` read-only with a local context.

---

### Appendix: every open ZOM ticket (post-SQL)

Default row: not flagged since the brief, so out under the rule "Nothing else goes in". Basis RECORD.

| Ticket | State | Owner | Title | Outcome |
|---|---|---|---|---|
| ZOM-16 | Backlog | marcus.bennett | Liquid Impact | Out (default) |
| ZOM-48 | Backlog | Robert | Reward Animations | Out (default) |
| ZOM-56 | Backlog | marcus.bennett | Glued VFX | Out (default) |
| ZOM-62 | Todo | vincent.parker | Zombie Ops #3 Spec (Dead Eye) | Out (default) |
| ZOM-64 | Backlog | marcus.bennett | Experiment with VFX when matching boss busters off t | Out (default) |
| ZOM-65 | Backlog | none | Profile page endpoints | Out (default) |
| ZOM-66 | Backlog | none | Stats endpoints | Out (default) |
| ZOM-69 | Backlog | none | Bot system | Out (default) |
| ZOM-70 | Backlog | none | Rewards system | Out (default) |
| ZOM-73 | Backlog | arthur.blake | A/B Test Item Sizes | Out (default) |
| ZOM-76 | Backlog | EMPLOYEE_0032_NAME | [PERSON_NAME_0120] to implement this VFX | Out (default) |
| ZOM-78 | Backlog | douglas | Event Calendar For Zombie Match 3D | Calendar ticket, gets the link |
| ZOM-97 | Todo | Robert | REVISION FOR ITEMS | Out (default) |
| ZOM-104 | Backlog | claire.morgan | Gas Can improvement | Out (default) |
| ZOM-118 | Todo | marcus.bennett | Shop Animations Master Ticket | Out (default) |
| ZOM-119 | Backlog | marcus.bennett | Shine for gold and gem piles. | Out (default) |
| ZOM-121 | Backlog | marcus.bennett | Card pack animation in the shop | Out (default) |
| ZOM-122 | Backlog | marcus.bennett | Simple animations for offers bands and labels. | Out (default) |
| ZOM-130 | Todo | leonard.hayes | Create an out of moves screen flow with offers | Out (default) |
| ZOM-137 | Backlog | claire.morgan | FOOD ITEMS | Out (default) |
| ZOM-147 | Backlog | claire.morgan | Peach | Out (default) |
| ZOM-148 | Backlog | claire.morgan | Plum | Out (default) |
| ZOM-150 | Backlog | claire.morgan | Cherries | Out (default) |
| ZOM-151 | Backlog | claire.morgan | Cucumbers | Out (default) |
| ZOM-155 | Backlog | claire.morgan | Squash | Out (default) |
| ZOM-168 | Backlog | EMPLOYEE_0032_NAME | 5th In-game Boost Double Damage | Out (default) |
| ZOM-171 | Todo | martin.walsh | Icon for double damage in-game boost | Out (default) |
| ZOM-181 | Todo | claire.morgan | 8. Vaious Solid color Plates/cups/mugs/egg on plates | Out (default) |
| ZOM-182 | Todo | claire.morgan | 9. Bagel | Out (default) |
| ZOM-184 | Todo | claire.morgan | 11.Curling Iron (Maybe Drop the item) | Out (default) |
| ZOM-202 | In Progress | arthur.blake | Minimize or migrate selection panel for easier diffi | Out (default) |
| ZOM-236 | Backlog | EMPLOYEE_0032_NAME | Shop Pack Idle animation | Out (default) |
| ZOM-237 | Backlog | none | packs animations bugs | Out (default) |
| ZOM-243 | Backlog | marcus.bennett | Poison/Fire/Shock Death Vfx Animations | Out (default) |
| ZOM-255 | Backlog | owen.baker | Tap to skip kill cam + Dimming the board area and on | Out (default) |
| ZOM-292 | Todo | arthur.blake | Level Editor Improvements 2.0 | Out (default) |
| ZOM-293 | Todo | Robert | Dynamic Difficulty Tiering Down Issue | Out (default) |
| ZOM-311 | In Progress | arthur.blake | Consider migrating the list of items and list of mon | Out (default) |
| ZOM-317 | Backlog | martin.walsh | Martin to polish UI assets in FIGMA | Out (default) |
| ZOM-342 | Todo | claire.morgan | Indoor Plant | Out (default) |
| ZOM-348 | Todo | none | Rotating Shop Discount Issues | Out (default) |
| ZOM-359 | Regression | arthur.blake | Phone heating up too much after playing 15 to 20 lev | Out (default) |
| ZOM-386 | Todo | douglas | Track Player Card Inventory and Sync to BigQuery | Out (default) |
| ZOM-387 | Todo | arthur.blake | Giant Analytics Ticket | Out, analytics |
| ZOM-390 | Backlog | julia.lawson | Icon and Event Visual for Win Streak Event (axe aren | Axe Arena not in beta |
| ZOM-400 | Todo | arthur.blake | We want to add a new field to left_level event to tr | Out (default) |
| ZOM-427 | Todo | arthur.blake | App icon is too zoomed in for android | Out (default) |
| ZOM-429 | Backlog | douglas | Leaderboard next session doesn't start without killi | Held beat ticket, gets the note |
| ZOM-438 | Todo | arthur.blake | Investigate why some zombie tracks do not spawn | Out (default) |
| ZOM-439 | Todo | arthur.blake | Investigate card_upgrade event not recording correct | Out (default) |
| ZOM-441 | Todo | arthur.blake | Fix reward_str and chest_content_str sending issue | Out (default) |
| ZOM-442 | In Validation | oliver.brooks | Analytics Instrumentation for Tropy Reward Redeem | Out, analytics |
| ZOM-443 | Todo | arthur.blake | Investigate non-random item removal from board due t | Out (default) |
| ZOM-449 | Backlog | arthur.blake | Some items are acting weird in low-end android devic | Out (default) |
| ZOM-453 | Todo | samuel.turner | Fix text inconsistency | Out (default) |
| ZOM-458 | Todo | arthur.blake | Quitting algo levels still makes the level change an | Out (default) |
| ZOM-465 | In Progress | marcus.bennett | Endless Mode Master VFX Ticket | F1 open (SCOPE_GAP) |
| ZOM-467 | In Progress | marcus.bennett | Zombie Match 3d - Marketing Videos | Out (default) |
| ZOM-468 | Todo | arthur.blake | Low-end devices rendering issues | Out (default) |
| ZOM-471 | Todo | samuel.turner | Add red dot icon for players not in Plague Race | Out, Leonard "we don’t need it!" Aug 13 |
| ZOM-475 | Todo | oliver.brooks | Consecutive glass impact sfx/vfx causes crash on and | Not a beat (SC-8, do not grade) |
| ZOM-477 | Todo | EMPLOYEE_0032_NAME | DOT kills can take too long and cause perceived unre | Out (default) |
| ZOM-481 | Todo | owen.baker | Zombie Health bar persists too long after death. | Out (default) |
| ZOM-482 | Backlog | EMPLOYEE_0032_NAME | Make "Fast-forwarding" another boolean properties in | Out (default) |
| ZOM-483 | Todo | calvin.price | Infinite lives from new-install are not granted, rew | Out (default) |
| ZOM-484 | Todo | marcus.bennett | Info Screen Animations | Out (default) |
| ZOM-504 | Backlog | EMPLOYEE_0032_NAME | In endless mode, objects might stay persistent in th | Out, visual, bot only |
| ZOM-505 | Backlog | vincent.parker | Tutorial repeats at level 19 in V 1736 Android versi | Out (default) |
| ZOM-508 | Todo | oliver.brooks | Assisted Start | Out (default) |
| ZOM-513 | In Progress | claire.morgan | Convert Maracas into multi-color variant-enabled | Out (default) |
| ZOM-514 | In Progress | claire.morgan | Request to add motorcycle helmet as a survival item | Out (default) |
| ZOM-517 | Backlog | EMPLOYEE_0032_NAME | Monster loses enrage during item refill in endless m | Out, retest clean |
| ZOM-520 | Todo | oliver.brooks | First loss as level doesn't reset win streak | Out (default) |
| ZOM-521 | In Progress | calvin.price | Master Ticket - VFX implementation | Out, see sweep |
| ZOM-526 | In Progress | none | Tokens traveling to live-ops | Out, see sweep |
| ZOM-528 | In Progress | calvin.price | Claimed Cards traveling to inventory section | Out, see sweep |
| ZOM-534 | In Progress | douglas | Quest points not resetting until app restart in prod | Quests not held, good on prod |
| ZOM-535 | Todo | EMPLOYEE_0032_NAME | Fast matching might target an already-dead zombie | Out (default) |
| ZOM-539 | Todo | samuel.turner | Implement Red Dot for Cards and Shop | Out (default) |
| ZOM-541 | In Progress | calvin.price | Cards Collect Vfx animation | Out, see sweep |
| ZOM-542 | Regression | samuel.turner | Update home screen and victory score screen for game | Out, not flagged since brief |
| ZOM-543 | In Progress | calvin.price | Queue Manager | Out, see sweep |
| ZOM-544 | In Progress | EMPLOYEE_0032_NAME | Implement Google Apple Login | Not a beat |
| ZOM-545 | Todo | douglas | Ingest bot params from a spreadsheet | Out (default) |
| ZOM-546 | Todo | owen.baker | Bug: refill algorithm spawns fewer items over time | Out, retest clean |
| ZOM-548 | In Validation | EMPLOYEE_0032_NAME | Track events for boss arena as listed in the spreads | Out, analytics, Boss Arena off |
| ZOM-549 | In Validation | EMPLOYEE_0032_NAME | Add new fields to left_level and endless_left analyt | Out, analytics |
| ZOM-552 | In Progress | oliver.brooks | Season Pass Analytics | Out, analytics |
| ZOM-554 | Todo | owen.baker | Quiting level mid tornado boost breaks the object ph | Out (default) |
| ZOM-556 | Todo | calvin.price | When the daily gift is skipped, it doesn't reset to  | Daily gift not held, wrong counter |
| ZOM-559 | Todo | oliver.brooks | Homing out on android(samsung), sound disappears. | Out (default) |
| ZOM-560 | Todo | samuel.turner | The abandoned pack win streak freezer reward is not  | Out (default) |
| ZOM-562 | Todo | owen.baker | Orphan items in boss arena | Boss Arena off |
| ZOM-564 | Todo | oliver.brooks | "Free" label stays on boosters after Tutorial | Out (default) |
| ZOM-565 | Todo | calvin.price | Endless Horde Start Screen Vfx | Out, see sweep |
| ZOM-566 | In Progress | owen.baker | Collect&Win Analytics | Out, analytics |

ENG-2240 Web interface for the liveops calendar (Todo): decoy for the calendar ticket, out. No non-ZOM open ticket since June matches a live-ops beat.
