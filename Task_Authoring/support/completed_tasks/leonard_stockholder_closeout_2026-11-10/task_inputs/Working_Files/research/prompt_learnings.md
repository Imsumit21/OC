# Prompt learnings for a 5/5 platform /prompt (Eval 1)

Sources (read-only): the 11 submitted `04_Prompt.txt` files under `Task_Authoring/support/completed_tasks/*/task_inputs/`, 52 distinct platform /prompt reports (`eval_reports/*prompt*`, plus the copies in `Audit-Report/` and `run_forensics/`), earlier prompt revisions in `run_forensics/rev*/04_Prompt.txt`, the completed-tasks README and each task README, the root `learnings` file (§4, §20–26, §63–66), `Evals/1_Prompt_Eval.md` (Local Overrides, §1.2–1.5, §2.6–2.8), `Evals/references/rules/prompt_qc_examples.md` and `prompt_qc_cases.json` (calibration_cases).

The main finding: across 52 reports, only **4 findings came from the prompt's wording** (2 Contrived, 1 Originality, 1 Business Function fit). About **17 UGT, 9 Clarity and 22 Cross-Service Coherence findings came from the records**. In some of those, a **scope phrase in the prompt** met records that didn't close it. Once the wording is clean, the prompt usually doesn't change any more. Vincent's prompt stayed byte-identical across 7 rounds (6 FAIL, then PASS). Robert LLC and Claire also went from FAIL to PASS without a prompt edit.

---

## 1. Task table

Word counts are from `wc -w` on the submitted prompt. Rounds are counted as platform reports on disk (F = FAIL, NF = NON-FAIL, P = PASS). The final scores are the last report's.

