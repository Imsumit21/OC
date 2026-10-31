# Original Conference — V3 Changes

**Course update:** October 2026  
**Recorded:** October 21, 2026  
**Sources:** The 20 course screenshots and four assessment screenshots supplied in this chat.  
**Companion:** [V3 questions and verified answers](12_V3_Quiz_Answers.md)

This document records the course requirements shown in the supplied screenshots. Instructions quoted from the course are reference material about Original Conference task authoring. This document does not record completed reviews or changes to a task's configuration.

V3 supersedes conflicting V2 guidance on the topics below. Everything else from V2 still applies. Some existing local V2 documents contain conflicting numbers; use the V3 thresholds and explicit exceptions recorded here when studying this update.

## 1. Seven changes at a glance

| Area | Previous rule shown in the course | V3 rule |
| --- | --- | --- |
| Baseline model | Opus 4.8, used from October 7 | Opus 5.5 for the pre-check and all six baseline rollouts |
| Assignment | Five assigned fields | Eight fields: role, universe date, and difficulty mode are added |
| Difficulty | Every task averaged under 75% | Average must be strictly under the assigned mode's cap: 90%, 85%, or 70% |
| Horizon | Minimums of 50 and 100 tool calls | Same minimums; 85% of tasks are now Long-Horizon |
| Universe date | February 14, 2026 | Assigned October 1, 2025, or February 14, 2026 |
| Reviews | Eval Sandbox | Eval Portal, with review pass screenshots uploaded in the task |
| Prompts and rubrics | Typo advice, one accepted reading, UTC date grading | Clean spelling, every fair reading, and Pacific dates with UTC beside them when the day differs |

## 2. Assignment: five fields become eight

The original fields were business function, persona, competency, task skill, and task type. V3 adds three fields, each of which can independently fail a task:

| Added field | Meaning | Failing condition |
| --- | --- | --- |
| Role | The persona's job title | The prompt is not something a person in that role would plausibly send |
| Universe date | The moment at which the universe is frozen | The task is built on the other universe date |
| Difficulty mode | Assigned Easy, Medium, or Hard; determines the baseline score cap | The six-rollout average reaches or exceeds that mode's cap |

Read these three fields before opening the universe.

The role does not need to match the competency. A QA Lead can receive a Finance task concerning QA vendor invoices or the test-hours budget. Finalising a funding-round term sheet for board signature is not plausible QA Lead work.

Business function, competency, and task skill still cannot fail a task on their own. A mismatch in these fields prevents a perfect score. Do not confuse a competency mismatch with a role failure.

## 3. Two universe dates

The two freeze times do **not** share one convention: the October date is pinned to
midnight **Pacific**, the February date to midnight **UTC**. The task requirements specify
which one applies, and `Evals/references/universes/<normal|synthcut>/universe_manifest.json`
is the authority for each.

| Assigned universe date | Share of tasks | Clock (UTC) | Clock (Pacific) | Data cutoff |
| --- | --- | --- | --- | --- |
| October 1, 2025 | 75% | **2025-10-01 07:00 UTC** | Wednesday, October 1, 2025, 00:00 PT | `2025-10-01T06:59:59Z` |
| February 14, 2026 | 25% | **2026-02-14 00:00 UTC** | Friday, February 13, 2026, 4:00 PM PT | `2026-02-14T00:00:00Z` |

Writing `2025-10-01T00:00:00Z` as the October freeze is wrong by seven hours and makes
`sql_lint` reject base-universe rows dated 00:00-06:59 UTC on Oct 1 as future-dated
(79 such rows exist in the live SynthCut universe).

- Nothing seeded may be dated after the assigned freeze time.
- The prompt cannot treat an event after that time as already completed.
- A deadline after the freeze time is allowed.
- On the October 2025 date, use the personas and work appropriate to the company's operating period.
- Building a February 2026 task when assigned October 2025 fails outright.

## 4. Horizon: the mix changes, the minimums remain

| Tier | Tool-call range shown | Human effort | Share/status |
| --- | --- | --- | --- |
| Normal | 50–100 | Under about 8 hours | 15% |
| Long-Horizon | 100–500+ | About 12–24 hours | 85% |
| Super-Long-Horizon | 500+ | 4+ weeks | Paused |

