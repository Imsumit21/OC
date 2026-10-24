-- ============================================================================================
-- extract_schema.sql — read-only schema export of the universe database (PostgreSQL).
-- Run each query in the platform's Universe Explorer (Database → Query → Run Query).
-- Every statement is a SELECT: nothing is created, changed or deleted.
--
-- Save the outputs inside Task_Authoring/references/ (JSON cell → file):
--   Q1 → universe_schema_live.json        tables + columns (tools/sql_lint.py reads this file)
--   Q2 → universe_constraints_live.json   primary keys, unique, foreign keys, checks
--   Q3 → universe_indexes_live.json       all indexes (incl. unique indexes not declared as constraints)
--   Q4 → universe_enums_live.json         enum types and their allowed values
--   Q5 → universe_triggers_live.json      triggers (side effects of an INSERT/UPDATE: counters, changelog)
--   Q6 → universe_rowcounts_live.json     approximate rows per table
-- If the Explorer truncates a large cell, uncomment the schema filter in Q1/Q2
-- (e.g. AND c.table_schema = 'slack') and run once per schema; merge the arrays.
-- ============================================================================================


-- Q1 · Tables and columns (one JSON cell → references/universe_schema_live.json) ---------------
SELECT json_agg(t ORDER BY t.table_schema, t.table_name) AS schema_json
FROM (
    SELECT c.table_schema,
           c.table_name,
           json_agg(json_build_object(
               'column',     c.column_name,
               'type',       c.data_type,               -- e.g. character varying, jsonb, boolean, ARRAY, USER-DEFINED
               'udt',        c.udt_name,                -- underlying type (enum name, _text for text[], …)
               'default',    c.column_default,
               'nullable',   c.is_nullable,             -- 'YES' / 'NO'
               'position',   c.ordinal_position,
               'max_length', c.character_maximum_length,
               'generated',  c.is_generated,            -- 'ALWAYS' = computed column: never insert into it
               'identity',   c.is_identity
           ) ORDER BY c.ordinal_position) AS columns
    FROM information_schema.columns c
    JOIN information_schema.tables tb
      ON tb.table_schema = c.table_schema
     AND tb.table_name   = c.table_name
    WHERE tb.table_type = 'BASE TABLE'
      AND c.table_schema NOT IN ('pg_catalog', 'information_schema', 'pg_toast')
      -- AND c.table_schema = 'slack'
    GROUP BY c.table_schema, c.table_name
) t;


-- Q2 · Constraints: PRIMARY KEY, UNIQUE, FOREIGN KEY, CHECK ------------------------------------
SELECT json_agg(x ORDER BY x.table_schema, x.table_name, x.kind, x.name) AS constraints_json
FROM (
    SELECT n.nspname  AS table_schema,
           cl.relname AS table_name,
           con.conname AS name,
           CASE con.contype WHEN 'p' THEN 'PRIMARY KEY' WHEN 'u' THEN 'UNIQUE'
                            WHEN 'f' THEN 'FOREIGN KEY' WHEN 'c' THEN 'CHECK'
                            WHEN 'x' THEN 'EXCLUDE' ELSE con.contype::text END AS kind,
           (SELECT json_agg(a.attname ORDER BY k.ord)
              FROM unnest(con.conkey) WITH ORDINALITY AS k(attnum, ord)
              JOIN pg_attribute a ON a.attrelid = con.conrelid AND a.attnum = k.attnum) AS columns,
           pg_get_constraintdef(con.oid) AS definition      -- FK target table/columns, CHECK expression
    FROM pg_constraint con
    JOIN pg_class cl     ON cl.oid = con.conrelid
    JOIN pg_namespace n  ON n.oid  = cl.relnamespace
    WHERE n.nspname NOT IN ('pg_catalog', 'information_schema', 'pg_toast')
      -- AND n.nspname = 'slack'
) x;


-- Q3 · Indexes (a UNIQUE index enforces uniqueness even without a declared constraint) ---------
SELECT json_agg(json_build_object(
           'table_schema', schemaname, 'table_name', tablename,
           'index', indexname, 'definition', indexdef)
       ORDER BY schemaname, tablename, indexname) AS indexes_json
FROM pg_indexes
WHERE schemaname NOT IN ('pg_catalog', 'information_schema', 'pg_toast');


-- Q4 · Enum types and allowed values -----------------------------------------------------------
SELECT json_agg(json_build_object(
           'schema', n.nspname, 'type', t.typname,
           'values', (SELECT json_agg(e.enumlabel ORDER BY e.enumsortorder)
                        FROM pg_enum e WHERE e.enumtypid = t.oid))
       ORDER BY n.nspname, t.typname) AS enums_json
FROM pg_type t
JOIN pg_namespace n ON n.oid = t.typnamespace
WHERE t.typtype = 'e';


-- Q5 · Triggers (what else changes when you INSERT/UPDATE) -------------------------------------
SELECT json_agg(json_build_object(
           'table_schema', event_object_schema, 'table_name', event_object_table,
           'trigger', trigger_name, 'timing', action_timing,
           'event', event_manipulation, 'action', action_statement)
       ORDER BY event_object_schema, event_object_table, trigger_name) AS triggers_json
FROM information_schema.triggers;


-- Q6 · Approximate row counts per table --------------------------------------------------------
SELECT json_agg(json_build_object(
           'table_schema', schemaname, 'table_name', relname, 'approx_rows', n_live_tup)
       ORDER BY schemaname, relname) AS rowcounts_json
FROM pg_stat_user_tables;


-- Q7 · Same as Q1 as a plain table, for reading by eye (not for the tools) ---------------------
SELECT c.table_schema, c.table_name, c.ordinal_position AS pos, c.column_name,
       c.data_type, c.udt_name, c.is_nullable, c.column_default
FROM information_schema.columns c
JOIN information_schema.tables t
  ON t.table_schema = c.table_schema AND t.table_name = c.table_name
WHERE t.table_type = 'BASE TABLE'
  AND c.table_schema NOT IN ('pg_catalog', 'information_schema', 'pg_toast')
  -- AND c.table_schema = 'slack'
ORDER BY c.table_schema, c.table_name, c.ordinal_position;
