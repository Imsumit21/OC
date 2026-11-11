# Deep hardness analysis: how this task reaches a /hardness 5

**`00_Rev5_Design_Brief.md` is now the single design of record, and its Resolutions section overrides this file.** Within this file, later sections override earlier ones. It carries the latest findings.

Analysis only. No prompt, Oracle Event or criterion text. This file supersedes section 7 of `00_Pre_Scenario_Analysis.md` where they differ, and `/create-scenario` should start from it.

Evidence: `00_Opus_Behaviour.md` (30 runs, how Opus works), `00_Score5_Study.md` (10 unique hardness reports), `00_Carrier_Calibration.md` (miss rates), `00_Base_Feasibility.md`, `00_Design_Review.md`, and three blind planning runs by fresh Opus 5.5 agents with no knowledge of the traps. Blind plans show intent, not execution.

## 1. Conclusions

1. **No evaluator has ever given a 5.** Stored scores: 2, 2, 2, 3, 3, 3, 3, 3, 4, 4. A 5 here would be a first, so it stays a target, not a forecast. Scores 3–5 clear the gate equally.
2. **Evaluators refuse a 5 by listing what survived.** "24 of 34 rows are exactly right", "substantial core work remains correct and usable". So the lever is not more traps. It is **fewer independent things that can survive**.
3. **All 10 stored tasks were multi-part registers.** The shape most likely to reach a 5 has never been tried: one conclusion that feeds everything, acted on at once.
4. **Reliability comes from a wall plus splitters.** Douglas kept its headline wrong in 6 of 6 runs behind a carrier no run read, while two other carriers made runs differ. That is how a central failure and the six-run gates can coexist.
5. **Opus's path is close to fixed, so placement can be planned.** It reads the ask by call 3, goes to what the rule names, reaches named sources within about 25 calls, and reaches unnamed services late or never.

## 2. How Opus works, and what follows

| Observed behaviour | Evidence | Design consequence |
|---|---|---|
| Reads the ask, then the rule, then what the rule names | Near-fixed across 30 runs; all 3 blind plans | Anything the path names gets read. Hide nothing there |
| Pages named channels, reads only that channel's named thread | All 3 blind plans page #zombie-design back to the note; 5/6 paged a named channel | **K5 as a channel post would be read.** It must be a thread reply under a parent the ask doesn't name |
| Drops thread markers in its own parsing | `reply_count` printed 19/22, `latest_reply` 0/22; dropping it matched the Julia reply misses (n=6) | Replies under unnamed parents in the ask's own channel are a fair splitter |
| Skips GitHub unless a build is disputed | 3/3 blind plans; inline comments missed 21/30 | **K3 can be the wall**, if the path gives a fair reason to go there but not to the inline read |
| Fixes its PR endpoint early | Audit "no such review exists" after 477 review reads, 0 inline reads | The rule should say review notes, which implies the text, and inline stays a separate read |
| Spends 1–2 Gmail searches, touches 10–33 % of listed mail, never follows `nextPageToken` (0/58) | Forensics; 3/3 blind plans | K1 works among routine mail, but must be reachable without page 2 |
| Searches keywords for coaching and corrections | All 3 blind plans list "walked through", "helped", "coached", "explained", "hint", "doesn't count", "exclude", "duplicate" | **K1's wording must avoid all of these** while keeping the rule's meaning (learnings §54) |
| Says it will search each tester's name in Slack, Gmail, Contacts | 3/3 blind plans, though real runs key on entities and rarely do this | **No deciding record names a tester.** Join by host, date or group. Put no job on tester contacts |
| Checks "works in games" unprompted | 1 of 3 blind plans | K4 is weaker than assumed unless the form is clean and the fact is off-path |
| Stops at a clean tie-out or full count | Forensics Q5 | **The wrong answer must tie out**: log, tickets and form mails reconcile 60 for 60 |
| Parks doubts as "unresolved", and offers a with-and-without view | 3/3 blind plans | A cushion. A hedge isn't a wrong answer. The ask must need one call and a state on every ticket |
| Reads all, writes all, 0–2 reads after the first write | First write at 73–98 % of events; reply last 30/30 | A hidden fact moves every output together, and nothing gets corrected late |
| Softens a judgement it has read | B r1, B r5 | Use binary outcomes with a stated test |
| Effort doesn't track score | 895 calls scored 100, 1,266 scored 77 | Volume stays horizon only |

