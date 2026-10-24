**Long-Horizon Task Guidelines**

*How to build a task that genuinely needs 100 or more tool calls — and how the minimum is counted now that Oracle Events exist.*

## **Change log**

| Date | Updates |
| :---- | :---- |
| Sep 26, 2026 | Rewritten for Spec V2. Tool-call minimum now attaches to the golden run — a rollout scoring 100% on the rubric — where one exists. Super-Long-Horizon marked paused. Difficulty bands updated to the spec's numbers. Hint and golden-solution references removed. Examples rebuilt on the ML-selected task. |
| Aug 2026 | Original release. |

## **1 · The tiers**

| Tier | Tool calls | Share of the project |
| :---- | :---- | :---- |
| **Normal** | 50 – 100 | 50% |
| **Long-Horizon** | 100 – 500+ | 50% |
| Super-Long-Horizon | 500+, roughly three to four weeks of human effort | Paused |

| SUPER-LONG-HORIZON IS PAUSED The tier still appears on the Task Type & Horizon screen in the task builder, but it is not being assigned. Everything in this document applies to Long-Horizon. |
| :---- |

## **2 · How the minimum is counted \[Changed 09/26\]**

| If your six rollouts… | …the minimum applies to |
| :---- | :---- |
| include at least one that scored **100% on your rubric** | That **golden run** alone |
| include none that scored 100% | The **average across all six** |

A **golden run** is a baseline rollout that passed every criterion in your rubric. It is something the model produced during the baseline, not a document you write. In practice, a task whose rollouts average 84 calls **meets** the Long-Horizon minimum if one of those rollouts passed everything and used 130 calls — and the same task fails the minimum if no rollout reached 100%.

| NOT THE SAME THING AS ORACLE EVENTS Oracle Events are the solution path you write and /oe checks. They are required on every task and they matter enormously, but they do not enter this calculation. Only a rollout that scored 100% changes how your tool-call minimum is measured. One golden run out of six will not put your difficulty band at risk. That gate only trips when five or more of the six pass everything. |
| :---- |

| PADDING IS ITS OWN FAILURE Blocked calls and repeated calls add nothing to real depth. An inflated tool-call count is a failing error in its own right, and it is visible in the trajectory: twenty consecutive failed searches on the same term do not read as a hundred-call task. |
| :---- |

## **3 · What makes a task genuinely long**

Length comes from **breadth of evidence and depth of reasoning**, not from the number of deliverables. A task asking for ten emails is not long-horizon; it is one task repeated ten times.

| Lever | What it adds | What it costs you if done badly |
| :---- | :---- | :---- |
| **More sources that genuinely matter** | Each additional service the agent has to reconcile adds real calls | A service touched trivially does not count and reads as padding |
| **Day-level rather than total-level data** | Forces aggregation and repeated queries rather than one lookup | Nothing, if the daily data actually exists |
| **Threads that must be read past the apparent conclusion** | Forces continued reading where the agent would naturally stop | Nothing — this is the strongest lever available |
| **A correction planted later in discovery order** | Forces re-work and re-verification of earlier findings | If the correction is reached first, it adds nothing |
| **Distractors that look authoritative** | Forces the agent to check rather than accept | Grading the distractor is a rubric defect |
| **Several write actions with real dependencies** | Each one needs its own verification first | Independent writes bolted together are bolt-ons |

### **The lever that works best**

In the ML-selected example, the highest-value structure was a Slack thread containing a message that *sounds* like a conclusion, followed by six more messages that overturn it. Opus ran 70 tool calls, got every total right, and inverted both of the consequential findings — because it stopped reading at 21:08 and the story continued until 21:54.

That is the shape to aim for. The difficulty did not sit in the volume of data. It sat in knowing when not to stop.

## **4 · A worked scale**

Here is how the ten-hour example task distributes its work. Use it to calibrate what “long” actually looks like.

| Read the channel across the launch window, \~12,100 messages  \~4 hr Reconstruct the build history from the submission messages   \~45 min Read the playable thread past the apparent conclusion        \~20 min Pull daily spend, installs and revenue by hand               \~2 hr Reconcile the design doc against the data                    \~30 min Find the PRs and confirm what each contains                  \~40 min Write the record, then raise the tickets                     \~1 hr 45                                                       total  \~10 hr |
| :---- |

Six services carry real weight: Slack, Snowflake, GitHub, Confluence, Linear and Trello. No single one of them answers more than a fraction of the question.

## **5 · The human time estimate**

Estimate how long a person would take to do this manually — no tools, no AI, no search. Then justify it sub-task by sub-task; the arithmetic has to add up to the number you entered. **The field blocks pasting.**

