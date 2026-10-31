> V2 source document. For V3 tasks the assignment's universe date selects Feb 14, 2026 (normal) or Oct 1, 2025 (synth-cut) — see `Task_Authoring/setup/GEN_EXECUTION.md` § 0a.

**Common Errors & Pre-QC** 

The complete failure-mode register, and the checklist to run before you submit · Updated September 26, 2026

*Every defect the project scores, what each one looks like in practice, and how to avoid it. If you read one guideline before submitting, read section 9\.*

## **Change log**

| Date | Updates |
| :---- | :---- |
| Sep 26, 2026 | Rewritten for Spec V2 and expanded to the full register — all 65 live failure modes, each with a severity and a fix. Golden Solution modes re-expressed as Oracle Events. Two hint modes retired. Contributor scoring and promotion added. New V2 errors added: LLM-written artifacts, wrong model, tool-call minimum counted against the golden run. |
| Aug 2026 | Original release. |

## **1 · How to read this**

The project tracks 67 failure modes. Two of them — *Hint Missing* and *Low Hint Effectiveness* — are **retired**, because hinting no longer happens inside the task. The remaining **65** are all catalogued below, grouped by the artifact they attach to.

| Severity | What it means |
| :---- | :---- |
| Fail | The task fails on that dimension. One is enough |
| Non-fail | Scored and recorded, but does not fail the task on its own. Several together will pull your score down |

| HOW YOUR OWN SCORE WORKS Tasks are scored 1–5 at both the attempt layer and the reviewer layer. Two consecutive tasks scoring 4 or above that pass through to the delivery layer promotes you. A 2 means fixable errors and visible potential — it is not a removal. A 1 means spam or an unrecoverable task with no improvement potential. Two consecutive scores of 2 or below disables the account, as does suspicious behaviour or spam at any point. QMs and CSMs are in the War Room while you task, concentrated on prompt and rubric quality. There are three breakout rooms — attempters, reviewers, and blockers with a floating QM or CSM. Your first task is live-reviewed, so use the feedback before habits set. |
| :---- |

## **2 · New in Spec V2**

These are not on the historical register because they did not exist before. Each is independently capable of failing a task.

| Error | Detail |
| :---- | :---- |
| **LLM-written prompt or rubric** | Prompts and rubric criteria must be human-written from scratch. Drafting *or polishing* with an LLM is prohibited. An AI-text detector screens the prompt |
| **Sandbox used to write** | The eval sandbox may query the universe. It may not generate your prompt, your Oracle Events or your criteria |
| **Wrong baseline model** | The pre-check and all six rollouts run on **Opus 5.5**. Selecting anything else is a failing error |
| **Tool-call minimum mis-measured** | If a rollout scored 100% on your rubric, that **golden run** is what the minimum applies to. If none did, the six-rollout average is. Counting the steps in your Oracle Events set is **not** how this is measured |

## **3 · Prompt — ground truth, feasibility and clarity**

| Failure mode | Severity | What it looks like · how to avoid it |
| :---- | :---- | :---- |
| **Multiple Valid Answers** | Fail | Two careful runs end in different final universe states. “pause the worst one” when two campaigns are equally bad. Pin the artifact, the recipient and the action |
| **Action Decision Ambiguity** | Fail | Two readings lead to two different write actions — chase a person, or file a document. Say which situation is actually true |
| **Major Clarity / Specificity Issues** | Fail | The intent cannot be recovered at all. Vague about *where* the answer lives is fine; vague about *what is being asked* is not |
| **Minor Clarity / Specificity Issues** | Non-fail | The wording varies but the action does not — email or Slack DM to the same named person about the same thing |
| **Prompt Impossible Request** | Fail | The universe cannot satisfy it. Verify the evidence exists before you write the prompt |
| **Prompt Impractical Request** | Fail | Technically possible but not achievable within the task. Walk your own Oracle Events path and count the steps |
| **Prompt Feasibility with Tools** | Fail | The tools available to the assigned persona cannot do it — most often an ACL-restricted read. Check from the persona's view, not Universe Explorer |
| **Prompt Conflicting Instructions** | Fail | Two requirements cannot both be satisfied. Read the prompt back as if you had to execute it literally |
| **Prompt Impractical Secondary Request** | Non-fail | A secondary ask is unachievable while the core ask is fine. Drop the secondary ask or make it achievable |
| **Prompt Misaligned with Today's Date** | Non-fail | The prompt asks about something after February 14, 2026\. Every date must be absolute and in the past |

