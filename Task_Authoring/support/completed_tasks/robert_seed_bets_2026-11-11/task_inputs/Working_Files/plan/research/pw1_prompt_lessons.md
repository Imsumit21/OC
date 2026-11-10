# PW1: prompt-stage lessons and candidate test (task_inputsS2)

Robert · Co-founder & Creative Director · Executive · Finance · Analysis and synthesis · Long Horizon · Easy · clock Saturday Feb 14, 2026 (normal).
Candidate: `plan/prompt_candidate.txt`, 115 words, 6 sentences. Written 2026-11-08. Read-only research: no universe search, no tool run, no SQL run.

## Bottom line

- The candidate is close. It matches no Portal Fail pattern: no hidden destination, no field list, no hint, no tool name, no item from the dossier's never-name list, no "today" or "this morning".
- One real defect: "under his message". Leonard's ask is two top-level messages, and "tell me here" sits in the second. The surface's D4 binds the first, so a fair run can miss it. Say "reply to him in #winddown".
- Cut two spans: ", payee by payee" (reads as bookkeeping and enumeration) and "and where it goes" (the next sentence says it).
- Replace "Can you take care of what he asked for?". It is word for word the LLC prompt's second sentence.
- The likeliest score below 5 is Business Function 3, the same cap the winddown task never cleared. STEP 0.6 can't be measured locally.
- Nothing about S2 has been Portal-tested. Every prediction below is my reading of past reports. No /injection or /prompt report exists for this task.

## Evidence base

- 52 Portal /prompt reports on disk, across 9 tasks: 27 PASS, 5 NON-FAIL, 20 FAIL.
- Only 3 of the 20 FAIL reports led to a prompt edit (Julia ZM r1, Julia ZM3D r1, Frederick bridge r4). In the other 17 the prompt hash stayed the same and the fix went into the SQL.
- Truthfulness, Today's Date, Tool Mention, Persona, Competency, Task Skill and Data Seeding never scored below 5 in those 52 reports.

## 1. Failures and near-misses

### 1a. What the Portal really failed

Ranked by how often it happened and how close it sits to this candidate. Rows 1 to 7 come from Portal reports on disk.

| # | Portal result | Task, round | Quoted wording | Rule | Fix that worked |
|---|---|---|---|---|---|
| 1 | UGT 2 in 17 reports (7 tasks), Clarity 2 in 9. A prompt sentence reaches further than the records settle. | robert_llc r1 | "When you're done, the project should match the sheet." The VO campaign is on the sheet with no issue, so one run creates an issue and another doesn't. | Eval 1 §2.1, §2.6; C6, C7 | Records only, prompt unchanged. The project description became "One issue per thing the LLC might take from HG or pay for". PASS 5 in r2. |
| 1 | same | claire r1 | "open ART tickets for any new store art": 2 tickets or 4. | same | Records only. Leonard's reply in Martin's thread: "tickets are just for store art that still has to be made". PASS 5 in r2. |
| 1 | same | robert_winddown, first report | "anything that clashes with what we already decided": no record defined a clash, so the list was open. | same | Records only. Doc rule 10 defined a clash. UGT 5 in the next report. |
| 2 | Cross-Service Coherence 2 in 13 reports (7 tasks), 3 in 10 more. | every multi-round task | No prompt wording involved. Examples: Todo tickets with finished comments (claire r1), a phantom Vercel label (winddown), a Layer receipt against base Slack (winddown). | Eval 1 §3.2 | SQL only. The reports say so directly: "The prompt doesn't need to change". |
| 3 | Business Function 3 in all 8 winddown reports. It caps the verdict at NON-FAIL. | robert_winddown | Whole job. "vendor close-out bookkeeping fits Finance / Legal / HR / Ops at least as well." | Eval 1 §1.4; `task_categories.md` ("Financial reconciliation" is the Finance row) | Never cleared. The task shipped at NON-FAIL 3. Same persona and function scored 5 on LLC ("founders' strategy and money decision"), and bridge scored 5 ("Investor communications for a bridge round are founder/exec work"). |
| 4 | Contrived 2: enumerated deliverable specs. | julia_zm3d r1 | "work out the windows it runs in, whether it's held and until when, the push that goes with it, and what still has to land before it runs and who owns that" | Eval 1 §1.2: any red flag fails; two triggers not needed | Point at the record: "What he wants in it is in his message, and his working rules for building it are in the brief he shared with me." Contrived 5 in r2 and r3. |
| 5 | Contrived 2: hidden destination and recipients. | julia_zm r1 | "put it where it's supposed to go and share it with the people who should have it" | Eval 1 §2.7; cases K42, K47 | Name both: "put it in the zm difficulty folder and share it with everyone on monday's tuning invite". Contrived 5 from r2. |
| 6 | Originality, Dataset Duplicate: meaning 0.804, wording 0.034. Hard cap at 2. | frederick_bridge r4 | "own the fundraising section of the Oct 14 board pre-read". The same text passed r3, before STEP 0.6 existed. | STEP 0.6 (Portal only; 0.80 is the line) | A new job, not new words: the Q4 send list. Meaning fell to 0.762. Portal: "The fix is a different task, not new wording of the same one." |
| 7 | Feasibility 2. | robert_winddown, fourth report | No prompt wording. Google Workspace's cost sat only in a Gmail PDF, which returns no bytes. | Eval 1 §2.2 | SQL. The figure went into a readable ENG-2464 comment. |

