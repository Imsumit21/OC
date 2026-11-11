# 00 Design Review (independent, adversarial; rev 2 design)

Status: COMPLETE. Holds no prompt, Oracle Event or criterion text. Rates marked "mine" are judgement, not measurements.
Bottom line: rev 2 is not ready for `/create-scenario`. Four blockers break the score-4 logic or the UGT, and all four can be fixed without adding rows.

## Predicted /hardness band
As written: **3** (range 2-4), confidence about 60 %. With B1-B4 repaired: 4 about 55 %, 3 about 35 %. A real six-run average below 70 % is unlikely either way (section 6).

## Blockers
**B1. Block size matches r4, not r5, and reversal is not designed.**
Evidence: section 3 cites "9-12 of 60" against r5's 29 %, but 8/9/10/12 of 60 is 13-20 %. r4's 6 of 34 (18 %) scored 3 (r4 line 111). The surface rows S-K1b, K2b, K3c and K4b only say tickets "end in the excluded state". So a miss is an omission: nothing is deleted or reverted, which is the r6/r7 reason for a 3. r5 reached 4 because wrong writes had to be undone across four outputs (r5 line 130). Section 10 budgets 24 writes and calls state writes "may add more", while section 3 makes them mandatory.
Repair: every session ticket takes a state write, counted or excluded, so a miss leaves 8-12 wrong positive writes. Those 60 writes go into section 10 (see M7).

**B2. K2 contradicts itself, and its weight is mostly fictional.**
Evidence: sections 6 and 7 say the sessions are regrouped, not excluded. Surface S-K2a says "excluded (12)", S-K2b "end in the excluded state", and S-G1/G2/G3 list K2. Regrouping moves neither the valid count, the overall mean nor the tally, so K2's unit is 8 of 97, not 21. Its ticket state write may vanish too. A miss then touches one register column and one split: "one cause and two outputs", a 3 at best.
Repair: pick one before scenario. Either the pre/post split is itself the headline Leonard asked for, carried by the memo, the reply and a per-ticket group write, or K2 is demoted to a side channel and removed from BLOCKS and G1-G3. It also must not be solvable from a build field on the ticket (see K2 in Check 1).

**B3. K3's beating record does not beat the wrong source.**
Evidence: "Done, not reproduced" claims no fix, and a comment saying a PR left the group untouched is compatible with it, so neither shows instability. The real proof is base: ZOM-559, Vincent `1758564051.199019`, the S24 crash thread. So a run can reach "exclude" with no PR read, and section 7's .50 does not apply. Leonard's note says "clean data from a tech-stable **beta**". Tech-stable there qualifies the beta, not friend sessions, so no rule exists yet. /prompt 2.1: "a Done ticket ... is not the event unless the prompt says it is".
Repair: use the tech-stable rule record section 6 already requires. It states that a device group clears only on a clean pass on that device, and that the ZOM-559 sound bug is not a session blocker (ZOM-559 stays Todo). The ticket then cites a QA pass, and the same person's inline comment on #463 says that pass had no Samsung device. That is a real missing part, with no fix, branch or build claim.

**B4. The Sep 30 date floor turns the "later corrections" upside down.**
Evidence: all session tickets, and the Done ticket (ZOM-567+), date from Sep 30 16:26Z. If the K1 mail is older, /prompt 2.1 check 1 (newer source) favours the ticket. If it is newer it has 7.5 hours and becomes the top line of any inbox listing, so "unpointed" is gone. K4 is worse: Julia authors the log saying "RPG/casual gamers" while being a party to the DM that refutes it. The PR comment must also post-date the Done ticket, or it reads as stale.
Repair: make the log a transcription. Each ticket states the observer's form date and the session date. K1's mail and K4's DM fall after the form date and before the Sep 30 batch, so the fact date, not the ticket date, governs. Date the PR comment after the ticket closes.

## Major
**M1. F and S are obligations, not facts, and lack an incorporation chain.** WORKFLOW `prompt-incorporation-v1`: a discovered Slack message cannot add actions, and /hardness excludes such misses. A Robert reply under an unrelated root ("Can you check if it's item specific?") has no chain. Repair: the seeded ask record delegates by owner, saying Robert has set how excluded sessions are handled and who gets the memo, without saying where. The chain then runs prompt to ask to instruction with no prompt change, and the thread stays hidden.

