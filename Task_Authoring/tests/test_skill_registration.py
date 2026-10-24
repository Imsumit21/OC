"""Exercise the real registration CLIs against disposable workspace trees."""
from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SETUP = Path(__file__).resolve().parents[1] / "setup"
SKILLS = ("create-alpha", "create-zeta")


class SkillRegistrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="skill-registration-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve() / "workspace with spaces"
        self.root.mkdir()
        self.bundle = self.root / "Renamed Authoring"
        (self.bundle / "setup").mkdir(parents=True)
        for name in ("install.py", "uninstall.py", "skill_links.py"):
            shutil.copy2(SETUP / name, self.bundle / "setup" / name)
        for name in SKILLS:
            skill = self.bundle / "skills" / name
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text(f"---\nname: {name}\ndescription: Test skill\n---\n")
        (self.root / "Evals").mkdir()
        (self.root / "Evals" / "sentinel").write_text("read-only fixture")

    def cli(self, script="install", *args, ok=True):
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        result = subprocess.run(
            [sys.executable, "-B", str(self.bundle / "setup" / f"{script}.py"), *args],
            cwd=self.tmp.name, env=env, text=True, capture_output=True,
        )
        if ok:
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((self.root / "Evals" / "sentinel").read_text(), "read-only fixture")
            return json.loads(result.stdout)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        return result

    def registry(self, agent):
        return self.root / (".claude" if agent == "claude" else ".agents") / "skills"

    def assert_links(self, agent):
        for name in SKILLS:
            link = self.registry(agent) / name
            self.assertTrue(link.is_symlink(), str(link))
            self.assertFalse(link.readlink().is_absolute())
            self.assertEqual(link.resolve(), self.bundle / "skills" / name)
            self.assertEqual((link / "SKILL.md").read_bytes(),
                             (self.bundle / "skills" / name / "SKILL.md").read_bytes())

    def test_default_remains_claude_and_reinstall_is_idempotent(self):
        first = self.cli()
        self.assertEqual(first["new_links"], list(SKILLS))
        self.assert_links("claude")
        self.assertFalse(self.registry("codex").parent.exists())
        links = {name: (self.registry("claude") / name).lstat().st_mtime_ns for name in SKILLS}
        second = self.cli()
        self.assertEqual(second["new_links"], [])
        self.assertEqual(second["already_linked"], list(SKILLS))
        self.assertEqual(links, {name: (self.registry("claude") / name).lstat().st_mtime_ns
                                 for name in SKILLS})

    def test_codex_only_and_both_share_live_source(self):
        self.cli("install", "--target", "codex")
        self.assert_links("codex")
        self.assertFalse(self.registry("claude").parent.exists())
        both = self.cli("install", "--target", "both")
        self.assertEqual(both["targets"]["codex"]["new_links"], [])
        self.assertEqual(both["targets"]["claude"]["new_links"], list(SKILLS))
        self.assert_links("claude")
        source = self.bundle / "skills" / SKILLS[0] / "SKILL.md"
        source.write_text(source.read_text() + "\nUpdated source\n")
        for agent in ("claude", "codex"):
            self.assertEqual((self.registry(agent) / SKILLS[0] / "SKILL.md").read_bytes(),
                             source.read_bytes())

    def test_both_install_dry_run_creates_nothing(self):
        report = self.cli("install", "--target", "both", "--dry-run")
        for agent in ("claude", "codex"):
            self.assertEqual(report["targets"][agent]["would_create"], list(SKILLS))
            self.assertFalse(self.registry(agent).parent.exists())

    def test_conflicts_abort_all_targets_before_creating_links(self):
        target = self.registry("codex")
        target.mkdir(parents=True)
        conflict = target / SKILLS[-1]
        conflict.write_text("user file")
        result = self.cli("install", "--target", "both", ok=False)
        self.assertIn("conflicts", result.stderr)
        self.assertEqual(conflict.read_text(), "user file")
        self.assertEqual(list(target.iterdir()), [conflict])
        self.assertFalse(self.registry("claude").parent.exists())

    def test_dangling_links_and_real_skill_directories_are_conflicts(self):
        target = self.registry("codex")
        target.mkdir(parents=True)
        conflict = target / SKILLS[0]
        conflict.symlink_to("missing-folder", target_is_directory=True)
        self.cli("install", "--target", "codex", ok=False)
        self.assertEqual(conflict.readlink(), Path("missing-folder"))
        conflict.unlink()
        conflict.mkdir()
        (conflict / "SKILL.md").write_text("user skill")
        self.cli("install", "--target", "codex", ok=False)
        self.assertEqual((conflict / "SKILL.md").read_text(), "user skill")
        self.assertFalse((target / SKILLS[-1]).exists())

    def test_selective_uninstall_preserves_other_target_and_config(self):
        self.cli("install", "--target", "both")
        config = self.registry("codex").parent / "config.txt"
        config.write_text("user config")
        report = self.cli("uninstall", "--target", "codex")
        self.assertEqual(report["removed_links"], list(SKILLS))
        self.assertEqual(report["pruned_empty_dirs"], [".agents/skills"])
        self.assertEqual(config.read_text(), "user config")
        self.assert_links("claude")
        self.assertEqual(self.cli("uninstall", "--target", "codex")["removed_links"], [])

    def test_uninstall_keeps_unmanaged_entries_and_unrelated_skills(self):
        self.cli("install", "--target", "codex")
        target = self.registry("codex")
        (target / SKILLS[0]).unlink()
        (target / SKILLS[0]).mkdir()
        (target / SKILLS[0] / "SKILL.md").write_text("user skill")
        unrelated = target / "unrelated"
        unrelated.symlink_to(self.bundle / "skills" / SKILLS[-1], target_is_directory=True)
        report = self.cli("uninstall", "--target", "codex")
        self.assertEqual(report["left_untouched"], [SKILLS[0]])
        self.assertEqual(report["removed_links"], [SKILLS[-1]])
        self.assertTrue(unrelated.is_symlink())
        self.assertEqual((target / SKILLS[0] / "SKILL.md").read_text(), "user skill")

    def test_uninstall_default_remains_claude(self):
        self.cli("install", "--target", "both")
        self.cli("uninstall")
        self.assertFalse(self.registry("claude").parent.exists())
        self.assert_links("codex")

    def test_uninstall_dry_run_matches_real_pruning_and_is_idempotent(self):
        self.cli("install", "--target", "both")
        preview = self.cli("uninstall", "--target", "both", "--dry-run")
        for agent in ("claude", "codex"):
            self.assert_links(agent)
        actual = self.cli("uninstall", "--target", "both")
        for agent in ("claude", "codex"):
            self.assertEqual(preview["targets"][agent]["would_remove"],
                             actual["targets"][agent]["removed_links"])
            self.assertEqual(preview["targets"][agent]["would_prune"],
                             actual["targets"][agent]["pruned_empty_dirs"])
            self.assertFalse(self.registry(agent).parent.exists())
        again = self.cli("uninstall", "--target", "both")
        self.assertTrue(all(r["removed_links"] == [] for r in again["targets"].values()))

    def test_relative_links_survive_moving_workspace(self):
        self.cli("install", "--target", "both")
        moved = self.root.with_name("moved workspace")
        self.root.rename(moved)
        self.root = moved
        self.bundle = moved / self.bundle.name
        for agent in ("claude", "codex"):
            self.assert_links(agent)
        self.assertTrue(all(r["new_links"] == [] for r in
                            self.cli("install", "--target", "both")["targets"].values()))

    def test_registry_symlinks_are_rejected_before_either_target_changes(self):
        for component in (".agents", ".agents/skills"):
            with self.subTest(component=component):
                external = Path(self.tmp.name) / "other registry"
                external.mkdir(exist_ok=True)
                link = self.root / component
                link.parent.mkdir(parents=True, exist_ok=True)
                link.symlink_to(external, target_is_directory=True)
                for script in ("install", "uninstall"):
                    result = self.cli(script, "--target", "both", ok=False)
                    self.assertIn("symlinked skill registry", result.stderr)
                    self.assertFalse(self.registry("claude").parent.exists())
                    self.assertEqual(list(external.iterdir()), [])
                link.unlink()
                if component.endswith("/skills"):
                    link.parent.rmdir()

    def test_registry_files_and_invalid_options_are_rejected(self):
        for script in ("install", "uninstall"):
            for args in (("--target", "unknown"), ("--typo",)):
                self.cli(script, *args, ok=False)
        self.registry("codex").parent.write_text("user file")
        for script in ("install", "uninstall"):
            self.cli(script, "--target", "both", ok=False)
        self.assertFalse(self.registry("claude").parent.exists())
        self.assertEqual(self.registry("codex").parent.read_text(), "user file")

    def test_missing_evals_fails_without_registering(self):
        shutil.rmtree(self.root / "Evals")
        result = self.cli("install", "--target", "both", ok=False)
        self.assertIn("beside the sandbox Evals/", result.stderr)
        for agent in ("claude", "codex"):
            self.assertFalse(self.registry(agent).parent.exists())


if __name__ == "__main__":
    unittest.main()
