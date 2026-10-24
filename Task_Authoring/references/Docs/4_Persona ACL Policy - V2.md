**Persona ACL Policy**

*What your assigned persona can read, what it can write, and how to build an Access Control task that is difficult rather than broken.*

## **Change log**

| Date | Updates |
| :---- | :---- |
| Sep 26, 2026 | Rewritten for Spec V2. Hint-based recovery paths removed. Confluence and Snowflake flagged as unclassified. Oracle Events replace golden-solution references. Taxonomy screenshots removed. |
| Aug 2026 | Original release. |

## **1 · Quick reference**

| Question | Answer |
| :---- | :---- |
| Can I switch to a different persona? | No. The assigned persona is fixed. Switching is a failing error |
| Does the ACL restrict what the agent can write? | No. Writes are governed by the tool catalog only |
| Does knowing a record's ID bypass the ACL? | No. A denied by-ID read returns “not found” |
| Can I build the task on something only I can see? | No. Universe Explorer is author god-mode |
| Does the verifier see more than the agent? | No. Both use the persona's scoped view |
| Are Confluence and Snowflake scoped? | Unclassified. Check from the persona's view before you rely on either |

## **2 · Purpose and authority**

Every task is assigned a persona. That persona is not decoration. It does three things at once:

1. **It sets the voice.** The prompt has to read as something that person would plausibly send. A prompt that could not have come from your persona is a failing error, scored under assignment alignment.  
2. **It sets the remit.** An artist asking for a cap-table revision strains credulity even if the competency is Finance; find the version of the assigned work that person would genuinely be pulled into.  
3. **It sets the ACL.** It determines which records the agent is permitted to read, and therefore what is and is not solvable.

The third one is the reason this document exists. The first two are covered in the **Prompt Writing** guideline.

## **3 · Service access matrix**

| Service | Class | Read behaviour for the agent |
| :---- | :---- | :---- |
| **GitHub** | Unscoped | All repositories, pull requests, reviews and release history are visible to every persona |
| **Linear** | Unscoped | All issues, projects and cycles are visible |
| **Trello** | Unscoped | All boards, lists and cards are visible |
| **Contacts** | Unscoped | All people, roles and addresses are visible |
| **Gmail** | Scoped | Only mail the persona sent, received or was copied on |
| **Slack** | Scoped | Only channels the persona is a member of, and only DMs it is party to |
| **Google Calendar** | Scoped | Only the persona's own calendar and events it is invited to |
| **Google Drive** | Scoped | Only files and folders shared with the persona |
| **Google Docs** | Scoped | Inherits Drive sharing |
| **Google Sheets** | Scoped | Inherits Drive sharing |
| **Google Slides** | Scoped | Inherits Drive sharing |
| **Confluence** | Unclassified | Not named in either column. Verify from the persona's view |
| **Snowflake** | Unclassified | Not named in either column. Verify from the persona's view |

| THE TWO UNCLASSIFIED SERVICES Confluence and Snowflake are fully in scope as task sources, and the ML-selected example task depends on both. They are simply not named in the policy's scoped/unscoped table. Until that is resolved, treat them as verify before you depend on them: open the specific page or table from the assigned persona's view and confirm it returns data. Do not assume either behaviour. |
| :---- |

## **4 · Scoped read behaviour**

On a scoped service, the filter applies to every read path, not just to browsing.

| Call | Behaviour |
| :---- | :---- |
| list | Returns only records within the persona's scope |
| search | Searches only within the persona's scope. A match outside it does not appear |
| Read by ID | Returns the record if it is in scope, and **“not found”** if it is not |

| “NOT FOUND” IS THE DENIAL MESSAGE The agent is never told that a record exists but is off-limits. It is told the record does not exist. That is what makes Access Control a genuinely hard characteristic — and it is also why a task that quietly depends on an unreadable record looks, to everyone downstream, like a task whose evidence simply is not there. |
| :---- |

## **5 · Writes are not governed by the ACL**

This is the single most common misunderstanding in this document.

* What the agent may **write** is determined by the tool catalog available to the task, not by the persona's read scope.  
* A persona who cannot read a particular Drive folder may still be able to create a document. A persona with no visibility into a Slack channel may still be able to post to one it is in.  
* Do not reason from “my persona can't see this” to “my persona can't write here”. Check the catalog.  
* Equally, do not write a rubric requiring a write action the catalog does not support. That criterion is unpassable and will show up as an invalid all-fail.