**M2. K4 is not on a deep page, and its rule is missing.** Measured in `D076RBM29JS`: 37 messages since Sep 22, and the 50th newest is Sep 8, so every post-note message sits on the first page. The 44 % deep-page rate does not apply. The note's "casual and/or RPG gamer friends" does not exclude industry people, and the base hook is one artist friend, in a public channel. Reading B (keep them) is open. Repair: the audience rule record says game-industry people don't count. Write the DM message in Turkish, as 23 of the last 37 messages are. That matches the voice and escapes English keyword search while staying readable. Tie it to tester names.

**M3. One Slack search defeats several thread-reply channels.** In the stored trajectories, 93 Slack search results held 203 thread-reply hits, 10 of them in DMs. So `slack_search_public_and_private` finds replies wherever they sit. Any shared word ("sessions", "friends", "re-run") across K2, F and S falls to one query. One Gmail listing after Sep 22 shows K1 and D together, and D's mandatory read pulls every run into the mailbox. Repair: give each carrier its own vocabulary, and add a free offline collision test to the no-loop plan: run the 15 likeliest queries over the seeded text before spending a run.

**M4. The "calibrated" row is not calibrated.** K2 uses .35 against a measured 22 %, F .30 against 17 %. D uses .40 although a named-vendor mail measured 0/78, and it is the only panel source. K3b has no carrier at all and every ticket is read. C's .50 is really bimodal: no link gives about .9 with no split, a link gives about .1. Repair: relabel the row "author prior", use the measured values, and treat D and K3b as correct-work weight. Design C's link or drop C.

**M5. "Lands a block" is not "scores 4".** BLOCKS includes F, a weight-6 unit with no reversal, and K2. The section 1 claim "a 4 is likely" therefore rests on an event wider than a 4. Section 3 itself shows a one-block miss can score 3. Repair: report P(block with reversal) only, and treat a single-block 4 as uncertain.

**M6. G1-G3 are a compound choke and clash with section 2.** Any of six channels fails all three, so P(G1 passes a run) is .032 calibrated and .163 planning, and P(0 of 6 pass) is .82 and .34. Section 2 promises zero predicted all-fail rows. One block then spreads over five rows, while GEN_EXECUTION line 276 fails a fact in three or more rows. Repair: keep G1 as the one aggregate control, drop G3's channel link or G3 itself, and pre-register the /create-allfail reason for G1 and G2.

**M7. Volume: 60 ticket reads are replaceable.** `linear_list_issues` has a caller-set `maxDescriptionChars` (a stored run passed 300 and got `descriptionTruncated`), so section 10's "list view's truncation" is not a limit. `linear_show_data` is still unknown (Ask_Carriers [U]), and the Sheets log may replace all 60 anyway. That leaves about 240, under the proposed 260 floor. Repair: stop counting reads, count the 60 B1 state writes (about 300 again, and real), test `linear_show_data` first, and fix which field lives on which surface: comment, Doc, ticket.

**M8. The storyline overstates the decision.** The note sequences the call after "clean data from a tech-stable beta", and the beta had not shipped. A pivot recommendation on Oct 1 contradicts Leonard's own order. Repair: the seeded ask frames this as the friend-feedback and retention read feeding the later call, and the recommendation row becomes a stated boundary.

**M9. Assignment fit is defensible, not clear.** See Check 5. Repair: same rows, but the memo's question becomes which audience the beta push should target, with the pivot tally secondary.

**M10. The no-loop ladder has no rungs left.** See Check 7.

**M11. K1's join is undefined.** Section 7 says "the evening" and 10 sessions. If those sessions span days, the mail cannot decide the block. Repair: one hosted gathering on one date, session date on each ticket, no other session by that observer that day, and the mail says plainly what he did.

## Minor
- m1. Resolved: `linear_update_issue` has `state`. Close section 4 and section 13.
- m2. Resolved: Julia (`EMPLOYEE_0005`) is not among the 12 members of `#zombie-prs`, though the channel is public. Whether her search reaches it is still untested, so keep it non-load-bearing.
- m3. #463's 8 inline comments are all bots, dated Sep 25, and it merged Sep 26 00:08Z. rc_9 is its only human comment, and it comes post-merge. Fine under Check C, but give it a reason: it hosts the tracking used on the QA pass.
- m4. The base results mail has no per-player stars, only a report link, so all 10 ratings are seeded. Give the void a stated reason without a refund.
- m5. Robert's bots thread hosts S and undercuts E's retention read. Expect a caveat and accept it in the boundary.
- m6. Section 11 says a comment after close fails. Pick an excluded state that lets a run comment after the state write, or the F order becomes a false failure.
- m7. Script: S-K3b should carry K3 as well, so a K3 miss is 73.2 %, not 78.4 %.

