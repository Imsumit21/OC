**Oracle Events**

*What replaced the golden solution, how to write a set that passes /oe, and how to turn it into a rubric.*

| NEW IN SPEC V2 This guideline is new. It replaces the golden-solution material that used to sit inside Overall Task Flow and Rubric Writing. If you tasked on this project before September 2026, read it in full — the artifact, the check that validates it, and the way it feeds the rubric have all changed. |
| :---- |

## **Change log**

| Date | Updates |
| :---- | :---- |
| Sep 26, 2026 | New document. Oracle Events replace the free-text golden answer; /oe replaces /golden; the tool-call minimum now attaches to the golden run, not to the Oracle Events set. |

## **1 · What changed, and why**

| Earlier | Now |
| :---- | :---- |
| A free-text **golden answer** describing the finished result | **Oracle Events** — the key steps a correct agent takes, from discovery to completion |
| Checked by /golden | Checked by /oe |
| Written after the rubric, or alongside it | Written **before** the rubric, and used to derive it |
| Rubric prefill generated a draft set from the golden answer | Prefill is off. You write every criterion yourself, from your own Oracle Events |
| The tool-call minimum used the rollout average | It uses the **golden run** — a rollout that scored 100% on your rubric — if you have one, and the average across all six only if you do not |

The reasoning is that a finished answer tells a reviewer very little about whether a task is solvable, and nothing at all about *how*. A step list tells them both.

## **2 · What Oracle Events are for**

### **2.1 They prove the task is solvable**

With hinting removed from the task, there is no longer a hint that can rescue an agent from a prompt that turns out to be impossible. Your Oracle Events are the demonstration that a correct path exists: **following them literally should produce a correct trajectory.**

### **2.2 They drive the rubric**

Every action in your Oracle Events becomes an Outcome rubric. Gaps that no Outcome can cover become Process candidates. Writing the Oracle Events first makes the rubric step substantially faster and materially better — the most common rubric defect in the last audit was missing coverage, and a complete OE set is the cheapest protection against it.

### **2.3 What they do *not* do: set the tool-call minimum**

This one causes confusion, so it is worth stating plainly. The tool-call minimum for your tier is measured against the **golden run** where one exists — and a golden run is a **baseline rollout that scored 100% on your rubric**, meaning it passed every criterion. It is a run the model produced. If no rollout reached 100%, the minimum is measured against the average across all six.

| ORACLE EVENTS ARE NOT A GOLDEN RUN Your Oracle Events are a path you write. They are required on every task, they prove solvability and they drive the rubric — but they have no bearing on how your tool-call count is measured. Counting the steps in your OE set and comparing that number to your tier minimum tells you nothing about whether the task passes. |
| :---- |

## **3 · The five fields**

| Field | What goes in it |
| :---- | :---- |
| **Action** | What needs to happen — search, retrieve, send, create, update |
| **Information** | What needs to be discovered or verified before the agent can act |
| **Tool / Service** | Which tool and which service, matching where the data actually lives |
| **Parameters** | The important inputs: identifiers, filters, date ranges, values |
| **Expected Data** | What the step should retrieve or produce |

| FORMAT Oracle Events are free-form text, not structured JSON. They are written in a field that blocks pasting, because they must be written by you rather than generated. Number them, and keep each one to a few lines. |
| :---- |

## **4 · What a good event looks like**

| OE 2  Establish which build the January approval message refers to.       slack\_conversations\_history (channel C09UHHN6PFZ, 2026-01-17..20)       Expected: 1.0.56 posted 01-17; approval 01-19 06:41; 1.0.57       submitted 06:44 and released 01-20. OE 4  Aggregate paid spend by network for the title.       Snowflake AD\_SPEND\_DAILY, filter game\_id \= combo\_fighter       Expected: 152 rows, channel \= meta on all of them, 4510.33 USD,       615 paid installs, 2025-12-26 to 2026-02-08. OE 5  Establish that the primary lookup is unavailable and recover.       gmail\_search\_messages (query: "Season Pass rollback")       \-\> returns a server error on every attempt       Agent then reads the same thread from the shared drive copy.       Expected: the rollback decision and its date, from the drive document. |
| :---- |

Each one names the action, the service, the filter and the expected values. That is what /oe needs in order to check it, and it is what lets you write the corresponding rubric without going back into the universe.

## **5 · Completeness**

| Requirement | What fails it |
| :---- | :---- |
| Covers the full critical path | The set jumps from “searches Slack” to “notifies the owner” with the analysis missing |
| Includes the key discovery and retrieval steps | A fact appears in the expected data with no event explaining how it was obtained |
| Includes the dependencies between steps | Nothing records that B can only happen once A has produced its value |
| Includes every required write or action | The prompt asks for tickets to be raised and no event covers it |
| **Does not** describe what the final response should say | “The agent's final response explains that the tutorial change caused the drop” |

