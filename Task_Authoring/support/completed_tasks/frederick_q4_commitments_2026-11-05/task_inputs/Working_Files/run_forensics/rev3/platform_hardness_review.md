# Hardness review (Opus observed)

## 1. Scope

- Review: chat review, attempt 6ae9909f707bc2aa0a7ed6e9, `/hardness`, mode `OPUS_OBSERVED`, spec `Evals/1A_Hardness_Eval.md` (model-aware-v3)
- Review date: 2026-11-03
- Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
- Universe: `Universe_SynthCut/` (hg4-synth-sep30cut v16); provenance `Evals/references/universes/synthcut/universe_manifest.json`
- Authority contract: `prompt-incorporation-v1`

**Reviewed input fingerprints (SHA-256)**

| Input | Saved path | SHA-256 |
|---|---|---|
| Prompt (rev 6) | `Evals/task_inputs/04_Prompt.txt` | 32f7ab0cabd613da0dc4797a9d2f82afcb5b4ed76db1255d507261f98b225dac |
| Task details (rev 2) | `Evals/task_inputs/00_Task_Assigned_Inputs.md` | 7460cb5f1b4e282b0aa7812786d42e7ee12c342709a2aea0c26d89088e7f0077 |
| Injection SQL (rev 5) | `Evals/task_inputs/01_Universe_Inject.sql` | 2176eb708f74d57e4acfae369ce2acf107f2f119e085b69522f13b37cf19d551 |
| Opus run (Run1_trajectory.json) | `Evals/task_inputs/opus/trajectory.json` | d5dc726b6150ffe83595926de4711a6c17f02d2ff3af25accc8c27789d7ca0f1 |

