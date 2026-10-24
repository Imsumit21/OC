# Persona and ACL references

Use `roster.json` for exact persona keys, names, emails, roles and departments,
and `acl.md` for the existing identity and read-access rules.

The roster is copied byte for byte from the existing reference and currently
contains 17 personas. Existing read-filtering rules are preserved; the policy
adds the current live-service clarification for Snowflake and Confluence.
`manifest.json` retains original source hashes and current bundled hashes.
Read the actual roster instead of relying on a memorized member count.

The access matrix lists seven scoped and six unscoped services. Snowflake and
Confluence moved from "not specified" to unscoped on 2026-09-27, following QC
Rating Form V12 (Prompt - Feasibility). Both are live under `service-availability-v1`
in [ENVIRONMENT.md](../../ENVIRONMENT.md#live-service-availability). Assess
actual task-specific restrictions from evidence. The complete capability inventory is in `../tools/catalog.json`.

User-supplied task assignment details stay in
`Evals/task_inputs/00_Task_Assigned_Inputs.md`. Roster lookups can verify those
details, but inferred or resolved fields must not be saved as if the user
supplied them. Record the distinction in the evaluation report.
