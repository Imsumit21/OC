"""Shared CLI and ownership checks for workspace-local skill registration."""
from __future__ import annotations

import argparse
from pathlib import Path


def arguments(description: str) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--target", choices=("claude", "codex", "both"), default="claude",
                        help="Skill registry to update (default: claude).")
    parser.add_argument("--dry-run", action="store_true", help="Preview without changing files.")
    return parser.parse_args()


def targets(root: Path, selection: str) -> dict[str, Path]:
    registries = {"claude": root / ".claude" / "skills",
                  "codex": root / ".agents" / "skills"}
    selected = registries if selection == "both" else {selection: registries[selection]}
    # Relative links and selective pruning require real workspace-local directories.
    # Validate every selected registry before either script makes any changes.
    for target in selected.values():
        for directory in (target.parent, target):
            if directory.is_symlink():
                raise ValueError(f"Refusing a symlinked skill registry directory: {directory}")
            if directory.exists() and not directory.is_dir():
                raise ValueError(f"Skill registry directory is occupied by a file: {directory}")
    return selected


def owned_link(link: Path, source: Path) -> bool:
    """A same-named file/directory or a link to another bundle is never ours."""
    try:
        return link.is_symlink() and link.resolve() == source.resolve()
    except (OSError, RuntimeError):
        return False
