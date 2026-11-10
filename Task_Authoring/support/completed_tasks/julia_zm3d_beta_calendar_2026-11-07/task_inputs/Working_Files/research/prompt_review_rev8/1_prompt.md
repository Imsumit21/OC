## PROMPT EVALUATION REPORT

### Task: ZM3D beta live-ops and push calendar for the four buy weeks, with a run/hold recommendation to Frederick
### Assigned Persona: Julia Lawson - Product Manager (julia_lawson, julia.lawson@harmonygames.co, Product)
### Assigned Business Function: Product
### Assigned Competency: Marketing and GTM
### Assigned Task Skill: Planning and decision support
### Assigned Horizon: long-horizon (Long Horizon)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Eval version: task-quality-v1. Eval release SHA-256: c5b89f4c40a7902f968001f1aa6c710d47bf203842455bbe8dbb668ec7c8943b.
Reviewed prompt SHA-256: 2a23afd87c4ca1b4736385b39bdeb2248119a8f4f33dcd8c3ff9acd8156a2beb (prompt unchanged). Prompt record SHA-256: 1b1b55add5de1e2c4a71925cb8f235319b422d9ff9647aa736269c60b6798863. SQL sha256: 0e8c8ad83f3be435db1f9268f114c916f52293993eb687a55b34005015f9f815 (revision of 091722f6…b876).
`authority_contract: prompt-incorporation-v1`

Final report on SQL 0e8c8ad8…f815, after Eval 0 and the deep recheck. The first draft, on SQL 091722f6…b876, was NON-FAIL 3; the revision closed the one issue behind that score.

---

### Injection Gate
- State: reviewed by a separate independent evaluator on this hash, so the local gate state is equivalent to CURRENT. The store-bound gate helper was not run, by instruction.
- Reviewed SQL sha256: 0e8c8ad83f3be435db1f9268f114c916f52293993eb687a55b34005015f9f815. Eval 0 verdict: PASS, COMPLETE (`injection-static-v2`, delta on 091722f6; 96 statements, lint 0 flags).
- Eval 0 findings on records this prompt depends on: no defects. Each advisory it carried into `/prompt` was tested against the rule that it counts only if it changes a value, set, order, recipient or destination the answer is graded on. None does.

| Eval 0 item | Record | Ruling |
|---|---|---|
| G1 | Premium strip note on #472 | Placement only. Value and owner are the same. Reachable through #472's review comments |
| G2 | ZOM-534 "nothing else has to land" against Vincent's Sep 12 `"0:10:60"` timer error | Hidden DM. Oliver's next message there, three hours later, is "this is fixed", without naming the error; Douglas's "backend timing edge case" also fits it. No change to the set |
| G3 | ZOM-542 stays Regression | Base state. The comment no longer claims the work never reached a build. Decoy ticket |
| F3 | SC-47 Weekly Quests row | Confluence row is Domino Delights. The ZM3D quest beat does not read it |
| A6 | "Product ... he" and Robert | Spec: "Owner: Robert (Product)." Settles the approver |
| A11 | SC-15 repair of ZOM-521 | Not graded; child states and comments agree |
| N6 | ZOM-521 "icons" item ticked against Marcus's Sep 30 note | Marcus explains it: "Collect & Win came in after my note above". His note is newer, so the icon animation stays in the set |
| D5, D7 | ZOM-344, ZOM-432 Done | ZOM-432 is backed by the #471 diff (`img - DailyGift.png`). Both tickets are out of the set either way |
| SC-6, SC-13, SC-38 | Brian's address, list name, Season Pass ship date and analytics | No graded value reads them. My DR5 ruling uses only that the pass shipped, not when |

### Evidence limits
- The guideline PDFs in `Evals/Docs` could not be read: `pypdf`, `pdftotext` and `pdftoppm` are absent and the fonts defeat a stdlib stream read. This covers Prompt Writing, Overall Task Flow, Universe and Tools, Persona ACL Policy, Common Errors, Example Task and Unique_Ground_Truth. `QC_Rating_Form_V12.csv`, `scoring.json`, `common_errors.md`, `acl.md` and Eval 1's own inline rules were read. Phase 0.3 example calibration is the check left without its source.
- The catalog has no return schemas, so rendering of cells, comment lists and review comments is taken from raw records and tool names.
- Dataset similarity library not bundled: Originality is N/A.
- P3 and P4 ran on the previous SQL hash (see Deep Recheck).
- Eval 0's rev7 report was not opened. F3, A6, A11, N6, D5 and D7 were judged from their entries in the rev8 report and the records they name.
- `hg_prompt_checks.py start` and the store-bound writers were not run by instruction. The record was validated with the helpers' read-only functions (source anchors, UGT schema, premise facts).

---

### Revision check (091722f6 to 0e8c8ad8)

Prompt, assignment and date are byte-identical. Statement-level diff: 12 lines removed, 10 added.

| Change | Check | Result |
|---|---|---|
| Brief adds "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date." | Heading style runs shifted by 103; all nine ranges land on their headings | Closes the draft's Clarity issue |
| Sheet gets `web_view_link` `https://drive.google.com/file/d/1oIsTl3jQeyuTuqudrlGaxEze57_FtuiMHX72lDwtDSE/view` | Matches the pattern on 200 of 356 base spreadsheets, including the 44-character id | Consistent; gives the agent a link value for ZOM-78 |
| Premium strip note moves from #473 (post-merge conversation comment) to a review comment on #472 | rev_1 APPROVED 15:52:58Z, same time as the comment; merged 15:53:04Z; `Assets/RewardVFXManager.cs` is in the #472 diff; no base rc on #472 | Consistent; now before the merge |
| #473 comment, timeline event, updated_at bump, Slack mirror and parent update removed | No `#473` reference left in the SQL; base rows stand | Clean |
| New #zombie-prs mirror for #472, parent reply_count 4 | Base count 3, latest_reply unchanged at the merge mirror 1759247586.958099; new ts sits between approved and merged | Consistent |
| ZOM-534 note adds "That is on main, so nothing else has to land for the beta." | Commit 47c65623e7 (2025-09-10) "Using remaining-time endpoint to sync quests end with client"; Oliver: "yeah its on main" | Consistent |
| ZOM-521 note adds ZOM-541 | ZOM-541 In Progress, Calvin | Consistent |
| ZOM-542 note drops "still at the mockup stage" | No conflict with Sep 22 base | Consistent |
| Trello: "The rollover does not wait on them" replaces "Nothing in the beta waits on them" | PN row 2 detail is "Revisit once new quests roll out.", so the old wording overclaimed | Consistent |

Unchanged rows keep the earlier checks. The header comment's "PR bumps" is now stale; it is a SQL comment and no task reads it.

---

### Phase 1: Prompt Structure & Persona

**Persona:** PASS (5)

| Check | Finding |
|---|---|
| Role plausibility | Yes. Confluence Live-Ops Event Calendar: "Daily live-ops pod review. Design, led by Julia Lawson, walks the coming weeks with Frederick Stone". Frederick asks her directly. |
| Voice match | Yes, against the role. Short first-person delegation. |
| Access plausibility | Yes. She is the addressee of the message, a share target of the brief and deck, the sheet owner, and on Brian's mail. |
| Responsibility scope | Yes. The calls are hers: "The rules stay here; the calls are yours." |
| Identity gate | Exact roster match: julia_lawson, julia.lawson@harmonygames.co, Product Manager, Product. |

**Assigned Competency:** PASS. The output is a launch calendar for paid UA weeks, push plan and copy review, and a run/hold call for the buy. That sits inside GTM work even though much of the evidence is engineering state. Not clearly another competency.

**Assigned Task Skill:** PASS. "This goes into the pivot call, so I need your call, not a list of what we have."

**Business Function:** PASS (5), with an overlap note. The label maps to Product & Design. A live-ops calendar also touches Engineering & Live-Ops, but the work is deciding what runs for a beta, not operating or shipping it.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y — PASS
- Ambiguity: which beats exist, which ticket is the calendar ticket, and the lock are all in the environment.
- Dynamic Change: Douglas Sep 16 "they land in the new week fine, so not blocking" is replaced by Vincent Sep 30; Brian Oct 29 is replaced by Oct 31; Robert's Sep 18 approval is withdrawn Sep 30; ZOM-432 opens as a to-do and closes Sep 30.
- Multi-Source: Slack, Docs, Slides, Sheets, GCal, Gmail, GitHub, Linear, Trello, Confluence.
- Data seeding: PASS. 100-word trigger; every rule is in the brief or the thread.

