#!/usr/bin/env python3
"""Register skills and task input instructions without changing global settings."""

import json
from pathlib import Path
import sys

RETIRED = ("golden", "hint")


def install(root):
    root = Path(root).resolve()
    source = root / "claude" / "skills"
    if not (root / "Evals" / "WORKFLOW.md").is_file() or not source.is_dir():
        raise ValueError("Keep Evals/ and claude/ beside each other in the workspace.")
    # Overlay extraction can leave a retired definition on disk. Never register
    # it again; only the link created by this package is eligible for removal.
    definitions = sorted(p for p in source.glob("*/SKILL.md") if p.parent.name not in RETIRED)
    if not definitions:
        raise ValueError("No supplied skills found.")
    target = root / ".claude" / "skills"
    try:
        target.resolve().relative_to(root)
    except ValueError:
        raise ValueError("Refusing to register through a .claude path outside this workspace.")
    pending = []
    remove = []
    for name in RETIRED:
        retired = target / name
        managed = retired.is_symlink() and retired.resolve() == (source / name).resolve()
        if (retired.exists() or retired.is_symlink()) and not managed:
            raise ValueError(f"Existing {name} skill is not package-managed; no links changed: {retired}")
        if managed:
            remove.append(retired)
    for definition in definitions:
        name = definition.parent.name
        destination = target / name
        if destination.exists() or destination.is_symlink():
            if destination.resolve() != definition.parent.resolve():
                raise ValueError(f"Existing skill conflicts; no links changed: {destination}")
        else:
            pending.append((destination, name))
    instructions = root / "claude" / "CLAUDE.md"
    instruction_target = root / ".claude" / "CLAUDE.md"
    if not instructions.is_file():
        raise ValueError("Missing claude/CLAUDE.md task input instructions.")
    add_instructions = not (instruction_target.exists() or instruction_target.is_symlink())
    if not add_instructions and instruction_target.resolve() != instructions.resolve():
        raise ValueError(f"Existing project instructions conflict; no links changed: {instruction_target}")
    target.mkdir(parents=True, exist_ok=True)
    for retired in remove:
        retired.unlink()
    for destination, name in pending:
        destination.symlink_to(Path("../../claude/skills") / name, target_is_directory=True)
    if add_instructions:
        instruction_target.symlink_to(Path("../claude/CLAUDE.md"))
    return {
        "workspace": str(root),
        "registered_skills": [p.parent.name for p in definitions],
        "new_links": len(pending),
        "retired_links": [p.name for p in remove],
        "input_instructions": str(instruction_target),
        "new_instruction_link": add_instructions,
    }


def main():
    try:
        result = install(Path(__file__).resolve().parent.parent)
    except (OSError, ValueError) as error:
        print(f"Skill registration failed: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