## Check 1: walk-through
| Ch | Surfaces? | Connects? | Stated | Mine | Verdict |
|---|---|---|---|---|---|
| K1 | Likely via `from:` or an inbox list | Yes, if M11 is fixed | .50 | .40 | **Strongest.** Holds if B4 is fixed |
| K2 | Search on "0.3.133"; #builds Sub #133 shows the Android change Sep 26 | Yes, and a build field solves it with no date | .35 | .25 | Fair trap, small effect (B2) |
| K3 | ZOM-559 on any Samsung search | Reaches "exclude" without the PR | .50 | .15 | **Weakest block** (B3) |
| K3b | Every ticket is read | Opus knows Galaxy model names | .35 | .05 | Not a channel |
| K4 | Only if it opens Brian's DM; then page 1 | Needs tester names and a rule | .40 | .25 | Moderate (M2) |
| F | Runs parse DMs and drop reply markers (r4, r5) | Valid only with a chain | .30 | .35 | Good carrier, weak value (M1) |
| C | No path designed | None | .50 | .1 or .9 | Undesigned |
| D | Mandatory read | Same record as the data | .40 | .05 | Not a channel |
| S | Thread is read for bots/retention | Needs a chain | .25 | .20 | Fine, low value |
Several at once: yes. A keyword Slack search hits K2, F and S. A mailbox list hits K1 and D. A Samsung search neutralises K3 and K3b. No single read beats all of them.

## Check 2: fairness
- **K1:** the mail is a fact and the rule is the note's "No coaching", so it is fair if the join is closed (M11) and the date holds (B4). Describing an evening is not a /prompt riddle: 2.7 reads prompt wording, not seeded records.
- **K4:** unfair as designed. No rule excludes industry friends, so /hardness can call a keep a reasonable reading (1A section 3). Depth is not the issue: fix the rule (M2).
- **K3:** unfair as designed. Done next to open ZOM-559 leaves two supported readings with no definition, and a miss may be scored ambiguous. B3 closes it.
- **F, S:** unmentioned-policy risk, earning no credit (M1). **K2:** fair once B2 is settled.

## Check 3: score-4 logic
- If exactly one block lands: K1 or K4 with positive writes gives four outputs wrong, about r5 in breadth and r4 in size, so a coin flip. Without B1 it matches r4 or r6: score 3.
- K2 as grouped does not need reversal, which is the problem. It can reach 4 only if the split is a headline and each ticket carries a group write (B2).
- Writes needed: a positive wrong state on each missed ticket, a wrong headline in the memo and reply, and a wrong register verdict. A per-ticket flip alone risks r4's "bounded and mechanical", so the figures must move too. Two blocks landing makes 4 far safer than any single block widened.

## Check 4: coherence
- 60 tickets in 7.5 hours: passes as a batch, but only with B4's form dates. Very late Turkey hours are no defect (Check C).
- Observer pool: 11 Slack-active plus 3 commit-only. Douglas (4 messages) and Frederick (2) are thin, so check each author's channel membership (3.2).
- 10 sessions by one person: fine as one gathering, odd across a week (M11). Zero Slack chatter on 60 sessions is implausible but not a failure.
- Panel void: passes if a reason is given (m4). Android note: passes if dated by Sep 28 16:11 and silent on "required".
- Julia at the clock: plausible. Day-9 interim read: plausible only with M8. No /injection failure found beyond B4's lifecycle risk.

## Check 5: assignment fit
/prompt 1.5 lists "campaigns/GTM". The work is an iterate-or-pivot product call, with QA-flavoured channels: K2 and K3 hold builds, PRs and device stability, and ticket close-out is Engineering Ops in feel. GTM content is the panel, K-4 audience split, E and the leadership note. It clears "clearly belongs to a different competency", but not by much. Base supports the repair: audience direction is unsettled (`1759173459.621579`).

## Check 6: forecast
The table matches `00_PreScenario_Policy.txt`, and the "coin flip or worse" reading is honest. The inputs are what is wrong. Scratch re-run, same model, rho .6:

