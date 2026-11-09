# Independent read of 04_Prompt.txt

Prompt sha256 22df2abfec652efab31a87a9cfb74b77632113a98dae00225368f31f29b66ae9 (prefix 22df2abfec65 matches).
Persona: Samuel Turner, Game Designer. Clock: Oct 1, 2025 00:00 PT.

## Result

| ID | Finding | Eval section | Severity |
|---|---|---|---|
| F1 | The rule doc says a changed line "needs a string ticket under DES-314". Neither the prompt nor the DM says whether the agent files it, so write sets differ. | 2.6 write-action gate | **FAIL, conditional** (see section 3) |
| F2 | S3, S4 and S5 can each be deleted with nothing lost, because the DM carries them. They are not unrelated asks. | 1.3.2 Bolt-on | **Clean** under the controlling band, with literal exposure to common_errors 6.6 |
| - | AI-Text red flags: 0 of 5 | 1.2 / 2.7 | Clean |
| - | Delegation scan | 2.6 gate | Clean |
| - | Trap hint, riddle, audit form, if-chain, hidden destination, command list | 2.7 / 1.3.1 | Clean |
| - | Pre-solving, tool mention | 1.3.3 / 1.3.4 | Clean |
| - | Statements attributed to the DM: 9 of 9 supported | 1.2 incorporation | Clean |
| - | Persona fit | 1.1 | Clean |

The prompt's own wording has no failing defect. The one FAIL comes from a sentence in the doc the prompt
pulls in, and the fix belongs in that doc, not in the prompt.

Sentences, with word counts:

- S1 (21): "We're about to put more money behind beta and Leonard wants one straight answer on what we actually say to players."
- S2 (31): "His DM to me from yesterday has the whole job in it, it starts from the Zombie Match PN sheet, and I need you to do all of it for me."
- S3 (21): "The new sheet and the one-page note go in my Drive folder and the checklist goes on our push notifications card."
- S4 (16): "He also wants things done on the tickets and some emails sent, so do those too."
- S5 (12): "When it's all finished tell him the counts in that same DM."
- S6 (9): "You don't need to run anything by me first."

## 1. AI-Text red flags (1.2)

| Red flag | Found? | Quote and defence |
|---|---|---|
| Document formatting | No | One unbroken paragraph. No headings, bullets, numbers or bold. |
| Polished connective phrasing | No | The connectives are "also", "so do those too", "When it's all finished". A search for "additionally", "furthermore" and "please ensure" finds none. |
| Enumerated deliverable specs or preservation rules | No | Nearest candidate is S3, "The new sheet and the one-page note go in my Drive folder and the checklist goes on our push notifications card." It names three things and where they go. It gives no contents, columns or preservation rule. Naming a destination passes in the calibration ("post the summary in #winddown"). The column list stays in the DM. |
| Even, symmetric sentence lengths | No | 21, 31, 21, 16, 12, 9 words. Shortcuts are present: "PN sheet", "DM", and the comma splice "has the whole job in it, it starts from". |
| Staged errors | No | No misspellings and no non-ASCII characters. The comma splice in S2 is ordinary typing, not planted. |

I cannot defend any flag. Spec-sheet register triggers (2.7): 0 of 4.

## 2. Delegation scan (2.6)

No "I'll", "I need to", "I want to" or "I'm going to" statement appears anywhere.

| Statement | Next to agent imperative? | Who acts |
|---|---|---|
| "We're about to put more money behind beta" | Not an ask | The company. No write in this task. |
| "I need you to do all of it for me" | Is the imperative | The agent. "you" and "for me" settle it. It is not "I need to". |
| "He also wants things done on the tickets and some emails sent, so do those too" | Is the imperative | Leonard wants, the agent does. "so do those too" settles the passive "done" and "sent". |
| "You don't need to run anything by me first" | Beside all of them | The agent acts. Samuel gives up his own review and promises no action of his own. |

Result: no user-self-action reading exists. Hard gate clean.

## 3. Write-action divergence (2.6)

Intent is clear and the key details are present, either in the prompt or in the DM. The prompt can be read two
ways on one point only, F1.

Writes the DM states. Each maps to a prompt sentence:

