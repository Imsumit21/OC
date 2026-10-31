# Prompt and Rubric Common Errors

HarmonyGames · Source: `Docs/Prompt_Rubric_Common_Errors.html` (October 4, 2026),
from 340 prompt reviews and 343 rubric reviews. 104 prompts failed. 130 rubrics
failed. A score of 1 or 2 fails that requirement, and the attempt takes the
lowest score.

The deep recheck passes at the end of `/prompt` and `/rubric` fill this
checklist. See [Review procedure](#review-procedure).

Eval 1 and Eval 3 adopt this checklist. These points stay stricter in the evals
than in the source page, and this copy follows the evals:

- A competency or task-skill mismatch fails (Eval 1 §1.5), not a 3.
- A prompt that treats an event after the clock as already done fails (Eval 1 §2.8), not a 3.
- One loose factual slip fails Truthfulness, and spec-like or polished voice fails Contrived (Eval 1, 2026-10-05), not a 3.
- A title that starts "The Agent's …" is nonstandard: a 3 on Agent-Centric Phrasing when such titles are 10% or fewer of the rows, a fail above that (Eval 3 Local Overrides).
- Rubric quality, weights, process and agent-centric phrasing keep only the narrow non-fail bands in the Eval 3 Local Overrides (rubric-flow-v2, 2026-10-09), which are stricter than the QC form. Those bands decide; this copy does not add any.

The SQL working-hours check from the source page is not adopted.

## 1 · How to read this

Do the blanks in order. An empty blank is an open fail.

**The test.** Write Reading A and Reading B. If the decision, the writes, the
destination, or the contents differ, quote the sentence or the record that kills
one of them. If you cannot quote it, the task fails. The sections after the form
are only for a blank that will not fill.

## 2 · Kill the other reading

Write the outcome the prompt wants, then the best other outcome a careful person
could still defend. This blank is most of the prompt fails.

| | Reading A, the one the prompt wants | Reading B, the best other one |
|---|---|---|
| Decision | | |
| Writes | | |
| Destination | | |
| Contents | | |
| Quote | | |

The quote has to be a prompt sentence or a record this person can open. “B is
less likely” is not a quote.

While you write B, each of these must come out as one answer. If two answers
fit, the prompt needs the choosing sentence, unless only one reported figure
differs and both values are on records (Eval 1, both-fair figure).

- Which items are in the set, and which are out.
- Which number, if two amounts or dates exist.
- Which source wins, if two records disagree.
- What counts as the event. A deck, a Done ticket, or a draft does not, unless the prompt says it does.
- What gets written. “Or” cannot mean both close it and only comment.

## 3 · Five lines

| Line | Fill this |
|---|---|
| Two services | ________ and ________. Each one changes a graded fact. Dropping either one changes the answer. |
| Named cause | ________. If the prompt states one, it fails. The prompt keeps the symptom. |
| Tight claims | Channel, ticket, vendor, amount, date, or fiscal period, and the record that matches each. Write “none stated” if the prompt names none. |
| Hidden record | A record the answer needs that this person cannot open. Write “none”, or the prompt must say that record is missing. |
| Search hits | `linear_`, `gmail_`, `slack_`, `MCP`, `tool`, `First`, `Then`, `Finally`. A hit fails. “Check Slack” and “the Linear ticket” can stay. |

A sentence that can be deleted without changing the rest of the task is a
bolt-on. Nothing the prompt treats as already done sits after the task clock
(2026-02-14 00:00 UTC, or 2025-10-01 00:00 PT on an Oct 1 task).

SQL, or “no SQL”: ids do not collide, columns exist, the author of an added
message is a member of its channel, and apostrophes inside quoted strings are
doubled (`don''t`).

## 4 · One line per outcome

List every outcome the prompt requires, including exclusions (“only these rows”,
“leave it open”).

`R# | the title | wrong answer that fails this title | another allowed answer that still passes | record`

- No row for an outcome: a row is missing on the artifact the prompt named.
- The wrong answer still passes: the row is too wide. It must name the value.
- The other allowed answer fails: the row is too narrow. An added channel, heading, or cause must come out.
- The title says “that message”, “the above”, or “the correct figure”: the real value belongs in the title.
- Two writes, two services, or a verdict plus its reason share a line: split them.
- The record cell is an inference: the row is wrong. It must point at the message or the cell.

## 5 · Three searches on the rubric

- `does not`, `must not`, `never`, `without`, `avoid`, `fails to`. A hit is rewritten as a condition on a write the Agent must make (an exact count or scope), or a requirement inside a required artifact. Never a standalone row an agent passes by doing nothing (“leaves ENG-123 open”, “leaves the sheet as found”). “Reports that PR 438 had no review” can stay.
- `such as`, `e.g.`, `for example`. Each hit is a Moderate issue, once per row, including inside a quoted record name.
- Titles that do not start with “The Agent”. No catalog tool name in a title.

A lookup is weight 1, a comparison is 3, a join across sources is 5. If one
mistake fails two rows, one of them goes. A repeated list keeps at most five
sample rows plus one count row. No row should fail every careful run because
the value is not in the records.

### Filled once, so you can see the size

The UA-board prompt failed at the quote in section 2. Reading A relabels only
Not Started cards. Reading B relabels the whole list, because “honest again”
plus the admin note also catches In Progress.

- BAD: “work out which of the not started ones are actually done and fix their labels the way i laid out in admin when i turned trello back on, so the board is honest again”
  - “Not started” is one set. “Honest again” plus the admin note can mean the whole list, including In Progress cards. The quote box was empty.
- GOOD: “Leave In Progress and At Risk cards as they are.”
  - One sentence makes Reading B impossible. The rule in the admin note still has to be found.

## 6 · Prompt patterns

Use a pattern only when the matching blank will not fill. A 2 fails the task.
Business function bottoms out at 3: it does not fail the node, and it does block
a 5.

| Check | Fails that name it | What a 2 means |
|---|---|---|
| Unique ground truth | 66 of 104 | Two concrete outcomes both fit |
| Clarity | 46 of 104 | Two readings change what gets written |
| Cross-service | about 40 of 104 | The answer sits in one service, or a second service changes no graded fact |
| Truthfulness | 11 of 104 | A tight id, amount, date, or fiscal period is wrong |
| Feasibility | 9 of 104 | This person cannot do an explicit request |
| Naturalness | 8 of 104 | It reads as a spec or a step list |
| Data missing | 4 of 104 | A needed fact is not in the records |
| Persona access | 3 of 104 | A required record is hidden from this person |
| Investigation | 1 of 104 | The prompt already states the cause |

These also fail at 2 when they hit: a catalog tool name, a bolt-on sentence, a
Snowflake or Confluence contradiction, and injection SQL that breaks an id, a
date, or a link.

### 6.1 Unique ground truth

Section 2. Wording can differ. The decision, the writes, the destination, and
the contents have to be the same. A later record can pick one side. The more
likely reading does not win by itself.

- BAD: “work out which of the not started ones are actually done and fix their labels the way i laid out in admin when i turned trello back on, so the board is honest again”
  - “Not started” is one set. “Honest again” plus the admin note can mean the whole list, including In Progress cards.
- GOOD: “On the zombie match launch list, fix the cards that still say Not Started when the work was already done. Use the rule I posted in admin the day I turned Trello back on. Leave In Progress and At Risk cards as they are.”
  - The set is one list status. The rule still has to be found. The other cards stay out.

### 6.2 Clarity

Section 2. A different channel to the same person, with the same contents, is a
3, not a 2.

- BAD: “Wrap up the leftover reviews or flag them before Friday.”
  - One reading closes them. The other only comments.
- GOOD: “Can you sort out the leftover reviews before Friday? Arthur posted how he wants each kind handled.”
  - One request. The per-case rule lives in a seeded record, Arthur’s post, so each item still has one action. A chain of if / but-not / then-also clauses in the prompt fails Contrived (Eval 1 §2.7).

### 6.3 Cross-service

Section 3, the two services. This check has no 3. A second service that does not
change the answer still fails.

- BAD: “Read the #zombie-marketing thread and tell me which of those five campaigns we already paused.”
  - The thread already lists the five and which were paused.
- GOOD: “Tell me which of the campaigns Jane named in #zombie-marketing are actually paused. The thread is what she remembers. The campaign record is the status.”
  - Neither source alone is enough, and the prompt says which one wins.

### 6.4 Truthfulness

Section 3, tight claims. One wrong channel, ticket, vendor, amount, date, or
fiscal period is a 2. A loose error, such as a wrong first name, is also a 2,
even when there is only one (Eval 1, 2026-10-05).

- BAD: “Leonard’s note in #ua-spend on February 11 said the Adjoe test starts the 12th. Use that.”
  - The note is in #zombie-marketing, dated February 10, and the test had already started.
- GOOD: “Use the note I wrote when I turned the Adjoe test on.”
  - No date or channel to get wrong; the note supplies them. A line telling the agent the prompt may be off hints at the trap and fails Contrived (Eval 1 §2.7).

### 6.5 Feasibility and access

Section 3, the hidden record. Gmail, Slack, calendar, Drive, Docs, Sheets, and
Slides show only what this person can see. Contacts, GitHub, Snowflake, Trello,
Linear, and Confluence are unscoped. A universe browser does not make a hidden
mailbox visible. `Evals/references/persona/acl.md` is the authority for scope.

- BAD: “Pull the invoice Jane sent Marcus and reply from my mailbox with the amount.”
  - The invoice is only in Marcus’s mailbox.
- GOOD: “Use the invoices in my mail and the shared ledger. If a bill is missing from those, say it is missing.”
  - A gap stays a gap.

### 6.6 Tools, step lists, and bolt-ons

Section 3, the search hits. A catalog operation, an MCP server name, or “use the
Gmail tool” fails. “Check Slack” stays. A “first / then / finally” list fails. A
sentence that can be deleted without changing the task fails. An opaque id or
“January 15 at 3:47 PM” fails unless the task is about that timestamp.

- BAD: “First search Gmail for the invoice, then open Snowflake, then use linear_create_issue. Also book a dentist for Thursday.”
- GOOD: “The Adjoe invoice and the install ledger disagree. Put the difference on the existing Linear project and tell me which number you used.”

### 6.7 Investigation

Section 3, the named cause. This check has no 3. Naming the symptom can pass.
Stating the cause does not.

- BAD: “The CPI jump is the Adjoe incentivized test. Write that up for Robert.”
- GOOD: “CPI jumped last week and I don’t know which test did it. Tell Robert what the records support, and say so if they don’t settle it.”

### 6.8 Clock, assignment, universe, SQL

**Clock.** The universe date is the task date's clock: 2026-02-14 00:00 UTC on a
Feb 14 task, 2025-10-01 00:00 PT on an Oct 1 task. A prompt that treats an
event after the clock as already done fails (Eval 1 §2.8). A future deadline can
stay a deadline.

**Assignment.** Business function has no 2; a mismatch is a 3, which blocks a
pass at 5. A competency or task-skill mismatch fails (Eval 1 §1.5). The job
title does not have to match the competency.

**Missing fact.** A key fact that is absent, or that no catalog tool can
retrieve, is a 2. A detail the prompt does not need can pass.

**Snowflake and Confluence.** A closed ticket with later activity, or line items
that do not sum to the total, is a 2 even if no agent has missed it yet.

**Injection.** Skip it only when no-injection is saved. A colliding id, a
missing column, a date that breaks the thread, an added message whose author is
not in its channel, or an undoubled apostrophe inside a quoted string is a 2.

## 7 · Rubric patterns

Among 286 reviews that were not a pass at 5. Count each row once, at its highest
severity. Missing outcomes count in the numerator only. A cascade group counts
once. Quality fails on any Major or any Moderate. Minor issues on 5–10% of the
rows are a 3, and on more than 10% a fail (Eval 3 Local Overrides).

| Issue | Reviews | Severity |
|---|---|---|
| Duplicate or cascade | 128 | Moderate, once |
| Missing coverage | 100 | Major |
| Overly specific | 92 | Major |
| Incorrect | 87 | Major |
| Not atomic | 85 | Major |
| Wrong category | 72 | Moderate |
| Not self-contained | 63 | Major |
| Unauthorized | 61 | Major |
| Overly broad | 45 | Major (2026-10-17) |
| Harmless specificity | 16 | Minor |
| Unobservable | 8 | Major |
| Not agent-centric | 6 | Major, and fails phrasing |
| Vague exemplar | 5 | Moderate |

These fail the rubric on their own: any weight two levels off, or more than 10%
of the rows one level off; two rows that every run will fail because the row is
wrong; zero Outcome rows; one invalid process row, or two or more missing
ordering checks; nonstandard Agent titles such as "The Agent's …" on more than
10% of the rows; one title that is not about The Agent or that names a tool; one
prohibition title, or one row an agent passes by doing nothing; a row missing
title, category, weight, justification, or evidence. The narrower cases (a few
rows one weight level off, exactly one missing ordering check, a few "The
Agent's …" titles) are the non-fail bands in the Eval 3 Local Overrides.

### 7.1 Missing coverage

Section 4, a missing row.

- BAD: The prompt says Arthur’s cut mail carries only his rows. The rubric grades the rows and never grades that the mail has nothing else.
  - A run that attaches the whole pack passes every row.
- GOOD: “The Agent sends arthur.blake@harmonygames.co a cut mail whose body contains only the eight cut rows.”
  - The exclusion is phrased as what the body contains.

### 7.2 Overly specific

Section 4, the other allowed answer. An exact value that is the only correct
value is fine. `214 MB` and `214.0 MB` are the same number. A row must not lock
a channel, a heading, or a cause the records do not settle.

- BAD: “The Agent’s Slack post says the CPI jump was caused by the Adjoe incentivized UA test.”
  - The records show concurrency, not causation. A careful refusal fails the row.
- GOOD: “The Agent reports that the records do not establish a cause for the CPI jump, and names the Adjoe test as concurrent.”

### 7.3 Incorrect

Section 4, the record.

- BAD: “The Agent states that Firebase moved to the paid plan and the free tier was switched off on December 27, 2025.”
  - Nothing in the records says that.
- GOOD: “The Agent states the Firebase plan status recorded on the billing page, and does not supply a switch-off date the page does not give.”

### 7.4 Not atomic

Section 4. Different writes and different services are separate rows. A verdict
and its reason are separate rows. Fields of one message can stay together. A
bundle is not repaired by weakening it to “at least N” or “any one of.”

- BAD: “The Agent posts the variance to Slack and creates the Linear ticket.”
- GOOD: Two rows. One for the Slack post and the variance it must contain. One for the Linear ticket and the same variance.

### 7.5 Not self-contained

Section 4, the title.

- BAD: “The Agent includes the 15 taxonomy events.”
  - Invented names pass. A note that accepts more than the title is the same failure. A note that accepts less is overly specific.
- GOOD: “The Agent includes begin_level, left_level, and notification_permission, each marked implemented or not implemented.”

### 7.6 Unauthorized

Section 4.

- BAD: The prompt says to mark what has not been paid. The rows require AppLovin, AdMob, and Meta to be marked paid out.
- GOOD: “The Agent marks each network the ledger shows as unpaid, and leaves the others unmarked.”

### 7.7 Too broad, duplicates, category

Sections 4 and 5.

- BAD: “The Agent emails Arthur his cut.”
  - The mail can attach the whole bible and still pass. Another row catching it is not a defense.

An umbrella row that repeats narrower rows is a duplicate, counted once. Two
rows that both fail when one email misses one recipient are one group. Outcome
is the default. A write labeled Process is the wrong category.

### 7.8 Phrasing

Section 5.

- BAD: “The Slack update mentions the launch date.”
  - The subject is the message. One title like this fails agent-centric for the set.
- GOOD: “The Agent includes the launch date of 2026-02-12 in the Slack update.”
- BAD: “The Agent does not close ENG-123.”
  - A prohibition fails even when the prompt forbids the action. “The Agent leaves ENG-123 open” fails the same way: an agent that does nothing passes it.
- GOOD: “The Agent closes exactly three of the leftover reviews.”
  - A count on a write the Agent must make. With a row for each review that must close, a run that also closes ENG-123 fails it, and so does a run that does nothing.

`such as`, `e.g.`, and `for example` in any graded field are a Moderate issue,
once per row.

### 7.9 Weights, process, and rows that always fail

| Weight | Work |
|---|---|
| 1 | One lookup or a literal from one source |
| 3 | One comparison, calculation, or small reconciliation |
| 5 | A join across sources, or a cause drawn from more than one record |

Weight the row, not how important it feels. A bundle gets split, not a 5.

Process is only an order that every valid path must follow and that an outcome
row cannot see. Most tasks need none. One invalid process row fails Process Rubrics.

Two rows that every careful run will fail, because the value is not in the
records or only another person can see it, fail the rubric before any rollout.
A real model miss is not that defect.

## Review procedure

The checklist is filled by the deep recheck in [deep_recheck.md](deep_recheck.md),
not by one reviewer. Prompt passes P1–P4 fill sections 2, 3 and 6. Rubric passes
R1–R7 fill sections 4, 5 and 7, and read the prompt only to know what the rows
must cover. Every blank a pass owns gets an answer and a quote.

`deep_recheck.md` sets the pass inputs, the finding format, the main-session
check, where confirmed findings go, and the `## Deep Recheck` section that ends
the report.
