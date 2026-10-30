You are fixing the Phase 0–1 authoring tools before the next task starts. Read these in full before planning:

1. Task_Authoring/plans/Learnings_And_Improvements_2026-10-25.md: §1 (decisions), §4.2 (the work, each row with its
   acceptance test) and §6.
2. Task_Authoring/support/audit/phase0_1/AUDIT_REPORT.md: the evidence and smallest fix for B1, B2, H3, H1, H2, M1–M7
   and L1–L10.
3. Task_Authoring/plans/Implementation_Prompt_Phase0_1.md. Its HARD CONSTRAINTS, the one-owner rule and the tool style
   still apply, except where this file says otherwise.
4. Task_Authoring/setup/GEN_EXECUTION.md §1.

Scope:
1. The P0 rows of §4.2: B1, B2, H3, D3, D5, D6, MK.
2. Then the move (MV).
3. Then the P1 rows: G1, V1, H1, H2, M2, M5, M7.

Stop after P1 and report. P2 waits for my go.

Rules:
- No task is in flight: Season Pass is skipped.
  - Its whole task folder is archived at Task_Authoring/support/archive/task_inputs_season_pass_2026-10-25/. It is
    read-only; never run its scripts.
  - Read Season Pass evidence only through the frozen copies, Task_Authoring/support/backtests/season_pass/rev13/ and
    rev14/; check each README and SHA256SUMS first.
  - Task_Authoring/task_inputs/ is now a fresh V3 template for the next task. Write nothing there.
- Until the move, change existing files only through support/pending_edits/ (the staged copies) and
  support/pending_tools/, and keep MANIFEST.json consistent.
  - The staged documents already hold the 2026-10-25 learnings edits: 01_Scenario_Design S0/S4/S5a,
    01_Universe_Injection S5f, 01a_Hardening MODE B (pre-check), 09_Rubric_Writing gate 5, and the Guide.
  - Keep those edits, and add to those files rather than replacing them.
- The move:
  - When P0 passes, stop and ask me to confirm a maintenance window.
  - Then run check-only, take a fingerprint, apply, and run the sandboxed self-tests (§4.2 MV).
  - Never run the live `stage_gate.py --self-test` against the shared cache.
- Process:
  - Never run git.
  - Python stdlib only, run with `python3 -B`.
  - Every new test plants the failure it guards against.
- G1's acceptance targets are the grades of record in support/backtests/season_pass/rev14/README.md. Revision 13 must
  still reproduce exactly (plans/Rev13_Results.md; support/analysis/rev13_check.json).
- Don't edit support/analysis/*.py: they are the reference implementations those grades were taken with. Port the
  fixes into the tools.

Report:
- **Per row:** the change, the files, the test that plants the failure, and the acceptance evidence (command and
  output).
- **The move log:** fingerprints before and after, the check-only output, and the self-test results.
- **Deviations**, with reasons, and **open issues**.

Use the evidence labels [O] / [D] / [I].

Before coding, reply with a one-screen work plan and wait for my OK.
