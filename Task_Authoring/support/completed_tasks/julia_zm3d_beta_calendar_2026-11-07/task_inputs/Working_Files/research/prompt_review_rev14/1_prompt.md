## PROMPT EVALUATION REPORT

### Task: Julia Lawson builds the ZM3D beta live-ops and push calendar for four buy weeks and sends Frederick a run/hold recommendation
### Assigned Persona: Julia Lawson - Product Manager (julia_lawson, julia.lawson@harmonygames.co, Product)
### Assigned Business Function: Product
### Assigned Competency: Marketing and GTM
### Assigned Task Skill: Planning and decision support
### Assigned Horizon: Long Horizon (task type long-horizon; difficulty mode medium)

Scope: chat review from R14/inputs (prompt, assignment and date byte-identical to every earlier round), actual review date 2026-11-06, `Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)`. Prompt sha256 in the record. SQL sha256 edae63f3e83852f212c19892a9c9cf7304404b80db3178f92a470f301a598e13 (read, never executed). Eval version task-quality-v1, release sha256 c5b89f4c40a7902f968001f1aa6c710d47bf203842455bbe8dbb668ec7c8943b. No reference files, error/async config or dynamic context. `authority_contract: prompt-incorporation-v1`; `evidence_contract: stage-evidence-v1`, nothing reused.

Rule sources: the prompt, Frederick's DM and thread reply, his brief. Every other record is a fact source.

TODO status: Intake DONE. 0.5 Injection gate DONE (Eval 0 on this hash). 0.1 DONE for scoring.json, the QC rating form CSV, the visible QC spec strings, roster, ACL and catalog; the Evals/Docs PDFs could not be read here (no pypdf, pdftotext or pdftoppm). 0.2 DONE. 0.3 Example Task not read (same limit). 1.1 to 1.5, 2.1 to 2.8, 3.1, 3.2, 4.1, 4.2 DONE. 2.9 N/A. Phase 5 DONE.

---

### Delta (every changed statement read in full)

From 1f2175a2 to this hash, one statement changed, the brief row: "Endless goes down as its weekly windows, with the daily reset noted." was added, and "its owner is told" became "you tell its owner". All nine `style_runs` land on their headings in the 3,170-character body.

From ffbac458 to 1f2175a2:

| Statement | Change | Effect on this review |
|---|---|---|
| Frederick thread reply | Opens "Two things on top of the brief." | None |
| Robert Sep 18 | "one week of the beta", "lands in time" | None; approval still pulled |
| Robert Sep 30 | Drops "my later word..." sentence | None; the brief carries that rule |
| Vincent lightSweep | "next store build" | Fits base: Oliver's commit 25c6c66b6b lands after the submission builds |
| New Douglas reply + parent counts | "Both tables are updated." in Brian's thread | Closes the reward-table fork |
| Brief, Span | Clip rule; windows close 23:59 UTC | Fixes Season Pass First window and all end instants |
| Brief, Scope | "the rotating shop is not a beat" | Removes a candidate beat |
| Brief, When a beat starts | "same beat" wording | None |
| Brief, Held | "A held beat keeps its usual windows and weeks on its row, marked held." | Fixes the Weekly Leaderboard row |
| Brief, Push copy | "(Login Calendar and Weekly Rankings are fine)"; held "with which of those its row is missing" | Row 13 has no naming miss; bounds the missing cell |
| Brief, Config locks | "moves to any time before it" | States the boundary |
| Deck slides 1, 2 | "Beta-cohort buy"; "any scale-up comes after the pivot call" | Closes C3 |
| Arthur #468 rc_38 + mirror | "still need their final models before the event runs" | Stronger |
| Arthur #472 rc_1 + mirror | "premium strip art" | Now plainly player-facing art |
| New cmt_zom465_3 (Brian) | "the Collect & Win icon does have to land before the event runs" | Closes the icon fork |
| ZOM-504 comment | "Re-tested:" wording | None |
| ZOM-542 | state_id Todo | Fits "Picking this up after the bug list" |
| ZOM-563 comments | New Douglas note; Vincent note reworded | Fits base DM "I updated the prod environment with the latest teams/social changes" at 18:16 UTC |

---

### Injection Gate
- State: Eval 0 ran on this hash. It is a separate reviewer's report, not the Evals gate helper, which is out of bounds here.
- Reviewed SQL sha256: edae63f3e83852f212c19892a9c9cf7304404b80db3178f92a470f301a598e13. Eval 0 verdict: PASS, COMPLETE, no demonstrated defect.
- Eval 0 findings on records this prompt depends on: none changes a value, set, order, recipient or destination, so none is scored. ADV-2 (ZOM-344) is its one coherence advisory and stays here under STEP 0.5. ADV-3, 7 to 10, 12 to 16, 19 to 21 are cosmetic.
- Checked directly here as well: author membership for all added Slack messages, doubled apostrophes, weekday arithmetic, mail dates, Drive parents, mirrors. `hg.py lint` on this hash: 0 FAIL, 0 CHECK.

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
| Reply on lock miss | Brief "Config locks", Sep 26 mail, spec | Brief to mailbox and Confluence | `gmail_reply_to_message` | Julia mailbox copy | Reply to Brian: moved to any time before Oct 31 00:00 UTC |

The Brian reply is incorporated: the prompt points to the brief, and the brief states the write. Brian's own "If the new date is a problem on your side, reply on this mail." names the thread.

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** PASS (5)

### Unique Ground Truth comparison

Unique Ground Truth: PASS 5

Basis: Every fork is ruled out by a quoted rule or record, and the moved date sits inside a stated boundary. The reward-table item is outside the scored comparison because its channel is not persona-visible, and the only record on it says it is done. The thinnest kill is the Weekly Leaderboard hold.