**Never rely on these:** subagent autocompact failures, `jq` missing, the move 404, or overflow notice wording. They are harness effects, and explicit-model agents completed 68/68. The parent's choices after a failure are fair to grade, but a design that scores only because agents die will not last.

**Correction to the calibration file:** of the roughly 6 surfaced-but-unapplied misses, only 2 were truly read and softened. So "Opus reads it and ignores it" barely exists. Fair difficulty here is almost entirely about what gets surfaced, plus making the join hard after it is.

## 3. The goal: what the request must do

These are principles for `/create-scenario` and the prompt brief, not prompt text.

1. **One conclusion.** The request is for a single audience call. Every other output derives from it, or from the same session verdicts.
2. **Don't invite an audit.** The blind plans were told to work out which sessions count, and they hunted for exclusions. The request should name the note and the workbook, and ask for the read and close-out. The rules enter through the note, incorporated by name. Note that this is the most sensitive lever: if the word "valid" appears, the agent audits.
3. **Require commitment.** One call, and a state on every ticket, because Leonard needs to act. That removes the "unresolved" and with-and-without cushions. A seeded record carries this, not a prompt rule.
4. **Acted on at once.** The reply goes to Leonard, and the close-out writes land. The eval says "A simple repair after the fact does not erase a consequential error".
5. **No extra deliverables.** Register, memo, reply, ticket states. No side tabs, splits or independent sections, since each one is a cushion.

## 4. The scenario: rev 4 structure

**Fewer survivors:**

| Part | Rev 3 | Rev 4 | Why |
|---|---|---|---|
| Panel | Independent figure | Each player carries an audience label, so the panel feeds the same audience rule | It no longer survives a wrong conclusion |
| Retention | Two rows | One context row | Independent, correct-work weight only |
| K2 tutorial split | Side channel | Dropped | Moves nothing central |
| S memo access | Side channel | Dropped | Moves nothing central |
| C duplicates | Row | Kept as data hygiene only | Mandatory read, not a trap |
| Ordinary session samples | 3 rows | 2 rows | Restraint |

**Blocks, re-placed:**

| Ch | Role | Rev 4 placement | Join after surfacing |
|---|---|---|---|
| K3 | Strongest block, not a true wall | See section 10 | Group by device, including model names |
| K1 | Splitter | Plain-language mail among routine form mails, first page of a sensible search, using none of the keywords in section 2 | One host, one date |
| K5 | Splitter | **Thread reply** under an unnamed parent in `#zombie-design`, naming the build by id | Sessions by build id on the form |
| K4 | Splitter | Turkish line in the Julia–Brian DM, referring to the group, no tester names, no job on contacts | "Work friends" on the form |
| F | Side | Robert's reply, reached through the ask's delegation | Writes on not-counted tickets |

**Each route is independent.** No block unlocks another, which answers the gateway warning: several routes lead to the same wrong conclusion, not one door.

**The wrong answer must tie out:** 60 forms, 60 tickets, 60 log rows, 60 form records, and the casual lead looks clean.

**The right answer must also be clear:** 17 counted sessions, RPG leads 3.83 to 3.38, and all 15 miss combinations flip past the tie band (`00_PreScenario_Audience_Table.txt`). Adding labelled panel players changes this, so the table must be re-proved.

**Risk the wall creates:** if K3 fails 6 of 6, those rows are all-fail. That is legal when valid, as Douglas's 17 were, but the headline rows need pre-registered reasons, and the fairness of the K3 path must be airtight. A 6/6 wall lowers the mean and adds no spread, so K1, K4 and K5 must split runs.

## 5. Forecast (UNCALIBRATED)

Rev 4 surface: 20 slots, weight 74, 10 weight-5 rows. A single block miss now scores 68.9 %, under 70 % on its own. Output: `00_PreScenario_Policy_rev4.txt`.

