"""Every authoring skill has an OpenCode slash command, `.opencode/commands/<skill>.md`, that loads it."""
from __future__ import annotations

from pathlib import Path
import re
import unittest


BUNDLE = Path(__file__).resolve().parents[1]
COMMANDS = BUNDLE.parent / ".opencode" / "commands"
GOOD = "---\ndescription: Design the task\n---\nLoad the `create-x` skill with the skill tool and follow it.\n\n$ARGUMENTS\n"


def skills():
    return sorted(p.parent.name for p in (BUNDLE / "skills").glob("*/SKILL.md"))


def split(text):
    """(front matter, body) of a command file, or (None, text) when it has no front matter."""
    head, sep, body = text.partition("\n---\n")
    if not text.startswith("---\n") or not sep:
        return None, text
    return head[4:], body


def problems(name, text):
    """Why a command file would not run skill `name` as written; empty when it would."""
    front, body = split(text)
    if front is None:
        return ["missing front matter"]
    found = []
    # One plain description line and nothing else: any other key (agent, model, subagent, template), however it is
    # quoted or spaced, would change how OpenCode runs the skill; the body is the template.
    match = re.fullmatch(r"description: ([A-Za-z0-9][^\n]*)", front)
    if not match:
        found.append("front matter is not exactly one plain 'description: ...' line")
    elif re.search(r":(\s|$)| #", match.group(1)):
        found.append("the description is not one plain YAML string (': ' or ' #' inside)")
    if f"Load the `{name}` skill with the skill tool and follow it." not in body:
        found.append("the body does not load its own skill")
    if "$ARGUMENTS" not in body:
        found.append("the body does not pass $ARGUMENTS")
    if "!`" in body:
        found.append("the body runs a shell block, which OpenCode runs outside the permission flow")
    return found


class OpencodeCommandTests(unittest.TestCase):
    def test_every_skill_has_a_command(self):
        self.assertTrue(skills())
        self.assertEqual([name for name in skills() if not (COMMANDS / f"{name}.md").is_file()], [])

    def test_no_create_command_without_a_skill(self):
        self.assertEqual(sorted(p.stem for p in COMMANDS.glob("create-*.md") if p.stem not in skills()), [])

    def test_each_command_loads_its_own_skill_with_the_arguments(self):
        for name in skills():
            with self.subTest(skill=name):
                self.assertEqual(problems(name, (COMMANDS / f"{name}.md").read_text(encoding="utf-8")), [])

    def test_the_guard_rejects_commands_that_would_run_differently(self):
        self.assertEqual(problems("create-x", GOOD), [])
        bad = {
            "quoted key": GOOD.replace("Design the task\n", 'Design the task\n"subagent": true\n'),
            "space before the colon": GOOD.replace("Design the task\n", "Design the task\nagent : build\n"),
            "flow mapping": GOOD.replace("description: Design the task", "{description: Design the task, model: x}"),
            "comment": GOOD.replace("Design the task", "Design the task # note"),
            "colon in the description": GOOD.replace("Design the task", "Design: the task"),
            "no front matter": GOOD.split("---\n", 2)[2],
            "another skill": GOOD.replace("`create-x`", "`create-y`"),
            "no arguments": GOOD.replace("$ARGUMENTS", "args"),
            "shell block": GOOD.replace("$ARGUMENTS", "$ARGUMENTS !`git status`"),
        }
        for label, text in bad.items():
            with self.subTest(label):
                self.assertTrue(problems("create-x", text), text)


if __name__ == "__main__":
    unittest.main()
