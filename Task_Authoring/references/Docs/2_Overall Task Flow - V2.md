> V2 source document. For V3 tasks the assignment's universe date selects Feb 14, 2026 (normal) or Oct 1, 2025 (synth-cut) — see `Task_Authoring/setup/GEN_EXECUTION.md` § 0a.

**Original Conference \- Overall Task Flow**

**The 20 steps that need your input**

*The master guideline. It walks the whole task in order and points at the specialist document wherever one exists.*

## **Change log**

| Date | Updates |
| :---- | :---- |
| Sep 26, 2026 | Rewritten for Spec V2. Seven hinting steps removed. Golden solution replaced by Oracle Events. Baseline model updated to Opus 5.5. LLM writing ban added. Tool-call minimum rule updated. Four sandboxes collapsed to one. All 22 screenshots removed — 19 showed the pre-V2 task builder, and all 22 carried a contributor username and session token burned into the image. |
| Aug 2026 | Original release. |

| SCREENSHOTS HAVE BEEN REMOVED FROM THIS RELEASE Every image in the previous version showed the pre-V2 task builder, and each one carried personal information burned into the pixels. They will be restored once a task has been built end to end under the new taxonomy. |
| :---- |

## **0 · Your assignment**

Read-only, but write it down. Five axes are fixed for you and your scenario has to fit all five.

| Axis | What it fixes | Mismatch severity |
| :---- | :---- | :---- |
| **Business function** | The part of the company the work belongs to | Non-fail if ambiguous |
| **Persona** | Who is asking, and what the agent may read | Fail if implausible |
| **Competency** | The type of work | Non-fail if ambiguous |
| **Task skill** | What the agent must be good at | Non-fail if weak |
| **Task type** | How large the task must be | Fail if under tier |

You may not switch personas. The competency drives what kind of work the task is, and does not have to be the obvious match for the persona's job title. The assigned task skill must be genuinely exercised; stacking a second is encouraged.

### **Horizon**

| Tier | Tool calls | Share |
| :---- | :---- | :---- |
| **Normal** | 50 – 100 | 50% |
| **Long-Horizon** | 100 – 500+ | 50% |
| Super-Long-Horizon | 500+ | Paused — visible on the task screen, not assigned |

| HOW THE MINIMUM IS COUNTED \[CHANGED 09/26\] A golden run is a baseline rollout that scored 100% on your rubric. If one of your six rollouts did, the minimum applies to that run alone. If none did, it applies to the average across all six. A golden run is something the model produced; it is not the Oracle Events set you write, and writing good Oracle Events does not change how the count is measured. Padding with blocked or repeated calls is a failing error in its own right. |
| :---- |

## **What changed in Spec V2**

| Change | What it means for you |
| :---- | :---- |
| **Opus 5.5** | The baseline model for the pre-check and all six rollouts. Any other model is a failing error |
| **No LLM writing** | Prompts and rubric criteria must be human-written from scratch. Rubric prefill is off, the Oracle Events field blocks pasting, and an AI-text detector screens the prompt |
| **Oracle Events** | The golden solution is gone. You write the key steps a correct agent takes, in five fields |
| **No hinting** | The hint, the reference run, the second verifier, the silver trajectory and hint cleanup are all removed. One run, one verifier |
| **Tool-call minimum** | Applies to the golden run — a rollout that scored 100% on your rubric — where one exists, otherwise to the average across all six rollouts |

## **The four stages**

| Stage | Steps | What happens |
| :---- | :---- | :---- |
| **Build** | 1–6 | Persona, universe exploration, optional friction, optional files, injection SQL, the prompt |
| **Validate** | 7–11 | /injection, /prompt, the Opus 5.5 pre-check, /hardness |
| **Ground truth** | 12–18 | Baseline rollouts, Oracle Events, /oe, /rubric, the rubric set, human time estimate |
| **Prove it** | 19–22 | Verifier, all-fail justifications, difficulty bands, submit |

| DON'T SIT AND WATCH Trigger the six baseline rollouts at step 12 and click Next immediately. You write your Oracle Events and your rubrics while they run in the background. Watching them costs about an hour per task. |
| :---- |

## **1 · Persona selection**

