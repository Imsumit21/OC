# 07 — Baseline rollouts (screens 40–43)

Your prompt exactly as written, **six trajectories on Opus 5.5**, one run. Re-apply
the SQL first. Trigger the runs and move on — write the Oracle Events and rubrics
while they run.

Save one file per rollout: `trajectory-run-1.json` … `trajectory-run-6.json`. An
errored rollout is an empty file; it is excluded from the all-fail denominator and
the difficulty statistics. Three or more errored rollouts fail the task.

If friction is configured, confirm here that the forced error fired and the async
submit → check → get sequence appeared (`03_Error_Async_Config.txt` → post-baseline checks).

Never hand-edit an exported trajectory. Do not tune the prompt to the baseline.
