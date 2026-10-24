#!/usr/bin/env python3
"""Remove this bundle's skill symlinks for Claude, Codex, or both.

The default remains Claude. Removes only links resolving to this bundle's current
skill folders and prunes empty registry directories. Real files/directories,
unrelated skills, project instructions, source data, and global settings stay intact.

    python3 Task_Authoring/setup/uninstall.py --target codex --dry-run
    python3 Task_Authoring/setup/uninstall.py --target codex
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from skill_links import arguments, owned_link, targets


def main() -> int:
    args = arguments(__doc__)
    bundle = Path(__file__).resolve().parent.parent
    root = bundle.parent
    source = bundle / "skills"
    if not source.is_dir():
        print("No bundle skills/ found; nothing to unregister.", file=sys.stderr)
        return 1

    selected = targets(root, args.target)
    names = sorted(p.parent.name for p in source.glob("*/SKILL.md"))
    reports: dict[str, dict] = {}
    remove_key = "would_remove" if args.dry_run else "removed_links"
    prune_key = "would_prune" if args.dry_run else "pruned_empty_dirs"
    for agent, target in selected.items():
        removed, left_untouched = [], []
        for name in names:
            link = target / name
            if not (link.is_symlink() or link.exists()):
                continue
            if owned_link(link, source / name):
                if not args.dry_run:
                    link.unlink()
                removed.append(name)
            else:
                left_untouched.append(name)

        pruned = []
        simulated_removed = {target / name for name in removed}
        for directory in (target, target.parent):
            if not directory.is_dir():
                continue
            if args.dry_run:
                empty = all(child in simulated_removed for child in directory.iterdir())
                if empty:
                    simulated_removed.add(directory)
                    pruned.append(str(directory.relative_to(root)))
            else:
                try:
                    directory.rmdir()  # Fails harmlessly if any unrelated entry remains.
                except OSError:
                    continue
                pruned.append(str(directory.relative_to(root)))
        reports[agent] = {"path": str(target), remove_key: removed,
                          "left_untouched": left_untouched, prune_key: pruned}

    result = {
        "workspace": str(root), "dry_run": args.dry_run, "target": args.target,
        "targets": reports,
        "note": ("DRY RUN — no changes made. " if args.dry_run else "")
        + "Only this bundle's selected skill symlinks removed; unrelated files and settings untouched.",
    }
    if len(reports) == 1:
        report = next(iter(reports.values()))
        result.update({key: report[key] for key in (remove_key, "left_untouched", prune_key)})
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as error:
        print(f"Uninstall failed: {error}", file=sys.stderr)
        raise SystemExit(1)
