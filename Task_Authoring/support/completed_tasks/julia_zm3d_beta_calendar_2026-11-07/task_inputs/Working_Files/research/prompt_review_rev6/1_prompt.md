# Local independent /prompt review — SQL revision 6 (f8d905bd…249c), prompt 2a23afd8…2beb

Saved by the authoring session from the reviewer's hand-back (the reviewer could not write report files). This was a delta review by the round-3 main reviewer, not a fresh blind round: it carried P1–P4 forward from revision 5. Independent Eval 0 on this hash is `0_injection.md` beside this file (PASS / COMPLETE). Revision 7 followed for Eval 0 advisories E1 and D6; its fresh blind round is in `../prompt_review_rev7/`.

Revision f8d905bd passes: every dimension is now 5. The revised Trello comment settles the quest fork (F1), which was the only failure on the previous hash. None of the 13 changed statements introduces a contradiction or a new fork.

One caveat on how complete this is. I re-checked every changed record myself, but no fresh blind P1–P4 passes were run on this hash. Their findings on the previous hash were carried forward for the unchanged prompt and the 84 unchanged statements. If per-hash blind passes are required, run fresh P1 and P2 before treating this as final; together with the pending Eval 0, that's in the verdict's next action.

**Inputs checked**
- Prompt: `2a23afd8…2beb`, identical to before. Assignment `e8b82698…` and date `2f0af108…` are also unchanged.
- SQL: `f8d905bdd0c29585b17090b54aeb7837135f9d2462440ba71d81192d0871249c`, 97 statements.
  - I diffed it line by line against `3c035f2a…bc6f`: 12 rows edited, 1 added, none removed.
  - Lexical check: quotes balance, no string left open, every INSERT has as many columns as values.
- Check record: `R6/out/1_prompt_checks.json`, 14 readings and 13 comparisons, SHA-256 `f94fb7f24221281199d470bf8a37e204f9d78e7ae7518e880f177ce18537b8fb`.
  - I validated it read-only with the same harness as before (`review_rev5/work/scripts/validate6.py`, which uses the Evals helpers under `python -B`). Result: ok, no pending items, no contradicted premises, UGT PASS 5.
  - The generated UGT section to paste verbatim into the report is `R6/work/ugt_section.md`.
  - The review-context hash is a local stand-in (`baa2276f…`, from `R6/work/review_context.json`), because the Evals input store is off-limits.
- Git status is clean. Nothing was written under `Evals/`.

R6 = `/private/tmp/claude-501/-Users-sumit-Source-OC/31efe88c-a4b8-45a0-b2fb-ff911ab57eec/scratchpad/review_rev6`

---

## 1. Changed-record ledger