**Naturalness:** PASS

| Red flag | Found? | Quote |
|---|---|---|
| Document formatting | No | Two plain paragraphs |
| Polished connectives | No | None |
| Enumerated deliverable specs or preservation rules | No | Contents are delegated: "What he wants in it is in his message" |
| Even, symmetric sentences | No | Mixed lengths |
| Staged errors | No | Clean typing |

**Anti-Patterns:**

| Pattern | Status | Note |
|---|---|---|
| Command List | PASS | "Once the sheet's done" is a dependency, not a procedure |
| Bolt-On | PASS | Each sentence serves the calendar; removing the hold-note sentence would drop a real write tied to the same decision |
| Pre-Solving | PASS | No cause, beat or date named beyond the buy start |
| Tool Mention | PASS | "sheet", "ticket" are natural; no tool or server names |

**Prompt diversity (1.4):** beyond one Slack post. Six writes in four services.

---

### Requirement Ledger

| # | Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|---|
| R1 | Take on Frederick's ask | SQL rows bca78437… and 890dc27f… | DM history and thread | `slack_conversations_history`, `slack_conversations_replies` | DM member | Scope and exclusions read |
| R2 | Follow working rules | Doc f_7c3e91a4… | Link from message, Drive search | `gdocs_get_document_text` | Shared reader | Rules applied |
| R3 | Every beat players can see | Brief Scope; Confluence calendar; CDK stack; PNs Beta | Docs, Confluence, GitHub | `confluence_get_page`, `github_get_file_contents` | Unscoped | 7 beats |
| R4 | Windows in UTC | Brief; GCal evt_5c1e83a7…; CDK; Season Pass spec | Calendar search on release | `gcal_list_events`, `gcal_search_events` | Julia's calendar | Collect & Win first window Fri Oct 10 00:00 UTC, 10 windows; Season Pass Nov 1 00:00 UTC; Endless and leaderboard Mondays |
| R5 | If anything is held and until when | Vincent #zombie-match3d; ZOM-429; brief hold rule | Slack search, Linear | `slack_conversations_search_messages`, `linear_get_issue`, `linear_list_comments` | Channel member; unscoped | Weekly leaderboard held until the fix is confirmed on prod, no date guessed |
| R6 | Push for each beat; Pushes tab one line per row | Push Notifications Zombie Match, PNs Beta; Frederick reply | Sheet search | `gsheets_search_spreadsheets`, `gsheets_values_get` | Shared | 10 lines: 2 go, 8 held with what is missing |
| R7 | Still to do and owner | Arthur's review comments on #468, #470, #472; ZOM-465; Brian mails; sweep of 21 tickets | PR review comments across the cohort the brief's hold rule already sends the agent through, Linear comments | `github_get_pull_request_comments`, `github_get_pull_request_reviews`, `linear_list_comments` | Unscoped | Six items with owners |
| R8 | Exclusions | Brief (Boss Arena), Frederick (Zombie Lane, four push rows), Robert DM (Halloween) | Thread, DM | Slack reads | Member | Not on the calendar |
| R9 | Config lock and reply | Brief Config locks; spec "locked 24h before each season opens"; Brian Sep 26 mail | Confluence, Gmail | `confluence_get_page`, `gmail_search_messages`, `gmail_reply_to_message` | Unscoped; Julia's mailbox | Earlier date before Oct 31 00:00 UTC, reply on the Sep 26 thread |
| R10 | Write the sheet | Sheet f_e4a17c90… tabs Calendar, Pushes | Frederick "ZM Live Ops folder" | `gsheets_values_update`, `gsheets_values_append` | Owner | Both tabs filled |
| R11 | Note on held beat's ticket | ZOM-429, assignee Douglas | Linear search | `linear_create_comment` | Writes unscoped | Comment on ZOM-429 |
| R12 | Link on calendar ticket | ZOM-78 and Frederick's comment; sheet `web_view_link` | Linear search on calendar; Drive metadata | `gdrive_get_file_metadata`, `linear_create_comment` | Owner; writes unscoped | Sheet link on ZOM-78 |
| R13 | Recommendation with trade-offs | Frederick's message | Thread | `slack_send_message` | DM member | Run/hold call in the DM |
| R14 | Final answer to Julia | Prompt | n/a | Final response | n/a | What was done |

Instruction chain: prompt "What he wants in it is in his message" incorporates FM and FR; prompt "his working rules for building it are in the brief" incorporates BR. Confluence, GCal, GitHub, Linear, Trello and Gmail are fact sources, except that the lock value comes from the spec through the brief's Config locks rule. No unmentioned policy adds an obligation. Confluence's "documented Product approval" is not needed because the brief states the rule.

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** PASS (5)

### Unique Ground Truth comparison

Unique Ground Truth: PASS 5

Basis: Every decision, write and destination resolves from the prompt, Frederick's message and reply, the brief and the newest applicable record. The weekly leaderboard hold end is set by the brief: until the fix is confirmed on prod, with no guessed date. The moved config date is a both-fair figure, bounded by the lock. Three additive still-to-do forks are excluded by the brief's definition and later records.