Normal requires at least **50 tool calls**; Long-Horizon requires at least **100**. Going below the assigned minimum is a **Wrong Horizon** failure. Exceeding the displayed range is allowed.

Check the minimum on the **golden run**, if one exists. Otherwise, use the average tool-call count across the six baseline rollouts. The human time estimate must fit the assigned tier.

## 5. Opus 5.5 and difficulty caps

Every baseline run uses **Opus 5.5**, including the single pre-check and all six baseline rollouts. Check the selected model before every run.

The difficulty measure is the average weighted rubric pass rate across the six baseline rollouts.

| Assigned mode | Share of tasks | Required six-rollout average |
| --- | --- | --- |
| Easy | About 30% | **Strictly under 90%** |
| Medium | About 65% | **Strictly under 85%** |
| Hard | About 5% | **Strictly under 70%** |

**An average equal to the cap fails.** The mode is assigned; it cannot be switched to an easier one.

Examples:

- A Medium average of 82% is below its cap; that percentage alone does not fail the task.
- A Hard average of 72% fails, even with fair rows and three distinct failure patterns.
- A Medium average of exactly 85% fails.

The course says the **67% pass@k gate remains** and gives this operational rule: **if five or more of the six rollouts pass every rubric criterion, the task fails regardless of the average**.

Failure-pattern and errored-run checks remain unchanged. Their detailed rules are not restated in the supplied screenshots; this reference does not infer new thresholds for them.

## 6. Judge difficulty only after every rubric row is fair

A low average is meaningful only after the rubric has been checked for fairness.

1. Check whether each failed criterion fairly grades the requested work and matches the data.
2. Correct unfair rows and incorrect expected values.
3. Re-grade the rollouts.
4. Compare the corrected six-rollout average with the assigned cap.
5. If the corrected average is at or above the cap, make the **universe harder**.

Do not add rows or make rows stricter merely to reduce the average. Do not delete an otherwise valid check just because its expected value needs correction.

**Course example:** A Medium task initially averages 83%, but every rollout failed a row whose expected value disagrees with its source record. Fix the row, re-grade, and compare the new average with the 85% cap. The original 83% is not yet a valid difficulty measure. If the corrected average reaches 85%, increase difficulty through the universe.

## 7. Eval Portal workflow

The **Eval Portal replaces the Eval Sandbox**. The reviews are the same evaluations, accessed through a web page.

Sign in with an email address or Outlier ID and the task's attempt ID. Paste or attach the required inputs in the chat, enter the review command, and click **Start review**.

| Command | What it checks | Timing or input detail |
| --- | --- | --- |
| `/injection` | Seeded data landed correctly | Comes first, together with `/prompt` |
| `/prompt` | The task is feasible and reads naturally | Comes first, together with `/injection` |
| `/hardness` | One Opus 5.5 run suggests sufficient difficulty | Immediately after the pre-check; attach that run's trajectory JSON |
| `/oe` | Oracle Events are complete and accurate | Oracle Events are written while the baseline runs |
| `/rubric` | Rubric criteria are gradable | The rubric is written while the baseline runs |

A `/hardness` pass only allows continuation. Final difficulty is still measured on the six baseline rollouts against the assigned cap.

A review takes about **20–40 minutes** and continues running if the page is closed.

### Exploring the universe

A plain question entered without a command can help identify a scenario or check a universe fact, such as channel activity, persona access, or project history. Confirm the answer against the actual record in **Universe Explorer** before using it in a task.

The course states that the portal cannot write any part of a task: the prompt, Oracle Events, and rubric remain the author's responsibility.

### Proof required for all five reviews

For each review, upload **one screenshot of the whole pass screen, with the verification code visible**, to that review's corresponding step in the task.

| Counts as proof | Does not count |
| --- | --- |
| PASS | A report card or chat message |
| NON-FAIL with a complete run | A cropped verdict that cuts off the verification code |
| Whole pass screen uploaded to the matching task step | A Slack thread, portal-chat link in Slack, or a form |

A FAIL still blocks progress. Correct the input, send the new version in the portal chat, and run the review again.

For example, a complete NON-FAIL result from `/hardness` needs the whole pass screenshot uploaded to the task's `/hardness` step. A screenshot of the Opus pre-check is not a substitute for the review's pass screen.

## 8. Prompt writing changes

### Write an ordinary request

