# How completed tasks closed open sets at /prompt and kept their difficulty

Read: the root `learnings` file, `completed_tasks/README.md`, all seven task READMEs (Lessons carried forward first), and the
eval_reports of Julia, Q4 commitments, Bridge and Douglas. I also read Robert's /prompt reports, which you didn't list, because Robert
is the only Planning task and it has a per-row "by when" cell. Task_Authoring/task_inputsS/ was not read. Anything here about your
current task comes only from scratchpad CENSUS_BRIEF.md. SQL quotes use single apostrophes instead of the doubled SQL form.

## Evidence warnings

- **Julia's report numbers are not chronological.** True order by SQL revision: r1 (rev 4), r2 (7), r3 (9), r4 (12), an unstored PASS
  (rev 14), r6 (17), r7 (20), r8 (22), r9 (25), r11 (28), r12 (30), **the file named `1_prompt_PASS_r5.md` (42)**, r13 (45), r14 (48).
  There is no r10 file. The prompt is byte-identical from r2 on, so every fix after r1 was in the SQL.
- **Q4's only /prompt report does not cover its final SQL.** `1_prompt_PASS_r1.md` reviewed SQL `2176eb70…`, which is the stored rev3.
  The submitted SQL is `69603ab4…` (rev4, the de-named version). No stored /prompt report shows the de-named records passing. Don't
  cite Q4 as proof that de-naming is /prompt-safe.
- One-run /hardness outcomes are single observations. Rates below come from baselines or the hardening reports' multi-run counts.
- "60-83 calls before the Bridge write lever" comes from Q4's `00_Completed_Task_Learnings.md`. I did not re-derive it.

## Main findings

1. **Every UGT failure was closed in records, never by changing the prompt.** Three fix types worked: a rule sentence, a dated record,
   or narrowing what the deliverable asks for. Narrowing was the cheapest: it needs no new record, and an unrequested value is not a
   fork ("not graded", Julia r3 F30).
