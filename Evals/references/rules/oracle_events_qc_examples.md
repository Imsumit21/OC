# OE review examples from QC

These examples supplement `oracle-events-v2` completeness and accuracy checks.
They come from a user-supplied export of historical QC feedback: **39 criterion
flags, 32 task/attempt pairs, 31 tasks**, across Brookfield, MoveOps, Keystone and
Star PM. The original OE artifacts/universes were not re-audited here. Names,
parameters and IDs below are historical examples, not HarmonyGames contracts.

The [case file](oracle_events_qc_cases.json) preserves each reported selection,
justification, task/attempt/audit ID, source CSV row and source hash. It excludes
worker/auditor email addresses. The source CSV is
`ea_advanced_qc_oe_nonfail_2026-09-25.csv`. Selected Non-Fail options score 3;
they are defects under these OE dimensions, not a FAIL band. Missing justification
stays an unexplained historical flag, not an invented new check.

## Apply these checks when relevant

Use the matching step checks, coverage entries and path model already required
by Eval 2. No additional user input, JSON authoring format or rubric is required.
For each material issue, show the OE passage, actual task/source/tool evidence
and its consequence. Use this table as a review aid, not a fixed error quota.

| Pattern | Historical example | What to verify now |
|---|---|---|
| Discovery before ID use | …354f4 uses `je_6b82ce3a71dc4a83` without saying how it is found. | A material existing ID must come from the prompt, a discoverable record or an earlier step. An exact ID is not compulsory when a supported search uniquely finds it. Check `dependencies` and coverage. |
| Tool arguments and their meaning | …10ace supplies an email ID to an email-search query; …86e1b uses database column `assignee_id` as tool argument `assignee`. | Match the task's actual API schema and the argument's meaning. A string can have the correct type but be the wrong kind of input. Preserve supported aliases and distinguish harmless descriptive shorthand from a broken literal call. Check `tool_service` and `parameters`. |
| Material defaults and limits | …2ec97 expects a Sent-folder message from a search that defaults to Inbox; …4f0d2 says a listing tool accepts a filter it lacks. | Verify folder/mailbox, default date window, pagination, limits and server-side versus subsequent local filtering when they affect retrieval. An optional API argument can be necessary for this task. Unavailable default behavior stays unresolved. |
| Service-specific identity | …dafd9f expects CRM object IDs from Contacts; …9cb35 pairs a loan number with the wrong borrower. | Verify the same entity and the correct service's ID namespace across joins and subsequent actions. Similar names or matching string types do not prove identity. Use source selections and downstream bindings. |
| Required population and joins | …9cb35 checks only problem loans although the ask covers every active loan; …52957 omits owner mapping and deduplication. | Derive the full requested population before filtering. Explain joins, keys, status-history deduplication, units, time windows and aggregates needed for the result. Rubric spot-checking does not permit a solver to skip requested records. Check coverage, `information`, `expected_data` and dependencies. |
| Every required action | …52977 mentions owed cost breakdowns but omits the requested calendar block; …4f0bb omits a record update. | Map each authorized action to an executing step. Mentioning an issue or retrieving its source does not perform its required write. Establish why the task requires the write before calling it missing. |
| Actual completion and offered branches | …52977 offers `create_draft` as a completed email delivery; …2ec9e says update status OR add a note where both may be required. | A draft, preview or prepared object does not prove sending, publishing or applying. Audit each branch explicitly advertised as sufficient, including its preconditions and required end state. One valid path is enough; optional alternatives need not be invented. Any AND/OR defect must follow the actual prompt/incorporated instructions. |
| Action ownership | …10aed turns the user's “I'll post an update … and send Harry a summary” into Agent actions. | Distinguish Agent requests from the user's own promised actions and background narrative. Bind each proposed write and recipient to prompt authority. An OE cannot create permission or an obligation. |
| Time, lifecycle and state | …3d7b9f treats later duplicates as disproving an earlier backfill; …10af3 copies a settled bill's zero balance onto a newly created unpaid bill. | Keep the relevant time and entity lifecycle aligned. Check current versus historical status, proposed versus completed work, current source state versus expected state after creation/update, and null versus a real status. A real record can still be the wrong comparison. |
| Grounded expected data | …1fbba expects 16 bills/$21,000 while the auditor reports 5 bills/$19,500; …2ec9b cites the wrong author/date. | Reproduce material counts and totals from the effective data/injection and verify authors, dates, IDs and state. Intended injections and prior runs do not establish the effective universe. An unverified record absence remains unresolved. |
| Expected findings, not vague verbs | …965fa7 says “cross-reference the amounts” without the important finding. | State what retrieval or calculation is expected to establish, with task-relevant values or a supported absence result. This is Expected Data, not a script for what the final response should say. |
| Absence, exclusivity and designed gaps | …965fae calls a normally absent CRM deal a tracking defect and prescribes a write; …965fa7 says a contact exists only in CRM although another valid source has it. | Verify the applicable relationship/design before declaring a missing record erroneous. Use scoped absence evidence, including relevant attachments. A false “only” claim and the feasibility of its otherwise valid lookup are separate questions. Do not infer a needed repair solely from a missing link. |
| Consequence and severity | …1fbbd misstates how many trap values are wrong while its actual steps and values remain correct. | Explain whether the imprecision changes execution/results. Preserve Minor for harmless imprecision and Inaccurate for wrong existing steps/expected data with consequential errors. Do not import inconsistent historical labels as new rules. |

## Avoid false alarms when using this corpus

- **No blanket hardcoded-ID requirement.** The feedback for CSV row 13 asks for
  missing IDs and repeats one ID. A valid discovery path may satisfy the need;
  the complete original OEs are required to settle that historical judgment.
- **Use current service evidence.** Namespaces, wrappers and aliases vary across
  these universes. Verify the current schema before declaring a tool nonexistent
  or rejecting a prefix. The bundled flat catalog does not capture every default
  or semantic capability; establish those separately when material.
- **Keep scope and dates attached to a claim.** “No record at the backfill date”
  is not contradicted by a record created afterwards. A missing relationship may
  be intentional. A new object's state need not equal an existing settled one.
- **Preserve uncertainty and category distinctions.** Some historical selections
  conflict with their prose (e.g. CSV rows 5, 19, 30, 33). Preserve the recorded
  label for provenance; determine the current finding from evidence and impact.
  CSV row 31 has no justification and supports no concrete example by itself.
- **No automatic task impossibility.** Wrong OEs may be fixable. Apply the existing
  supplied-path versus task-wide-blocker distinction. `/prompt` owns task design
  and overall feasibility; these examples do not change its report or score.

## What the helper does and what the reviewer does

`hg_oe_path.py` already checks declared tools/service membership, primitive
argument types, source-selected expected values, downstream bindings and cycles.
`hg_oe_review.py` scores recorded missing, inaccurate and minor findings. Neither
extracts every obligation from prose or proves query meaning, tool effects,
population completeness, chronology, intended relationships or arbitrary joins.
Those require the explicit evidence review above. Record the result in the
existing step/coverage checks; do not call catalog validation a complete audit.
These are sourced review examples, not 39 independently replayed regression tests.