| Rates | E[avg] probe | P(<70) | One run lands block with reversal | E[avg], 40 passing weight added |
|---|---|---|---|---|
| Author, B2 fixed | 59.3 % | 94 % | 82 % | 71.2 % |
| Measured carriers (M4), B2 fixed | 66.2 % | 74 % | 82 % | 76.1 % |
| Mine, B2 fixed | 74.8 % | 23 % | 61 % | 82.1 % |
Two further limits. The 27-slot surface is 84.5 % flippable, while stored tasks passed 282 of 393 rows 6/6, so a real rubric dilutes it (last column; the 40 is an illustration). And rho .6 is a choice that lifts P(SD) and P(all). Honest reading: 85 % is likely safe, 70 % is not.

## Check 7: no-loop plan
Sound: pre-registered moves, a two-revision cap, reading by block, no new rows. Missing:
- The ladder is spent. K1 is already unpointed mail, F already a non-cohort root, K3 already inline, and no Doc carrier exists. K2 and K4 have no move. Name one real move per channel.
- No row for a miss /hardness rules a task defect, which is the costliest outcome (fix: chain or rule, not placement).
- No row for score 3 with no block landed, or for a landing only on side channels.
- No post-baseline stop rule: nothing covers a 4 followed by an average of 70-85 %. State whether that ships.
- No same-SQL rerun: a second run costs no /injection or /prompt, so use it before editing on a near miss, but never to pick the best run.
- Pre-register one probe phrase per record. r4 and r5 ran 4-8 subagents, and the calibration warns main-trajectory matching can miss their reads.
- Step 1 sees only seeded records, so it tests logic, not findability. Add M3's collision test.

## Base spot-checks (5)
1. Note `1758517286.431379`: quote confirmed, but tech-stable qualifies the beta (B3, M8).
2. Hook `1758570425.654109`: Brian confirmed, one Cypher Games artist friend, public channel. DM depth and language measured (M2).
3. PR #463: exists, merged Sep 26, 8 bot comments, next is rc_9. Feasibility confirmed (m3).
4. Thread `...1843922088670958384`: real, no star data (m4).
5. `#zombie-prs`: Julia not a member (m2).
Holds: disjoint blocks, retiring fix claims and the card-move cut, the ID floors, E as correct work, keeping traps out of the prompt, and the frank section 13.

## Rev 3 delta
Checked against the rev 3 analysis, surface and policy output, not the repair list. Rates here are judgement. Section 8's "Reviewer's judgement" row is not mine: I never rated K5, and I gave K3 .15 on rev 2. My rev 3 rates are K1 .35, K3 .25, K4 .25, K5 .25.

**(1) Status**
- B1 **partly:** every ticket takes a state write (section 10, K?b rows), so a miss leaves positive wrong writes. No record yet says which Linear state means counted, or authorizes 60 writes.
- B2 **closed:** K2 is one weight-3 row, outside H1, G1, G2.
- B3 **partly:** the comment now truly beats the ticket. But the rule requires a pass on that device, and a ticket citing an unnamed pass lets Opus default to "not cleared" with no PR read. Repair: the ticket cites the full QA matrix, whose base runbook lists "current-gen Samsung / Pixel", so Samsung looks covered until the comment.
- B4 **partly:** forms are in section 6, but section 11 still says "Julia's batch log". K5's form must predate Sep 24. K4's reserve (below) breaks it.
- M1 **closed** in design; prove it at /prompt. M2 **partly:** the rule is seeded and the line is Turkish, but no tie to tester names is stated. M3 **partly:** plan only, and K5 collides (below).
- M4 **closed:** relabelled, D and C moved to correct work. M5 **closed:** the >= 2 column is now the stated route.
- M6 **open:** G3 went but H1 came, so three aggregates still share four channels. P(H1 passes a run) is .06-.27, P(0 of 6) .15-.69. Section 2 still promises zero predicted all-fail, and no reason is pre-registered.
- M7 **partly:** the sums work, but `linear_show_data` and the field map are deferred.
- M8 **closed:** line 68's heading is stale. M9 **closed.** M11 **closed.**
- M10 **partly:** the rows are added, but two moves are wrong (below).