## **4 · Prompt — naturalness, tools and truthfulness**

| Failure mode | Severity | What it looks like · how to avoid it |
| :---- | :---- | :---- |
| **Explicit Tool Mention** | Fail | An actual MCP tool name: “run linear\_create\_issue”. Name the problem, not the route |
| **Tool / MCP Server Mentioned** | Non-fail | “via the Gmail MCP server”, or “the QuickBooks tool”. Say “check what the publisher sent us” |
| **Contrived / Unnatural Prompt** | Fail | Reads like an LLM wrote it: perfect capitalisation, enumerated steps, markdown, “Please ensure”. Type it yourself, fast, without proofreading |
| **Somewhat Contrived / Unnatural Prompt** | Non-fail | Mostly natural but with one tell — a full internal ID, or a suspiciously complete requirement list |
| **Major Factual Errors** | Fail | Wrong person, non-existent document, contradicted figure. One is enough to fail. Check every proper noun against the explorer |
| **Minor Factual Errors — two or more** | Fail | Two small inaccuracies compound into a failing score |
| **Minor Factual Errors — one** | Non-fail | A single small slip. Still worth eliminating |

| THE ENTITY TRAP The commonest major factual error is a half-remembered *real* entity. There are three Marcuses — Marcus Bennett, Marcus Lee, and a Marcus at marcus@harmonygames.co — plus an Oscar Bennett. ENG-\#\#\#\# and ZOM-\#\#\# are different series. Verify against the universe, never against memory. |
| :---- |

## **5 · Prompt — depth, investigation and assignment**

| Failure mode | Severity | What it looks like · how to avoid it |
| :---- | :---- | :---- |
| **Tool Dependence** | Fail | General knowledge answers it without touching the universe. Anchor the question to specific records |
| **Cross-service Requirement** | Fail | One service resolves the whole thing, or a second is touched only trivially. Spread the evidence across three |
| **Pre-solved** | Fail | The prompt states the root cause, leaving nothing to diagnose. Seed the symptom and the evidence instead |
| **Bolt-on requests** | Fail | An unrelated extra ask. If a sentence can be deleted without affecting anything else, cut it |
| **Persona Mismatch — major** | Fail | The prompt could not plausibly come from that person, or a different persona was used |
| **Persona Mismatch — minor** | Non-fail | Plausible but strained — the remit is a stretch for that role |
| **Business Function Mismatch** | Non-fail | Ambiguous between your assigned function and another |
| **Competency Mismatch** | Non-fail | The task could equally be filed under a different competency. Let the competency drive the work |
| **Task Skill Weak** | Non-fail | The assigned skill is nodded at rather than exercised. Make it central, and stack a second if it helps |

## **6 · Universe**

| Failure mode | Severity | What it looks like · how to avoid it |
| :---- | :---- | :---- |
| **Missing Universe Data** | Fail | The evidence the task needs is not there, or is not reachable by the persona. Confirm every source before writing the prompt |
| **Temporal Field Inconsistency** | Fail | A date after February 14, 2026; a comment predating its parent; created after updated. The single most common seeding defect |
| **Cross-service Referential Inconsistency** | Fail | A Slack thread about a pull request that does not exist in GitHub. Every reference must resolve |
| **Quantitative / Reconciliation Inconsistency** | Fail | A doc saying \$65 while the linked sheet says \$35, with no intent behind it. Line items must sum to their totals |
| **State / Lifecycle Inconsistency** | Fail | A ticket marked Closed whose pull request was never merged; a task Done with an open blocker |
| **Identifier / Uniqueness / Format Inconsistency** | Fail | An ID that breaks the existing pattern, a duplicate key, or an invented field |
| **Semantic / Category Inconsistency** | Fail | One programme under two names in two services with nothing connecting them. If the reconciliation is intended, say so in your Oracle Events |
| **Other Universe Inconsistency** | Fail | Anything else that makes the universe read as synthetic — business messages at 3am, AI-flavoured boilerplate in a seeded doc |
| **Minor Universe Inconsistency** | Non-fail | A small incoherence with no effect on solvability |