Second-hand: the primary report is not in completed_tasks, so these rest on another document's account.

| # | Result | Task | Quoted wording | Rule | Fix | Source |
|---|---|---|---|---|---|---|
| 8 | Truthfulness 2 | robert-vendor-schedule rev2 | Leonard's Friday note called "this morning". The persona's today is Saturday Feb 14. | §2.8 | Use "yesterday" or a weekday name | `learnings` §20 |
| 9 | Prompt FAIL 2, contrived | dd-q4-claims-register | "The tab we already use", plus repeated column and label rules | §1.2, §2.7 | None verified; the task was skipped | `learnings` §4 |
| 10 | Platform linter "Prompt Task Skill Weak - V2" (Marginal: enumeration, not analysis) | frederick_handover rev2 | "worked out, one row per account" | Eval 1 §1.5; C4 | "For each one, figure out who actually holds it, whether money's still moving on it, and what we should do with it." Task Skill 5 per the check | That task's `04_Prompt_Check.md`, finding 6 |

### 1b. Near-misses: raised by the Portal, then rejected

| Wording | Suspected | Portal ruling |
|---|---|---|
| A single "then" before the reply: julia_zm (13 reports), winddown (6), LLC (3), bridge (1) | Command List | Rejected 23 times out of 23: one dependency-ordered word, no first/finally. Optional rewording offered, never required. |
| "When you're done, the project should match the sheet." (LLC) | Spec register, bolt-on | Rejected: "At most one register trigger... the gate needs two." It still opened the fork in row 1. |
| "Put the plan sheet in my Drive, laid out like his draft…" (LLC r1, r3) | Spec register | Rejected: it points at Leonard's own record and is the same trigger row as above. |
| "His email lays out what he's after." (bridge r6, marked borderline) | Bolt-on | Rejected: it adds no ask and is the clause that incorporates the email's rules. |
| "work through his ask and everything it points to, build the register the way he wants it…" (winddown) | Audit form | Rejected: it names concrete, persona-known outputs, unlike #1 and #43. |
| "If his sign-off rules say something has to happen to the tickets that aren't on prod, go ahead and do that too, no need to wait on me." (Douglas; same shape in julia_zm) | If-chain, trap hint | Rejected: one conditional that grants permission and settles act-versus-defer. |
| "Leonard also emailed me about the go/no-go, so please handle what he asked for…" (Douglas) | Hidden destination | Rejected: the record is named and Leonard is the destination. |
| "before he archives anything on google after the 15th" (winddown) | Trap hint | Rejected: Leonard's own plan in his own terms. |
| "Then reply to him in that DM thread…" (LLC r3) | False state premise | Rejected: replying under his message creates the thread. |
| "Put the plan sheet in my Drive…" (LLC r3) | Shutdown premise | Rejected: the clock is before Feb 15, and Leonard's DM says keep it in your drive. |
| Claire's four-verb sentence ("Comment each ad's call… assign… open… reply…") | Over-stacking | Rejected: soft flag, 0 to 1 triggers, no bolt-on. |

