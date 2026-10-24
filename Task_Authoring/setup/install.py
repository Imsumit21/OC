#!/usr/bin/env python3
"""Register shared authoring skills for Claude, Codex, or both in this workspace.

Creates relative folder symlinks in .claude/skills (Claude) or .agents/skills
(Codex). The default remains Claude. All destinations are checked before creating
directories or links; existing conflicting entries are never replaced.

    python3 Task_Authoring/setup/install.py --target both --dry-run
    python3 Task_Authoring/setup/install.py --target both

The script locates the workspace from its own resolved path, independently of cwd.
It never changes global settings, Evals/, claude/, or the universe exports.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from skill_links import arguments, owned_link, targets


def main() -> int:
    args = arguments(__doc__)
    bundle = Path(__file__).resolve().parent.parent
    root = bundle.parent
    source = bundle / "skills"

    if not (root / "Evals").is_dir() or not source.is_dir():
        print("Keep the authoring bundle beside the sandbox Evals/ in the workspace.",
              file=sys.stderr)
        return 1
    definitions = sorted(source.glob("*/SKILL.md"))
    if not definitions:
        print(f"No authoring skills found under {source}.", file=sys.stderr)
        return 1

    selected = targets(root, args.target)
    pending: list[tuple[Path, str]] = []
    reports: dict[str, dict] = {}
    create_key = "would_create" if args.dry_run else "new_links"
    for agent, target in selected.items():
        report = {"path": str(target), create_key: [], "already_linked": []}
        for definition in definitions:
            name = definition.parent.name
            destination = target / name
            if destination.is_symlink() or destination.exists():
                if not owned_link(destination, definition.parent):
                    print(f"Existing skill conflicts; no links changed: {destination}",
                          file=sys.stderr)
                    return 1
                report["already_linked"].append(name)
            else:
                link = os.path.relpath(definition.parent, start=target)
                pending.append((destination, link))
                report[create_key].append(name)
        reports[agent] = report

    if not args.dry_run:
        for target in selected.values():
            target.mkdir(parents=True, exist_ok=True)
        for destination, link in pending:
            destination.symlink_to(link, target_is_directory=True)

    result = {
        "workspace": str(root), "dry_run": args.dry_run, "target": args.target,
        "registered_skills": [d.parent.name for d in definitions], "targets": reports,
        "note": ("DRY RUN — no changes made. " if args.dry_run else "")
        + "Only selected workspace skill symlinks registered; source data and global settings untouched.",
    }
    if len(reports) == 1:  # Retain the original single-target summary fields.
        report = next(iter(reports.values()))
        result.update({create_key: report[create_key], "already_linked": report["already_linked"]})
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as error:
        print(f"Skill registration failed: {error}", file=sys.stderr)
        raise SystemExit(1)