| # | Record | What changed | My check (base evidence) | Result |
|---|---|---|---|---|
| 1 | gmail_messages, Brian's SENT copy of the Sep 22 mail | Labels now `["ARCHIVED","SENT","Label_b19fb8d1b3"]` and `X-Gmail-Labels` "Archived,Sent,Opened". Body "Nothing else changes from the September handoff." → "Nothing else changes." `in_reply_to` and `references` NULL → `''`. | Brian's base sent mails (Jan 30 2025) carry `['ARCHIVED','SENT','Label_b19fb8d1b3']`, "Archived,Sent,Opened", and `''` for both fields. Base header forms: "Archived,Sent,Opened" ×15, "Archived,Sent" ×11. The snippet stops before the edited sentence, so it is still consistent. | Consistent. Closes the Brian half of P2-DR2 and the ARCHIVED / `in_reply_to` parts of Eval 0 D2. |
| 2–3 | Julia's and Frederick's copies of the Sep 22 mail | Same body edit; `in_reply_to` and `references` → `''`. | Matches #1. Inbox labels unchanged. | Consistent |
| 4 | Brian's SENT copy of the Sep 26 mail | ARCHIVED label plus header; `''` fields. Body unchanged. | As #1 | Consistent |
| 5–6 | Julia's and Frederick's copies of the Sep 26 mail | `''` fields | As #1. The reply target for the lock rule (thread `julia.lawson@harmonygames.co/1844311412966040123`) is unchanged. | Consistent. F4 unaffected. |
| 7 | drive_files `f_7c3e91a4…` (the brief, a native Doc) | `size` 13872 → NULL; `content_path` → NULL | Every base native Doc/Sheet carries both fields: 539 of 539 native `.docx` Docs and 356 of 356 native `.xlsx` Sheets in `gdrive/data.json`. These two injected files are the only native Docs/Sheets without them. The body is still read through gdocs (`docs_documents` row unchanged). No other record states a size or path for it. | A field-shape departure from base convention, not a factual contradiction. It no longer points at bytes that don't exist (the old Eval 0 D1). Not scored; listed under open items. |
| 8 | drive_files `f_e4a17c90…` (the calendar sheet) | Same as #7 | As #7. The sheet's tabs come from `sheets_sheets`, unchanged. | Same as #7 |
| 9 | linear_comments `cmt_zom526_2` (Brian, Sep 26) | Adds "…and, once that event is back, Axe Arena". "the event runs" → "the events run". | Base #company-internal, Sep 22, Brian: "We've decided to postpone Axe Arena for the beta release." Leonard, Sep 22: "Axe Arena is descoped". Leonard, Sep 23: "I moved out rewarded ads and axe arena". Brian, Sep 11: "[PERSON_NAME_0022] will move on to Axe Arena after the Season Pass". ZOM-526's base description doesn't list Axe Arena ("together with season passes and collect&win events"). Adding scope for a postponed event is plausible and contradicts nothing. | Consistent |
| 10 | linear_comments `cmt_zom526_3`, new (Calvin `usr_49b9dfa5208d400d`, 2025-09-30T16:24:19Z, seq 3) | "Collect and Win tokens go through the queue manager now (#472). Only the Axe Arena travel is left here, and that waits on the event coming back." | Base PR #472 "Implement Win&Collect into Queue Manager" merged 2025-09-30T15:53:04Z, 31 minutes before the comment. Its commit `b336cf3599` "Implement Win&Collect into Queue Manager" is dated Sep 29. Calvin is the queue-manager assignee (ZOM-543), and his ZOM-543 comment at 16:20:37 is 4 minutes earlier and consistent. ZOM-521 still shows "Tokens traveling to live-ops" unticked, which matches the Axe Arena remainder. The ID is unique and the sequence continues from 2. | Consistent. Closes the ZOM-526 half of Eval 0 D6: the ticket stays In Progress with stated remaining scope. |
| 11 | UPDATE ZOM-526 `updated_at` | 09-26 15:40:50 → 09-30 16:24:19 | Equals the newest comment; before the clock. | Consistent |
| 12 | linear_comments `cmt_zom544_1` (Vincent, Sep 29) | Now "Apple sign-in works from the settings menu, but progress does not restore yet: levels, currencies and cards are not synced." Dropped "on the auth branch" and the Google Play sentence. | Base: Vincent's Sep 25 checklist ("Levels completed :no_entry:", "Currencies … :no_entry:", "Cards owned … :no_entry:") agrees. His base tests were on "/auth" builds ("Match 3D iOS Submission - #41 - [PERSON]/auth"), so the comment is now less specific but not contradictory. ZOM-544 is still In Progress. | Consistent. This removes both of the "unverified build or platform" hooks that P1-DR2 relied on. |
| 13 | trello_actions `68dac8204f1e9a3b7c2d5e61` text | "New quest set goes in with the Mon Oct 13 rollover if it is ready. Nothing in the beta waits on it, the current set runs the whole time either way." | ID, date, member (Leonard), card, list and the badge update are unchanged. The card's base state (dueComplete false, list BETA) agrees with "if it is ready". The quest push row ("Not Ready", "Revisit once new quests roll out.") stays held either way. No apostrophe. | Consistent. Settles F1 (see below). |

---

## 2. Dimension scores (revision f8d905bd)

