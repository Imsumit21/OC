# Hardness review (Opus observed)

## 1. Scope

- Review: chat review, attempt 6ae9909f707bc2aa0a7ed6e9, `/hardness`, mode `OPUS_OBSERVED`, spec `Evals/1A_Hardness_Eval.md` (model-aware-v3)
- Review date: 2026-11-04
- Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
- Universe: `Universe_SynthCut/` (hg4-synth-sep30cut v16); provenance `Evals/references/universes/synthcut/universe_manifest.json`
- Authority contract: `prompt-incorporation-v1`
- Why this rerun: the injection SQL moved from rev 5 to rev 8 (alias rewording of the Spotlight Fest, Framewell and Lanternfly notes, Lanternfly note threaded, Hootline terms doc removed, Clipforge and Hootline mail edits), and a new Opus run on rev 8 was supplied. The earlier report (rev 5 SQL, a different run) is history only; no score is inherited.

**Reviewed input fingerprints (SHA-256)**

| Input | Saved path | SHA-256 |
|---|---|---|
| Prompt (rev 6) | `Evals/task_inputs/04_Prompt.txt` | 32f7ab0cabd613da0dc4797a9d2f82afcb5b4ed76db1255d507261f98b225dac |
| Task details (rev 2) | `Evals/task_inputs/00_Task_Assigned_Inputs.md` | 7460cb5f1b4e282b0aa7812786d42e7ee12c342709a2aea0c26d89088e7f0077 |
| Injection SQL (rev 8) | `Evals/task_inputs/01_Universe_Inject.sql` | 69603ab4b6a4ee6c926c1d8a4ab6ba396ca531f321e877e6c06797d0e2304e6b |
| Opus run (`Run1_trajectory (2).json`, saved as opus rev 9) | `Evals/task_inputs/opus/trajectory.json` | 637c04535a86ec2221dbe920f5530ef34012d6b026618d6a22b58f522f2c872b |

