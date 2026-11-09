# Deep Recheck P2: SQL revision 7 delta

SQL: inputs_rev7/01_Universe_Inject.sql, sha256 045f64bd805524ec1d0d0c4972a54ac4a682672fba2dc0c9dda0ea7971ef09d0. Header counts (125 INSERT, 11 UPDATE) match the file.

## Rev7 changes, each checked against base

| Row | Change | Check |
|---|---|---|
| Notes doc (line 19) | Notice-route line removed | Body is 2032 characters, matching its style-run end of 2032. No injected row still mentions a notice route. The only remaining "notice" text is Sunset's "Formal notices are a separate step that legal will walk you through later", which is consistent with the removal. |
| Sunset mail (line 90) and Leonard's quoted reply (line 93) | "How each holder gets formal notice…" line removed | Removed in both copies. size_estimate drops by the removed line's length: 1715 → 1648 (−67) and 1884 → 1815 (−69, the quote line with "> "). The snippets begin before the change, so they are unchanged. |
| ENG-2448 | Back to "Email: PERSON_5275_EMAIL" | This is TOR's correct messaging address (see rev3). Nothing now reads a legal-notice address. |
| KPMG clarification (line 86) | Adds "For item 4, we need any new financing and the decision to wind down." | size_estimate 1379 → 1448 (+69 = the added sentence). The thread snippet is unchanged and still correct. No financing since the 21 Jul 2023 seed: the 23 Jan 2026 recap was proposed only (leonard@…_1855133803855213163). The wind-down is on record (see NB-29 below). |
| Slide el_3f1b82e16a82 | "Why we are closing" | No data claim. |

- **DR7: closed.** The Orrick copy no longer conflicts with anything, because no injected record states notice terms.
- **DR6: closed** (moot).
- **DR1–DR4:** closed as in rev2.
- **DR5:** conditional, unchanged.

## Opened by rev7: NB-29 decision date, now task-touched (NON-FAIL)

- **Prompt sentence:** "an answer to KPMG's audit request for Griffin from yesterday". KPMG item 4 now explicitly asks for "the decision to wind down".
- **Feb 9 side:**
  - slack messages/C07C2866011/2026-02.json (#executives, Leonard, 2026-02-09T21:33:04Z): "at least we finalized the decision to shut down".
  - Leonard's mail to PERSON_4337 on 9 Feb 2026 11:12 PST (leonard@…_1856675475513544349): "we've decided to shut the company down".
- **Feb 10 side:** slack messages/C05URGU759U/2026-02.json (Leonard, 2026-02-11T20:54:20Z): "We didn't finalize this decision until yesterday".
- **Severity under the date-slip rule:** the date changes no order, window or count the answer uses, because the event falls after Dec 31, 2025 either way. That makes it one minor inconsistency, NON-FAIL. It is also a P1 fork if a rubric row grades the decision date.
- **Smallest fix:** make KPMG's sentence "For item 4, we need any new financing and the decision to wind down, dated by when you first told Griffin." That settles the date on Feb 9, 2026 (the mail above). The alternative is for the rubric to accept Feb 9 or Feb 10, 2026.

## Verdict

Cross-Service Coherence: **NON-FAIL**, on one low-impact item, NB-29, which the new KPMG item-4 sentence brings into scope. It becomes PASS with the fix above.

Caveat: if the main session counts the acknowledged base remnants (DR2's raw email, NB-22 in the letters) as live, NB-29 would be the second low-impact item, which fails under the strict rule.

Feasibility, Persona ACL, Data Exists and Tool Use stay PASS.
