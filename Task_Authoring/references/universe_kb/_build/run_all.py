"""Rebuild every universe_kb output in dependency order (stdlib only; ~10 min, peak RSS < 2 GB).
Run from anywhere:  python3 Task_Authoring/references/universe_kb/_build/run_all.py --task-dir <task folder>
Needs ../entities.json (built by Task_Authoring/tools/entity.py) before assemble_activity."""
import argparse, runpy, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
STEPS = ["pass_slack", "pass_github_linear", "pass_gmail", "pass_gmail_copies", "pass_other", "pass_beats", "pass_slack_claims",
         "assemble_activity", "assemble_hazards_traps", "assemble_cohorts", "assemble_integrations_conventions", "assemble_timeline", "render_md"]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-dir", default=os.environ.get("TASK_AUTHORING_TASK_DIR",
                        os.path.abspath(os.path.join(HERE, "../../../task_inputs"))))
    parser.add_argument("steps", nargs="*", choices=STEPS)
    args = parser.parse_args(argv)
    sys.path.insert(0, os.path.abspath(os.path.join(HERE, "../../../tools")))
    from task_context import load_context, ContextError
    try:
        # Validate the configured source before importing common. Both assigned
        # dates can intentionally share that export; the assigned freeze remains
        # separate and an earlier-date rebuild has its own output directory.
        task_dir = os.path.abspath(args.task_dir)
        context = load_context(task_dir, require_source=True)
    except ContextError as error:
        parser.exit(2, "KB SOURCE BLOCKED: " + str(error) + "\n")
    os.environ["TASK_AUTHORING_TASK_DIR"] = task_dir
    sys.path.insert(0, HERE)
    existing = sys.modules.get("common")
    if existing and getattr(existing, "CONTEXT", {}).get("context_hash") != context["context_hash"]:
        parser.exit(2, "KB SOURCE BLOCKED: start a fresh builder process when changing task context\n")
    import common  # noqa: F401 - validates static-reference review before running any pass
    os.chdir(HERE)
    for step in (args.steps or STEPS):
        started = time.time()
        runpy.run_path(os.path.join(HERE, step + ".py"), run_name="__main__")
        print("%-36s %6.1fs" % (step, time.time() - started), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