Run /injection the moment you finish the SQL. It catches most of the above. Remember that your injection SQL is the **only** record of what you changed — if it does not reproduce your universe in a fresh environment, the task cannot be re-run.

## **7 · Oracle Events**

These three modes were written against the golden solution. They now attach to the Oracle Events set, which replaced it.

| Failure mode | Severity | What it looks like · how to avoid it |
| :---- | :---- | :---- |
| **Incomplete solution path**registered as Incomplete Golden Solution | Non-fail | A required write is missing, a fact appears with no event retrieving it, or dependencies between steps are absent |
| **Inaccurate solution path**registered as Inaccurate Golden Solution | Non-fail | A service, ID, filter or expected value that the universe contradicts. Naming Sheets for a figure that only exists in Snowflake counts |
| **Minor inaccuracies**registered as Minor Golden Solution Inaccuracies | Non-fail | An imprecise date range or a rounded figure that does not change the path |

Two additional defects /oe flags that are not on the historical register: **non-actions** (“the agent does not give up”) and **final-response content** (“the response explains that…”). Neither belongs in an Oracle Event.

## **8 · Rubrics**

### **8.1 Overall quality thresholds**

| Failure mode | Severity | Threshold |
| :---- | :---- | :---- |
| **10%+ Major Rubric Errors** | Fail | More than one criterion in ten carries a major defect |
| **15%+ Moderate Rubric Errors** | Fail | More than 15% moderate-or-worse |
| **20%+ Minor Rubric Errors** | Fail | More than 20% minor-or-worse |
| Up to 10% Major Errors | Non-fail | Recorded but under threshold |
| Up to 15% Moderate Errors | Non-fail | Recorded but under threshold |
| 5–20% Minor Errors | Non-fail | Recorded but under threshold |

The defects those percentages are counting, in order of how often they were recorded in the last audit of 37 tasks: **incorrect** (22%), **non-atomic** (22%), **missing coverage** (21%), unauthorized (6%), overly specific (5%). Those top three are 65% of everything found.

| RUBRICS PUNISH GOOD AGENTS MORE THAN THEY LET BAD ONES THROUGH 44% of recorded issues fail a correct answer; 29% pass an incorrect one. And four out of five defects originate in the rubric itself rather than in the solution path — writing excellent Oracle Events does not save a sloppy rubric. |
| :---- |

### **8.2 Category balance and Process criteria**

| Failure mode | Severity | How to avoid it |
| :---- | :---- | :---- |
| **No Outcome Rubrics** | Fail | Outcome is the default. Every action in your Oracle Events should produce one |
| **Process-Heavy** | Fail | More than 50% Process. Tighten the Outcomes until the Process rubrics become unnecessary |
| **Process Rubric Not Needed** | Fail | Two or more Process criteria that fail the three-condition test. When in doubt, default to Outcome |
| **Missing Process Rubric** | Non-fail | A genuine ordering requirement with no criterion covering it. Ordering is the one thing an Outcome cannot prove |

### **8.3 Phrasing and framing**

| Failure mode | Severity | How to avoid it |
| :---- | :---- | :---- |
| **Rubric is not written as an action performed by the agent** | Fail | Passive voice, or a tool name anywhere. Agent \+ active verb \+ context |
| **Rubric is agent-centric but does not follow the pattern** | Non-fail | “The Agent's status update covers X” rather than “Agent sends a status update covering X” |
| **Criteria Framing** | Fail | A negatively-framed criterion with no matching explicit prohibition in the prompt. Error-recovery criteria are the usual culprit |

### **8.4 Weights**

| Failure mode | Severity | How to avoid it |
| :---- | :---- | :---- |
| **Major Criteria Weight Disagreement** | Fail | Weights set by importance instead of difficulty, or values other than 1, 3 and 5\. A 5 needs three or more difficulty axes; a 3 needs exactly two |
| **Minor Criteria Weight Disagreement** | Non-fail | One or two criteria a band off. Re-check against the four axes |

### **8.5 All-failing rubrics**

| Failure mode | Severity | How to avoid it |
| :---- | :---- | :---- |
| **2+ Invalid All-Fail Rubrics** | Fail | Fix the criteria rather than justifying them. An invalid all-fail makes the task look harder than it is |
| **One Invalid All-Fail Rubric** | Non-fail | Same fix, one instance |
| **Poor All-Fail Rubric Justification** | Non-fail | A sound criterion with an unfactual or irrelevant justification |

