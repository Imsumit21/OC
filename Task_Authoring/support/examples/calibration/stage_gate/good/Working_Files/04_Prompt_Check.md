# Prompt Check — stage-gate-fixture
> Prompt: 04_Prompt.txt · 50 words · sha256 19c9b7220c07 · checked 2026-10-04 against 04_Prompt_Writing_Brief.md (2026-10-04)
> Report-only. No replacement wording. Typos, capitalisation and AI-likeness are not assessed (scored by /prompt §1.2).

## Summary

Fail 0 · Non-fail 0 · Advisory 1 (C20) · UNVERIFIED none · checks clean: C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C21, C22, C23, C24 · predicted /prompt band: PASS · Status: READY FOR /prompt

## Findings

| # | Check | Dimension · severity | Quoted span | Rule (source) | Defect |
|---|---|---|---|---|---|
| 1 | C20 | Today's date · Advisory | "before monday" | Prompt Writing §4.2 | relative date; resolves to 2026-02-16 only through the calendar |

## UGT readings

Deliverable 1 (schedule): Reading A = file in d_cc3e90160f490686039986; Reading B = channel post only; settled by "put the schedule in my drive folder for the sale" (same material result impossible, folder named by the persona).

## Verification log

| Span | Type | Universe record | Result |
|---|---|---|---|
| "winddown" | channel | C0ADGSZKR3R | match |
| "domino delights" | game | ENG-2280 | match |
| "leonard" | person | leonard.hayes@harmonygames.co | match |

## Brief coverage

| Brief item | Present in the prompt |
|---|---|
| §4 defect schedule | "put the schedule in my drive folder for the sale" |
| §4 hand-off note | "tell him in winddown once its there" |

## Self-review

| Check | Verdict | Strongest counter-reading | Resolution (evidence) | Unresolved |
|---|---|---|---|---|
| C1 Field limit | clean | the strongest reading that /prompt scores C1 the other way | resolved against Eval 1 §1.1 and 04_Prompt_Writing_Brief.md | none |
| C2 Assignment bound | clean | the strongest reading that /prompt scores C2 the other way | resolved against Eval 1 §1.2 and 04_Prompt_Writing_Brief.md | none |
| C3 Persona | clean | the strongest reading that /prompt scores C3 the other way | resolved against Eval 1 §1.3 and 04_Prompt_Writing_Brief.md | none |
| C4 Competency / skill | clean | the strongest reading that /prompt scores C4 the other way | resolved against Eval 1 §1.4 and 04_Prompt_Writing_Brief.md | none |
| C5 Complexity and seeding | clean | the strongest reading that /prompt scores C5 the other way | resolved against Eval 1 §1.5 and 04_Prompt_Writing_Brief.md | none |
| C6 Unique Ground Truth | clean | the strongest reading that /prompt scores C6 the other way | resolved against Eval 1 §1.6 and 04_Prompt_Writing_Brief.md | none |
| C7 Clarity | clean | the strongest reading that /prompt scores C7 the other way | resolved against Eval 1 §1.7 and 04_Prompt_Writing_Brief.md | none |
| C8 Incorporation | clean | the strongest reading that /prompt scores C8 the other way | resolved against Eval 1 §1.8 and 04_Prompt_Writing_Brief.md | none |
| C9 Pre-solved | clean | the strongest reading that /prompt scores C9 the other way | resolved against Eval 1 §2.1 and 04_Prompt_Writing_Brief.md | none |
| C10 Discovery collapse | clean | the strongest reading that /prompt scores C10 the other way | resolved against Eval 1 §2.2 and 04_Prompt_Writing_Brief.md | none |
| C11 Investigation to action | clean | the strongest reading that /prompt scores C11 the other way | resolved against Eval 1 §2.3 and 04_Prompt_Writing_Brief.md | none |
| C12 Tool use and cross-service | clean | the strongest reading that /prompt scores C12 the other way | resolved against Eval 1 §2.4 and 04_Prompt_Writing_Brief.md | none |
| C13 Coherence | clean | the strongest reading that /prompt scores C13 the other way | resolved against Eval 1 §2.5 and 04_Prompt_Writing_Brief.md | none |
| C14 Tool mention | clean | the strongest reading that /prompt scores C14 the other way | resolved against Eval 1 §2.6 and 04_Prompt_Writing_Brief.md | none |
| C15 Command list | clean | the strongest reading that /prompt scores C15 the other way | resolved against Eval 1 §2.7 and 04_Prompt_Writing_Brief.md | none |
| C16 Contrived register | clean | the strongest reading that /prompt scores C16 the other way | resolved against Eval 1 §2.8 and 04_Prompt_Writing_Brief.md | none |
| C17 Truthfulness | clean | the strongest reading that /prompt scores C17 the other way | resolved against Eval 1 §3.1 and 04_Prompt_Writing_Brief.md | none |
| C18 Feasibility | clean | the strongest reading that /prompt scores C18 the other way | resolved against Eval 1 §3.2 and 04_Prompt_Writing_Brief.md | none |
| C19 Persona ACL | clean | the strongest reading that /prompt scores C19 the other way | resolved against Eval 1 §3.3 and 04_Prompt_Writing_Brief.md | none |
| C20 Today's date | Advisory | the strongest reading that /prompt scores C20 the other way | resolved against Eval 1 §3.4 and 04_Prompt_Writing_Brief.md | none |
| C21 Injected friction | clean | the strongest reading that /prompt scores C21 the other way | resolved against Eval 1 §3.5 and 04_Prompt_Writing_Brief.md | none |
| C22 Universe coherence | clean | the strongest reading that /prompt scores C22 the other way | resolved against Eval 1 §3.6 and 04_Prompt_Writing_Brief.md | none |
| C23 Originality | clean | the strongest reading that /prompt scores C23 the other way | resolved against Eval 1 §3.7 and 04_Prompt_Writing_Brief.md | none |
| C24 Diversity | clean | the strongest reading that /prompt scores C24 the other way | resolved against Eval 1 §3.8 and 04_Prompt_Writing_Brief.md | none |

