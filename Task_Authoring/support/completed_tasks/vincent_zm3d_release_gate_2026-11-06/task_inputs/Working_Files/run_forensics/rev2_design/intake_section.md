## 15 Revision intake (S0r)

Verdicts consumed: `run_forensics/rev1/precheck.node_verdicts.json`, from `/create-hardening` MODE B (`Working_Files/01a_Hardening_Report.md`). The export `precheck` is the platform Opus 5.5 pre-check of 2026-11-04 (sha256 `f2b7862f…`). It is BOUND to rev1 on evidence: sole revision, with the rev1-only "build status means" row seen. It certifies rev1 only; it is historical for rev2 and certifies nothing there. Platform `/hardness`: score 1, Too easy, HOLD.

| Node | Runs | Proposed verdict | Disposition | Evidence (run · event) |
|---|---|---|---|---|
| R_DONE_BUILD (T1 ZOM-569) | precheck (1 of 1) | LEAKED | rebuild (R2): ZOM-569 closed at 18:05Z, before both Started lines, after Oliver's 18:02Z "fixed on my branch"; the 21:40Z comment that dated the fix is gone; the base #2028 change line decides. Low weight in the projection | precheck event 158 (`cmt_zom569_1` read), precheck event 179 (commit list with the 21:36Z fix) |
| R_DONE_SERVER (T2 ZOM-567) | precheck (1 of 1) | LEAKED | rebuild (R1): the #zombie-ops withdrawal and Douglas's reply are deleted. Douglas's 22:01:52Z DM says #36 is rolled out (code side) and Arthur's inline review comment on #36 (22:35Z) says the chest rows are still dev-only. match3d-backend has no Slack mirror | precheck event 294 (`from:douglas` search), precheck event 301 (withdrawal thread), precheck event 386 (post-candidate sweep) |
| R_CORRECTION (T3 ZOM-435, T3b ZOM-473) | precheck (1 of 1) | LEAKED; pending keys ZOM-435 / ZOM-473 flagged as CONFOUNDED candidates | keep. CONFOUNDED rejected: call and build status match the truth and only the QA-result wording differs (representation). Both re-tests are checks on the candidates, so they can't move before the run's date floors | precheck event 38 (Trello card ZOM-570 names), precheck event 386 (Brian's DM in the sweep), precheck event 493 (register write) |
| R_UPDATE_RULE (T4 update path) | precheck (1 of 1) | FALSE | purge as a solver rule: no ablation changes a value. T4 / CH3 stay as a trap and chain, and B01 stays a core write slot | precheck event 394 (DM pointer), precheck event 400 (Brian's doc), precheck event 462 (ZOM-581 filed) |
| R_ALIAS (T5 ZOM-562) | precheck (1 of 1) | LEAKED | keep: the vendor's session notes are a check on the candidates, inside every dated Gmail window | precheck event 327 (`after:2025/09/29`), precheck event 346 (decoded body) |
| R_FILTER (T6 scope) | precheck (1 of 1) | LEAKED; V01 failed | keep. V01 is CONFOUNDED (fairness, on the grader): Leonard's rule gives the run's own ticket a row. Rebuilt: V01's expected keys are the 132 truth keys plus ZOM-581 | precheck event 34 (rules doc), precheck event 462 (ZOM-581 created), precheck event 493 (133 rows) |
| R_COMPLETION (T7 ZOM-563) | precheck (1 of 1) | LEAKED | keep: Vincent's prod check is base data in a DM the run reads | precheck event 303 (DM D079SNE2TL4 read) |
| scale:comments (channel) | precheck (1 of 1) | HELD | keep. Two rev2 traps now sit in comments the run skipped: R_SYMPTOM_NOTE on ZOM-293 and the continuity notes on ZOM-458 / ZOM-535 | precheck event 436 (ZOM-293 read through `linear_get_issue` only), precheck event 224 (ZOM-458 comments read) |
| new: R_OLD_NOTE (T16 ZOM-458, ZOM-535) | — | not yet run | rebuild (new rule, A14): Brian's Sep 29 group-DM message, before the run's DM floor (Sep 30 02:40Z) and Slack floor (Sep 30 18:30Z) | precheck event 394 (Brian DM read only from ts 1759200000), precheck event 385 (sweep `after:1759257000`) |
| new: R_SYMPTOM_NOTE (T17 ZOM-293) | — | not yet run | rebuild (new rule, A17): Vincent's Jul 3 comment says what goes wrong on a ticket whose description doesn't | precheck event 436 (`linear_get_issue` ZOM-293, no comment read), precheck event 493 (written NO CALL) |

Routing:
- Universe changes go to S5a onward (§14 design_delta rows R1–R3b) and to `/create-injection` as rev2. rev2 is stored at `run_forensics/rev2/`; rev1 stays at `run_forensics/rev1/`.
- No prompt-side defect: the prompt is unchanged.
- No OE or rubric exists yet. Rubric writing must keep weight 5 on the R1 / R2 / R3a / R3b rows and give the register row the self-filed-ticket allowance.
