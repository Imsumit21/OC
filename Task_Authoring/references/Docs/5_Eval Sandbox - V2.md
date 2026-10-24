**Eval Sandbox**

*One sandbox, five commands, four clicks. What each eval checks, what to paste with it, and the sequence that turns a finished command into a verdict you can read.*

## **Change log**

| Date | Updates |
| :---- | :---- |
| Sep 26, 2026 | Rewritten for Spec V2. Four sandboxes collapsed to one. /golden removed, /oe added. /rubric is audit-only and prefill is disabled. NEEDS-REVISION retired. /prompt documented as the feasibility guardrail. |
| Aug 2026 | Original release. |

## **1 · What it is**

Your task includes one **Eval Sandbox** — a Claude Code sandbox preloaded with your assigned universe files, the eval scripts and the Claude skills that drive them. You type a slash command and it produces a report on whatever you have just built.

* It exists purely to validate your work at checkpoints. **No deliverables are captured from it.**  
* It is provisioned for you, once, and stays open for the whole task. There is no setup command.  
* It holds the same universe files the agent will work against.  
* It is **not** a workspace. Do not run your trajectories, your account rehydration, or any other task work inside it.

| IF IT TAKES MORE THAN TEN MINUTES TO LOAD Refresh your browser. Refreshing re-attaches you; it does not reset the sandbox or lose anything. If a refresh does not bring it up, raise it as a blocker rather than continuing to retry. |
| :---- |

### **What changed in V2**

| Earlier | Now |
| :---- | :---- |
| Four sandboxes, one per stage | One sandbox, provisioned once, open throughout |
| Six commands, including /golden | Five commands. /golden went with the golden solution; /oe replaced it |
| /rubric generated a draft set and prefilled the Criteria Builder | /rubric audits criteria you already wrote. Prefill is disabled |
| Verdicts included NEEDS-REVISION | Four verdicts: PASS, NON-FAIL, FAIL, NOT EVALUATED |

| QUERY HERE. NEVER WRITE HERE. The sandbox may be used to query the universe and understand your data. It may not be used — and nor may any other model — to generate your prompt, your Oracle Events or your rubric criteria. That is a spec violation independent of what the evals report. |
| :---- |

## **2 · The five commands**

| Command | Runs right after | What it checks |
| :---- | :---- | :---- |
| /injection | Injection SQL & Changelog | SQL structure, record references and IDs, dates, data coherence |
| /prompt | Write the Prompt | Solvability, clarity, unique ground truth, tool mentions, naturalness |
| /hardness | Opus Difficulty Check | Whether one Opus trajectory suggests the task is hard enough to continue |
| /rubric | Rubric Instructions | Coverage, atomicity, phrasing, weights, category balance |
| /oe | Oracle Events | Completeness and accuracy of your solution path |

### **What to paste**

| Command | Paste with it |
| :---- | :---- |
| /injection | Your injection SQL |
| /prompt | Exact prompt · assignment and persona · injection SQL · error and async configuration · *optionally* any files the prompt references |
| /hardness | Exact prompt · injection SQL · one Opus trajectory run JSON, **uploaded into the sandbox as a file** |
| /rubric | Your rubric criteria · exact prompt · verified Oracle Events · assignment and persona · injection SQL |
| /oe | Oracle Events · exact prompt · assignment and persona · injection SQL · *optionally* any files the prompt references |

| PASTE THE PROMPT EXACTLY AS SUBMITTED Not a tidied-up version and not a paraphrase. A cleaned-up prompt makes the report describe a task you are not building, and the verdict is then worthless. |
| :---- |

### **When a command does not apply**

* **You seeded nothing.** /injection has no SQL to check, so it does not apply. Do not paste an empty SQL block to satisfy it, and do not go looking for a verdict.  
* **The trajectory file is missing.** /hardness needs the Opus run JSON uploaded as a file. Pasting the prompt and the SQL alone is not enough; you get NOT EVALUATED and a re-run.

Every other command applies to every task.

## **3 · The loop**

Running the command is only the first of four steps, and this is the part that most often costs a verdict.

| Step | What it does |
| :---- | :---- |
| **1 · Run** | Type the command in the sandbox chat. Wait for it to finish |
| **2 · Capture Files** | Pulls the report out of the sandbox |
| **3 · Save** | Persists it. **Takes a few seconds** |
| **4 · Verdict** | Appears on the next step in the sidebar |

| BE PATIENT ON SAVE Save is not instant, and while it runs the page can look like nothing is happening. Do not click Save again, do not refresh, and do not navigate away. A second click or an early exit produces a missing report and a NOT EVALUATED verdict — and then a full re-run. |
| :---- |

### **Two pairs run together**

| Checkpoint | Commands | How to run it |
| :---- | :---- | :---- |
| After the prompt | /injection \+ /prompt | **Two chat sessions, both at once**, then Capture Files **once** |
| After Oracle Events | /rubric \+ /oe | **Two chat sessions, both at once**, then Capture Files **once** |
| After the Opus pre-check | /hardness | One chat session |

