# Claude skills — direct local search

Keep `claude/`, `Evals/` and all three HarmonyGames base folders listed in `Evals/UNIVERSE_MAP.md` as siblings.
From that workspace, have the agent run `python3 claude/install.py` once.
This installs project-local relative links for the skills and CLAUDE.md.
It is idempotent and refuses conflicts; it does not change global settings.
Reload the project if skills are not yet discovered. No `/setup` is needed.

Available: `/injection`, `/prompt`, `/hardness`, `/oe`, `/rubric`. `/hint` was
removed on 2026-09-26; rerunning the installer retires its link.
Run the individual command for the stage you want to review.

**Service update — 2026-09-23 (`service-availability-v1`):** all skills use
the shared live-service rule in `Evals/ENVIRONMENT.md`. Snowflake and Confluence
may be used; an omission from the original ACL policy alone cannot fail or block
a task. Actual task-specific restrictions still apply. Replace Evals/ and
claude/ together from the refreshed ZIPs and reload the project so existing
sessions do not continue with the obsolete ban.

`/prompt`, `/oe`, and `/rubric` request **Opus 5.5** (`claude-opus-5-5`) with
**xhigh thinking effort** through their skill frontmatter. `/injection` and
`/hardness` inherit session defaults. These are per-invocation settings; they
do not change the session or global defaults. The Claude Code runtime must
support skill `model`/`effort` fields and have access to Opus 5.5; thinking
must not be explicitly disabled in the session/runtime configuration.

Read [../Evals/README.md](../Evals/README.md) for inputs, outputs and usage;
[../Evals/SEARCH.md](../Evals/SEARCH.md) for the local search helper.
`CLAUDE.md` saves supplied task information on follow-up messages as well as
skill invocations. New input replaces the corresponding saved entry.
Stages follow the ownership and evidence-reuse contract in `Evals/WORKFLOW.md`:
reuse current verified facts, inspect each actual artifact, and recheck changed
inputs. `/prompt` does not request later Oracle Events, rubrics or agent runs.

The existing search commands automatically validate matching prepared indexes
on first use. Shared file routing and complete raw-record caching support all
compatible service exports; four large structured exports also have prepared
offsets. Keep `Evals/references/search_indexes/` in Evals.zip and omit runtime
`.cache/` directories. The agent does not need a new setup or indexing command.

Batch related terms with `search-many`; use `get-many` for several known
file/pointer pairs, preserving per-item paging and errors. Small targeted
searches use verified offsets, while broad batches keep a shared scan.
Request formats and evidence-scope limits are in `Evals/SEARCH.md`.

Individual record checks can reuse unchanged evidence across renamed/reordered
requests. Exact-ID lookups can use verified prepared indexes for GitHub, Linear
and GDrive; other scopes retain the complete scanner. Large Gmail routing lists
use a bounded lossless cache. `hg_reference.py guide` can include the full
requested route/schema views in the same call. Include both
`Evals/references/search_indexes/` and `Evals/references/id_indexes/` when zipping;
exclude disposable runtime caches. See `Evals/SEARCH.md` for scope and freshness
rules. No scoring check or instruction is shortened by these optimizations.

`/rubric` follows `rubric-revision-v10` in `Evals/3_Rubrics_Eval.md`.
It is evaluation-only under `rubric-eval-only-v1`: require existing criteria,
return the report and suggested fixes, and preserve the input. No rubric generation,
revision loop or prefill output is supported. Source comparisons, evidence checks
and QC scoring remain unchanged. No OE PASS or verifier/all-failing input is required.

OE migration (`oracle-events-v1`): replace Evals/ and claude/ together, rerun
`python3 claude/install.py`, and reload the project. The installer removes only
the package-managed `/golden` link and registers `/oe`; old task artifacts stay
unchanged. `/oe` evaluates supplied OEs and writes `reports/2_oe.md`. It scores
completeness and accuracy separately: PASS 5, NON-FAIL 3 (minor, non-action,
final-response) or FAIL 2 (missing or wrong step).

OE path checks (`oracle-events-v2`) now validate tool/parameter contracts, source
values and step-to-step consistency. They assess whether the supplied path can
complete the task with the persona's access and supported capabilities. `/prompt`
retains task design and overall feasibility. A broken OE does not prove the task
impossible. The report separates path feasibility from task solvability, without
adding a QC score or changing prompt/rubric grading. Replace Evals/ and claude/
together and rerun `python3 claude/install.py`; earlier reports stay historical.