| Dimension | Score | Note |
|---|---|---|
| Unique Ground Truth | 5 (PASS) | All 13 alternatives excluded, or inside the brief's lock boundary (B8) |
| Feasibility | 5 | Unchanged; all five writes are cataloged |
| Persona ACL Reachability | 5 | All required scoped reads still visible to Julia; the changed records are in Gmail she receives, or in unscoped Linear and Trello |
| Explicit Tool Mention | 5 | Prompt unchanged |
| Clarity & Specificity | 5 | |
| Contrived / Unnatural | 5 | |
| Alignment with Today's Date | 5 | Newest injected event is 2025-09-30T22:10:41Z; the new comment is 09-30T16:24:19Z |
| Originality | N/A | No samples bundled |
| Truthfulness | 5 | All 8 premises still verified |
| Tool Use & Cross-service | 5 | |
| Investigation + Action | 5 | |
| Coherence (Bolt-on) | 5 | |
| Persona | 5 | |
| Business Function | 5 | |
| Assigned Competency | 5 | |
| Assigned Task Skill | 5 | |
| Complexity & Data Seeding | 5 | |
| Data Exists | 5 | |
| Cross-Service Coherence | 5 | Nothing counted. No State/Lifecycle, Quantitative or low-impact inconsistency. The Drive shape change (#7/#8) is not a factual inconsistency. |

---

## 3. Updated fork list

- **F1: quest still-to-do. Now settled.**
  - Reading A (lead): none.
  - Reading B1: the Oct 13 quest set (Leonard/Douglas).
  - Settled by the owner's record: "Nothing in the beta waits on it, the current set runs the whole time either way." The brief counts only "what still has to land before it runs for bought users".
- **F2: leaderboard held.** Settled. Brief: "Hold a beat only when players provably cannot enter, score or claim on prod even after a restart." Vincent: "it still does not start a new week. I killed the app and reopened it twice". Unchanged.
- **F3: C&W first window is Fri Oct 10 00:00 UTC.** Settled. Brief: "a window the release instant pre-empts does not count". Release is 2025-10-08 15:00 UTC. Unchanged.
- **F4: reply to Brian on his Sep 26 mail.** Settled. Brief: "its owner is told in a reply on the mail where they committed to it". Brian: "reply on this mail". Unchanged by the Gmail edits.
- **F5: Halloween off.** Settled. Robert: "Take it off the beta calendar". Unchanged.
- **F6: C&W icon animation is a still-to-do (Marcus).** Settled. Brief: "not polish nobody flagged". Marcus: "still to do on my side". Unchanged.
- **F7: sheet link goes on ZOM-78.** Settled. Frederick: "Let us use this ticket for the ZM3D beta live-ops calendar". Unchanged.
- **F8: Brian's new date (Oct 29 or Oct 30).** Authorized boundary: "lands before its lock". The rubric must accept any date before Fri Oct 31 00:00 UTC. Unchanged.
- **F9: ZOM-544 not a still-to-do.** Settled, more firmly than before. Brief: "For each beat, what still has to land before it runs". Arthur: "Season Pass schedules are already running on prod". The revised comment no longer mentions a branch or a platform.
- **F10: Plague Race push is held.** Settled. Brief: "Ready and LIVE". Unchanged.
- **F11: leagues and the weekly leaderboard are one beat.** Settled. #zombie-ops: "Weekly leagues: every monday at 00:00 AM UTC". Unchanged.
- **F12: hold-until is open-ended.** Settled. Brief: "Hold a beat only when…". The rubric must not require a date. Unchanged.
- **F13 (new candidate): Axe Arena token travel on ZOM-526, or Axe Arena as a beat.** Excluded.
  - Frederick DM2: "Leave off the four rows for things that are not in the beta: … Axe Arena".
  - Calvin: "that waits on the event coming back".
  - Base: Axe Arena was postponed for the beta on Sep 22.
- **New candidate: C&W token travel (ZOM-526).** Out, as before, now because it has shipped via #472 rather than because it wasn't needed. No change to the sweep.
- **New owner or hold questions from the changed records:** none.

---

## 4. Final verdict for f8d905bd

### Injection Gate
- Independent Eval 0 on this hash: pending at the time of writing.
- Eval 0 on the previous hash `3c035f2a…bc6f`: PASS / COMPLETE.
- I checked every task-required changed record directly (ledger above).

### FINAL VERDICT: PASS

Score: 5

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Before submission, get the independent Eval 0 for f8d905bd. If the platform requires blind deep-recheck passes per hash, run fresh P1 and P2 on f8d905bd.

Evidence limits:
- Phase 5 for this revision was a main-session recheck of the 13 changed statements against the P1–P4 findings from `3c035f2a`. Those findings were carried forward for the unchanged prompt and the 84 unchanged statements under stage-evidence-v1. No fresh blind passes were started on f8d905bd.
- The independent Eval 0 on this hash is pending.
- The official prompt-checks helpers bind to the off-limits input store, so the record was validated with the same helper functions in a local read-only harness.
- Runtime handling of the native Doc and Sheet records whose `content_path` and `size` are now NULL can't be determined statically.

**Lowest Dimension:** none below 5.

**Summary:** The revised Trello comment settles the one open UGT fork. The other edits clear earlier advisories: the September-handoff phrase is gone, the Gmail label and field shapes match base, ZOM-526's remaining scope is now stated, and the ZOM-544 hooks are gone. All 13 changed statements check out against base evidence and none opens a new fork.

---

## 5. Open items and status of the earlier "second strict reviewer" list

1. **ZOM-526 / ZOM-528 still open after work landed (Eval 0 D6):** partly closed.
   - ZOM-526 is closed as an issue: Calvin states the remaining scope (Axe Arena travel), which fits Axe Arena's Sep 22 postponement.
   - ZOM-528 is unchanged: still In Progress although card-pack commits landed Sep 29 ("Adding card pack animation"). No record says the cards' travel to inventory shipped, so it isn't demonstrated. It's excluded from the still-to-do set either way.
2. **ZOM-544 (P1-DR2 risk):** closed. Both hooks are gone, and the rejection quotes still hold.
3. **ZOM-521 ticks "Live-ops icons … animations" (N6):** unchanged. Consistent by timing: ZOM-525 was Done on 09-17, and C&W arrived 09-26.
4. **#468 `ev_6` "reviewed" numbered after close (N2):** unchanged, with base precedent.
5. **Gmail, Drive and calendar-invite shape:**
   - Gmail: improved. ARCHIVED and the `''` fields now match base. Still unchanged: `mbox_from` lacks the trailing `\r` that base messages carry.
   - Drive: changed and arguably worse in shape. The two native files now have NULL `content_path` and `size`, while all 951 base native Docs/Sheets have both. It asserts no false bytes and contradicts no fact. A strict reviewer could at most call it one low-impact format variation (NON-FAIL 3). I don't score it.
     - Minimum change if you want it gone: restore `size` and `content_path` to the base pattern, as in revision `3c035f2a`. That brings back the old D1 (a `content_path` with no bytes behind it). You can't satisfy both points, so pick the convention match.
   - Missing invitation mails for the release event: unchanged. That's the base norm; Julia has an invitation mail for only 5 of her 15 invited events in Aug–Sep.
6. **Informal references:** Brian's "September handoff" is closed (sentence removed). The brief's undefined "Aug-Sep live-ops cohort" is unchanged and has no effect, because there's no CHANGES_REQUESTED review in that window.
7. **"Product" means Robert (A6):** unchanged. Only Confluence supports it ("Owner: Robert (Product)").
8. **Rubric traps downstream:** updated.
   - The quest rollover's still-to-do must now be graded as none, or not graded. Don't require mention of the Oct 13 set, which is conditional ("if it is ready").
   - New mild tension: the quest push row's "Revisit once new quests roll out." sits beside Leonard's "Nothing in the beta waits on it". The push is held as Not Ready either way. The rubric must accept the push's "what is missing" with or without a reference to new quests.
   - Unchanged constraints:
     - no hold-until date
     - any handoff date for Brian before Fri Oct 31 00:00 UTC
     - leagues and the weekly leaderboard as one beat
     - a ZOM-78 comment or a link update
     - a DM thread reply or a new DM message
     - no strict grading of copy-naming details on held pushes
9. **Assignment axes (Business Function / Competency overlap):** unchanged. I judged both defensible at 5.