| # | Write | DM quote | Prompt |
|---|---|---|---|
| W1 | New sheet in Samuel's Drive folder, one row per message, seven columns | "Put it in one sheet in your Drive folder, one row per message" | S3 |
| W2 | One-page note in the same folder | "Next to it a one-page note for the team" | S3 |
| W3 | Comment the call on each ticket | "Leave the call as a comment on each ticket" | S4 |
| W4 | Move each ticket | "move the ticket to match" | S4 |
| W5 | New ticket where none exists, no duplicates | "Anything with no ticket gets one, but don't make a second one" | S2, S4 |
| W6 | Each Go on a checklist on the card | "Every Go goes on a checklist on our push notifications card" | S3 |
| W7 | Email each asker except Leonard | "Email each person who asked for something, apart from me" | S4 |
| W8 | Go, Hold and Drop counts in the DM | "tell me here how many Go, Hold and Drop" | S5 |

### The three axes you named

| Axis | Competing reading | Settled by | Fork? |
|---|---|---|---|
| Act vs defer | Stage everything for Samuel's review | S6 "You don't need to run anything by me first." | No |
| Send vs draft | Draft the emails, Samuel sends | S4 "some emails sent, so do those too", plus DM "Email each person" | No |
| All of the DM vs part | Only what the prompt lists | S2 "has the whole job in it ... do all of it". S2 to S5 also reach all of W1 to W8. | No |

### The two strongest readings

| | Reading A: the DM is the whole job | Reading B: the DM, plus what its rule doc says a row needs |
|---|---|---|
| Support | S2 "has the whole job in it". The DM's ticket writes are comment, move and create-if-none. The DM points at the doc to "make a call". The sentence sits among column definitions, so it answers the String change column. | S2 "do all of it". Doc: "A line that differs from what the client ships needs a string ticket under DES-314". DM: "Anything with no ticket gets one". S6 removes any chance to ask. |
| Writes | W1 to W8. String change is filled in on the sheet and no ticket is made. | W1 to W8, plus W9: one new string ticket under DES-314 for each Go whose final headline differs from what the client ships, emoji aside. |

**They differ:** Reading B adds Linear issue creates that Reading A does not make. That is F1.

### Does anything resolve F1?

The best rebuttal comes from `prompt-incorporation-v1` (WORKFLOW.md), which says "a reference used for facts
does not incorporate all its rules" and a source "cannot silently add a new obligation". The DM aims the doc
at one job, "make a call on each one using the message rule doc". On that view the sentence is a fact that
fills an existing column, and S2's "the whole job" excludes W9.

I do not think that closes it, for three reasons quoted from the records:

1. The doc is already doing more than the call. The DM's "move the ticket to match" cannot be carried out
   without the doc's "Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo".
   So a "calls only" scope cannot hold, and the string-ticket rule is a ticket rule in that same doc, under
   the same parent.
2. The sentence names no actor. "needs a string ticket" does not say who files it or when.
3. S6 removes the check-in that would settle it in real life, so the agent decides alone.

The eval also says "A leading or more-likely interpretation alone does not resolve it", so "A is more likely"
is not enough. Reading A is the better reading, and I would expect the contract to keep W9 out of the required
set. That does not stop runs from splitting on it, and the gate tests the write the agent chooses.

**Severity: FAIL, on two conditions.**

- At least one Go row's final headline differs from what the client ships. I could not check this inside my
  read limits. With none, there is no fork and F1 is clean.
- No other persona-visible record settles who files string tickets. Also unchecked, for the same reason.

A reviewer who accepts the contract rebuttal would score this clean. My confidence in FAIL over clean is
moderate. It matters more if the rubric counts new tickets, because the DM's "don't make a second one" invites
an exact count that W9 would break.

### Forks considered and rejected

| Candidate | Why it is not a fork |
|---|---|
| "a one-page note for the team": must the agent share it or post it? | No text asks for that, and S3 fixes the location. Samuel's folder is private with no shares in base data, so an agent may add a share. Nothing requires it, so the rubric must not grade it. |
| "apart from me": Leonard or Samuel? | The DM's author is Leonard, so "me" is Leonard. Reading it as Samuel is a misreading. |
| "He also wants": a second request outside the DM? | "also" continues S3's list. S2 says the DM is the whole job. |
| "that same DM": thread or new message? | Same recipient and channel, so wording only. |
| "a checklist": new or existing? | The card has no checklists in base data. |