## **6 · Universe Explorer is author god-mode**

Universe Explorer shows you the whole universe regardless of persona. It is a build tool. It is not what the agent sees, and it is not what the verifier sees.

| If you build on something only you can see… | …this is what happens |
| :---- | :---- |
| The evidence is in a doc not shared with your persona | The agent cannot reach it. Every rubric depending on it fails all six rollouts, and every one of those all-fails is invalid |
| You cite the record ID in the prompt to help | It does not help. A denied by-ID read still returns “not found”, and now the prompt also names an ID a real person would not know |
| You assume the verifier will check it anyway | It will not. The verifier uses the same scoped view |

**The check:** for every piece of evidence your task depends on, open it from the assigned persona's view and confirm it returns. Do this before you write the prompt, not after the baseline comes back.

## **7 · Building a good Access Control task**

Access Control is one of the six stackable task characteristics. Done well, it tests whether the agent recognises a boundary and works with it. Done badly, it produces a task that is simply missing its evidence.

**✓**  The information the agent needs is reachable, but **not by the first obvious route**. A restricted doc is summarised in a channel the persona is in.

**✓**  The agent has to notice that a source it expected to exist is not visible, and find the equivalent elsewhere.

**✓**  The correct behaviour is to escalate — to ask the person who does have access — and the prompt makes that a reasonable action.

**✗**  The only copy of a required figure sits behind the boundary. The task is not hard, it is impossible.

**✗**  A rubric requires the agent to state that a specific document exists but is restricted. It cannot know that; it was told the document does not exist.

**✗**  The boundary is invisible in the trajectory — nothing the agent does reveals whether it encountered the ACL at all.

### **Always name the alternative path**

Before you finalise an Access Control task, write down the route a correct agent takes when the primary source is unavailable, confirm that route exists in the universe, and put it in your Oracle Events as an explicit step. If you cannot name it, you have built an unsolvable task.

| THERE IS NO HINT TO RESCUE IT Under the previous spec a hint could unblock an agent that had run into an unforeseen boundary. Hinting has been removed from the task. The /prompt feasibility check in the eval sandbox is now the only guardrail before the baseline, so treat a FAIL there as fatal rather than advisory. |
| :---- |

## **8 · ACL and forced errors do not mix**

A forced tool error on a scoped service is **indistinguishable from an ACL denial** from the agent's point of view. Both come back as a failure to retrieve.

* If your task depends on the agent reasoning about *why* it cannot see something, do not also force an error on that tool.  
* If you want to test error recovery, prefer an unscoped service — GitHub, Linear, Trello or Contacts — where the ACL is not also filtering the result. The signal is much cleaner.  
* An error rate of 1.0 means the tool fails on every call. A retry will never succeed, so a rubric expecting a successful retry on that tool is unpassable.

## **9 · How ACL mistakes are scored**

| Defect | Severity | Where it surfaces |
| :---- | :---- | :---- |
| The prompt could not plausibly have been written by the assigned persona | Fail | Assignment alignment |
| Using a persona other than the one assigned | Fail | Assignment alignment |
| The task requires reading something the persona cannot read | Fail | Prompt feasibility — usually caught by /prompt |
| A rubric depends on evidence outside the persona's scope | Fail | Invalid all-fail rubrics, two or more of which fails the task |
| A rubric requires the agent to describe a restriction it was never shown | Moderate | Unauthorized rubric criterion |
| The prompt names a record ID the persona would not know | Moderate | Contrived prompt |

## **10 · Before you leave the persona step**

* You are using the persona you were assigned.  
* The prompt reads as something that person would actually send, about work they would actually be pulled into.  
* Every piece of evidence the task depends on has been opened from the persona's view and confirmed readable.  
* If Confluence or Snowflake is on the critical path, you have verified access specifically, not assumed it.  
* Every write action the task requires is supported by the tool catalog.  
* If you injected an error, it is not on a scoped service whose denial the agent is meant to reason about.  
* If the task has an access boundary, the alternative path exists, you have named it, and it appears in your Oracle Events.