Alternative selection: Every beat, push row, still-to-do candidate, write and destination was swept, with all forks raised by passes on five hashes. G is the strongest alternative: it flips the status, the ZOM-429 write and the recommendation.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | All three Collect &amp; Win items are flagged since the brief. The October season is clipped to the span. Brian is told in a reply, with a new time before the lock. | Plan seven beats on the calendar with Boss Arena, Zombie Lane, the rotating shop and the Halloween one-off off it; hold Weekly Leaderboard until its fix is confirmed on prod; Collect &amp; Win starts late; two pushes go, eight are held. | Fill the Calendar and Pushes tabs; comment on ZOM-429; link the sheet on ZOM-78; reply to Brian on the Sep 26 mail; send Frederick the recommendation in the DM. | Julia sheet ZM3D Beta Live-Ops Calendar; Linear ZOM-429 and ZOM-78; Gmail thread of the Sep 26 mail; Slack DM D05SD5QLG94. | Collect &amp; Win Still to do: prod deploy (Douglas), final vial models (Claire), event icon animation (Marcus). Season Pass First window Oct 6 00:00 UTC. Endless four weekly windows with the daily reset noted. Brian handoff moved to Thu Oct 30. | BR\_STILL (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql pointer docs\_documents f\_7c3e91a4d2b85f60e1a9c4): "anything flagged since this brief as still needed for it (prod deploy, config or player-facing art)"; BZ (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql pointer linear\_comments cmt\_zom465\_3): "the Collect &amp; Win icon does have to land before the event runs"; BR\_CLIP (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql): "Clip anything that starts before or runs past that to those two instants." |
| B | The icon animation is cosmetic polish, so it stays off the Collect &amp; Win row. | Plan seven beats on the calendar with Boss Arena, Zombie Lane, the rotating shop and the Halloween one-off off it; hold Weekly Leaderboard until its fix is confirmed on prod; Collect &amp; Win starts late; two pushes go, eight are held. | Fill the Calendar and Pushes tabs; comment on ZOM-429; link the sheet on ZOM-78; reply to Brian on the Sep 26 mail; send Frederick the recommendation in the DM. | Julia sheet ZM3D Beta Live-Ops Calendar; Linear ZOM-429 and ZOM-78; Gmail thread of the Sep 26 mail; Slack DM D05SD5QLG94. | Collect &amp; Win Still to do: prod deploy (Douglas), final vial models (Claire) only. Season Pass First window Oct 6 00:00 UTC. Endless four weekly windows with the daily reset noted. Brian handoff moved to Thu Oct 30. | BR\_STILL (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql pointer docs\_documents f\_7c3e91a4d2b85f60e1a9c4): "what still has to land before it runs for bought users"; Z565 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql pointer linear\_comments cmt\_zom565\_2): "so they can follow and do not have to land before the beta" |
| C | First window means the first one that opens inside the span, so Season Pass shows Nov 1 and the October season is only noted. | Plan seven beats on the calendar with Boss Arena, Zombie Lane, the rotating shop and the Halloween one-off off it; hold Weekly Leaderboard until its fix is confirmed on prod; Collect &amp; Win starts late; two pushes go, eight are held. | Fill the Calendar and Pushes tabs; comment on ZOM-429; link the sheet on ZOM-78; reply to Brian on the Sep 26 mail; send Frederick the recommendation in the DM. | Julia sheet ZM3D Beta Live-Ops Calendar; Linear ZOM-429 and ZOM-78; Gmail thread of the Sep 26 mail; Slack DM D05SD5QLG94. | Collect &amp; Win Still to do: prod deploy (Douglas), final vial models (Claire), event icon animation (Marcus). Season Pass First window Nov 1 00:00 UTC. Endless four weekly windows with the daily reset noted. Brian handoff moved to Thu Oct 30. | BR\_SPAN (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql): "The calendar covers Mon Oct 6 00:00 UTC to Sun Nov 2 23:59 UTC"; BF26 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql): "The November season still opens on Sat Nov 1." |
| D | The prompt lists four writes and the brief is rules for building the calendar, so mail to Brian stays with Julia and is only flagged to her. | Plan seven beats on the calendar with Boss Arena, Zombie Lane, the rotating shop and the Halloween one-off off it; hold Weekly Leaderboard until its fix is confirmed on prod; Collect &amp; Win starts late; two pushes go, eight are held. | Fill the Calendar and Pushes tabs; comment on ZOM-429; link the sheet on ZOM-78; send Frederick the recommendation in the DM. No mail to Brian. | Julia sheet ZM3D Beta Live-Ops Calendar; Linear ZOM-429 and ZOM-78; Slack DM D05SD5QLG94. | Collect &amp; Win Still to do: prod deploy (Douglas), final vial models (Claire), event icon animation (Marcus). Season Pass First window Oct 6 00:00 UTC. Endless four weekly windows with the daily reset noted. Brian handoff moved to Thu Oct 30. | P (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/04\_Prompt.txt): "Once the sheet's done, link it on the calendar ticket and send Frederick the recommendation he asked for." |
| E | The handoff moves back to the original Wed Oct 29. | Plan seven beats on the calendar with Boss Arena, Zombie Lane, the rotating shop and the Halloween one-off off it; hold Weekly Leaderboard until its fix is confirmed on prod; Collect &amp; Win starts late; two pushes go, eight are held. | Fill the Calendar and Pushes tabs; comment on ZOM-429; link the sheet on ZOM-78; reply to Brian on the Sep 26 mail; send Frederick the recommendation in the DM. | Julia sheet ZM3D Beta Live-Ops Calendar; Linear ZOM-429 and ZOM-78; Gmail thread of the Sep 26 mail; Slack DM D05SD5QLG94. | Collect &amp; Win Still to do: prod deploy (Douglas), final vial models (Claire), event icon animation (Marcus). Season Pass First window Oct 6 00:00 UTC. Endless four weekly windows with the daily reset noted. Brian handoff moved to Wed Oct 29. | BR\_LOCK (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql): "moves to any time before it" |
| F | Endless is listed as 28 daily windows, since it resets daily and Every window is stated as an instant. | Plan seven beats on the calendar with Boss Arena, Zombie Lane, the rotating shop and the Halloween one-off off it; hold Weekly Leaderboard until its fix is confirmed on prod; Collect &amp; Win starts late; two pushes go, eight are held. | Fill the Calendar and Pushes tabs; comment on ZOM-429; link the sheet on ZOM-78; reply to Brian on the Sep 26 mail; send Frederick the recommendation in the DM. | Julia sheet ZM3D Beta Live-Ops Calendar; Linear ZOM-429 and ZOM-78; Gmail thread of the Sep 26 mail; Slack DM D05SD5QLG94. | Collect &amp; Win Still to do: prod deploy (Douglas), final vial models (Claire), event icon animation (Marcus). Season Pass First window Oct 6 00:00 UTC. Endless 28 daily windows. Brian handoff moved to Thu Oct 30. | BR\_END (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql): "Every window is stated in server time (UTC) as a start-end instant" |
| G | Nothing is held. Vincent does not say a player cannot enter, score or claim, one tester is unverified, and a stale reset is a reset gap. | Plan seven beats with nothing held; Weekly Leaderboard runs; Collect &amp; Win starts late; two pushes go, eight are held. | Fill the Calendar and Pushes tabs; link the sheet on ZOM-78; reply to Brian on the Sep 26 mail; send Frederick the recommendation in the DM. No note on ZOM-429. | Julia sheet ZM3D Beta Live-Ops Calendar; Linear ZOM-78; Gmail thread of the Sep 26 mail; Slack DM D05SD5QLG94. | Collect &amp; Win Still to do: prod deploy (Douglas), final vial models (Claire), event icon animation (Marcus). Season Pass First window Oct 6 00:00 UTC. Endless four weekly windows with the daily reset noted. Brian handoff moved to Thu Oct 30. | BR\_HOLD (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql): "Hold a beat only when players provably cannot enter, score or claim on prod even after a restart." |

