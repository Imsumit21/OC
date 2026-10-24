**Guideline — Change Log**

HarmonyGames / Original Conference guidelines ·  Update date: October  02, 2026

| SPEC V2 — READ THIS BEFORE YOUR NEXT TASK These guidelines have been updated for Spec V2. Several things you may have done on every previous task are now prohibited, and one whole stage of the task flow has been removed. Skim the table below in full; the individual guidelines carry the details. |
| :---- |

## **What changed**

| Date | Area | Earlier | Now | Note |
| :---- | :---- | :---- | :---- | :---- |
| Oct 2, 2026  | [**QC Spec Doc**](https://static.remotasks.com/uploads/6a5595596cf3031de47f0ea2/QC_Spec_Doc_V2.html) | Today’s Date \- Fixed  Universe “today” date was February 28, 2026  | Universe Today’s Date is February 14, 2026 00:00.  | Corrected the fixed universe “today” date in the Alignment with Today’s Date dimension. |
| Oct 2, 2026 | **Gate Rules** | Weighted average pass rate \<=75% Agent failure rate (Pass @1) \<= 4/6 i.e 67% | Weighted average pass rate \<=90% Agent failure rate (Pass @1) \<= 3/6 i.e 50% | Changed the gate rules as per QC Spec doc.. |
| Sept 29, 2026 | **Baseline model** | Opus 4.8 | Opus 5.5 | Both the single difficulty pre-check and all six baseline rollouts run on Opus 5.5. Selecting any other model is a failing error. |
| Sept 29, 2026 | **Who writes the prompt and the rubrics** | Not policed | Humans only | Prompts and rubric criteria must be written by you, from scratch. Using an LLM to draft or to polish either one is prohibited. Prompts are screened by an AI-text detector. |
| Sept 29, 2026 | **Rubric prefill** | /rubric generated a draft set that populated the Rubric Criteria Builder | Disabled | The builder now opens empty. /rubric is an audit of criteria you already wrote. |
| Sept 29, 2026 | **Golden solution** | Free-text golden answer, checked by /golden | Replaced by Oracle Events | You now write the key *steps* a correct agent takes, not the finished answer. Checked by /oe. See the Oracle Events guideline. |
| Sept 29, 2026 | **Hinting** | You wrote a hint, ran a second hinted trajectory, ran a second verifier, picked a silver trajectory, then scrubbed the hint | Removed from the task | Hinting is now automated and sits outside the task. Seven steps are gone. There is one agent run and one verifier. |
| Sept 29, 2026 | **Feasibility guardrail** | A hint could rescue an over-hard task | /prompt in the eval sandbox | With no hint to fall back on, the sandbox feasibility check is the only thing standing between you and an unsolvable task. Treat a FAIL there as fatal. |
| Sept 29, 2026 | **Minimum tool calls** | Average across the rollouts | The golden run, if one exists | A **golden run** is a baseline rollout that scored 100% on your rubric. If one of your six rollouts did, the horizon minimum applies to that run alone. If none did, the average across all six is used instead. Note that this is a *run the model produced* — it is not the Oracle Events set you write. |
| Sept 29, 2026 | **Horizon tiers** | Normal, Long-Horizon, Super-Long-Horizon | Normal 50% / Long-Horizon 50% | Super-Long-Horizon is **paused** in V2. It is documented but not assigned. |
| Sept 29, 2026 | **Oracle Events** | — | New required artifact | Five fields per step: Action, Information, Tool / Service, Parameters, Expected Data. |
| Sept 29, 2026 | **Rubric rules** | — | Five new prohibitions | No grading unstated expectations · no hard-coded conclusion on ambiguous evidence · grade how the agent *handles* a distractor, not the distractor · no hard-coded titles or phrasings · spot-check repetitive items instead of one criterion per row. |
| Sept 29, 2026 | **Prompt realism** | Guidance only | Enforced | An LLM-sounding prompt is the single most common rejection. Exact titles and values are fine when human-readable; opaque IDs are not. |
| Sept 29, 2026 | **Eval sandbox** | Six commands across four sandboxes | Five commands in one sandbox | /injection · /prompt · /hardness · /rubric · /oe. One sandbox, provisioned once, open all task. /golden is retired. |
| Sept 29, 2026 | **Dynamic context & sources** | A separate authoring step | Removed | The step is gone. Source and distractor design still matters — it now lives inside your Oracle Events and your scenario design. |
| Sept 29, 2026 | **Difficulty bands** | pass@1 under 40%, three distinct failure signatures | pass@k 67% · ≥2 distinct patterns · average weighted rubric score under 75% | V2 targets are bands, not points. See Common Errors and Pre-QC. |
| Sept 29, 2026 | **Scoring and promotion** | Not published | Published | Attempt layer and reviewer layer, a 1–5 task score, promotion on two consecutive 4+ tasks that reach delivery. See Overall Task Flow. |
| Sept 29, 2026 | **Support** | Ad hoc | War Room with three breakouts | Attempters, reviewers, and blockers, with QMs and CSMs focused on prompt and rubric quality. |
|  | **Documentation set** | Eleven documents | Twelve | Oracle Events is new. Taxonomy screenshots have been removed from Overall Task Flow pending a worked example built under the V2 taxonomy. |

## **What was removed outright**

If you have these in your habits or your notes, drop them. They no longer exist anywhere in the flow:

| Retired | Why |
| :---- | :---- |
| The **Hint** input | Hinting moved outside the task and is automated. |
| The **reference / hinted agent run** | There is one agent run: the baseline. |
| The **reference rubric verifier** and its all-fail rating | There is one verifier, against the baseline. |
| **Silver trajectory** selection | No second trajectory to choose between. |
| **Difficulty rating and trajectory label** | Superseded by the automatic baseline statistics. |
| **Hint cleanup** and its no\_hint\_evidence / trajectory\_still\_coherent checks | Nothing to scrub. |
| The **golden answer** field and /golden | Replaced by Oracle Events and /oe. |
| The **Dynamic Context & Sources** step | Removed from the taxonomy. |
| The **difficulty bonus** screen | Removed from the taxonomy. |
| The **NEEDS-REVISION** verdict | Retired with the /hint eval in the previous release. |

| KNOWN INCONSISTENCIES IN THE LIVE TAXONOMY Three screens in the task builder still carry text from the hinted flow and have not yet been updated. Where they conflict with this guideline set, these guidelines are correct: Verifier Instructions describes two verifiers and walks you to a hint step. There is one verifier and no hint step. Error Injection & Async Wait says the configuration applies to “all four runs… the reference-trajectory (hinted) agent run.” It applies to the baseline run and the verifier. Reference File Uploads says files are available “in both the baseline and hinted runs.” There is only the baseline run. The Task Type & Horizon screen also still shows the Super-Long-Horizon tier. That tier is paused and will not be assigned. |
| :---- |

## **Universe work in flight**

Engineering is regenerating the synthetic **Confluence** and **Snowflake** data so it matches the real Drive and Excel data, and is clearing personal information out of the artifacts. Both services remain part of the thirteen and remain valid sources for a task. When the regenerated universe lands, re-verify any Confluence or Snowflake figure you had already noted — row counts and specific values may move.