**(2) Newly broken**
- **Arithmetic: compatible, with one condition.** All four blocks must push the same way. My example: casual 9 at 3.7, RPG 8 at 3.5; K1 13, K4 9, K5 10 are RPG at 4.3-4.4; K3 11 is casual at 3.0. All 15 miss combinations flip, smallest margin .185. If one block pushes the other way, two misses can cancel and a wrong run gets the right answer.
- **Fairness: solvable only with a stated rule.** It must fix the metric (session or tester), one audience label per session (the note says "and/or"; K4's form says both), ties and a minimum. A gap of .2 on 9 against 8 sessions is noise, so "too small to call" is a reasonable answer unless the rule closes it. /hardness would then give no credit.
- **Answer source conflict:** line 12 says the answer draws on panel and retention, but H1 is sessions only, and neither has an audience cut. The rule must say sessions decide.
- **Thin base:** 43 of 60 not counted (72 %), and block means sit 0.8 above counted ones, a visible hint. C is outside G1 and H1, so duplicates must not sit in the 17, or the surface is wrong.
- **K4 Turkish line:** no /prompt problem: 2.7 reads prompt wording, the voice matches the DM, and Opus reads it. It must be unambiguous and name the batch. But the K4 move "before the note" cannot post-date the form, which reopens B4.
- **K5:** the store-builds rule points straight at a "dev build" search, and a post in the anchor channel is one hit. Word it by build id only. "Over 100 parents back" is wrong for Sep 25: 73-89 parents follow it; Sep 24 is at most about 105. Its #7 label is really #2, K1's type. Its base support is Brian's, in a DM Julia can't see; keep K5's observer off Brian.
- **Form mails:** not padding, if each is the source of a ticket's form date, which B4 needs. Purely filler mails would be. Two costs: Brian cannot send one, as brian.foster@ is the SC-6 address, so his forms need another carrier. And reading forms puts K1's sender on the path, so K1 falls to about .35. The K1 move into the form thread is backwards: opening that thread shows it (mail reply 33 % against separate 57 %).

**(3) Band for target 4 (judgement):** 4 about 40 %, 5 about 20 %, 3 about 15 %, 2 or below about 25 %, confidence medium-low. Up from rev 2, because a miss now reaches the central answer. At my rates: one run lands >= 1 block 71 %, >= 2 34 %; average 73.7 %, 81.9 % with 40 easy weight. Below 70 % is still unlikely.

**(4) Blockers to /create-scenario:** none block starting. Three must be its first acts, before SQL: the audience rule plus a proven number table; Brian's form carrier; and the state mapping with its authorization. Fix the K1 and K4 moves in the same pass.

**(5) Score 5 target (all judgement)**
- (a) **What 5 needs:** the central result wrong, not just a flipped word. A run needs the wrong audience, plus a counted base mostly invalid. One block makes 35-43 % of the sessions it counts invalid (9/26 to 13/30). Two make 53-59 %. r5's "why not 5" then applies inversely: at two blocks, most of the claimed evidence is wrong.
- A flip alone: usually 4. The memo's headline, count and mean are wrong, but 47-51 of 60 verdicts, retention, panel and delivery stand, and the fix is "exclude, recompute". A fair evaluator could argue 5, since the one question asked is answered wrong; I put that at about 15 %. Retention and panel hold it at 4 mainly in the one-block case. At two or more blocks they are side evidence and hold little.
- (b) **Raises 5 fairly:** make the audience answer the memo's single decision, with panel and retention stated as context only (the rule, not extra work). Give the unassigned Trello role to an existing target-audience field the answer already governs, only if the ask already requires it. Otherwise leave it, as a new write is a step. Do B3's QA-matrix repair and K5's build-id wording, which raise >= 2 blocks, the true route. Keep rubric rows outside blocks few. Do not link blocks through one shared record: that is a choke point, and it splits nothing.
- (c) **Gates:** patterns are safe while blocks stay disjoint (P(pat) 96-100 %). All-fail is the real cost: H1, G1 and G2 pass only with all four blocks, so harder hiding pushes P(0 of 6) past .7. All three need a valid all-fail reason: a findable record, and any single block visibly solved by some run. SD falls if every run lands two or three blocks (scores 56-65 %, SD under the .1 floor), so one clean run helps. Keep at least one block near .25, or spread goes.
- (d) **One run, judgement:** P(score 5) about 20 % as designed, 25-30 % with (b). P(score 3 or above) about 75 %, conditional on the audience rule being fair. If H1 is ruled ambiguous, P(5) falls under 10 %.
