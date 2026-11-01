# 06_PreCheck_Trajectory/ — Opus 5.5 pre-check (screens 33–39)

1. Re-apply `01_Universe_Inject.sql` in the runner (Database tab → Query → Run Query).
2. Run **one** trajectory on **Opus 5.5**. Download it here as `trajectory.json`
   (the Evals `opus` key).
3. Read it. Proceed only if it failed on substantive parts (a hidden authority missed,
   a thread read short, a stale summary trusted, a cohort member dropped). If it solved
   the task or only missed cosmetics, answer "No" and run `/create-hardening` before
   anything else.
4. Record your answer and explanation in `PreCheck_Difficulty_Check.md`.
5. Run `/hardness` with the prompt, the SQL (or "no injection") and this JSON
   **uploaded as a file**. Score 1–2 = HOLD → `/create-hardening`; 3–5 = PROCEED.
