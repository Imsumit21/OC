# Normalized replay of the rev6 pre-check

Derived copy, for tool corroboration only. It is not an export, and the grading of record stays the hand adjudication in `../review/surface_adjudication.md`.

Changes made to a scratch copy of event 463's `values`, nothing else:
1. The 22 payee labels were replaced by the surface's truth keys (`map.json`).
2. Total rows had their Bucket blanked, so they do not count as payees; the JPMorgan bucket "None (own accounts)" was written as "Not a cost".
3. Integer amount cells were written as floats, because the tools compared integer strings unequal to float truth.

Result: `nv.json` gives RET LANDED on MotMot, CH-RET FAILED, go-rule count 1, all controls HELD. `sg.json` gives the proxy score. The same hand-graded failures appear, apart from the known D1, D2, D4 surface pins and C1's false pass.
