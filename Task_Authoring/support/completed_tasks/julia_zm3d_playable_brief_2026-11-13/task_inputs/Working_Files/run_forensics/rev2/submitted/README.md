# rev2 as submitted to the platform

`01_Universe_Inject.sql` in this folder is the copy that was pasted into the platform: rev2 with its four header
comment lines removed before submission (2026-11-12 07:29 local). Every statement is byte-for-byte the same as
`../01_Universe_Inject.sql`; `diff` shows only lines 1-4 of rev2 removed. The six baseline runs in
`07_Baseline_Trajectories-2` ran on these statements (trajectory_ledger: BOUND rev2).

| Copy | sha256 | Lines |
|---|---|---|
| `../01_Universe_Inject.sql` (rev2, gated locally) | 7d1f2aaeb29cf27791f7e69c9449a7f021689dd2fa0622dd382624b64064418d | 290 |
| `01_Universe_Inject.sql` (submitted; platform reports for rev2 name this hash) | c037dd89736e83e0ca136aaa14985b8e2b7524f74a56b423a7480bb3cc421197 | 286 |

The local stage gates need line 1 of the working file to be the `-- Are you planning to inject? Yes` marker
(`tools/sql_lint.py`), so the task folder's working copy is rev2 with the header (its file time set back to its render
time, 06:50:35, so the freshness checks see the order they passed in); paste from this folder (or strip the four header
lines) when the platform needs the SQL again.