Alternative selection: Tested every decision a careful person could dispute: the only hold, the late beat, the write not named in the prompt, the hold end, the moved date, the one-off, the Season Pass first cell and the three additive still-to-do forks from the deep recheck. Reading I is the strongest: it is the one fork where the brief's own words appear to support the alternative.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Follow the prompt, Frederick's message and reply, and the brief; apply the newest record to each decision. | Run Collect &amp; Win from Fri Oct 10 00:00 UTC (late, not held), Season Pass, Endless, Plague Race, quest rollover and daily gift; hold the weekly leaderboard; send 2 of 10 pushes; keep Boss Arena, Zombie Lane and Halloween off. | Fill the Calendar and Pushes tabs of ZM3D Beta Live-Ops Calendar; add a Linear note on ZOM-429; link the sheet on ZOM-78; send Frederick the recommendation in DM D05SD5QLG94; reply to Brian on his Sep 26 mail with the earlier date. | Sheet f\_e4a17c90b3d25f6a8c1d73 (Calendar, Pushes); Linear ZOM-429; Linear ZOM-78; Slack DM with Frederick; Gmail reply on Brian's Sep 26 thread. | Collect &amp; Win: 10 windows from Fri Oct 10 00:00 UTC, still to do Oct 8 prod release (Douglas), final vial models (Claire), event icon animation (Marcus). Season Pass: October season running, November opens Sat Nov 1 00:00 UTC, still to do November config before Oct 31 00:00 UTC (Brian) and premium strip date range (Oliver). Weekly leaderboard: held until the ZOM-429 fix is confirmed on prod, no date guessed. Endless: daily 00:00 UTC, weekly Monday 00:00 UTC. Plague Race, quest rollover, daily gift: in, push held. Pushes that go out: lives recharged and 7-day lapsed; held: quests, 1-day lapsed, FTUE, Win &amp; Collect, Plague Race, Login Calendar, Season Pass, Weekly Leaderboard. | P (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/04\_Prompt.txt): "What he wants in it is in his message, and his working rules for building it are in the brief he shared with me."; BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "The rules stay here; the calls are yours." |
| B | The weekly leaderboard is not held: it is a reset that needs a restart, the Sep 16 ticket note says so, and no ticket note is written. | Run every beat including the weekly leaderboard; no beat is held. | Fill both tabs; link on ZOM-78; send Frederick the recommendation; reply to Brian. No ZOM-429 note. | Sheet; ZOM-78; Slack DM; Gmail reply. | Weekly leaderboard status Running, windows each Monday 00:00 UTC; otherwise as Reading A. | L429 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "if a player force-closes and reopens, they land in the new week fine, so not blocking."; BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "a reset that needs a restart" |
| C | Collect &amp; Win is held until the backend release, or starts on the release day, so it runs from Wed Oct 8. | Hold Collect &amp; Win until Oct 8 and run its Wed-Thu window. | Fill both tabs; note on the Collect &amp; Win ticket and ZOM-429; link on ZOM-78; recommendation; reply to Brian. | Sheet; a Collect &amp; Win ticket; ZOM-429; ZOM-78; Slack DM; Gmail reply. | Collect &amp; Win status Held until 2025-10-08, first window Wed Oct 8. | A470 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "they reach prod with the next backend release"; FM (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "if anything is held and until when" |
| D | The prompt lists the writes; the reply to Brian is not one of them, so the moved date stays in the sheet and the recommendation. | Run Collect &amp; Win from Fri Oct 10 00:00 UTC (late, not held), Season Pass, Endless, Plague Race, quest rollover and daily gift; hold the weekly leaderboard; send 2 of 10 pushes; keep Boss Arena, Zombie Lane and Halloween off. | Fill both tabs; note on ZOM-429; link on ZOM-78; recommendation to Frederick. No mail to Brian. | Sheet; ZOM-429; ZOM-78; Slack DM. | Collect &amp; Win: 10 windows from Fri Oct 10 00:00 UTC, still to do Oct 8 prod release (Douglas), final vial models (Claire), event icon animation (Marcus). Season Pass: October season running, November opens Sat Nov 1 00:00 UTC, still to do November config before Oct 31 00:00 UTC (Brian) and premium strip date range (Oliver). Weekly leaderboard: held until the ZOM-429 fix is confirmed on prod, no date guessed. Endless: daily 00:00 UTC, weekly Monday 00:00 UTC. Plague Race, quest rollover, daily gift: in, push held. Pushes that go out: lives recharged and 7-day lapsed; held: quests, 1-day lapsed, FTUE, Win &amp; Collect, Plague Race, Login Calendar, Season Pass, Weekly Leaderboard. | P (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/04\_Prompt.txt): "Once the sheet's done, link it on the calendar ticket and send Frederick the recommendation he asked for." |
| E | The Hold until (UTC) column takes an instant, so the hold is planned to end at the first Monday reset after the Oct 8 release, Mon Oct 13 00:00 UTC. | Run Collect &amp; Win from Fri Oct 10 00:00 UTC (late, not held), Season Pass, Endless, Plague Race, quest rollover and daily gift; hold the weekly leaderboard; send 2 of 10 pushes; keep Boss Arena, Zombie Lane and Halloween off. | Fill the Calendar and Pushes tabs of ZM3D Beta Live-Ops Calendar; add a Linear note on ZOM-429; link the sheet on ZOM-78; send Frederick the recommendation in DM D05SD5QLG94; reply to Brian on his Sep 26 mail with the earlier date. | Sheet f\_e4a17c90b3d25f6a8c1d73 (Calendar, Pushes); Linear ZOM-429; Linear ZOM-78; Slack DM with Frederick; Gmail reply on Brian's Sep 26 thread. | Weekly leaderboard: held until Mon Oct 13 00:00 UTC, W2 onward running; otherwise as Reading A. | SH (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): ""Hold until (UTC)""; FM (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "if anything is held and until when" |
| F | The earlier config date goes back to Brian's first commitment, Wed Oct 29, rather than the last day before the lock. | Run Collect &amp; Win from Fri Oct 10 00:00 UTC (late, not held), Season Pass, Endless, Plague Race, quest rollover and daily gift; hold the weekly leaderboard; send 2 of 10 pushes; keep Boss Arena, Zombie Lane and Halloween off. | Fill the Calendar and Pushes tabs of ZM3D Beta Live-Ops Calendar; add a Linear note on ZOM-429; link the sheet on ZOM-78; send Frederick the recommendation in DM D05SD5QLG94; reply to Brian on his Sep 26 mail with the earlier date. | Sheet f\_e4a17c90b3d25f6a8c1d73 (Calendar, Pushes); Linear ZOM-429; Linear ZOM-78; Slack DM with Frederick; Gmail reply on Brian's Sep 26 thread. | November config due Wed Oct 29; otherwise as Reading A. | BM1 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "The config handoff we agreed with Product is for Wed Oct 29" |
| G | Robert approved the Halloween one-off, so it takes a recurring slot in a beta week. | Add the Halloween one-off in a recurring slot; everything else as Reading A. | Fill the Calendar and Pushes tabs of ZM3D Beta Live-Ops Calendar; add a Linear note on ZOM-429; link the sheet on ZOM-78; send Frederick the recommendation in DM D05SD5QLG94; reply to Brian on his Sep 26 mail with the earlier date. | Sheet f\_e4a17c90b3d25f6a8c1d73 (Calendar, Pushes); Linear ZOM-429; Linear ZOM-78; Slack DM with Frederick; Gmail reply on Brian's Sep 26 thread. | Halloween one-off row in W4; otherwise as Reading A. | ROB1 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "approved from my side for one of the beta weeks" |
| H | Season Pass has no window that opens before the calendar span, so its First window is Nov 1 00:00 UTC, or Oct 6 00:00 UTC clipped to the span. | Run Collect &amp; Win from Fri Oct 10 00:00 UTC (late, not held), Season Pass, Endless, Plague Race, quest rollover and daily gift; hold the weekly leaderboard; send 2 of 10 pushes; keep Boss Arena, Zombie Lane and Halloween off. | Fill the Calendar and Pushes tabs of ZM3D Beta Live-Ops Calendar; add a Linear note on ZOM-429; link the sheet on ZOM-78; send Frederick the recommendation in DM D05SD5QLG94; reply to Brian on his Sep 26 mail with the earlier date. | Sheet f\_e4a17c90b3d25f6a8c1d73 (Calendar, Pushes); Linear ZOM-429; Linear ZOM-78; Slack DM with Frederick; Gmail reply on Brian's Sep 26 thread. | Season Pass First window Nov 1 00:00 UTC or Oct 6 00:00 UTC; otherwise as Reading A. | BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "The calendar covers Mon Oct 6 00:00 UTC to Sun Nov 2 23:59 UTC"; BM2 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "The November season still opens on Sat Nov 1." |
| I | Season Pass Still to do also lists a premium buy check on a prod build, because the brief says an unverified build is a still-to-do and Oliver asked for that test. | Run Collect &amp; Win from Fri Oct 10 00:00 UTC (late, not held), Season Pass, Endless, Plague Race, quest rollover and daily gift; hold the weekly leaderboard; send 2 of 10 pushes; keep Boss Arena, Zombie Lane and Halloween off. | Fill the Calendar and Pushes tabs of ZM3D Beta Live-Ops Calendar; add a Linear note on ZOM-429; link the sheet on ZOM-78; send Frederick the recommendation in DM D05SD5QLG94; reply to Brian on his Sep 26 mail with the earlier date. | Sheet f\_e4a17c90b3d25f6a8c1d73 (Calendar, Pushes); Linear ZOM-429; Linear ZOM-78; Slack DM with Frederick; Gmail reply on Brian's Sep 26 thread. | Season Pass Still to do adds a premium buy check on a prod build; otherwise as Reading A. | BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "an unverified build or platform is a still-to-do, not a hold."; OL12 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C08R6BF4ENN/2025-09.json pointer /21/text): "We need to test the premium buy on a prod build" |
| J | Collect &amp; Win Still to do also lists PR \#477's title change, which is open and is not analytics. | Run Collect &amp; Win from Fri Oct 10 00:00 UTC (late, not held), Season Pass, Endless, Plague Race, quest rollover and daily gift; hold the weekly leaderboard; send 2 of 10 pushes; keep Boss Arena, Zombie Lane and Halloween off. | Fill the Calendar and Pushes tabs of ZM3D Beta Live-Ops Calendar; add a Linear note on ZOM-429; link the sheet on ZOM-78; send Frederick the recommendation in DM D05SD5QLG94; reply to Brian on his Sep 26 mail with the earlier date. | Sheet f\_e4a17c90b3d25f6a8c1d73 (Calendar, Pushes); Linear ZOM-429; Linear ZOM-78; Slack DM with Frederick; Gmail reply on Brian's Sep 26 thread. | Collect &amp; Win Still to do adds \#477 title change (Owen); otherwise as Reading A. | PR477 (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/data.json pointer /pull\_requests/2382/title): "Collect And Win Analytics and title change"; FM (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "what still has to land before it runs and who owns that" |
| K | Season Pass Still to do also lists a prod deploy for ZOM-563, because golden frames and names are premium perks. | Run Collect &amp; Win from Fri Oct 10 00:00 UTC (late, not held), Season Pass, Endless, Plague Race, quest rollover and daily gift; hold the weekly leaderboard; send 2 of 10 pushes; keep Boss Arena, Zombie Lane and Halloween off. | Fill the Calendar and Pushes tabs of ZM3D Beta Live-Ops Calendar; add a Linear note on ZOM-429; link the sheet on ZOM-78; send Frederick the recommendation in DM D05SD5QLG94; reply to Brian on his Sep 26 mail with the earlier date. | Sheet f\_e4a17c90b3d25f6a8c1d73 (Calendar, Pushes); Linear ZOM-429; Linear ZOM-78; Slack DM with Frederick; Gmail reply on Brian's Sep 26 thread. | Season Pass Still to do adds ZOM-563 prod deploy (Douglas); otherwise as Reading A. | Z563 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3640/title): "Teams' lives, golden frames and names not working on prod env"; BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "prod deploy" |

Explicit option inventory: The prompt lists no candidate options to choose between.
Inventory evidence: P (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/04\_Prompt.txt): "Can you take it on for me?"

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: B
Resolution: EXCLUDED. Newer source: Vincent's Sep 30 retest on the prod build replaces Douglas's Sep 16 note for the same bug and scope. Authority: the brief holds a beat on an established failure that survives a restart. Source identity: Vincent is the ticket's reporter and QA tester. Scope: only the leaderboard changes. Same result: no, the decision and a write differ.
Resolution evidence: VIN (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "it still does not start a new week. I killed the app and reopened it twice"; BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "Hold a beat only when players provably cannot enter, score or claim on prod even after a restart. An established failure holds it"; Z429 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3495/description): "When the weekly leaderboard is ended, it doesn't start the new one or let me claim my rewards."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Hold versus run. |
| writes | DIFFERENT | B drops the ZOM-429 note. |
| destinations | DIFFERENT | B has no ZOM-429 destination. |
| contents | DIFFERENT | Status and windows differ. |

Authority chain: P → BR

Resolution relevance challenge: The quotes address this exact difference: the retest states the failure survives a kill and reopen, which is the brief's test, and it is two weeks newer than the note that says a restart works.
Delegation challenge: NOT_CLAIMED. No alternative is accepted.
Challenge evidence: VIN (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "Same on the second device."; BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "a reset that needs a restart"

Compared alternative: C
Resolution: EXCLUDED. Authority: the brief says a beat waiting only on the release starts late and is not held, and that a window the release pre-empts does not count. The release instant is Wed Oct 8 15:00 UTC, after the Wed-Thu window opened at 00:00 UTC, so the first window is Fri Oct 10 00:00 UTC.
Resolution evidence: BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "A beat that is only waiting on that release starts late, it is not held."; BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "so a window the release instant pre-empts does not count."; GC (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "'2025-10-08 15:00:00+00'"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Held versus late. |
| writes | DIFFERENT | C adds a note on a Collect &amp; Win ticket. |
| destinations | DIFFERENT | C adds that ticket. |
| contents | DIFFERENT | Status and first window differ. |

Authority chain: P → BR

Resolution relevance challenge: The brief sentence is written for this case and the GCal instant fixes the arithmetic.
Delegation challenge: NOT_CLAIMED. No alternative is accepted.
Challenge evidence: BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "Collect &amp; Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC"

Compared alternative: D
Resolution: EXCLUDED. Authority: the prompt incorporates the working rules, and the Config locks rule requires the owner to be told in a reply on the mail. Brian's Sep 26 mail asks for exactly that. Lock: Nov 1 00:00 UTC minus 24h is Oct 31 00:00 UTC; Fri Oct 31 10:00 Istanbul is 07:00 UTC, so it misses.
Resolution evidence: BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "A committed date that misses the lock moves earlier and its owner is told in a reply on the mail where they committed to it."; BM2 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "If the new date is a problem on your side, reply on this mail."; CSP (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/confluence/confluence\_working.json pointer /pages/20/body): "locked 24h before each season opens"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same beats run and hold. |
| writes | DIFFERENT | D drops the Gmail reply. |
| destinations | DIFFERENT | D has no Gmail destination. |
| contents | SAME | Sheet contents are the same. |

Authority chain: P → BR

Resolution relevance challenge: The prompt's list of writes does not say it is exhaustive and the incorporated brief names this write in terms.
Delegation challenge: NOT_CLAIMED. No alternative is accepted.
Challenge evidence: P (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/04\_Prompt.txt): "his working rules for building it are in the brief he shared with me"

Compared alternative: E
Resolution: EXCLUDED. Authority: the brief now answers this case directly: a hold with no dated fix runs until the fix is confirmed on prod, and it says to state that instead of guessing a date. ZOM-429 has no due date or PR, so the hold has no dated fix. The column heading does not outrank the rule.
Resolution evidence: BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date."; GC (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "The server windows that are still on the DEV stack go live with this release"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same run and hold decision in the sheet. |
| writes | SAME | Same writes. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | A states the open hold and its lift condition; E states an instant. |

Authority chain: P → BR

Resolution relevance challenge: The sentence names this exact situation and rules out the date E would write. The GCal description shows the Oct 8 release is not a dated leaderboard fix.
Delegation challenge: NOT_CLAIMED. No alternative is accepted.
Challenge evidence: SH (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): ""Hold until (UTC)""; BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "say that instead of guessing a date."

Compared alternative: F
Resolution: BOTH_FAIR_FIGURE. Only the named earlier date differs. The brief gives a limit, not a date, so either value is a fair call and the decision, reply and thread are the same.
Resolution evidence: BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "A committed date that misses the lock moves earlier and its owner is told in a reply on the mail where they committed to it."; CSP (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/confluence/confluence\_working.json pointer /pages/20/body): "locked 24h before each season opens"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same decision. |
| writes | SAME | Same reply. |
| destinations | SAME | Same thread. |
| contents | DIFFERENT | The named earlier date differs. |

Both-fair figure: DATE, New November config handoff date
Value for A: before Oct 31 00:00 UTC. Evidence: CSP (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/confluence/confluence\_working.json pointer /pages/20/body): "locked 24h before each season opens"; BM2 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "The November season still opens on Sat Nov 1.". Derivation: Nov 1 00:00 UTC minus 24 hours is Oct 31 00:00 UTC; any earlier instant meets the lock.
Value for F: Wed Oct 29. Evidence: BM1 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "The config handoff we agreed with Product is for Wed Oct 29"
Newer source check does not settle it: Brian dropped Oct 29 for Oct 31, but Oct 31 misses the lock, so the newer mail names no valid date.
Authority check does not settle it: The brief sets the limit and says the date moves earlier; it names no date.
Source identity check does not settle it: Both dates trace to Brian and the spec; identity does not rank them.
Scope check does not settle it: Both apply to the same November config.
Same material result check does not settle it: Decision, reply, recipient and thread match; only the named date differs.
Every explicit ask: Each reading fills the sheet and replies to Brian on the Sep 26 mail with a date before the lock.
Next step unchanged: The agent writes the same reply and the same Still to do row; nothing later depends on which earlier date is named.
Rubric must accept: before Oct 31 00:00 UTC or Wed Oct 29

Resolution relevance challenge: The rule gives a limit, not a value, so no quote ranks the two.
Delegation challenge: NOT_CLAIMED. No delegation is claimed; this is a both-fair figure.
Challenge evidence: BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "moves earlier"

Compared alternative: G
Resolution: EXCLUDED. Newer source and authority: the brief says Product's later word counts, Robert is Product, and his Sep 30 DM withdraws the Sep 18 approval and says to take it off the calendar.
Resolution evidence: ROB2 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "pulling my ok. Take it off the beta calendar"; BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "if he takes that back his later word is the one that counts."; CSP3 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/confluence/confluence\_working.json pointer /pages/20/body): "Owner: Robert (Product)."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Halloween in versus out. |
| writes | SAME | Same writes. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | A Halloween row exists only in G. |

Authority chain: P → BR

Resolution relevance challenge: The later DM addresses the same one-off and scope.
Delegation challenge: NOT_CLAIMED. No alternative is accepted.
Challenge evidence: ROB2 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "my later word on this one is the one that counts."

Compared alternative: H
Resolution: EXCLUDED. Authority: the brief defines the start as the first window that opens after the server windows are live, and Arthur says the Season Pass schedule is already running on prod on Sep 30, so that window is the season opening on Oct 1. Oct 6 is not an opening instant and the brief bars a different instant. Nov 1 skips a season the premium strip note confirms.
Resolution evidence: BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "A beat starts with the first window that opens after its server windows are live on prod"; BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "Season Pass seasons open on the 1st at 00:00 UTC."; A470 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "Season Pass schedules are already running on prod"; A472 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "is still set to the October range"; BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "a different instant is not."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same decision. |
| writes | SAME | Same writes. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | One cell differs. |

Authority chain: P → BR

Resolution relevance challenge: The start rule is not limited to the span, and the span sentence sets what the calendar covers, not when a window opened.
Delegation challenge: NOT_CLAIMED. No alternative is accepted.
Challenge evidence: BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "Every window is stated in server time (UTC) as a start-end instant."

Compared alternative: I
Resolution: EXCLUDED. Authority: the unverified clause sits in the hold test and contrasts with an established failure, so it sorts failure reports. No record reports a premium buy failure on prod. A test is not a prod deploy, config or flagged art. Newer source: after Oliver's Sep 12 ask, Vincent bought the pass on the latest builds, Leonard played the production build the same day, and the pass reached production. Brief: not what already shipped.
Resolution evidence: BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "An established failure holds it; an unverified build or platform is a still-to-do, not a hold."; BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "(prod deploy, config, player-facing art an owner has flagged)"; BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "Not what already shipped"; VN16 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C08R27X0EAH/2025-09.json pointer /698/text): "After purchasing premium pass, lives are reset to 8 after every win."; LH16a (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C08R27X0EAH/2025-09.json pointer /663/text): "Playing submission candidate."; LH16b (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C08R27X0EAH/2025-09.json pointer /685/text): "This is production build"; CSP4 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/confluence/confluence\_working.json pointer /pages/20/body): "Reached production in the week of"; A470 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "Season Pass schedules are already running on prod"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same decision. |
| writes | SAME | Same writes. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | One extra line in one cell. |

