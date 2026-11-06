# Local /oe run — evidence

Current OE: `08_Oracle_Events.df9a71e8.md` (35 events, sha256 `df9a71e8253cd300…`; same bytes as `task_inputs/08_Oracle_Events.md`).

- `oe_review_record.df9a71e8.json`: the format-2 oracle-events-v2 review record for that text.
- `validate.df9a71e8.json`: output of `Evals/tools/hg_oe_review.py validate` on the record. Verdict PASS, score 5, execution COMPLETE, completeness 5, accuracy 5, path feasibility SUPPORTED, task solvability SUPPORTED_BY_OE, prompt follow-up NONE. 764 Expected-line values ledgered, 0 unledgered, 0 absence claims, 0 missing / inaccurate / minor / unresolved.
- Deep recheck: `../deep_recheck/O1.md`, `O2.md`, `O3.md`. Every finding was rejected against the records. `oracle_adjudication.md` holds the GPT-6.1 oracle's round-2 PASS on all five rejections.

Superseded (`*.superseded_6148bcbc.*`): the earlier review of sha `6148bcbc…`, also PASS 5. The only change between the two texts is in OE 26: the runbook quote now stops before "and link it here." and one sentence was added linking the update-row failure to OE 31's ticket fields.

`inputs_vincent_store.json` is the Evals store manifest used for the first run. The shared store backup is in `../evals_store_backup_20261105/`.