## 4. Sentence tests

| Sentence | Trap hint / riddle | Audit form | If-chain | Hidden destination | Command list | If deleted, what breaks? |
|---|---|---|---|---|---|---|
| S1 | No | No | No | n/a | No | "His", "He" and "him" lose their referent and the motive goes. Load-bearing. |
| S2 | No | No | No | No | No | The whole task goes. Load-bearing. |
| S2 clause "it starts from the Zombie Match PN sheet" | No | No | No | n/a | No | **The source stops being unique.** Base has two workbooks, Push Notifications Zombie Match (f_a325dd4af80afc5994d5dc) and Push Notifications Domino Adventure (f_351b98dfb06f61fb8357d0), and each has its own `PNs Beta` tab. The DM says only "PN sheet" and "PNs Beta tab". Keep this clause. |
| S3 | No | No | No | No, names both places | No | Nothing. The DM states both places. |
| S4 | No | No | No | No | No | Nothing. "do all of it" and the DM cover it. It adds least of the six. |
| S5 | No | No | No | No, "that same DM" points to S2's DM | No | Nothing. DM: "tell me here". |
| S6 | No | No | No | n/a | No | Partly. "do all of it" and "do those too" still say act, but S6 is the only explicit waiver of review, so a cautious agent could stage the emails without it. S4 and S6 overlap here: either alone holds the line, so do not delete both. |

Notes on the closest calls:

- **Trap hint.** "what we actually say to players" is Leonard's own goal in his own words. It points at no
  hidden item. The DM's distrust line ("The PN sheet says six are Ready and I don't trust that") is not in the
  prompt. This sits with "CPI jumped last week", not with #31.
- **Audit form.** "do all of it for me" has a similar shape to #1 ("complete the ... handoff it requires"), but
  it has none of the form verbs and is close to the passing "can you check what's still open and close it out?"
- **Hidden destination.** Unlike #42 and #47, the places are named. Unlike #44, "that same DM" has a clear
  antecedent. "my Drive folder" resolves to Samuel's one owned folder. "our push notifications card" resolves
  to `[Feature] Push Notifications - Samuel + Leonard`, open on ZM ROADMAP. The other base matches are
  `local Push Notification` (DD Product Roadmap) and `Push-notification boost` (closed).
- **Command list.** "When it's all finished" is one closing step, copied from the DM's "When it's done". There
  is no procedure. A case-insensitive search for the common_errors hit words finds only "first" in S6, which
  means "beforehand", not a step.
- **If-chain.** The prompt contains no "if", "unless" or "but".
- **Pre-solving.** No cause, answer or count is stated. "Zombie Match" names a start point, not a finding.
- **Tool mention.** "Drive folder", "DM", "tickets", "card" and "emails" are natural service references.

### F2: deletion and bolt-on

S3, S4 and S5 pass the literal test of being removable, and common_errors 6.6 says "A sentence that can be
deleted without changing the task fails." I still score them clean:

- `scoring.json`, which the eval says outranks inline text, defines the fail as "One or more asks are unrelated
  to the task's central purpose".
- Eval 1.2 also describes a bolt-on as "unrelated asks".
- All three restate parts of the same job, and Coherence has no NON-FAIL band.

The counterargument: `scoring.json` yields to the Local Overrides, and they adopt common_errors. But the override
row lists what it adopts and bolt-ons are not on that list, common_errors says "this copy follows the evals", and
its own BAD example is an unrelated ask ("Also book a dentist for Thursday."). So I read 6.6 as meaning unrelated
sentences too.

A reviewer applying 6.6 word for word could still hit them. No change is needed under the controlling band.

## 5. Attribution check