Authority chain: P → BR

Resolution relevance challenge: Oliver's line is a pre-release request on a test-build post. Later records on the same issue show the purchase exercised and the pass shipped, and the clause B relies on has no failure to act on.
Delegation challenge: NOT_CLAIMED. No alternative is accepted.
Challenge evidence: OL12 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C08R6BF4ENN/2025-09.json pointer /21/text): "We need to test the premium buy on a prod build"; LH16c (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C08R27X0EAH/2025-09.json pointer /682/text): "Season pass is looking pretty good."

Compared alternative: J
Resolution: EXCLUDED. Authority: a beat does not wait on client PR merges, and the still-to-do types are prod deploy, config and flagged art. \#477 is a client PR; its analytics are excluded by name; its title change is text in a PR, and no persona-visible note says it has to land before the event runs.
Resolution evidence: BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "not when its client PRs merged"; BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "(prod deploy, config, player-facing art an owner has flagged)"; BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "not analytics, not polish nobody flagged."

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same decision. |
| writes | SAME | Same writes. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | One extra line in one cell. |

Authority chain: P → BR

Resolution relevance challenge: The vial models and icon animation are also client work, but each has a note saying it is missing or still to do. \#477 has only a PR title. SC-18 also bars relying on its state.
Delegation challenge: NOT_CLAIMED. No alternative is accepted.
Challenge evidence: A468 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "The final vial models are missing"; L465b (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "is still to do on my side"

Compared alternative: K
Resolution: EXCLUDED. Authority: the Still to do list is per beat, and a beat is an event window, a reset or a start push. ZOM-563 is about Teams by its own title, carries no Season Pass link, and no record ties it to the beat. The tie is the reader's inference from a separate leaderboard report.
Resolution evidence: BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "For each beat, what still has to land before it runs for bought users"; BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "Every ZM3D beat a player can see in those weeks: an event window, a reset or a start push."; Z563 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3640/title): "Teams' lives, golden frames and names not working on prod env"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Same decision. |
| writes | SAME | Same writes. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | One extra line in one cell. |