### 1c. Suspected locally, never confirmed by the Portal

- "Then" as a fail: Claire's GPT red team failed "Then comment each ad's call…" and the word was dropped. The Portal rejected that pattern 23 times.
- Relative-day advisories (C20) sit in nearly every check. Today's Date scored 5 in all 52 reports.
- frederick_q4's check predicted NON-FAIL on C7 (open reminder time, reply channel). The Portal gave PASS 5 in its first round.
- julia_zm3d's check predicted NON-FAIL on C7 for "If a beat ends up held". The Portal raised no such finding.
- "yesterday" (card spend) and "this afternoon" (handover) were reworded locally on a UTC-clock worry. No Portal ruling on either is on disk.
- AI-text advisories ("The text is model-written"): every report says prompts are screened, but no report states a detector result.
- The other direction: local PASS predicted nothing. Local checks predicted PASS before the Portal failed LLC r1 and julia_zm3d r1. julia_zm3d rev14's local PASS 5 never reached the Portal.

### 1d. Evidence missing

- frederick_handover and frederick_card_spend have no /prompt reports on disk, only local checks that cite them. The raw linter output is not on disk either.
- julia_zm3d has 3 reports on disk; its author counted four failed rounds.
- julia_zm r1's prompt (hash 11634c6ef520) is not stored. I quote it from the report.
- `ugt-fork-v1`, `base-data-v1`, the Portal's known-issue list and STEP 0.6 are not in the local Evals bundle. They are known only through reports.
- robert-vendor-schedule and dd-q4-claims-register reports were outside this read list, so rows 8 and 9 are `learnings` summaries.

## 2. Wording that passed

Prompts scoring 5 on every text dimension ran 87 to 130 words. The candidate's 115 fits.

| Job | Wording | Task, Portal result |
|---|---|---|
| Opening | "Leonard sent me a DM on Thursday night about setting up the LLC so we can keep Combo Fighter going after the shutdown, and I want my answer ready before Monday's call." | LLC, PASS 5 twice |
| Opening | "Leonard's email yesterday puts the vendor and partner backlog on me this week." | frederick_q4, PASS 5 first round |
| Delegation | "Can you take his message and do it all for me?" | claire, PASS 5 twice |
| Delegation | "can you take it off my plate?" | julia_zm, PASS 5 |
| Pointer to rules | "going by his email for what needs doing and how we decide each one" | frederick_q4 |
| Pointer to rules | "His email lays out what he's after." | bridge, PASS 5 r6 to r10 |
| Named destination | "The log goes in my Q4 commitments folder" | frederick_q4 |
| Named destination and audience | "put it in the zm difficulty folder and share it with everyone on monday's tuning invite" | julia_zm |
| Named destination | "Put the gate register in a new tab of my release gate sheet" | vincent, PASS 5 r7 |
| Layout pointer | "laid out like his draft" | LLC |
| Ticket work | "make the call on every item the way he lays it out" | LLC |
| Ticket work | "settle each of the linear issues like he asked" | winddown (text dimensions all 5) |
| Order word | "When it's all done," / "Once the sheet's done," | frederick_q4; julia_zm3d (Contrived 5) |
| Closing reply, pointer | "reply to leonard in the dm with what he asked for" | julia_zm; same in Douglas, frederick_q4 |
| Closing reply, named contents | "reply on his thread with how many ended up in each group" | bridge |
| Closing reply, named contents | "reply to him in that DM thread with what I'd do and what it costs each of us a month, with the link to the sheet" | LLC |

No permission line is needed. LLC passed without one, and the candidate has no "I'll" beside an imperative.

## 3. The candidate, line by line

"Fine" means leave it. Severity words follow the playbook. The S2 facts below come from `01_Universe_Inject.sql`, `plan/wording.json` and `01_Gradable_Surface.json`.