Use the persona you were assigned. It sets the voice, the remit and the read scope. Four services — GitHub, Trello, Linear and Contacts — are unscoped and visible to every persona. Gmail, Slack, Calendar and the Drive family are scoped and filter every read, including reads by ID. Confluence and Snowflake are not classified either way; verify access from the persona's view before you depend on them.

**Writes are never governed by the ACL.** Determine what you can write from the tool catalog. And **Universe Explorer is author god-mode** — the agent and the verifier both use the persona's scoped view, so never build on or grade against evidence only you can see.

See: Persona ACL Policy.

## **2 · Universe Explorer**

Thirteen services, one frozen clock. Everything before February 14, 2026, 00:00 UTC is the past; nothing after it has happened. Explore until you can name three services that will each carry real weight in your scenario.

Engineering is currently regenerating the synthetic Confluence and Snowflake data to match the real Drive and Excel data, and clearing personal information from the artifacts. Both remain valid task sources. If you recorded a value before the refresh lands, re-verify it afterwards.

See: Universe and Tools.

## **3 · Error injection and async wait optional**

| Setting | Behaviour | Tests |
| :---- | :---- | :---- |
| Error rate **1.0** | Fails every call — a permanent outage a retry can never clear | Workaround or escalation |
| Error rate **below 1.0** | Fails that proportion of calls, marked transient | Retry behaviour |
| **Async wait** | Search becomes submit → check → get, 30–35 seconds per call | Parking a dependency and resuming |

| THREE RULES The task must still be solvable without any tool you kill. Name the alternative path, confirm it exists, and put it in your Oracle Events. Async affects search only, never fetch. If the prompt names the exact artifact, the agent fetches it and never pays the delay. A forced error on a scoped tool is indistinguishable from an ACL denial. Prefer an unscoped service for error recovery. |
| :---- |

Both are entirely skippable. A well-built universe with no injected friction beats a broken task with a killed tool.

## **4 · Upload reference files optional**

Files uploaded here are available to the agent during the baseline run. Use them when the scenario genuinely calls for an attachment the agent has to read. If the prompt references a file, remember to paste it alongside /prompt and /oe as well.

## **5 · Injection SQL and changelog**

You add depth by seeding data — adding or editing universe records so the difficulty lives in what the agent has to discover. Six rules govern it: on the clock, consistent across services, coherent with the universe, structurally valid, reachable and findable, and natural rather than pre-solving.

Your SQL is the **only** record of what you changed. A reviewer re-injects it into a fresh environment when a re-run is needed; if it does not reproduce your universe, the task cannot be re-run at all.

See: Universe and Tools, section 6\.

## **6 · Write the prompt**

### **Rule zero — seed the context, don't type it in**

**✗**  Every requirement spelled out, exact IDs and titles, numbered steps to follow.

**✓**  Put the detail in a channel and say “check \#channel and follow what's there”. Name the problem, not the method.

### **Write it yourself V2**

Prompts must be written by you, from scratch. Drafting *or polishing* with an LLM is prohibited, and an AI-text detector runs on your prompt before anything else in the pipeline. Think about how you actually type when messaging an assistant: no capitals, no proofreading, vague where a real person would be vague.

### **The hard rules**

| Always | Never |
| :---- | :---- |
| Require real tool use | Name a tool, a parameter, or an MCP server |
| Span at least two or three services | Pre-solve it by stating the root cause |
| Sound like a real person typing | Include internal IDs a real person would not know |
| State dates absolutely | Announce an injected failure or wait |
| Ask for investigation *and* action | Format it like a document |
| Keep every sentence load-bearing | Bolt on an unrelated request |

### **The skeleton**

| \[something is visibly wrong, said the way a colleague would say it\] \[work out what actually happened\]          \<- investigation \[then do something about it\]               \<- action, across 2+ services \[a constraint, a deadline, or who to tell\] |
| :---- |

### **The ambiguity line**

**Discovery ambiguity is good.** The agent does not know where the answer is, which sources matter, or which source is authoritative — but every reasonable run ends in the same final state. **Decision ambiguity fails.** Two readings lead to two different write actions, recipients or filing locations. Unique Ground Truth has no passing middle band: 1–2 or 5, nothing between.

See: Prompt Writing.

