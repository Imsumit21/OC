import unittest

from generators.core import sqlvalue
from generators.core.values import SpecError
from generators.services import gmail, linear, registry, slack


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
            registry.emitter("gcal", "gcal/1.0")

    def test_slack_thread_parent_convention_recorded(self):
        entry = self.conv["slack.thread_parent_id"]
        self.assertEqual(entry["status"], "platform-verified")
        self.assertEqual(entry["value"], "row id")

    def test_slack_constants_equal_documented_values(self):
        c = self.conv
        self.assertEqual(c["slack.message.ts"]["value"], slack.TS_LAST_DIGIT)
        self.assertEqual(c["slack.message.shape"]["value"], slack.MESSAGE_TYPE)
        self.assertEqual(c["slack.membership.event"]["value"], slack.JOIN_TEXT)
        self.assertEqual(c["slack.thread.counters"]["value"], ", ".join(slack.PARENT_UPDATE_COLUMNS))
        self.assertIn(str(slack.ID_LENGTH), c["slack.message.id"]["value"])
        self.assertEqual(c["slack.membership.first_join"]["status"], "unverified")
        for cid in slack.CONVENTIONS:
            self.assertIn(c[cid]["service"], ("slack", "*"), cid)

    def test_slack_first_join_needs_override(self):
        with self.assertRaisesRegex(SpecError, "unverified convention"):
            registry.conventions_used({"slack.channel_first_join"}, self.conv, {})
        used = registry.conventions_used({"slack.message", "slack.channel_join"}, self.conv, {})
        self.assertNotIn("slack.membership.first_join", [u["id"] for u in used])
        self.assertIn("slack.membership.event", [u["id"] for u in used])

    def test_gmail_constants_equal_documented_values(self):
        c = self.conv
        self.assertEqual(c["gmail.snippet"]["value"], str(gmail.SNIPPET_CHARS))
        self.assertEqual(c["gmail.headers"]["value"], ", ".join(gmail.HEADER_ORDER))
        self.assertEqual(c["gmail.date"]["value"], gmail.DEFAULT_OFFSET)
        self.assertEqual(c["gmail.message.shape"]["value"], f"{len(gmail.MESSAGE_COLUMNS)} columns")
        self.assertEqual(c["gmail.body.crlf"]["value"], "\r\n")
        self.assertEqual(c["gmail.labels"]["value"],
                         " | ".join(", ".join(gmail.DEFAULT_LABELS[r]) for r in ("sender", "recipient", "self")))
        for cid in gmail.CONVENTIONS:
            self.assertIn(c[cid]["service"], ("gmail", "*"), cid)
            self.assertNotEqual(c[cid]["status"], "unverified", cid)       # a Gmail render needs no override

    def test_haystack_kinds(self):
        self.assertEqual(registry.haystack_kinds()["slack.haystack"], slack)
        self.assertEqual(registry.haystack_kinds()["gmail.haystack"], gmail)
        plain = {"key": "A", "kind": "linear.comment", "fields": {}}
        self.assertEqual(registry.expand_record("records[0]", plain), [plain])
        self.assertEqual(registry.expand_record("records[0]", "not an object"), ["not an object"])


if __name__ == "__main__":
    unittest.main()
