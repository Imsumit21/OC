<!-- Source: CB guideline PDF (watermarked copy) (Archive 6.zip, received 2026-11-01). Text extracted with pdftotext; watermark lines removed; two-column pages may interleave. -->

Example Task
A complete Long-Horizon task, end to end, adapted to Spec V2 · Updated October 26, 2026
This task was selected by the ML team as a high-quality example. Everything below is real output from it. The
original was built with a golden answer and two hints; what follows shows the same work expressed the V2
way, as Oracle Events.
Baseline table note updated: new tasks run on Opus 5.5.
Marcus Bennett — Artist (Design)
Persona
1 · The assignment
Original release.
Replaced with the ML-selected task and adapted to Spec V2. Golden answer re-expressed as Oracle
Events. Hint, reference run and silver-trajectory sections removed. Baseline model updated to Opus 5.5.
Baseline table notes that this run used Opus 5.5. New tasks run on Opus 4.8.
Marketing and GTM
Competency
Ambiguity · Dynamic Change · Multi-Source
Characteristics
Long-Horizon
Task type
Analysis and Synthesis, stacked with Retrieval and Actions
Task skill
Prompt cleaned up: capitals and apostrophes restored, and the line hinting at the trap removed. The
baseline ran on the original. New section 9: the same task, done badly.
Updates
Change log
Human time estimate
Injected friction
Slack · Snowflake · GitHub · Confluence · Linear · Trello
Services that carry weight
Note how the persona and the competency relate. Marcus is an artist, not a marketer — but he made the marketing
videos, the capture tool and the playable visual effects, so the GTM work genuinely went through him. That is what
a well-chosen competency looks like: not the obvious match for the job title, but a defensible one.
2 · The prompt
Robert wants the Combo Fighters launch written down properly before
Leonard archives everyone's Google accounts on February 15, and honestly
I don't think anybody actually knows what state it's in. I did the
marketing videos and the capture tool and the playable VFX so most of the
creative side went through me, but the campaign and the paid side was
Leonard and I only ever saw pieces of it in chat. Can you work out what
really happened and what is still genuinely open? Then put the record
somewhere proper next to the rest of the launch stuff and raise tickets
for whatever someone needs to pick up. After this week there's nobody
left to ask.
How the prompt achieves it
Property
Why it works
Marcus explains what he did and did not see, which is why he is asking rather
than answering
It justifies the persona
Nothing warns the agent about the summaries it will find. It has to work out
for itself that the newest one is wrong
It leaves the trap hidden
Work out what happened, then write the record and raise the tickets —
investigation and action
It has two phases
Nothing in it says what the answer is. “I don't think anybody actually knows”
is the opposite of a root cause
The route varies; the destination does not. One record, filed alongside the
launch material, plus tickets for the open items
It has unique ground truth
It is not pre-solved
No document, no channel, no ticket, no figure. It names a deadline and a
feeling
Normal capitals and spelling, no markdown, one long run-on sentence that
doubles back. Nothing an AI-text detector would flag
It reads like real typing
It names nothing
The baseline in section 6 ran on an earlier wording of this prompt. It was all lowercase, left out the apostrophes and
also asked for “what we actually shipped and spent versus what people think we did”, a line that hints at the trap.
THE DATE
“February 15” is absolute and sits one day after the frozen clock — which is exactly right. It is a deadline, not a
description of something that already happened. A prompt describing a February 15 event as completed
would be a failing error.
3 · What was seeded
One Slack message, from Robert, dated February 13, 2026:
"before Leonard archives everything I want the combo fighters launch
written down somewhere that isn't this channel. As far as I'm concerned
we shipped it and ran it across all the networks we wired up, meta was
just the biggest spend. The playable is the only thing I'd call
unfinished. Correct me if I'm wrong on any of that."
It is the newest message on the subject, it comes from the chief product officer, and it addresses the persona by
name. Both halves of it are wrong, in opposite directions:
“we ran it across all the networks” — meta was the only network that ever bought an install. The other six
names in the codebase are monetization placements, not acquisition channels.
THIS IS DYNAMIC CHANGE DONE PROPERLY
“the playable is the only thing I'd call unfinished” — the playable is the one creative that actually shipped.
Nine events cover the critical path. Three of them, in full:
Aggregate paid spend by network for the title.
Snowflake AD_SPEND_DAILY, filter game_id = combo_fighter
Expected: 152 rows, channel = meta on all of them, 4510.33 USD,
615 paid installs, 2025-12-26 to 2026-02-08.
Read the 2026-02-11 playable thread to its end, not to 21:08.
Expected: rejection 21:03, workaround 21:10, "it works" 21:22,
campaign on 21:37, bid set 21:42, iOS-only confirmed 21:54.
Establish which build the January approval message refers to.
slack_conversations_history (channel C09UHHN6PFZ, 2026-01-17..20)
Expected: 1.0.56 posted 01-17; approval 01-19 06:41; 1.0.57
submitted 06:44 and released 01-20.
4 · The Oracle Events
The most authoritative-sounding summary in the universe is the thing the agent has to overturn. And it is not
a truthfulness defect on the author's part — truthfulness applies to what you assert in the prompt, not to
what a character believes. Robert being wrong is realistic, and his own message ends with “Correct me if I'm
wrong on any of that.”
What makes them good
Every event names the service, the filter and the expected values. That is what /oe checks against, and it is
what lets the rubric be written without going back into the universe.
OE 7 is the whole task in one event. The instruction is explicitly “to its end, not to 21:08” — the author knew
where the agent would stop and recorded the correct behaviour precisely.
No event describes the final response. OE 4 records what the query returns, not what the write-up should say
about it. The write-up is the rubric's business.
No non-actions. Nothing says “the agent does not stop early”. OE 7 says what reading to the end actually
produces.
5 · The rubric set
31 criteria, all Outcome. No Process rubric was needed, because every requirement was provable from the final
record. That is a perfectly normal shape for a task this size.
Why that weight
Agent's record states build 1.0.10 was reviewed and
published on 2025-12-21
Agent's record identifies Leonard's February 15 archive
as the deadline
Stated directly in the seeded message
Agent's record states lifetime installs total 901 — 615
paid plus 286 organic, split 695 iOS and 206 Android
One aggregation over the install tables. Two axes:
discovery effort and reasoning depth
Agent's record states the playable shipped and was live
Requires reading one thread past its apparent
conclusion
Criterion (abbreviated)
One source, literal lookup, no reconciliation and
no reasoning
Three timestamps across two services, with a
three-minute gap that decides the answer
Slack, GitHub and Snowflake all have to be
reconciled against each other, and a distinction
has to be inferred that no single source states
Agent's record establishes that 1.0.57, not 1.0.56, is
the build that went to store review
Agent's record classifies the AppLovin, Unity,
Ironsource, AdMob, liftoff and mintegral mentions as
monetization placements that bought no installs
What the set deliberately does not do
It does not enumerate branches. Where more than one filing location was defensible, the criterion is phrased
broadly enough that either satisfies it.
It does not grade every row of the spend data. It grades the totals, the classification, and the two figures that
only exist after reconciliation.
It does not require a section header called “Confirmed vs Pending”. It requires confirmed items to be separated
from pending ones.
It does not require a document titled “Combo Fighters Launch Record”. It requires a launch record in the same
folder as the existing launch material.
Result
6, all completed
Every one correct
Both inverted
Consequential findings
Totals reported
Tool calls, best rollout
Best rollout
Opus 5.5 (the baseline at the time; new tasks also use Opus 5.5)
Rollouts
Measurement
6 · The baseline
Opus reported the playable as unfinished and the title as live on Google Play. Both are false, and both are exactly
what Robert's message claimed. The model found the data, computed it correctly, and then deferred to the most
confident-sounding summary in the channel.
Not in the volume of data — the model handled 12,100 messages and several Snowflake tables without
trouble. It sat in knowing when not to stop. The playable thread reads like it concluded at 21:08; the story
continues until 21:54. That single structural choice is what produced a task nothing passed.
WHERE THE DIFFICULTY ACTUALLY SAT
The justification includes the dead ends: a person without search tooling scrolls the wrong month, reads the partner
channel that covers the same window for a different title, and opens marketing documents belonging to the other
two games. The arithmetic adds up to the number entered, which is what the step requires.
Read the channel across the launch window, ~12,100 messages
Reconstruct the build history from the submission messages
Read the playable thread past the apparent conclusion
Pull daily spend, installs and revenue by hand
Reconcile the design doc against the data
Find the PRs and confirm what each contains
Write the record, then raise the tickets
7 · The human time estimate
8 · What to take from this task
1. Seed one message, not ten. A single authoritative-but-wrong summary from a senior person did more work
than any amount of additional data would have.
2. Put the correction second in discovery order. The trap only works because the agent meets the claim before it
meets the evidence that overturns it.
3. Name nothing in the prompt. Every channel, document and figure the agent needs was discoverable. None was
handed over.
4. Write Oracle Events with real values in them. “152 rows, all channel = meta , 4510.33 USD” is what makes
both /oe and the rubric step straightforward.
5. Weight by difficulty. The criterion that carries the task's whole point — a record exists in the right place — is
not the highest-weighted one. The reconciliations are.
6. All-Outcome is fine. If every requirement is provable from the final state, you do not need a single Process
criterion.
9 · The same task, done badly
This version uses the same task, written badly on purpose with the mistakes reviewers find most often, so you can
compare it with sections 2, 4 and 5. Each numbered marker points to a problem explained below it.
Prompt
Please conduct a comprehensive review of the Combo Fighters launch. 1 Use slack_conversations_history on
channel C09UHHN6PFZ and query AD_SPEND_DAILY in Snowflake. 2 The issue is that Robert thinks we ran ads on
every network, but the other networks were only ad placements, and the playable did ship. 3 Create a Google
Doc titled “Combo Fighters Launch Record” with the findings, or just summarise it back to me if that's easier. 4
Also, can you book a meeting with Julia next week to go over Q2 plans? 5
Pre-solved (Fail). It gives away both findings the task is built around.
Explicit tool mention (Fail) and an opaque ID. It names a function and a raw channel ID that Marcus would
never type. It also tells the agent where to look, which removes the discovery.
Contrived. Formal wording that reads like an LLM wrote it. The AI-text detector would flag it.
Multiple Valid Answers (Fail). One run writes a doc, another just replies. A Google Doc is also a weak home
when the Google accounts are being archived.
Bolt-on (Fail) and a relative date. The meeting has nothing to do with the launch record, and “next week”
isn't an absolute date.
The agent searches Slack for the launch discussion.
The agent looks at the ad data in Google Sheets.
Expected: spend was mostly Meta.
The agent does not stop at the first message it finds.
The agent's final response explains that Robert was wrong
about the networks and the playable.
The agent creates the Google Doc.
Oracle Events
OE 1 has no Expected line. Nothing to check against the universe.
OE 2 names the wrong service and a wrong fact (Inaccurate). The spend is in Snowflake, not Sheets, and every
Combo Fighters row there is Meta, not “mostly”.
OE 3 is a non-action. “Does not stop” isn't a step. OE 7 in section 4 says what reading to the end actually finds.
OE 5 has no location and no Expected line.
OE 4 describes the final response. That belongs in the rubric.
Incomplete. The build history, the GitHub check, the playable thread, the installs and revenue, and the tickets
have no steps at all.
Not self-contained: doesn't say it was
1.0.56, so any build number passes.
The response identifies the build that was approved.
The Agent uses slack_conversations_history to read the prototype
channel.
Names a tool, and it's a Process criterion
the Outcome criteria already cover.
Negative framing with no prohibition in
the prompt, and nothing a grader can
The Agent does not trust Robert's message.
Incorrect: repeats both of Robert's
wrong claims. Also two facts in one
criterion.
The Agent reports that the launch ran on all the ad networks they
wired up and that the playable is unfinished.
Weight 2 isn't allowed. Two claims in
one, and “well formatted” can't be
checked.
The Agent's record is well formatted and lists the open items.
Hard-coded title the prompt only set
because it was badly written, and a
location that won't survive the Google
archive. Section 5 asks for a launch
record in the same folder as the existing
launch material.
The Agent creates a Google Doc titled “Combo Fighters Launch
Record”.
Problem
Criterion
Rubric
Missing coverage. There are no criteria for the build history, the network classification, the spend totals, the
playable shipping, or the tickets. An agent could miss all of these and still score well.
Nothing for the bolt-on. The Julia meeting shouldn't be in the prompt at all, so no criterion should reward it.
Original Conference · Example Task · Spec V2 · Updated Oct 26, 2026
