<!-- Source: CB guideline PDF (watermarked copy) (Archive 6.zip, received 2026-11-01). Text extracted with pdftotext; watermark lines removed; two-column pages may interleave. -->

Oracle Events
HarmonyGames · Universe date: October 1, 2025 or February 14, 2026, 00:00 UTC · Updated October 19, 2026
NEW IN SPEC V2
What replaced the golden solution, how to write a set that passes /oe , and how to turn it into a rubric.
Updates
1 · What changed, and why
New document. Oracle Events replace the free-text golden answer; /oe replaces /golden ; the toolcall minimum now attaches to the golden run, not to the Oracle Events set.
Second universe date added: October 1, 2025. Review steps follow the Eval Portal.
Change log
This guideline is new. It replaces the golden-solution material that used to sit inside Overall Task Flow and
Rubric Writing. If you tasked on this project before September 2026, read it in full — the artifact, the check
that validates it, and the way it feeds the rubric have all changed.
Written before the rubric, and used to derive it
Prefill is off. You write every criterion yourself, from your own Oracle Events
Rubric prefill generated a draft set
from the golden answer
Checked by /oe
Written after the rubric, or alongside
Checked by /golden
It uses the golden run — a rollout that scored 100% on your rubric — if you
have one, and the average across all six only if you do not
The tool-call minimum used the
rollout average
Oracle Events — the key steps a correct agent takes, from discovery to
completion
A free-text golden answer describing
the finished result
Earlier
The reasoning is that a finished answer tells a reviewer very little about whether a task is solvable, and nothing at all
about how. A step list tells them both.
2.1 They prove the task is solvable
2 · What Oracle Events are for
With hinting removed from the task, there is no longer a hint that can rescue an agent from a prompt that turns out
to be impossible. Your Oracle Events are the demonstration that a correct path exists: following them literally
should produce a correct trajectory.
2.2 They drive the rubric
Every action in your Oracle Events becomes an Outcome rubric. Gaps that no Outcome can cover become Process
candidates. Writing the Oracle Events first makes the rubric step substantially faster and materially better — the
most common rubric defect in the last audit was missing coverage, and a complete OE set is the cheapest
protection against it.
2.3 What they do not do: set the tool-call minimum
ORACLE EVENTS ARE NOT A GOLDEN RUN
This one causes confusion, so it is worth stating plainly. The tool-call minimum for your tier is measured against the
golden run where one exists — and a golden run is a baseline rollout that scored 100% on your rubric, meaning it
passed every criterion. It is a run the model produced. If no rollout reached 100%, the minimum is measured
against the average across all six.
The important inputs: identifiers, filters, date ranges, values
Parameters
Which tool and which service, matching where the data actually lives
What the step should retrieve or produce
FORMAT
What needs to be discovered or verified before the agent can act
Tool / Service
Expected Data
What needs to happen — search, retrieve, send, create, update
Information
What goes in it
Action
3 · The five fields
Your Oracle Events are a path you write. They are required on every task, they prove solvability and they drive
the rubric — but they have no bearing on how your tool-call count is measured. Counting the steps in your OE
set and comparing that number to your tier minimum tells you nothing about whether the task passes.
Oracle Events are free-form text, not structured JSON. They are written in a field that blocks pasting, because
they must be written by you rather than generated. Number them, and keep each one to a few lines.
Establish which build the January approval message refers to.
slack_conversations_history (channel C09UHHN6PFZ, 2026-01-17..20)
Expected: 1.0.56 posted 01-17; approval 01-19 06:41; 1.0.57
submitted 06:44 and released 01-20.
4 · What a good event looks like
Establish that the primary lookup is unavailable and recover.
gmail_search_messages (query: "Season Pass rollback")
-> returns a server error on every attempt
Agent then reads the same thread from the shared drive copy.
Expected: the rollback decision and its date, from the drive document.
Aggregate paid spend by network for the title.
Snowflake AD_SPEND_DAILY, filter game_id = combo_fighter
Expected: 152 rows, channel = meta on all of them, 4510.33 USD,
615 paid installs, 2025-12-26 to 2026-02-08.
Each one names the action, the service, the filter and the expected values. That is what /oe needs in order to
check it, and it is what lets you write the corresponding rubric without going back into the universe.
The prompt asks for tickets to be raised and no event covers it
Includes every required write or action
Nothing records that B can only happen once A has produced its
Includes the dependencies between steps
A fact appears in the expected data with no event explaining
how it was obtained
Includes the key discovery and retrieval steps
The set jumps from “searches Slack” to “notifies the owner” with
the analysis missing
Covers the full critical path
What fails it
Requirement
5 · Completeness
“The agent's final response explains that the tutorial change
caused the drop”
Does not describe what the final response should
6 · Accuracy
Oracle Events describe the path. What the agent ultimately reports is graded by the rubric, not recorded here.
If you find yourself writing “the response explains…”, convert it into the discovery step that produced the
finding.
THE FINAL RESPONSE IS NOT AN ORACLE EVENT
Tools and services match where the data actually lives. Naming Google Sheets for a figure that only exists in
Snowflake is an accuracy failure even if the figure itself is right.
Parameters, entity names, IDs and expected data match the universe. Check each one against the explorer. A
channel ID from memory is the classic way to fail /oe .
Following the events literally produces a correct trajectory. Read your own set as if you were the agent. If a
step cannot be executed from what the previous steps produced, something is missing.
7 · No non-actions
An Oracle Event must describe an observable action or discovery. Statements about what the agent refrains from
doing are not events.
“The agent does not stop at the first explanation it finds.”
“The agent does not stall when the search fails.”
“The agent does not give up.”
✓ “Establishes that the mail search is unavailable, then reads the same thread from the shared drive copy.
Expected: the rollback decision and its date.”
✓ “Reads the 2026-02-11 playable thread to its end. Expected: rejection 21:03, workaround 21:10, campaign live
Step 1 — write every Outcome
8 · From Oracle Events to rubrics
For every action in your Oracle Events, write an Outcome rubric verifying the result, plus a content rubric if the
prompt set specific requirements about what that result must contain. For every key fact the user asked to be told
directly, write an Outcome covering the final response.
Step 2 — look for the gaps
Once all the Outcomes exist, ask whether any requirement — explicit or implicit — is left that no Outcome can
verify. The primary case is ordering: A must happen before B, but both Outcome rubrics pass regardless of
sequence. In rare cases source verification qualifies too.
Step 3 — apply the three-condition test
1. The requirement is needed by every valid solution path, or the criterion is phrased broadly enough to allow
alternatives.
3. The criterion describes a behavioural property, not an execution trace.
2. A stricter Outcome rubric cannot capture the same requirement.
If any condition fails, tighten the Outcome instead. If all three hold, write the Process rubric. When in doubt, default
to Outcome.
THE RULE, STATED PRECISELY
Rubric it produces
[wt 3] Agent notifies the owner of the discrepancy.
[wt 3] Agent schedules the review.
[wt 1, Process] Agent notifies the owner before scheduling the
review — ordering, which neither Outcome can prove
OE 9 — Notify the owner, then schedule the
review
[wt 5] Agent's record classifies the AppLovin, Unity, Ironsource,
AdMob, liftoff and mintegral mentions as monetization
placements that bought no installs.
[wt 3] Agent's record states total paid spend of $4,510.33 across
the campaign window
OE 4 — Aggregate paid spend by network.
Snowflake AD_SPEND_DAILY ,
game_id = combo_fighter . Expected: 152
rows, all channel = meta , 4510.33 USD
Blocked, with no override. Read the report, fix the events, re-run. The evals are
deterministic — re-running unchanged returns the same verdict
Proceed
What to do
Verdict
/oe runs at the Oracle Events step, in the web portal. Send your Oracle Events in the chat, with the exact task
prompt, your task details and the injection SQL saved for the attempt, then type /oe and click Start review.
9 · The /oe check
Worked conversion
Oracle Event
It is not “actions become Outcome, reads become Process.” It is Outcome first, Process only when no
Outcome can verify the requirement — and that requirement can attach to any event in your set, write or
scores each defect.
/oe does not issue NON-FAIL. It either passes or it blocks. The severities in section 10 are how the QC register
10 · The defects /oe flags most
A service, ID, filter or expected value that the universe
contradicts
Non-fail
Inaccurate solution path
A required write is missing, or a fact appears with no
event retrieving it
Non-fail
What it looks like
Severity
Incomplete solution path
Defect
If you injected a forced error or an async wait, the recovery or wait path appears as an explicit event.
Every required write the prompt asks for appears somewhere in the set.
Reading the set straight through produces a trajectory that would actually work.
Original Conference · Oracle Events · Spec V2 · Updated Oct 19, 2026
Every parameter, ID and figure has been checked against the explorer.
Every event names its service and its expected data.
No event describes what the final response should say.
Every event describes an observable action or discovery.
You wrote every event yourself. Nothing was generated or pasted.
An imprecise date range or a rounded figure that does
not change the path
Non-fail
11 · Before you leave the Oracle Events step
/oe returned PASS.
An event describing what the answer should say
Moderate
Final-response content
What it looks like
Minor inaccuracies
“does not give up”, “does not stall”
Moderate
Non-actions
Severity
Defect