No-transcribable-sentence pass: zero hits outside quoted prompt spans; prompt hash unchanged (19c9b7220c07).

Unresolved: none.

```
STAGE GATE prompt-check: PASS — Task_Authoring/support/local_search/cache/stage_gate_selftest/gen · 04_Prompt_Check.md#768fb7a25f6f · 04_Prompt.txt#19c9b7220c07 · blocking 0 · warnings 0 · checks 21
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Check.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 04_Prompt_Writing_Brief.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 04_Prompt_Writing_Brief.md)
[PASS] chain.prompt-writing: upstream 'prompt-writing' PASS pasted and current (04_Prompt_Writing_Brief.md#b2e5ff44a81f)
[PASS] structure.sections: 7 required sections present and non-empty (04_Prompt_Check.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Check.md
[PASS] structure.prompt_hash: header ties the report to 04_Prompt.txt (50 words, sha256 19c9b7220c07)
[PASS] evidence.quoted_spans: 1 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] evidence.coverage_spans: 2 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] structure.c_checks: every C1–C24 has a recorded result
[PASS] evidence.verification_log: 3/3 items carry a source pointer (min 100%)
[PASS] structure.summary_band: summary band present
[PASS] structure.summary_status: summary status present
[PASS] tier.hardness: Long Horizon → --profile extreme: manifest present, hardness_gate PASS pasted in the dossier and current
[SKIP] tier.hardness_rerun: hardness_gate --profile extreme re-run skipped (--rerun lint)
[PASS] boundary.replacement+prompt_phrases: human-only boundary clean in 04_Prompt_Check.md (replacement, prompt_phrases)
[PASS] boundary.advice+typo: human-only boundary clean in 04_Prompt_Check.md (advice, typo)
[PASS] review.counter_readings: 24 evidenced counter-readings (of 24 found; need ≥ 24) in 04_Prompt_Check.md
[PASS] review.coverage: self-review addresses all 25 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```








## Route

No Fail: paste 04_Prompt.txt exactly as saved into /prompt, paired with /injection.