| Prompt says | DM or record says | Supported? |
|---|---|---|
| "We're about to put more money behind beta" | "we're about to put more money behind beta" | Yes, verbatim |
| "Leonard wants one straight answer on what we actually say to players" | "I want one straight answer on what we actually say to players" | Yes, verbatim |
| "His DM to me from yesterday" | Sender EMPLOYEE_0038 is Leonard Hayes. D06L58XCVKK is the only IM holding both men. ts 1759264851 is 2025-09-30 20:40:51 UTC, which is 13:40 PT the day before the clock. | Yes |
| "it starts from the Zombie Match PN sheet" | "The PN sheet says six are Ready"; "Take every row on the PNs Beta tab" | Yes. "Zombie Match" is Samuel's addition, not in the DM. It matches the base workbook title, and the doc says "live in Zombie Match today". |
| "The new sheet ... go in my Drive folder" | "Put it in one sheet in your Drive folder" | Yes. "new" is Samuel's gloss and is consistent. |
| "the one-page note go in my Drive folder" | "Next to it a one-page note for the team" | Yes |
| "the checklist goes on our push notifications card" | "Every Go goes on a checklist on our push notifications card" | Yes |
| "He also wants things done on the tickets and some emails sent" | "Leave the call as a comment on each ticket and move the ticket to match"; "Email each person who asked for something" | Yes |
| "tell him the counts in that same DM" | "When it's done tell me here how many Go, Hold and Drop." | Yes |

Nothing is invented. The DM's pointer to "the message rule doc" resolves to "Beta message rule", owned by Leonard
and shared with Samuel. Its Go, Drop and Hold match the DM's "how many Go, Hold and Drop". The DM gives
instructions and context, not a precomputed answer, so the four incorporation conditions in 1.2 hold.

## 6. Persona (1.1)

A Game Designer would plausibly send this. Nothing is out of role.

- Leonard is Co-founder & Creative Director, so a DM to a designer fits.
- Base data ties Samuel to this exact work: the card is named `Samuel + Leonard` and carries the comment "Samuel
  says 3 days", and the sheet sits under `Design/`.
- "PN" is natural shorthand for this role. No analyst or engineering jargon appears.
- S6 waives only Samuel's own review, which is his to waive.

## 7. Smallest fixes

**F1.** Do not change the prompt. A prompt-side fix would need a per-case rule or a pointer at the row, and 2.7
says a per-case rule belongs in a seeded record. Change one clause in the "Beta message rule" doc.

Current: "A line that differs from what the client ships needs a string ticket under DES-314, because the
strings are hard-coded."

- If no ticket is wanted: "A line that differs from what the client ships is a yes under String change, because the strings are hard-coded."
- If a ticket is wanted: "A line that differs from what the client ships needs a string ticket under DES-314, because the strings are hard-coded, so file one when you make the call."

Either edit changes the SQL and its hash, so /injection must run again. The doc's style run ends at 1426, which
is the current body length, so it must move with the text. If a ticket is wanted, every new-ticket count in the
OE and rubric must include string tickets.

**F2.** No change. Optional only: deleting S4 removes the vaguest sentence ("things done") and the task stays
the same, because S6 and the DM's "Email each person" still settle send vs draft. This is safe only if S6 stays.
S3 and S5 would stay literally deletable either way.

## Checks I could not run

These need rows outside the two records you allowed. None is a finding.

1. Does any Go row's line differ from what the client ships? (Decides F1.)
2. Does another record say who files string tickets? (Decides F1.)
3. Was any ask filed after the DM and before the clock? The DM says "up to today", meaning Sep 30, while the task's
   today is Oct 1. Rows in that window would change the cohort.
4. Did Samuel file an ask himself? "apart from me" excludes only Leonard, so the agent would be emailing Samuel from
   Samuel's own account.
5. Does the SQL add a rival to anything checked here: a second Leonard DM on Sep 30, a second Samuel folder, or
   another push notifications card? Base has no such DM or folder, and its near-match cards are covered in section 4.
6. Does DES-314 exist? It is not in base (highest DES number is 312), so it must come from the SQL. The DM names it;
   the prompt does not.

## Read limits and disclosures

- Base checks used read-only Python and grep on `Universe_SynthCut`. I avoided the search helpers because they write
  caches under `Evals/`. No SQL was run, and I did not run `hg_store_input.py` or `hg_write_output.py`.
- My `sed` ranges printed lines next to the two records: a gdrive row titled "Phone message checks", a Slack reply
  from Vincent with its UPDATE, and a Trello INSERT header. No finding uses them.
- One `ls` to confirm the output folder printed two filenames under `Working_Files/plan/`. I did not open them.
- D06L58XCVKK lists two extra bare member IDs (U04UP2L1RUY, U06LEMPBQJC) and `num_members` 4, though it is `is_im`.
  This looks like an export artifact. It does not affect "His DM to me" and is not scored.
