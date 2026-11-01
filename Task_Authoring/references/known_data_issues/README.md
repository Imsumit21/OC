# Known data issues per universe (do not grade, do not depend on)

`normal.md` (NB-1–NB-33, Feb 14, 2026 universe) and `synthcut.md` (SC-1–SC-73, Oct 1, 2025 universe) list base-data
conflicts that reviewers have already failed tasks on, sorted by FAILs caused. Received 2026-11-01. The Portal's
`/prompt` and `/injection` cite the same cards as `known_base_issues.md`; the local `Evals/` bundle does not ship
them, so this folder is the authoring copy.

How the stages use them:
- **Scenario / injection:** no load-bearing fact, trap, Oracle Event or rubric row may depend on a listed item. When a
  task touches one, use the card's "Safer" alternative or a field the card does not name, and cite the card id in the
  dossier's coherence audit ("touched: SC-43 — not graded; pool uses ledger rows as-is").
- **Prompt:** never ask for a value a card says not to grade.
- **Oracle Events / rubric:** never put a "Don't grade" value on an `Expected:` line or in a criterion.
- `watch` cards are not always a fail: check both sides and record which one the task relies on and why.
- An injection must not "fix" a listed conflict silently: either avoid it or repair it per
  `references/Hardness_Manifest_Spec.md` `hazard_acknowledgements` (`resolution: repaired`).