| Rates (my priors, ρ = 0.6) | E[avg] | P(< 70 %) | E[avg], +40 easy weight | P(all gates) | ≥ 1 block | ≥ 2 blocks |
|---|---|---|---|---|---|---|
| K3 works as a wall (.65) | 58.5 % | 94 % | 73.1 % | 72 % | 90 % | 61 % |
| K3 doesn't (.30) | 63.6 % | 79 % | 76.4 % | 81 % | 82 % | 47 % |
| Strong Opus | 74.3 % | 29 % | 83.3 % | 79 % | 65 % | 25 % |

- **The 62 % design target is met only with the wall in place, and only if the rubric stays small.** Those 40 extra weight points cost about 14 points of average.
- The probe's 20 rows is a target, not a guarantee. `/rubric` coverage rules may force more rows.
- **Chance of a 5:** I can't defend a figure, since there's no precedent. The reviewer estimated 25–30 % for rev 3. Rev 4 removes the survivors it named, so my judgement is that it's somewhat higher, perhaps 30–40 %. Treat that as an opinion.
- **Chance of clearing the gate:** driven by at least one block landing, 65–90 % on these priors, and one block now flips the central answer.

## 6. Fairness limits

| Limit | Rule | How rev 4 stays inside it |
|---|---|---|
| Two supported readings | UGT 2.1 | Audience rule with metric, labels, tie and minimum. Every stability, build and audience rule is a dated record |
| Unincorporated rules | `prompt-incorporation-v1` | Note named in the prompt, then a seeded ask delegating by owner |
| Riddle or trap hint | `/prompt` 2.7 | Ordinary request, plain facts in records |
| Unrealistic behaviour | `/prompt` 2.7 | Each block has a business reason. Reversals come from different people, not one person flipping |
| One door | Gateway warning | Four independent routes |
| Unreachable data | `/hardness` defect | Every record has a working path for a careful person, and Gmail isn't page-2-only |
| Row inflation | v2 guide | Few rows, and no dozens of rows on one miss |
| Tool quirks | Fragile lever | Nothing depends on a tool error or a dying agent |
| Over-tuned wording | Learnings §54 | Keep the meaning the rule covers, drop only the keywords |

**Where the risk is highest:** the request that doesn't invite an audit. If it reads as "trust the log", `/hardness` could treat a miss as reasonable. The note must clearly be named as the rule source, so checking it is plainly the job.

## 7. What can still go wrong

- A thorough run reads inline comments, then a 3 or lower is possible. Julia runs missed only 3/12.
- Opening #463 may be natural, since the ticket cites it, so the wall may leak. The move is the second real PR reserve.
- An evaluator may decide a single flipped answer on an interim read is bounded, since the pivot call comes later. The memo's single decision must be something Leonard acts on now.
- Ties, tiny samples and labels could make the audience row look arbitrary on a real read of 17 sessions.
- Everything here rests on 5 hardened tasks and 3 blind plans.

## 8. Tests to run before spending a real run

1. **Blind plan on the real prompt.** Repeat the blind planning exercise with the drafted prompt, and confirm it no longer hunts for exclusions.
2. **Search-collision test.** Run every query from the three blind plans over the seeded text. Any hit on a deciding record is a leak.
3. **Tie-out test.** Confirm the wrong path reconciles 60 for 60.
4. **Flip proof.** The solver re-proves the audience table with panel labels, on final seeds.
5. **Careful-person walk.** A subagent given only the records proves each deciding record can be reached and joined, so no miss can be ruled a defect.
6. **Then** one Opus pre-check, read by block using section 9 of the main analysis.

## 9. Effect on the open decisions

- **Decision 6 (62 %):** now reachable, but only with the wall holding and a small rubric. I'd keep 62 % as the aim and treat about 64 % as acceptable.
- **New decision:** do you accept rev 4's narrower deliverable, with K2 and S dropped and retention reduced to context? It is the main change aimed at a 5.
- **New decision:** do you accept a wall, meaning some headline rows may fail all six runs with valid reasons, as Douglas's did?

## 10. Latest findings: rev 5 changes

Sources: `00_Inline_Comment_Study.md`, `00_Route_Hunt.md`, `00_Playable_Decision_Check.md`. Find odds are reviewer judgement.

