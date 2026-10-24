Here is a red-team analysis of the V2 task-authoring harness, ranked by severity. These findings expose mechanical gaps where an authoring model can follow every instruction, clear every blocking script, and still output broken, trivial, or internally contradictory tasks. 

### 1. The "Predicted All-Fail" Loophole (Unsolvable Task Bypasses QC)
* **Location:** `09_Rubric_Coverage_Plan.md` — Hard gate 11, Section E Summary (`predicted all-fail rows ≤ 1 ☐`), and Check mode 5.1 (`Two or more → FAIL`).
* **The Exploit:** An AI authoring a task to look "extremely hard" for frontier models can intentionally design a task with one rubric criterion that asks for a value that is strictly `entity_unreachable` or `target_data_absent`. Every single agent tested will fail this criterion, artificially capping the maximum possible score and ensuring the task looks incredibly difficult.
* **Why gates miss it:** The hard-coded logic in the playbook and the check phase literally permits one guaranteed failure. Check mode explicitly states that a FAIL is only triggered if "Two or more" rows are predicted to fail. A task with exactly one mathematically unsolvable grading row will cleanly pass all gates.
* **Mechanical Fix:** Change the tolerance to strictly 0. Update Gate 11 to read "One or more fail the rubric...". Update Section E to `predicted all-fail rows = 0 ☐`, and Check mode 5.1 to `One or more → FAIL`.

### 2. Tier Volume Downgrade (Easy Task Disguised as 500+ Calls)
* **Location:** `04_Prompt_Brief.md` — Procedure §4 (Breadth for the tier) and Check mode C12 (Tool use and cross-service).
* **The Exploit:** The harness dictates that Long-Horizon tasks require 100-500+ calls and 10+ services. However, check C12 establishes the strict QC floor as only "≥ 2 services". It explicitly labels the design target of 10 services as "Advisory here." An AI can write a trivial 2-service, 5-call prompt, log the finding as "Advisory", and pass the `prompt-check` stage gate because Advisory findings do not block handoff.
* **Why gates miss it:** The primary difficulty levers (breadth and volume) are designated as non-blocking `Advisory` tags rather than hard constraints tied to the assigned tier. The stage gate script only blocks on `FAIL` or `C2`.
* **Mechanical Fix:** Make C12 tier-aware. Change the rule to: "Fail if tier is Long-Horizon and services < 10; Fail if tier is Normal and services < 7. Delete 'Advisory here'."

### 3. Open-Ended Delegation Shortcut (Bypasses UGT & Depth)
* **Location:** `04_Prompt_Brief.md` — UGT procedure (C6) step 3: "A choice the persona explicitly delegates... and open-ended work with objective acceptance boundaries pass."
* **The Exploit:** To satisfy Unique Ground Truth (UGT) without doing the rigorous work of pinning a precise 500+ call final state, the AI generates a prompt that explicitly delegates the choice (e.g., "Find *any* 5 open bugs anywhere and assign them to *anyone* on the dev team"). This creates an objective acceptance boundary, cleanly passing C6. However, an agent can shortcut this by picking the first 5 records on page 1, completely neutralizing the intended long-horizon difficulty.
* **Why gates miss it:** C6 provides a blanket exemption for "open-ended work" without verifying if that open-endedness collapses the discovery volume required by the task tier.
* **Mechanical Fix:** Add a condition to C6: "Open-ended boundaries or explicit delegation Fail if they allow the agent to satisfy the requirement without traversing the minimum volume or services intended by the task tier (i.e., if it introduces a low-effort shortcut)."

### 4. The Visibility Check "Load-Bearing" Blindspot (False Feasibility)
* **Location:** `08_Evidence_Ledger.md` — Hard gate 5 (Persona reachability).
* **The Exploit:** For seeded records, the AI is instructed to prove visibility by running `persona_view.py check-sql --load-bearing <ids>` and pasting the YES lines verbatim. The AI can intentionally omit the ID of an inaccessible critical-path record from the `--load-bearing` argument. The script will output YES for the provided IDs, the AI pastes them, and the stage gate script "re-runs every pasted line." The gate blindly trusts the AI's selection of which IDs needed checking.
* **Why gates miss it:** The stage gate only validates the text the AI *chose* to paste, not the semantic completeness of the IDs against the actual ledger facts. 
* **Mechanical Fix:** The stage gate script must not rely on pasted text. It must dynamically parse the `08` ledger's Fact table (§B), extract all IDs/pointers for scoped services, and automatically run `can-see` / `check-sql` against that exhaustive set to strictly enforce visibility.

### 5. Clock Rule Contradiction (Blocks Future / Scheduling Tasks)
* **Location:** `08_Evidence_Ledger.md` — Hard gate 4 vs `04_Prompt_Brief.md` Hard gate 4.
* **The Exploit/Contradiction:** `04` Gate 4 states "A later date may appear only as a deadline that has not happened yet," correctly allowing tasks like scheduling a meeting for next week. But `08` Gate 4 strictly states: "A record dated on or after the clock is a universe defect (Temporal Field Inconsistency, Fail) — report it, do not route around it." If the prompt correctly asks to schedule a future calendar event, the expected OE data must have a date > clock. The AI in check mode will rigidly flag this as a Fail, blocking any forward-looking tasks.
* **Why gates miss it:** The `08` rule conflates a record's *creation/modification* timestamp with *semantic* timestamps (like the target start time of a future meeting or deadline).
* **Mechanical Fix:** Update `08` Gate 4 to read: "A record's creation or modification timestamp on or after the clock is a Fail. Semantic dates (e.g., meeting start times, scheduled deadlines) may be after the clock if they represent unhappened future events."

### 6. Rubric Shallow Process Bypass (Agents Can Spoof Outcomes)
* **Location:** `09_Rubric_Coverage_Plan.md` — Procedure §3 (Three-condition test) and Category 2.6.
* **The Exploit:** The playbook actively forces the AI to delete "Process" criteria in favor of "Outcome" criteria ("no stricter Outcome can capture it"). In a massive 500+ call task, the final Outcome might just be a single Slack message. If the rubric only grades the final message content, an agent might guess the answer, hallucinate it, or find a single god-mode search shortcut. Because the rubric plan systematically stripped out checking the intermediate tool uses, the agent gets a 5/5 without ever navigating the 500+ call labyrinth.
* **Why gates miss it:** The QC spec optimizes for "Outcomes" to avoid brittle grading, but for Long-Horizon evaluations, outcomes alone rarely prove the required reasoning depth was achieved.
* **Mechanical Fix:** In `09` Procedure §3 and Category (2.6), add: "For Long-Horizon tiers, Process criteria MUST be retained if the final Outcome does not mathematically guarantee that the deep discovery path was taken (e.g., if the answer could be achieved via a single shortcut search)."