Explicit option inventory: The prompt has no candidate option list.
Inventory evidence: P (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/04\_Prompt.txt): "Can you take it on for me?"

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: G
Resolution: EXCLUDED. A week that does not start cannot be entered, and the player stays in last week after two restarts on two devices. That is not a reset that needs a restart. The word still ties it to ZOM-429, where the symptom includes the claim. It is newer than Douglas Sep 16, and no later record disputes it.
Resolution evidence: VP (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql pointer slack\_messages b5f2955c2e154efc6835946ecfe1758e): "it still does not start a new week. I killed the app and reopened it twice, played a few levels, and my week is still last week one. Same on the second device."; Z429 (/Users/sumit/Source/OC/Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer issues ZOM-429 description): "When the weekly leaderboard is ended, it doesn't start the new one or let me claim my rewards."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Held against not held. |
| writes | DIFFERENT | Reading G drops the ZOM-429 note. |
| destinations | DIFFERENT | Reading G drops ZOM-429. |
| contents | SAME | Same Still to do and windows apart from the status. |

Authority chain: P → BR\_HOLD → VP

Resolution relevance challenge: The quote states the failure after restart on prod. It does not use the rule verbs, so this kill rests on plain meaning; that is recorded as the thinnest kill.
Delegation challenge: NOT_CLAIMED. No materially different call is delegated.
Challenge evidence: VP (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql pointer slack\_messages b5f2955c2e154efc6835946ecfe1758e): "it still does not start a new week. I killed the app and reopened it twice, played a few levels, and my week is still last week one. Same on the second device."; Z429 (/Users/sumit/Source/OC/Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer issues ZOM-429 description): "When the weekly leaderboard is ended, it doesn't start the new one or let me claim my rewards."

Compared alternative: D
Resolution: EXCLUDED. The prompt delegates the whole job and points to the brief, and the brief states this write. Brian names the same place.
Resolution evidence: BR\_LOCK (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql): "A committed date that misses the lock moves to any time before it and you tell its owner in a reply on the mail where they committed to it."; P (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/04\_Prompt.txt): "Can you take it on for me?"; BF26B (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql): "If the new date is a problem on your side, reply on this mail."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same. |
| writes | DIFFERENT | Reading D drops the reply. |
| destinations | DIFFERENT | Reading D drops the mail thread. |
| contents | SAME | Same cells. |

Authority chain: P → BR\_LOCK

Resolution relevance challenge: The rule is explicit that the owner is told in a reply. Take it on for me hands that to the Agent.
Delegation challenge: NOT_CLAIMED. No materially different call is delegated.
Challenge evidence: BR\_LOCK (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql): "A committed date that misses the lock moves to any time before it and you tell its owner in a reply on the mail where they committed to it."

Compared alternative: B
Resolution: EXCLUDED. Brian, who is not the assignee, states on Sep 30 that the icon must land before the event runs. That closes the gap the owner note left.
Resolution evidence: BZ (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql pointer linear\_comments cmt\_zom465\_3): "the Collect &amp; Win icon does have to land before the event runs"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same. |
| writes | SAME | Same. |
| destinations | SAME | Same. |
| contents | DIFFERENT | One item and owner in one cell. |

Authority chain: P → BR\_STILL → BZ

Resolution relevance challenge: The quote answers the exact open question: must this item land before the event runs.
Delegation challenge: NOT_CLAIMED. No materially different call is delegated.
Challenge evidence: BZ (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql pointer linear\_comments cmt\_zom465\_3): "the Collect &amp; Win icon does have to land before the event runs"

Compared alternative: C
Resolution: EXCLUDED. The clip rule makes the running October season a window inside the span that starts Oct 6 00:00 UTC, so it is the first window. Oct 1 and Nov 1 both fall away.
Resolution evidence: BR\_CLIP (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql): "Clip anything that starts before or runs past that to those two instants."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same. |
| writes | SAME | Same. |
| destinations | SAME | Same. |
| contents | DIFFERENT | One date in one cell. |

Authority chain: P → BR\_CLIP

Resolution relevance challenge: The rule states what happens to anything that starts before the span.
Delegation challenge: NOT_CLAIMED. No materially different call is delegated.
Challenge evidence: BR\_CLIP (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql): "Clip anything that starts before or runs past that to those two instants."

Compared alternative: E
Resolution: AUTHORIZED_VARIATION. The brief accepts any time before the lock, so both dates are valid.
Resolution evidence: BR\_LOCK (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql): "moves to any time before it"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same. |
| writes | SAME | Same. |
| destinations | SAME | Same. |
| contents | DIFFERENT | The moved date differs inside the boundary. |

Authority chain: P → BR\_LOCK
Authority kind: OBJECTIVE_ACCEPTANCE_BOUNDARY
Acceptance boundary: Any instant before Oct 31 00:00 UTC, the lock 24h before the Nov 1 00:00 UTC open.
Acceptance for A: Thu Oct 30 is before the lock.
Acceptance for E: Wed Oct 29 is before the lock.

Resolution relevance challenge: The rule names the boundary itself.
Delegation challenge: EXPLICIT_AUTHORITY. The words any time before it authorize every date in the boundary.
Challenge evidence: BR\_LOCK (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql): "moves to any time before it"

Compared alternative: F
Resolution: EXCLUDED. The rule names the weekly windows and makes the daily reset a note.
Resolution evidence: BR\_ENDLESS (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql): "Endless goes down as its weekly windows, with the daily reset noted."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same. |
| writes | SAME | Same. |
| destinations | SAME | Same. |
| contents | DIFFERENT | The Endless Windows cell differs. |

Authority chain: P → BR\_ENDLESS

Resolution relevance challenge: The sentence answers the exact cell.
Delegation challenge: NOT_CLAIMED. No materially different call is delegated.
Challenge evidence: BR\_ENDLESS (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql): "Endless goes down as its weekly windows, with the daily reset noted."

Strongest-alternative challenge (G): G is not a strawman: Vincent does not use the rule verbs and one tester reported it. It fails on his two restarts, two devices and the word still against ZOM-429.
Challenge evidence: VP (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev14/inputs/01\_Universe\_Inject.sql pointer slack\_messages b5f2955c2e154efc6835946ecfe1758e): "it still does not start a new week. I killed the app and reopened it twice, played a few levels, and my week is still last week one. Same on the second device."; Z429 (/Users/sumit/Source/OC/Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer issues ZOM-429 description): "When the weekly leaderboard is ended, it doesn't start the new one or let me claim my rewards."

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

#### Decision sweep

Basis labels: RECORD, SCOPE_GAP, SILENCE. "Rule" means Frederick's message, reply or brief.

**Beats**