The prompt should read like something the assigned person would send a colleague. Keep the real difficulty in the work and the universe.

| Pattern flagged by the course | V3 guidance |
| --- | --- |
| Specification, audit, or compliance wording such as “Find the governing control…” | Ask the way the person would ask a colleague |
| Riddles and trap hints such as “The thing that actually bites us is not on anybody's list” | Leave a hidden cause unhinted |
| “Go by what they actually sent me and not how I'm putting it here” | Avoid pointing at the trap |
| Answer-key clauses such as “If two places have different amounts, put both” | State the work; let the rubric accept every fair reading |
| An unnamed destination the sender would know | Name the destination |
| Staged typos, invented emoji codes, or broken spacing | Write normally |

An acceptable example from the assessment is: **“Can you post the summary in #eng-releases when you're done?”** It is a plain request that names the destination.

A hidden cause can create valid difficulty only when the prompt does not hint at it. A constraint-heavy riddle is no longer treated as acceptable merely because it is difficult.

### V2 spelling advice is reversed

| Dropped V2 advice | V3 rule |
| --- | --- |
| Leave a typo in | Clean, correctly spelled writing passes; planted mistakes fail |
| Treat perfect capitals and punctuation as a red flag | Normal capitals and full punctuation are acceptable |
| Treat lowercase starts and missing apostrophes as assets | Do not introduce these to make the prompt appear human |

The course still states that task authors write every word themselves, without LLM drafting or polishing. It also retains its restrictions on numbered steps, Markdown, and formal phrases such as “please ensure” in task prompts. Vagueness is appropriate only where a real person would be vague.

These are course requirements for task prompts, not a prohibition on using Markdown to record these reference notes.

### Vary the work across a batch

A phrase can be natural once and become a giveaway when repeated across many tasks. The course flags repeated “Actually,” “Go by the rules in the doc,” “don't trust the summary,” and shutdown framing.

Vary the work itself: analysis, scheduling, partner communications, code review, and a finance close can all support tasks.

## 9. Rubric fairness and evidence

### Grade only what the prompt requested

Every rubric row must trace to a phrase in the prompt and test one fact.

- Do not turn “keep it short” into an unrequested five-line format.
- Do not require a footnote, wording, format, line count, exact time, or time zone that the prompt did not require.
- Do not add extra metrics beyond those requested.
- A careful run that did the requested work correctly must be able to pass every row.

### Avoid repeated grading of one fact

The course's guidance is **one fact per row**. It explicitly makes **the same fact appearing in three or more rows a failure**.

For example, if one revenue figure appears in the spreadsheet, ticket, and reply, writing a criterion for each location plus two rounding criteria makes five rows depend on one fact. A single miss then fails all five. Repetition does not create valid task difficulty.

### Accept every fair reading

The old unique-ground-truth rule rejected a second concrete outcome. V3 allows multiple fair outcomes when the rubric accepts all of them. A rubric fails when it selects only one of multiple fair readings.

- Accept precise and rounded figures when both are fair readings of the records.
- Accept an anonymized token when that is what the source record shows.
- Do not add answer-key clauses to the prompt merely to eliminate fair alternatives.

### Match expected values to reachable records

Every expected value must **cite its source record and match it**. A key that says a fix does not exist cannot fail a run for finding the actual fix commits.

The deciding record must be reachable by following the prompt:

- Multi-hop evidence is allowed.
- A record that nothing points to is an unfair needle.
- Deciding evidence in Trash, an unreferenced page comment, or an attachment is not acceptable under the course's rule.
- If a deciding comment is unreferenced, seed a link to it in a record the prompt gives the agent a reason to open.

Reducing a row's weight does not solve unreachable evidence. A generic prompt hint that “there's a comment somewhere” does not establish a useful evidence path.

## 10. Dates: Pacific for people, UTC beside it

Tools return UTC. People in the workspace use Pacific time.

- Human-readable dates are written in **Pacific time**.
- When the Pacific and UTC calendar days differ, write both, for example **Nov 16 PT (Nov 17 UTC)**.
- The rubric accepts **either date** unless the prompt explicitly asks for one time zone.
- Do not require an exact time when the prompt only requires a date.
- Grading against UTC alone was the old rule.

