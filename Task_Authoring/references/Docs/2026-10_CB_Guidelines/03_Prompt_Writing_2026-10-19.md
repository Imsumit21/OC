<!-- Source: CB guideline PDF (watermarked copy) (Archive 6.zip, received 2026-11-01). Text extracted with pdftotext; watermark lines removed; two-column pages may interleave. -->

Prompt Writing Guideline
HarmonyGames · Universe date: October 1, 2025 or February 14, 2026, 00:00 UTC · Updated October 19, 2026
Change log
How to write a prompt that is hard because the universe is hard — and that reads like a colleague typed it,
because under Spec V2 you have to type it yourself.
Rewritten for Spec V2. LLM-written prompts prohibited; AI-text detection section added. Baseline
model updated to Opus 5.5. Hinting and golden-solution references removed. Tool-call minimum rule
updated. Super-Long-Horizon marked paused. Examples rebuilt on the ML-selected task.
Role, Universe date and Difficulty mode added to the assignment. Second universe date: October 1,
2025. Tiers show human effort; shares now 15% and 85%. Naturalness updated: clean spelling passes;
spec language, trap hints and answer-key clauses are contrived. Unique ground truth fails only when the
rubric picks one reading.
Updates
01 · What a task looks like
Original release.
A task is a short, informal message from one member of staff to an assistant, dropped into a universe that has been
prepared so the message is hard to act on.
<- investigation
[a constraint, a deadline, or who to tell]
<- action, across 2+ services
[then do something about it]
[work out what actually happened]
[something is visibly wrong, said the way a colleague would say it]
Difficulty has to come from the environment, never from a vague prompt. A task that is hard because the
information is scattered and some of it is stale is exactly right. A task that is hard because nobody can tell
what was asked fails Unique Ground Truth and is rejected. A constraint-heavy riddle that points at the trap is
contrived, not hard. A hidden cause is good difficulty only when the prompt does not hint at it.
THE ONE RULE THAT GOVERNS EVERYTHING ELSE
02 · Your assignment
Eight axes are fixed for you. Your scenario has to fit all eight.
Fail if the prompt could not
plausibly come from someone in
that role
The persona's job title
Fail if the prompt could not
plausibly come from that person
Who is asking, and what the agent may read
Non-fail if ambiguous between
yours and another
2.1 Assigned persona — follow it exactly
Fail if the average weighted
rubric score lands above your
mode's ceiling
How hard the task must be
Fail if the task is built on the
other universe date
Fail if the real tool-call count
lands under your tier
The date the universe is frozen at
Difficulty mode
How large the task must be
Universe date
Non-fail if only marginally
exercised
What the agent must be good at
Task skill
The type of work
Competency
Task type
Non-fail if ambiguous between
yours and another
The part of the company the work belongs to
Mismatch severity
Business function
What it fixes
Persona
You may not switch personas, and you may not build around a persona's limitations by pretending they do not
apply. The persona sets the voice, the remit and the read scope. The Persona ACL Policy guideline covers the read
scope in full.
2.2 Assigned competency — the work, not the job title
The competency drives what kind of work the task is. It does not have to be the obvious match for your persona. A
Game Engineer assigned the Finance competency writes a budgeting or forecasting task, because a Game Engineer
can plausibly be pulled into one. Mentioning a budget figure inside an engineering task does not make it a Finance
2.3 Assigned task skill — one is mandatory, stacking is optional
The assigned skill has to be genuinely exercised, not nodded at. Stacking a second is encouraged and is how most
strong tasks end up structured — the ML-selected example stacks Analysis and Synthesis with Retrieval and Actions.
Paused — still visible on the task
screen, but not assigned
Super-Long-Horizon
Long-Horizon
Under ~8 hours
Normal
Share of the project
Human effort
Tool calls
2.4 Assigned task type — how big the task is
HOW THE MINIMUM IS COUNTED [CHANGED 09/26]
If any of your six rollouts scored 100% on your rubric, that rollout is a golden run and the tool-call minimum
applies to it alone. If none did, the minimum applies to the average across all six. A golden run is a run the
model produced, not a document you write — the Oracle Events set does not enter this calculation.
Padding does not help. Blocked calls and repeated calls add nothing to real depth, and an inflated count is a
failing error in its own right.
Rule zero — seed the context, don't type it in
03 · Inject the context into the universe
“Hi, can you help me do…” followed by every requirement spelled out, exact ticket IDs, exact document titles,
and numbered steps.
✓ Put the detail in a Slack channel, then say “check #channel and follow what's there”. Name the problem, not the
method. “that revenue thing”, “the bug people keep complaining about”.
Everything about how the universe should be prepared — the six consistency rules, the clock, what makes seeded
data read as real — is in the Universe and Tools guideline. Two points bear repeating here because they are
prompt-side failures, not universe-side ones:
Seed the symptom, never the conclusion. A prompt that states the root cause is pre-solved, which is a failing
error. There is nothing left to diagnose.
Every rubric has to trace back to the prompt. If you seeded a requirement into the universe and the prompt
gives the agent no reason to go looking for it, the resulting criterion is unauthorized.
LLM USE IS PROHIBITED
4.1 Write it yourself V2
04 · Writing the prompt
Prompts must be written by you, from scratch. Using an LLM to draft the prompt is prohibited, and so is using
one to polish it. The web portal may be used to query the universe; it may not be used to write your
prompt. An AI-text detector runs on your prompt before anything else in the pipeline.
What to do instead
Spec, audit or compliance language: “find the
governing control … complete the decision record”
Say it the way a colleague would: what looks wrong and what
you need done
Leave the hidden cause hidden. Do not point at the trap
A constraint-heavy riddle or trap hint: “the thing
that actually bites us is not on anybody’s list”
Write normally. Clean, correctly spelled writing passes
Staged typos, broken spacing, or emoji that do not
exist in the workspace
State the work. Leave the grading to the rubric
An answer-key clause: “if two places have different
amounts, put both”
A hidden destination: “the same place the rest of
these calls have been going”
Each can be fine once. Vary the setup from task to task
The same framing in every task: “actually”, “don’t
trust the summary”, “go by the rules in the doc”, the
shutdown backdrop
Name where the output goes when the person would know it
Plain prose with no structure at all
Markdown — headings, bold, bullets, horizontal
What to do instead
Red flag
Let sentences run on and double back — “oh and also”
Neatly enumerated steps 1, 2, 3
Be vague exactly where a real person would be vague
“whatever julia was talking about”
Perfect ticket IDs and document titles
Unnaturally complete — nothing left unsaid
“can you check on the launch stuff”
Formal phrasing: “Please ensure”, “Kindly proceed
EXACT TITLES AND VALUES
Red flag
An LLM-sounding prompt is the single most common reason a prompt is rejected. Think about how you actually
type when you are messaging an assistant in your own life. You type what you need and hit enter. Clean, correctly
spelled writing is fine.
Referencing an exact title or value is fine when it is already human-readable — GEOGAMES_SPEC.docx or
*ea96 . It is not fine when it is not, like geogames_spec_23mf2ldf02lfasdlov23rmf.docx or a full
agent_id lifted from a run. A real person would never type the second kind.
Always
4.2 The hard rules
Name a tool, a parameter, or an MCP server
Require real tool use — if general knowledge answers it,
it is not a task
Span at least two services, ideally three
Pre-solve it by stating the root cause
Include internal IDs a real person would not know
Sound like a real person typing: first person, informal
An actual MCP tool name
Non-fail
Names the server, not the tool
Non-fail
Refers to a system as “the X tool”
Names services the way a colleague would
“have a look in the finance sheet and the email
thread”
“use the QuickBooks tool to pull the invoice”
On bolt-ons
“check it via the Gmail MCP server”
Severity
“run linear_create_issue for each open item”
What you wrote
Three severities, and they are not the same:
Pose it as a riddle, hint at the trap, add an answer-key
clause, or write it like a spec
Name where the output goes when the person would
know it
On naming tools
Bolt on an unrelated request
Keep every sentence load-bearing
Format it like a document
Ask for investigation and action
Announce an injected failure or an async wait
State dates absolutely, anchored to your universe date.
“Today” is your universe date: Saturday, February 14,
2026 or Wednesday, October 1, 2025, at 00:00
4.3 Implicit requirements
The test is simple: if you can delete a sentence without affecting anything else in the prompt, it should not be
there. An unrelated extra request does not add horizon, it adds a second task.
Implicit requirements are encouraged — things a competent assistant would obviously infer, like checking the data
before filing a bug, or telling the person who asked. Keep them genuinely inferable rather than hidden gotchas. A
requirement nobody could reasonably infer produces an unauthorized rubric criterion, which is a scored defect.
What the agent learns early is overturned by what it
finds later
Seeding
Seeding
The prompt under-specifies by design; the agent
resolves the gaps from the environment
Configuration
Error Recovery
Forced tool failures; the agent retries, works around, or
escalates
Submit-then-wait tools; the agent parks the
dependency and resumes
Async Tool Calls
Seeding
Information split across three or more sources, with
distractors and disagreements
Configuration
Persona + seeding
The agent must work within what its persona may read
Access Control
Multi-Source
Dynamic Change
Ambiguity
How you build it
Definition
Characteristic
05 · Difficulty characteristics to build in
The three you build by seeding
All six are optional and all six stack. A single task can carry one or all of them.
Ambiguity
Over-specified. “The Q1 board deck on Drive has a revenue figure that disagrees with the finance sheet in row
47. Fix the deck and email Frederick.”
Identify the details the agent needs — dates, names, priorities, constraints — remove them from the prompt, and
plant them across Slack threads, email chains, doc comments, tickets and spreadsheet notes. Then add noise:
related-but-irrelevant material nearby, so the agent has to separate signal from it.
✓ Ambiguous. “Frederick mentioned the board deck numbers looked off — can you look into it?” with the real
discrepancy sitting between the Drive deck and the Sheets data.
Dynamic Change
Multi-Source
overturns.
Create an initial state the agent discovers first, then plant a contradicting update it reaches later. Discovery order is
what makes it land. Put the correction where a plausible investigation path meets it second, after the thing it
Spread what is needed across at least three systems, add lookalike distractors — old threads, archived tickets, draft
docs — and introduce a disagreement so the agent has to judge which source is authoritative.
Whether the agent retries
Search becomes submit → check → get,
with a 30–35 second delay per call
Whether the agent parks the
dependency and resumes
Fails that proportion of calls, and is marked
transient
Async wait
Whether the agent finds a workaround
or escalates
Error rate below 1.0
Fails on every call. A retry will never
succeed — a permanent outage
Error rate 1.0
What it tests
Behaviour
Setting
The two you configure
THREE HARD RULES ON INJECTED FRICTION
Your task must still be solvable without any tool you kill. Name the alternative path out loud before you
configure anything, confirm it exists in the universe, and show it in your Oracle Events.
Async affects search only, never fetch. If your prompt names the exact document, channel or ticket, the agent
fetches it directly and never pays the delay. Write the prompt so discovery is unavoidable.
A forced error on a scoped tool is indistinguishable from an ACL denial. If your task depends on the agent
reasoning about why it cannot see something, do not also force an error on that tool.
Search is fuzzy and returns ranked candidates. Fetch by ID is exact and instant.
06 · How agents search
Naming an exact artifact in the prompt collapses discovery to a single fetch. That is usually the opposite of what
you want.
Agents stop early. A message that sounds like a conclusion will end the investigation, even when the thread
continues afterwards. That is a legitimate and effective trap — the ML-selected example is built on one.
Agents will bypass a slow path if a faster one exists. If you configured an async wait, open the trajectory and
confirm the submit → check → get sequence actually appears.
07 · The ambiguity line
✓ Discovery ambiguity. The agent does not know where the answer is, which sources matter, or which of two
sources is authoritative — but every reasonable run still ends in the same final state.
UNIQUE GROUND TRUTH HAS NO MIDDLE BAND
Decision ambiguity. Two readings lead to two different write actions and the rubric accepts only one. Act now
or defer. Escalate to A or to B. File in X or in Y.
If two careful runs land the agent in two different final universe states and the rubric accepts only one of
them, the prompt fails. If the rubric accepts every fair reading, it passes. This dimension scores 1–2 or 5, with
nothing in between.
It states no root cause the agent is supposed to find, and has no riddle, trap hint or answer-key clause.
Every date is absolute. Anything already done sits before your universe date; a deadline may come after it.
It names no tool, no MCP server and no parameter, and it names where the output goes when the person
would know it.
It reads like a person typing, not like a document, a spec or an audit. Clean spelling is fine.
Every sentence is load-bearing — nothing can be deleted without consequence.
/prompt returned PASS or NON-FAIL. A FAIL there is fatal — with hinting removed, nothing downstream
rescues an unsolvable prompt.
Original Conference · Prompt Writing Guideline · Spec V2 · Updated Oct 19, 2026
It requires at least two services, ideally three, and both investigation and action.
It could plausibly have been sent by your assigned persona, about work in your assigned competency.
Every name, ID and figure has been checked against the explorer, not against memory.
Two careful runs would end in the same final state, or the rubric accepts both.
You wrote every word of it yourself, without an LLM drafting or polishing.
08 · Before you submit the prompt