| Item | Outcome | Basis | Settled by |
|---|---|---|---|
| Collect & Win | In, late start, not held. First window Fri Oct 10 00:00 UTC. Windows: Oct 10-12, then each Mon-Tue, Wed-Thu, Fri-Sun, last Oct 31 00:00 to Nov 2 23:59 UTC. W1 (from Oct 10) to W4 | RECORD | Rule "starts late, it is not held"; rc_10 "still on the DEV stack only"; cmt_zom563_1 "wait for the Oct 8 release"; GCal 2025-10-08 15:00Z. Wed window opened 00:00 UTC, before the release |
| Plague Race | In, W1 to W4, no dates | RECORD | Rule; rc_10 "already running on prod" |
| Weekly Leaderboard (leagues) | Held until the fix is confirmed on prod. Keeps Mon 00:00 to Sun 23:59 UTC windows and W1 to W4, marked held | RECORD | Vincent Sep 30 meets the hold test and is newer than Douglas Sep 16; rule "keeps its usual windows and weeks"; CDK `LEAGUES_SCHEDULE` "0 0 * * 1" via `github_get_file_contents` |
| Endless Monster Mode | In, W1 to W4. Four weekly windows Mon 00:00 to Sun 23:59 UTC, daily 00:00 UTC reset noted | RECORD | Rule "Endless goes down as its weekly windows, with the daily reset noted."; Confluence "daily reset 00:00 UTC, weekly reset Monday 00:00 UTC" |
| Season Pass | In. First window Oct 6 00:00 UTC. Windows Oct 6 00:00 to Oct 31 23:59 UTC and Nov 1 00:00 to Nov 2 23:59 UTC | RECORD | Rule "Clip anything that starts before or runs past that to those two instants."; "closing 23:59 UTC on its last day"; rc_1 October range; Brian Nov 1 |
| Quest rollover | In, W1 to W4, no dates | RECORD | ZOM-534 Leonard (reporter) "it is good on prod now" |
| Daily gift | In, W1 to W4, no dates | RECORD | ZOM-556 Vincent "claiming works and nothing is lost"; rule "Wrong counters ... do not hold" |
| Boss Arena | Off | RECORD | Rule |
| Rotating shop | Off | RECORD | Rule "the rotating shop is not a beat" |
| Zombie Lane | Off | RECORD | Reply "keep Zombie Lane off the calendar" |
| Halloween one-off | Off | RECORD | Robert Sep 30 "pulling my ok. Take it off the beta calendar"; rule "his later word is the one that counts" |
| Desert and Port themes | Not beats | RECORD | Robert Sep 30 "nothing waits on new themes" |

**Push rows (PNs Beta, sheet row number)**

| Row | Item | Status / Live col | Outcome, what is missing | Basis | Settled by |
|---|---|---|---|---|---|
| 2 | Quests | Not Ready / LIVE | Hold: Ready | RECORD | Rule |
| 3 | Hourly Coins | Not Ready / LIVE | Left off | RECORD | Reply |
| 4 | Lives recharged | Ready / LIVE | Send, no game name | RECORD | Reply "fine to go out" |
| 5 | 1 day lapsed | Ready / LIVE | Hold: game name (copy says Puzzles vs Zombies) | RECORD | Rule; spec rename 24 July 2025 |
| 6 | 7 days lapsed | Ready / LIVE | Send | RECORD | Reply |
| 7 | FTUE | Ready / LIVE | Hold: game name (Puzzles vs Zombies) | RECORD | Rule |
| 8 | Win & Collect | Not Ready / WIP | Hold: Ready, LIVE, event name | RECORD | Rule; Confluence "under a different name" |
| 9 | Nathan's Treasure Hunt | Not Ready / WIP | Left off | RECORD | Reply |
| 10 | Plague Race | Ready / WIP | Hold: LIVE | RECORD | Rule |
| 11 | Streak Fever | Not Ready / WIP | Left off | RECORD | Reply |
| 12 | Axe Arena | Not Ready / WIP | Left off | RECORD | Reply |
| 13 | Login Calendar | Not Ready / WIP | Hold: Ready, LIVE | RECORD | Rule "(Login Calendar and Weekly Rankings are fine)" |
| 14 | Season Pass | Not Ready / WIP | Hold: Ready, LIVE | RECORD | Rule |
| 15 | Weekly Leaderboard | Ready / WIP | Hold: LIVE | RECORD | Rule |

**Still-to-do candidates flagged since the brief (created Sep 24 17:15 UTC)**

| Item | Outcome | Basis | Settled by |
|---|---|---|---|
| Collect & Win prod deploy | In, Douglas | RECORD | rc_10; GCal organizer douglas@; cmt_zom563_1 |
| Final vial models | In, Claire | RECORD | Arthur rc_38 "still need their final models before the event runs" |
| Collect & Win event icon animation | In, Marcus | RECORD | Brian cmt_zom465_3 "does have to land before the event runs". Brian is not the assignee |
| Collect & Win reward tables | Out | SCOPE_GAP, no cell | Douglas, the person asked: "Both tables are updated." Only his word, so not RECORD under the owner-claim rule. No cell: the only record on it says done, and request and answer sit in one thread in #zm-collect-win, which Julia is not in. Portal L409 treats that channel as not visible to her |
| Weekly Leaderboard fix | In, Douglas | RECORD | Rule "its fix if it is held"; ZOM-429 assignee |
| November config | In, Brian, moved to any time before Oct 31 00:00 UTC | RECORD | Spec "locked 24h before each season opens"; Oct 31 10:00 Istanbul is 07:00 UTC, a miss; rule "any time before it" |
| Premium strip art | In, Oliver | RECORD | Arthur rc_1 |
| Daily gift frame ZOM-432 | Out, shipped | RECORD | Samuel; #471 commit "Fixing UI Elements on Daily Gift"; builds #50 and #135 in #builds Sep 30 |
| Quests more content, Trello #61 | Out | RECORD | Closed-list rule: no post-brief flag says "still needed". Leonard's note says "The weekly rollover does not wait on them". Relabelled from SCOPE_GAP: the kill is the rule, not his word |
| lightSweep box | Out | RECORD | Vincent (reporter) "nothing has to land for the beta" |
| Airstrike freeze | Out, unverified | RECORD | Leonard (reporter) "Could not get it to freeze" |
| ZOM-526 token travel | Out | RECORD | Brian; #472 merged; rest waits on Axe Arena |
| ZOM-565 Endless VFX | Out | RECORD | Brian "do not have to land before the beta" |
| ZOM-566 and PR #477 | Out | RECORD | Rule "not analytics"; Brian on the header and info text |
| ZOM-552, 442, 549, 548 | Out | RECORD | Rule "not analytics" |
| ZOM-543 queue manager | Out | RECORD | Not deploy, config or art; #472 merged |
| ZOM-521, 528, 541 card VFX | Out | RECORD | Card pack is not a beat |
| Collect & Win Bug_Checklist canvas (8 open items) | Out | RECORD | Vincent "none of them blockers and doesn't affect the submission" |
| Marcus particles note Sep 24 16:58 UTC | Out | RECORD | Predates the brief's created time |
| Store approval of Sep 30 builds | Out | RECORD | Deck dated Sep 23, not flagged since the brief |

Julia's mail: 287 threads scanned by subject for Aug and Sep 2025; only Brian's two mails carry a config commitment.

**Open PRs:** #477 analytics, out. #476 vision bot, not a beat. match3d-backend#34 draft, no review. auth-game-backend#2 and game-of-dominoes-backend#79, not ZM3D beats. **Change-request rule:** all 74 CHANGES_REQUESTED reviews checked; latest are match3d-backend#4 (June) and match3d#303 (July), none on or after Aug 1, so no beat holds under it. The undefined "Aug-Sep live-ops cohort" changes nothing.

