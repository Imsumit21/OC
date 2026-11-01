<!-- Source: CB guideline PDF (watermarked copy) (Archive 6.zip, received 2026-11-01). Text extracted with pdftotext; watermark lines removed; two-column pages may interleave. -->

Universe and Tools
HarmonyGames · Universe date: October 1, 2025 or February 14, 2026, 00:00 UTC · Updated October 19, 2026
Change log
What the simulated company is, which thirteen services it runs on, how the clock works, and what “deep
enough” means before you start building.
Rewritten for Spec V2. Confluence and Snowflake confirmed in scope and flagged for regeneration.
Baseline model updated to Opus 5.5. Taxonomy screenshots removed. Golden-solution and hint
references removed throughout.
Second universe date added: October 1, 2025. Date rules now point to your universe date.
1 · The company
Original release.
Updates
A fighting game, most recently launched
19, across product, engineering, design, data, marketing, finance and operations
October 1, 2025 (a Wednesday) or February 14, 2026 (a Saturday), 00:00 UTC
Universe date
13 connected systems
Services
A zombie match-3, still finding its audience
Staff personas
A domino-matcher, the studio's established revenue source
Flagship title
Third title
Detail
Newer title
HarmonyGames is a founder-led mobile game studio. It is small enough that one person's Slack DMs matter and
large enough that nobody has the whole picture. That combination is what makes it useful as an evaluation
universe: the information an agent needs genuinely exists, and it is genuinely scattered.
External correspondence, publishers, investors,
vendors
The outside view, which frequently
disagrees with the inside one
The richest source of evidence and of
distractors. Most tasks start here
Channels, DMs, the running commentary on
everything
Shared files and folder structure
Both a source and a destination — most
tasks end in a ticket
Policies, conventions and process
documents an agent should apply
Team wiki and knowledge base
Product-side planning, often out of date
relative to Linear
Roadmap, feature and prototype boards
Data warehouse, analytics tables
The only place many figures can be
derived rather than read
UNIVERSE WORK IN FLIGHT
Snowflake
The ground truth about what actually
shipped and when
Engineering tickets, bugs, projects, cycles
Confluence
Resolving “tell whoever owns it” into a
real recipient
Code, pull requests, reviews, release history
Trello
Ordering evidence, and a natural place
for a deadline to live
People lookup, email addresses, roles
Contacts
Meetings, availability, scheduling
Summarised figures that go stale the
moment the data moves
Numbers that must reconcile against
Snowflake and against each other
Pitch decks, quarterly reviews, reports
Google Calendar
Linear
Tracking sheets, budgets, financial records
Google Slides
Long-form statements of intent that the
data can contradict
Design docs, specs, legal documents, postmortems
What it is good for
Google Docs
What lives there
Where a written deliverable is expected
to land
Service
Google Sheets
Google Drive
GitHub
What it is good for
What lives there
Service
2 · The thirteen services
Engineering is regenerating the synthetic Confluence and Snowflake data so it matches the real Drive and Excel
data, and is clearing personal information out of the artifacts. Both services remain fully in scope for a task. If
you recorded a Confluence page or a Snowflake row count before the refresh lands, re-verify it afterwards —
values may move, and a rubric asserting a stale figure becomes an incorrect criterion.
3 · The clock
Why it matters
Write dates absolutely
The universe is frozen at your universe date: October 1, 2025, 00:00 UTC or February 14, 2026, 00:00 UTC.
Everything before that instant is the past. Nothing after it has happened.
“February 20, 2026”, never “next week” or “by Friday”. Relative dates break
on replay and are scored as errors
A prompt or a seeded record that treats something after your universe date
as already done describes something that has not happened. A deadline may
come after it. Failing error
Created before updated
Nothing may post-date the clock
A record whose created_at is later than its updated_at , or a comment
that predates its parent, is a temporal field inconsistency
Business messages at three in the morning, or a weekday standup landing on
a Sunday, read as synthetic
Working hours are real hours
4 · What the agent can and cannot see
Check the weekday before you seed anything recurring
October 1 is a Wednesday; February
14 is a Saturday
list , search and by-ID reads all
filter. A denied read returns “not found”
Gmail · Slack · Google Calendar · Drive
· Docs · Sheets · Slides
Neither column names them. Open each
one from the persona's view and
confirm the record is readable before
you depend on it
Confluence · Snowflake
Not classified
Every persona sees the same records
GitHub · Trello · Linear · Contacts
Scoped — persona-filtered
Behaviour
Unscoped — shared
Services
Your assigned persona controls what the agent is allowed to read. Four services are shared by everyone; the rest are
filtered.
TWO RULES THAT CATCH PEOPLE OUT
Writes are never governed by ACL. Determine what your persona can write from the tool catalog, never from
what it can read.
Universe Explorer is author god-mode. It shows you everything. The agent and the verifier both use the
persona's scoped view. Never build a task on, or grade against, evidence only you can see.
The full policy, including the failure signatures of each ACL mistake, is in the Persona ACL Policy guideline.
Three or more services is the working target. Two is the floor, and only when the second one carries real weight.
6 · Making the universe carry the difficulty
You add depth by seeding data — adding or editing universe records so that the work lives in what the agent has to
discover, not in how the prompt is worded.
Call it data seeding or injection. “SQL injection” means a security vulnerability and is not what this is.
The prompt states the root cause, leaving the agent nothing to diagnose. Failing
Not pre-solved
“Investigate something and send one email” is not a task. Before you write a prompt, check it against all four of
TERMINOLOGY
A pure lookup, or a pure write with nothing to work out first
Investigation and action
One service resolves the whole thing, or a second is touched only trivially. Failing
Genuinely cross-service
A question general knowledge can answer without touching the universe
Real tool use
What fails it
Requirement
5 · The depth bar
Anything referenced somewhere exists
where it is referenced
Cross-service referential inconsistency
— a Slack thread about a PR that is not
in GitHub
Temporal field inconsistency
Pre-solved prompt, or AI-flavoured
boilerplate in the seeded text
Seed the symptom and the evidence,
never the conclusion
Unsolvable task, or evidence nobody
can find
Your persona can read it, and a realistic
search path reaches it
Natural, not pre-solving
Reachable and findable
Identifier inconsistency — an ID that
breaks the ENG-#### or ZOM-###
pattern
No invented fields; IDs follow the existing
format
State and lifecycle
Quantitative reconciliation inconsistency
— a doc saying $65 against a sheet
saying $35
Structurally valid
Figures reconcile with the records they are
derived from
Coherent with the universe
Every date sits before your universe date,
and created never post-dates updated
Consistent across services
On the clock
Failure signature if you break it
What it means
The six consistency rules
Two further defects are easy to miss because nothing about them looks wrong in isolation.
State inconsistency. A ticket marked Closed whose linked pull request was never merged; a task marked Done
with an open blocker still attached.
Semantic inconsistency. The same programme described under two different names in two services, with
nothing connecting them. This one is sometimes deliberate — if you intend the agent to reconcile the two
names, say so in your Oracle Events. If you did not intend it, it is a defect.
7 · Your injection SQL is the record
The SQL you submit is the only record of what you changed. A reviewer re-injects it into a fresh environment when
a re-run is needed.
If it does not reproduce your universe exactly, your task cannot be re-run at all, and it will be returned.
Every statement must be valid against the real schema. Invented columns fail.
Keep the changelog entry aligned with the SQL — a changelog describing an edit the SQL does not make is its
own defect.
Run /injection in the web portal immediately after you write it. It checks structure, references, IDs, dates
and coherence, and catches most of the above before it costs you a cycle.
8 · Tool behaviour worth knowing before you build
Consequence for your design
If your prompt names the exact document or thread, the agent fetches it directly
and skips discovery entirely
Search is fuzzy; fetch is exact
Behaviour
Async waits affect search only
The matching fetch stays instant. An async wait only bites when discovery is
genuinely required
On a scoped service the agent cannot tell them apart. Do not force an error on a
tool whose denial the agent is meant to reason about
Snowflake answers must be
derived
A forced error looks like an ACL
denial
Figures there usually need a query and an aggregation, which is exactly why
Snowflake criteria tend to carry high weights
They add nothing to real depth, and an inflated tool-call count is a failing error in
its own right
Blocked and repeated calls still
9 · Before you leave the universe step
Every cross-reference resolves to a record that actually exists.
Every date in every seeded record sits before your universe date.
At least three services carry real weight.
Your persona can read every piece of evidence the task depends on — confirmed from the persona's view, not
from Universe Explorer.
Every ID follows the existing format for its service.
Every figure reconciles with the record it is derived from, unless the disagreement is the point of the task.
/injection returned PASS.
Nothing you seeded states the conclusion the agent is supposed to reach.
Original Conference · Universe and Tools · Spec V2 · Updated Oct 19, 2026
