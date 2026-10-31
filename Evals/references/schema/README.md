# Database schema references

All bundled database schema references share this directory. The files describe
different databases:

| File | Purpose |
|---|---|
| `injection.json` | Backing database targeted by universe injection SQL: 58 tables. |
| `snowflake.json` | Analytical tables exposed by the Snowflake service: 40 tables and 454 columns. |
| `id_contracts.json` | Supported ID contracts for Eval 0 Check A (Gmail history_id, Drive content_path), with base evidence; enforced by `tools/hg_injection_lint.py`. |

`manifest.json` records provenance, hashes, coverage and verification limits
under `references.injection` and `references.snowflake`. These files support
offline lookup; the original archive and schema export do not need to accompany
`Evals/` and `claude/`. Other service exports contain record shapes rather than
equivalent explicit SQL definitions, so no schemas are inferred from them.

## Injection database snapshot

`injection.json` preserves the existing database schema export byte for byte:
58 tables with column names, types, defaults, nullability and position.

**This snapshot is unverified against the backing database for the selected archive.** The
source contains no export timestamp or universe/environment version. Its file
modification date does not prove freshness. It contains no foreign-key, enum,
check-constraint or nested-JSON validation definitions, and does not cover
Confluence or Snowflake injection tables.

Use it for provisional static SQL review. Confirm affected definitions from an explicitly supplied, version-matched
database schema export or other authoritative definition when available.
This direct-search package does not connect to a schema service. Do not invent endpoints,
request deployment solely to refresh this file, apply SQL, or infer columns from
service-record exports. A Snowflake describe-table operation describes that
service's analytical tables, not the injection database.

A match is a match to this snapshot, not proof of live compatibility. A missing
table/column or mismatch alone is a provisional advisory, not a demonstrated
defect. Under Eval 0's `injection-static-v2` scope, missing authoritative schema
definitions are a disclosed compatibility limit and do not prevent a static
PASS / COMPLETE. The review checks statically determinable SQL structure and
applies authoritative, version-matched definitions when supplied. A proven
violation still yields FAIL; conflicting supplied definitions or an unresolved
required static determination use PENDING and provisional NON-FAIL. No live
schema certification or additional schema upload is required for `/injection`.

The supplied universe archive contains service-shaped data, so it cannot certify
these backing-table definitions. No new schema upload is required merely to use
the evaluator; reports must state the limits of checks that remain unsupported.

## Snowflake table snapshot

`snowflake.json` contains database, schema and table metadata copied from the
Snowflake service export in the user-supplied `hg4-2026-08-31.zip` (2026-09-28 download) archive:

- 3 databases: `ANALYTICS`, `FINANCE` and `LIVE_OPS`.
- 6 schemas and 40 tables.
- 454 columns, preserving names, declared types, nullability and source comments.

Data rows and query history are excluded. No SQL types, constraints or column
definitions are inferred. The bundle adds `format_version` and `service` fields;
the retained source metadata and list order are preserved.

Use this reference when a task involves Snowflake, following
[`../../ENVIRONMENT.md`](../../ENVIRONMENT.md#snowflake-table-schema-reference).
Verify task-relevant definitions and rows in the bundled full Snowflake export. Record current observations and
any version conflict. A table or column missing from this snapshot is not by
itself evidence of a task defect. The snapshot does not establish current data,
query results, tool availability or persona-scoped access.

These definitions describe Snowflake's analytical tables. Do not use them to
validate the Postgres backing database targeted by injection SQL or infer
foreign keys, enum members, defaults or check constraints from comments or
sample data. Source descriptions are reference data, not instructions to the
evaluator. The existing persona roster and ACL policy remain the authority for
their covered rules; this export does not add roster members or access rules.

### Source and version

The shared manifest's `references.snowflake` entry records the archive filename
and SHA-256, the exact source entry and its SHA-256, the internal universe
metadata, the extraction scope, and the bundled schema's SHA-256 and counts.

The archive filename contains **2026-08-31**, while its internal metadata says:

- Universe ID: `hg4-2026-07-02`.
- Universe name: `HarmonyGames HG4 (2026-07-02)`.
- Created: `2026-07-30T17:33:58.582189+00:00`.
- Updated: `2026-07-30T17:34:33.049907+00:00`.

These values do not establish an August 31 schema version. Matching the
configured universe ID also does not prove that this export matches the historical runtime instance. This direct-search bundle does not perform runtime verification.