Authority chain: P → BR

Resolution relevance challenge: The possessive in the title covers all three items. A Teams screen is not a window, reset or start push, and Season Pass is already running. SC-16 also bars using this ticket's status.
Delegation challenge: NOT_CLAIMED. No alternative is accepted.
Challenge evidence: A470 (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "Season Pass schedules are already running on prod"

Strongest-alternative challenge (I): The brief says an unverified build is a still-to-do, Oliver named the test, and the spec records no purchase. It is removed by reading the clause in its sentence, which sorts failures, and by the later records on the same issue. It is additive, so it contradicts nothing in Reading A.
Challenge evidence: BR (/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review\_rev8/inputs/01\_Universe\_Inject.sql): "An established failure holds it; an unverified build or platform is a still-to-do, not a hold."; OL12 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C08R6BF4ENN/2025-09.json pointer /21/text): "We need to test the premium buy on a prod build"; VN16 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C08R27X0EAH/2025-09.json pointer /698/text): "After purchasing premium pass, lives are reset to 8 after every win."

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

The fork list is in `## Deep Recheck`.

The full decision sweep (59 rows: every beat, excluded item, push row, still-to-do candidate and write, each with its settling record) is `decision_sweep` in 1_prompt_checks.json.

**2.2 Feasibility:** PASS (5)

A. Tools

| Ask | Capability | Tool | Feasible? |
|---|---|---|---|
| Fill sheet tabs | Write cell ranges | `gsheets_values_update`, `gsheets_values_append` | Yes |
| Note and link on tickets | Add a comment | `linear_create_comment` | Yes |
| Recommendation | Post in DM | `slack_send_message` | Yes |
| Reply to Brian | Reply on a thread | `gmail_reply_to_message` | Yes |

No format conversion or attachment is asked for.

B. Data

