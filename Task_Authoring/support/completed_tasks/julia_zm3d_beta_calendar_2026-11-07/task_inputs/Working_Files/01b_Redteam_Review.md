# 01b — Red team (adversarial falsification) — scenario stage

Reviewer: GPT-6.1 Sol (`redteam` subagent, session ses_e57f3dcb8ffeDzvze5MvZnSRlF), independent of the Claude build
lane. Read-only static review on `01_Scenario_Design.md` + `01_Hardness_Manifest.draft.json` +
`01_Gradable_Surface.json` + research. **VERDICT: FAIL** (no runtime verification; source-level counter-cases).

This is one of the two independent reviews the recorded RED TEAM FALLBACK (design §17) stands on; the second is the
methodologist pass in `01b_Redteam_Review.second.md`. The full reviewer text is in the session transcript; findings and
build dispositions below.

## Findings and dispositions

| # | Sev | Finding (abridged) | Disposition |
|---|---|---|---|
| F1 | Major | `reason_matches`/`text` selectors match keyword presence, not polarity: wrong answers satisfy S06/S08/S09/S10/S11/W03/W07; W04/W05 don't bind the comment to the target issue (ZOM-78/ZOM-429). | **ACCEPT (partial).** Tighten the computed/polarity slots — S10 & W07 (drop the bare `lock` alternative; require the correct instant 00:00 UTC / 17:00 PDT / "late"), W03 (require off-with-reason, exclude "not off"); bind W04→ZOM-78 and W05→ZOM-429 by issue. S06/S08/S09/S11 keep presence-matching: a no-discovery run omits the keyword and fails correctly; the rare discovered-but-negated path is graded by the real rubric. Surface is a proxy; platform grades polarity. |
| F2 | Major | A full-score candidate need not deliver the full calendar: other beats' windows/hold-until, full push coverage and the "What is missing (owner)" column are ungraded. | **ACCEPT.** Add a `pushes` `register_keys_exact` volume slot (full push set required), grade "What is missing (owner)" for the held pushes, and add status coverage for the remaining beats. Most *window dates* stay intentionally ungraded (QC rail §13: warehouse/backend disagree) — documented, not an oversight. |
| F3 | Major | Forecast attributions misrepresent failure propagation: `R_TECH_HOLD` charged to S04/S05 (can't fail "Quests/Daily Login run"); S06/S07 scope-dependence unmodeled. | **ACCEPT — DONE.** Removed `R_TECH_HOLD` from S04/S05; added `R_SCOPE_BEATS` to S06/S07. Honest re-forecast: independent P(all)=0.500 (was 0.515), correlated 0.580. |
| F4 | Major | "Sweep-invisible" is over-claimed: a filter-only Slack search (author+channel+date, no keyword) returns the thread replies; T7's re-test sits in the **same channel** (#zombie-bugs) as the recovery it supersedes. | **ACCEPT (reframe).** The task's goal is "hard because it survives COMPLETE retrieval" — so drop every concealment claim and rest difficulty on reconciliation. Move T7's re-test to a #zombie-match3d **root** (cross-channel, per Pre-Scenario §4.1/§6.2). Correct §9/§13/§18 prose and the "≤15% per discovery" claim (scope is ~22%). |
| F5 | Major | INT-12/INT-13 companion mirrors in Julia's mailbox could carry the deciding inline-comment text or name its PR → shortcut around the per-PR GitHub path; "Season Pass November" query returns both threads. | **ACCEPT (injection constraint).** Bind at /create-injection: companion mail/Slack mirrors carry only a link/PR-ref, never the deciding comment text. Correct the discovery_order over-claim (finding both Season-Pass threads and reconciling them is the intended work, not a leak). |
| F6 | Major | The 22 `github_get_pull_request_reviews` calls aren't clearly necessary (deciding text is in inline/conversation comments whose own timestamps give post-merge-ness) → honest floor ~112 < 130/75. | **PARTIAL ACCEPT.** Make the review-list necessary honestly: add an explicit readiness clause — a beat runs only if its live-ops PRs carry no unresolved CHANGES_REQUESTED review blocker; certifying *absence* requires reading each PR's reviews. Recount; keep the ≥130 floor without padding. (Bears on the requester's 130 target — see status note.) |
| F7 | Minor | P01 (weight 5) vs P02 (weight 3) apply the same copy rule; the August rename is redundant once the brief states the name. | **ACCEPT.** Set P01 to interpretation (weight 3) for band consistency unless a genuine third reconciled source is required. |
| — | — | Locator error: §2 cites `slack:D05GU6L0XFH/1759248350.473459` for the Oct 1 auto-battler message; that ts is Sep 30 16:05 (Robert's pivot question). | **ACCEPT — verified.** The Oct 1 03:32Z message is `1759289577.628399`. Fix the §2 citation. |

Not-a-defect (reviewer agreed): S10 is reachable (10:00 Istanbul = 07:00 UTC, 7h past the Oct 31 00:00 UTC lock);
persona denial — none established (planned seeds verified at injection); coherence — no executed contradiction yet.

---

## Round 2 — re-review of the hardened design (redteam, ses_e579e61e9…) · VERDICT: FAIL (source-tracing; no runtime)

Round-1 Major findings re-checked + regression scan. Dispositions:

| # | Finding (abridged) | Disposition |
|---|---|---|
| 1 | Polarity leaks on negated markers ("not late"/"not cancelled") and fails ISO/long-form correct answers | PARTIAL/FIXED. Added ISO/long-form accepted renderings + ISO date acceptance in S10/W07 (false-negatives fixed, verified). Residual negation-paraphrase leak is an inherent regex limit → rubric-authoritative for polarity/timezone (§13); the forecast uses weights/mechanisms, not the regex. |
| 2 | W04/W05 text-on-linear can't bind a comment to its issue | ACCEPT (structural) — rubric-authoritative for destination binding (§13). |
| 3 | An incomplete calendar can satisfy the surface | ACCEPT (partial). C05 (8th beat) + P06 (held-push reason) added; full completeness is rubric-graded (§13). |
| 4 | Call-floor regression to ~129 | ACCEPT — FIXED. Honest recount → 128 unconditional / 79 per-record; floor 130→128, requester re-confirmed 2026-11-05. Gate PASS. |
| 5 | Suppressing the INT-01 mirror is an integration-parity anomaly (Julia can't see #zombie-prs) | ACCEPT — FIXED. §16 seeds the faithful mirror; non-load-bearing by ACL, not suppression. |
| 6/7 | S01 formats incomplete; computed instant not decision-discriminating (15:00Z vs 18:00Z same answer) | ACCEPT. Renderings added; §9/§18 now call the Istanbul→UTC arithmetic a weak contributor (real difficulty = dev-vs-prod deploy reconciliation). |
| Zombie Lane | C03 "runs" rests on Android-only verification | ACCEPT. R3 sharpened (held only on an ESTABLISHED failure; unverified ≠ held); R_HOLD_SCOPE controls metadata fixed. |

Residual (accepted): difficulty is BORDERLINE/UNCALIBRATED, resolved at /create-difficulty (§18).

---

## Round 3 — re-review of the ENRICHED design (redteam, ses_e56ffdbd4) · VERDICT: FAIL (repair, then run)

Enrichment to the 48-member cohort + 2 new mechanisms. Dispositions:

| # | Finding | Disposition |
|---|---|---|
| Major 1 | R_INFRA_SCOPE conflates Status with Still-to-do; D12 tokens is genuine work, not an error; S07 charged wrongly | ACCEPT — FIXED. Dropped D12; removed R_INFRA_SCOPE from S07; narrowed it to one honest over-hold (queue → Plague Race, C01 only). |
| Major 2 | Not all 48 members are decision-bearing (ZOM-484 Axe Arena out of scope; analytics members) | ACCEPT — PARTIAL. Dropped ZOM-484 (→ 47). The analytics/infra members are kept as certify-absence reads (same logic the methodologist accepted in round-2 for the 41 review reads); documented as such. |
| Major 3 | 209 is enumerated workload, not a necessary floor; Aug–Sep review clause supports ~30 certs not 41 | ACCEPT. Design §18 now labels ~255 / ≥150 unbatched a workload estimate; the ~130 floor is confirmed only by an efficient trajectory at the baseline (168 even without the review reads). |
| Minor | flat-prior tally | ACCEPT — corrected (~33/108 after S11 single-route). |
| S11 icon | RESOLVED (base #456 omits C&W); test redundant routes | ACCEPT — S11 single mechanism R_ICON_SCOPE (fails only if both the Marcus note AND the #456 enumeration are missed). |
| S07 / D5 attacks | FAILED (slots fair); hardening intact | No change. |

Residual (accepted): difficulty UNCALIBRATED/BORDERLINE (P(all) 0.479–0.533), SD-gate the limiter; settled at /create-difficulty. Biggest risk: a thorough Opus resolves the retrieved carriers.
