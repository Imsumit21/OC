# Douglas: Zombie Match 3D beta server sign-off register (submitted 2026-10-28)

Persona Douglas (Software Engineer) · Long Horizon · Engineering / Engineering Ops / Retrieval · difficulty mode medium · env hg4-with-gsuite-bundle-1174 · universe hg4-2026-08-31 · universe date Oct 1, 2025 · platform task 6ad90ea979eb9e5d89f8879f.

`task_inputs/` is the full slot folder as submitted. `work/dg_beta_server/` holds the ID minting and SQL / manifest / dossier builders. `work/scratch_scoring/` holds the rubric-replay scripts used to project difficulty from trajectories (`r3/sim7.py`, `rub/grade3.py`, `rub/parse.py`) and the OE generator (`oe/gen.py`). `eval_reports/` holds every platform eval report (/injection, /prompt, /hardness, /oe, /rubric).

## Final state
- Injection SQL `01_Universe_Inject.sql` sha256 2131bbeff16b, 404 INSERTs (hardening round 3; three earlier rounds missed the difficulty gates).
- Friction: none.
- Oracle Events: 66 events; /oe NON-FAIL (a Linear state id seen only in run output; one wrong approval condition) → PASS 5 after the fixes.
- Rubric: 76 rows (75 Outcome, 1 Process), weight 314; /rubric FAIL 1 → PASS 5 after applying its Fix List verbatim.
- Baselines (6/6 completed): weighted 51.9 / 71.0 / 44.6 / 51.9 / 73.6 / 44.6 → average 56.3%, pass@1 0/6, SD 0.117, 4 failure patterns (largest 33%), counted calls 163–238 (avg 196). 17 all-fail rows, all VALID (11_AF_Justification.md).

## Key answers
- Register in Arthur's Drive folder "ZM Beta sign-off" (d_69fcebc484d472907b0b5c), 17 tickets: on prod ZOM-499 (#44 redeployed before the freeze), ZOM-510 (Zombie Lane rewards import to prod); not on prod the other 15 (ZOM-336, 392, 503, 518, 550, 435, 557, 256, 487, 537, 444, 531, 459, 509, 436).
- Out: ZOM-547/553 (Arthur's reply-all), ZOM-461 (12 s before the cut), ZOM-457 (parent).
- Share with Leonard as commenter; DM reply to Arthur in D05QQF7V404 (2 on prod, 15 keys); 15 tickets back to Todo, each with a comment naming the change still to go out.

## Lessons carried forward
- Model the rubric before hardening: per-ticket status rows that every run passes flatten SD and lift the average; projections made with a grouped rubric were wrong for three rounds.
- Hidden facts that bit: inline review comments on PRs (#38, #39, #46 — no run used them), a reply-all inside a thread a sender search does not open, a Confluence page comment. Spread them over different surfaces so failure patterns differ.
- /oe: never put a value seen only in run output (ids, ranking) in an Expected line; state the rule in force at the clock.
- /rubric: one row per target for writes and per fact in a requested list (no sampling of moves, comments or a reply's list); don't lock file type; never bundle "each saying …" into a count row; keep weights consistent per ticket determination; apply the Fix List verbatim.
- Local gate: diversity.authority_share fails structurally when one rules card governs every row (same as the Frederick task); it does not affect the platform.