**Writes and destinations**

| Item | Outcome | Basis | Settled by |
|---|---|---|---|
| Sheet | ZM3D Beta Live-Ops Calendar, tabs Calendar and Pushes | RECORD | DM "the calendar sheet in your ZM Live Ops folder" |
| Calendar ticket | ZOM-78, not ENG-2240 | RECORD | cmt_zom78_1 |
| Held-beat note | ZOM-429 only. A held push is not a held beat | RECORD | Rule "Hold a beat only when players provably cannot enter, score or claim" |
| Recommendation | DM D05SD5QLG94 | RECORD | DM "back here" |
| Brian reply | Sep 26 mail, in scope | RECORD | Rule; prompt "Can you take it on for me?"; Brian "reply on this mail" |
| New date | Any instant before Oct 31 00:00 UTC | RECORD, objective boundary | Rule "any time before it". Later rubric must not lock one date |

The full fork list, with every fork raised on any hash, is in `## Deep Recheck`.

---

**Feasibility:** PASS (5). Every write has a cataloged operation; all facts exist. No per-X breakdown. Numeric asks are dates only; catalog has no return schemas, so rendering is an evidence limit, not a defect.

**Persona ACL Reachability:** PASS (5). Lens 1: DM, Robert DM, #zombie-match3d, #zombie-bugs, #zombie-art by membership; brief and deck by reader share; `Push Notifications Zombie Match` by share; Julia's sheet by ownership; mail by her mailbox copies; release event on her calendar. GitHub, Linear, Trello, Confluence unscoped. #zombie-prs and #zm-collect-win need no read. Lens 2: no ask directs an out-of-view read. No required record is hidden.

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

**Tool Use & Cross-service:** PASS (5). Trello is a decoy, not required. Graded fact per service: GitHub (which windows are on prod, vial and strip items), GCal (release instant, so Oct 10), Gmail (Oct 31 commitment), Confluence (24h lock, Endless resets), GSheets (push rows), Slack (Leaderboard hold, Halloween pull), Linear (owners, icon item, ZOM-78). Dropping any changes an answer.

**Investigation + Action:** PASS (5). Writes depend on findings.

**Clarity:** PASS (5). Intent is clear, no "I'll" statement exists, and the write-action test gives one set. "you tell its owner" closes the last write split. Top level or in thread in the DM is the same recipient and the same write.

**Contrived:** PASS (5). All Eval 2.7 indicators No. The destination and recipient are named; a single "If" is not an if-chain; "If a beat ends up held" does not point at which beat.

**Alignment with Today's Date:** PASS (5). All relative words resolve; future dates are treated as future.

**Originality:** N/A, no samples supplied.

---

### Phase 3: Universe Feasibility

**Data Existence:** PASS (5). 7 of 7 premises plus all sweep records. All retrievable via cataloged tools. Linear comments exist only through the SQL (base `comments` is empty); `linear_list_comments` is cataloged.

**Cross-Service Coherence:** PASS (5).

| # | Status on edae63f3 | Evidence | Scored? |
|---|---|---|---|
| C1 (SC-13) | Present | SQL Trello action `"name":"BETA: Sep 30"` against list record `BETA: Oct 10`. The action agrees with 67 base actions; the odd one out is the base list record. The answer reads the comment text, never the list name | No |
| C2 (SC-62) | Present | Confluence "re-imported from Google Sheets hourly in production" against CDK `IMPORT_REWARDS_SCHEDULE ... "*/5 * * * *"`. No graded fact touches it | No |
| C3 | Fixed | Slide 2 "any scale-up comes after the pivot call" agrees with slide 3 | Closed |

**What this score relies on.**
- It does not rest on Eval 1's text. Eval 1 has no sentence saying a base issue that changes no task value is unscored.
- `base-data-v1`, the label the Portal cites, is not in the local bundle (no hit under Evals/). I have seen only the six lines of the Portal report for this task that I was cleared to open: L323, L334, L362, L405 to L409.
- Those lines score these same two items: "SC-13/18/22/38/62 not task-dependent", and "No graded value depends on the list name".
- The coordinator reports that the Portal failed an earlier round on SC-15 because it touched the task. L362 says "SC-15 fixed"; I saw nothing further on that.
- The local known-issues README agrees on direction: its cards are "do not grade, do not depend on". Eval 1 STEP 0.5 uses the same test for Eval 0 findings.
- I weigh the Portal's result on the same two items in the same task as the best evidence of the gate that will actually apply, so I score 5.

**If a reviewer reads §3.2 alone.** §3.2 fails on presence, "whether or not the contributor introduced it". C2 touches Confluence, which the QC form names as synthetic data, so it counts: one low-impact item, NON-FAIL 3. C1 is Trello, outside that synthetic list, but §3.2's SQL bullet ("no injected record contradicts established base data") can reach it. If it counts too, that is two low-impact items: FAIL 2. So §3.2 alone gives 3 or 2, and the overall verdict becomes NON-FAIL 3 or FAIL 2. My earlier note said 2 flat; I had not yet weighed the QC form's synthetic-data line.

Changed records checked for new inconsistencies, none found:
- Brief row on this hash: offsets, no stale "its owner is told", Doc and Drive rows unchanged.
- Douglas reply: author in channel, parent id, `thread_ts_legacy`, reply_count 2 to 3, reply_users 1 to 2, ts matches created_at. SC-57 touched, no posting graded.
- cmt_zom465_3: sequence 3, follows 18:05:02, `updated_at` raised to match, and "the master VFX list was ticked" agrees with the ZOM-521 `[X]` icon line.
- cmt_zom563_1 and _2: sequence, 18:17:05 follows `started_at` 18:14 and the base DM at 18:16; closing comment matches `completed_at`.
- ZOM-542 Todo fits its comment. rc_38 and rc_1 match their Slack mirrors. Brief `style_runs` land on all nine headings.

