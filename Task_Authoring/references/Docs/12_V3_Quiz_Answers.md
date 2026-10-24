# Original Conference — V3 Questions and Verified Answers

**Recorded:** October 21, 2026  
**Reference:** [V3 changes and rules](11_V3_Changes.md)

Answers are derived from the supplied V3 course material. The eight assessment answers were cross-checked against that material; this is not a record of submission or platform grading.

## 1. Assessment answer sequence

Read each of the four assessment screenshots from top to bottom.

| Screenshot | Top question | Bottom question |
| --- | --- | --- |
| 1 — 4:33:59 AM | **C** | **A** |
| 2 — 4:34:22 AM | **B** | **D** |
| 3 — 4:34:34 AM | **D** | **A** |
| 4 — 4:34:46 AM | **B** | **C** |

Full sequence: **C, A, B, D, D, A, B, C**.

## 2. Full correct options and reasons

### Question 1 — Role plausibility

**Question:** Your assignment is Priya Raman, role QA Lead, competency Finance. Which prompt fails on the role?

**Correct option C:**

> Finalise the term sheet for our next funding round and send it to the board for signature.

**Reason:** Finalising a funding-round term sheet for the board is implausible QA Lead work. A QA Lead can plausibly request Finance work about QA invoices or a test-hours budget. Role and competency do not have to match.

**Course basis:** Slide 03, assignment fields.

### Question 2 — Outright task failure

**Question:** Which of these fails the task outright?

**Correct option A:**

> The task is built on February 14, 2026, but your assignment says October 1, 2025.

**Reason:** A universe-date mismatch independently fails the task. Business function, competency, and task skill mismatches alone do not. A Medium average of 82% is below the 85% cap.

**Course basis:** Slides 03–04 and 06.

### Question 3 — Hard difficulty cap

**Question:** Your task is Hard. The six rollouts average 72%, every row is fair, and there are three distinct failure patterns. Does it pass the difficulty check?

**Correct option B:**

> No. A Hard task has to average under 70%.

**Reason:** Hard requires a six-rollout average strictly below 70%. Three failure patterns do not override the cap. The old universal 75% bar no longer applies.

**Course basis:** Slide 06.

### Question 4 — Proof of a complete NON-FAIL review

**Question:** /hardness comes back NON-FAIL with a complete run. What counts as proof?

**Correct option D:**

> The whole pass screen, uploaded to the /hardness step in your task.

**Reason:** NON-FAIL counts when the run is complete. The screenshot must show the whole pass screen with its verification code visible and must be uploaded to the corresponding task step. A pre-check screenshot, Slack link, or crop without the code does not qualify.

**Course basis:** Slide 09.

### Question 5 — Acceptable prompt wording

**Question:** Which of these lines is fine in a prompt now?

**Correct option D:**

> “Can you post the summary in #eng-releases when you're done?”

**Reason:** This is an ordinary request that names the output destination. The other choices use a trap hint, an answer-key clause, or specification language flagged by the course.

**Course basis:** Slides 11–12.

### Question 6 — Clean writing

**Question:** You wrote your prompt yourself. It has normal capitals, full punctuation and no typos. A teammate says to add a couple of typos so it reads as human. What's right?

**Correct option A:**

> Leave it clean. Clean, correctly spelled writing passes, and staged typos fail.

**Reason:** V3 reverses the old advice to leave a typo or treat perfect capitals and punctuation as suspicious.

**Course basis:** Slide 13.

### Question 7 — Repeated grading of one fact

**Question:** The same revenue figure ends up in the spreadsheet, the ticket and the reply. You write a row for each, plus two more that check its rounding. What's the problem?

**Correct option B:**

> One fact now fills five rows, so a single miss fails all five. Three or more rows on one fact is a fail.

**Reason:** The same underlying revenue figure is graded five times. The course explicitly makes grading one fact in three or more rows a failure. The issue includes the repeated location checks, not just the rounding checks.

**Course basis:** Slide 14.

### Question 8 — Unreachable deciding evidence

**Question:** Every run fails one row. You find that the deciding record is a comment on a Confluence page, and nothing in the prompt or the data points to it. What's the fix?

**Correct option C:**

> Seed a link to it in a record the prompt gives the agent a reason to open.

**Reason:** Multi-hop evidence is allowed when a reachable evidence path exists. An unreferenced comment is an unfair needle. Linking to it from a relevant record makes it discoverable. A generic hint in the prompt or a lower rubric weight does not fix the evidence path.

**Course basis:** Slide 15.

## 3. Worked questions included in the course material

These three examples appeared in the original 20 course screenshots and are separate from the eight assessment questions above.

### Course example A — Medium 83% with an incorrect expected value

**Question:** Your task is Medium. The six rollouts average 83%. Then you notice that one row's expected value doesn't match the record it came from, and every run failed that row. What do you do?

**Correct option D:**

> Fix the row so it matches the record, re-grade, and compare the new average with the 85% cap.

**Reason:** Correctness and fairness come before judging difficulty. If the corrected average reaches or exceeds 85%, make the universe harder. Do not ignore the bad value, discard an otherwise valid check, or add stricter rows to lower scores.

**Source:** Original course screenshot 7; the displayed feedback marks D correct.

### Course example B — What follows the Opus pre-check

**Question:** Your Opus 5.5 pre-check run is done, and the task looks hard enough. What's next in the Eval Portal?

**Correct option A:**

> /hardness, with that run's trajectory JSON attached.

**Reason:** `/hardness` immediately follows the pre-check. Its pass screen goes to the task's `/hardness` step. Passing permits continuation; final difficulty is measured across the six baseline rollouts.

**Source:** Original course screenshot 10; the displayed feedback marks A correct.

### Course example C — Pacific and UTC dates differ

**Question:** A ticket was closed at 03:00 UTC on November 17. The prompt asks when it was closed and doesn't name a time zone. What should the rubric row accept?

**Correct option B:**

> Either November 16 or November 17.

**Reason:** 03:00 UTC on November 17 is 7:00 PM Pacific on November 16. Write the reference as **Nov 16 PT (Nov 17 UTC)** and accept either day unless the prompt specifies one time zone. The prompt did not require an exact time.

**Correction to preserve:** The course screenshot shows option C, “Only November 16, because the people in the workspace are on Pacific time,” selected and marked incorrect. Pacific is the primary display convention, but that does **not** justify rejecting the UTC day when the prompt leaves the time zone unspecified.

**Source:** Original course screenshots 17–18.

## 4. Rules to remember when answering similar questions

- **Role and competency differ:** QA-related Finance work can fit a QA Lead; corporate fundraising generally does not.
- **Wrong universe date fails:** Do not substitute the other freeze date.
- **Caps are strict:** Easy <90%, Medium <85%, Hard <70%; equality fails.
- **Fairness comes first:** Correct rows and re-grade before judging the average.
- **Review proof is specific:** Whole pass screen, visible verification code, matching task step; complete NON-FAIL qualifies.
- **Clean spelling passes:** Do not plant typos.
- **Every fair reading passes:** Multiple reasonable outcomes are allowed.
- **One fact must not fill three or more rubric rows.**
- **Evidence must be reachable:** Multi-hop is allowed; an unreferenced needle is not.
- **Pacific display does not mean Pacific-only grading:** Accept either Pacific or UTC day when they differ unless the prompt specifies one.
