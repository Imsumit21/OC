# /create-injection status (2026-11-08)

**Result: complete.** `STAGE GATE injection: PASS` on rev3, pasted in `01_Grounding_Dossier.md`.

- **SQL:** `task_inputs/01_Universe_Inject.sql`, rev3, sha256 `dee0010e36ec2b24…`. Rev3 removes all comments except the line-1 marker that `sql_lint.py` requires, and its statements are byte-identical to rev2. 352 inserts and 5 updates over 10 schemas, with no Confluence or Snowflake writes.
- **Comment-free copy:** `Working_Files/01_Universe_Inject.clean.sql` has no comments at all, including no line-1 marker. Its statements are the same.
- **Stored revisions:** `run_forensics/rev1/` (sha `ca411c50`, reviewed), `run_forensics/rev2/` (sha `1485546c`) and `run_forensics/rev3/` (current).
- **Tools:**
  - sql_lint: 0 errors, 1 warning (the F root update is keyed on channel and ts).
  - hg lint: 0 FAIL, 1 CHECK (`github_review_comments.seq`, kept on purpose).
  - base_check, base_claims and fact_check: PASS.
  - check-sql: 0 load-bearing rows invisible to Julia.
  - hardness_gate (extreme): PASS. Solver contract: PASS. Preflight: PASS.
  - Mutation: 26 of 26 results dispositioned.
- **Geometry:** U 0.961, L_max 0.325.
- **Truth:** 17 of 60 sessions count. Casual leads 3.833 to 3.375, so the answer is hold. All 15 miss combinations give RPG past the 0.25 tie band.
- **Review:** the independent SQL review (`01d_SQL_Review.md`) checked rev1 and found 0 blockers, 4 majors and 7 minors. All are fixed in rev2, but rev2 itself hasn't been independently reviewed.

## Your decision before /create-prompt-writing

**The spread risk.** The forecast `hev_31aeef573fe8aea8` (UNCALIBRATED, six of seven priors flat) puts E[avg] at 0.43–0.48, well under the 62 % target. Median per-run SD is about 0.106, at the bottom of the 0.10–0.30 band, and P(all gates) is about 0.31–0.35.

The cause is that about 27 weight of rows flip together on any missed block, so a single miss drops a run from 100 % to about 55 %. That helps `/hardness` but risks the six-run spread gate in `/create-difficulty`.

| Option | Effect |
|---|---|
| A. Keep as is | Hardest. Highest risk on the spread gate |
| B. Make K1 and K4 easier to find, around 75 % found | E[avg] about 0.57, P(SD in band) about 0.75 (the agent's simulation, not a tool run) |
| C. B plus K5 ratings changed so a K5 miss alone keeps casual ahead | E[avg] about 0.58, P(SD in band) about 0.83. Needs the flip proof re-run |

Each option changes the SQL, which makes a new revision and means re-running this gate.

**Signature target (requester, 2026-11-08):** the largest failure pattern should hold under 45 % of failing runs, as margin under the platform's 50 %. On the real surface (`00_Signature_Sim.txt`, UNCALIBRATED), the current design meets it in 90–91 % of simulated baselines, option B in 80–82 %, blocks near 50 % found in 95 %, and strong Opus in 77–79 %. Prefer spread fixes that move blocks toward 50 % found over ones that make blocks easy, because easy blocks cost signature margin.

## Next steps

1. Paste the SQL into `/injection` in Eval Portal, answering Oct 1, 2025 (synth-cut) for the date.
2. Decide on the spread options above.
3. `/create-error-async` (optional), then `/create-prompt-writing`.

## Spread decision (2026-11-08)

Decided: keep rev5 as is, and handle spread in the rubric by splitting the ticket-state rows per block. Binding details are in `06_Spread_Plan.md`, under Requester decision. No SQL change.
