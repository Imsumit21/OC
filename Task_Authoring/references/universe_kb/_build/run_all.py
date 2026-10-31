"""Rebuild one universe's universe_kb outputs in dependency order (stdlib only; ~10 min, peak RSS < 2 GB).

Per-universe contract: one run builds exactly one universe, selected by the activated task
context (`universe.key`, `source.paths`, `source.kb_output_path`). Outputs go only to
`source.kb_output_path`; the legacy `references/universe_kb/` root is never written. A run
refuses a not-ready source (naming the missing universe folder) and refuses to switch
universe mid-process.

Run from anywhere:  python3 Task_Authoring/references/universe_kb/_build/run_all.py --task-dir <task folder>
Needs <source.kb_output_path>/entities.json (built by Task_Authoring/tools/entity.py build in the
same task context) before assemble_activity.
"""
import argparse, runpy, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
STEPS = ["pass_slack", "pass_github_linear", "pass_gmail", "pass_gmail_copies", "pass_other", "pass_beats", "pass_slack_claims",
         "assemble_activity", "assemble_hazards_traps", "assemble_cohorts", "assemble_integrations_conventions", "assemble_timeline", "render_md"]


def universe_contract(context):
    """Validate one-universe-per-run and return (key, kb_output_path); raise ValueError with the reason."""
    universe = context.get("universe") or {}
    source = context.get("source") or {}
    key = universe.get("key") or source.get("universe")
    if not key:
        raise ValueError("the task context has no universe; select a task date first")
    if source.get("status") != "ready":
        folder, prefix = universe.get("folder"), universe.get("prefix")
        hint = ("install %s/%s_HarmonyGames_* per Evals/UNIVERSE_MAP.md" % (folder, prefix)
                if folder and prefix else "install the %s universe data per Evals/UNIVERSE_MAP.md" % key)
        raise ValueError("%s source is %s (%s); %s" % (key, source.get("status") or "missing",
                                                       source.get("reason") or "no validated export", hint))
    output = source.get("kb_output_path")
    if not output:
        raise ValueError("universe %s has no source.kb_output_path; one universe writes one folder" % key)
    active = os.environ.get("TASK_AUTHORING_UNIVERSE")
    if active and active != key:
        raise ValueError("TASK_AUTHORING_UNIVERSE=%s but the context selects %s; one universe per run" % (active, key))
    return key, output


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-dir", default=os.environ.get("TASK_AUTHORING_TASK_DIR",
                        os.path.abspath(os.path.join(HERE, "../../../task_inputs"))))
    parser.add_argument("steps", nargs="*", choices=STEPS)
    args = parser.parse_args(argv)
    sys.path.insert(0, os.path.abspath(os.path.join(HERE, "../../../tools")))
    from task_context import load_context, ContextError
    try:
        task_dir = os.path.abspath(args.task_dir)
        context = load_context(task_dir, require_source=True)
        universe, output = universe_contract(context)
    except (ContextError, ValueError) as error:
        parser.exit(2, "KB SOURCE BLOCKED: " + str(error) + "\n")
    os.environ["TASK_AUTHORING_TASK_DIR"] = task_dir
    sys.path.insert(0, HERE)
    existing = sys.modules.get("common")
    if existing and getattr(existing, "CONTEXT", {}).get("context_hash") != context["context_hash"]:
        parser.exit(2, "KB SOURCE BLOCKED: start a fresh builder process when changing task context\n")
    import common  # noqa: F401 - validates static-reference review before running any pass
    if common.UNIVERSE_KEY != universe or os.path.realpath(common.OUT) != os.path.realpath(output):
        parser.exit(2, "KB SOURCE BLOCKED: builder resolved %s -> %s, not the context universe %s -> %s\n"
                    % (getattr(common, "UNIVERSE_KEY", "?"), getattr(common, "OUT", "?"), universe, output))
    os.chdir(HERE)
    steps = args.steps or STEPS
    publishes = [s for s in steps if s.startswith("assemble_") or s == "render_md"]
    if publishes and not os.path.isfile(os.path.join(output, "entities.json")):
        parser.exit(2, "KB SOURCE BLOCKED: %s/entities.json missing for universe %s; run "
                    "`python3 Task_Authoring/tools/entity.py build` in the same task context first\n"
                    % (output, universe))
    if publishes:
        common.jload_kb("entities.json")   # a stale or foreign entities.json stops the run before any step
    for step in steps:
        started = time.time()
        runpy.run_path(os.path.join(HERE, step + ".py"), run_name="__main__")
        print("%-36s %6.1fs" % (step, time.time() - started), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