* **Include the dead ends.** A person without search tooling scrolls the wrong month, reads the partner channel covering the same window for a different title, and opens marketing documents belonging to the other two games.  
* **Include the workaround.** If you forced an error, count the time spent on the alternative path.  
* **Include the re-reading.** Anything overturned later has to be revisited.  
* Do not include time the agent does not spend either — the estimate is for a human doing the same work, not for a human learning the universe from scratch.

## **6 · The difficulty bands**

These are bands, not points, and the statistics are computed for you from the six baseline rollouts.

| Check | Target | Fails when |
| :---- | :---- | :---- |
| Difficulty bar | Average weighted rubric score under **90% (changed \- Oct 2, 2026\)** | The average lands at 90% or above **(changed \- Oct 2, 2026\)** |
| Calibrated baseline | pass@k threshold **50% (changed \- Oct 2, 2026\)** | Four  or more of six rollouts pass every rubric **(changed \- Oct 2, 2026\)** |
| Failure concentration | At least **two** distinct failure patterns | One signature covers more than half the failing rollouts |
| Tool call volume | Above your assigned tier | The relevant count lands under the tier, or the average is under 15 |
| Completed runs | All six complete | Three or more runs end in an error |

A **failure signature** is the specific set of rubrics a rollout failed. Two rollouts that failed exactly the same rubrics share one signature; a rollout that failed a different combination is a different signature.

| IF A BAND FAILS, CHANGE THE TASK — NOT THE RUBRIC Revise the prompt or deepen the universe. Deleting the easiest criteria to pull the average down is the tempting shortcut: it creates a missing-coverage defect, it shows up in review, and it leaves the task exactly as easy as it was. |
| :---- |

| WHERE THE TASK BUILDER DISAGREES The Difficulty & Failure-Pattern Check screen still states pass@1 under 40% and at least three distinct signatures. The numbers in the table above come from the spec and are the ones in force. Where the two disagree, the spec governs. |
| :---- |

## **7 · The Opus 5.5 pre-check**

Before committing to six rollouts you run a **single** Opus 5.5 trajectory and read it. Opus 5.5 is the strongest model available; if it breezes through on the first try, the full baseline will too.

**✓**  It failed on substantive parts rather than formatting

**✓**  It struggled with multi-step reasoning, or missed a cross-service connection

**✓**  It stopped at the message that sounded like a conclusion

**✗**  It solved the task completely and correctly

**✗**  The only misses were cosmetic, or it found everything in one or two services

**✗**  Nothing about the run surprised you

Answering “No — Opus passed too easily” blocks the rest of the task until you make it harder. That is the point of the gate.

## **8 · The baseline**

Your prompt exactly as written, six trajectories, on Opus 5.5, one run only. **Trigger the rollouts and click Next immediately** — write your Oracle Events and your rubrics while they run. Sitting and watching costs about an hour per task.

When they return:

* If you injected a forced error, open the trajectory and confirm the tool actually failed. If the agent never called it, the injection did nothing and your recovery rubrics are ungradeable.  
* If you injected an async wait, confirm the submit → check → get sequence appears. Agents have been observed bypassing the slow path and reading the data directly.  
* Note the tool-call counts, and note which rollouts — if any — passed every rubric criterion. If one did, its count is what the tier minimum is measured against. If none did, the average is.

| DO NOT TUNE TO THE BASELINE The baseline is the measurement, not the target. Revising the prompt until the numbers look right destroys the only difficulty signal the task has. |
| :---- |

## **9 · Long-horizon rubrics**

A long task produces a large deliverable, and large deliverables tempt two specific rubric mistakes.

| Temptation | What to do instead |
| :---- | :---- |
| One criterion per row of a long output | Spot-check up to five hard or edge cases per group, and add one criterion checking the volume |
| One criterion covering the whole artifact | Split it. One verifiable claim per criterion |
| Grading the same figure everywhere it appears | Grade it once, where it matters most |
| Weighting by how much work the section took you | Weight by how difficult it is for the model — a long section of literal lookups is still weight 1 |

The ML-selected example is 31 criteria for a ten-hour task. That is the right order of magnitude. Sixty would be duplicate grading; twelve would be missing coverage.

## **10 · Before you submit a Long-Horizon task**

* At least three services carry real weight, and none of them is trivially touched.  
* The tool-call minimum is cleared — measured against the golden run if any rollout scored 100%, otherwise against the six-rollout average.  
* No part of the count comes from blocked or repeated calls.  
* The human time estimate is justified sub-task by sub-task and the arithmetic adds up.  
* The Opus pre-check produced a run you would describe as struggling.  
* All six rollouts completed, with fewer than three errored runs.  
* Average weighted rubric score is under 75%, with at least two distinct failure signatures.  
* No band was met by deleting criteria.

