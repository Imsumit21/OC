# Current-tree verification re-run (not the stale round1 logs)

Tree: tools last edited 2026-10-26 01:08; bundles rebuilt from the current tree; round1 logs (23:31) are stale and
are marked "fixed, log stale" where applicable, never "accepted limitation".

| Bundle | Tier | Verdict | Verified by | Notes |
|---|---|---|---|---|
| code_g1 | code | **UNKNOWN** (rejected) | — | both providers unavailable: "Generation credentials are unavailable"; claude-opus-5-5 hold timeout. UNKNOWN is not passed. |
| code_h1 | code | **FAIL** | openai/gpt-6.1-sol#max | 3 findings: control subtraction removes unrelated mechanism evidence and keeps stale provenance; channel proposals misattribute known HELD / unknown FAILED provenance; reference_landed uses a different class-attribution contract. |
| code_f1 | code | **UNKNOWN** (rejected) | — | both providers unavailable (credentials / hold timeout). UNKNOWN is not passed. |
| code_misc | code | **FAIL** | openai/gpt-6.1-sol#max | control ablation-equality check runs on every control, not only the moved ones; the supplied artifacts did not include the `surface.gradeable` hunk (bundle was built before that addition). |
| redteam_grading | redteam | **FAIL** | openai/gpt-6.1-sol#max | surviving: cohort-range endpoints contaminate group membership; Oxford-comma and backticked key lists; colon-terminated list items end the section; `test`/move-to-self patches; a named-group key regex crashes the decoder; `text` selectors read nested identifiers; wrapped email IDs fail. |
| redteam_attribution | redteam | **UNKNOWN** (rejected) | — | both providers unavailable. UNKNOWN is not passed. |
| redteam_forecast | redteam | **FAIL** | openai/gpt-6.1-sol#max | surviving: rate unit can be consumed by a different latent; dropped provenance disappears when every record is dropped and unrelated drops can attach; `inf` Beta parameters accepted; a known but irrelevant brief key bypasses the keyless guard; theta=1 sampler picks one batch; top-25 slot truncation. |
| methodology | methodology | not run this round | — | claims updated but no final methodology verdict on the current tree. |

Round-1 findings that the current code fixes are recorded as **fixed, log stale** (the old FAILs are not reopened):
G1 decoder defects, declared-ungradable gates, replay/replace semantics, register identity, delivery binding, entry
tail, exact issue match, range-endpoint Counter; H1 seeded supersession/revision, observation collapse, rho, key-event
deciders, unknown decisions, class equality, observation/verdict coexistence; F1 rate units by latent, revision keys,
exact batch sampler, mechanism guard; M5 golden scan completeness; M7 WARN cases; V1 empty/null labels; WT scratch
temp folders; E2E exact proposal/rate assertions.

Local acceptance on this tree: E2E 14/14; suite 14/14; falsify_g1 28/28 planted cases and 12/12 fixtures; falsify_h1
PASS; rev13 0 differences (truth and solver); rev14 failed sets of record; A17/A15/A7 priors exact; c05 two known seed
differences with SP-039 pending.
