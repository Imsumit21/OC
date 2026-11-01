# Frederick Stone: Q3 Standard Metrics card-spend breakdown (submitted 2026-10-25)

Attempt 6ad83eebbd6456fd065bbd20 · persona Frederick Stone (Co-founder) · long-horizon · difficulty mode medium · universe date Oct 1, 2025 07:00.

`task_inputs/` is the full slot folder as submitted. `work/` holds the local helper scripts (feed parsing, category and run-rate math, rubric fix scripts) and the baseline write extracts in `work/bl/`.

## Final state
- Injection SQL `01_Universe_Inject.sql` sha256 7b3552ae971b: /injection PASS, /prompt PASS, /hardness NON-FAIL 3 (PROCEED).
- Oracle Events: 38 events, /oe PASS 5.
- Rubric: 63 Outcome rows, 243 points; /rubric reached a clean review after four rounds.
- Baselines (6 of 6 completed): weighted pass 75.3 / 79.0 / 79.0 / 79.0 / 69.5 / 87.7, average 78.3%, pass@1 0%, per-run SD 0.054.
- All-fail rows R16, R28, R44, R46: all VALID (Webflow forward and Murf email never opened). Justifications in `task_inputs/11_AF_Justification.md`.

## Key answers
- Q4 run-rate 2,869.80; disputed charges Midjourney 60.00, LinkedIn 99.99, SavvyCal 16.00, Buttondown 20.00 (195.99).
- Ledger tie-out 97,968.21; opex 96,968.21 after the 1,000.00 Unity Ads reclass.
- Reply recipients: Leonard, Arthur and Robert (robert@harmonygames.co).

## Lessons carried forward
- /rubric needs the key `title` (not `criterion`), titles in the form "The Agent <verb> …" (never "The Agent's …"), one claim per row, and layout-tolerant tie-out rows.
- When a /rubric report gives checked fixes, copy them word for word and change nothing else.
- Base-grep every injected vendor before writing vendor notices; findable traps leak to Opus.
- The platform verifier copy has no "Run #N" headers; normalise it before `difficulty_stats.py --build` and keep the original paste.