## **7 · Eval sandbox**

One sandbox, provisioned once, open for the whole task. Five commands.

| Command | Runs right after | Checks |
| :---- | :---- | :---- |
| /injection | Injection SQL | SQL structure, references, IDs, dates, coherence |
| /prompt | Write the Prompt | Solvability, clarity, ground truth, tool mentions, naturalness |
| /hardness | Opus Difficulty Check | One Opus trajectory, uploaded as a file |
| /rubric | Rubric Instructions | Coverage, atomicity, phrasing, weights, balance |
| /oe | Oracle Events | Completeness and accuracy of the solution path |

/injection and /prompt run in parallel in two chat sessions, as do /rubric and /oe. For a parallel pair, wait for both to finish and click **Capture Files once**.

The loop is **Run → Capture Files → Save → verdict**, every time. Save takes a few seconds; wait for it. Verdicts are PASS, NON-FAIL (a pass), FAIL (blocked, no override) and NOT EVALUATED. The evals are deterministic, so fix the artifact before re-running.

| /PROMPT IS THE FEASIBILITY GUARDRAIL \[CHANGED 09/26\] With hinting removed, nothing downstream rescues a prompt that turns out to be impossible. Treat a FAIL there as fatal, not advisory. |
| :---- |

See: Eval Sandbox.

## **8 · Opus 5.5 pre-check**

Run a **single** Opus 5.5 trajectory and read it before committing to six. Opus 5.5 is the strongest model available; if it breezes through, the full baseline will too.

**✓  Proceed.** It failed on substantive parts, struggled with multi-step reasoning, missed a cross-service connection, or stopped at a message that sounded like a conclusion.

**✗  Go back.** It solved the task, the only misses were cosmetic, it found everything in one or two services, or nothing surprised you.

Answering “No — Opus passed too easily” blocks the rest of the task until you make it harder. Then run /hardness, uploading that run's trajectory JSON as a file.

## **9 · Baseline rollouts**

Your prompt exactly as written, six trajectories on Opus 5.5, one run only. Trigger them and move on.

* If you injected a forced error, confirm in the trajectory that the tool actually failed. If the agent never called it, your recovery rubrics are ungradeable.  
* If you set an async wait, confirm the submit → check → get sequence appears. Agents have been observed bypassing the slow path.

| DO NOT TUNE TO THE BASELINE The baseline is the measurement, not the target. Revising the prompt until it passes destroys the only difficulty signal the task has. |
| :---- |

## **10 · Oracle Events V2**

Write the key steps a correct agent takes, in five fields: **Action**, **Information**, **Tool / Service**, **Parameters**, **Expected Data**. Free-form text, and the field blocks pasting.

They do two jobs. They prove the task is solvable — with no hint to fall back on, nothing else does. And they drive the rubric: every action becomes an Outcome criterion.

**Completeness:** full critical path, key discovery and retrieval steps, dependencies between steps, every required write — and *no* description of what the final response should say. **Accuracy:** services match where the data lives, parameters and expected data match the universe, and following the events literally produces a correct trajectory. **No non-actions** — “the agent does not give up” is not an event.

See: Oracle Events.

## **11 · Rubrics**

Two categories. **Outcome** is the default and checks the final state. **Process** is the exception and checks something the final state cannot prove, almost always ordering. A set with no Outcome rubrics fails; so does a set that is more than half Process; so does having two or more Process criteria that fail the three-condition test.

Phrasing is **Agent \+ active verb \+ necessary context**, affirmative, self-contained, with no tool names. Weights are **1, 3 or 5**, set by **difficulty for the model** — not by importance to the user.

### **Four things not to grade V2**

* Unstated expectations the prompt never asked for.  
* A specific conclusion drawn from evidence that supports more than one reading.  
* The distractor. Grade how the agent *handles* it; ignoring it is often valid.  
* Hard-coded titles and phrasings. Grade the substance.

Rubric prefill is off. The Criteria Builder opens empty, and /rubric audits what you put in it.

See: Rubric Writing.

## **12 · Human time estimate**

How long a person would take manually — no tools, no AI, no search — justified sub-task by sub-task, with the arithmetic adding up to the number you entered. Include the dead ends and the workaround path. The field blocks pasting.