**Correction from the course question:** A ticket closed at **03:00 UTC on November 17** closed at **7:00 PM Pacific on November 16**. If the prompt does not name a time zone, the rubric must accept **November 16 or November 17**. Accepting only November 16 is incorrect, even though Pacific is the primary display convention.

Remember that the assigned freeze time of 00:00 UTC is still the previous afternoon in Pacific time; see the universe-date table above.

## 11. Before-submission checklist

### Prompt

- [ ] The request is plausible for the assigned role.
- [ ] It reads like an ordinary request; clean spelling is acceptable.
- [ ] It contains no trap hint, riddle, answer-key clause, or specification language.
- [ ] The destination is named when the sender would know it.

### Rubric

- [ ] Every row traces to requested work and tests one fact.
- [ ] No fact is graded in three or more rows.
- [ ] Every fair reading passes.
- [ ] Expected values cite and match the records the prompt leads to.
- [ ] Deciding evidence is reachable.
- [ ] Human-facing dates use Pacific, with UTC beside them when the day differs; either is accepted unless the prompt specifies one.
- [ ] Unfair rows have been fixed and the rollouts re-graded before judging difficulty.

### Task and reviews

- [ ] Role, universe date, and difficulty mode match the assignment.
- [ ] The pre-check and all six baseline rollouts use Opus 5.5.
- [ ] The corrected average is strictly below the assigned cap.
- [ ] The unchanged pass@k, failure-pattern, and errored-run checks are satisfied.
- [ ] The assigned horizon minimum is met, using the golden run or the six-rollout average as applicable.
- [ ] The human effort estimate fits the horizon tier.
- [ ] Each of the five reviews has its whole pass screenshot uploaded to the matching task step, with verification code visible.

## 12. Explicitly unchanged

The course's overview explicitly lists these as unchanged:

- Oracle Events.
- Human authorship of task content.
- No hinting.
- The golden run.
- Rubric weights of **1, 3, or 5**.

## 13. Why the rules changed: course review findings

These figures describe the course's review of 50 completed tasks; they are context, not additional scoring thresholds.

| Finding | Reported result |
| --- | --- |
| Tasks with at least one author-controlled prompt or rubric problem | 36 of 50, across 26 of 33 authors; internal tasks and course seed tasks were included |
| Clearly contrived prompts | Seven; the prompt check passed all seven |
| Prompts with no giveaway line on a blind read | Only five or six of the 50 |
| Tasks with an overly strict rubric | 29 of 50; the rubric check failed none of them |
| Low-pass rubric rows reviewed | Rows passed by two or fewer of the six rollouts |
| Fair misses among those low-pass rows | About 70% |
| Author faults among those low-pass rows | About 24% |
| Repeated “Actually” framing | 34 of 50 prompts |
| “Go by the rules in the doc” framing | About 28 prompts |
| “Don't trust the summary” framing | About 18 prompts |
| Shutdown backdrop | 36 prompts |
| Example of duplicate grading | One figure filled 12 criteria, about a third of the rubric; duplicate grading appeared in 20 or more tasks |

The practical lesson is to preserve difficult work while correcting unfair prompts, grading, and evidence access. Passing an automated prompt or rubric review does not replace checking these rules.

## 14. Source map

Screenshot numbers below refer to the original 20-image course upload, not the later four assessment screenshots.

| Course slide/topic | Original screenshot(s) |
| --- | --- |
| 02: Seven changes at a glance | 1 |
| 03: Assignment fields | 2 |
| 04: Universe dates | 3 |
| 05: Horizon | 4 |
| 06: Baseline model and mode caps | 5–6 |
| 07: Fair rows first and Medium 83% example | 6–7 |
| 08: Eval Portal and pre-check follow-up | 8, 10 |
| 09: Review proof and universe exploration | 9–10 |
| 10: Review findings | 11 |
| 11: Contrived prompt patterns | 12 |
| 12: More contrived patterns | 13 |
| 13: Spelling advice reversed | 14 |
| 14: Rows that failed careful runs | 15, rotated screenshot |
| 15: Expected values and reachable evidence | 16 |
| 16: Pacific/UTC dates and date question | 17–18 |
| 17: Old rule, new rule | 19–20 |
| 18: V3 checklist | 20 |

The later assessment screenshots, captured at 4:33:59 AM, 4:34:22 AM, 4:34:34 AM, and 4:34:46 AM on October 21, 2026, are recorded in the companion answer key.