**The truth flips, so the wrong answer agrees with the leaders.** Base already leans hardcore: Robert wrote "leaning more hardcore" and Leonard agreed (`1759178344.878219`), so RPG could be reached with no session work. Rev 5 makes **casual** the true lead on counted sessions. The natural read gives RPG, tying out cleanly and matching what the CEO and creative director already believe, so nothing prompts a second look. Coached and industry batches are RPG and high, Samsung and dev-build batches are casual and low, which fits each story. Proof: `00_PreScenario_Audience_Table.txt`. Base Sep 29 discussion says "we decided", so the seeded ask must reopen it. Julia opposed the change, so the true answer agrees with her, and the rubric must not reward that by accident.

**The decision Leonard acts on now.** The playable cannot carry it: Frederick paused it on Sep 29 and the vendor confirmed a Nov 3 restart. The best fit is **keep or hold the Sep 29 "cards earlier" change** (level 17 to 5) for the next submission. It is unshipped, Leonard framed it by audience himself, and it leaves iterate-or-pivot alone. A seeded Leonard ask, dated Sep 30 20:13Z to Oct 1 00:00Z, asks for a binary call. It must not say the change shipped, merge it with the PR #466 tutorial change, or invent a release date. A wrong call has Brian continue a change the true audience doesn't want, carried by a message to Brian that the ask authorizes. Stakes are moderate: one build cycle, no money, and retractable.

**K3 is not a true wall.** It is one direct call away. Revised build:
- The Done ticket names #463 only as the build the pass ran on, with no words about review, notes, comments or devices. My earlier "review notes" wording would leak.
- The review implication sits in the rule record, without a quoted marker. That wording is the best-supported cause of the 18/18 against 3/12 gap, though rule wording and PR count can't be separated.
- #463's only human review is Owen Baker's empty approval. Citing anyone else makes reviews look empty and pushes runs to the inline read. So cite Owen, once his role is checked, since he is an engineer rather than QA.
- Date the comment Sep 27–29 so its mirror falls past page 1. That needs one out-of-order ticket close, or an existing Done ticket.
- **Coherence risk:** 0 of 23 human inline comments in match3d are post-merge. Run this past `/injection` and `/prompt` early.

**Other placements:**
| Record | Change |
|---|---|
| K1 | Julia has no base mail after Sep 17, so a bare listing shows only seeded mail, and volume can't hide it. Only vocabulary works: no playtest, beta, session or form in the subject or body, and refer to the gathering by host and day |
| K5 | Give sessions two or three ordinary build ids, so a search on one reveals nothing. Author Robert or Leonard, deep in their feeds. Candidate parent `1758757016.553559`, once its replies are read |
| K4 | Late Sep 23, the DM's only fitting window apart from Sep 29, accepting page 1 of Brian's feed. Hook `1758570425.654109` is in #zombie-design, not the DM |
| F | Keep reachable through a topic search. It is the easiest to find |
| All | Disjoint vocabulary, one record per day: K4 Sep 23, K5 Sep 25, F Sep 26, never Sep 27–28 |

**Find odds after fixes (judgement):** F .70, K4 .45, K1 .40, K5 .40, K3 .35–.40. As miss rates that is about .30, .55, .60, .60, .60–.65, close to or above the rev 4 priors, and K4 and K1 are better than assumed. Section 5's forecast stands as a rough guide, with the "K3 works" row the nearer one, but no block is safe alone.

**Unfair lines not to cross:** don't remove build ids from forms, strip K1's host and day, drop F's delegation chain, or make K3 depend on the mirror. One live check is still needed on attachment search and non-member channel reads.

**New decision:** do you accept reversing the truth, with casual as the true lead, so the wrong answer agrees with Leonard and Robert? I recommend yes. It is the strongest single change for hardness, and it needs the seeded ask to reopen a call Robert described as decided.

## 11. K3 carrier fixed: real open PR #476

Source: `00_K3_Carrier_Check.md`. Verdict: use with changes. This replaces #463, so the post-merge problem is gone: every one of Arthur's 12 inline comments is pre-merge, and this one is too. In section 10, citing Owen, the Sep 27–29 date and the out-of-order close are all void.