Other known cards touched, no task value changed: SC-15 and SC-16 (repaired by the SQL, not graded), SC-18 (#477 is out as analytics), SC-38 (lock only is read from the spec).

Noted, not scored: `PNs Beta` Status and Live columns disagree on sight (Not Ready / LIVE), but the brief treats them as two axes, so this is designed friction. #468 timeline ev_6 sits after `closed` with a null date; SQL-made, changes no value, stays with Eval 0.
- Injection SQL considered: Yes. Static integrity: Eval 0 PASS on this hash, plus direct task-relevant checks. Sources, access and configuration: supported.

| Prompt ask / source | Static evidence | Discovery/access | Task coherence |
|---|---|---|---|
| Calendar and pushes | NEW | Supported | PASS |
| Ticket note, link | NEW | Supported | PASS |
| Recommendation, Brian reply | NEW | Supported | PASS |

---

### Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score | Justification |
|---|---|---|---|
| Prompt | Unique Ground Truth | 5 | Every fork settled by a quoted rule or record; thinnest kill is the Weekly Leaderboard hold |
| Prompt | Feasibility | 5 | All asks doable |
| Prompt | Persona ACL Reachability | 5 | All required reads visible |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 5 | One write set |
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
| Universe | Cross-Service Coherence | 5 | SC-13 and SC-62 present, not task-dependent; 3 or 2 if §3.2 is read alone |

---

### Issues Found

No fail-level issue.

| # | Issue | Severity | Dimension |
|---|---|---|---|
| 1 | SC-13 and SC-62 are present. The 5 rests on Portal practice, not Eval 1 text | Decides the verdict if a reviewer reads §3.2 alone | Cross-Service Coherence |
| 2 | Vincent's retest does not use the rule's verbs, so the hold rests on plain meaning | Minor; would be fail-level if a reviewer rejects the kill, since it flips the status and the ZOM-429 write | Unique Ground Truth |
| 3 | ZOM-344 Done against later quest-chest timing complaints (Eval 0 ADV-2) | Advisory | Injection Gate |

P4's extended items: none is scorable. §2.7 and §1.2 test prompt wording; §2.7 itself says "A per-case rule belongs in a seeded record, not in the prompt"; deep_recheck says the persona's own style "is not a standard"; Eval 0 leaves voice out and no record speaks to a solver or grader. I also tested §1.2's "instructions or context rather than a precomputed answer": the brief gives rules, not cell answers. Exposure remains if a reviewer extends these tests to records. The sharpest are DR2 (a Sep 24 rule that foretells the reversal), DR19 (Brian's comment states the answer), DR3 (one refrain across 4 authors) and DR4 (audit vocabulary, undefined "cohort").

### Recommended Improvements

All optional; none is needed for this verdict. Any SQL edit changes the hash and needs a rerun of Eval 0 and the affected phases.

1. Issue 2: name the verb in Vincent's Sep 30 post. For example end it "...my week is still last week one, so I cannot get into this week or claim last week's rewards." Checked: "claim" and "rewards" come from ZOM-429's description; no value, id or new lock-in is added.
2. Issue 1: moving Leonard's rollover note off Trello card 61 to a surface with no list-name field removes SC-13 from the task. SC-62 is base data and stays.
3. Issue 3: Eval 0's fix for ADV-2, a sentence on L213 separating art sign-off from claim timing.
4. For OE and rubric: accept any handoff time before Oct 31 00:00 UTC; require no window dates for quests, daily gift and Plague Race; strip art needs-by is "before that season opens"; accept PT renderings of the same instant.

### Evidence limits
Evals/Docs PDFs and the Example Task were not readable here, so Phase 0.3 calibration did not run; every scored rule was applied from Eval 1, scoring.json and the QC form, so no scored check is left open. Runtime visibility of non-member public Slack channels is unverified; no required record depends on it. Tool return shapes and live writes are not proven by local reads. Art sprites are LFS pointers and could not be viewed. `review_context_sha256` is null and full `validate_record` did not run, because `start` is out of bounds; the UGT object passed `hg_prompt_ugt.validate_review` read-only with a local context. Outputs were written under R14/out, not through `hg_write_output.py`.

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
| ZOM-348 | Todo | none | Rotating Shop Discount Issues | Rotating shop, not a beat |
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
| ZOM-465 | In Progress | marcus.bennett | Endless Mode Master VFX Ticket | Icon animation in, Marcus (RECORD, Brian) |
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
| ZOM-542 | Todo | samuel.turner | Update home screen and victory score screen for game | Out, not flagged since brief |
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

---

## Deep Recheck

Passes: P1g, P1h, P2e, P3, P4, each a fresh agent blind to this main review. Model and effort are not stated in the pass files.