2. **New sentences open new forks.** Three of Julia's five UGT-failing rounds came from text the previous revision had just added:
   fork H (the "not copied yet" row), fork S (the "go by the build" clause) and fork Y (Leonard's new reply). When a later revision
   added a record under an existing closed rule, it passed first time: ZOM-295 under rule 1 at r14 (fork AK). Add records under
   existing rules, not new rules.
3. **Closing forks costs no difficulty, because judgement traps never landed anyway.** Julia: "Every judgement trap was resisted in 22
   of 22 runs". Difficulty came only from records runs didn't open.
4. **The settling record can itself be the trap.** Julia's fix for fork Y sits in a DM thread reply that runs open about 45% of the
   time. /prompt accepted it as settled. Off-path placement is not penalised so long as the prompt's pointer chain reaches the record.
5. **"Trap hint" has never been applied to a rule in a seeded record.** The term appears only for prompt text, and no finding on it was
   ever confirmed (section 2).
6. **An owner's word settles only when a rule names that person for that exact question and the statement covers that exact scope.**
   Otherwise it is a fork or a trap (section 3).
7. **PR #477, the third item in your last failure, is known-issue card SC-18.** It reads "Don't grade: PR #477's state" and has "Caused
   10 FAILs". Nothing graded should rest on that PR. SC-16 has a similar effect on ticket states (section 6).
8. **Baseline pass rate follows graded weight behind off-path carriers, not the number of traps.** Douglas reached 56.3% that way.
   Every run missing a trap gives a low average but fails spread (Q4: 71.0%, SD 0.016). Aim for records caught about half the time,
   on different habits.

---

## 1. Open-set failures at /prompt and what fixed each one

Type: **RULE** = sentence added or changed in a brief; **RECORD** = new or rewritten dated record; **NARROW** = deliverable or scope cut.

### Julia (ZM difficulty baseline)

| Round | Open item and the two readings | Type | Wording that closed it |
|---|---|---|---|
| r1 F1 | Which tickets get a comment. Rule 6 reached every ticket statement the builds contradict (ZOM-42 "6-7 levels", ZOM-275 message, Not shipped tickets) | RULE | "Ticket comments, only two kinds: where Blake's store builds mail or his reply to it says a ticket's text is wrong, comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them. Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is a bit off. Same tickets, no new ones." |
| r1 F2 | ZOM-282 Live, or Replaced by PR #401 | RULE | "Nothing else makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don't" |
| r1 F3 | Scope start "Apr 21" with no timezone moved ZOM-23 and ZOM-30 (35 vs 33 rows) | NARROW | Start date removed: "created up to Aug 31 (so everything since we started ZM)" |
| r2 F1 | ZOM-250 Editor only, or Replaced by ZOM-277. No record ranked the statuses | RULE | "Replaced: only when another ticket's closing note says it replaces this one. Name that ticket. ... a ticket players never had stays Editor only or Not shipped." |
| r4 H | Mailman, Mayor2, PartyGirl: 0.8/0.8 from git, or "not copied yet" from the sheet. The r3 fix created this | RULE | "Copy its Live tab as it stands: a monster it hasn't copied yet goes on the tab as not copied yet, don't work numbers out from anywhere else." |
| r4 J | ZOM-271's "ATK POWER": 35 or 36 tickets | RULE | "attack power in the title counts too, written out (ATK on its own doesn't)" |
| r7 S | Promotion and demotion window: latest games (write-ups) or first games since the last change (code). The new "go by the build" clause created this | NARROW + RULE | The blanket clause was split by question: "For when a new player gets their starting tier, where a write-up and the build disagree, go by the build. For which games promotion and demotion look at, write it the way ZOM-42 words it." |
| r11 Y | "leave the level editor tickets off too (162, 163, 201 and 250), the designers keep their own list for those". ZOM-173, 277, 315 are also level editor tickets: 24 or 21 rows, 9 or 6 comments | RECORD (reworded) | "take 162, 163, 201 and 250 off the list too. just those four, on top of the ones i already left off. no comments on them either." The category label and the reason were both removed |

Other Julia forks, confirmed or raised but closed by a quote and so not failures:

- **L (raised in r6, r7, r8, r12):** unticked "Before Monday" checklist items read as pending. Closed by the labels "rule 6 change:" and
  "rule 7 change:", the date order after "rest of the card stands.", and the later "no comments on them either."
- **AJ (r13):** ZOM-199 Not shipped. Excluded by rules 1 and 6 plus Blake's mail.
- **AK (r14):** ZOM-295 off under rule 1, settled at first pass.

