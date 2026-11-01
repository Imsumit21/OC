<!-- Source: CB guideline PDF (watermarked copy) (Archive 6.zip, received 2026-11-01). Text extracted with pdftotext; watermark lines removed; two-column pages may interleave. -->

Hardness Guide
October 19, 2026
HarmonyGames task revision · Universe date: October 1, 2025 or February 14, 2026, 00:00 UTC · Updated
Sources: CS = task_writer_cheat_sheet.html , cited by card name. HB = handbook.html (identical to
opus_failure_report.html ), cited by section. Anything uncited is local practice.
First release as a PDF. Aim updated to Opus 4.8; targets box and Snowflake and Confluence caution
Aim and targets box updated to Opus 5.5. Average weighted rubric score now capped by Difficulty
mode: Easy 90%, Medium 85%, Hard 70%. Universe date: October 1, 2025 or February 14, 2026.
Updates
Change log
The aim is a task where Opus 5.5 fails for a real weakness, set off by a realistic task, and caught by a rubric row a
careful agent would pass. Build each task on 1–2 traps. Pilot 3–5 tasks with at least 3 runs each, and keep a trap
only if it fails in more than one run for the reason you designed (CS: How to use it). Section 7 turns the misses from
the current runs that scored under 0.80 into patterns a new task can follow.
Baseline model: Opus 5.5, for the pre-check and all six rollouts. Average weighted rubric score at most 90%
(Easy), 85% (Medium) or 70% (Hard), by your Difficulty mode. pass@k at most 67%: no more than four of six
rollouts pass every criterion.
THE TARGETS [CHANGED 10/1 9 ]
SNOWFLAKE AND CONFLUENCE
Confirm Snowflake and Confluence are available for your task before you build any trap below on them.
Shares of root failures come from HB §3. Trends are EA Advanced, Opus 4.6 → 4.8 (CS: Overview).
1 · Where Opus fails
Information seeking 22%. The source holding the answer was never opened. That one pattern is about 1 in 8 of
all root failures. Falling (36→25%), but depth, pagination and scope traps still hold.
Instruction adherence and deliverable form 20%. Opus's own template replaces the dictated string, schema,
negative constraint or audience. Rising (5→7%).
Output fidelity 9%. A retrieved fact is dropped or blurred on the graded surface. Falling (20→15%).
Calibration and honesty 8%. False "no record" claims; invented values to fill slots.
Task completion 7%. Investigates, then skips the write, stops short of the terminal state, or writes to the wrong
target. Rising (14→18%).
Domain and policy rules 5%. Applies the obvious test instead of the stated rule. Rising (1→5%).
Quantitative 4%. Derived figure never computed, or the sum covers the wrong set. Rising.
Source evaluation, temporal, synthesis, judgment: 3% each. Judgment is rising (2→7%).
Default override
Compression loss
Requirement neglect
Premature closure
Leading mechanisms (HB §7):
Mechanism
Tool use, conflict, extraction, verification: 2% each. Long-horizon: 1%.
Execution slip
Effort truncation
Failed tasks average 2.9 root failures. 69% of failed information-seeking criteria are cascades from an earlier miss
(HB At a glance, §3).
"HG" marks traps whose CS example already happened in HarmonyGames.
2 · Trap catalogue (CS capability cards, adapted to this universe)
Constraint for this bundle: Gmail and Slack serve attachment metadata only. Never put a decisive fact in their
attachment bodies.
Information seeking
Decisive mail only in Gmail SENT. Seed the decisive mail (e.g. Leonard's six termination letters) only in SENT,
with an in-universe hint that it was sent. Search defaults to INBOX and has a folder parameter. Targets: a source
never queried. (HG)
Reversal in a thread reply. Let the top-level Slack history read coherently and put the reversal in a later-dated
thread reply. The task rule says "status from most recent record". Targets: search stops at the first hit. (HG
BoomBit)
Population no filter matches. Define the population by a business rule ("every 2025 publisher conversation")
that no single Trello label, Linear team or Snowflake item_id filter covers. Put the biggest item outside the
convenient slice. Targets: proxy-filter under-scoping.
Value only in an unnamed service. Put one needed value only in a service the prompt doesn't name but that is
on the tool list (Snowflake, a Sheets tab). The prompt gives a reason to look ("anything added since"). Targets: a
source never queried.
Domain and policy rules
Decoys under the same tag. Put QA/test grants in the same Snowflake item_id as real ones, with the
exclusion on a Confluence page. Grade the headline total, not a footnote. (HG ENG-2275: 630,000, not 671,000)
Approval only in a message. The approved treatment lives in a Slack or Gmail reply; the Linear or Trello record
is unchanged. A tidy alternative story is available.
Operands without the result. Every operand sits in records Opus must read (Snowflake spend and installs, a
Sheets budget), but no derived figure is stored. A status flag offers an easier verdict. Targets: derivable figure left
uncomputed.
Quantitative
Tempting field that isn't the test. Expose a field like a Trello "Done" label or Linear priority, while the real test
sits in a Confluence checklist. One item passes the field and fails the rule.
Population spans two statuses. "In Review" is still open. The prompt says "every open X / full exposure".
Paginate past one page and show the total ( total=80, returned=50 ).
Conflict and anomaly
Doc subtotal vs warehouse total. The doc's figure is a subtotal of the warehouse total (GDD builds cover 401 of
901 Snowflake installs). Targets: two figures never compared. (HG)
Three explanations, none settleable. Seed three plausible explanations (Slack, a Linear comment, a Confluence
postmortem) that the data can't decide between. Grade naming the conflict. Targets: collapsed into one cause.
Source evaluation and currency
Undated stale note vs dated merge. An undated Linear description ("not yet pushed") is superseded by a dated
GitHub merge whose title undersells it. Ask for the corrected state written back. (HG ENG-2441 / PR #37)
Tidy summary vs ledger. A pre-labelled Sheets summary diverges from the Snowflake ledger by design, and the
primary source is slightly harder to read.
Verification
Confirmation only by exact id. Keyword searches return empty; a search by the exact ticket or PR id returns the
confirming record. Add skeptical user framing. Targets: an empty result taken as absence.
Scoped query returns the org-wide set. A second system holds the much smaller correct count. Targets:
unchecked load-bearing figure.
Synthesis and entity tracking
Container named for one entity. A game's Slack channel or Drive folder is named after one entity but its
contents mix entities. The key exists only on line items.
Answer in structured fields. The answer sits in due_date , assignee_id or state of a list result Opus maps
by title only.
Related work scattered across lists. Related work sits in different Trello lists with no shared label; the link is in
checklist names. (HG cards #8/#11/#12/#15/#23)
Tool-use mechanics
Unreadable obvious copy. The obvious copy (a Drive .docx) is redacted or unparsable; the authoritative copy is
in Gmail SENT. (HG)
Display id returns "not found". get-by-id fails on the display id (Linear ENG-2441 ) while list/search returns the
record.
Defining clause in a 50K+ char doc. Put it in a Confluence or Drive doc, outside any greppable phrase. (HG seed
Decisive value on a second, short Sheets tab. A long first tab states a conflicting value.
Faithful extraction
Summary endpoint omits the decisive field. E.g. a GitHub PR list without the body; the detail endpoint must
hold what the summary lacks.
Temporal
Near-identical checklists. 10–20 Trello cards whose checklists differ by one word, with a per-card "outstanding"
note required.
Item on the period's last day. One item falls on the last day of the period, the tool's end bound is exclusive, and
the prompt or spec says "inclusive".
Freshest-looking source predates a dated change. E.g. GDD dated Feb 9, ads switched on Feb 12. State the
user's present explicitly; the February universe is dead after Feb 11, 2026.
Instruction adherence and deliverable form
Channel roster contradicts the audience limit. The named delivery channel's members break the audience
limit, and the roster is one call away. (HG admin_foundersonly has 7 members)
Labelled slot per item, often honestly "none". Several items' correct value is "none".
Literal schema and exact row count. Dictate a literal Sheets schema, "exactly N rows", and one money/date
notation across all sibling outputs.
Judgment and disposition
Owner acts next, not the visible name. E.g. the approver rather than prepared_by .
Sweeping narrative vs per-item records. A sweeping later-dated narrative (sunset, hand-off) is contradicted by
a few items' own records. Grade those items one row each. (HG 40-card register)
Task completion
User's own tiering test. Give the user's tiering test plus one finding that passes it but looks minor. Grade the
obligation tied to the tier, e.g. that a Linear ticket exists.
Outcome wording, state/field write required. The prompt states the outcome ("get it reflected in Linear"),
which needs a state or field change. A comment is the tempting look-alike. (HG ENG-2438)
No-action items in the batch. The prompt says "note every item you review, including exclusions".
Second recipient in reference data only. The second recipient appears only in reference data (a Sheets vendor
list or Confluence contacts). One explicit recipient gives an easy stopping point.
Attractive wrong Trello list. A semantically attractive wrong list sits beside the named one; the right one is
resolvable from an id already retrieved.
One finding mirrored on three surfaces. Email, channel and Linear description, each with all IDs and amounts.
Figures inline as well as in the doc. Figures are required inline in the email or Slack post while a Drive doc also
carries them.
Output fidelity
Calibration and honesty
Tool-confirmed negatives must be stated. E.g. "no Linear team, no Trello board". (HG)
Column the records leave blank. E.g. "market, where recorded", with a tempting fill nearby.
Indirect data vs explicit human statement. Indirect Snowflake rows (test-track Android installs) vs one explicit
statement ("No android for now"). (HG)
Long-horizon state
"Could not verify" section. A conclusion depends on a link Opus will probably skip.
Tracker state change as a separate final write. It comes after a long session, on a tracker already Done. (HG
ART-743, about 170 calls)
A misapplied cohort shows up again as a wrong total
Facts that must all reach the deliverable and be joined
What it looks like
Strict output instructions given early in a long task
Deliverable form + long-horizon
Output fidelity + synthesis
Traps that fail together more often than chance (CS: Stacking traps; HB §5):
Rule + number
3 · Stacking and row independence
Skipped: multimodal. It is 0% of EA failures (CS: Multimodal).
"Systems checked" log covers empty sources. It must list every named source, including ones that legitimately
return nothing.
Don't stack: information seeking with source evaluation (0.68), temporal (0.63) or deliverable form (0.77). If the
source is never opened, the second trap is masked (HB §5).
Keeping rows independent:
Give each trap its own fact. "If five criteria depend on the same hidden fact, the task measures one weakness
five times" (CS: Fairness checklist).
Cap information-seeking traps. Grade the hidden fact on at most two surfaces.
Grade retrieved inputs and computed results as separate rows (CS: Quantitative).
✅ " with the write absent
Grade record state, the tool call or the artifact, never narration. Opus says "LOCKED
(CS: Task completion). Never grade hidden reasoning (CS: Conflict).
4 · Rubric rules
Exception for surface carry. When the trap is carrying a fact to every surface, one row per surface is correct (CS:
Output fidelity).
Name the surface and the exact value, with full identifiers. Then "the Mueller account" or "30+" fails (CS:
Output fidelity).
Name the predictable wrong figure. "630,000, not 671,000" (CS: Domain; Information seeking).
Split each action into two rows. One for existence on the exact target ( idList = BD Follow Up; state = Todo),
one for content (CS: Task completion).
Pair positive and fail-if rows. For empty-lookup traps, add a row that fails any false absence claim (CS:
Calibration; Verification).
Write ordering as an observable call sequence. "Log write occurs before the first Drive doc write" (CS: Longhorizon).
Accept either honest provenance. A recorded query result or an explicit "not queried". Fail only claims the
trajectory doesn't support (CS: Long-horizon).
Conflict rows require both sources named, and pass whether or not a side is picked (CS: Conflict).
Grade enumerations as the exact set and counts as "exactly N rows" (CS: Output fidelity; Instruction
adherence).
Word rows so hedges fail. "States ENG-2438 will not ship" is not met by "fix, accept or hold" (CS: Judgment).
Close to verbatim from CS: Fairness checklist:
5 · Fairness checklist
1. Evidence is reachable. Everything the answer needs exists and can be found with the task's tools. Try it yourself
with the same tools.
2. Nothing is hidden. Anything the rubric checks is asked for in the prompt or follows unavoidably from it.
3. There is one defensible answer. If two readings are reasonable, rule one out in the prompt or accept both.
5. One miss fails one criterion.
4. Each criterion checks one thing in a requested output, with the exact value or action.
6. Seed data is consistent, except where the inconsistency is the point, and then the rubric rewards noticing it.
7. No unstated conventions (formatting, etiquette) unless the prompt or a spec asks for them.
8. It fails for the designed reason. Run several times, keep only if it fails in more than one run, and read the
transcript.
Card-level checks:
Hidden depth must be tool-reachable: a folder parameter, an offset, a replies call (CS: Information seeking).
A broken authority needs another working route, and "unconfirmed, flagged" must be accepted (CS: Source
evaluation).
State the evidentiary standard in the prompt. "Only what we can back up" (CS: Calibration).
The governing rule must be retrievable and cued by the prompt (CS: Domain).
Scope words are explicit, and the later record is dated clearly after the earlier one (CS: Information seeking).
"Not found" means out of scope, not nonexistent (CS: Tool-use).
6 · Tool-call scale
No trap warnings in the prompt. The cue lives in the universe (CS: Information seeking, trap 1).
Target 50–100 necessary calls for a normal task and 100+ for a long-horizon one, through real scope. Test for every
expected call: skipping it would change a graded value.
Legitimate ways to add scope:
More entities, each verified in 2+ services. E.g. 12 Trello cards, each checked against Linear state, its GitHub PR
and the Slack thread tail. Each cross-check is a natural trap slot.
Per-item writes, including notes on no-action items (CS: Task completion).
Decisive replies inside 5+-reply threads.
A source the user calls complete that isn't. "The Trello board has everything", while 3 items live only in Slack or
Gmail. The prompt's scope rule must define the population independently of that source (HB §4.1 Lessons).
Collections that need paging. Slack, Snowflake or Linear sized past one page, with a visible total and in-scope
items past the cut (CS: Information seeking, trap 2).
Never use filler: no duplicate reads, no irrelevant services, no errors without a fallback. No summary doc that
answers everything either; remove it or make it demonstrably stale.
Estimating the call count from the oracle events. For each write event, list the reads that justify its content, then:
N ≈ discovery (list channels/projects/boards/tables, ~5-10)
+ sum over entities and services of reads (1-3 each: search, open, replies)
+ sum over collections of ceil(population / page_size)
+ oracle write events
+ read-backs confirming terminal states
Validate the estimate:
Worked example: 15 entities × 2.5 services × 1.6 reads ≈ 60, plus 8 pages, 15 writes, 6 discovery calls and 4 readbacks, gives about 93. Scale to 25+ entities across 3 services for long-horizon.
Run the reference agent 3 times and take the median number of distinct calls.
Close shortcuts. If passing runs use far fewer calls than N, a shortcut exists.
End long tasks with a graded final reply plus a separate state-change row. Late instructions do get dropped:
A summary instruction executed 37–45 calls later was lost (HB §4.5).
Opus 5 slipped on a final state write after about 170 calls (CS: Long-horizon, trap 5).
7 · Patterns that still fail
Taken from the current L11 and L12 runs that scored under 0.80. The model finishes most of the task. These are the
last steps it drops, written so a new task can plant the same shape. Use one or two per task. Give each its own fact.
Derived figure, required on every surface. Put every operand in records the task already has to open, and store no
total. Ask for the figure in the working sheet and again in the message or page that reports it. Grade each surface on
its own, and name the predictable wrong total (the subset, the labeled feed, the first number someone stated). One
correct surface does not carry the other.
Allocation, not a round sum. A payment, a pack, or a count is the sum of named parts, and no row stores the split.
Grade the parts and the total as separate rows. A reply that states only the round total fails.
Stale record overwritten. Leave the old claim in the document, draft, or ticket the user will ship. Put the correction
in a later dated message, merge, or ledger, with a title that undersells it. Grade the field or the sent text after the
write. A correct chat reply with the old field left in place fails.
Tempting status loses to the stated rule. Seed a coherent wrong story on the obvious field: Done, a shipped build,
"send it as-is," "signed off on my end," or "chase these." Put the real test in a rule the prompt names (a checklist, a
freeze, a register, a later addendum). One item passes the field and fails the rule. Grade the disposition that rule
requires, worded so a hedge fails.
Exclusion moves the headline. Put the decoys in the same tag, channel, or roster as the real items. State the
exclusion where a search will find it. Grade the headline total and the reason for the exclusion. A footnote that
mentions the decoys while leaving them in the total fails.
Code or ledger against the claim. A chat message states the flattering status ("already built," "the only unfinished
piece," "live on both stores"). The repository, the event log, or the warehouse says otherwise. Grade the
contradicted claim, and grade the empty or negative finding ("no such code," "no team, no board").
Exact set. The deliverable is a named collection: every channel, every enemy, every open item. Order and page it so
the convenient slice is short of the set. Grade the exact set and the exact count. A near list fails.
Next actor, and the send that is not allowed yet. The decision belongs to the person who must act, who is not the
name on the record. A second action, an external email or a vendor send, waits on that person's review. Grade the
message to the actor, and grade the absence of the premature send.
Later evidence written onto the existing record. The repro, the still-open card, or the corrected scope lives in a mail
thread, a board list, or a build note. The ticket the user will read is unchanged. Grade a comment or a field write on
that ticket that carries the later fact. A summary that never touches the ticket fails.
Gap plus the follow-up it creates. A real absence (a lapsed policy, a missing entity, a fee still owed, a renewal ahead)
has to be stated, and it creates one small write: a named owner, a calendar reminder, or a ticket. Grade the absence
and the write separately.
Original Conference · Hardness Guide · Spec V2 · Updated Oct 19, 2026
Do not multiply one fact. Grade a hidden or derived fact on at most two surfaces. A long register of the same miss
fails many rows and still posts a high mean, so the task looks finished.