No prompt reference files: the prompt points only to environment records (Leonard's email and what it links to).

**Run provenance.** The export's init record has `model: claude-opus-5-5[1m]`. Assistant messages carry `model: claude-opus-5-5`, and the result record's `modelUsage` names `claude-opus-5-5` as the canonical model. Claude Code 2.1.280, session caca6d91-2f1d-451f-8671-00c36fc7c06b. The run has 772 records and ends in a `result` record (`subtype: success`, `terminal_reason: completed`, 266 turns), with no subagents. The first user turn is the saved prompt word for word, with no added hint text, so the run is unhinted. Its tool results return the injected records (Leonard's Sep 30 email, the guardrails doc, the README, the keep-running card), so the overlay was live in this run.

**Assignment.** Persona Frederick Stone, Co-founder. Task type long-horizon, difficulty mode **easy**.

## 2. Input and authority issues

- None blocking. The SQL was treated as a static overlay. The run's tool results confirm the injected records it relied on.
- **Incorporation chain.** The prompt says "going by his email for what needs doing and how we decide each one". Leonard's Sep 30 email (Gmail thread ...784171) brings in four sources: the runway guardrails doc, "the one change I posted in #executives on Monday" (Slack, Sep 29, 17:15 UTC), "ESG's note about signing" (ESG's Sep 24 email, plus Leonard's Sep 25 reply on that thread about cards on the founders' board To Do list and the intake checklist), and "the README in the folder has the columns". So the README's column definitions and its Contacts rule ("only add someone who isn't in Contacts already") are incorporated. The ESG intake checklist comes in through Leonard's Sep 25 reply on the ESG thread, which the email incorporates.
- **Not incorporated (facts only):** Robert's Sep 25 Slack opinion ("cancel every marketing tool"), the stale Jul 31 "Vendor & partner tracker" sheet and the UA spend buckets doc.

## 3. Checklist

| Check | Status |
|---|---|
| Model, unhinted status and task match confirmed | NEW, done |
| Requirement map built from the prompt and incorporated sources | NEW, done |
| Material tool calls, writes and final response reviewed | NEW, done (all 265 main-agent calls indexed; every write payload read) |
| Source checks on the deciding records (base and SQL) | NEW, done |
| Persona and ACL access for the missed item | NEW, done (Linear is unscoped per `acl.md`; the Gmail record is in Frederick's own mailbox) |
| Output capability (Sheets, Trello, Calendar, Gmail, Contacts) | SUPPORTED: every write returned success in the run |
| Narrow-miss, failure-pattern and tool-call lines | NEW, done |

## 4. Requirement map and outcomes

Each company's expected decision comes from the guardrails doc (first rule that fits), with the Monday change, ESG's note and Leonard's Sep 25 reply applied.

| # | Requirement | Expected (source) | Observed (trajectory call #) | Outcome |
|---|---|---|---|---|
| R1 | Scope: everyone engaged with an offer, trial, quote, terms or ask, minus cold pitches, ad networks, PlayableX, Craftsman+, Singular, investors and Mattel | 34 injected companies plus base-data Balancy, **plus Nintendo** (developer-portal terms, see R6). Nova Rewards withdrew its offer (Sep 23), so it is out. Rayking was only forwarded internally, so it is out. | 35 companies logged, Nova and Rayking correctly left out. **Nintendo never considered**: its registration mails appeared once in a list (#25) and were never opened. No Linear call was made. | MATERIAL_FAIL (Nintendo only) |
| R2 | Answered: Motive Forge (Arthur, Sep 19 email), Spotlight Fest (Robert, Sep 17 call and Slack), Lanternfly (Leonard's Saturday call, in a Slack DM on Sep 29), Balancy (Leonard's Sep 11 "circle back later" email, base data). No new message to any of them. | All four marked Answered, with who answered and when, and no message sent (#172). Lanternfly was correctly not taken as Fred's own "we'll take a look". | MET |
| R3 | End, cash test (10): Brightlane, Ascendo, Lingora, Panelpulse, Pixel Harbor (Fred's "I'll come back" is not an answer), Soundvault, Streamcast, Reviewly (trial turns paid Oct 20), Clipforge (Paylane notice: 20-video cap reached, so the Studio plan starts Oct 16), Wishwave (Monday change: partner-booked travel counts) | All 10 End, with correct last-day dates (#172). Clipforge cancelled in writing to billing@paylane.io, not by replying to the no-reply notice (#194). Reviewly cancelled by email to the onboarding contact, as its terms allow (#191). | MET |
| R4 | Keep (3): Vaultline, Certwell, and Pingwise ("night pager" on Arthur's card). Tell them we're staying. Next date = next bill. | All three Keep, dated Oct 12, Oct 20 and Nov 1. Pingwise told not to downgrade (#195–197). | MET |
| R5 | Sign: Playfuse (NDA on ESG template, no review), Kinetic Arcade (exclusivity, ESG), Orbit (portal, no ESG), Lumencloud (36-month term, ESG), Bundlehouse (18-month IP licence, ESG), Markward (click-through; the July "accept small stuff yourself" rule was replaced on Sep 25) | All six correct, including the July-rule trap and the ESG/no-ESG split (#172, #175–180) | MET |
| R6 | **Sign: Nintendo developer portal Global ToS and NDA.** Linear ZOM-567, comment by Arthur, Sep 25: needs acceptance by a company officer from their own login, by Oct 15, or the request lapses. No fee, no exclusivity, no IP licence, either side can end it, so no ESG review. The kits wait until after the raise, so no Q4 cash. The base Sep 4 registration mail in Frederick's inbox reads "NDA Effective: 09/04/2025", which makes it look already done. | No log row, no Trello card, not in Leonard's "waiting on Arthur or me to sign" list | MATERIAL_FAIL |
| R7 | Park (12): Glyphworks, Driftwood, Quillcraft, Loopnote, Hootline, Retainly, Benchmarkly, Tilecast, Echohall, Framewell (Leonard's Sep 26 Slack thread reply: held free to Feb 1, "treat them like the other free ones", which overrides the Nov 1 order form), Cloudlark, Pressbeam | All 12 Park, dated Jan 5 (#172) | MET |
| R8 | Log: a sheet in the Q4 commitments folder, README columns, one row per company, Decision and Next date per the README | Template copied into the folder as "Q4 commitments log". 35 rows, 7 columns, values match R2–R7 (#170, #172). Missing Nintendo row, from R6. | MET except the R6 row |
| R9 | Trello: a card for each item that needs signing, on the Harmony Games board's To Do list, company name in the title | Six cards in To Do, with company titles and due dates (#175–180). Missing Nintendo card, from R6. | MET except the R6 card |
| R10 | Calendar: one reminder per company on the January review day (Jan 5, 2026) for Park and "later" answers | 14 all-day events on Jan 5 (12 Park plus Lanternfly and Balancy), one per company (#250–263) | MET |
| R11 | ESG: one intake email per ESG agreement, with the checklist fields | Three emails (Kinetic, Lumencloud, Bundlehouse) covering all six checklist fields (#181–183) | MET |
| R12 | Written answer to everyone waiting (portals and no-reply notices excepted) | 31 vendor replies on their threads, plus the Paylane cancellation. Answered companies were not contacted. (#184–215) | MET |
| R13 | Contacts: each company's contact, company in the job field, no duplicates | 32 added with the company as job. Markward, Lumencloud and Kinetic (already present) were skipped. The Balancy contact is not in base contacts. | MET |
| R14 | Reply to Leonard on his email: what we're keeping and what's waiting on Arthur or him to sign | Replied on his thread (#264). Keep list correct. Sign list has six items and **omits Nintendo**, from R6. | MINOR_GAP, consequence of R6 |

## 5. Grouped failures and independent causes

**F1. Nintendo developer-portal terms missed (one cause, three affected outputs).**
- **Deciding records.** Linear ZOM-567 (injected) and Arthur's Sep 25 comment: the officer must accept by Oct 15, "leaving the acceptance for Leonard or me". The decoy is the base Gmail thread frederick@harmonygames.co_1842359398719557772 ("Your Nintendo Developer Registration has been completed … NDA Effective: 09/04/2025"), with related Sep 4 Nintendo mails in the same mailbox.
- **Access.** Linear reads are unscoped (`Evals/references/persona/acl.md`), and the registration mail is in Frederick's own inbox. The run's own `gmail_list_threads` result (#25) showed the Nintendo threads.
- **What the run did.** It never opened them and made no Linear call, so Nintendo got no log row (R8), no signing card (R9) and no line in Leonard's reply (R14).
- **Practical effect.** An officer acceptance due Oct 15 is not escalated, and the request lapses. This is a genuine retrieval failure: the item is in scope under Leonard's definition (terms in front of us, plus a sign-up) and can be found through the agent's own tools.
- **Strongest counter-reading.** Nintendo is a platform, not a "vendor or partner". Leonard's email defines the backlog by engagement and terms, not by vendor type, and Arthur's comment explicitly leaves the acceptance with Leonard or Arthur, which is exactly what Leonard's reply asks for. The miss stands.

**Independent causes: 1.**

No other MATERIAL_FAIL or MINOR_GAP stands on its own. All other traps were handled correctly: Framewell's Slack-thread override, the Monday travel change on Wishwave, the replaced July signing rule on Markward, the "night pager" alias for Pingwise, the Paylane cap notice and billing address for Clipforge, Lanternfly's Slack-DM "later", the ESG/no-ESG routing, Nova's withdrawn offer and Pixel Harbor's non-answer.

## 6. Narrow-miss, failure-pattern and tool-call lines

**Narrow miss: YES.** One independent cause.
- **Failed share: about 5%.** The core rests on 36 per-company decisions with their log rows, plus delivery items: 6 signing cards (7 expected), 14 reminders, 3 ESG emails, the vendor replies and the Leonard reply.
- **What the miss costs.** One decision and row out of 36, one card out of 7, and one item in the reply's sign list out of 7. Weighting the Sign decision as central still gives about 4–6%.
- **Mode.** Difficulty mode is Easy, so the loss is 10% and the limit is 90%. The failed share is below the loss.

> **Why Easy:** this run's only miss was one cause (the Nintendo developer-portal terms in Linear ZOM-567, where Arthur's Sep 25 comment leaves the Oct 15 officer acceptance with Leonard or Arthur), and it got about 95% of the task right. The baseline averages six runs, and runs that avoid this one miss score above the Easy limit (90%). Add a second, independent trap in a different part of the task (another item, source or decision), get a new unhinted Opus run and send /hardness again.

**Failure-pattern risk: NO.** Each trap is listed with the share of the weighted core it decides and this run's result:

| Trap | Share | This run |
|---|---|---|
| Nintendo (Linear correction beats the "NDA Effective" mail) | ~5% | wrong |
| Framewell (Slack thread reply beats the order form) | ~3% | right |
| Wishwave (Monday travel change) | ~3% | right |
| Markward (July rule replaced) | ~3% | right |
| Pingwise ("night pager" alias) | ~3% | right |
| Clipforge (Paylane cap notice and billing-address cancel) | ~4% | right |
| Lanternfly (Slack-DM "later", Answered plus reminder) | ~4% | right |
| ESG routing for Kinetic, Lumencloud and Bundlehouse vs the Playfuse template NDA | each ~3% | right |
| Already-answered items (Motive Forge, Spotlight Fest) | each ~2% | right |
| Nova Rewards withdrawn | ~2% | right |
| Pixel Harbor non-answer | ~2% | right |

Largest share: about 5%, which is under 30%.

**Tool calls: 265** (main-agent `tool_use` blocks). Task type long-horizon, minimum 100. Not under 90% of the minimum (90).

## 7. Correct work and usability

This was a near-complete, carefully executed run, and the result can be used as it stands except for the missing Nintendo item. Across 35 companies, every decision, Next date, reply, ESG intake email, signing card and Jan 5 reminder matches the incorporated rules. That includes every trap whose correction sat in Slack, a thread reply, a Trello checklist alias or a payments notice.

## 8. Task and environment defects

None found that affect this assessment. The run hit one tool-output size limit (`contacts_get_contacts`) and recovered from it. No capability gaps.

## 9. Unassessed scope

None material. One run only: no average, pass@1 or repeatability claim.

## 10. Score rationale

- **Band table.** Without the narrow-miss rule, F1 would at most be a bounded correction (one row, one card, one reply line). That is band 3, not 4, because nearly all core work stays correct.
- **Narrow-miss rule.** All material failure comes from one cause, and the failed share (about 5%) is below the Easy-mode loss (10%), so the narrow-miss rule sets the score to **2 (Easy, FAIL, HOLD)**.
- **Why not 1.** The run has a genuine, consequential miss.

**Suggested natural revisions (advice; the task stays the author's design).** The traps this run solved were all linked from Leonard's email or sat in obvious places:
- Leonard's email names the Monday change, and the Framewell override is a thread reply in the same channel as the vendor discussion.
- The one trap that worked was an item outside the obvious filter, in a different service (Linear).

Add a second independent trap of that kind in another part of the task. Options:
- **Another in-scope item outside the paperwork folder and inbox,** with terms or an ask recorded in another service.
- **A correction in another service** that flips one company's decision. For example, a vendor's later email revising a date or price that moves it between End and Park, or a calendar note or DM showing that someone already answered a company that otherwise looks open.

Each new trap needs its own deciding record and should change a decision plus a write (row and card or reminder).

## 11. Next action

Revise the task to add a second, independent trap, get a new unhinted Opus run on the revised task and send `/hardness` again. Changing the injection or prompt makes the earlier `/injection` and `/prompt` passes outdated, so rerun those first.

### FINAL VERDICT: FAIL

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Assessment version: model-aware-v3

Assessed model: Opus

Assessment mode: OPUS_OBSERVED

Score: 2

Execution status: COMPLETE

Difficulty: Easy

Gate decision: HOLD

Gate reason: INSUFFICIENT_DIFFICULTY

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Add a second independent trap in a different part of the task, get a new unhinted Opus run and send /hardness again.

Evidence limits: One run only; no average-score or repeatability claim.
