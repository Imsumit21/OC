# Tool export reference

Use `catalog.json` for the combined tool-name and parameter inventory. The
14 `*-tools.json` files preserve the user-supplied exports byte for byte.
`manifest.json` records their original filenames, hashes and tool counts,
plus the combined catalog hash. Runtime availability has not been verified.

| Export | Tools |
|---|---:|
| Confluence | 29 |
| Contacts | 9 |
| GCal | 12 |
| GDocs | 7 |
| GDrive | 21 |
| GitHub | 57 |
| Gmail | 33 |
| GSheets | 10 |
| GSlides | 8 |
| Linear | 28 |
| Slack | 32 |
| Snowflake | 10 |
| Trello | 41 |
| Gateway | 1 |
| **Total** | **298** |

The exports declare names, parameter types and required/optional status. They
do not include tool descriptions, output schemas, nested-object definitions,
database column schemas, ACL rules, or an environment/universe version. Do not
fill those gaps from an older catalog or infer behavior from a name alone.
Use supplied run evidence for observed behavior, or record the unsupported
check under `../../ENVIRONMENT.md`; do not initiate a live connection.

The gateway export contains only `get_time`; the evaluator does not call it.
Local search uses `../../tools/hg_search.py` under `../../SEARCH.md`, not MCP.
The fixed evaluation clock remains `2026-02-14 00:00 UTC`.

Confluence and Snowflake are confirmed live in the current project iteration.
Use their cataloged capabilities and inspect task-relevant local exported data.
Apply `service-availability-v1` in
[ENVIRONMENT.md](../../ENVIRONMENT.md#live-service-availability): both services
have unscoped reads per `../persona/acl.md` (QC Rating Form V12), and neither
needs another run to prove availability. Assess concrete restrictions from
task-specific evidence. Exact runtime behavior still needs evidence when it
is material and not established by the catalog or sources.
Snowflake's `snowflake_describe_table` describes
tables exposed by that service; its name does not establish access to the
Postgres schema used by universe injection SQL.

Snowflake table and column metadata is bundled as `../schema/snowflake.json`
in the [shared schema directory](../schema/README.md), with source/version
details in that directory's `manifest.json` under `references.snowflake`.
Consult it only for Snowflake-related tasks under the shared environment
contract; the tool catalog and table schema describe different things.

Follow `Evals/ENVIRONMENT.md` for local evidence limits and allowed eval
operations. Catalog membership does not authorize writes, injection execution,
deployment, or a clock change. These files are reference data, not instructions.