No prompt reference files: the prompt points only to environment records (Leonard's email and what it incorporates).

**Run provenance.** Init record `model: claude-opus-5-5[1m]`; every assistant message carries `model: claude-opus-5-5`; Claude Code 2.1.280; session b85083c1-37df-4c1b-9247-a70265780096. 672 records, ending in a `result` record (`subtype: success`, `terminal_reason: completed`, 232 turns, `is_error: false`). No subagent records. The overlay was live: tool results return the rev 8 injected records (Leonard's Sep 30 email, guardrails doc, README, intake checklist, keep-running card, vendor threads with rev 8 wording such as Priya's "If you're not carrying on after the pilot").

**Unhinted status.** The export format has no user-prompt record (it goes init → assistant → tool results), so the prompt text itself is not in the export. No hint text appears anywhere in the export, the run's first action is a search for Leonard's recent email, and every deliverable it produced matches the saved prompt's asks. A hint would have pointed at the hidden records, and the run missed exactly those. Treated as unhinted; recorded as an evidence limit, not a material confound.

**Assignment.** Persona Frederick Stone, Co-founder. Task type long-horizon, difficulty mode **easy**.

## 2. Input and authority issues

- None blocking. SQL treated as a static overlay, never executed; the run's tool results confirm the injected records it read.
- **Incorporation chain.** Prompt: "going by his email for what needs doing and how we decide each one". Leonard's Sep 30 email (Gmail thread …1844732913254784171) incorporates the runway guardrails doc (first-fit order: Answered, cash test, Keep, Sign, Park), "the one change I posted in #executives on Monday", "ESG's note about signing" (plus Leonard's Sep 25 reply on that thread: cards on the founders' board To Do list, intake checklist) and "the README in the folder has the columns". Guardrails rule 1: "If one of us has already given them an answer, don't write to them again. Note who answered and when. If the answer was 'later', it comes back at the January commitments review."
- **Facts, not obligations:** the Slack notes by Leonard and Robert, Arthur's Linear comment and the Balancy thread supply facts that settle a company's status under those incorporated rules; they add no new obligation.

## 3. Checklist

| Check | Status |
|---|---|
| Model, unhinted status and task match | NEW, done (prompt turn absent from export; see limits) |
| Requirement map from prompt and incorporated sources | NEW, done (rev 8) |
| Material tool calls, writes and final response | NEW, done (all 231 main-agent calls indexed; every write payload and result read; only #14 search syntax error and #27 missing `jq` failed, both recovered) |
| Source checks on deciding records (base and SQL) | NEW, done (SQL l.222, 226, 229, 556, 558; base Slack parents `messages/C07C2866011/2025-09.json#/866`, `messages/D05S58U4SAK/2025-09.json#/100`; base Gmail `threads/frederick@harmonygames.co_1840501641217286806.json`) |
| Persona access to deciding records | NEW, done: Frederick (EMPLOYEE_0008) is a member of #executives C07C2866011 and DM D05S58U4SAK (`slack/channels.json`); EMPLOYEE_0038 = Leonard Hayes, EMPLOYEE_0016 = Robert (`slack/users.json`); Linear reads unscoped (`acl.md`); Balancy thread in Frederick's mailbox |
| Discoverability of Slack thread replies | SUPPORTED: the same `slack_search_public_and_private` tool returned these thread replies and DM replies in the earlier Opus run (rev 5 wording), so search covers them |
| Output capability (Sheets, Drive, Trello, Calendar, Gmail, Contacts) | SUPPORTED: every write returned success |
| Narrow-miss, failure-pattern and tool-call lines | NEW, done |

## 4. Requirement map and outcomes

| # | Requirement | Expected (source) | Observed (trajectory call #) | Outcome |
|---|---|---|---|---|
| R1 | Scope per Leonard's definition | 36 companies: 34 injected engaged companies plus Nintendo (Linear ZOM-567) and Balancy (base thread, Leonard engaged, 1-month trial offered). Out: Nova (withdrawn), Rayking (only forwarded), cold pitches, ad networks, PlayableX, Craftsman+, Singular, investors, Mattel | 34 logged (#218); Nova and cold pitches correctly left out. Nintendo and Balancy never surfaced: no tool result in the run contains "Nintendo", "ZOM-567" or "Balancy"; the one Linear call was `linear_list_issues "Clipforge HG-2291 UGC"` (#81) | MATERIAL_FAIL (Nintendo, Balancy) |
| R2 | Answered rows, no new message: Motive Forge (Arthur, Sep 19), **Spotlight Fest (Robert, Sep 17)**, **Lanternfly (Leonard, Sat Sep 27, "later")**, Balancy (Leonard, Sep 11, "later") | Robert in #executives Sep 17 18:41 UTC (SQL l.222): "had the call about the Dec 5 indie showcase. we're sitting this one out this year, I let Rina know". Leonard in DM D05S58U4SAK Sep 29, thread reply (SQL l.229): "I rang Wen back on Saturday about their Southeast Asia deal and let them know Southeast Asia has to wait until after the raise. we'll pick it up again in January" | Motive Forge correct (Answered, Arthur, Sep 19, not contacted). Spotlight Fest logged **End** and Rina emailed a no (#152). Lanternfly logged **Sign** (see R6). Balancy absent | MATERIAL_FAIL (Spotlight, Lanternfly, Balancy) |
| R3 | End, cash test (10): Clipforge, Pixel Harbor, Brightlane, Soundvault, Reviewly, Streamcast, Lingora, Panelpulse, Ascendo, Wishwave | Clipforge: Paylane cap notice, cancel to billing@paylane.io; Wishwave: Monday change; Pixel Harbor: Fred's "I'll come back" is not an answer | All 10 End with correct last-day dates (#218); Clipforge cancelled to billing@paylane.io (#140) and Priya told (#141); Reviewly cancelled to its contact (#142) | MET |
| R4 | Keep (3): Pingwise ("night pager"), Vaultline, Certwell; tell them we're staying; next bill date | All three Keep, Nov 1 / Oct 12 / Oct 20; staying emails (#153–155) | MET |
| R5 | Sign (6 found): Kinetic (ESG), Lumencloud (ESG), Bundlehouse (ESG), Orbit (portal), Markward (July rule replaced), Playfuse (template NDA, no ESG) | All six correct, ESG/no-ESG split right, three correct ESG intake emails (#174–176), six correct To Do cards (#178–180, #182–184) | MET |
| R6 | **Sign: Nintendo** portal Global ToS and NDA (ZOM-567, Arthur Sep 25, SQL l.558): officer acceptance by Oct 15, "no fee, no fixed term, no exclusivity, nothing about our IP" → card, no ESG, no contact, no vendor reply | No row, no card, absent from Leonard's sign list | MATERIAL_FAIL |
| R7 | **Lanternfly** not a Sign item (Answered, Leonard, later) | Leonard's DM (SQL l.229) | Logged Sign; ESG intake email sent opening a legal matter (#177); Trello card "Sign: Lanternfly Publishing … ESG review first" (#181); Wen told it is "with our lawyers for review first" (#159); listed in Leonard's sign list (#231). The run's own summary flags it: "your Sep 10 'we'll get back to you' wasn't treated as an answer … I put it in the sign-after-ESG group" | MATERIAL_FAIL (same cause as R2 Lanternfly) |
| R8 | Park (12): Framewell, Hootline, Glyphworks, Cloudlark, Echohall, Pressbeam, Retainly, Quillcraft, Tilecast, Benchmarkly, Loopnote, Driftwood | **Framewell**: Leonard's #executives thread reply Sep 26 (SQL l.226): "Maren called me back about the Pro plan. they'll hold it at no charge until Feb 1 with nothing to sign before then … treat them like the other free ones"; Maren Holt is Framewell's contact ("Framewell Pro for Harmony Games") | 11 Park correct. Framewell logged **End** (Oct 15) and Maren told "We're going to pass on Pro for now, so please don't set it up for Nov 1" (#144) | MATERIAL_FAIL (Framewell) |
| R9 | Log: "Q4 commitments log" in the Q4 commitments folder, README columns, one row per company, Decision/Answered by/Next date per README | Sheet created in folder d_80a8c04753ba82ba4ba6a5 (#216), 7 README columns, 34 rows (#218). Wrong rows: Spotlight, Lanternfly, Framewell; missing rows: Nintendo, Balancy | MET in form; 5 rows wrong/missing (consequence of R2/R6/R7/R8) |
| R10 | Trello: one card per Sign item on the Harmony Games board To Do list, company in title | 7 cards in To Do (#178–184): 6 correct, 1 wrong (Lanternfly), Nintendo missing | Consequence of R6/R7 |
| R11 | Calendar: one Jan 5, 2026 reminder per company that comes back in January (12 Park + Lanternfly + Balancy = 14) | 11 all-day Jan 5 events (#220–230), one per company, all correct. Missing Framewell, Lanternfly, Balancy | Consequence of R2/R8 |
| R12 | Written answer to everyone waiting; none to already-answered companies | 32 vendor replies plus the Paylane cancellation (#140–173). Correct except: Rina (#152) and Wen (#159) should not have been written to again, and Maren (#144) got a wrong answer (a no instead of "we'll pick it up in January") | Consequence of R2/R8 |
| R13 | ESG intake: one email per ESG agreement, checklist fields | 3 correct (Kinetic, Lumencloud, Bundlehouse) plus 1 spurious (Lanternfly, #177) | Consequence of R7 |
| R14 | Contacts: each company's contact, company in job field, no duplicates | 31 added with company as job (#185–215); already-present Kinetic, Lumencloud, Markward contacts skipped. Balancy contact missing | MINOR_GAP (from R1 Balancy) |
| R15 | Reply to Leonard on his email: what we're keeping and what's waiting on Arthur or him to sign | Replied on his thread (#231). Keep list correct. Sign list has 7 items: includes Lanternfly (wrong) and omits Nintendo | Consequence of R6/R7 |

## 5. Grouped failures and independent causes

Each cause rests on a different deciding record and a different company; a run could make any one without the others.

**F1. Lanternfly: Leonard's "later" answer missed (DM thread reply).** Deciding record: DM D05S58U4SAK, Leonard, 2025-09-29 19:31 UTC, a thread reply under his Sep 17 "we have no localization though" (SQL l.229–230; parent base `messages/D05S58U4SAK/2025-09.json#/100`). It names only "Wen" and "their Southeast Asia deal"; Wen Halvorsen is Lanternfly's partnerships contact. The run searched Slack for "Lanternfly" (#86, no hits) and never searched the contact name or opened the DM. **Affected outputs:** log row (Sign instead of Answered by Leonard, Sep 27), a spurious ESG matter (#177), a wrong Trello card (#181), an email to Wen contrary to rule 1 that contradicts what Leonard told them (#159), a missing Jan 5 reminder, and a wrong line in Leonard's sign list (#231). This is the largest single miss.

**F2. Framewell: Leonard's Sep 26 note missed (#executives thread reply).** Deciding record: SQL l.226, thread reply under an unrelated "Playtestcloud results" post (base `messages/C07C2866011/2025-09.json#/866`), naming only "Maren" and "the Pro plan". Free until Feb 1 with nothing to sign → Park. The run decided End from the Nov 1 order form. **Affected outputs:** log row, a written refusal of a free plan already sent to Maren (#144), a missing Jan 5 reminder.

**F3. Spotlight Fest: Robert's Sep 17 answer missed (#executives).** Deciding record: SQL l.222, "had the call about the Dec 5 indie showcase … I let Rina know", 11 minutes after the "Spotlight Fest showcase call" with Rina in Frederick's calendar (SQL l.551). The run found that calendar event (#80) but not Robert's line, and decided End. **Affected outputs:** log row (End, Answered by blank), a second no sent to Rina (#152) contrary to rule 1.

**F4. Nintendo developer-portal terms missed (Linear).** Deciding record: ZOM-567 and Arthur's Sep 25 comment (SQL l.556, l.558): officer acceptance by Oct 15 or the request lapses, "leaving the acceptance for Leonard or me". The run made no Linear browsing call. **Affected outputs:** missing log row, missing To Do card, missing item in Leonard's sign list.

**F5. Balancy omitted (base Gmail thread).** Deciding record: `threads/frederick@harmonygames.co_1840501641217286806.json`: Balancy offered a 1-month trial after a call; Leonard replied Sep 11 "we'll circle back with you as soon as we get some bandwidth" (Answered, later). **Affected outputs:** missing log row, contact and Jan 5 reminder. Lower weight than F1–F4 (a base-data item that no injected record mentions), and the score does not depend on it.

**Strongest counter-readings, tested.**
- *"The alias notes are unfair."* Each note uniquely identifies its company by contact name plus offer (Maren + Pro plan; Wen + Southeast Asia deal; Rina + Dec 5 showcase; the only other showcase, Pixel Harbor's, is Oct 24). Frederick can see all three. The same search tool returned thread and DM replies in the earlier run. Guardrails rule 1 requires checking whether someone already answered, which makes these records part of the job, not trivia. The misses stand.
- *"Lanternfly as Sign is a reasonable reading."* Only without Leonard's DM. With it, rule 1 is the first fit and stops the order.
- *"Shared root cause: no broad Slack sweep."* F1–F3 share a behaviour, but they rest on three different records about three companies, and F4 (Linear) and F5 (Gmail) are unrelated to Slack. Grouping F1–F3 as one cause would still leave three independent causes.

**Independent causes: 5** (at least 3 even under the strictest grouping).

## 6. Narrow-miss, failure-pattern and tool-call lines

**Narrow miss: NO.** Independent causes: 5. Failed share: **about 17%**, resting on 36 core per-company decisions with their log rows, weighted centrally, plus delivery items (7 Sign cards, 14 reminders, 3 ESG intakes, vendor answers, the Leonard reply):
- Decisions/rows: 5 of 36 wrong or missing (~14%).
- Reminders: 3 of 14 missing (~21%). Cards: 1 wrong and 1 missing of 7. ESG: 1 spurious of 4 sent. Vendor emails: 3 wrong sends of 33. Leonard reply: 2 of 7 sign items wrong; keep list right.

Difficulty mode Easy, loss 10% (limit 90%). The failed share is above the loss and there are several causes, so the narrow-miss rule does not apply.

**Failure-pattern risk: NO.**

| Trap (deciding record) | Share of weighted core | This run |
|---|---|---|
| Lanternfly: Leonard's DM reply ("Wen", SQL l.229) | ~7% | wrong |
| Framewell: Leonard's #executives thread reply ("Maren", SQL l.226) | ~4% | wrong |
| Spotlight Fest: Robert's Sep 17 line ("Rina", SQL l.222) | ~3% | wrong |
| Nintendo: ZOM-567 comment beats "NDA Effective 09/04" | ~4% | wrong |
| Balancy: Leonard's Sep 11 "circle back" (base) | ~3% | wrong |
| Clipforge: Paylane cap notice and billing-address cancel | ~4% | right |
| Wishwave: Monday travel change | ~3% | right |
| Markward: July rule replaced | ~3% | right |
| Pingwise: "night pager" alias on Arthur's card | ~3% | right |
| ESG routing (Kinetic, Lumencloud, Bundlehouse vs Playfuse template NDA) | ~3% each | right |
| Pixel Harbor non-answer; Nova withdrawn; Motive Forge answered | ~2% each | right |

Largest share: about 7% (Lanternfly), under 30%. The run failed five traps and passed the rest, which is the spread the baseline's failure-pattern check needs.

**Tool calls: 231** (main-agent `tool_use` blocks). Task type long-horizon, minimum 100. Not under 90% of the minimum (90).

## 7. Correct work and usability

Substantial correct work remains: 31 of 36 decisions are right, including every End (Clipforge's Paylane cancellation, Reviewly, Wishwave's travel change), all three Keeps, the six findable Sign items with the right ESG/no-ESG split, 11 of 12 Parks with their Jan 5 reminders, Motive Forge as Answered, a well-formed log in the right folder with the README columns, correctly titled To Do cards and 31 correctly tagged contacts. The keep list sent to Leonard is fully correct.

## 8. Task and environment defects

None found that affect this assessment. Two non-write calls failed (#14 search syntax, #27 `jq` not installed) and the run recovered. No capability gaps; every write succeeded.

## 9. Unassessed scope and evidence limits

- The export has no user-prompt record, so the exact prompt the run received cannot be quoted from it (see Section 1); nothing suggests a hint.
- One run only: no average, pass@1 or repeatability claim.

## 10. Score rationale

- **Band 4.** Five independent material failures need correcting across every deliverable: five log rows, three missing reminders, one wrong and one missing card, a spurious ESG matter to withdraw, three vendor emails already sent that are wrong (a free Framewell plan refused; Rina and Wen written to after a founder had already answered them, with Wen told something that contradicts Leonard's call), and two wrong items in Leonard's sign list.
- **Why not 3.** The correction is not bounded to one item or one output. It spans the log, calendar, board, legal intake, outbound vendor mail and the founder reply, and some of it is external and already sent.
- **Why not 5.** The central result is still largely usable: about 83% of the weighted core is right, the keep list is fully right, and most End, Park and Sign work stands.
- **Narrow-miss and tool-call rules** do not apply (5 causes, ~17% failed share above the Easy 10% loss; 231 calls).

## 11. Next action

This gate is cleared for dependent authoring. Keep the observed failure evidence. When you write the OEs and rubric, cover the five missed items:
- Lanternfly, Spotlight Fest, Motive Forge and Balancy are Answered rows with no new email; only Lanternfly and Balancy get a reminder.
- Framewell is Park, with a "we'll pick it up in January" answer and a reminder.
- Nintendo gets a Sign row, a To Do card and a line in Leonard's sign list, with no contact, vendor reply or ESG intake.
- The reminder set has 14 entries.

### FINAL VERDICT: NON-FAIL

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Assessment version: model-aware-v3

Assessed model: Opus

Assessment mode: OPUS_OBSERVED

Score: 4

Execution status: COMPLETE

Difficulty: Hard

Gate decision: PROCEED

Gate reason: OBSERVED_OPUS_FAILURE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed with dependent authoring; retain the observed failure evidence.

Evidence limits: One run only; no average-score or repeatability claim. The export omits the user-prompt record.
