# Blind comparison — prompt check vs QC labels

Label set: `Evals/references/rules/prompt_qc_cases.json`, 25 cards / 24 tasks, Jun–Jul 2026, four
non-HarmonyGames universes, scored on the pre-Spec-V2 QC form (no ACL, no spec-sheet gate, MCP-server
mention = Non-fail). Every card carries ≥ 1 flag: 10 FAIL, 15 flagged-non-fail, **0 clean** → the set
measures recall and severity, not precision. Universes are absent → Truthfulness / Feasibility /
universe-rooted UGT flags are judged text-only (span listed as UNVERIFIED = detected).
16 cards had their flag topic disclosed in `prompt_qc_examples.md` (required reading) → "lead".

## Verdict level

| Card | Label | v0 | v1 (blind) | v2 (post-fix re-run) | Class |
|---|---|---|---|---|---|
| 64 | FAIL UGT | F | F | F | ok |
| 65 | FAIL UGT (promised call, no time) | F | F | F | ok |
| 66 | FAIL UGT (cross-service joins) | NF | F | F | ok (v1 via command list) |
| 67 | FAIL UGT (no reason) | F | F | F | ok |
| 68 | FAIL minor factual ×2 | F | F | NF | D universe-only (phantom email) |
| 69 | FAIL ADA (two boards) | F | F | F | ok |
| 70 | FAIL ADA (now vs after approval) | F | F | F | ok |
| 71 | FAIL UGT ($8,400 conflict) | F | F | NF | D universe-only |
| 72 | FAIL Feasibility (no reason) | F | F | F | ok (via pre-solved) |
| 73 | FAIL ADA | F | F | F | ok |
| 74 | NF minor clarity | P | P | NF | H unpinned detail not reported |
| 75 | NF minor factual | NF | NF | NF | ok |
| 76 | NF minor clarity | F | F | NF | A clarity over-severity |
| 77 | NF MCP server (product names) | NF | NF | NF | F older rule (flag itself not reproduced) |
| 78 | NF minor clarity | NF | NF | NF | ok |
| 79 | NF minor clarity | F | F | NF | A clarity over-severity |
| 80 | NF minor clarity + minor factual | F | F | F | C Evals stricter (spec-sheet ≥ 2) — label older rules |
| 81 | NF minor clarity | F | F | NF | A ("I'll" already resolved by v1 text; applier over-read) |
| 82 | NF minor factual | P | P | NF | H + D |
| 83 | NF factual + BF + persona | F | F | NF | A (delegated discretion) |
| 84 | NF persona | F | F | P | B bolt-on over-call; G persona unverifiable |
| 85 | NF minor clarity | NF | NF | NF | ok |
| 86 | NF minor clarity | P | P | NF | H |
| 87 | NF factual + clarity | NF | F | NF | E command-list over-call |
| 88 | NF minor clarity | F | F | NF | A |

Agreement: v0 14/25 · **v1 14/25 (56%)** · **v2 21/25 (84%)**. Lead-free subset (9): v1 4/9 → v2 9/9;
lead subset (16): v1 10/16 → v2 12/16. v2 is a post-hoc re-run of the fixed rules (not blind).

## Flag level (17 text-judgeable label flags; 12 need the absent universe)

Dimension match: v1 11/17 → v2 15/17. Dimension + severity band: v1 8/17 → v2 15/17.
Unmatched after v2: 77 (product names — older rule, not reproduced by design), 80a (final-response
contents ambiguity; the check raises spec-sheet Contrived on the same paragraph instead).
Universe-only flags (12): every span is in the C17 verification list (detected as UNVERIFIED) except
66 (join reliability), 72 (no explanation), 83/84 persona/BF fit.

## Disagreement classes

- A — Clarity over-severity (76, 79, 81, 83, 88): Fail called on a vague verb with no competing concrete write; QC scores these Minor. Playbook fix (C7).
- B — Bolt-on over-call (65, 69, 71, 84): asks tied to one review/deadline are stacking, not bolt-ons (QC Coherence pass text). Playbook fix (C13).
- C — Spec-sheet / command-list Contrived never flagged by labels (66, 72, 80): Evals §2.7 gate is stricter than the July QC form. Label older rules; kept.
- D — Universe-only (66, 68, 71, 72, 75, 80b, 82, 83): not measurable text-only; covered by C17/C6 when run against a universe. Added narrative/background premises and join reliability.
- E — Command-list over-call on a single check-before-acting step (87). Playbook fix (C15).
- F — MCP/product names (77): label used the retired reading; current rule (prompt_qc_examples, row 103) keeps product names clean. No change.
- G — Persona "fits another better" (83, 84): needs org-role evidence; C3 covers it.
- H — Unpinned channel/time/detail reported as clean (74, 82, 86): QC scores Minor clarity (Non-fail). Playbook fix (C7: report each unpinned detail).
