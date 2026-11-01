"""End-to-end: a scratch V3 task with a small Linear spec, rendered, re-rendered, checked and broken on purpose."""
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

from generators.core import pipeline
from generators.core.values import SpecError
from generators.tests.fixtures.task_fixture import LINEAR_DIR, Fixture, base, lit, ref

RENDER = Path(__file__).resolve().parents[1] / "render.py"


@unittest.skipUnless((LINEAR_DIR / "data.json").is_file(), "synth-cut Linear export not installed")
class RenderTest(unittest.TestCase):
    def setUp(self):
        self.fx = Fixture()

    def tearDown(self):
        self.fx.cleanup()

    def mtimes(self, task):
        build = task / "Working_Files" / "build"
        return {p.relative_to(build).as_posix(): p.stat().st_mtime_ns for p in build.rglob("*") if p.is_file()
                and p.name != ".lock"}

    # ---- the happy path
    def test_render_is_idempotent_and_check_passes(self):
        task = self.fx.write()
        rep = pipeline.render(task)
        self.assertEqual(rep["verdict"], "PASS", rep["validation"])
        self.assertEqual({c["status"] for c in rep["changes"]}, {"new"})
        before = self.mtimes(task)
        rep2 = pipeline.render(task)
        self.assertEqual({c["status"] for c in rep2["changes"]}, {"unchanged"})
        self.assertEqual(before, self.mtimes(task))
        self.assertEqual(pipeline.check(task)["verdict"], "PASS")
        self.assertFalse((task / "Working_Files" / "build" / "staging").exists()
                         and any((task / "Working_Files" / "build" / "staging").iterdir()))

    def test_derived_values(self):
        res = pipeline.build(self.fx.write())
        ops = {(op.table, op.op, op.col("id") or dict(op.where).get("id")): op for op in res.ops}
        upd = ops[("linear.linear_issues", "update", "ENG-2366")]
        self.assertEqual(dict(upd.cols), {"updated_at": "2025-09-30T11:00:00Z"})
        self.assertEqual(dict(ops[("linear.linear_teams", "update", "team_ENG")].cols), {"issue_counter": 2369})
        i1 = ops[("linear.linear_issues", "insert", "ENG-2367")]
        self.assertEqual(i1.col("updated_at"), "2025-09-30T10:00:00Z")
        self.assertEqual(i1.col("priority"), 2)                          # base ENG-2366 priority
        self.assertEqual(i1.col("project_id"), self.fx.record("PRJ")["fields"]["id"]["value"])
        i2 = ops[("linear.linear_issues", "insert", "ENG-2368")]
        self.assertEqual(i2.col("updated_at"), "2025-09-30T09:00:00Z")   # started_at, newer than created_at
        seq = [(op.col("issue_id"), op.col("sequence")) for op in res.ops if op.table == "linear.linear_comments"]
        self.assertEqual(seq, [("ENG-2366", 1), ("ENG-2367", 1), ("ENG-2367", 2)])
        self.assertEqual([op.table for op in res.ops][:3],
                         ["linear.linear_projects", "linear.linear_issues", "linear.linear_issues"])

    def test_published_part_parses_back(self):
        task = self.fx.write()
        pipeline.render(task)
        text = (task / "Working_Files" / "build" / "parts" / "linear.sql").read_text()
        res = pipeline.build(task)
        val = pipeline.validate(res, pipeline.emitter.render_full([], [text]))
        self.assertEqual(val["verdict"], "PASS", val)
        tampered = text.replace("'Final bill'", "'Final  bill'")
        val = pipeline.validate(res, pipeline.emitter.render_full([], [tampered]))
        self.assertEqual(val["verdict"], "FAIL")
        self.assertTrue(any("Final  bill" in m for m in val["compare"]))

    def test_agreement_lists_e_string_values(self):
        res = pipeline.build(self.fx.write())
        val = pipeline.validate(res)
        self.assertEqual(val["verdict"], "PASS")
        self.assertEqual(val["agreement"]["count"], 1, val["agreement"])
        self.assertIn("linear.linear_projects", val["agreement"]["first"][0])
        self.assertIn("description", val["agreement"]["first"][0])

    def test_check_reports_stale_after_spec_change(self):
        task = self.fx.write()
        pipeline.render(task)
        self.fx.record("C1")["fields"]["body"] = self.fx.text("C1.txt", "Listed the done items.")
        self.fx.write()
        rep = pipeline.check(task)
        self.assertEqual(rep["verdict"], "FAIL")
        self.assertEqual({s["path"].rsplit("/", 1)[-1] for s in rep["stale"]},
                         {"linear.sql", "provenance.json", "build_record.json"})
        rep = pipeline.render(task)
        self.assertEqual({c["status"] for c in rep["changes"]}, {"changed"})

    def test_drift_refused_then_accepted(self):
        task = self.fx.write()
        pipeline.render(task)
        rec_path = task / "Working_Files" / "build" / "build_record.json"
        rec = json.loads(rec_path.read_text())
        rec["dependencies"]["conventions"] = "0" * 64
        rec_path.write_text(json.dumps(rec))
        rep = pipeline.render(task)
        self.assertEqual(rep["verdict"], "REFUSED")
        self.assertIn("conventions", rep["drift"])
        self.assertEqual(pipeline.check(task)["verdict"], "FAIL")
        rep = pipeline.render(task, accept_upgrade=True)
        self.assertEqual(rep["verdict"], "PASS")
        log = (task / "Working_Files" / "build" / "upgrades.jsonl").read_text().splitlines()
        self.assertEqual(len(log), 1)
        self.assertIn("conventions", json.loads(log[0])["upgrades"])
        self.assertEqual(pipeline.check(task)["verdict"], "PASS")

    def test_validation_failure_publishes_nothing(self):
        self.fx.record("C3")["fields"]["created_at"] = lit("2025-07-26T22:14:57Z")
        task = self.fx.write()
        rep = pipeline.render(task)
        self.assertEqual(rep["verdict"], "FAIL")
        self.assertIn("L5", rep["validation"]["invariants"]["FAIL"])
        self.assertFalse((task / "Working_Files" / "build" / "parts").exists())

    # ---- expected failures, each with its named error
    def fails(self, pattern, exc=SpecError):
        task = self.fx.write()
        with self.assertRaisesRegex(exc, pattern):
            pipeline.build(task)

    def test_unknown_field(self):
        self.fx.record("C1")["fields"]["color"] = lit("x")
        self.fails("unknown fields")

    def test_text_sha_mismatch(self):
        self.fx.record("C1")["fields"]["body"]["sha256"] = "0" * 64
        self.fails("sha256 is")

    def test_seed_before_its_after_event(self):
        self.fx.record("C1")["fields"]["created_at"] = lit("2025-09-29T17:00:00Z", after=["spec:I1/created_at"])
        self.fails("is not after")

    def test_post_freeze_event(self):
        self.fx.record("C2")["fields"]["created_at"] = lit("2025-10-01T08:00:00Z")
        self.fails("seed bound", pipeline.BuildError)

    def test_unverified_convention_without_override(self):
        del self.fx.doc["overrides"]
        self.fails("unverified convention")

    def test_context_mismatch(self):
        self.fx.doc["task"]["universe"] = "normal"
        self.fails("task.universe")
        self.fx.doc["task"]["universe"] = self.fx.ctx["universe"]["key"]
        self.fx.doc["task"]["context_hash"] = "0" * 64
        self.fails("task.context_hash")

    def test_snapshot_mismatch(self):
        self.fx.doc["snapshot"]["linear"]["sha256"] = "0" * 64
        self.fails("the spec pins")

    def test_dangling_base_citation(self):
        self.fx.record("C3")["fields"]["issue"] = base("issues", "ENG-99999", "id")
        self.fails("not found in the pinned export")

    def test_base_value_drift_is_a_missing_field(self):
        self.fx.record("I1")["fields"]["priority"] = base("issues", "ENG-2366", "no_such_field")
        self.fails("has no field")

    def test_cite_not_verbatim(self):
        self.fx.record("C3")["fields"]["body"] = self.fx.text("C3.txt", "Moved.", cites=["spec:I1/id"])
        self.fails("does not occur verbatim")

    def test_claim_without_census(self):
        self.fx.record("C3")["fields"]["body"] = self.fx.text("C3.txt", "Moved to ENG-2367.", claims=["ENG-2366 open"])
        self.fails("claims without census evidence")

    def test_ref_to_base_value(self):
        self.fx.record("I2")["fields"]["team"] = ref("I1/team")
        self.fails("points at a base value")

    def test_parent_after_child(self):
        self.fx.record("I1")["fields"]["parent"] = ref("I2")
        self.fx.record("I2")["fields"]["parent"] = lit(None)
        self.fails("sorts after its child")

    def test_null_in_not_null(self):
        self.fx.record("C2")["fields"]["body"] = lit(None)
        self.fails("NULL in NOT NULL", pipeline.BuildError)

    def test_existing_issue_id(self):
        self.fx.record("I2")["fields"]["id"] = lit("ENG-2366")
        self.fails("already exists in the base export")

    def test_unknown_user(self):
        self.fx.record("C2")["fields"]["author"] = lit("usr_nobody")
        self.fails("is not in the pinned base")

    def test_duplicate_spec_issue_id(self):
        self.fx.record("I2")["fields"]["id"] = lit("ENG-2367")
        self.fx.record("I2")["fields"]["parent"] = lit(None)
        self.fails("declared twice")

    def test_uncited_fact_tokens_are_flagged(self):
        rep = pipeline.provenance_report(pipeline.build(self.fx.write()))
        self.assertEqual(rep["verdict"], "PASS")
        self.assertEqual(rep["columns_without_provenance"], [])
        self.assertIn("C2.body: un-cited amount $1,250.00", rep["uncited_fact_tokens"]["first"])
        self.assertFalse(any(f.startswith("C3.body") for f in rep["uncited_fact_tokens"]["first"]))  # cited ENG-2367

    def test_wrong_value_type(self):
        self.fx.record("I2")["fields"]["title"] = lit({"a": 1})
        self.fails("unsupported value type", pipeline.BuildError)

    def test_reference_cycle(self):
        self.fx.record("I1")["fields"]["created_at"] = ref("I2/created_at")
        self.fx.record("I2")["fields"]["created_at"] = ref("I1/created_at")
        self.fails("reference cycle")

    # ---- determinism and the CLI
    def test_byte_identical_across_hash_seeds(self):
        task = self.fx.write()
        code = ("import sys, hashlib; sys.path.insert(0, %r); sys.dont_write_bytecode = True\n"
                "from generators.core import pipeline\n"
                "res = pipeline.build(%r); pipeline.validate(res)\n"
                "files = dict(res.files); files['rec'] = pipeline._json_bytes(pipeline.record(res, {}))\n"
                "print(sorted((k, hashlib.sha256(v).hexdigest()) for k, v in files.items()))\n"
                % (str(RENDER.parents[1]), str(task)))
        outs = set()
        for seed in ("1", "2"):
            env = dict(os.environ, PYTHONHASHSEED=seed)
            proc = subprocess.run([sys.executable, "-B", "-c", code], capture_output=True, text=True, env=env,
                                  timeout=300)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            outs.add(proc.stdout)
        self.assertEqual(len(outs), 1)

    def test_cli(self):
        task = self.fx.write()

        def run(*args):
            return subprocess.run([sys.executable, "-B", str(RENDER), *args], capture_output=True, text=True,
                                  timeout=300)

        p = run("validate", "--task-dir", str(task), "--json")
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(json.loads(p.stdout)["validation"]["verdict"], "PASS")
        self.assertEqual(run("render", "--task-dir", str(task)).returncode, 0)
        self.assertEqual(run("check", "--task-dir", str(task)).returncode, 0)
        self.assertEqual(run("parse-back", "--task-dir", str(task)).returncode, 0)
        p = run("explain", "--task-dir", str(task), "--row", "linear.linear_issues:ENG-2366", "--json")
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(json.loads(p.stdout)[0]["columns"][0]["provenance"]["convention"],
                         "linear.issue.updated_at_follows_comments")
        self.assertEqual(run("provenance", "--task-dir", str(task)).returncode, 0)
        (task / "01_Universe_Inject.sql").write_text("-- Are you planning to inject? Yes\n")
        self.assertEqual(run("store-revision", "--task-dir", str(task), "--rev", "rev1").returncode, 0)
        (task / "01_Universe_Inject.sql").write_text("-- Are you planning to inject? Yes\nBEGIN;\n")
        p = run("store-revision", "--task-dir", str(task), "--rev", "rev1")
        self.assertEqual(p.returncode, 1)
        self.assertIn("immutable", p.stderr)
        self.fx.record("C1")["fields"]["color"] = lit("x")
        self.fx.write()
        p = run("validate", "--task-dir", str(task))
        self.assertEqual(p.returncode, 1)
        self.assertIn("SPEC FAIL", p.stderr)


if __name__ == "__main__":
    unittest.main()
