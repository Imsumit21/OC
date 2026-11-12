# rev1 as submitted to the platform

`01_Universe_Inject.sql` in this folder is the copy that was pasted into the platform: rev1 with its four header
comment lines removed before submission (2026-11-12 02:40 local). Every statement is byte-for-byte the same as
`../01_Universe_Inject.sql`; `diff` shows only lines 1-4 of rev1 removed.

| Copy | sha256 | Lines |
|---|---|---|
| `../01_Universe_Inject.sql` (rev1, gated locally) | 78465cd474f817d507e482d1af2bc2b7cc12ad15878d0c900ff5644f96a24898 | 290 |
| `01_Universe_Inject.sql` (submitted; `/injection`, `/prompt` and `/hardness` reports name this hash) | 3a76797fbde16ffa560e3bc54794965464db8f8ef38dc1019f8b11df3ceaeddb | 286 |

The local stage gates need line 1 of the working file to be the `-- Are you planning to inject? Yes` marker
(`tools/sql_lint.py`), so the task folder's working copy is rev1 with the header; paste from this folder (or strip
the four header lines) when the platform needs the SQL again.