| Needed | Where | Found? | Evidence |
|---|---|---|---|
| Release instant | GCal, Julia's calendar | Yes | `2025-10-08 15:00:00+00`, "release window 18:00-19:00 Istanbul time" |
| Collect & Win windows | Brief; Confluence; CDK | Yes | "Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC" |
| Season start | Brief; spec; CDK `0 0 1 * *` | Yes | "Season Pass seasons open on the 1st at 00:00 UTC" |
| Leaderboard reset | CDK `LEAGUES_SCHEDULE` | Yes | `"0 0 * * 1"` |
| Endless resets | Confluence; CDK | Yes | "daily reset 00:00 UTC, weekly reset Monday 00:00 UTC" |
| Hold evidence | #zombie-match3d; ZOM-429 | Yes | "still does not start a new week" |
| Hold end | Brief | Yes, as a rule | "A hold with no dated fix runs until the fix is confirmed on prod". No fix date exists: searched Slack 2025-09, Linear, GitHub PRs and commits since Sep 15, the ZM ROADMAP board, Gmail for ZOM-429 and GCal |
| Lock | Spec | Yes | "locked 24h before each season opens" |
| Push rows | PNs Beta rows 2-15 | Yes | 14 rows, Status and Status (NA, WIP, LIVE) columns |
| Change-request blockers | GitHub reviews | Yes, none | 74 CHANGES_REQUESTED reviews, newest 2025-07-16 (match3d#303) |

"Until when" is answerable from the brief, so no ask depends on a missing value.

C. Dimensional: no per-X numeric breakdown. Beats, windows, weeks and pushes are all carried by the sources.

D. Numeric observability: instants come as ISO values or stated local times with a zone. Oct 31 10:00 Istanbul is 07:00 UTC; Oct 8 18:00 Istanbul is 15:00 UTC. Rendering by tools is an evidence limit only.

E. Persona ACL. Scoped services from `acl.md`: Gmail, Slack, GCal, GDrive, GDocs, GSheets, GSlides.

| Required fact | Record | Scoped | Visibility basis | Verdict |
|---|---|---|---|---|
| Frederick's ask and reply | DM D05SD5QLG94 | Slack | Julia in members | Feasible |
| Robert's withdrawal | DM D05GU6L0XFH | Slack | Julia in members | Feasible |
| Robert's approval | #zombie-art | Slack | Julia in members, joined 2025-05-06 | Feasible |
| Vincent's retest | #zombie-match3d (private) | Slack | Julia in members, joined 2025-01-12, no leave event | Feasible |
| Brief | f_7c3e91a4… | GDrive/GDocs | Shared, reader | Feasible |
| UA plan | f_2b9d4e7a… | GDrive/GSlides | Shared, reader | Feasible |
| Calendar sheet | f_e4a17c90… | GSheets | Owner | Feasible |
| Push sheet | f_a325dd4a… | GSheets | Domain, Julia in shares | Feasible |
| Release event | evt_5c1e83a7… | GCal | Julia's own calendar copy | Feasible |
| Brian's mails | Julia copies | Gmail | Julia's mailbox | Feasible |

Lens 2: no ask directs a read outside her view. #zombie-prs and #zm-collect-win are not hers, and nothing required sits only there: the #zombie-prs mirrors repeat GitHub, which is unscoped.

**2.3 Truthfulness:** PASS (5)

| Claim | Record | Accurate? | Evidence |
|---|---|---|---|
| "Frederick messaged me yesterday" | bca78437…, D05SD5QLG94 | Yes | 2025-09-30T20:20:17Z |
| "the Zombie Match 3D beta" | Deck; #company-internal | Yes | "Beta target: Sep 30." |
| "the four buy weeks that start Monday the 6th" | Deck slide 2 | Yes | "W1 Mon Oct 6 - Sun Oct 12"; Oct 6, 2025 is a Monday |
| "the brief he shared with me" | f_7c3e91a4… | Yes | Owner Frederick, Julia reader |
| "my live-ops calendar sheet" | f_e4a17c90… | Yes | Owner Julia, folder ZM Live Ops |
| "its ticket so the owner picks it up" | ZOM-429 | Yes | Assignee Douglas |
| "the calendar ticket" | ZOM-78 | Yes | "Let us use this ticket for the ZM3D beta live-ops calendar" |
| "the recommendation he asked for" | bca78437… | Yes | "send me your recommendation back here" |

No channel, amount, vendor or fiscal period is stated. No departed person acts: Douglas, Brian, Claire, Marcus, Oliver are active in late September. Nothing asserted sits after the clock.

**2.4 Tool Use & Cross-service:** PASS (5)

| Service | Graded fact it changes | Read/Write |
|---|---|---|
| Slack | Leaderboard held; Halloween off; exclusions | Read, Write |
| GCal | Collect & Win first window | Read |
| Gmail | Date that misses the lock | Read, Write |
| Confluence | Lock value and Endless cadence | Read |
| GitHub | Prod state; vial models; premium strip (review comment on #472); leaderboard cron | Read |
| Linear | Icon animation owner; which tickets drop out; ZOM-429, ZOM-78 | Read, Write |
| GSheets | Push status and copy; destination | Read, Write |
| GDocs, GSlides | Rules; weeks | Read |
| Trello | Quests: the rollover does not wait on the new ones | Read |

**2.5 Investigation + Action:** PASS (5). Every write depends on findings. Complexity hygiene: no blocked or repeated calls are designed in.

**2.6 Clarity & Specificity:** PASS (5)
- Intent, who, what and where are clear. No first-person "I'll" statements.
- Write-action divergence: none. All readings fill the same tabs and make the same notes, link, post and reply.
- The earlier Minor issue is closed. Frederick's "if anything is held and until when" and the `Hold until (UTC)` column now have a rule: "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date."
- The moved config date is a bounded call, not a misreading: the brief sets the limit and the rubric must test the limit.

**2.7 Contrived / Unnatural:** PASS (5)

| Indicator | Found? |
|---|---|
| Exact timestamps, opaque IDs, generated filenames | No. "Monday the 6th" is natural |
| Arbitrary format constraints, unrealistic behaviour | No |
| Step commands, padding | No |
| Trap hint or riddle | No. "If a beat ends up held" names no beat or cause |
| Hidden destination | No. "my live-ops calendar sheet" and "the calendar ticket" are named; Frederick's message and ZOM-78's comment lead to each |
| Audit form or if-chain | No. One conditional, carried by seeded rules |
| Spec-sheet triggers | 0 of 4 |

Natural difficulty: conflicting records, scattered facts, later corrections, implicit rules in records.

**2.8 Alignment with Today's Date:** PASS (5). Yesterday is Sep 30. Monday the 6th is ahead of the clock. Oct 8, Oct 31 and Nov 1 are future plans, not treated as done.

**2.9 Originality:** N/A. No samples supplied and the library is not bundled.

---

### Phase 3: Universe Feasibility

**Data Existence:** PASS (5). All 8 premises and every required fact exist in base or proposed records and have a catalog read path. The sheet now carries a link value for ZOM-78.

**Cross-Service Coherence:** PASS (5)
- Injection SQL considered: Yes. Static evidence: direct task-relevant checks plus Eval 0 PASS on this hash. P2 found no inconsistency on this hash.

| Artifact | Tested against | Result |
|---|---|---|
| Frederick's message and reply | DM history; PNs Beta rows 3, 9, 11, 12; Confluence Zombie Lane; translated tab | Consistent. Four named rows exist; the translated tab is the Domino set |
| Vincent's retest | ZOM-429; Sep 22 #zombie-bugs thread; DMs of Sep 30 | Consistent. He is testing prod that evening |
| Douglas ZOM-429 note | Issue updated_at 2025-09-22 | Consistent |
| Arthur #470 comment | PR merged 15:51:15, rev_9 15:51:06; Owen Sep 26 "Igual no va para release ahora"; CDK prod schedules | Consistent. Prod deploys on Sep 29 and 30 were Google login and teams; no record says Collect & Win shipped |
| Arthur #468 comment | Merge 16:13:50, comment 15:36:41; path in diff; `#zm-collect-win` | Consistent |
| Arthur #472 comment | rev_1 APPROVED 15:52:58, merge 15:53:04; path in diff; the comment says "Separately" | Consistent. Pre-merge; the off-topic placement is explained in the comment |
| Slack PR mirrors | Thread counts 41, 16, 3 become 42, 17, 4; latest_reply kept at the merge mirror; ts match created_at | Consistent |
| ZOM-432 Done | PR #471 diff: `Assets/Sprites/Daily Gift/img - DailyGift.png`; #builds iOS #50 and Android #135 on Sep 30 | Consistent |
| ZOM-344 Done | Slack, mail, git | No conflict found |
| ZOM-521 unticked, ZOM-526, ZOM-528 | SC-15 repaired by the description update; #472, #475 merges precede the comments | Consistent |
| ZOM-543 "in progress" | Trello #63 ticked 16:40:22, comment 16:20:37 | Sequential, no conflict. Linear stays In Progress as in base |
| ZOM-465 icon note | No Collect & Win-named animation clip on main; #454, #456, #458, #475 predate or skip it | No conflict found |
| ZOM-471 note | #zombie-match3d Aug 13: Leonard "we don’t need it!", Vincent "it already has start button" | Consistent |
| ZOM-504 note | Vincent DM Sep 3: "I couldn't repro without bots" | Consistent |
| ZOM-565 note | Commit 44988da015 2025-09-29, Marcus's Slack "i wrote a comment on the linear task" 14:34:25 | Consistent |
| ZOM-534 note | Commit 47c65623e7 2025-09-10; Oliver "yeah its on main" | Consistent |
| ZOM-566 In Progress | Owen 16:49 "squeeze analytics events first", #477 22:26 | Consistent |
| Trello card 61 comment | list name "BETA: Sep 30" matches later actions (SC-13, not graded); badge and activity updated; new wording fits PN row 2 "Revisit once new quests roll out." | Consistent |
| Brian's mails | Weekdays; +0300 headers; internal_date; three mailboxes | Consistent. Oct 29 Wed, Oct 31 Fri, Nov 1 Sat |
| GCal release | 4 copies, same ical_uid; 15:00Z = 18:00 Istanbul | Consistent |
| Brief, deck, sheet | Drive naming (.docx, .xlsx, none for slides); dates; shares; style runs; web_view_link pattern | Consistent |
| Slack authors | Frederick, Robert, Vincent, bot are members of their channels | Consistent |
| Apostrophes | `Nathan''s` doubled; lint clean | Consistent |
| Confluence values used | "24h" lock, Endless cadence, Collect & Win windows, Robert (Product) | No conflict on a value the answer needs |

Known base issues touched: SC-13 (list name, not read by the answer), SC-15 (repaired), SC-18 (#477, not relied on), SC-38 (analytics excluded by the brief). No "don't grade" value is required. SC-7: no leave event for Julia in the two channels she needs.

Advisories, not scored. None changes a graded value, and P2 and Eval 0 list the same ones:
- `github_timeline_events` #468#ev_6 (`reviewed`) sorts after ev_5 (`closed`) while the review is timed before the merge. Its created_at is NULL as in base. Eval 0's call; the answer does not read it.
- The premium strip note sits on a Queue Manager PR. It is reachable: GitHub is unscoped, #472 is in the Aug-Sep cohort the brief's hold rule makes the agent check, and the comment says "Separately". All three Arthur notes are now review comments, read through `github_get_pull_request_comments`; the catalog has no return schema, so that rendering is an evidence limit. Julia cannot use the #zombie-prs mirror.
- Deck slide 2 "scaled up week by week if the cohorts hold" and slide 3 "hold the spend there until the pivot call" are compatible only if the pivot call gates scaling. Leonard's Sep 22 note puts the decision 15 to 20 days after the beta. No value depends on it.

---

### Phase 4: Final Evaluation

**Scoring Table:**

| Dimension | Sub-Dimension | Score | Justification |
|---|---|---|---|
| Prompt | Unique Ground Truth | 5 | Comparison above; ten forks ruled out by quotes, one both-fair figure |
| Prompt | Feasibility | 5 | All tools and data exist; "until when" answered by the brief |
| Prompt | Persona ACL Reachability | 5 | All ten scoped reads visible to Julia |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 5 | No write divergence; hold end now set by the brief |
| Prompt | Contrived / Unnatural | 5 | Plain request, no flags |
| Prompt | Alignment with Today's Date | 5 | All references resolve |
| Prompt | Originality / Sample Similarity | N/A | No samples, library not bundled |
| Prompt | Truthfulness | 5 | 8 of 8 premises verified |
| Prompt | Tool Use & Cross-service | 5 | Each service changes a graded fact |
| Prompt | Investigation + Action | 5 | Six writes fed by investigation |
| Prompt | Coherence (Bolt-on) | 5 | One situation |
| Prompt | Persona | 5 | Exact roster, role fits |
| Prompt | Business Function | 5 | Product decision; overlap noted |
| Prompt | Assigned Competency | 5 | GTM calendar for paid buy |
| Prompt | Assigned Task Skill | 5 | Planning and decision support is the point of the task |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three dimensions; short trigger |
| Universe | Data Exists | 5 | Required facts present |
| Universe | Cross-Service Coherence | 5 | No inconsistency in task-touched data; Eval 0 PASS, P2 no finding |

Lowest: no scored dimension below 5.

---

### Issues Found

No fail-level or score-affecting issue remains. The rows below are for the rubric stage.

| # | Issue | Severity | Dimension |
|---|---|---|---|
| 1 | Closed by the revision. On 091722f6 the only hold had no source for "Hold until (UTC)"; the new brief sentence settles it. | Closed | Clarity |
| 2 | The new November config date is a both-fair figure. Brief: "moves earlier". Spec: "locked 24h before each season opens". | Minor, rubric guidance | Unique Ground Truth |
| 3 | Still to do lists have required items, and a careful run may add lines for the premium buy, #477 or ZOM-563. | Minor, rubric guidance | Unique Ground Truth |
| 4 | Season Pass First window has one right value, Oct 1 00:00 UTC, but a run can state the same facts in another layout. | Minor, rubric guidance | Unique Ground Truth |

### Recommended Improvements

No prompt or SQL change is required.

1. Rubric: the November config row must accept any time before 2025-10-31 00:00 UTC, including Wed Oct 29.
2. Rubric: grade Still to do by the required items only: Oct 8 release (Douglas), final vial models (Claire), event icon animation (Marcus), November config (Brian), premium strip (Oliver). Use no exact-set row. No row may require the premium buy, #477 or ZOM-563 (SC-16, SC-18).
3. Rubric: test that the October season is open and the November season opens Nov 1 00:00 UTC, not one layout of the first-window cell.
4. Rubric: accept the leaderboard hold stated as until the fix is confirmed on prod. Do not pin whether the held row shows its Monday cadence or leaves Windows blank. Do not pin Oct 13 as a date for the quests push. Check that the sheet is linked on ZOM-78, not one exact URL.
5. Optional, only if a stricter close on DR5 is wanted: seed a dated, persona-visible record that the premium buy passed on a prod build. This adds a new fact, so no wording is proposed.

---

## Deep Recheck

Passes: P1, P2, P3, P4, run by the coordinator as separate blind subagents; their reports do not state model or effort.

**Which pass ran on which hash.** P1 and P2 ran on the current SQL, 0e8c8ad8…f815. P3 and P4 ran on the previous SQL, 091722f6…b876. The prompt, assignment and date are byte-identical across both. I checked P3 and P4 against the diff: P4 reads only the prompt. P3's 14 premises quote lines that did not change, or changed elsewhere in the row (L103, L130); only its SQL-read section cites removed rows (#473, the "2 to 3" reply count), and Eval 0 and P2 re-ran that on the current hash. Neither result is affected.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 49 sentences, on 0e8c8ad8 | 7 forks, 5 notes | 0 fails, 1 both-fair figure |
| P2 | 6 prompt sentences, 38 source sentences, 96 statements, on 0e8c8ad8 | 0 findings, 7 advisories | 0 |
| P3 | 6 sentences, 14 premises, on 091722f6 | None | 0 |
| P4 | 6 sentences, on 091722f6 | None | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| P1-DR1 | P1 | "if anything is held and until when" | SQL L103 brief; ZOM-429 `due_date` null | §2 which date | Unique Ground Truth | REJECTED | "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date." |
| P1-DR2 | P1 | "what still has to land before it runs" | SQL L180 ZOM-534; commit 47c65623e7 | §2 which items | Unique Ground Truth | REJECTED | "That is on main, so nothing else has to land for the beta." `git merge-base` confirms the commit is on main, which clears P1's stated limit |
| P1-DR3 | P1 | "moves earlier" | SQL L111; spec; Brian Sep 22 and Sep 26 | §2 which date | Unique Ground Truth | BOTH_FAIR_FIGURE | One date differs, both on Julia's records, no check ranks them, writes are the same. Newer mail drops Oct 29, but the Oct 31 it names misses the lock |
| P1-DR4 | P1 | "First window (UTC)" | SQL L101, L97; #470 rc_10; #472 rc_1 | §2 which date | Unique Ground Truth | REJECTED | "A beat starts with the first window that opens after its server windows are live on prod" and "Season Pass schedules are already running on prod" give Oct 1. Oct 6 is not an opening: "a different instant is not". P1's three values also fail the both-fair limit of two |
| P1-DR5 | P1 | "an unverified build or platform is a still-to-do, not a hold." | #zombie-ops Sep 12; #zombie-bugs Sep 16; spec | §2 which items | Unique Ground Truth | REJECTED | See rulings below |
| P1-DR6 | P1 | "what still has to land before it runs" | #477 title and commits; SQL L101, L107 | §2 which items | Unique Ground Truth | REJECTED | See rulings below |
| P1-DR7 | P1 | "For each beat" | ZOM-563; SQL L99, L107 | §2 which items | Unique Ground Truth | REJECTED | See rulings below |
| P1-N1 | P1 | "Fine for this PR. Separately" | #472 rev_1 | §2 | Unique Ground Truth | REJECTED | State APPROVED, so not a change-request hold |
| P1-N2 | P1 | "The rollover does not wait on them" | SQL L235 | §2 | Unique Ground Truth | REJECTED | Same sentence: "the current quests keep running either way" |
| P1-N3 | P1 | "Revisit once new quests roll out." | PN row 2; Trello | §2 | Unique Ground Truth | REJECTED | Row is Not Ready, so held either way; "if they are ready" makes Oct 13 no fixed date |
| P1-N4 | P1 | "say that instead of guessing a date" | SQL L103, L109 | §2 | Unique Ground Truth | REJECTED | Pushes need "what is missing"; no push gets a date under either reading |
| P1-N5 | P1 | "link it on the calendar ticket" | SQL L130 | §2 | Clarity | REJECTED | Link and file id reach the same sheet |
| P2-A1 | P2 | "deploy the win and collect to pro servers" | POD notes mail, Sep 29 | §3 | Cross-Service Coherence | REJECTED | Supports Arthur's note. Douglas is on both. Not in Julia's mailbox; no date conflict |
| P2-A2 | P2 | "latest teams/social changes" | DM D079SNE2TL4 | §3 | Cross-Service Coherence | REJECTED | Names only teams and social |
| P2-A3 | P2 | `reviewed` after `closed` | `#468#ev_6` | §3 | Cross-Service Coherence | REJECTED | `created_at` null as in base; the answer does not read it |
| P2-A4 | P2 | "hold the spend there until the pivot call" | Deck slides 2 and 3 | §3 | Cross-Service Coherence | REJECTED | Compatible if the call gates scaling; no value depends on it |
| P2-A5 | P2 | "Queue manager is in progress" | SQL L169; Trello card 63 | §3 | Cross-Service Coherence | REJECTED | Comment 16:20:37, tick 16:40:22; sequential |
| P2-A6 | P2 | "still set to the October range" | SQL L148; repo | §3 | Data Exists | REJECTED | Unconfirmed in code, not contradicted; sprites are LFS pointers |
| P2-A7 | P2 | "Separately" | SQL L148; #472 diff | §3 | Cross-Service Coherence | REJECTED | Path is real and the comment states the change of topic; a difficulty point |

P2's four findings on the previous hash (post-merge #473 note, ZOM-542 wording, hold end, missing link) all cite text the revision changed. I opened each changed statement; all four are closed on this hash.

**Rulings on DR5, DR6 and DR7.** Each stands or falls on the brief, which the prompt incorporates and which defines the Still to do cell: "For each beat, what still has to land before it runs for bought users (prod deploy, config, player-facing art an owner has flagged) and who owns it. Not what already shipped, not analytics, not polish nobody flagged."

- **DR5, premium buy on a prod build: REJECTED.** Reading B rests on the clause "an unverified build or platform is a still-to-do". That clause is the second half of "An established failure holds it; an unverified build or platform is a still-to-do, not a hold", so it sorts failure reports, and no record reports a premium buy failure on prod. A test is also not a prod deploy, config or art. Oliver's Sep 12 ask has later records on the same issue: Vincent, Sep 16: "After purchasing premium pass, lives are reset to 8 after every win."; Leonard, same day: "Playing submission candidate." and "This is production build"; spec: "Reached production in the week of"; Arthur: "Season Pass schedules are already running on prod". The spec's "No Season Pass purchase has been recorded yet" is a sales statement. **This is the weakest of the three.** No record says in words that the buy passed on a prod build. A reviewer who reads the clause as covering any untested feature would keep this fork, and a kept set fork is a UGT fail.
- **DR6, #477 title change: REJECTED.** The commits are "Changed titled to collect and win main screen header" and "Change text on Collect And Win info screen". #477 is a client PR, and the brief says a beat starts "not when its client PRs merged". Its analytics are out by name. The title change is not a deploy, config or art, and no persona-visible note says it must land first, unlike Arthur's "The final vial models are missing" and Marcus's "is still to do on my side". Brian's "Analytics and name changes first" is in #zm-collect-win, which Julia cannot read, and it sets priority, not a gate. SC-18 also bars relying on the PR's state.
- **DR7, ZOM-563: REJECTED.** The list is "For each beat", and a beat is "an event window, a reset or a start push". The ticket's title is "Teams' lives, golden frames and names not working on prod env", with no project link and no Season Pass mention. The tie to Season Pass is the reader's own step from a separate leaderboard report. SC-16 also bars using this ticket's status.

All three alternatives are additive: each keeps every item in Reading A and contradicts none. That is why the rubric note above matters, but it is not the ground for rejection. The ground is the quoted definition.

Effect on verdict: unchanged from the revised draft. No dimension changed in the recheck. Clarity moved from 3 to 5 earlier, because of the SQL revision.

Fork list:
- F1: Weekly leaderboard hold end | Until the fix is confirmed on prod | A named instant, or all four weeks | Settled by: "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date."
- F2: Quest rollover Still to do | Nothing | ZOM-534 day-boundary case | Settled by: "That is on main, so nothing else has to land for the beta."
- F3: New November config date | before Oct 31 00:00 UTC | Wed Oct 29 | Both fair: before Oct 31 00:00 UTC or Wed Oct 29, BOTH_FAIR_FIGURE; the rubric must accept either
- F4: Season Pass First window | Oct 1 00:00 UTC | Nov 1 or Oct 6 00:00 UTC | Settled by: "A beat starts with the first window that opens after its server windows are live on prod"; "Season Pass schedules are already running on prod"
- F5: Season Pass Still to do | Two items | Plus premium buy check | Settled by: "An established failure holds it; an unverified build or platform is a still-to-do, not a hold."; "After purchasing premium pass, lives are reset to 8 after every win."
- F6: Collect & Win Still to do | Three items | Plus #477 title change | Settled by: "not when its client PRs merged"; "(prod deploy, config, player-facing art an owner has flagged)"
- F7: Season Pass Still to do | Two items | Plus ZOM-563 prod deploy | Settled by: "For each beat"; "Teams' lives, golden frames and names not working on prod env"
- F8: Weekly leaderboard held | Held | Not held, a reset that needs a restart | Settled by: "it still does not start a new week. I killed the app and reopened it twice"
- F9: Collect & Win first window | Fri Oct 10 00:00 UTC | Held, or Wed Oct 8 | Settled by: "A beat that is only waiting on that release starts late, it is not held."; "so a window the release instant pre-empts does not count."
- F10: Reply to Brian | Required on the Sep 26 mail | Not required | Settled by: "its owner is told in a reply on the mail where they committed to it."
- F11: Halloween one-off | Off | In a recurring slot | Settled by: "pulling my ok. Take it off the beta calendar"

Fix-text check (deep_recheck step 5): no prompt, SQL or OE rewrite is proposed. The rubric notes use only values quoted above: the lock derives from "locked 24h before each season opens" and "opens on Sat Nov 1"; the owners come from their records. Item 5 is a plain description with no wording.

Platform defects: none scored. `[PERSON_NAME_2549]` in PN rows 7 and 14 is the source string. FD-2880 limited P1's commit search for ZOM-534; the git history settled it.

### FINAL VERDICT: PASS

Score: 5

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Next action: Proceed to /hardness on SQL 0e8c8ad8…f815, and carry the four rubric notes into /oe and /rubric.

Evidence limits: P3 and P4 ran on the previous SQL hash, with an identical prompt. The guideline PDFs in Evals/Docs could not be read (Phase 0.3 calibration only; no scored check depends on them). The catalog has no return schemas, so tool rendering, including review comments, is taken from raw records. The record was validated with read-only helper functions, not the store-bound writer. Eval 0's rev7 report was not opened. Originality is N/A. DR5's rejection rests on reading the clause within its sentence and on later records, not on a record stating the buy passed on a prod build.

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

**Lowest Dimension:** None below 5 among the 18 scored dimensions.

**Summary:** On SQL 0e8c8ad8 the prompt is a short, natural delegation whose premises all check out, and every required record is visible to Julia. Every decision, write and destination resolves from the prompt, Frederick's message, the brief and the newest applicable record, with one both-fair figure for the new config date. The three additive forks were each ruled out by the brief's definition of Still to do; DR5 is the closest call.