Wait for both chats to finish before capturing. **One click saves both reports.** Clicking Capture Files once per command is the single most common misstep in the flow. If you seeded nothing, the first pair collapses to /prompt on its own.

## **4 · Reading the verdict**

| Verdict | Appears on | What it means |
| :---- | :---- | :---- |
| PASS | All five commands | Through. Move on |
| NON-FAIL | /prompt · /hardness · /rubric | This is a pass. Read the report if it is useful, then proceed |
| FAIL | All five commands | **Blocked.** No override. Fix the artifact, then re-run |
| NOT EVALUATED | All five commands | The command did not run, or Capture Files / Save did not complete |

| NON-FAIL IS A PASS \[CHANGED 09/26\] The name reads like a hedge and people treat it as a soft warning. It is not. It scores as passing. Revising and re-running to chase the word PASS costs you a cycle and changes nothing. NEEDS-REVISION no longer exists; if you remember it from the earlier flow, forget it. |
| :---- |

### **When it fails**

1. Open the report and read what it flagged. The report names the defect; guessing at the fix is how people burn three cycles on one problem.  
2. Fix the underlying artifact in its own step.  
3. Come back and re-run the command in full: Run, Capture Files, Save.

**The evals are deterministic.** An unchanged input returns the same verdict.

## **5 · What each command is really for**

### **/prompt — the guardrail that replaced the hint**

Under the previous spec a hint could rescue a prompt that turned out to be impossible. Hinting is gone from the task, so nothing downstream does that any more. /prompt is now the only thing standing between you and an unsolvable task. **Treat a FAIL there as fatal, not advisory.**

It asks: can the assigned persona actually solve this, given its ACL? Does every careful run end in the same final state? Are tools, MCP servers or parameters named? Does it read like a person typed it?

### **/injection — the universe check**

It reads your SQL, not your description of it. It catches dates after the frozen clock, comments that predate their parent, references to records that do not exist, IDs that break the existing format, and figures that do not reconcile. Run it the moment you finish the SQL, not at the end of the task.

### **/hardness — it reads one real trajectory**

It runs right after the Opus 5.5 pre-check and needs that run's trajectory JSON uploaded as a file. It looks at how the strongest available model actually behaved — where it stalled, what it missed, how many calls it took.

| A HARDNESS VERDICT IS NOT THE DIFFICULTY GATE The real bands are measured later, off the six baseline rollouts. And if Opus solved the task cleanly on the first attempt, the answer is to make the task harder — not to re-run the eval. |
| :---- |

### **/oe — does your solution path work?**

It checks completeness (full critical path, key discovery steps, dependencies, every required write, and no description of what the final response should say) and accuracy (services match where the data lives, parameters and expected data match the universe, and following the events literally produces a correct trajectory). The full treatment is in the **Oracle Events** guideline.

### **/rubric — an audit, not a generator \[Changed 09/26\]**

The draft-generating mode is gone and rubric prefill is switched off, because rubric criteria must be human-written. **The Criteria Builder opens empty and stays that way until you fill it.** An empty builder is the expected state, not a bug.

The audit checks that every prompt requirement has a criterion; that each criterion makes one verifiable claim with no duplicates; that phrasing is agent-centric and affirmative with no tool names; that weights are 1, 3 or 5 and set by difficulty; and that there is at least one Outcome rubric with Process under half the set.

## **6 · The mistakes that cost a cycle**

| Mistake | What happens |
| :---- | :---- |
| Clicking Capture Files once per command in a paired run | Unnecessary, and the most common misstep in the flow |
| Clicking Save twice because it looked stuck | A missing report and a NOT EVALUATED verdict |
| Navigating away while Save is still running | Same — the verdict never appears |
| Re-running a FAIL without changing the artifact | The same FAIL, a cycle later |
| Running /hardness without uploading the trajectory JSON | NOT EVALUATED, and a re-run with the upload |
| Pasting a tidied-up version of the prompt | A verdict on a task you are not building |
| Chasing PASS after a NON-FAIL | A wasted cycle; NON-FAIL already passed |
| Using the sandbox to draft a prompt, an OE or a rubric | A spec violation, independent of what the evals say |

## **7 · The whole thing in seven lines**

| One sandbox. Provisioned for you. No /setup. Five commands: /injection  /prompt  /hardness  /rubric  /oe Run \-\> Capture Files \-\> Save \-\> verdict. Every time. Save takes a few seconds. Wait for it. Paired runs: two chats, both at once, capture ONCE. PASS and NON-FAIL both pass. FAIL blocks, with no override. Query the universe here. Never write your task here. |
| :---- |

| WHERE THE LIVE TASK SCREENS STILL SAY OTHERWISE Both Run Evals steps are titled “in Sandbox 1” and point you to “Eval Sandbox 1”. There is only one sandbox; the numbering is a leftover from the four-sandbox flow. The /prompt paste list also mentions dynamic context, which no longer exists in the V2 flow, so there is nothing to paste for it. The /rubric chat in the Run Evals step lists no paste items — use the list in section 2 above. |
| :---- |