| THE FINAL RESPONSE IS NOT AN ORACLE EVENT Oracle Events describe the path. What the agent ultimately reports is graded by the rubric, not recorded here. If you find yourself writing “the response explains…”, convert it into the discovery step that produced the finding. |
| :---- |

## **6 · Accuracy**

* **Tools and services match where the data actually lives.** Naming Google Sheets for a figure that only exists in Snowflake is an accuracy failure even if the figure itself is right.  
* **Parameters, entity names, IDs and expected data match the universe.** Check each one against the explorer. A channel ID from memory is the classic way to fail /oe.  
* **Following the events literally produces a correct trajectory.** Read your own set as if you were the agent. If a step cannot be executed from what the previous steps produced, something is missing.

## **7 · No non-actions**

An Oracle Event must describe an **observable action or discovery**. Statements about what the agent refrains from doing are not events.

**✗**  “The agent does not give up.”

**✗**  “The agent does not stall when the search fails.”

**✗**  “The agent does not stop at the first explanation it finds.”

**✓**  “Establishes that the mail search is unavailable, then reads the same thread from the shared drive copy. Expected: the rollback decision and its date.”

**✓**  “Reads the 2026-02-11 playable thread to its end. Expected: rejection 21:03, workaround 21:10, campaign live 21:37.”

## **8 · From Oracle Events to rubrics**

### **Step 1 — write every Outcome**

For every action in your Oracle Events, write an Outcome rubric verifying the result, plus a content rubric if the prompt set specific requirements about what that result must contain. For every key fact the user asked to be told directly, write an Outcome covering the final response.

### **Step 2 — look for the gaps**

Once all the Outcomes exist, ask whether any requirement — explicit or implicit — is left that no Outcome can verify. The primary case is **ordering**: A must happen before B, but both Outcome rubrics pass regardless of sequence. In rare cases source verification qualifies too.

### **Step 3 — apply the three-condition test**

1. The requirement is needed by every valid solution path, or the criterion is phrased broadly enough to allow alternatives.  
2. A stricter Outcome rubric cannot capture the same requirement.  
3. The criterion describes a behavioural property, not an execution trace.

If any condition fails, tighten the Outcome instead. If all three hold, write the Process rubric. When in doubt, default to Outcome.

| THE RULE, STATED PRECISELY It is not “actions become Outcome, reads become Process.” It is Outcome first, Process only when no Outcome can verify the requirement — and that requirement can attach to any event in your set, write or read. |
| :---- |

### **Worked conversion**

| Oracle Event | Rubric it produces |
| :---- | :---- |
| OE 4 — Aggregate paid spend by network. Snowflake AD\_SPEND\_DAILY, game\_id \= combo\_fighter. Expected: 152 rows, all channel \= meta, 4510.33 USD | *\[wt 5\]* Agent's record classifies the AppLovin, Unity, Ironsource, AdMob, liftoff and mintegral mentions as monetization placements that bought no installs. *\[wt 3\]* Agent's record states total paid spend of \$4,510.33 across the campaign window |
| OE 9 — Notify the owner, then schedule the review | *\[wt 3\]* Agent notifies the owner of the discrepancy. *\[wt 3\]* Agent schedules the review. *\[wt 1, Process\]* Agent notifies the owner before scheduling the review — ordering, which neither Outcome can prove |

## **9 · The /oe check**

/oe runs at the Oracle Events step, in parallel with /rubric, in the one eval sandbox. Paste your Oracle Events, the exact task prompt, the assignment and persona, and the injection SQL. Wait for both chats to finish, then click **Capture Files once**.

| Verdict | What to do |
| :---- | :---- |
| PASS | Proceed |
| FAIL | Blocked, with no override. Read the report, fix the events, re-run. The evals are deterministic — re-running unchanged returns the same verdict |
| NOT EVALUATED | The command did not run, or Capture Files / Save did not complete |

/oe does not issue NON-FAIL. It either passes or it blocks.

## **10 · The defects /oe flags most**

| Defect | Severity | What it looks like |
| :---- | :---- | :---- |
| **Incomplete solution path** | Fail | A required write is missing, or a fact appears with no event retrieving it |
| **Inaccurate solution path** | Fail | A service, ID, filter or expected value that the universe contradicts |
| **Minor inaccuracies** | Non-fail | An imprecise date range or a rounded figure that does not change the path |
| Non-actions | Moderate | “does not give up”, “does not stall” |
| Final-response content | Moderate | An event describing what the answer should say |

## **11 · Before you leave the Oracle Events step**

* You wrote every event yourself. Nothing was generated or pasted.  
* Every event describes an observable action or discovery.  
* No event describes what the final response should say.  
* Every event names its service and its expected data.  
* Every parameter, ID and figure has been checked against the explorer.  
* Reading the set straight through produces a trajectory that would actually work.  
* Every required write the prompt asks for appears somewhere in the set.  
* If you injected a forced error or an async wait, the recovery or wait path appears as an explicit event.  
* /oe returned PASS.

