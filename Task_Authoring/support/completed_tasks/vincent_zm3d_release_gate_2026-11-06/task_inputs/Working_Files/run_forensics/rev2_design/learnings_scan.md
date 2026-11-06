# Learnings, completed tasks and guidelines for the rev2 store-version fix

The subagent ran out of steps before it could write this file, so the lead recorded its findings. Source: `/Users/sumitkumar/Source/Outlier/OC/learnings` (the root learnings file); the plans file has almost nothing on coherence.

## 1. Learnings that apply
- **§24 (l.205–208), checklist #18:** fix the whole class, not just the instances the finding names. Here that means every place that carries the version label: four table cells, the repro line, and the docs, generators and slot B01 that repeat it.
- **§25 (l.210–213):** `/prompt` re-reads the same records for forks and coherence, with four blind passes. Run the fork sweep before submitting, and store each revision the platform reviewed.
- **§49 (l.526–546), §51 (l.555–566):** seeded notes must agree with the base, not only with each other. Read the known-data-issue cards; base_claims checks branch names only.
- **§39 (l.372–380), #13:** after any truth or text change, grep every artifact for the old strings.
- **#6 and #15:** the rules belong in the records, not the prompt. Any account where two rule sentences disagree is a fork; here that is Leonard's "every ZM store submission from now on" against iOS #49.
- **§55 (l.616):** a new record can trip an old solver heuristic. Prefer edits over new records.

## 2. Completed-task precedents
- **julia_zm_difficulty_baseline:** an injected mail says "The store builds players have today are iOS 0.3.49 (Leonard released it yesterday) and Android 0.3.133". It passed `/prompt` (r12–r14).
- **douglas_beta_server_signoff:** a version label on a record whose base state disagreed was a Major coherence finding. It was fixed by deleting the comments (`_1_prompt (2).md:34`).
- **arthur_sunset_delivery_plan:** a PR body naming things that weren't in the base code was fixed by rewriting it to name only base-proven things. Coherence went from 3 to 5.

## 3. Known data issues (synthcut)
- **SC-19:** Slack releases are 0.3.x, also called 1.3.x, so there are two version schemes. Don't unify them; remove the uncorroborated string.
- **SC-45, SC-56, SC-67:** the base's own build labels are inconsistent, so any new label must be corroborated.

## 4. Hardness constraints to keep
- `Hardness_Mastery.md:889–890`: one trap per fact; don't stack.
- `:894`: every build number maps back through records the persona can see.
- `:909–910`: RULE_IN_PROMPT, so nothing goes into the prompt.
- Keep the update-path FAIL exactly as findable as it is now: same doc, same owner, same date, no new pointer.
- Keep the new-ticket ask fair: the runbook's "File the bug with device, OS version, source build and repro steps" must still be answerable from the doc.

## 5. Checklist for this fix
1. Remove the uncorroborated version string; don't rename it to another unbacked number.
2. If a number stays, it must be one the base backs up (iOS 0.3.49 per C0880U9751A/463).
3. Sweep the whole class in one pass: the doc's cells and repro line, B01, the design, dossier and brief.
4. Fix Leonard's cadence sentence so it doesn't claim a gate for every store submission.
5. Add nothing to the prompt.
6. Add no new deciding record and no second pointer.
7. Afterwards, grep every artifact for `1.3.24`, "current store build" and "before the hotfix", then re-run every gate.