“All runs” means all that completed without error. If four of six completed, a rubric is all-fail only if the model failed it on all four.

## **9 · Trajectory and difficulty**

| Failure mode | Severity | What it looks like · how to avoid it |
| :---- | :---- | :---- |
| **Wrong Horizon** | Fail | The real tool-call count lands under your assigned tier |
| **Borderline Horizon** | Non-fail | Just inside the tier. Add another source rather than another deliverable |
| **Insufficient Tool Calls** | Fail | The average across trajectories is under 15, or the relevant count is under the tier. Where a rollout scored 100% on the rubric, the count is measured against that golden run rather than the average |
| **Too Easy** | Fail | pass@k over the 67% threshold — five or more of six rollouts pass everything |
| **Avg Pass Rate Too High** | Fail | The average weighted rubric score is 75% or above. Deepen the universe; do not delete criteria |
| **Too Few Signatures** | Fail | Fewer than two distinct failure patterns across the failing rollouts |
| **Signature Over-Concentrated** | Fail | One signature covers more than half the failing rollouts — a single choke point rather than real difficulty |
| **Wrong Model Selection** | Fail | Anything other than Opus 5.5 for the pre-check or the rollouts |
| **Too Many Erroneous Runs** | Fail | Three or more of six rollouts end in an error rather than completing |

| RETIRED MODES Hint Missing and Low Hint Effectiveness no longer apply. Hinting has been removed from the task, there is one agent run and one verifier, and no hint-related artifact is collected. |
| :---- |

## **10 · Pre-QC checklist**

Run this before you submit. It is ordered by how often each item is what actually fails a task.

### **Prompt**

* ☐ You wrote every word yourself, with no LLM drafting or polishing.  
* ☐ It reads like fast, unproofread typing — not like a document.  
* ☐ No tool name, no MCP server, no “the X tool”.  
* ☐ Two careful runs would end in the same final state.  
* ☐ It does not state the root cause.  
* ☐ Every sentence is load-bearing.  
* ☐ Every date is absolute and before February 14, 2026\.  
* ☐ Every name, ID and figure checked against the explorer, not memory.  
* ☐ It could plausibly come from your assigned persona, in your assigned competency.  
* ☐ At least two services, ideally three, and both investigation and action.

### **Universe**

* ☐ Every seeded date is on the clock, with created before updated.  
* ☐ Every cross-reference resolves to a record that exists.  
* ☐ Every figure reconciles, unless the disagreement is the point.  
* ☐ Every ID follows the existing format.  
* ☐ Every piece of evidence is readable from the persona's view.  
* ☐ The injection SQL reproduces your universe exactly.  
* ☐ /injection returned PASS.

### **Oracle Events**

* ☐ Every event is an observable action or discovery.  
* ☐ No event describes what the final response should say.  
* ☐ Every event names its service and its expected data.  
* ☐ Reading the set straight through produces a working trajectory.  
* ☐ Every required write appears somewhere in the set.  
* ☐ If you injected friction, the recovery or wait path is an explicit event.  
* ☐ /oe returned PASS.

### **Rubrics**

* ☐ Every explicit request in the prompt has a criterion.  
* ☐ No criterion requires something the prompt never asked for.  
* ☐ Every criterion is Agent \+ active verb \+ context, affirmative, self-contained.  
* ☐ One verifiable claim per criterion, with no duplicates.  
* ☐ Weights are 1, 3 or 5, set by difficulty.  
* ☐ At least one Outcome rubric, Process under half the set, every Process criterion passing the three-condition test.  
* ☐ No tool names anywhere.  
* ☐ No hard-coded titles or phrasings, and no grading of the distractor.  
* ☐ /rubric returned PASS or NON-FAIL.

### **Difficulty and submission**

* ☐ Pre-check and all six rollouts ran on Opus 5.5.  
* ☐ All six completed; fewer than three errored.  
* ☐ Average weighted rubric score under 75%, with at least two distinct failure signatures.  
* ☐ The tool-call count clears your tier — measured against the golden run if a rollout scored 100%, otherwise against the six-rollout average.  
* ☐ No band was met by deleting criteria.  
* ☐ Every all-fail rubric is either valid and justified, or fixed.  
* ☐ The human time estimate is justified sub-task by sub-task and the arithmetic adds up.