| Task | Words | /prompt rounds | Final verdict and dimensions below 5 | Findings that cost points (quoted) |
|---|---|---|---|---|
| claire_zm3d_halloween_art_plan | 125 | F, P, P | **PASS 5**, all dims 5 (Originality N/A) | r1 UGT 2 + Clarity 2: prompt span "open ART tickets for any new store art" gave "2 new issues (icon, iPad 12.9" set) or 4 (also Martin's exported Halloween iPhone 6.5" and Google Play sets); no record settles it". Fixed in data (Leonard: "tickets are just for store art that still has to be made"). r1 Coherence 2: "58 injected UA-library tickets are Todo … while their descriptions and comments show finished, live creatives". Soft note in r3 (no score change): "the last sentence restates Leonard's own asks after 'take his message and do it all for me', so the ask list reads a little long". |
| douglas_beta_server_signoff | 100 | NF 3, F 2, P, P | **PASS 5** | Every finding was in the data. NF: "reference a match3d-backend `prod` branch. No such branch is in the base branch export". F: ZOM-535 Todo / ZOM-504 Backlog carrying injected "client side fix … ok on 0.3.132" comments, "lifecycle inconsistencies never take the minor Non-Fail band". Praised in the PASS: "one permission conditional; no hint at the trap"; "'go ahead and do that too, no need to wait on me' settles act versus defer". |
| frederick_bridge_pipeline | 95 | F, F, P, F, NF, P×5 | **PASS 5** (r10) | r1 UGT 2: nine forks, e.g. "Play Ventures: written no (Sep 15) vs 'they didn't respond' (Sep 23) … Passed or Awaiting reply?". r2 UGT 2: Initial Capital "Awaiting reply" vs "Not contacted this round". **r4 Originality 2 (hard gate):** the rev6 prompt "own the fundraising section of the Oct 14 board pre-read" scored meaning 0.804 against an existing task. "Rewording alone won't move a meaning score; the request itself has to be a different job". The rev7 job ("who from the bridge round gets the Q4 investor update") cleared it at 0.762. r5 NF: LVP "09/07" (a Sunday) vs the Sep 9 call. |
| frederick_q4_commitments | 98 | P | **PASS 5** first round | Advisory only (Balancy in scope with no injected record). Contrived: "No opaque ids, timestamps, spec register, trap hints, hidden destinations (folder, board, calendar and thread are all named), audit wording or if-chains." |
| julia_zm_difficulty_baseline | 103 | F×6, NF, P×6 | **PASS 5** (r14) | **r1 Contrived 2: hidden destination.** "put it where it's supposed to go and share it with the people who should have it". The report: "Julia owns 'ZM monster enrage' inside the ZM Difficulty folder … and is an attendee on the 'ZM difficulty tuning' invite". Fixed to "put it in the zm difficulty folder and share it with everyone on monday's tuning invite". The other rounds failed UGT on record forks: an "Apr 21" scope start with no timezone, "35 vs 33 rows"; "ATK POWER" vs "attack power", 35 vs 36 tickets; a level-editor list "(162, 163, 201 and 250)" that skipped ZOM-173/277/315. The same report rejected "if his rules say something needs to happen on the tickets, go ahead and do that too" as a riddle or if-chain: "It names its source ('his rules') and the object ('the tickets')." |
| julia_zm3d_beta_calendar | 100 (rev1: 157) | F, F, F | **Never passed** (task moved) | **r1 Contrived 2: enumerated deliverable specs.** "work out the windows it runs in, whether it's held and until when, the push that goes with it, and what still has to land before it runs and who owns that" / "whether it goes out or waits, and if it waits, what's missing". Verdict: "restating Frederick's DM field list instead of pointing to it". r1/r3 UGT 2 + Clarity 2: the open set "what still has to land" (about 90 candidates), and the brief clause "an unverified build or platform is a still-to-do" fed no answer but made six forks. r2 Coherence 2: ZOM-521 checklist ticked vs ZOM-526 In Progress. |
| robert_llc_takeover | 130 | F, P, P | **PASS 5** | r1 UGT 2 + Clarity 2: prompt span "When you're done, the project should match the sheet" vs the project scope "One issue per thing the LLC might take from HG". The Meta VO campaign "has no issue, so one run creates a Linear issue for it and another doesn't". Also "Whoever runs an item today moves it" named nobody for AppsFlyer. Fixed in records with the prompt unchanged. The PASS calls the same sentence "a plain completion ask". |
| robert_winddown_closeout | 99 | F×5, NF×3 | **NON-FAIL 3** (best) | **Business Function 3 in all 8 rounds:** "Vendor/account close-out fits Finance / Legal / HR / Ops ('contracts … company operations') at least as well as Founders / Exec / Strategy" ("Minor (blocks a 5 only)"; "Set by the taxonomy assignment, not the prompt"). Feasibility 2: "Google Workspace's rule-8 cost is only in an unreadable Gmail PDF attachment". Coherence 2/3: FINANCE_LEDGER vs the P&L ("AWS 1,485 vs 0 and UA 2,853.64 vs 5,000"); costs-tab header year slip. |
| vincent_zm3d_release_gate | 87 | F×6, P | **PASS 5** (r7, same prompt bytes as r1) | All data. UGT 2: two incorporated rules fit one ticket. ZOM-477 fit both "Any other bug a player can see is a known issue" and "requests for design, balance or tuning changes … no call", giving "KNOWN ISSUE or NO CALL". UGT 2: build status "n/a" or "in candidate" for ZOM-429/517, then for ZOM-435/473. Coherence 2: injected "don't run on boot" vs the start script; "1.3.24 the current store build" vs App Store 1.3.38. |
| frederick_card_spend_q3 | 69 | no report on disk (README: "/prompt PASS") | PASS | — |
| frederick_account_handover | 104 | no report on disk | — | — |

Findings from outside the completed set, from `learnings`:
- robert-vendor-schedule, **Truthfulness 2**: the prompt called a Friday note "this morning", but "The platform reads the universe date 'February 14, 2026' as the persona's today (Saturday), so 'this morning' was false" (§20).
- dd-q4-claims-register, **Contrived**: "'The tab we already use' concealed a destination the persona would know". The prompt also "repeated row/column instructions, decision labels, count breakdowns and the conflict-column rule. The platform judged the combination a deliverable specification" (§4).

---

## 2. Patterns in the prompts that scored 5 on every prompt dimension

**Length and shape.** Passing prompts run 69–130 words (median about 100) in 3–6 sentences and 1–2 paragraphs. They use no bullets, no bold and no numbered steps. The one prompt that failed on length (julia beta rev1) was 157 words, and the extra words were field lists. Claire's 125 words drew the soft "reads a little long" note. Robert LLC passed at 130 because its extra words are writes, not specs.

**Voice.** First person, the persona delegating to an assistant, with contractions, in a casual-to-neutral register. Lowercase passed for Julia and Robert ("leonard dm'd me on tuesday…"). Clean spelling raises no flag. The reports' justifications: "Plain, natural request; detail lives in records" (bridge); "Natural, unpolished co-founder delegation; no spec register, hint, hidden destination or if-chain" (winddown); "short, plain delegation" (bridge, Voice match).

**Starting point (the anchor).** Every passing prompt opens with **who asked, through which channel, and when**, then hands the job over:
- "Leonard asked me in #zombie_marketing yesterday to own the art side of Halloween…" (Claire)
- "Arthur asked me in our DM for the server side of the beta sign-off before Thursday's go/no-go." (Douglas)
- "Leonard asked me in his Sep 30 email to sort out who from the bridge round gets the Q4 investor update" (bridge)
- "Leonard's email yesterday puts the vendor and partner backlog on me this week." (q4)
- "Leonard sent me a DM on Thursday night about setting up the LLC…" (Robert LLC)
- Vincent anchors on the objects instead: "the ZM store candidates Arthur cut yesterday, Android Submission #135 and iOS Submission #50? The store release ticket has the background."

The handover line follows: "Can you take it off my plate?", "Can you take care of it for me, the way he laid it out?", "Can you take his message and do it all for me?"

**Incorporation trigger.** One plain phrase points from the anchor to the rules, so the rules count as requirements and stay out of the prompt:
- "the way he laid it out" (Douglas)
- "His email lays out what he's after." (bridge)
- "going by his email for what needs doing and how we decide each one" (q4)
- "What he wants in it is in his message, and his working rules for building it are in the brief he shared with me." (Julia beta)
- "go through his ask and everything it points to and build the register the way he set it up" (Julia difficulty, PASS 5)
- "make the call on every item the way he lays it out … laid out like his draft" (Robert LLC)

The trigger also sets what can be graded. In Vincent's task the platform recorded "the QA Regression Runbook's checks are incorporated only for the new-ticket ask", and it then rejected runbook sign-off rubric rows (vincent README lesson 3).

**Destination.** Every place a write goes is named the way the persona would say it:
- Files and folders: "a plan doc and a tracker in my Drive", "the beta sign-off folder", "a Google Sheet in the Company Ops folder", "my Q4 2025 investor update folder", "my Q4 commitments folder", "my live-ops calendar sheet", "the zm difficulty folder", "a new tab of my release gate sheet"
- Boards and tickets: "the Existing Investor Update card in Trello", "our Harmony Games board", "the release ticket's description"
- Replies: "reply in Leonard's thread", "reply to him in that DM thread", "reply on his thread", "Reply in Arthur's candidates thread in #zombie-bugs"

Share audiences are named through a record the persona can see: "shared with everyone on the review so they can comment", "share it with everyone on monday's tuning invite", "share it with both of them", "share it with him and arthur".

**Writes listed as a run-on sentence, not a list.** Each write is a verb, an object and a destination, joined with commas and "and", sometimes ending with one "then". For example: "Put the gate register in a new tab of my release gate sheet, add the blockers to the release ticket's description, and file a new ZM ticket in Linear for anything the checks in the QA regression runbook turn up that nobody has filed yet. Reply in Arthur's candidates thread…" Julia difficulty's single closing "then reply" passed: "One short 'then reply' at the end; no step list."

**Reply contents as a short noun phrase, never a field list.** "with both links"; "with how many ended up in each group"; "with what I'd do and what it costs each of us a month, with the link to the sheet"; "with the two monthly totals and anything that clashes with what we already decided"; "with the QA call"; or simply "with what he asked for".

**Send vs draft and act vs defer.** Every write is a direct imperative: "reply", "send Frederick the recommendation", "comment", "assign", "open ART tickets", "file". None says "draft" or "stage". Where the source rules decide whether to act, one permission line settles it:
- "go ahead and do that too, no need to wait on me" (Douglas; "settles act versus defer")
- "go ahead and do it, you don't need to wait on me" (account handover)
- "You don't need to check with me before sending or updating anything." (card spend)
- "go with your read on the details, no need to check with me first" (Julia difficulty, winddown)

No passing prompt contains "I'll [verb]". Robert LLC's "what I'd do" is part of the reply's content, not something the persona will do.

**Conditionals.** At most one, and it is a permission conditional that names its source: "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too" (Douglas, "one permission conditional"). Julia beta's "If a beat ends up held, leave a note on its ticket so the owner picks it up" is one plain clause.

**Trap hints.** No passing prompt mentions staleness, conflict, "be careful" or a hidden problem. The traps (supersessions, decoys, leave changes) live only in the records. Scope words stay neutral: "everything that's live today", "every marketing and UA account I'm on", "every item", "anything … that nobody has filed yet". None of them carries a count.

**Dates and "today".** Relative words are fine, and each one resolves against the universe clock:
- Claire: "Yesterday/Thursday resolve to Sep 30/Oct 2; all records before the clock"
- Douglas: "Thursday = Oct 2, after the clock"
- winddown: "Friday = Feb 13; 'after the 15th' is still ahead"
- Robert LLC: the "Thursday night" DM is 2026-02-13T05:40Z, Thu 9:40pm PT

Deadlines are named future events: "before Thursday's go/no-go", "before Monday's call", "before the review", "before Friday's go/no-go", "on Monday, Oct 6, so it has to be done before then". Explicit dates appear when the persona would write them ("his Sep 30 email", "on Monday (Sep 29)").

**Identifiers.** Human-readable names only: "Android Submission #135 and iOS Submission #50" (the task is about them), "the Existing Investor Update card", "#zombie-bugs". There are no file IDs, ticket ranges or exact timestamps.

**Product names, not tools.** "in Linear", "card in Trello", "Google Sheet", "my Drive", "ART ticket", "DM". The reports scored these "Natural product language" / "Natural service names only".

---

## 3. Recurring failure points

| # | Failure (rule) | Quoted span | Where | Rule it broke |
|---|---|---|---|---|
| 1 | **Enumerated deliverable specs** (spec register) | "For each beat a player can see across those weeks, work out the windows it runs in, whether it's held and until when, the push that goes with it, and what still has to land before it runs and who owns that. Do the push plan the same way — for each beta push, whether it goes out or waits, and if it waits, what's missing." | julia beta rev1, Contrived 2 | §1.2 AI-text red flag "Enumerated deliverable specs"; "any red flag fails" (override 2026-10-05). It restated the DM's field list "instead of pointing to it". |
| 2 | **Spec register** (the combination) | rows/columns, decision labels, count breakdowns and the conflict-column rule restated in the prompt | dd-q4-claims-register (learnings §4) | §2.7 spec-sheet escalation: two or more triggers fail |
| 3 | **Hidden destination** | "put it where it's supposed to go and share it with the people who should have it" | julia difficulty r1, Contrived 2 | §2.7 hidden-destination row; calibration #42 "wherever that's actually been asked for", #47 "the same place the rest of these wind down calls have been going", #44 "answer him there too"; dd-q4 "the tab we already use" |
| 4 | **Riddle / trap hint** | "I have a nagging feeling the thing that actually bites us is not on anybody's list"; "at least a couple of the conclusions people settled on in Slack do not survive contact with the code" | calibration #31 (FAIL) | §2.7 Riddles override; the control "CPI jumped last week and I don't know which test did it" passes |
| 5 | **If-chain** | "If he asked me somewhere else, not the rules or his posts about them, to shut something off or hand it over, answer him there too." | calibration #44 (FAIL) | §2.7: "A per-case rule belongs in a seeded record, not in the prompt." Contrast the passes: Douglas's single permission conditional, and Julia difficulty's "if his rules say…" (DR11 REJECTED) |
| 6 | **Audit form** | "Find the current governing control he meant, reconcile its evidence, and complete the decision record, remediation, and handoff it requires"; "apply it to the full in-scope upload-thread cohort, reconcile the decisions chronologically, classify the outcomes, rank…" | calibration #1, #43 | §2.7 audit forms; the control "Arthur wants the merge-review stuff sorted before the next push, can you check what's still open and close it out?" passes |
| 7 | **Command list** | "First… Then… Finally…", numbered steps | Eval §1.3.1 (no completed task failed it) | One closing "then reply" passed (Julia difficulty) |
| 8 | **Tool mention** | `slack_send_message`, "use the Linear MCP server", "the GitHub tool", parameter names | Eval §1.3.4, pass/fail (none failed) | Product names pass: "in Linear", "card in Trello" |
| 9 | **Opaque ID / exact timestamp** | "January 15 at 3:47 PM", file IDs, agent IDs | Eval §2.7 (none failed) | "Android Submission #135" passed because it is readable and is the task's subject |
| 10 | **False premise about today** | Leonard's Friday 10:12 am note called "this morning" when today is Sat Feb 14 | robert-vendor-schedule, Truthfulness 2 (learnings §20) | §2.8 / §2.3: "today" is the universe date, not the Pacific day of the freeze |
| 11 | **False state premise** | "Victor said his current art-canon handoff control has the review rules." (Victor left April 2025) | calibration #43 | §2.3 state-premise list |
| 12 | **Scope phrase in the prompt that records don't close** (UGT fork from a record) | "open ART tickets for any new store art" (2 or 4 tickets) | claire r1, UGT 2 + Clarity 2 | §2.1 UGT and §2.6 Action Decision Ambiguity (different write sets). Fixed by a record: "tickets are just for store art that still has to be made" |
| 13 | **Completion claim that clashes with a record** | "When you're done, the project should match the sheet" vs project "One issue per thing the LLC might take from HG" (create the VO issue or not) | robert LLC r1, UGT 2 + Clarity 2 | §2.6 write-vs-no-write divergence; fixed in records, prompt unchanged |
| 14 | **Two incorporated rules fit one item** | "Any other bug a player can see is a known issue" vs "requests for design, balance or tuning changes … no call" | vincent r1, UGT 2 | §2.1: nothing ranks the rules. Apply every rule sentence to every item (learnings §21) |
| 15 | **Open-set rule / clause with no truth value** | "what still has to land" (about 90 candidates); "an unverified build or platform is a still-to-do, not a hold" | julia beta r1/r3, UGT 2 | learnings §63: "An open set in a rule cannot be patched item by item"; delete clauses no answer depends on |
| 16 | **Unscoped boundary in an incorporated rule** | scope start "Apr 21" with no timezone (35 vs 33 rows); "attack power in the title counts too" vs "ATK POWER" | julia difficulty r1/r4, UGT 2 | §2.1; give every date-keyed boundary its zone and every term its forms |
| 17 | **Dataset duplicate** | "own the fundraising section of the Oct 14 board pre-read" (meaning 0.804) | bridge r4, Originality 2 (hard gate) | §2.9 / STEP 0.6: change the job, not the wording |
| 18 | **Business function fit** | "own the account close-out register" assigned as Executive | winddown, BF 3 in all 8 rounds (caps at NON-FAIL) | §1.4: fits another category "at least as well". Compare Robert LLC Exec 5 "founders' strategy and money decision" and q4 Exec 5 "Co-founder covering for co-founder" |
| 19 | **Ask that cannot be fully met** | the rule-8 cost only in "an unreadable Gmail PDF attachment" | winddown r3, Feasibility 2 | Local override: "No middle band. Any explicit ask that cannot be fully fulfilled fails." Also: an injected Confluence page never loads (learnings §26) |
| 20 | **I'll / you ambiguity** | "I'll post … and send Harry …"; "stage for approval" then update tracking | QC cases …10aed, …52957 | §2.6 Delegation Clarity hard gate: an ambiguous "I'll [verb]" next to imperatives fails |
| 21 | **Over-stacking** (soft) | restating Leonard's own asks after "take his message and do it all for me" | claire r3, note only | §1.2 soft flag; escalates only together with spec triggers |

There is no direct evidence of a "vague verb" failure in the completed set. The closest are the open-population scope phrases (#12, #13, #15). The prompt text passed in each case, and the gap was that no record closed the population. Treat every scope word ("any", "every", "anything that", "should match") as a claim that the universe must close.

Process notes from the reports and learnings:
- **A PASS does not carry over.** Julia beta "/prompt r2 passed UGT, and /prompt r3 failed UGT on a clause and a note that were already in the SQL it passed" (§64).
- **/injection PASS does not clear /prompt.** "/prompt re-reads the same records for answer forks and cross-service coherence, with four blind deep-recheck passes" (§25).
- **Any edit means re-running the checks.** "A punctuation-only edit changed the prompt hash and invalidated the prior check" (§7).

---

## 4. Checklist for my prompt (most important first)

1. **Do** open with the anchor: who asked, where, and when ("Leonard asked me in #zombie_marketing yesterday…", "Leonard sent me a DM on Thursday night…").
2. **Do** use one plain incorporation trigger and leave every rule, label, column and count in that record: "the way he laid it out", "going by his email for what needs doing and how we decide each one". Know exactly which records it incorporates, because that is the gradable scope.
3. **Don't** list per-row or per-item fields, column sets, labels, preservation rules or reply formats (julia beta rev1: "the windows it runs in, whether it's held and until when, the push…" failed Contrived 2).
4. **Do** name every destination the persona knows: folder, sheet and tab, board and card, ticket field, channel and thread ("a new tab of my release gate sheet", "Arthur's candidates thread in #zombie-bugs").
5. **Don't** hide a destination or audience: never "where it's supposed to go", "the people who should have it", "the tab we already use", "answer him there too".
6. **Do** name share audiences through a record the persona sees ("everyone on monday's tuning invite", "everyone on the review so they can comment").
7. **Do** settle act vs defer and send vs draft in one line ("go ahead and do that too, no need to wait on me" / "You don't need to check with me before sending or updating anything"), and write every action as an imperative: "reply", "send", "file", "comment". Never "draft" or "stage" unless that is the deliverable.
8. **Don't** write "I'll …", "I'm going to …" or "I need to …" anywhere. A persona self-action next to imperatives fails Clarity.
9. **Don't** use more than one conditional. The only safe one is a permission conditional naming its source ("If his sign-off rules say something has to happen to the tickets…, go ahead"). No if / but-not / then-also chains.
10. **Don't** hint at the trap ("not on anybody's list", "some of this is stale", "be careful with…"). Naming the symptom is fine.
11. **Don't** pre-solve: no counts, no trap entities, no causes, no "the two that…". Use neutral scope ("every ad we're running", "every item").
12. **Do** census every scope or completion phrase in the prompt ("any new store art", "the project should match the sheet", "anything … nobody has filed yet") so the records give exactly one population. These spans produced the UGT + Clarity 2 forks.
13. **Do** resolve every relative date against the universe date: Oct 1 2025 is a Wednesday (yesterday = Tue Sep 30), and Feb 14 2026 is a Saturday (yesterday = Fri Feb 13). Never use "this morning" or "today" for an event on the Pacific freeze day. Make deadlines named future events ("before Thursday's go/no-go").
14. **Do** make every premise literally true at the clock: the requester, the channel, the date, the folder or sheet exists and belongs to the persona, nobody who has left acts, and nothing relied on postdates the clock.
15. **Do** keep it to 70–130 words, 3–6 sentences and 1–2 paragraphs, with writes joined in a run-on sentence. At most one closing "then". No bullets or numbering.
16. **Do** write in the persona's plain first-person voice with contractions. Lowercase is fine, and clean spelling is fine. **Don't** use polished connectives ("Additionally", "Please ensure") or plant typos.
17. **Don't** name tools, functions, parameters, MCP servers or "the X tool". Product names ("in Linear", "card in Trello", "my Drive", "Google Sheet") are fine.
18. **Don't** use opaque IDs, file names or exact timestamps. Readable identifiers are fine when the task is about them ("Android Submission #135").
19. **Do** keep one workflow, where every clause serves the same job. Don't restate the requester's asks after "do what he asked" (Claire's soft note).
20. **Do** frame the job as the assigned function's work so no other category fits as well. Robert winddown's "close-out register" as Executive was capped at BF 3 in all 8 rounds, while "make the call … what it costs each of us a month" scored Exec 5.
21. **Do** change the job, not the wording, when a library task is close (meaning ≥ 0.80 is a hard 2; bridge cleared at 0.762 with a different deliverable).
22. **Do** check every graded fact is readable by the persona in a readable form: not only in a PDF attachment, and never only on an injected Confluence page.
23. **Do** apply every incorporated rule sentence to every item, giving each boundary its timezone and each term its variants ("ATK POWER"). Close open sets with a rule plus a cutoff, and delete clauses that no answer depends on.
24. **Do** freeze the prompt bytes once Contrived, Clarity, Date, Truthfulness and Tool Mention are 5, and fix later forks in the records (Vincent, Robert LLC and Claire all passed with the prompt unchanged). Re-run every check after any edit, even punctuation.
