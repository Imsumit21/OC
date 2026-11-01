<!-- Source: CB guideline PDF (watermarked copy) (Archive 6.zip, received 2026-11-01). Text extracted with pdftotext; watermark lines removed; two-column pages may interleave. -->

CB Guideline: Reaching the Tool-Call
Minimum (50 or 100)
This guide is based on 10 real Enterprise Atlas tasks and the Opus 5.5 baseline runs behind
them (runs from Sep 29 to Oct 10, 2026). One task fell short, four only just made it and five
cleared it easily. For each one we looked at every tool call in a representative run to see
where the calls actually went. Keep the one-page checklist (Appendix) open while you
design.
Super-Long-Horizon: paused. You'll see it on the task screen, but it isn't assigned.
Long-Horizon: 100 or more (100–500+).
The result:
If any rollout scored 100% on your rubric, that run is the golden run, and its
count is the one that counts. If more than one scored 100%, the lowest count
among them is used.
If none scored 100%, the average of all six is used.
Inside your tier is a PASS.
A Normal task over 100 is a NON-FAIL, because it belongs in a higher tier.
Under your tier is a FAIL.
Part 2. Where tool calls actually come from
What we saw in the 10 tasks:
No review checks this early. /prompt and /hardness don't count calls. You first see
real numbers on the Opus pre-check and the six baseline rollouts. The pre-check is a
single run of the same model, so treat its count as an early warning.
Padding is a failing error on its own. Blocked calls, repeated calls and steps added
only to raise the number all count against you. The count has to come from real work.
Volume comes from items that each need their own check. The biggest task asked
for every open Domino Delights ticket to be triaged. The run opened 152 tickets and
Normal: 50–100 tool calls.
What gets counted: your six Opus 5.5 baseline rollouts.
The tiers:
Part 1. How the count works
1. The items: what is the set the agent must work through (tickets, obligations, claims,
contracts, screens)? How many are there, as the persona would see them on the
universe date?
2. The calls per item: what must the agent open to decide each one? In our runs, one item
that lived in one place took about 2 calls, for example open the ticket and then read its
comments. Every extra source an item needs adds more.
3. The finding: a careful agent spends a good part of the run searching and listing. In the
Normal runs, search and list calls made up 14 to 53 of the total.
4. The writes: count one call for each separate write the task needs: each reply, each
ticket update, each sheet edit.
5. Leave a margin. Normal tasks that averaged 50 to 54 had 2 or 3 of their six runs under
50, so a task that averages just over 50 is one re-run away from failing. The same applies
at 100 for Long-Horizon. For Normal, also stay clear of 100. One task averaged 95.7, and
one of its runs reached 112.
Add a call budget to your decision map:
Part 4. What adds real calls (do these)
Make the work about a set, and make every item count. Use "every open ticket",
"each obligation", "each item Leonard flagged", where the agent can't skip an item
without getting the result wrong.
Make each item need its own record. If one list or search call shows every item's
status, the set costs one call. Put the deciding fact for each item where only that item's
own comments, thread, PR or email reveal it.
Part 3. Plan your call budget before you write
read each ticket's comments, about 2 calls per ticket, for 402 calls on average. The
prompt was three sentences.
Per-item writes count too. One task had the agent take departed staff off every open
Linear ticket. That was 91 separate updates, plus 12 new tickets, for 170 calls on
average.
Short prompts can still produce big counts. "Go through the stuff I flagged, fix
whatever doesn't hold up" averaged 86 calls, with 95 on the golden run. Each flagged
claim in the board draft had to be checked against Linear, GitHub or Snowflake, and then
Touching many services does not raise the count. The task that fell short used 8
services and averaged 46 calls. A borderline task used 10 services and averaged 54.
Making more files and messages does not raise it either. The task that fell short
made 10 writes: a sheet, a doc, sharing and a Slack post. It still averaged 46.
The same task gives different counts on every run. The six runs of one task were 12
to 27 calls apart on Normal tasks, and over 100 calls apart on the 402-call task.
Make each item need a second source. For example, a claim in a doc has to be checked
against Linear, GitHub or Snowflake. This also adds difficulty, because a careless agent
trusts the first source.
Tie a write to each finding. If an item turns out stale, wrong or open, it gets its own
comment, update or ticket. The writes should follow from what the agent finds, not from
a list in the prompt.
For Long-Horizon, plan for a big set or deep items. The two Long-Horizon tasks that
cleared 100 comfortably worked through 91 and 152 items.
Part 5. What doesn't add calls, or backfires (avoid these)
"How many [items] fit [my set] for [persona] on [date]? List them with where each
one's status is decided."
"Can one search or list call tell the status of every [item], or does each need its own
record opened?"
"Which [items] need a second service to confirm?"
Do the math: items × calls per item + finding + writes. Is it inside your tier with room to
Ask the portal assistant (copy and paste):
Count the items in your set from the persona's view, and write the number down.
Part 6. Self-check before you run /prompt
A small, fixed set. Four tests or four screens can't produce 50 calls of real work,
however many services you add.
The answer in one channel or one thread. The task that fell short had most of its
answer in one publisher channel.
Extra services or extra output files just to add steps. Neither raised the count in our
sample.
Volume without difficulty. Calls alone don't make a task hard. The 170-call unassign
task scored 85–95% on every run (89.5% on average). A Normal task at 95 calls
averaged 90.8%. Both would fail today's 85% weighted-pass limit for medium tasks.
Mechanical rows raise the count but not the difficulty, so pair volume with items that
need judgement.
Padding. Don't ask for repeated checks, force errors or add steps nobody would really
take. Padding is a failing error.
Step lists in the prompt to make the agent do more. This fails the prompt review and
makes the task easier.
Over-scoping a Normal task. Over 100 is a NON-FAIL. If your set is that big, the task
belongs in Long-Horizon.
Part 7. Reading the count after the baseline and fixing it
widen the set so more items really need checking
Look at all six runs, not just the average. Note the lowest and highest counts and how
many runs fall under your tier.
Check for a golden run. Its count replaces the average. In all three of our tasks that had
a golden run, it was the run with the most calls. Careful runs check more, so a golden
run usually helps. One task averaged 49, which would have failed. Its golden run made
59 calls, so it passed.
Watch for a fast run that scores 100%. It sets your count, so a shallow perfect run can
fail you. It also means the task is too easy.
If you're under the tier:
Check that every item changes the result. If an agent could skip an item and still pass
the rubric, that item adds no real calls.
add the write that each finding calls for
Don't add services, files or steps in the prompt. None of these raised the count in our
sample, and steps in the prompt fail review.
After changing the scope, run the one-correct-answer checklist on the new items, and
update your OE and rubric rows to cover them.
make each item need a second source
move each item's deciding fact into its own record, so one list call can't answer it
Part 8. Worked examples (real tasks)
1. Under the bar: a small set in one channel
Task: A marketing persona asks about the Brazil ad tests: list every test and its date, what
was broken while each one ran, and what's still broken now.
Counts: six runs of 41 to 53 calls, average 45.8. Five of the six runs were under 50. FAIL
(Normal).
What the runs show: The set was four tests, and most of the answer sat in one publisher
channel. The run's 18 Slack calls did most of the reading. It made 10 writes (a sheet, a doc,
sharing and a Slack post), and they did not lift the count.
What would raise it (Part 4): Make each test need its own evidence that one channel
doesn't give, for example the build, ticket or config change behind each break. Or widen the
set to every campaign the publisher ran. Don't add another output file.
2. Saved by the golden run
Task: Reconcile a stale optimization board against what actually shipped, then report how
many screens made it into the client.
Counts: 58, 48, 59, 43, 43, 43. The average is 49.0, which would fail. The 59-call run scored
100%, so the count is 59. PASS (Normal).
Lesson (Part 7): The 100% run made 35 GitHub calls, checking screens against pull
requests, and it was the longest of the six. Design so the correct path is the thorough one,
but don't rely on the golden run. Four of the six runs were under 50.
3. A short prompt with a big count: per-item checks
Task: "Finish the board update draft: go through the stuff I flagged, fix whatever doesn't
hold up, and sort out whatever's still hanging off it."
Counts: six runs of 71 to 95 calls. The golden run made 95. PASS (Normal).
4. A big set at Long-Horizon
Why it works (Part 4): Each flagged claim had to be checked in another service. The run
made 16 Linear, 16 GitHub and 8 Snowflake calls, then left 5 ticket comments and 4 ticket
updates. The prompt didn't list a single step.
Counts: six runs of 372 to 479 calls, average 402. Weighted pass rate 65–70%. PASS (LongHorizon).
Task: "Leonard asked me to triage all the open Domino Delights tickets... dig up where each
ticket actually stands now, do everything he asked and reply to him."
Why it works (Parts 2 and 4): The run opened 152 tickets and read each one's comments.
Each ticket's real status was only in its own history, so no shortcut existed. The volume
came from judgement, so the task was both long and hard.
5. Long enough, but too easy
Task: Work out which contracts and subscriptions are really closed, open a ticket for each
one that isn't, and unassign departed staff from every open ticket.
Counts: six runs of 161 to 179 calls, average 170. PASS (Long-Horizon). But every run
scored 85–95%.
Lesson (Part 5): 91 of the calls were the same unassign update. That raised the count but
not the difficulty. Today the task would fail the 85% weighted-pass limit. Get your volume
from items that need judgement, not from repeated mechanical writes.
6. Borderline Long-Horizon
Task: Two related asks: find where the End Game VFX sign-off really stands and record it
where it was asked for, then correct every place that still shows old numbers about the
video pipeline.
Counts: 105, 108, 107, 107, 86, 106. Average 103.2. PASS (Long-Horizon), but only 3 calls
over the bar.
Set defined, and items counted from the persona's view on the universe date.
Every item changes the result; none can be skipped.
Each item's deciding fact lives in its own record, not in one list or one channel.
Items that need a second source are identified.
One write planned for each finding that needs action.
Budget: items × calls per item + finding + writes, inside the tier with a margin.
Normal stays clear of 100.
Tier noted: Normal 50–100, or Long-Horizon 100+.
The answer in one channel or thread.
Extra services or files only to add steps.
Repeated mechanical writes as your main source of volume.
Step lists in the prompt.
Padding: blocked, repeated or pointless calls.
A small, fixed set.
Golden run checked; its count replaces the average.
All six counts read: lowest, highest, how many under the tier.
After the baseline
Under the tier: widen the set, give each item its own record, add a second source per
item, add per-finding writes.
Then re-check one correct answer on the new items, and update the OE and rubric.
A fast 100% run? The task is too shallow.
Before you write the prompt
Appendix. One-page checklist
Lesson (Part 3): The task touched 11 services and made 23 writes (12 Slack messages and
6 Trello comments among them), and it still only just cleared 100. One run under 100 shows
how small the margin was. Plan for more items that each need checking, so normal run-torun variation can't drop you under.
