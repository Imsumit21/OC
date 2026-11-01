import json
import shutil
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path

from generators.core.values import SpecError
from generators.spec.load import load_spec

SCRATCH = Path(__file__).resolve().parents[2] / "support" / "scratch"
SHA = "a" * 64


def minimal(**over):
    doc = {
        "spec_version": "hg-gen/1",
        "task": {"slug": "s", "revision": "rev1", "universe": "synthcut", "freeze_utc": "2025-10-01T00:00:00Z",
                 "clock_utc": "2025-10-01T07:00:00Z", "context_hash": "h"},
        "library": {"emitters": {"linear": "linear/1.0"}},
        "snapshot": {"linear": {"file": "data.json", "sha256": SHA}},
        "records": [{"key": "T1", "kind": "linear.team_update", "fields": {
            "team": {"origin": "base", "construction": "reference",
                     "base": {"service": "linear", "collection": "teams", "record": "team_ENG", "field": "/id"}},
            "issue_counter": {"origin": "authored", "construction": "transform", "fn": "linear.next_issue_number/1"}}}],
    }
    doc.update(over)
    return doc


class SpecLoadTest(unittest.TestCase):
    def setUp(self):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        self.dir = Path(tempfile.mkdtemp(prefix="gen_spec_", dir=SCRATCH))

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def write(self, doc=None, raw=None):
        (self.dir / "spec.json").write_bytes(raw if raw is not None else json.dumps(doc).encode())
        return load_spec(self.dir)

    def fails(self, pattern, doc=None, raw=None):
        with self.assertRaisesRegex(SpecError, pattern):
            self.write(doc, raw)

    def test_minimal_loads(self):
        spec = self.write(minimal())
        self.assertEqual(spec.services(), ["linear"])
        self.assertEqual(len(spec.sha256), 64)

    def test_unknown_top_key(self):
        self.fails("unknown keys", minimal(extra=1))

    def test_version(self):
        self.fails("is not 'hg-gen/1'", minimal(spec_version="hg-gen/2"))

    def test_duplicate_json_key(self):
        raw = json.dumps(minimal()).replace('"spec_version": "hg-gen/1"',
                                            '"spec_version": "hg-gen/1", "spec_version": "hg-gen/1"')
        self.fails("duplicate JSON key", raw=raw.encode())

    def test_not_utf8(self):
        self.fails("not strict UTF-8", raw=b'{"a": "\xff"}')

    def test_duplicate_record_key(self):
        doc = minimal()
        doc["records"].append(dict(doc["records"][0]))
        self.fails("duplicate record key", doc)

    def test_unknown_kind_and_field(self):
        doc = minimal()
        doc["records"][0]["kind"] = "linear.cycle"
        self.fails("unknown record kind", doc)
        doc = minimal()
        doc["records"][0]["fields"]["color"] = {"origin": "authored", "construction": "literal", "value": "x"}
        self.fails("unknown fields", doc)

    def test_missing_required_field(self):
        doc = minimal()
        del doc["records"][0]["fields"]["team"]
        self.fails("required fields missing", doc)

    def test_bare_value_refused(self):
        doc = minimal()
        doc["records"][0]["fields"]["team"] = "team_ENG"
        self.fails("bare literals are refused", doc)

    def test_base_literal_refused(self):
        doc = minimal()
        doc["records"][0]["fields"]["team"] = {"origin": "base", "construction": "literal", "value": "team_ENG"}
        self.fails("a literal is always authored", doc)

    def test_text_path_confined(self):
        doc = minimal()
        doc["records"][0]["fields"]["team"] = {"origin": "authored", "construction": "literal",
                                               "text": "texts/../x.txt", "sha256": SHA}
        self.fails("texts/<name>.txt", doc)

    def test_emitter_pin_and_unused_pin(self):
        self.fails("installed emitter", minimal(library={"emitters": {"linear": "linear/0.1"}}))

    def test_snapshot_pin_shape(self):
        self.fails("64 lower-case hex", minimal(snapshot={"linear": {"file": "data.json", "sha256": "ABC"}}))
        self.fails("relative path", minimal(snapshot={"linear": {"file": "../x.json", "sha256": SHA}}))

    def test_census_shape(self):
        self.fails("census/<name>.json", minimal(census={"c": {"file": "x.json", "sha256": SHA}}))

    def test_decimal_numbers(self):
        doc = minimal()
        doc["records"].append({"key": "U1", "kind": "linear.issue_update", "fields": {
            "issue": {"origin": "base", "construction": "reference",
                      "base": {"service": "linear", "collection": "issues", "record": "ENG-1", "field": "/id"}},
            "priority": {"origin": "authored", "construction": "literal", "value": 1.50}}})
        spec = self.write(doc)
        self.assertEqual(spec.records[1]["fields"]["priority"].value, Decimal("1.5"))


if __name__ == "__main__":
    unittest.main()