Non-set failures in the same chain: r3 was coherence (three sheet rows disagreed with match3d commits), r9 was NON-FAIL 3 (an injected
comment after the PR's `updated_at`, fixed by one UPDATE), and r1 also failed Contrived for a hidden destination.

### Bridge (Q4 investor send list)

| Round | Open item | Type | Wording that closed it |
|---|---|---|---|
| r1 F1 | Homa: co-dev talks or strategic investor | RULE | "if we pitched them the bridge or an investment alongside a co-dev deal, they count even when co-dev or publishing was on the table too." |
| r1 F2 | Play Ventures: written no vs "they didn't respond" | RECORD + RULE | Sep 25 correction: "it's still their no for this round"; doc: "A no to our pitch that they sent Griffin or an advisor rather than us counts too." |
| r1 F3 | Does connector outreach count as "we reached out" | RULE | "'Us' includes anyone who reached out or made an intro on our behalf (IH, Matthew, an advisor). Only outreach about the bridge counts, not RFP or partnership mail." |
| r1 F4 | a16z speedrun rejection a pass for the round? | RULE | "the program's decision and the feedback that comes with it aren't their answer on the bridge" |
| r1 F5, F6 | Paul's relayed yes; angels who answered without a call fit no bucket | RULE | "a yes with an amount"; "Angels who've said yes but haven't signed go here too, with the amount they said" |
| r1 F7, F8 | "Last two-way contact": does our trailing reply count; is there a window | NARROW | Column dropped. The term appears 12 times in r1 and 0 in every later round. r1 had offered this: "narrow the sheet so fewer judgment calls are graded" |
| r1 F9 | 1AM Gaming maps to which row | RULE | "1AM Gaming is the March Gaming Fund row on our list" |
| r2 F1 | Initial Capital: "Awaiting reply" or "Not contacted". The list note only implied contact: "an inference can't reject Reading B" | RECORD | Leonard's Sep 9 #bridge-pitch post, later quoted as "pinged Initial Capital on LinkedIn about the bridge" |

r4 failed Originality (dataset meaning 0.804), not an open set; changing the job cleared it at 0.762. r7 to r10 recorded two open
choices as AUTHORIZED_VARIATION because a record allows both: README "Google Sheets or Docs only", and comment "named F/up with and
the name". That is the fourth way to close a fork: let a record allow both answers, with the rubric accepting both.

### Robert (the only Planning task; report (N) = the file with suffix "(N)")

| Round | Open item | Type | Wording that closed it |
|---|---|---|---|
| first F1 | Do Pond5 and ElevenLabs get rows | RULE | Rule 3: "add what it misses inside any other costs-tab line that covers several vendors — each account there gets its own row." |
| first F2 | Hailuo.ai, Dailybot, UA Assets: open or Canceled | RECORD | New owner comments on ENG-2446, ENG-2452, ENG-2481 |
| first F3 | **Which clashes go in the reply** | RULE | Rule 10: "A clash is a decision one of us already posted in #winddown that Sunset's list or SVB's card terms would undo. Moving who pays for an account isn't one (it closes nothing), and requests or suggestions aren't decisions." |
| (3) | Google Workspace had no readable cost; Unity Ads row open; **Zapier's "by when" undecided** | RECORD | Leonard's ENG-2464 figure; project description "we cancelled the unity ads in the UA line after october, so they're not in here"; Oliver's ENG-2439 comment "both games' support buttons now open email instead of helpshift" |
| (6) | Ledger vs Cash P&L conflict under AWS and the ad accounts | NARROW | Rule 3: "AWS and the ad accounts in the UA line stay off the register: he and I are closing those out ourselves." |

### Douglas and Q4: no open-set /prompt failures

- **Douglas** failed only on coherence: a NON-FAIL for a missing `prod` branch, then FAIL 2 for "ok on 0.3.132" comments on Todo and
  Backlog tickets. Its 21 forks all closed, nearly all on the card and doc wording quoted in sections 2 and 3.
- **Q4** passed first time (with the SQL caveat above). Its author ran blind fork sweeps first; the rev3 sweep logged 46 forks: 5
  unsettled, 15 thin, 26 settled.

---

## 2. Scope-rule phrasing, and whether it ever read as a trap hint

### Forms that passed

| Form | Passing example |
|---|---|
| Class definition plus named exclusions | Q4: "anyone outside the investor work who has an offer, a trial, a quote, terms or an ask in front of us and that one of us has actually engaged with: a call, a reply, a sign-up or paper. Cold pitches nobody answered, including ones we only forwarded around internally, stay off it" |
| Closing tail after the rule | Julia: "Every other ticket stays as it is ... even if its wording is a bit off. Same tickets, no new ones."; Douglas: "Same ticket, no new ones." |
| "Only" plus "nothing else" | Julia: "only two kinds"; "Nothing else makes a ticket Replaced" |
| Closed key list | Julia: "just those four, on top of the ones i already left off." |
| A record type as the test | Bridge: "A call counts when it's on Fred's calendar, even if he couldn't make it; calls that never went on Fred's calendar don't."; Julia: "his closing note on those starts with 'tiers:'" |
| Ordered ladder | Q4: "Go top to bottom and stop at the first one that fits." |
| Copy, don't derive | Julia: "don't work numbers out from anywhere else." |
| Handed-off exclusion | Robert: "he and I are closing those out ourselves"; Bridge: "Let's not, only the people the doc says." |
| Tie-break per question | Julia rule 5 (r7 S row above) |
| Default for what's left | Bridge: "Everyone else stays off: they passed without a call or meeting, or nothing from us since Sep 3." |

### Forms that failed

- A category with a partial list, or a reason that reaches a wider class: "the level editor tickets ... (162, 163, 201 and 250), the
  designers keep their own list for those".
- A blanket tie-break: "where a write-up and the build disagree, go by the build".
- A definition with an undefined edge: "both sides took part", "a later ticket's closing note", "Apr 21".
- A new data value with no rule for it: the "not copied yet" row.

### Stray base records

- Fix the set with a rule, then census the base for members. When a stray base record fits, **adopt it**. Q4 did this with Balancy and
  Nintendo, and both became misses in all six baselines (the rev3 pre-check had found Balancy, so it was findable). The reviewer: "If you would rather keep Balancy
  out, the scenario has to exclude it in a record Frederick can see; changing the rubric alone won't do it."
- Reviewers checked strays against the class wording. Rule 1's exclusion handled out-of-scope tickets without a mention: ZOM-359 and
  the "parking this" comments on ZOM-400 and others were rejected as "not task-touched". Scope wording is what protects you here.
- Even Q4's pass carries the limit: "a vendor thread elsewhere that he can see could add a company to the set."

### Did a reviewer call such a rule a trap hint?

**No.** "Trap hint" appears in 31 of the 36 stored /prompt reports across these five tasks. Each hit is either the boilerplate Contrived line or
a P4 candidate against a **prompt** sentence. A search found 0 confirmed findings. The rejected candidates were:

- Douglas: "If his sign-off rules say ...".
- Robert: "before he archives anything on google after the 15th".
- Julia: "if his rules say ...". Julia r14's reason: "It names no ticket, trap or carve-out".

The only Contrived failure was Julia r1 (hidden destination). Eval 1 §2.7 says "A per-case rule belongs in a seeded record, not in the
prompt", and Bridge r10 credits exactly that: "The per-case rules live in Leonard's card comment and doc, not the prompt." Rules naming
specific members passed unchallenged ("ZOM-42 and the Not shipped and Editor only ones included", "1AM Gaming is the March Gaming Fund
row").

The real cost of a rule that names a carrier is on the hardness side. Julia T26: "carriers pointed by the card are no longer levers".
Robert's thread, named in card rule 2, landed 0 of 6.

---

## 3. Owner's claim versus independent confirmation

| Case | Claim | Outcome | Why |
|---|---|---|---|
| Bridge r8 | Paul: "Done, signed it last night" | **Rejected** | "someone only counts as a new investor once the DocuSign Completed notice is in. them telling us they're in doesn't count, and neither does me posting it here". The reviewer also checked no Completed notice existed for Paul |
| Bridge r1 F5 | Leonard's relay of Paul's yes | **Fork** | "No persona-visible record says a relayed yes counts; the relay exception covers passes only" |
| Bridge | Robert's relay of SciPlay's phone no | Accepted | The doc defines Passed, and Robert counts as "us" |
| Bridge | Advisor's read; Leonard's guess "so this is gonna be a no" | Rejected | "An advisor's own read on whether a firm invests isn't the firm's answer."; the reviewer called Leonard's line "his guess" |
| Bridge F11 | Arthur's later post vs his own ZOM-567 log | Later post wins | Doc: "Arthur tracks the tester adds"; post: "whatever the Linear log says". The reviewer: "later, names the same people and the same platform, and explicitly says the Linear log is wrong" |
| Robert rule 5 | "We cancelled it" | Status only | "Closed = the vendor itself has confirmed (their email, an in-app or bot notice, a final invoice) — say where. Requested = one of us has cancelled or asked but nothing has come back from the vendor." |
| Robert rule 8 | Owner's cost figure | Accepted, because the rule says so | "the monthly figure its owner gives in its Linear issue, or else its own last invoice or receipt". Where no figure was readable it failed, and a new owner comment closed it |
| Douglas F7, F8, F10 | Merge, Slack claim, late Approve | **Rejected** | Rule 3: "Merged is not on prod."; doc: "That comment is what puts the PR on prod, not the merge and not a Slack message."; "Approving afterwards doesn't fix it; redeploy."; "only counts if the PR already had an Approve review from someone other than its author" |
| Julia F-O/P | ZOM-281: "checked on the dev build", no PR | Accepted | Rule 3 names Blake on exactly this: "What is in the store builds and what counts as shipped: Blake's store builds mail and his reply to it."; his mail has the store-build scope: "Both were cut from main on Sep 26, and everything difficulty related was merged long before that." |
| Julia F13 | Brian's Slack "the editor bits too" | Rejected | Same rule 3 |
| Q4 F1 | Fred's own "I'll come back to you on this" | Not an answer | A holding reply promises an answer. His tracker still lists the choice as open |
| Q4 D | Leonard's Framewell note | Not an answer to the vendor | "records no answer given to Framewell" |
| Q4 F4 | Pilot dates in our tracker vs Paylane's notice | Vendor notice wins | Newer, more specific third-party record |

### What counted as a settling record

1. **Dated, persona-visible and quoted.** deep_recheck: rejection needs a quote "that rules out Reading B. An inference ('the agent would
   assume', 'B is less likely') is not a reason".
2. **Reachable through the incorporation chain**, or named by a rule.
3. **Covers the exact scope in question.** The Julia pair shows it. A "dev build" note alone would not cover the store builds. A named
   authority's class statement in store-build terms did.
4. **Consistent with the base.** An owner statement can settle UGT and still fail Coherence: Julia r2 (hp-boost comments vs commit
   b511fcbcd5), Julia r3 (sheet rows vs match3d), Douglas ("ok on 0.3.132" on a Todo ticket).

The rule of thumb: if the brief names who or what decides a question, that source settles it, whether an owner or a system notice. If
it doesn't, an owner's word is only a claim. A rule can also go the other way and make the confirmation mandatory, and that creates a
trap (Paul).

---

## 4. Julia-specific data traps

### Tools and carriers

- **DM D05HB64NMQU (Leonard and Julia):** `slack_read_thread` with Leonard's user id returns `channel_not_found`, and runs that didn't
  retry missed the thread. The DM read overflows to a file, and the run's own parser dropped `reply_count`. This is why DM thread
  replies are read only about 45% of the time. It is also all-or-nothing per run, so two thread carriers act as one.
- **GitHub:** `in:comments` search does not reach inline review comments, and a review's body can be empty. Only
  `github_get_pull_request_comments` returns them.
- **Linear:** base Linear has no comments, so every comment is injected. `linear_get_issue` returns none; `linear_list_comments` is the
  only reader.
- **Group DM CAFC495E4006:** was read by every run once card rule 2 pointed to it.

### Base facts that became forks or findings

- **Code vs write-ups:** `WinHistory.cs` counts the oldest games, not the latest (a base bug that produced fork S).
  `TierManager.cs` has `totalGames == 10` and `MaxTier = 5`; the deck says -2 to +2. Damage doesn't stack in `Monster.cs`. Reviewers
  said to keep rubric rows off each of these.
- **Prefab blobs** are cut at 10,240 bytes, so Mailman, Mayor2 and PartyGirl values can't be proved from the file.
  `VarC-Mayor2.prefab` has no Monster component.
- **Sheet dates are checked against main:** /injection r4 failed a History row dated Sep 2 because those values reached main only on
  Sep 6, through PR #417.
- **Commit b511fcbcd5** switched enrage hp off on 2025-06-19. Seeded comments that said otherwise failed.
- **Ticket edges:** ZOM-42 "6-7 levels"; ZOM-271 "ATK POWER"; ZOM-23 and ZOM-30 are Apr 20 in Pacific time; ZOM-173 carries base label
  "Level Editor", which strengthened fork Y.
- **EMPLOYEE_0032_NAME** is the assignee on ZOM-246, 254, 263, 274, 280, 281. It is accepted as shown (PLATFORM:anonymized-token).
- **PR dating:** 0 of 4,304 base comments or reviews postdate their PR's `updated_at`. An injected comment needs an UPDATE.
- **Trello:** the card id encodes its creation second, so a later description needs an `updateCard` action (r1, and /injection r2
  failed on that action's date). Board "Product Roadmap" is a real rename, not an error: DD Product Roadmap changed 2025-07-15.
- **Sharing:** the commenter role on a folder Leonard owns stayed unverified, so keep rubric rows off his exact role.

### Worth carrying into the calendar task

- **Trello card 58 "Minor Bugs to Fix" (BETA: Oct 10 list)** says of ZOM-535 "it's still happens for samsung devices". It was the
  contradiction that helped fail Douglas. It bears directly on your Samsung S23 item.
- **Earlier Julia tasks** (`learnings` §1-3, §54-58): Win & Collect "new runs starting Mon/Wed/Fri while its windows remained open every
  day"; Season Pass Done and merged vs base Slack showing production purchases; "The store version has this change" is a base-git claim.
- **Decoys off the true path:** in the early Julia pre-check, the run never opened #zombie-design or #zombie-bugs (Brian's recap, Vincent's
  request), so those decoys did nothing. In your task #zombie-bugs is live, because a reviewer used it.

---

## 5. What moved pass rates and held the call count

### Baseline results

| Task (mode) | Average | SD | Counted calls | Below 130? | Rows |
|---|---|---|---|---|---|
| Douglas (medium) | **56.3%** | 0.117 | 163-238, avg 196 | none | 76 |
| Q4 commitments (easy) | 71.0% | **0.016 FAIL** | 151-212, avg 189 | none | 102 |
| Bridge (medium) | 77.7% | 0.106 | 109-150, avg 131.5 | 3 of 6 (126, 109, 123) | 40 |
| Card spend (medium) | 78.3% | **0.054 FAIL** | 554-573 | none | 63 |
| Handover (Normal, medium) | 80.8% | 0.161 | 68-100 | Normal horizon | 37 |
| Julia (medium) | 83.8% | **0.099 FAIL** | 357-1,209, avg 818 | none | 81 |
| Robert (easy) | 85.7% | **0.034 FAIL** | 116-143, avg 130 | at least one (116) | 136 |

### What lowered the rate

| Lever | Task | Number |
|---|---|---|
| More graded rows behind carriers at different habits | Douglas round 3 | The round-2 design replayed on a valid rubric: 70.4%, SD 0.021, largest pattern 83%. Adding 5 rows behind `gmail_get_thread` (10/20 runs) and 2 behind early inline comments (4/20) gave 56.3%, SD 0.117, 4 patterns. Runs fell into three tiers by carrier: 71-74 (thread read), 52 (thread missed), 45 (thread and page comment missed) |
| Several independent off-path carriers | Bridge rev11 to rev12 | Rev11: two traps on the swept path, caught 7/7; about 81%, SD 0.06, largest pattern 83%. Rev12: DM, thread under an unrelated root, later post in another channel: 77.7%, SD 0.106, 4 patterns |
| One trap across several cells | Bridge build access | Rewritten to decide 4 cells: "A heavier trap moves each run's score more" |
| Removing the name from a correction | Q4 rev3 to rev4 | /hardness FAIL 2 (one miss) to NON-FAIL 4 (five misses). 71.0%, but all six runs missed the same five records (17 all-fail rows, 0 Linear calls), so SD 0.016 |
| Several carriers feeding one exact-count row | Julia final batch | R5 (exact 23 rows) failed in 5 of 6 runs, each differently: 33 rows (run-1), 29 (run-2: the second thread reply, #265 and #271 missed), 27 (run-4), 24 (run-5: ZOM-295 only, the #271 inline comment), 22 (run-6: ZOM-281 missing). That variety gave 4 patterns, though the average stayed 83.8% |

### What held calls above 130 without padding

- **Per-entity single-object writes with no batch form.** Q4: about 90 writes across 36 companies, every run 151 or more. Bridge: 25
  checklist items, 18 cards and 1 comment took it to 109-150 (from a reported 60-83), but three runs still fell under 130. Size for a
  lean run, not an average one.
- **A rule that forces a per-ticket read.** Julia's "tiers:" closing note needs `linear_list_comments` ticket by ticket: 741 calls, 619
  of them comment scans (r1). A run narrowed the scan to 222 calls (r2) until ZOM-281, a "tiers:" note on a non-Blake assignee, closed
  that shortcut. /hardness runs then made 836-1,084.
- **Per-record native files.** Card spend: 496 Sheets, 554-573 calls.
- **Per-ticket verification.** Douglas: per-PR reads plus a Todo move and comment per ticket, 163-238.

None of this buys difficulty. /hardness r7: "Call volume is not difficulty evidence on its own". Card spend's per-record traps all
leaked, and dd-2024-release-cost ran 1,002 calls and solved it.

### What raised pass rates or wasted effort

- **Wording forks in rules runs read directly.** Julia /hardness stayed FAIL 2 for three rounds: "The last several rounds added more
  wording forks to rules the Agent reads directly, and Opus resolves those reliably."
- **Naming the carrier.** Robert's thread 0/6. Julia T30 (reply in its own Gmail thread) 0/6, because a sender search finds it. T31
  (builds in comments) 0/6, because the value is in a mail every run reads.
- **Routine bulk writes.** Bridge rev17 added about 50 writes and got /hardness FAIL 1.
- **Always-pass rows.** Douglas: 14 rule rows carried about 70% of the weight. Robert: about 100 of 136 rows passed every run. Bridge:
  /rubric fixes took the projected SD from 0.131 to 0.106, and the draft matrix read 70.2% against the verifier's 77.7%.
- **Correlated carriers.** Julia: runs opened all threads or none, and the author's Monte Carlo at correlation 0.9 gave P(all gates) about 0.02 (a model, not a measurement). Bridge rev12 batch 1: SciPlay
  and Paul were caught by the same runs, largest pattern 80%. Same SQL, batch 2 passed, so sampling alone moved this gate.
- **Compact-rubric projections.** Douglas's 36-39% estimate was really 70.4%; three rounds were wasted.
- **Too little weight behind the carrier.** Julia round 5: 24% of weight behind thread replies, so "even 5 of 6 landed misses leave the
  average at 77%". Seven hardening rounds still ended at 83.8%.

### Measured read rates, for placing settling records

| Carrier | Read or caught |
|---|---|
| Hub, named card, notes doc, invite | about 100% |
| Reply in its own Gmail thread, found by a sender search | 6/6 |
| Code | about 80% |
| PR #243 and #244 inline comments | 70-75% |
| `gmail_get_thread` on a named thread | 10/20 |
| Later post in another channel, no pointer keywords | 5/6 (found via "tester"), then 3/6, same SQL; Q4's notes also cite 0/7 on an earlier placement |
| DM thread replies | about 45% |
| 1:1 DM about one item | 6/15; 1/6, then 3/6 |
| PR #271 inline comments | 5 of 15; about 50% in the report's 22-run count |
| Thread reply under an unrelated root | 4/15; 1/6, then 3/6 |
| Early-PR inline comments; Confluence page comments | 4/20 each |
| De-named record, or a service nothing points to (Q4) | 0/6 |

---

## 6. Lessons for per-beat still-to-do cells

The first group is observed in the tasks. The mapping to your last failure is my inference, based only on CENSUS_BRIEF.md.

### Observed

1. **A still-to-do cell is an open set, one per beat.** Its nearest precedents are Julia r1 F1 (which tickets get a comment), Robert's
   clash list and Robert's by-when cell. All three needed a class definition with named exclusions plus a closing tail.
2. **Rule the empty case.** Robert rule 6 is the template: "Moved and Closed rows get a dash, unless an export or a switch-over still
   has to happen before the access ends — then the day before it ends." Julia: "(leave it blank if it never got done)" settled ZOM-280's
   cancel date. Even so, that "unless" clause in Robert opened the Zapier fork until a record closed it.
3. **Drop the cell if a rule can't close it.** Bridge's last two-way contact, Robert's AWS rows.
4. **Scope tie-breaks to one question.** A blanket "go by X" sends readers to everything X says (Julia r7).
5. **Don't put a category label over a partial list, and don't give a reason wider than the list** (Julia r11).
6. **Watch date edges and cutoffs.** Julia r1 F3 failed on a timezone. Bridge F25 passed because each item was the same day in both
   zones. ENVIRONMENT allows either day where Pacific and UTC differ.
7. **Status notes need lifecycle care.** A fixed-and-verified note on an open ticket always fails, even if no agent trips on it (Douglas
   r1). Your own memory note adds the positive form: every open ticket near a beat says whether it has to land.
8. **Rubric shape.** Robert: split "what happens" from "by when", include "nothing is due" rows, and one Process row. Each all-pass
   per-beat row lowers SD, so give every carrier at least 2 weight-5 rows of its own and spread carriers over different habits.
9. **Sweep before submitting.** Q4's blind sweep preceded its first-time pass. Julia found forks one at a time over 14 rounds.

### Applied to your last failure

- **(1) ZOM-534 "on main" vs on prod, only the owner's claim.** Same gap as Julia's dev build vs store build, and Douglas's rule is
  explicit: "Merged is not on prod." Two precedents: name who decides that question for this scope, as card rule 3 did, and have that
  person say it in prod terms (Julia's class statement); or define the settling record (Douglas's "prod:" comment, Bridge's Completed
  notice). The record must be true to git.
- **(2) Samsung S23 and "an unverified build or platform is a still-to-do".** This is the Julia r1 F1 shape: a category clause that any
  stray base record can satisfy. Replace it with a closed class and a tail, in the form of Robert rule 10 or Julia's "only two kinds".
  Alternatively adopt the item as a real still-to-do, as Q4 did with Balancy. Check Trello card 58 first (section 4).
- **(3) PR #477.** Card SC-18. Whatever settles this should say whether the title change has to land, and should not depend on the PR
  being open or closed.

### Known-issue cards that touch your beats (`references/known_data_issues/synthcut.md`)

| Card | Don't grade |
|---|---|
| SC-18 | PR #477's state (10 FAILs) |
| SC-16 | Linear status as proof of whether work shipped (11 FAILs). Any still-to-do read from a ticket state is exposed |
| SC-15 | What is left on ZOM-521 (11 FAILs); already failed your task once per your memory note. Use child states |
| SC-8 | Whether the ZOM-475 glass crash is fixed (17 FAILs) |
| SC-38 | Season Pass ship date or analytics status (3 FAILs); avoid ZOM-529 |
| SC-47 | Weekly Quests status (3 FAILs); the live-ops calendar's "Failed Nov 2024" is contradicted |
| SC-62 | Reward-import cadence (the live-ops calendar is contradicted) |
| SC-31 | Live-ops weekend outage end date or affected events |
| SC-57 | Posting in #zm-collect-win |
| SC-68 | When Boss Arena reached prod |
| SC-19 | Matching app versions to a store build in Slack; match by date |
| SC-36 | Invite or share lists built from channel or calendar membership |

### Open question: extras in a still-to-do cell

CENSUS_BRIEF says "additive" did not save a candidate. Julia's reports did treat some extras as not material: F-AD (builds in all nine
comments) and F-rules-enrage-note ("neither required nor wrong"). The difference looks like whether the extra changes graded content.
A notes column outside the graded cell, allowed by a brief line, might use the AUTHORIZED_VARIATION route. That is **my suggestion and
no completed task tested it**.