## **13 · Verifier and all-fail justifications**

Confirm all six rollouts have finished first. There is **one** verifier in V2; the second, hinted verifier and its separate rating step are gone.

Then rate any rubric that failed **every completed run**. Before writing a justification, check that the criterion is self-contained, atomic, agent-centric, grounded in the universe, flexible enough to accept alternatives, and actually required by the prompt. If any of those is false, **fix the rubric instead** — an invalid all-fail makes the task look harder than it is. Two or more invalid all-fails is a failing error.

## **14 · Difficulty bands**

| Check | Target | Fails when |
| :---- | :---- | :---- |
| Difficulty bar | Average weighted rubric score under **90% *(changed from 75% \- Oct 2, 2026\)*** | 90% or above **(changed from 75% \- Oct 2, 2026\)** |
| Calibrated baseline | pass@k threshold **50% *(changed from 67% \- Oct 2, 2026\)*** | Four  or more of six pass everything **(changed \- Oct 2, 2026\)** |
| Failure concentration | At least **two** distinct patterns | One signature covers more than half the failing rollouts |
| Tool call volume | Above your tier | Under the tier, or an average below 15 |
| Completed runs | All six complete | Three or more error out |

| IF A BAND FAILS Revise the prompt or deepen the universe. Do not delete rubrics until the numbers look better — that creates a missing-coverage defect and leaves the task exactly as easy as it was. |
| :---- |

| WHERE THE TASK BUILDER DISAGREES The Difficulty & Failure-Pattern Check screen still states pass@1 under 40% and at least three signatures. The spec's numbers, above, govern. Three other screens also carry leftover hint-flow text — Verifier Instructions describes two verifiers, Error Injection refers to “the reference-trajectory (hinted) agent run”, and Reference File Uploads mentions “both the baseline and hinted runs”. All three are stale. |
| :---- |

## **15 · How the task is scored**

| Dimension | 1–2 FAIL | 3–4 PASS | 5 |
| :---- | :---- | :---- | :---- |
| **Unique Ground Truth** | Two valid answers | *does not exist* | Every expert agrees |
| **Agent-Centric Phrasing** | Passive, or names a tool | Valid but off-pattern | Clean throughout |
| **Prompt Clarity** | Vague, or two write paths | Wording varies, action doesn't | Unambiguous |
| **Truthfulness** | One major or two minor errors | One minor error | All verified |

See: QC Companion for the worked bands, and Common Errors and Pre-QC for the full failure-mode register.

## **16 · How you are scored, and where to get help**

Tasks are scored 1–5 at both the attempt layer and the reviewer layer. **Two consecutive tasks scoring 4 or above that pass through to the delivery layer promotes you.** A **2** means fixable errors and visible potential — not a removal. A **1** means spam or an unrecoverable task. **Two consecutive scores of 2 or below disables the account**, as does suspicious behaviour or spam.

QMs and CSMs are in the War Room while you task, with support concentrated on prompt and rubric quality. Three breakout rooms: **attempters**, **reviewers**, and **blockers** with a floating QM or CSM. Your first task is live-reviewed by a QM, so you get direct feedback before habits set.

## **17 · The guideline set**

| Document | What it covers |
| :---- | :---- |
| **Change Log** | Everything that changed in V2, in one table |
| **Overall Task Flow** | This document — the whole task in order |
| **Universe and Tools** | The company, the thirteen services, the clock, the depth bar, seeding rules |
| **Persona ACL Policy** | What the agent can read, what it can write, Access Control tasks |
| **Prompt Writing** | Naturalness, the hard rules, difficulty characteristics, the ambiguity line |
| **Oracle Events** | The five fields, completeness and accuracy, converting to rubrics |
| **Rubric Writing** | Categories, phrasing, weights, the four prohibitions, all-fails |
| **Eval Sandbox** | The five commands, what to paste, the loop, reading verdicts |
| **Long-Horizon Task** | The tiers, the tool-call minimum, human time, difficulty bands |
| **Common Errors and Pre-QC** | All 65 live failure modes, and the pre-submission checklist |
| **QC Companion** | The four scored dimensions, band by band |
| **Example Task** | The ML-selected task, end to end |

