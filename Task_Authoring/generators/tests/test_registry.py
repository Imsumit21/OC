import unittest

from generators.core import sqlvalue
from generators.core.values import SpecError
from generators.services import linear, registry


class ConventionsTest(unittest.TestCase):
    def setUp(self):
        self.conv, self.sha = registry.load_conventions()

    def test_every_used_convention_is_documented(self):
        for mod in registry.EMITTERS.values():
            for cid, kinds in mod.CONVENTIONS.items():
                self.assertIn(cid, self.conv, cid)
                for k in kinds:
                    self.assertIn(k, mod.KINDS, (cid, k))

    def test_code_constants_equal_documented_values(self):
        c = self.conv
        self.assertEqual(c["linear.project.color_default"]["value"], linear.PROJECT_DEFAULT_COLOR)
        self.assertEqual(c["linear.issue.state_history_empty"]["value"], linear.NEW_ISSUE_DEFAULTS["state_history_json"])
        self.assertEqual(c["linear.issue.links_empty"]["value"], linear.NEW_ISSUE_DEFAULTS["links_json"])
        self.assertEqual(c["linear.text_dates"]["value"], linear.TS_FORMAT)
        self.assertEqual(sqlvalue.json_text(["a", {"b": 1}]), '["a", {"b": 1}]')

    def test_verified_conventions_carry_evidence(self):
        for cid, entry in self.conv.items():
            self.assertIn(entry["status"], registry.STATUSES, cid)
            if entry["status"] != "unverified":
                self.assertTrue(entry["evidence"], cid)

    def test_unverified_needs_override(self):
        kinds = {"linear.team_update"}
        with self.assertRaisesRegex(SpecError, "unverified convention"):
            registry.conventions_used(kinds, self.conv, {})
        used = registry.conventions_used(kinds, self.conv, {"linear.team.issue_counter": {
            "reason": "r", "platform_follow_up": "p"}})
        self.assertIn("override", next(u for u in used if u["id"] == "linear.team.issue_counter"))

    def test_override_for_unused_convention_refused(self):
        with self.assertRaisesRegex(SpecError, "match no unverified convention"):
            registry.conventions_used({"linear.comment"}, self.conv, {"linear.team.issue_counter": {
                "reason": "r", "platform_follow_up": "p"}})

    def test_emitter_version_pin(self):
        self.assertIs(registry.emitter("linear", linear.VERSION), linear)
        with self.assertRaisesRegex(SpecError, "installed emitter"):
            registry.emitter("linear", "linear/0.9")
        with self.assertRaisesRegex(SpecError, "no emitter"):
            registry.emitter("gmail", "gmail/1.0")

    def test_slack_thread_parent_convention_recorded(self):
        entry = self.conv["slack.thread_parent_id"]
        self.assertEqual(entry["status"], "platform-verified")
        self.assertEqual(entry["value"], "row id")


if __name__ == "__main__":
    unittest.main()
