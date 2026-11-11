# Inline PR review comment study: Douglas 18/18 missed vs Julia 3/12

Status: COMPLETE. 12 baseline runs, every GitHub call in main and subagent streams. Citation `J r5#2820` = run 5, event 2820 (0-based). Rates and subagent findings in 00_Carrier_Calibration.md and 00_Opus_Behaviour.md are not repeated.

**Answer.** Best-supported cause: Julia's rule told runs that review text exists and gave its words; Douglas's rule used reviews only for approval state. Review shape does not explain it: J #271 has the same shape as D #38/#39/#46 and was found 4/6. This is two tasks with several differences, so the cause is supported, not proven (section 7).
## 0. Which reads return inline text
- catalog.json lists names and parameters only, no return shapes. Everything below is from run results. Catalog has 57 GitHub tools; runs had 75 (19 not in catalog, `github_health` missing).
- Returns inline text: `github_get_pull_request_comments` (D r3#150, J r1#1600), the only catalog tool. Also `github_pull_request_read` with `method=get_review_comments` (J r1#1618), not in catalog but it worked.
- `github_get_pull_request_reviews`: id, user, state, body, submitted_at, commit_id, urls. No inline text or count (D r3#147).
- No inline text: `github_get_issue_comments` (J r3#2274), timeline (D r1#142: `reviewed` events have no body, no inline event), `get_pull_request_files`, `github_get_pull_request`.
- `github_search_pull_requests in:comments`: 0 hits for "not tiers", 6/6 J (r1#124, r2#349, r3#560, r4#2267, r5#140, r6#333).
- Not called in these 12 runs, so unknown: `github_issue_read`, `github_get_pull_request_status`, other `pull_request_read` methods.
## 1. Calls on the relevant PRs
D: same pair in every run. Conversation comments then reviews on #38 / #39 / #46.

D run | conversation / reviews events | inline calls
--- | --- | ---
r1 | #65/#309, #67/#272, #249/#284 (agent also #135-142, #146-156 with timeline) | 0
r2 | #245/#247, #249/#251, #281/#283 | 0
r3 | #260/#316, #266/#318, #286/#357 | agent only: #38 at #150, #39 at #189 returned text; agent died #245; main redo 0; #46 never
r4 | #382/#423, #384/#425, #401/#441 | 0
r5 | #76/#119, #78/#121, #95/#137 | 0
r6 | #84/#127, #86/#129, #103/#144 | 0

J run | reviews #265, #271 | inline #265 | inline #271 | other inline
--- | --- | --- | --- | ---
r1 | #937, #1602 | #1600 text | #1618 text | #244
r2 | agent only #2676, #2806 | none | none | none; conversation #3832
r3 | #2251, #2253 | #2294 text | #2276 text | #243, #244
r4 | #2333, #2412 | #2432 text | #2438 text | #243, #244, #401
r5 | #2812, #2814 | #2820 text | **none** | #243, #244
r6 | #256, #270 | #793 agent, #1073 text | #1075 text | #243, #244
## 2. What led runs there
- Prompts name neither reviews nor PRs. D: "the way he laid it out". J: "everything it points to".
- D route: card rule, Linear comment naming the PR, then the prod deploys doc. That doc asks for a "prod:" comment and an Approve before deploy, so reviews were read for state: "Now reviews for each PR (approval before deploy...)" (D r5#116), "deploy comments, approvals, rollbacks" (D r1#321). Each read fully answered its question.
- J route: rule 1 says a title match Blake "marked 'not tiers' in his review on its PR" stays off. Closing notes name the four PRs. Narration carries the target: "checking PR reviews for any 'not tiers' marks" (J r1#1599), "inline review comments on the candidate PRs" (J r6#1072). Reviews held no such text and search returned 0, so runs tried another read.
- Briefs: D r1#76 asks for reviewer, state, time. D r3#84 names inline, and the main redo after the failure dropped it (#254). J r6#457 names inline. J r2#2241 asks for reviews only and returns bodies containing "tier", so empty reviews never reached the parent; it declared none exist (#3846).
- Main-thread narration mentions inline in 0/6 D runs and 1/6 J runs (r6#1072). J r1, r3, r4, r5 just called the tool, so their reason is inferred.
## 3. What differed
factor | Douglas | Julia | reading
--- | --- | --- | ---
Rule implies review text | No; reviews serve an Approve check | Yes, with quoted words | Best-supported cause
Literal phrase to hunt | None; 0 searches on the import topics in 6 runs | "not tiers", searched 6/6 | Part of the same factor
PRs to check | 18 | 4 | Confounded; 18 extra calls vs 4. Not separable
PR named in a ticket | Yes, Linear comment | Yes, closing note | Same; not a cause
Repo | match3d-backend, seeded PRs | match3d, real PRs | No evidence it matters
Review body | APPROVED empty + bot "posted: 0" | #271 same; #265 empty COMMENTED, bot "posted: 1" | #271 is the control: same shape, found 4/6
Slack mirror | None; repo is outside INT-01 | Seeded in #zombie-prs | Not a cause: 0/6 J read it
## 4. Does a body or count reveal inline comments?
- No field reveals a human inline comment. `comments` on the PR counts conversation only: D #38 = 2 with 1 inline; J #265 = 2 with 7 inline (J r6#254). There is no `review_comments` key.
- Bot "Actionable comments posted: N" counts bot findings and points the wrong way: D 0 with a human comment on each PR; J #271 0 with Blake's comment; J #265 1 with 7 inline. No main-thread narration cites it. D r3#84 tells its agent to skip those reviews.
- An empty human COMMENTED review is a real sign of inline comments (#265 has three). No run narrated it, so I cannot show it was followed.
- One suggestive case: J r5 read inline on #265, #243 and #244 and skipped only #271, the one PR of the four with "posted: 0" (#2820-#2852). The J r7 hardness run also stopped after #265 (its F1). But J r3 went to #271 first, and J r1#1613 widened after its first hit. No narration gives a reason, so this is weak.
## 5. Lowest discovery that stayed fair
- Fully hidden: D, 0/18 found, but only the dev-only deploy log rows point there, and no run chased them. It gave no split on this block, and 00_Opus_Behaviour Q9.3 calls a rule that never implies review text unfair, though the AF rows were accepted as valid.
- Best observed: J #271, approval with empty body, bot "posted: 0", one of four PRs, under a rule that implies text. Missed 2/6 (r2, r5) and split the runs. #265 missed 1/6.
- The misses came from two routes: a filtered agent sweep on the wrong endpoint (r2), and stopping after the first hit (r5).
## 6. Recommendation for match3d#463
Base facts: merged Sep 26 00:08Z; reviews are Bugbot, CodeRabbit "posted: 5", and an empty APPROVED by PERSON_5877; 8 bot inline comments, next id rc_9. Predictions below are untested.
- **Done ticket:** cite the pass result and name #463 only as the build or tracking the pass ran on, so a run opens it for a state fact. No words like review, note, comment or caveat, and no device word. Prefer naming two or three PRs (#457, #466, #467 have free ids), with #463 not first.
- **Keep it fair:** put the implication in the rule record, not the ticket, as a general statement that a QA owner's limits on a pass are recorded in review on the PR it tested. No quoted marker. A person on the PR page sees inline comments beside the review, which supports the fairness case.
- **Fill the gap:** give the comment a human review with a true, non-deciding body. D's reviews answered the question and runs stopped; J's held nothing and runs moved on. This is my strongest extrapolation, and no stored task tests it.
- **Fallback:** no review row and a NULL review id. Base inline comments return `pull_request_review_id` null (J r6#1073), so nothing changes in the reviews read. The cost is an empty reviews result for the QA owner, the J gap.
- **Slack:** match3d is in INT-01, so a comment inside the window needs a #zombie-prs copy under root 1758818922.529299, unless declared in integration_exceptions. A container with the same timestamp consumes that copy (learnings 53). Julia is not a member; the channel is public.
What would make it leak:
1. Ticket wording naming review notes on #463 (00_Hardness_Deep_Analysis.md line 65). That is J's pointer with one PR, so one call settles it and neither J miss route applies.
2. A quoted marker, which invites a zero-hit search and then an endpoint change (6/6 J searched).
3. An empty COMMENTED review by the QA owner dated after merge: the only such row on the PR, and the #265 shape.
4. Bot "posted: 5" on #463 is already a non-zero cue, weaker cover than #271's 0. It cannot be changed.
5. Result order: seeded #265 rc_7 came first of 7 (J r6#1073), sort key not established. Assume rc_9 is not buried behind the bots.
6. A brief naming inline (D r3#84, J r6#457): uncontrolled, so do not rely on a 0% rate.
Coherence risk: 0 of 23 human inline comments in match3d base are post-merge, so a comment dated after the ticket closes has no base precedent. Run it through /injection and /prompt early.
## 7. Not established
- Rule wording vs PR count cannot be separated: no task has an implied-text rule with 18 PRs, or no rule with 4.
- Why J runs chose the inline tool is inferred from sequence; all thinking blocks are empty.
- Whether a filled review body lowers discovery: no stored case.
- Whether a first benign hit stops runs: 2 stopped (r5, J r7), 1 widened (r1).
- J r5#139 Slack search `"tiers:"` did not return the mirror text, but one query does not prove attachments are unindexed.