| # | Span | Verdict | Risk | Rule | Suggested wording |
|---|---|---|---|---|---|
| 1 | "Leonard asked me in #winddown on Thursday" | Fine. Advisory on the opening. | True: the ask @-mentions Robert, Thu Feb 12 5:23 pm PT (2026-02-13T01:23Z). LLC passed the same Pacific reading ("Thursday night", 05:40Z). The first six words match the winddown prompt's opening. | §2.3, §2.8; C17, C20, C23 | Optional: "On Thursday in #winddown Leonard asked me for…" |
| 2 | "for one straight page on what each bet cost us to build and what it brought in" | Fine | A 16-word lift from the ask, but it is the ask's headline, not a rule. "Bet" carries the strategic framing. "Brought in" touches NB-26 for Combo Fighter; the method fixes the source ("as recorded"), so grade only the $11.75 table total. | C9, C16; playbook "Known data issues" | Keep. Run `hardness_v2_check.py` on the final text; I did not run it. |
| 3 | "ahead of his angel calls on Tuesday" | Fine. Do not cut. | This is the span that makes it investor work, which guards Business Function. Tue Feb 17 matches the calendar event, and it is a future date. | §1.4, §2.8 | Keep |
| 4 | "Can you take care of what he asked for?" | Change. Advisory. | Word for word the LLC prompt, same persona and clock. §2.9 is N/A with no supplied sample, so this won't fail /prompt, but the archive says not to copy a prompt. | `completed_tasks/README.md`; C23 | "Can you do this one for me?" |
| 5 | "He laid out how he wants it counted" | Fine | Does the incorporation job, like bridge's "His email lays out what he's after." It names neither the doc nor a rule, and hints at no trap. | §1.2 incorporation; C8; C16 pass example | Keep |
| 6 | "and where it goes" | Cut. Advisory. | The next sentence says where it goes, so the clause fails the deletion test. Alone it sits near the hidden-destination pattern. | §1.3.2; C13 | Delete |
| 7 | "Build the sheet in my Drive" | Small change. Advisory. | The destination is named and safe. But "the sheet" has no antecedent, and sentence 1 asked for a "page". | §2.6; C7 | "Build it as a sheet in my Drive" |
| 8 | "laid out like his" | Small change. Advisory. | One register trigger at most, as ruled on LLC. LLC had a noun ("his draft"); here "his" has nothing to refer to. | §2.7 register; LLC DR14, DR15 | "laid out like his working sheet" (add it to the brief's anchor table) |
| 9 | "and share it with him and Blake" | Fine | Named audience. Leonard's own word; LLC's check showed "Blake" resolves to one person. | §2.7; C17 | Keep |
| 10 | "Work through the Payee history project in Linear the way he wants" | Fine | AN2, exact name. The writes live in the method's last paragraph: readable, unique, an instruction, not an answer. | C8; C10; C14 | Keep |
| 11 | ", payee by payee" | Cut. Advisory, with a Business Function and Task Skill cost. | Names the method, not the problem. It reads as the enumeration the linter flagged in row 10, and the bookkeeping that cost winddown a 3. The method already says "each payee's issue", so no trigger is lost. | Rule zero; §1.5; C4; C16 | Delete |
| 12 | "When you're done," | Fine | Real dependency, and it avoids the "Then" search hit. | §1.3.1; C15 | Keep |
| 13 | "reply to him under his message in #winddown" | Change. Non-fail risk. | Two top-level messages exist (`…5821.640039`, `…5859.212469`), both with reply_count 0. "Tell me here" is in the second, but surface D4 binds the first. Reading A replies under the first, Reading B under the second, and a channel post also fits "tell me here". Same recipient and contents, so likely Clarity Minor (3 to 4), not a Fail. It would also make a rubric row fail a fair run. | §2.6; C7; `learnings` §5 | "reply to him in #winddown". Control: "post the summary in #winddown" passes. Widen D4 to match. |
| 14 | "with what each bet cost and brought in" | Tighten. Advisory. | Restates sentence 1 and lifts 13 words from the ask. Three content items is well short of the julia_zm3d field list, and LLC passed with this shape, so this is a preference. | §1.2; C16 | "with what he asked for" |
| 15 | "and what changes on the deck" | Keep, one word. | I tested it against the clash-list failure. It is closed: the deck has five lines. Reading B, editing the deck, is ruled out by "tell me here … what changes on the deck". It does presuppose a change, but in Leonard's words. It also adds investor framing. | §2.1; C6; C9 | "what changes on the draft deck", Leonard's own term |
| 16 | "with the link to the sheet" | Fine. Needed. | The ask doesn't request a link, so this is D3's only trigger. Six words match LLC, but they are generic. | C8 | Keep |

### Whole-prompt checks

| Check | Result |
|---|---|
| Never-name list (dossier) | Clean. No notice, SVB, Leapblock, Chase, contract, Western Union, warehouse, Deel, bucket, figure or date rule. |
| Tool names, MCP, "tool", First/Then/Finally, "I'll", "if" | Zero hits. |
| Premises | All eight hold in the SQL: the ask, Thursday, "one straight page", the Tuesday calls, the method and share line, the project name, Leonard's sheet, the deck. Nothing assumes business as usual after Feb 11. |
| Delegation | No first-person action beside an imperative. |
| Spec register | One trigger at most ("laid out like his"), two if a strict reader counts the reply contents. LLC passed three times with the same shape. Span 14's change removes the question. |
| Business Function | Likeliest sub-5. "Financial reconciliation" is literally the Finance row, and winddown's 3 was for bookkeeping. LLC and bridge show money work scores 5 when it reads as a founder or investor matter. Keep spans 2, 3 and 15; cut span 11. If it still scores 3, the pre-scenario §3 answer stands: a stronger judgment ask in the hub, not more figures. The verdict is then NON-FAIL, not FAIL. |
| Task Skill | Should hold once span 11 goes. |
| Dataset duplicate | Not measurable locally. See the map below. |

Sentence map against the LLC prompt:

| Candidate | LLC |
|---|---|
| S1 who asked, where, before which meeting | S1, same job |
| S2 "Can you take care of what he asked for?" | S2, identical |
| S4 sheet in my Drive, laid out like his, shared with him and Blake | S4, same writes, 8 words match |
| S5 work through the Linear project the way he wants | S3, same job |
| S6 when done, reply with the summary and "the link to the sheet" | S5 and S6, same job |

Three points bear on STEP 0.6:
- In LLC's report a Frederick task scored 0.708 on that frame alone ("shares only the 'Leonard DMed me, work it the way he laid out, reply in that DM' frame"). LLC, submitted since, is probably in the library now; that is my inference.
- Rewording won't move the meaning score. Bridge's fix was a new job.
- Pointer-only text may raise it. julia_zm3d went from 0.726 to 0.75 after its rewrite, on the same library build. That is one data point, but it is why sentence 1 should keep its specific content ("each bet", "angel calls").

### Suggested text

Retype this in your own voice first, since every report warns that prompts are screened for AI-written text.

> On Thursday in #winddown Leonard asked me for one straight page on what each bet cost us to build and what it brought in, ahead of his angel calls on Tuesday. Can you do this one for me? He laid out how he wants it counted. Build it as a sheet in my Drive, laid out like his working sheet, and share it with him and Blake. Work through the Payee history project in Linear the way he wants. When you're done, reply to him in #winddown with what he asked for, including what changes on the draft deck, and the link to the sheet.

### Follow-through if this is adopted

- Widen surface D4 to any reply to Leonard in #winddown, in a thread under either message or at channel level. Dropping the thread wording is what makes that fair under `learnings` §5.
- Add "his working sheet" to the brief's anchor table.
- R2's selector matches only the word "deck". Plan a real row at the rubric stage for what changes: the three cost figures and the blank revenue line.
- Run `/create-prompt-writing check` on the final hash. C17 and §5a need live `hg.py` lookups that this research did not do.
- A SQL alternative for span 13 exists: make the second message a thread reply under the first, then say "his thread". I don't recommend it. It costs a new /injection and hides the project, layout and reply asks behind a thread read.