| Item | Decision |
|---|---|
| PR | `match3d#476` "Vision bot", open at the clock. The KB's "opened and merged" line comes from the Normal universe (merged Oct 2) |
| Author | Arthur Blake, on his own PR. 4 of his 12 inline comments are own-PR notes, and 11 of 12 have a review row |
| What it establishes | The bot runs in Unity editor play mode, with no phone. Base supports that (`#if UNITY_EDITOR`, Arthur's DMs). "No Samsung hardware" follows from it. Don't say it can't run on a device, and don't call runs nightly |
| What the ticket may cite | Run #15, Success, Sep 25 12:31Z, on `Blake/visionBot`. Not a build, main or a full regression, since #13 on main failed and nothing ran after |
| Order | ZOM-567 after Sep 30 16:26:02Z, closed before the comment. If it names #476, it must come after 18:54:32Z |
| Placement chosen | `rc_27` plus review `rev_3`, on `VisionBatchCLI.cs`, **20:00–22:30Z, with its mirror** under `#zombie-prs` root `1759258475.735779`, reply_count to 30. Lint for the review exception is still untested |
| Rejected | The 22:40–23:50Z no-mirror slot. It hides slightly better but could read as an integration gap, and coherence was the risk to remove |
| Companion | Base own-PR notes all drew a CodeRabbit reply (4 of 4), so plan one here |
| Rule record | Must name the tool owner, so the path to Arthur's note is fair |

**How hard it is to find:** the PR itself is easy, since "QA" and "regression" match only #476 in match3d (body and title scan, not the live search). The hard step is that the comments result is about 266K characters and spills to a file, with 26 bot comments around one human note. The note likely sits first, on one precedent, and the sort key is unknown.

**Second route, to accept:** the Julia-visible runbook's manual real-device gate gives a careful reader a reason to doubt a bot-only pass. That helps fairness, and it raises K3's find odds, so the forecast should be re-run at scenario.

**Residual risks:** the review-exception lint, the spill behaviour resting on one observation, and six undated `reviewed` timeline rows on #476 that point to SHAs missing from commits. Nothing here should be graded on those rows.

## 12. Final minor hardening (rev 5.1)

| Fix | Change | Why it makes the task harder |
|---|---|---|
| K5 parent | Reply under Julia's friend-reactions root `1758581651.167799` (rc 15). The "New Item Thread" `1758757016.553559` is rejected: it is Robert's art item list, so a session reply would not fit | On-topic, so coherent, yet the ask doesn't name it, and the marker gets dropped in parsing. The root is from Sep 22–23, and the reply stays on Sep 25 |
| K3 runbook route | The ticket owner's dated line says the device gate is covered by run #15. That is a human claim, and Arthur's later note overturns it | Takes away the runbook's free doubt: the ticket answers it with a confident wrong claim. A careful reader can still reach Arthur's note, so it stays fair |
| Wrong-call consequence | The seeded ask has Julia tell Brian keep or hold. The instruction is a required write | A wrong call now sends a wrong instruction that must be withdrawn, adding reversal to the central answer |
| Thread freed | Memo-access thread `1759207989.371869` is unused, since S was dropped | One less shared route |
| Rubric budget | About 20–25 rows, recorded for the rubric plan | Protects the average from easy rows |

**Rev 5 forecast** (UNCALIBRATED; `00_PreScenario_Policy_rev5.txt`; rates are the route hunt's find odds, which are judgement):

| Rates (ρ = 0.6) | E[avg] | P(< 70 %) | E[avg], +40 easy weight | One run ≥ 1 block | ≥ 2 blocks |
|---|---|---|---|---|---|
| Find odds as judged | 52.4 % | 99 % | 69.1 % | 95 % | 76 % |
| Discounted × 0.7 | 62.3 % | 84 % | 75.5 % | 85 % | 53 % |
| Strong Opus × 0.4 | 74.4 % | 29 % | 83.4 % | 65 % | 26 % |

The discounted row is the planning case, and it meets the 62 % target only narrowly. The K3 runbook fix above is not separately modelled. The +40 column shows the rubric budget still matters most.