Which pass ran on which hash:
- **edae63f3 (this SQL):** Eval 0 (final), P1g (delta rerun, not a full scan), P1h (cold full pass), P2e (delta plus carry-over of byte-identical rows from its rev13 result), P3 (records reopened), P4.
- **1f2175a2:** P1e, P1g, P2d, P2e. **Rev12 SQL:** P1c, P1d, P1e, P1f, P2c, P2d. **1348d287 (rev11):** P1a, P1b, P2a, P2b. **ffbac458 (rev10):** P1a, P1b, P1c, P2a, P2b. Forks they raised were rechecked against this hash; none is carried on trust.
- **Main review:** ffbac458, then 1f2175a2, then the two-sentence delta to edae63f3. Lint on edae63f3: 0 FAIL, 0 CHECK.
- Disclosure: P1g and P2e each report one early read of review_rev13 inputs before reading the folder limit. Neither opened another reviewer's work.
- Disclosure, main review: my review_rev13 draft file carried the wrong head section. A shared work folder held a same-named file from another reviewer, and my script read it. Its sweep, scores and UGT section were mine. This report is rebuilt from my own head in the review_rev10 draft, so nothing from that file is in it.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1g | 46 sentences, 7 beats, 14 push rows, 6 writes | 0 | 0 |
| P1h | 46 sentences, 34 fork candidates | 0, with 5 weakest kills for re-judging | 0 |
| P2e | 6 prompt sentences, 111 SQL statements | 6 advisory | 6 as advisory, none scored |
| P3 | 6 sentences, 16 premises | 0, with 2 advisories | 2 as advisory, none scored |
| P4 | 6 prompt sentences | 0 on the prompt | 0 |
| P4 extended | 29 brief sentences, 121 record sentences | 24 exposure items | 0 scorable |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| W1 | P1h | "If a beat ends up held, leave a note on its ticket so the owner picks it up." | Vincent b5f2955c; ZOM-429 | §2 which items | Unique Ground Truth | REJECTED | Reading B (nothing held) ruled out by "it still does not start a new week. I killed the app and reopened it twice, played a few levels, and my week is still last week one. Same on the second device." with ZOM-429 "it doesn't start the new one or let me claim my rewards". "a reset that needs a restart" cannot apply after two restarts. Thinnest kill in the set, see Issues |
| W2 | P1h | "What he wants in it is in his message" | Trello card 61 action 68dac820 | §2 which items | Unique Ground Truth | REJECTED | Brief: "anything flagged since this brief as still needed ... Nothing else goes in". The only post-brief note says "The weekly rollover does not wait on them". The kill is the closed list, not Leonard's word |
| W3 | P1h | "his working rules for building it are in the brief" | github reviews, 74 CHANGES_REQUESTED | §2 which items | Unique Ground Truth | REJECTED | Opened: latest are match3d#303 (2025-07-16) and match3d-backend#4 (June). No qualifying review, so every definition of "cohort" gives no hold |
| W4 | P1h | "Can you take it on for me?" | Brief Config locks | §2 what gets written | Clarity | REJECTED | "you tell its owner in a reply on the mail where they committed to it." The prompt's list has no "only" |
| W5 | P1h | "the four buy weeks that start Monday the 6th" | CDK `LEAGUES_SCHEDULE` | §2 which date | Feasibility | REJECTED | "A held beat keeps its usual windows and weeks on its row, marked held."; CDK "PROD: every monday at 00:00 AM UTC"; `github_get_file_contents` is cataloged and GitHub is unscoped |
| P2-DR1 | P2e | "his working rules for building it are in the brief he shared with me" | GCal Oct 8; gdocs f_b7aae618602a7ccc0cc9a7 "it needs to be deployed to pro servers" | §3.2 | Cross-Service Coherence | CONFIRMED, advisory | Opened. A Sep 29 plan in Leonard's private doc (`shared_with_emails` empty); not a fact, not persona-visible, no graded value |
| P2-DR2 | P2e | "What he wants in it is in his message" | #472 rc_1 | Data exists | Data Exists | CONFIRMED, advisory | Opened; `git grep` finds no date text in the Season Pass prefabs. Single-source claim that nothing contradicts; Arthur is a third party |
| P2-DR3 | P2e | "What he wants in it is in his message" | #468 rc_38; CollectAndWinItem.asset | §3.2 | Cross-Service Coherence | CONFIRMED, advisory | Opened: `IsProductionObject: 1`. That flag does not say the models are final |
| P2-DR4 | P2e | "his working rules for building it are in the brief" | Brief hold rule; reviews | Data exists | Data Exists | CONFIRMED, advisory | Same as W3; the clause never fires |
| P2-DR5 | P2e | "live-ops and push calendar" | Snowflake push stats `event_live` | §3.2 | Cross-Service Coherence | CONFIRMED, advisory | Rows exist. Reply pins the source: "plan the PNs Beta tab as it stands" |
| P2-DR6 | P2e | "link it on the calendar ticket" | #468 ev_6 | §3.2 | Cross-Service Coherence | CONFIRMED, advisory | Id order only; dates correct; nothing graded reads it |
| P3-A1 | P3 | none | 13 columns missing from the snapshot | SQL hygiene | Injection schema | CONFIRMED, advisory | Same as Eval 0 ADV-13; snapshot is unverified |
| P3-A2 | P3 | none | L35 in #zm-collect-win | SQL hygiene | Persona access | CONFIRMED, advisory | Julia is not a member. Request and reply share the thread, so no cell depends on it |
| ADV-2 | Eval 0 | none | cmt_zom344_1 Done against Vincent 09-30 "the timing is off. Especially in the quest chests." | §3.2 | Cross-Service Coherence | CONFIRMED, advisory | Opened, including Marcus's DMs (Julia not in them). Eval 1 STEP 0.5 keeps it in the gate: it changes no value, set, order, recipient or destination. Art sign-off and claim timing are different scopes |
| SC-13 | P2e, P3, main | "What he wants in it is in his message" | SQL action "BETA: Sep 30"; list record "BETA: Oct 10" | §3.2 | Cross-Service Coherence | CONFIRMED present, not scored | Portal L407 "No graded value depends on the list name" |
| SC-62 | main | "What he wants in it is in his message" | Confluence "hourly"; CDK `*/5` | §3.2 | Cross-Service Coherence | CONFIRMED present, not scored | Portal L323, L406; the task uses the 24h lock only |
| M1 | main | none | Same POD doc: "I think could I also requested to update some rewards? I'm not sure if you already taken care of that." | §3.2 | Cross-Service Coherence | CONFIRMED, advisory | Found here. P2e read this transcript as fitting Douglas's reply; it sits oddly three days after "Both tables are updated." It may be a different request. Private doc, no graded value |
| P4-DR2 | P4 | B19: "only with the latest dated approval from Product, and if he takes that back his later wor | Brief f_7c3e91a4… (SQL l.121), dated Sep 24, six days before | §2.7 trap hint, riddle | Contrived / Unnatural | REJECTED | A precedence rule in a rules doc, stated openly; §2.7 places per-case rules in seeded records |
| P4-DR3 | P4 | "Parking it, nothing here has to land for the beta." (cmt_zom471_1, Sep 17) | "has/have to land" sits in 7 comments by 4 authors: slack a0 | Planted-record test | Contrived / Unnatural | REJECTED | Repeated phrase across records; realism is outside Eval 0 and P4 |
| P4-DR4 | P4 | B15-B16: "a change request outside the Aug-Sep live-ops cohort"; "An unresolved change-request  | SQL l.119. The vocabulary matches FAIL example #43 in §2.7 ( | §2.7 audit form | Contrived / Unnatural | REJECTED | §2.7 audit form tests the prompt; the clause never fires |
| P4-DR19 | P4 | "Marcus, the Collect & Win icon does have to land before the event runs, it is the one event ic | cmt_zom465_3 (SQL l.210), 8 minutes after Marcus's note, whi | Planted-record test | Contrived / Unnatural | REJECTED | A third-party fact record; it is what closes F5. Voice is not scored |
| P4-DR5 | P4 | B5: "A PT/PDT rendering of the same instant is fine, a different instant is not." | SQL l.113. Reads as a rubric tolerance clause. deep_recheck  | §1.2 voice; Eval 0 close | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |
| P4-DR6 | P4 | B12: "put down whether the beat is in, which weeks it runs and whether its push goes out, not i | SQL l.117. Cuts against F2 ("which windows it runs in") for  | §2.7 | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |
| P4-DR7 | P4 | B25-B26: "before its lock"; "in a reply on the mail where they committed to it." | SQL l.127. "Its lock" is never defined in the brief; only Co | §2.7 hidden destination, | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |
| P4-DR8 | P4 | B13, B15: "even after a restart"; "a reset that needs a restart" | The rule's dividing line matches Vincent's post exactly: "I  | §2.7 trap hint | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |
| P4-DR9 | P4 | "The Plague Race, leagues, Endless and Season Pass schedules are already running on prod."; "Fi | match3d#470 rc_10 (SQL l.154) sits on CollectAndWinMainScree | Planted-record test | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |
| P4-DR10 | P4 | "That was my report, it is good on prod now." | cmt_zom534_2 (SQL l.198). ZOM-534's description already show | Eval 0 closest quote | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |
| P4-DR11 | P4 | "The weekly rollover does not wait on them, the current quests keep running either way." | Trello action 68dac820… (SQL l.259), on a card with 0 commen | Planted-record test | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |
| P4-DR12 | P4 | "Let us use this ticket…"; "we are not spending art time" | Whole SQL: 0 contractions and 46 uncontracted forms across 5 | §1.2 voice | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |
| P4-DR18 | P4 | B26: "moves to any time before it" | SQL l.127. Reads as an acceptance range: a founder moving a  | §1.2 voice; Eval 0 close | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |
| P4-DR20 | P4 | B3a: "Clip anything that starts before or runs past that to those two instants." | SQL l.113. Closes an edge-value fork. "clip" in Frederick's  | §1.2 voice | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |
| P4-DR22 | P4 | B22: "(Login Calendar and Weekly Rankings are fine)"; B23: "with which of those its row is miss | SQL l.125. These are exact strings from two row copies on PN | §2.7 trap hint; Eval 0 c | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |
| P4-DR23 | P4 | "That update carried only these, the Collect & Win server windows wait for the Oct 8 release." | cmt_zom563_1 (SQL l.255), on a teams bug ticket with no ment | Planted-record test | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |
| P4-DR1 | P4 | "Coming back on the themed prop set I okayed in Martin's thread: pulling my ok." | Slack D05GU6L0XFH id 669d15f6… (SQL l.17). Volunteered in a  | §2.7 trap hint | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |
| P4-DR13 | P4 | R2-R5: "as it stands, one line per row"; "just those four"; "Copy that does not name the game a | SQL l.13. Nobody asked any of this. R4 narrows his own B22 u | Planted-record test | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |
| P4-DR15 | P4 | B9-B10: "the backend release instant read in UTC, not when its client PRs merged"; "starts late | SQL l.117. A generic rule with one case, Collect & Win (#470 | §2.7 | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |
| P4-DR16 | P4 | B2: "The rules stay here; the calls are yours."; B14: "An established failure holds it; an unve | Balanced aphorisms. "provably" (B13): 0 of 610,468. Semicolo | §1.2 voice | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |
| P4-DR17 | P4 | Collection level | Base Linear has 0 comments on 3,687 issues, so all 32 commen | Planted-record test | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |
| P4-DR21 | P4 | B17a: "A held beat keeps its usual windows and weeks on its row, marked held." | SQL l.119. A layout rule for the sheet, in plain words. | §1.2 voice | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |
| P4-DR24 | P4 | B8: "and the rotating shop is not a beat." | SQL l.115. Tacked onto an unrelated Boss Arena sentence. "ro | §1.2 voice, bolt-on form | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |
| P4-DR25 | P4 | B6a: "Endless goes down as its weekly windows, with the daily reset noted." | SQL l.113, new this round. Plain and grounded: Confluence /p | §1.2 voice | Contrived / Unnatural | REJECTED | Tests record voice, not prompt wording; §2.7 and deep_recheck P4 do not reach it |

Effect on verdict: Unique Ground Truth and Clarity move to 5 on this SQL; no dimension moved down. No fail-level finding is confirmed.

Forks: none open. No both-fair figure remains: the Season Pass date was one on ffbac458, and the clip rule settles it now.

- F1: Weekly Leaderboard held | Held | Nothing held | Settled by: "it still does not start a new week. I killed the app and reopened it twice, played a few levels, and my week is still last week one. Same on the second device."; ZOM-429 "it doesn't start the new one or let me claim my rewards"
- F2: Reply to Brian | Send it | No mail, flag only | Settled by: "you tell its owner in a reply on the mail where they committed to it."
- F3: Brian's moved date | Thu Oct 30 | Wed Oct 29, or the lock itself | Settled by: "moves to any time before it" (all accepted)
- F4: Endless Windows cell | Four weekly windows | 28 daily windows | Settled by: "Endless goes down as its weekly windows, with the daily reset noted."
- F5: C&W icon animation | In, Marcus | Out as polish | Settled by: "the Collect & Win icon does have to land before the event runs"
- F6: Season Pass First window | Oct 6 00:00 UTC | Oct 1 or Nov 1 | Settled by: "Clip anything that starts before or runs past that to those two instants."
- F7: Window close instants | 23:59 UTC | Next opener 00:00 | Settled by: "closing 23:59 UTC on its last day"
- F8: Held row cells | Usual windows, W1 to W4, marked held | None until fixed | Settled by: "A held beat keeps its usual windows and weeks on its row, marked held."
- F9: Row 13 name | Ready and LIVE only | Plus a rename | Settled by: "(Login Calendar and Weekly Rankings are fine)"
- F10: Row 2 What is missing | Ready | Plus new quests | Settled by: "with which of those its row is missing"
- F11: C&W reward tables | Out | Douglas still to do | Settled by: "Both tables are updated."; channel not visible to Julia (Portal L409)
- F12: UA spend path | Held until the pivot call | Scaled week by week | Settled by: "any scale-up comes after the pivot call"
- F13: Sep 30 prod update carried C&W | No | Yes, so an earlier start | Settled by: "That update carried only these, the Collect & Win server windows wait for the Oct 8 release."
- F14: Rotating shop as a beat | Off | On | Settled by: "the rotating shop is not a beat"
- F15: Quests more content | Out | Still to do | Settled by: "anything flagged since this brief as still needed"; "The weekly rollover does not wait on them"
- F16: C&W first window | Fri Oct 10 | Wed Oct 8 or Thu Oct 9 | Settled by: "the first window that opens after its server windows are live on prod"; "each opening 00:00 UTC"
- F17: Lock instant | Oct 31 00:00 UTC | All of Oct 31 | Settled by: "locked 24h before each season opens"
- F18: Which PNs Beta tab | Zombie Match | Domino Adventure | Settled by: "Ready and LIVE": the Domino tab has no Ready column, opened
- F19: Row 8 event name | Wrong name | Team also says Win & Collect | Settled by: Confluence "Same feature as Win & Collect on Domino Delights, under a different name"
- F20: Leagues and Weekly Leaderboard | One beat | Two beats | Settled by: "The Plague Race, leagues, Endless and Season Pass schedules"; CDK `LEAGUES_SCHEDULE`
- F21: Art gates the C&W start | Oct 10 stands | Start waits for art | Settled by: "A beat starts with the first window that opens after its server windows are live on prod"
- F22: ZOM-521 ticked icon row | Explained | Lifecycle contradiction | Settled by: "the master VFX list was ticked before that event merged"
- F23: Change-request hold | None | A cohort PR holds a beat | Settled by: No CHANGES_REQUESTED after 2025-07-16; opened

Platform defects: PLATFORM: anonymized tokens [PERSON_NAME_2549] and [PERSON_NAME_16313] in PNs Beta are the source strings; not scored.

### FINAL VERDICT: PASS

Score: 5

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), effort not reported by the runtime

Next action: None required for /prompt. If a reviewer reads §3.2 alone, this becomes NON-FAIL 3 or FAIL 2 on SC-62 and SC-13; decide before relying on the 5. Any SQL edit needs Eval 0 and the affected phases rerun.

Evidence limits: `base-data-v1` is not in the local bundle, so the Cross-Service Coherence 5 rests on six lines of the Portal report for this task, not on Eval 1 text. Evals/Docs PDFs and the Example Task were not readable. Non-member public Slack visibility is unverified, with no required record depending on it. `validate_record` did not run; the UGT object was validated read-only. No live tool was run.

**Lowest Dimension:** None below 5. Closest to moving: Cross-Service Coherence - 5 - SC-13 and SC-62 are present and left unscored on Portal practice.

**Summary:** All 18 scored dimensions are 5 and Originality is N/A. Every fork raised on five hashes is settled by a quoted rule or record, and no pass or Eval 0 finding is fail-level. The two soft spots are named above: the Weekly Leaderboard hold rests on the plain meaning of Vincent's retest, and the coherence score depends on the Portal's treatment of known base issues.
