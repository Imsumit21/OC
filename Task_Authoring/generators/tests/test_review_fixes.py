"""Regressions for the Phase 1 independent review (reviewer + red team, 2026-11-01): each failed before its fix."""
import hashlib
import importlib
import io
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

import generators
from generators.core import context, output, pipeline
from generators.core.ops import Op
from generators.core.values import SpecError, parse_value
from generators.validate import coltypes, parse_back
from generators.tests.fixtures.task_fixture import LINEAR_DIR, Fixture, base, lit, ref

CENSUS_OK = {
    "format": "hg-gen-census/1", "claim": "ENG-2366 open",
    "scope": {"entity": "ENG-2366", "aliases": ["store sunset ticket"]},
    "services": [{"service": "linear", "query": "ENG-2366", "query_sha256": "1" * 64, "pages": 1, "complete": True,
                  "result_sha256": "2" * 64}],
    "hits": [{"locator": "base:linear:issues/ENG-2366/state_id", "classification": "supports"}],
    "disposition": {"by": "reviewer", "verdict": "holds", "note": "Todo at the cut"},
}


@unittest.skipUnless((LINEAR_DIR / "data.json").is_file(), "synth-cut Linear export not installed")
class ReviewFixesTest(unittest.TestCase):
    def setUp(self):
        self.fx = Fixture()

    def tearDown(self):
        self.fx.cleanup()

    def validation(self):
        res = pipeline.build(self.fx.write())
        return pipeline.validate(res)

    # -- column types, ranges and lengths (validate/coltypes.py)
    def test_int4_overflow_fails_validation(self):
        self.fx.record("I2")["fields"]["estimate"] = lit(2147483648)
        val = self.validation()
        self.assertEqual(val["verdict"], "FAIL")
        self.assertTrue(any("estimate" in m and "int4 range" in m for m in val["types"]), val["types"])

    def test_text_in_integer_column_fails(self):
        self.fx.record("I1")["fields"]["priority"] = lit("not-an-int")
        task = self.fx.write()
        try:
            val = pipeline.validate(pipeline.build(task))
        except pipeline.BuildError as exc:                 # the early row rules may already refuse it
            self.assertIn("priority", " ".join(exc.problems))
            return
        self.assertEqual(val["verdict"], "FAIL")
        self.assertTrue(any("priority" in m for m in val["types"]), val["types"])

    def test_varchar_length_fails(self):
        self.fx.record("I2")["fields"]["title"] = lit("x" * 501)
        val = self.validation()
        self.assertEqual(val["verdict"], "FAIL")
        self.assertTrue(any("varchar(500)" in m for m in val["types"]), val["types"])

    def test_render_publishes_nothing_on_type_failure(self):
        self.fx.record("I2")["fields"]["estimate"] = lit(2147483648)
        task = self.fx.write()
        self.assertEqual(pipeline.render(task)["verdict"], "FAIL")
        self.assertFalse((task / "Working_Files" / "build" / "parts").exists())

    # -- identifiers are matched as PostgreSQL resolves them
    def test_quoted_identifier_case_is_not_normalised(self):
        res = pipeline.build(self.fx.write())
        text = res.full_sql()
        for bad in (text.replace("INSERT INTO linear.linear_issues ", 'INSERT INTO "LINEAR"."LINEAR_ISSUES" '),
                    text.replace("INSERT INTO linear.linear_issues ", 'INSERT INTO linear."Linear_Issues" '),
                    text.replace("(id, uuid, project_id,", '("ID", uuid, project_id,', 1)):
            val = pipeline.validate(res, bad)
            self.assertEqual(val["verdict"], "FAIL")
            self.assertIn("not in the universe schema", val["parse_back"])
        ok = text.replace("INSERT INTO linear.linear_issues ", "INSERT INTO LINEAR.LINEAR_ISSUES ")
        val = pipeline.validate(res, ok)                       # unquoted names fold to lower case: valid SQL
        self.assertNotIn("FAIL", val["parse_back"])
        self.assertTrue(val["grammar"])                       # but not the library's own spelling

    # -- stored revisions are never overwritten, even by a concurrent writer
    def test_store_revision_no_clobber_race(self):
        task = self.fx.write()
        (task / "01_Universe_Inject.sql").write_text("-- B\n")
        dest = task / "Working_Files" / "run_forensics" / "rev1" / "01_Universe_Inject.sql"
        dest.parent.mkdir(parents=True)
        dest.write_text("-- A\n")                              # the other writer got there first
        real = output._read_at
        calls = []

        def stale_first(dfd, name, rel):
            if rel.startswith(output.PROTECTED + "/") and not calls:
                calls.append(rel)
                return None                                    # this writer's first look saw no stored file
            return real(dfd, name, rel)
        with mock.patch.object(output, "_read_at", stale_first):
            with self.assertRaisesRegex(output.PublishError, "immutable"):
                output.store_revision(task, "rev1")
        self.assertEqual(dest.read_text(), "-- A\n")
        self.assertEqual([p.name for p in dest.parent.iterdir()], ["01_Universe_Inject.sql"])

    def test_store_revision_refuses_a_folder_swapped_for_a_symlink(self):
        task = self.fx.write()
        (task / "01_Universe_Inject.sql").write_text("-- A\n")
        elsewhere = self.fx.root / "elsewhere"
        elsewhere.mkdir()
        forensics = task / "Working_Files" / "run_forensics"
        forensics.mkdir(parents=True)
        os.symlink(elsewhere, forensics / "rev1")              # as if swapped in after the path check
        with mock.patch.object(output, "confine", lambda root, rel: Path(root) / rel):
            with self.assertRaisesRegex(output.PublishError, "without following a symlink"):
                output.store_revision(task, "rev1")
        self.assertEqual(list(elsewhere.iterdir()), [])

    def test_store_revision_refuses_a_task_folder_swapped_for_a_symlink(self):
        alt = self.fx.root / "alt_task"
        alt.mkdir()
        (alt / "01_Universe_Inject.sql").write_text("-- A\n")
        link = self.fx.root / "link_task"
        os.symlink(alt, link)                                  # as if the task folder were swapped after the check
        with mock.patch.object(output, "_root", lambda task_dir: Path(task_dir)), \
                mock.patch.object(output, "confine", lambda root, rel: Path(root) / rel):
            with self.assertRaisesRegex(output.PublishError, "without following a symlink"):
                output.store_revision(link, "rev1")
        self.assertEqual(sorted(p.name for p in alt.iterdir()), ["01_Universe_Inject.sql"])

    def test_store_revision_refuses_a_fifo_without_blocking(self):
        import threading
        task = self.fx.write()
        (task / "01_Universe_Inject.sql").write_text("-- A\n")
        dest = task / "Working_Files" / "run_forensics" / "rev1" / "01_Universe_Inject.sql"
        dest.parent.mkdir(parents=True)
        os.mkfifo(dest)
        outcome = []

        def store():
            try:
                output.store_revision(task, "rev1")
                outcome.append("stored")
            except output.PublishError as exc:
                outcome.append(str(exc))
        worker = threading.Thread(target=store, daemon=True)
        worker.start()
        worker.join(timeout=20)
        self.assertFalse(worker.is_alive(), "store_revision blocked on a FIFO")
        self.assertIn("not a regular file", outcome[0])

    def test_non_ascii_digits_in_a_timestamp_fail(self):
        self.fx.doc["records"].append({"key": "U1", "kind": "linear.issue_update", "fields": {
            "issue": base("issues", "ENG-2366", "id"), "state": lit("Done"),
            "started_at": lit("2025-\uff10\uff19-30T12:00:00Z"), "completed_at": lit("2025-09-29T20:00:00Z"),
            "updated_at": lit("2025-09-30T13:00:00Z")}})
        val = self.validation()
        self.assertEqual(val["verdict"], "FAIL")
        self.assertIn("L1", val["invariants"]["FAIL"])
        self.assertTrue(any("started_at" in m for m in val["invariants"]["FAIL"]["L4"]["first"]))

    def test_lone_surrogate_in_a_spec_value_refused(self):
        self.fx.record("I2")["fields"]["title"] = lit("bill \ud800")
        with self.assertRaisesRegex(SpecError, "lone surrogate"):
            pipeline.build(self.fx.write(raw=json.dumps(self.fx.doc).encode()))

    def test_unreferenced_text_file_refused(self):
        task = self.fx.write()
        (self.fx.spec_dir / "texts" / "orphan.txt").write_text("A")
        with self.assertRaisesRegex(SpecError, "files no field pins"):
            pipeline.build(task)

    def test_unknown_state_with_terminal_stamps_fails(self):
        self.fx.doc["records"].append({"key": "U1", "kind": "linear.issue_update", "fields": {
            "issue": base("issues", "ENG-2366", "id"), "state": lit("QA-unknown"),
            "completed_at": lit("2025-09-29T20:00:00Z")}})
        val = self.validation()
        self.assertEqual(val["verdict"], "FAIL")
        self.assertTrue(any("not a base state" in m for m in val["invariants"]["FAIL"]["L4"]["first"]))

    # -- inputs edited during a render are not published from stale bytes
    def test_input_edited_during_render_publishes_nothing(self):
        task = self.fx.write()
        real_add = output.Build.add
        text = self.fx.spec_dir / "texts" / "C1.txt"

        def add_and_edit(b, rel, data):
            if not text.read_bytes().startswith(b"edited"):
                text.write_bytes(b"edited meanwhile")
            return real_add(b, rel, data)
        with mock.patch.object(output.Build, "add", add_and_edit):
            with self.assertRaisesRegex(pipeline.BuildError, "inputs or dependencies changed"):
                pipeline.render(task)
        self.assertFalse((task / "Working_Files" / "build" / "parts").exists())

    # -- every spec input stays inside the task folder, no symlinked directory on the way
    def test_symlinked_texts_directory_refused(self):
        task = self.fx.write()
        outside = self.fx.root / "outside_texts"
        (self.fx.spec_dir / "texts").rename(outside)
        os.symlink(outside, self.fx.spec_dir / "texts")
        with self.assertRaisesRegex(SpecError, "symlink"):
            pipeline.build(task)

    def test_symlinked_spec_directory_refused(self):
        task = self.fx.write()
        outside = self.fx.root / "outside_spec"
        self.fx.spec_dir.rename(outside)
        os.symlink(outside, self.fx.spec_dir)
        with self.assertRaisesRegex(SpecError, "symlink"):
            pipeline.build(task)

    # -- emitter-computed values accept no provenance they would ignore
    def test_computed_counter_metadata_refused(self):
        t1 = self.fx.record("T1")["fields"]
        t1["issue_counter"] = {"origin": "base", "construction": "transform", "fn": "linear.next_issue_number/1"}
        with self.assertRaisesRegex(SpecError, "authored transform"):
            pipeline.build(self.fx.write())
        t1["issue_counter"] = {"origin": "authored", "construction": "transform", "fn": "linear.next_issue_number/1",
                               "after": ["spec:missing/created_at"]}
        with self.assertRaisesRegex(SpecError, "do not apply"):
            pipeline.build(self.fx.write())

    def test_ref_to_computed_value_refused(self):
        self.fx.record("I2")["fields"]["estimate"] = ref("T1/issue_counter")
        with self.assertRaisesRegex(SpecError, "emitter computes"):
            pipeline.build(self.fx.write())

    # -- census evidence has to be complete, not just hashed
    def census(self, doc):
        data = (json.dumps(doc) if not isinstance(doc, bytes) else doc)
        data = data.encode() if isinstance(data, str) else data
        (self.fx.spec_dir / "census").mkdir(exist_ok=True)
        (self.fx.spec_dir / "census" / "eng2366.json").write_bytes(data)
        self.fx.record("C3")["fields"]["body"] = self.fx.text("C3.txt", "Moved to ENG-2367.", cites=["spec:I1/id"],
                                                              claims=["ENG-2366 open"])
        self.fx.doc["census"] = {"ENG-2366 open": {"file": "census/eng2366.json",
                                                   "sha256": hashlib.sha256(data).hexdigest()}}
        return self.fx.write()

    def test_census_complete_passes(self):
        res = pipeline.build(self.census(CENSUS_OK))
        self.assertIn("Working_Files/spec/census/eng2366.json", res.inputs)

    def test_census_contents_checked(self):
        bad = [({}, "exactly the keys"), (b"not json", "not UTF-8 JSON"),
               (dict(CENSUS_OK, services=[dict(CENSUS_OK["services"][0], complete=False)]), "pagination"),
               (dict(CENSUS_OK, disposition={"by": "r", "verdict": "fails", "note": ""}), "needs 'holds'"),
               (dict(CENSUS_OK, claim="other"), "for claim")]
        for doc, pattern in bad:
            with self.subTest(pattern=pattern):
                task = self.census(doc)
                (self.fx.spec_dir / "census" / "eng2366.json").write_bytes(
                    json.dumps(doc).encode() if not isinstance(doc, bytes) else doc)
                with self.assertRaisesRegex(SpecError, pattern):
                    pipeline.build(task)

    # -- derivations the review found incomplete
    def test_project_updated_at_follows_base_issue_moved_in(self):
        self.fx.doc["records"].append({"key": "U1", "kind": "linear.issue_update", "fields": {
            "issue": base("issues", "ENG-2366", "id"), "project": ref("PRJ"),
            "updated_at": lit("2025-09-30T12:00:00Z")}})
        res = pipeline.build(self.fx.write())
        prj = next(op for op in res.ops if op.table == "linear.linear_projects")
        self.assertEqual(prj.col("updated_at"), "2025-09-30T12:00:00Z")
        self.assertEqual(pipeline.validate(res)["verdict"], "PASS")

    def test_canceled_before_started_fails(self):
        i2 = self.fx.record("I2")["fields"]
        i2["state"] = lit("Canceled")
        i2["canceled_at"] = lit("2025-09-29T23:00:00Z")
        val = self.validation()
        self.assertEqual(val["verdict"], "FAIL")
        self.assertIn("L4", val["invariants"]["FAIL"])

    # -- a stale output stays owned until it is pruned
    def test_stale_output_stays_owned_until_pruned(self):
        task = self.fx.write()
        pipeline.render(task)
        stale = task / "Working_Files" / "build" / "parts" / "gmail.sql"
        stale.write_text("-- an earlier build's part\n")
        rec_path = task / "Working_Files" / "build" / "build_record.json"
        rec = json.loads(rec_path.read_text())
        rec["outputs"]["Working_Files/build/parts/gmail.sql"] = output.sha256_file(stale)
        rec_path.write_text(json.dumps(rec))
        pipeline.render(task)                                  # without --prune: kept, and still owned
        self.assertTrue(stale.exists())
        self.assertIn("Working_Files/build/parts/gmail.sql", json.loads(rec_path.read_text())["stale_outputs"])
        chk = pipeline.check(task)
        self.assertEqual(chk["verdict"], "FAIL")
        self.assertIn("Working_Files/build/parts/gmail.sql", [s["path"] for s in chk["stale"]])
        pipeline.render(task, prune=True)
        self.assertFalse(stale.exists())
        self.assertEqual(json.loads(rec_path.read_text())["stale_outputs"], {})
        self.assertEqual(pipeline.check(task)["verdict"], "PASS")

    # -- round 2: an interrupted prune keeps ownership (outputs first, the record after)
    def test_interrupted_prune_keeps_ownership(self):
        task = self.fx.write()
        pipeline.render(task)
        stale = task / "Working_Files" / "build" / "parts" / "gmail.sql"
        stale.write_text("-- an earlier build's part\n")
        rec_path = task / "Working_Files" / "build" / "build_record.json"
        rec = json.loads(rec_path.read_text())
        rec["outputs"]["Working_Files/build/parts/gmail.sql"] = output.sha256_file(stale)
        rec_path.write_text(json.dumps(rec))
        real_unlink = os.unlink

        def failing_unlink(path, *a, **k):
            if str(path).endswith("gmail.sql"):
                raise OSError("disk says no")
            return real_unlink(path, *a, **k)
        with mock.patch.object(os, "unlink", failing_unlink):
            with self.assertRaisesRegex(output.PublishError, "prune failed"):
                pipeline.render(task, prune=True)
        self.assertTrue(stale.exists())
        self.assertIn("Working_Files/build/parts/gmail.sql", json.loads(rec_path.read_text())["outputs"])
        chk = pipeline.check(task)
        self.assertEqual(chk["verdict"], "FAIL")
        self.assertIn("Working_Files/build/parts/gmail.sql", [s["path"] for s in chk["stale"]])
        pipeline.render(task, prune=True)
        self.assertFalse(stale.exists())
        self.assertEqual(pipeline.check(task)["verdict"], "PASS")

    def test_stored_revision_symlink_refused(self):
        task = self.fx.write()
        source = task / "01_Universe_Inject.sql"
        source.write_text("-- A\n")
        dest = task / "Working_Files" / "run_forensics" / "rev1" / "01_Universe_Inject.sql"
        dest.parent.mkdir(parents=True)
        os.symlink(source, dest)
        with self.assertRaisesRegex(output.PublishError, "symlink"):
            output.store_revision(task, "rev1")

    def test_one_pin_per_text_file(self):
        self.fx.record("C1")["fields"]["body"] = self.fx.text("shared.txt", "A")
        self.fx.record("C2")["fields"]["body"] = dict(self.fx.text("shared.txt", "A"),
                                                      sha256=hashlib.sha256(b"B").hexdigest())
        with self.assertRaisesRegex(SpecError, "two different sha256"):
            pipeline.build(self.fx.write())

    def test_check_fails_when_an_input_changes_during_it(self):
        task = self.fx.write()
        pipeline.render(task)
        real_validate = pipeline.validate

        def validate_then_edit(res, *a, **k):
            out = real_validate(res, *a, **k)
            (self.fx.spec_dir / "texts" / "C1.txt").write_text("changed meanwhile")
            return out
        with mock.patch.object(pipeline, "validate", validate_then_edit):
            rep = pipeline.check(task)
        self.assertEqual(rep["verdict"], "FAIL")
        self.assertTrue(rep["inputs_changed"])

    def test_canceled_update_keeping_completed_at_fails(self):
        self.fx.doc["records"].append({"key": "U1", "kind": "linear.issue_update", "fields": {
            "issue": base("issues", "ENG-2366", "id"), "state": lit("Canceled"),
            "completed_at": lit("2025-09-29T20:00:00Z"), "canceled_at": lit("2025-09-30T12:00:00Z")}})
        val = self.validation()
        self.assertEqual(val["verdict"], "FAIL")
        self.assertTrue(any("completed_at" in m for m in val["invariants"]["FAIL"]["L4"]["first"]))

    def test_census_primitive_types(self):
        svc = CENSUS_OK["services"][0]
        for doc in (dict(CENSUS_OK, services=[dict(svc, service=True)]),
                    dict(CENSUS_OK, services=[dict(svc, pages=True)]),
                    dict(CENSUS_OK, hits=[{"locator": True, "classification": "supports"}]),
                    dict(CENSUS_OK, disposition={"by": True, "verdict": "holds", "note": ""})):
            with self.subTest(doc=doc):
                with self.assertRaises(SpecError):
                    pipeline.build(self.census(doc))

    # -- round 3: a dependency that changes while a render or check runs refuses it
    def _deps_changing(self):
        """Every dependency fingerprint after the first (the one taken before the build) sees a changed schema."""
        real = pipeline._fingerprint
        calls = []

        def fingerprint(tools):
            out = real(tools)
            calls.append(out)
            if len(calls) > 1:
                out = dict(out, data=dict(out["data"], schema_live="0" * 64))
            return out
        return mock.patch.object(pipeline, "_fingerprint", fingerprint)

    def test_dependency_change_during_render_publishes_nothing(self):
        task = self.fx.write()
        with self._deps_changing():
            with self.assertRaisesRegex(pipeline.BuildError, "dependencies changed"):
                pipeline.render(task)
        self.assertFalse((task / "Working_Files" / "build" / "parts").exists())
        self.assertFalse((task / "Working_Files" / "build" / "build_record.json").exists())

    def test_dependency_change_during_check_fails_it(self):
        task = self.fx.write()
        pipeline.render(task)
        with self._deps_changing():
            rep = pipeline.check(task)
        self.assertEqual(rep["verdict"], "FAIL")
        self.assertIn("data: changed during this run", rep["inputs_changed"])
        self.assertEqual(pipeline.check(task)["verdict"], "PASS")

    # -- formal gate (code + redteam): stored revisions are out of every build's reach
    def test_build_never_writes_a_stored_revision(self):
        task = self.fx.write()
        (task / "01_Universe_Inject.sql").write_text("-- A\n")
        saved = output.store_revision(task, "rev1")
        for rel in (saved.path, saved.path.replace("Working_Files/run_forensics", "working_files/RUN_FORENSICS"),
                    "Working_Files/run_forensics/rev2/new.sql", "./" + saved.path,
                    saved.path.replace("forensics", "foren\u017fics"),            # LATIN SMALL LETTER LONG S
                    saved.path.replace("Working_", "Working_\u200b"),             # ZERO WIDTH SPACE
                    saved.path.replace("Files", "\uff26iles")):                   # FULLWIDTH LATIN CAPITAL F
            b = output.Build(task, "overwrite")
            with self.subTest(rel=rel), self.assertRaisesRegex(output.PublishError, "only by store_revision"):
                b.add(rel, b"-- B\n")
            b.discard()
        self.assertEqual((task / saved.path).read_bytes(), b"-- A\n")

    def test_prune_never_removes_a_stored_revision(self):
        task = self.fx.write()
        source = task / "01_Universe_Inject.sql"
        source.write_text("-- A\n")
        saved = output.store_revision(task, "rev1")
        b = output.Build(task, "prune")
        changes = b.publish(prune=True, previous={saved.path: saved.sha256_new})
        b.discard()
        self.assertEqual([(c.path, c.status) for c in changes], [(saved.path, "stale")])
        self.assertEqual((task / saved.path).read_bytes(), b"-- A\n")
        source.write_text("-- B\n")
        with self.assertRaisesRegex(output.PublishError, "immutable"):
            output.store_revision(task, "rev1")
        self.assertEqual((task / saved.path).read_bytes(), b"-- A\n")

    # -- formal gate: publishing, pruning and staging act by folder descriptor, so a folder swapped for a symlink
    #    after the name check is refused; confine's name check is switched off to stand for that swap
    def _swap_after_check(self):
        return mock.patch.object(output, "confine", lambda root, rel: Path(root) / rel)

    def test_publish_refuses_a_folder_swapped_after_the_check(self):
        task = self.fx.write()
        rel = "Working_Files/build/parts/linear.sql"
        (task / rel).parent.mkdir(parents=True)
        b = output.Build(task, "swap")
        b.add(rel, b"-- B\n")
        b.plan()
        outside = self.fx.root / "outside"
        outside.mkdir()
        parts = task / "Working_Files" / "build" / "parts"
        parts.rename(parts.with_name("parts.old"))
        os.symlink(outside, parts)
        with self._swap_after_check(), self.assertRaisesRegex(output.PublishError, "without following a symlink"):
            b.publish()
        b.discard()
        self.assertEqual(list(outside.iterdir()), [])

    def test_prune_refuses_a_folder_swapped_after_the_check(self):
        task = self.fx.write()
        first = output.Build(task, "one")
        first.add("sub/old.txt", b"OLD")
        owned = {c.path: c.sha256_new for c in first.publish()}
        first.discard()
        outside = self.fx.root / "outside"
        outside.mkdir()
        (outside / "old.txt").write_bytes(b"OLD")            # same bytes, so only the folder walk can protect it
        (task / "sub").rename(task / "sub.old")
        os.symlink(outside, task / "sub")
        second = output.Build(task, "two")
        with self._swap_after_check(), self.assertRaisesRegex(output.PublishError, "without following a symlink"):
            second.publish(prune=True, previous=owned)
        second.discard()
        self.assertEqual((outside / "old.txt").read_bytes(), b"OLD")

    def test_staging_refuses_a_folder_swapped_after_the_check(self):
        task = self.fx.write()
        b = output.Build(task, "stage")
        outside = self.fx.root / "outside"
        outside.mkdir()
        staging = task / "Working_Files" / "build" / "staging"
        staging.mkdir(parents=True, exist_ok=True)
        os.symlink(outside, staging / "stage")
        with self._swap_after_check(), self.assertRaisesRegex(output.PublishError, "without following a symlink"):
            b.add("x.txt", b"X")
        self.assertEqual(list(outside.iterdir()), [])

    # -- formal gate: the base export, its manifest and the task context are re-checked before publishing
    def _external_changed(self, suffix):
        real = pipeline._sha_file
        return mock.patch.object(pipeline, "_sha_file", lambda p: "0" * 64 if str(p).endswith(suffix) else real(p))

    def test_base_export_or_manifest_change_during_render_publishes_nothing(self):
        for suffix in ("linear/data.json", "linear/source_manifest.json"):
            with self.subTest(suffix=suffix):
                task = self.fx.write()
                with self._external_changed(suffix), self.assertRaisesRegex(pipeline.BuildError, "changed during"):
                    pipeline.render(task)
                self.assertFalse((task / "Working_Files" / "build" / "parts").exists())
                self.assertFalse((task / "Working_Files" / "build" / "build_record.json").exists())

    def test_check_fails_when_the_base_export_or_context_changes_during_it(self):
        task = self.fx.write()
        pipeline.render(task)
        with self._external_changed("linear/data.json"):
            rep = pipeline.check(task)
        self.assertEqual(rep["verdict"], "FAIL")
        self.assertTrue(any("linear/data.json" in m for m in rep["inputs_changed"]), rep["inputs_changed"])
        real = pipeline.context.recompute
        calls = []

        def recompute(task_dir):
            calls.append(task_dir)
            ctx = real(task_dir)
            return ctx if len(calls) == 1 else dict(ctx, context_hash="0" * 64)
        with mock.patch.object(pipeline.context, "recompute", recompute):
            rep = pipeline.check(task)
        self.assertEqual(rep["verdict"], "FAIL")
        self.assertTrue(any(m.startswith("task context") for m in rep["inputs_changed"]), rep["inputs_changed"])
        self.assertEqual(pipeline.check(task)["verdict"], "PASS")

    # -- formal gate: L1 wants real calendar values in Linear's text date columns
    def test_impossible_calendar_date_is_refused(self):
        self.fx.record("I2")["fields"]["due_date"] = lit("2025-02-30")
        val = self.validation()
        self.assertEqual(val["verdict"], "FAIL")
        self.assertTrue(any("due_date" in m for m in val["invariants"]["FAIL"]["L1"]["first"]), val["invariants"])

    def test_sql_lint_that_does_not_complete_fails_validation(self):
        res = pipeline.build(self.fx.write())
        crashed = mock.Mock(returncode=1, stdout=b"", stderr=b"Traceback (most recent call last):\nValueError: boom")
        with mock.patch.object(pipeline.subprocess, "run", return_value=crashed):
            val = pipeline.validate(res)
        self.assertEqual(val["verdict"], "FAIL")
        self.assertEqual(val["sql_lint"]["errors"]["first"], ["line 0: tools/sql_lint.py did not complete "
                                                              "(exit 1, no well-formed report: ValueError: boom)"])
        self.assertEqual(val["invariants"]["FAIL"], {})          # the library's own checks still ran and are shown

    def test_sql_lint_that_times_out_or_cannot_start_fails_validation(self):
        res = pipeline.build(self.fx.write())
        for exc, why in ((subprocess.TimeoutExpired(["sql_lint.py"], pipeline.LINT_TIMEOUT), "it was stopped"),
                         (FileNotFoundError(2, "No such file or directory"), "could not be started"),
                         (PermissionError(13, "Permission denied"), "could not be started")):
            with self.subTest(exc=type(exc).__name__), mock.patch.object(pipeline.subprocess, "run", side_effect=exc):
                val = pipeline.validate(res)
                self.assertEqual(val["verdict"], "FAIL")
                self.assertIn(why, val["sql_lint"]["errors"]["first"][0])
                self.assertEqual(val["invariants"]["FAIL"], {})
        garbled = mock.Mock(returncode=0, stdout=b"\xff\xfe not json", stderr=b"")
        with mock.patch.object(pipeline.subprocess, "run", return_value=garbled):
            self.assertEqual(pipeline.validate(res)["verdict"], "FAIL")

    def test_sql_lint_report_of_the_wrong_shape_fails_validation(self):
        res = pipeline.build(self.fx.write())
        for report in ({"errors": []}, {"errors": [], "warnings": None}, {"errors": "none", "warnings": []},
                       {"errors": [], "warnings": [{"line": 3}]},
                       {"errors": [], "warnings": [{"line": "3", "msg": "x"}]},
                       {"errors": [], "warnings": [{"line": True, "msg": "x"}]}, ["errors"]):
            reply = mock.Mock(returncode=0, stdout=json.dumps(report).encode(), stderr=b"")
            with self.subTest(report=report), mock.patch.object(pipeline.subprocess, "run", return_value=reply):
                val = pipeline.validate(res)
                self.assertEqual(val["verdict"], "FAIL")
                self.assertIn("no well-formed report", val["sql_lint"]["errors"]["first"][0])
                self.assertEqual(val["invariants"]["FAIL"], {})

    # -- formal gate, round 2 (code + redteam)
    def test_root_refuses_a_symlink_on_the_way(self):
        task = self.fx.write()
        link = self.fx.root / "link_to_task"
        os.symlink(task, link)
        for call in (lambda: output.read_bytes(link, "00_Assigments.md"), lambda: output.Build(link, "b"),
                     lambda: output.TaskLock(link), lambda: output.store_revision(link, "rev1")):
            with self.assertRaisesRegex(output.PublishError, "without following a symlink"):
                call()
        with self.assertRaisesRegex(output.PublishError, r"must not contain '\.\.'"):
            output.read_bytes(task / ".." / "task", "00_Assigments.md")

    def test_publish_refuses_a_task_folder_swapped_after_the_check(self):
        task = self.fx.write()
        b = output.Build(task, "swap")
        b.add("Working_Files/build/parts/linear.sql", b"-- B\n")
        b.plan()
        decoy = self.fx.root / "decoy"
        decoy.mkdir()
        task.rename(self.fx.root / "task.moved")
        os.symlink(decoy, task)                                # the task folder swapped after Build checked it
        with self.assertRaisesRegex(output.PublishError, "without following a symlink"):
            b.publish()
        b.discard()
        self.assertEqual(list(decoy.iterdir()), [])

    def test_unchanged_target_edited_or_removed_after_plan_is_refused(self):
        task = self.fx.write()
        rel = "Working_Files/build/a.txt"
        target = task / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        for edit, left in ((lambda: target.write_bytes(b"B"), b"B"), (target.unlink, None)):
            target.write_bytes(b"A")
            b = output.Build(task, "unchanged")
            b.add(rel, b"A")
            self.assertEqual([c.status for c in b.plan()], ["unchanged"])
            edit()
            with self.assertRaisesRegex(output.PublishError, "changed since plan"):
                b.publish()
            b.discard()
            self.assertEqual(target.read_bytes() if target.exists() else None, left)

    def test_prune_refuses_aliases_of_a_stored_revision(self):
        task = self.fx.write()
        (task / "01_Universe_Inject.sql").write_text("-- A\n")
        saved = output.store_revision(task, "rev1")
        for alias in ("./" + saved.path, saved.path.replace("Working_Files/", "Working_Files/./", 1)):
            b = output.Build(task, "alias")
            with self.subTest(alias=alias), self.assertRaisesRegex(output.PublishError, "not a canonical"):
                b.publish(prune=True, previous={alias: saved.sha256_new})
            b.discard()
        for alias in (saved.path.replace("Working_Files/run_forensics", "working_files/RUN_FORENSICS"),
                      saved.path.replace("forensics", "foren\u017fics"), saved.path.replace("Files", "\uff26iles")):
            b = output.Build(task, "folded")
            with self.subTest(alias=alias):
                self.assertEqual([c.status for c in b.publish(prune=True, previous={alias: saved.sha256_new})],
                                 ["stale"])
            b.discard()
        self.assertEqual((task / saved.path).read_bytes(), b"-- A\n")

    def test_stored_revision_folder_is_refused_by_identity_too(self):
        task = self.fx.write()
        (task / "01_Universe_Inject.sql").write_text("-- A\n")
        saved = output.store_revision(task, "rev1")
        with mock.patch.object(output, "_protected", lambda root, rel: False):   # the name check off: identity alone
            b = output.Build(task, "identity")
            with self.assertRaisesRegex(output.PublishError, "is the stored-revision folder"):
                b.publish(prune=True, previous={saved.path: saved.sha256_new})
            b.discard()
            b = output.Build(task, "identity2")
            b.add("Working_Files/run_forensics/rev1/other.sql", b"-- B\n")
            with self.assertRaisesRegex(output.PublishError, "is the stored-revision folder"):
                b.publish()
            b.discard()
            with self.assertRaisesRegex(output.PublishError, "is the stored-revision folder"):
                output.append_line(task, "Working_Files/run_forensics/rev1/log.jsonl", "x")
        self.assertEqual((task / saved.path).read_bytes(), b"-- A\n")
        self.assertEqual(sorted(p.name for p in (task / saved.path).parent.iterdir()), ["01_Universe_Inject.sql"])

    def _on_publish(self, which, action):
        """Run `action` just before the `which`-th Build.publish call (1: the outputs, 2: the build record)."""
        real = output.Build.publish
        calls = []

        def publish(b, *a, **k):
            calls.append(b.build_id)
            if len(calls) == which:
                action()
            return real(b, *a, **k)
        return mock.patch.object(output.Build, "publish", publish)

    def _edit_c1(self):
        self.fx.record("C1")["fields"]["body"] = self.fx.text("C1.txt", "Listed the done items.")
        self.fx.write()

    def test_input_edited_while_the_outputs_are_published_fails_the_render(self):
        task = self.fx.write()
        with self._on_publish(1, self._edit_c1):
            with self.assertRaisesRegex(pipeline.BuildError, "outputs were replaced but the build record was not"):
                pipeline.render(task)
        build = task / "Working_Files" / "build"
        self.assertTrue((build / "parts" / "linear.sql").exists())
        self.assertFalse((build / "build_record.json").exists())
        chk = pipeline.check(task)
        self.assertEqual(chk["verdict"], "FAIL")
        self.assertIn("Working_Files/build/parts/linear.sql", [s["path"] for s in chk["stale"]])
        self.assertEqual(pipeline.render(task)["verdict"], "PASS")
        self.assertEqual(pipeline.check(task)["verdict"], "PASS")

    def test_input_edited_while_the_record_is_written_fails_the_render(self):
        task = self.fx.write()
        with self._on_publish(2, self._edit_c1):
            with self.assertRaisesRegex(pipeline.BuildError, "build record was written but no longer matches"):
                pipeline.render(task)
        self.assertTrue((task / "Working_Files" / "build" / "build_record.json").exists())
        self.assertEqual(pipeline.check(task)["verdict"], "FAIL")
        self.assertEqual(pipeline.render(task)["verdict"], "PASS")
        self.assertEqual(pipeline.check(task)["verdict"], "PASS")

    def test_hand_edited_build_record_cannot_direct_prune(self):
        task = self.fx.write()
        pipeline.render(task)
        victim = task / "01_Universe_Inject.sql"
        victim.write_text("-- the task's own SQL\n")
        rec_path = task / "Working_Files" / "build" / "build_record.json"
        good = rec_path.read_text()
        for key in ("01_Universe_Inject.sql", "./Working_Files/build/parts/linear.sql",
                    "Working_Files/build/upgrades.jsonl", "Working_Files/run_forensics/rev1/01_Universe_Inject.sql"):
            rec = json.loads(good)
            rec["stale_outputs"][key] = output.sha256_file(victim)
            rec_path.write_text(json.dumps(rec))
            with self.subTest(key=key), self.assertRaisesRegex(pipeline.BuildError, "not an output this library"):
                pipeline.render(task, prune=True)
        self.assertEqual(victim.read_text(), "-- the task's own SQL\n")
        rec_path.write_text(good)
        self.assertEqual(pipeline.check(task)["verdict"], "PASS")

    def test_append_line_never_writes_through_a_hard_link(self):
        task = self.fx.write()
        log = task / "Working_Files" / "build" / "upgrades.jsonl"
        log.parent.mkdir(parents=True, exist_ok=True)
        other = task / "elsewhere.txt"
        other.write_text("keep\n")
        os.link(other, log)
        output.append_line(task, "Working_Files/build/upgrades.jsonl", '{"a": 1}')
        self.assertEqual(other.read_text(), "keep\n")
        self.assertEqual(log.read_text(), 'keep\n{"a": 1}\n')

    def test_insert_must_write_required_columns_and_no_generated_one(self):
        cols = (("id", "c-1"), ("issue_id", "ENG-1"), ("author_id", "usr_a"), ("parent_id", None), ("body", "b"),
                ("created_at", "2025-09-01T00:00:00Z"), ("updated_at", "2025-09-01T00:00:00Z"), ("sequence", 1))
        found = coltypes.check_ops([Op("linear.linear_comments", "insert", cols)], pipeline.SCHEMA_LIVE)
        self.assertEqual(found, ["linear.linear_comments id=c-1: NOT NULL column is_edited has no default and is "
                                 "not written"])
        found = coltypes.check_ops([Op("slack.slack_messages", "update", (("text_fts", "x"),), where=(("id", "m1"),))],
                                   pipeline.SCHEMA_LIVE)
        self.assertTrue(any("generated column" in m for m in found), found)

    # -- formal gate, round 3 (code + redteam)
    def test_task_folder_swapped_for_another_task_during_the_build_is_refused(self):
        task = self.fx.write()
        other_fx = Fixture()
        try:
            other_fx.record("C1")["fields"]["body"] = other_fx.text("C1.txt", "Another task's note.")
            other = other_fx.write()
            moved = task.with_name("task.moved")
            real_previous, real_validate = pipeline.previous_record, pipeline.validate

            def previous_then_swap(task_dir):               # after the lock: the task path now leads to another task
                out = real_previous(task_dir)
                task.rename(moved)
                os.symlink(other, task)
                return out

            def restore_then_validate(res, *a, **k):        # and leads back before anything is published
                task.unlink()
                moved.rename(task)
                return real_validate(res, *a, **k)
            with mock.patch.object(pipeline, "previous_record", previous_then_swap), \
                    mock.patch.object(pipeline, "validate", restore_then_validate):
                try:
                    with self.assertRaisesRegex(SpecError, "without following a symlink"):
                        pipeline.render(task)
                finally:
                    if task.is_symlink():
                        task.unlink()
                        moved.rename(task)
            for t in (task, other):
                self.assertFalse((t / "Working_Files" / "build" / "parts").exists(), t)
            self.assertEqual(pipeline.render(task)["verdict"], "PASS")
        finally:
            other_fx.cleanup()

    def test_dependency_modified_during_a_render_publishes_nothing(self):
        task = self.fx.write()
        target = str(context.DEPENDENCY_FILES[0])
        real_stamp, real_validate = context.file_stamp, pipeline.validate
        touched = []

        def validate_after_a_touch(res, *a, **k):         # the file is modified (and put back) while the run works
            touched.append(True)
            return real_validate(res, *a, **k)

        def stamp(p):
            return ("moved",) if touched and str(p) == target else real_stamp(p)
        with mock.patch.object(context, "file_stamp", stamp), \
                mock.patch.object(pipeline, "validate", validate_after_a_touch):
            with self.assertRaisesRegex(context.ToolsChanged, "modified since this process loaded tools/"):
                pipeline.render(task)
        self.assertFalse((task / "Working_Files" / "build" / "parts").exists())
        self.assertFalse((task / "Working_Files" / "build" / "build_record.json").exists())

    def test_census_file_shared_by_two_claims_is_refused(self):
        self.census(CENSUS_OK)
        self.fx.record("C1")["fields"]["body"] = self.fx.text("C1.txt", "Listed the done items.",
                                                              claims=["ENG-2366 closed later"])
        entry = self.fx.doc["census"]["ENG-2366 open"]
        for spelling in ("census/eng2366.json", "census/ENG2366.json"):
            self.fx.doc["census"]["ENG-2366 closed later"] = dict(entry, file=spelling)
            with self.subTest(spelling=spelling), self.assertRaisesRegex(SpecError, "also the census file of claim"):
                pipeline.build(self.fx.write())

    def test_text_file_spelled_two_ways_is_refused(self):
        body = self.fx.record("C1")["fields"]["body"]
        self.assertEqual(body["text"], "texts/C1.txt")
        self.fx.record("C2")["fields"]["body"] = dict(body, text="texts/c1.txt")      # the same file on APFS
        with self.assertRaisesRegex(SpecError, "name the same file on a case-insensitive filesystem"):
            pipeline.build(self.fx.write())

    def test_upgrade_is_logged_before_the_record_and_only_once(self):
        task = self.fx.write()
        pipeline.render(task)
        rec_path = task / "Working_Files" / "build" / "build_record.json"
        rec = json.loads(rec_path.read_text())
        rec["dependencies"]["conventions"] = "0" * 64
        rec_path.write_text(json.dumps(rec))
        log = task / "Working_Files" / "build" / "upgrades.jsonl"
        real = output.Build.publish

        def record_fails(b, *a, **k):                       # stands for a crash while the record is written
            if b.build_id.endswith("-record"):
                raise output.PublishError("interrupted")
            return real(b, *a, **k)
        with mock.patch.object(output.Build, "publish", record_fails):
            with self.assertRaisesRegex(output.PublishError, "interrupted"):
                pipeline.render(task, accept_upgrade=True)
        self.assertEqual(len(log.read_text().splitlines()), 1)                     # logged although no record
        self.assertEqual(json.loads(rec_path.read_text())["dependencies"]["conventions"], "0" * 64)
        self.assertEqual(pipeline.render(task, accept_upgrade=True)["verdict"], "PASS")
        self.assertEqual(len(log.read_text().splitlines()), 1)                     # the repeat is not logged twice
        self.assertIn("conventions", json.loads(log.read_text())["upgrades"])
        self.assertEqual(pipeline.check(task)["verdict"], "PASS")

    def test_a_task_dir_inside_a_stored_revision_folder_cannot_write_there(self):
        task = self.fx.write()
        (task / "01_Universe_Inject.sql").write_text("-- A\n")
        saved = output.store_revision(task, "rev1")
        stored = task / saved.path
        forensics = task / "Working_Files" / "run_forensics"
        attempts = {
            "build in the forensics folder": lambda: output.Build(forensics, "x"),
            "build in a revision": lambda: output.Build(stored.parent, "x"),
            "build above it, publishing into it": lambda: output.Build(task / "Working_Files", "x").add(
                "run_forensics/rev1/01_Universe_Inject.sql", b"-- B\n"),
            "build above it, case alias": lambda: output.Build(task / "Working_Files", "x").add(
                "RUN_FORENSICS/rev1/new.sql", b"-- B\n"),
            "lock in a revision": lambda: output.TaskLock(stored.parent).__enter__(),
            "log in a revision": lambda: output.append_line(task / "Working_Files", "run_forensics/rev1/log", "x"),
            "store from a revision": lambda: output.store_revision(stored.parent, "rev2"),
        }
        for what, attempt in attempts.items():
            with self.subTest(what), self.assertRaisesRegex(output.PublishError, "stored-revision folder"):
                attempt()
        rebased = output.Build(task / "Working_Files", "prune")         # a stale path there is left, not removed
        self.assertEqual([c.status for c in rebased.publish(
            prune=True, previous={"run_forensics/rev1/01_Universe_Inject.sql": saved.sha256_new})], ["stale"])
        rebased.discard()
        self.assertEqual(stored.read_bytes(), b"-- A\n")
        self.assertEqual(sorted(p.name for p in stored.parent.iterdir()), ["01_Universe_Inject.sql"])

    # -- formal gate, round 4 (code + redteam)
    def test_clearing_a_staging_folder_keeps_a_stored_revision_inside_it(self):
        task = self.fx.write()
        b = output.Build(task, "example")                                  # the code review's example
        b.add("seed.sql", b"-- reviewed SQL\n")
        stored = b.staging / output.store_revision(b.staging, "rev1", "seed.sql").path
        b.discard()                                                         # best effort: the revision is kept
        self.assertEqual(stored.read_bytes(), b"-- reviewed SQL\n")
        self.assertFalse((b.staging / "seed.sql").exists())               # the rest of the staging folder is gone
        with self.assertRaisesRegex(output.PublishError, "holds a stored-revision folder"):
            output.Build(task, "example")
        self.assertEqual(stored.read_bytes(), b"-- reviewed SQL\n")
        nested = task / "Working_Files" / "build" / "staging" / "wipe"    # the red team's example
        nested.mkdir(parents=True)
        (nested / "01_Universe_Inject.sql").write_bytes(b"-- reviewed\n")
        victim = nested / output.store_revision(nested, "rev1").path
        with self.assertRaisesRegex(output.PublishError, "holds a stored-revision folder"):
            output.Build(task, "wipe")
        self.assertEqual(victim.read_bytes(), b"-- reviewed\n")

    def test_task_folder_swapped_while_publishing_writes_only_into_the_original_folder(self):
        task = self.fx.write()
        b = output.Build(task, "mid")
        b.add("Working_Files/build/a.txt", b"A")
        b.add("Working_Files/build/b.txt", b"B")
        decoy = self.fx.root / "decoy"
        (decoy / "Working_Files" / "build").mkdir(parents=True)
        moved = task.with_name("task.moved")
        real, swapped = output._write_at, []

        def swap_then_write(dfd, name, data):              # the swap lands between the hash check and the write
            if not swapped:
                swapped.append(name)
                task.rename(moved)
                os.symlink(decoy, task)
            return real(dfd, name, data)
        try:
            with mock.patch.object(output, "_write_at", swap_then_write):
                with self.assertRaisesRegex(output.PublishError, r"already published: \['Working_Files/build/a.txt'\]"):
                    b.publish()
        finally:
            if task.is_symlink():
                task.unlink()
                moved.rename(task)
        b.discard()
        self.assertEqual((task / "Working_Files" / "build" / "a.txt").read_bytes(), b"A")
        self.assertFalse((task / "Working_Files" / "build" / "b.txt").exists())
        self.assertEqual(list((decoy / "Working_Files" / "build").iterdir()), [])

    # -- formal gate, round 5 (code + redteam)
    def test_task_folder_replaced_by_another_real_folder_while_locked_is_refused(self):
        task = self.fx.write()
        other_fx = Fixture()
        try:
            other = other_fx.write()
            saved = task.with_name("task.saved")
            rel = "Working_Files/build/parts/linear.sql"

            def swap():                                     # another real folder (no symlink) at the task's path
                task.rename(saved)
                other.rename(task)

            def restore():
                task.rename(other)
                saved.rename(task)
            with output.TaskLock(task):                     # through the output API, under the lock
                b = output.Build(task, "swap")
                b.add(rel, b"-- for this task\n")
                b.plan()
                swap()
                try:
                    with self.assertRaisesRegex(output.PublishError, "no longer the task folder this command locked"):
                        b.publish()
                finally:
                    restore()
                b.discard()
            self.assertFalse((other / rel).exists())
            self.assertFalse((task / rel).exists())
            real_settle = pipeline._settle

            def settle_then_swap(res, deps, consequence):   # a render, swapped after its last check before publishing
                real_settle(res, deps, consequence)
                if consequence == "nothing published":
                    swap()
            with mock.patch.object(pipeline, "_settle", settle_then_swap):
                try:
                    with self.assertRaisesRegex(output.PublishError, "no longer the task folder this command locked"):
                        pipeline.render(task)
                finally:
                    if saved.exists():
                        restore()
            self.assertFalse((other / "Working_Files" / "build" / "parts").exists())
            self.assertFalse((task / "Working_Files" / "build" / "parts").exists())
            self.assertEqual(pipeline.render(task)["verdict"], "PASS")
        finally:
            other_fx.cleanup()

    # -- formal gate, round 7
    def test_task_folder_replaced_before_the_record_names_the_outputs_already_published(self):
        task = self.fx.write()
        original = task.with_name("task.original")
        real = output.Build.publish

        def replace_before_the_record(b, *a, **k):          # another real folder at the task path, just before
            if b.build_id.endswith("-record"):
                task.rename(original)
                task.mkdir()
            return real(b, *a, **k)
        outputs = ["Working_Files/build/parts/linear.sql", "Working_Files/build/provenance.json"]
        try:
            with mock.patch.object(output.Build, "publish", replace_before_the_record):
                with self.assertRaises(output.PublishError) as caught:
                    pipeline.render(task)
            self.assertIn("no longer the task folder this command locked", str(caught.exception))
            self.assertEqual(caught.exception.__notes__, [f"files already published: {outputs}"])
            for rel in outputs:
                self.assertTrue((original / rel).is_file(), rel)
            self.assertEqual(list(task.iterdir()), [])                 # the replacement is untouched
        finally:
            if original.exists():
                task.rmdir()
                original.rename(task)
        self.assertEqual(pipeline.render(task)["verdict"], "PASS")
        self.assertEqual(pipeline.check(task)["verdict"], "PASS")

    def test_every_failure_after_publishing_names_the_files_already_published(self):
        outputs = ["Working_Files/build/parts/linear.sql", "Working_Files/build/provenance.json"]
        record = "Working_Files/build/build_record.json"
        dependency = str(context.DEPENDENCY_FILES[0])
        real_publish, real_stamp = output.Build.publish, context.file_stamp
        for when, expected in (("outputs", outputs), ("record", [*outputs, record])):
            fx = Fixture()
            try:
                task, touched = fx.write(), []

                def publish(b, *a, _when=when, _task=task, **k):
                    done = real_publish(b, *a, **k)
                    if b.build_id.endswith("-record") == (_when == "record"):
                        if _when == "outputs":
                            touched.append(True)           # a dependency stamp moves (a tools/ change, not raised)
                        else:                              # the spec changes after the record was written
                            spec = _task / "Working_Files" / "spec" / "spec.json"
                            spec.write_bytes(spec.read_bytes() + b"\n")
                    return done

                def stamp(p):
                    return ("moved",) if touched and str(p) == dependency else real_stamp(p)
                with self.subTest(when=when), mock.patch.object(output.Build, "publish", publish), \
                        mock.patch.object(context, "file_stamp", stamp):
                    with self.assertRaises(pipeline.BuildError) as caught:
                        pipeline.render(task)
                    self.assertEqual(caught.exception.__notes__, [f"files already published: {expected}"])
                    for rel in expected:
                        self.assertTrue((task / rel).is_file(), rel)
            finally:
                fx.cleanup()

    # -- formal gate, round 9
    def test_an_interrupt_after_publishing_carries_the_note(self):
        task = self.fx.write()
        real = pipeline._settle

        def interrupt_at_the_last_settle(res, deps, consequence):
            if consequence.startswith("the build record was written"):
                raise KeyboardInterrupt
            return real(res, deps, consequence)
        with mock.patch.object(pipeline, "_settle", interrupt_at_the_last_settle):
            with self.assertRaises(KeyboardInterrupt) as caught:
                pipeline.render(task)
        files = ["Working_Files/build/parts/linear.sql", "Working_Files/build/provenance.json",
                 "Working_Files/build/build_record.json"]
        self.assertEqual(caught.exception.__notes__, [f"files already published: {files}"])

    def test_a_failed_staging_cleanup_after_publishing_does_not_replace_the_outcome(self):
        task = self.fx.write()
        real = output._remove_tree

        def too_deep(parent_fd, name, parts):               # clearing the outputs' staging folder fails
            if parts[-1] == "staging" and not name.endswith("-record"):
                raise RecursionError("a very deep staging tree")
            return real(parent_fd, name, parts)
        with mock.patch.object(output, "_remove_tree", too_deep):
            self.assertEqual(pipeline.render(task)["verdict"], "PASS")
        staging = task / "Working_Files" / "build" / "staging"
        self.assertTrue(any(staging.iterdir()))                         # left for the next build of the same id
        self.assertEqual(pipeline.render(task)["verdict"], "PASS")
        self.assertEqual(list(staging.iterdir()), [])
        self.assertEqual(pipeline.check(task)["verdict"], "PASS")

    def test_parse_back_takes_a_relative_sql_path_under_the_task(self):
        from generators import render as cli
        task = self.fx.write()
        self.assertNotEqual(Path.cwd().resolve(), task.resolve())
        (task / "assembled.sql").write_bytes(pipeline.build(task).full_sql().encode("utf-8"))
        with mock.patch("sys.stdout", new_callable=io.StringIO) as out:
            self.assertEqual(cli.main(["parse-back", "--task-dir", str(task), "--sql", "assembled.sql", "--json"]), 0)
        self.assertEqual(json.loads(out.getvalue())["verdict"], "PASS")

    def test_the_cli_prints_the_notes_an_error_carries(self):
        from generators import render as cli
        failure = output.PublishError("boom")
        failure.add_note("files already published: ['Working_Files/build/parts/linear.sql']")
        with mock.patch.object(cli.pipeline, "render", side_effect=failure), \
                mock.patch("sys.stderr", new_callable=io.StringIO) as err:
            self.assertEqual(cli.main(["render", "--task-dir", str(self.fx.write())]), 1)
        self.assertEqual(err.getvalue().splitlines(),
                         ["PUBLISH FAIL: boom", "  files already published: ['Working_Files/build/parts/linear.sql']"])

    def test_parse_back_of_a_foreign_file_reads_its_exact_bytes(self):
        from generators import render as cli
        task = self.fx.write()
        text = pipeline.build(task).full_sql()
        rendered = "E'Q4 close-out work for DD.\\nOne line per item.'"
        self.assertIn(rendered, text)
        foreign = task / "foreign.sql"
        for literal, differs in (("'Q4 close-out work for DD.\nOne line per item.'", False),
                                 ("'Q4 close-out work for DD.\r\nOne line per item.'", True)):
            foreign.write_bytes(text.replace(rendered, literal).encode("utf-8"))
            with self.subTest(literal=literal), mock.patch("sys.stdout", new_callable=io.StringIO) as out:
                cli.main(["parse-back", "--task-dir", str(task), "--sql", str(foreign), "--json"])
                report = json.loads(out.getvalue())
                self.assertEqual(bool(report["compare"]), differs, report["compare"])

    # -- dependency pins do not depend on what this process imported
    def test_tool_closure_is_import_independent(self):
        first = pipeline.tool_closure()
        self.assertEqual(first, pipeline.tool_closure())
        self.assertTrue({"sql_lint.py", "base_check.py", "task_context.py", "runtime_context.py"} <= set(first))
        with mock.patch.dict("sys.modules", {"unrelated_tool": mock.Mock(__file__=str(pipeline.TA / "tools" / "x.py"))}):
            self.assertEqual(first, pipeline.tool_closure())


def _annotated(x: int) -> int:     # this file has no `from __future__ import annotations`: x is the class int
    return x


def _run_py(code):
    """`code` in a fresh interpreter (no bytecode written), from the workspace root."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("TASK_AUTHORING_")}
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.run([sys.executable, "-B", "-c", code], capture_output=True, text=True, env=env,
                          cwd=str(pipeline.WS), timeout=300)


class PinnedLibraryTest(unittest.TestCase):
    """Formal gate, round 3: the library code a render runs is the code its build record pins."""

    def test_library_modules_run_from_the_bytes_they_are_pinned_by(self):
        p = _run_py(
            "import hashlib, sys\nsys.path.insert(0, %r)\n"
            "import generators\nfrom generators.core import pipeline\nimport generators.tests.fixtures.task_fixture\n"
            "mods = {n: m for n, m in sys.modules.items() if n.startswith('generators.')}\n"
            "assert len(mods) > 15, sorted(mods)\n"
            "for n, m in mods.items():\n"
            "    assert m.__spec__.loader is generators._FINDER, n\n"
            "    f = getattr(m, '__file__', None)\n"
            "    if f:\n"
            "        sha = hashlib.sha256(open(f, 'rb').read()).hexdigest()\n"
            "        assert generators._LOADED[generators._rel(f)] == sha, n\n"
            "assert generators.changed_since_load() == [], generators.changed_since_load()\n"
            "try:\n    import generators.core.no_such_module\nexcept ModuleNotFoundError:\n    pass\n"
            "else:\n    raise AssertionError('a module with no .py file was found')\n"
            "print('PINNED', len(mods))\n" % str(pipeline.TA))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("PINNED", p.stdout)

    def test_render_script_pins_itself(self):
        script = pipeline.LIB / "render.py"
        p = _run_py(
            "import hashlib, runpy, sys\nrunpy.run_path(%r, run_name='render_probe')\nimport generators\n"
            "assert generators._LOADED['render.py'] == hashlib.sha256(open(%r, 'rb').read()).hexdigest()\n"
            "assert sys.pycache_prefix.startswith('/dev/null/'), sys.pycache_prefix\nprint('PINNED')\n"
            % (str(script), str(script)))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("PINNED", p.stdout)

    def test_library_changed_on_disk_after_loading_is_refused(self):
        with mock.patch.dict(generators._LOADED, {"core/output.py": "0" * 64}):
            self.assertIn("core/output.py: changed on disk since this process loaded it",
                          generators.changed_since_load())
            with self.assertRaisesRegex(generators.LibraryChanged, "new process"):
                pipeline.dependencies()
            moved = pipeline._moved(pipeline._fingerprint(context.load_tools()))
            self.assertIn("library core/output.py: changed on disk since this process loaded it", moved)
        generators.ensure_current()

    def test_library_module_loaded_by_another_loader_is_refused(self):
        p = _run_py(
            "import importlib.util, sys\nsys.path.insert(0, %r)\n"
            "import generators\nfrom generators.core import pipeline\n"
            "path = generators.ROOT / 'core' / 'ops.py'\n"
            "spec = importlib.util.spec_from_file_location('generators.core.ops', path)\n"
            "module = importlib.util.module_from_spec(spec)\nspec.loader.exec_module(module)\n"
            "sys.modules['generators.core.ops'] = module\n"
            "try:\n    pipeline.dependencies()\nexcept generators.LibraryChanged as exc:\n    print('REFUSED', exc)\n"
            % str(pipeline.TA))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("REFUSED", p.stdout)
        self.assertIn("generators.core.ops: not loaded by the library's finder", p.stdout)

    # -- formal gate, round 6
    def test_a_module_first_loaded_elsewhere_then_reloaded_is_refused(self):
        p = _run_py(
            "import importlib, importlib.abc, importlib.util, shutil, sys, tempfile\nfrom pathlib import Path\n"
            "sys.path.insert(0, %r)\nimport generators\n"
            "shadow = Path(tempfile.mkdtemp()) / 'sqlvalue.py'\n"
            "wrapper = b'\\n_earlier = literal\\ndef literal(v, _impl=_earlier):\\n    return _impl(v)\\n'\n"
            "shadow.write_bytes((generators.ROOT / 'core' / 'sqlvalue.py').read_bytes() + wrapper)\n"
            "class Other(importlib.abc.MetaPathFinder):\n"
            "    def find_spec(self, fullname, path=None, target=None):\n"
            "        if fullname == 'generators.core.sqlvalue':\n"
            "            return importlib.util.spec_from_file_location(fullname, shadow)\n"
            "sys.meta_path.insert(0, Other())\nfrom generators.core import emitter, sqlvalue\nsys.meta_path.pop(0)\n"
            "importlib.reload(sqlvalue)\nfrom generators.core import pipeline\nshutil.rmtree(shadow.parent)\n"
            "assert emitter.literal is not sqlvalue.literal\n"
            "try:\n    pipeline.dependencies()\n"
            "except generators.LibraryChanged as exc:\n    print('REFUSED', exc)\n" % str(pipeline.TA))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("REFUSED", p.stdout)
        self.assertIn("generators.core.emitter.literal: holds generators.core.sqlvalue.literal from an earlier load",
                      p.stdout)

    def test_a_library_module_run_again_by_a_loader_called_directly_is_refused(self):
        p = _run_py(
            "import sys\nfrom importlib.machinery import SourceFileLoader\nsys.path.insert(0, %r)\n"
            "import generators\nfrom generators.core import pipeline, sqlvalue\n"
            "SourceFileLoader(sqlvalue.__name__, sqlvalue.__file__).exec_module(sqlvalue)\n"
            "try:\n    pipeline.dependencies()\n"
            "except generators.LibraryChanged as exc:\n    print('REFUSED', exc)\n" % str(pipeline.TA))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("REFUSED", p.stdout)
        self.assertIn("from an earlier load of generators.core.sqlvalue", p.stdout)

    def test_a_module_no_other_imports_from_run_again_by_a_loader_called_directly_is_refused(self):
        p = _run_py(
            "import sys\nfrom importlib.machinery import SourceFileLoader\nsys.path.insert(0, %r)\n"
            "import generators\nfrom generators.core import emitter, pipeline\n"
            "SourceFileLoader(emitter.__name__, emitter.__file__).exec_module(emitter)\n"
            "try:\n    pipeline.dependencies()\n"
            "except generators.LibraryChanged as exc:\n    print('REFUSED', exc)\n" % str(pipeline.TA))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("REFUSED", p.stdout)
        self.assertIn("generators.core.emitter: its own", p.stdout)

    def test_a_library_file_modified_since_loading_is_refused_even_with_its_bytes_put_back(self):
        real = generators._stamp
        target = generators.ROOT / "core" / "output.py"
        with mock.patch.object(generators, "_stamp", lambda p: ("moved",) if Path(p) == target else real(p)):
            self.assertIn("core/output.py: modified since this process loaded it", generators.changed_since_load())
            with self.assertRaisesRegex(generators.LibraryChanged, "new process"):
                pipeline.dependencies()
        generators.ensure_current()

    def test_a_bytecode_cache_under_the_library_is_refused(self):
        self.assertEqual(generators._bytecode_caches(), [])
        with mock.patch.object(generators, "_bytecode_caches", return_value=["core/__pycache__"]):
            self.assertIn("core/__pycache__: a bytecode cache under the library", generators.changed_since_load())
            with self.assertRaisesRegex(generators.LibraryChanged, "bytecode cache"):
                pipeline.dependencies()
        generators.ensure_current()

    def test_a_module_run_by_another_loader_then_by_the_finder_is_refused(self):
        p = _run_py(
            "import importlib, importlib.util, sys\nsys.path.insert(0, %r)\n"
            "import generators, generators.core\n"
            "name, path = 'generators.core.emitter', generators.ROOT / 'core' / 'emitter.py'\n"
            "spec = importlib.util.spec_from_file_location(name, path)\n"
            "module = importlib.util.module_from_spec(spec)\nsys.modules[name] = module\n"
            "generators.core.emitter = module\nspec.loader.exec_module(module)\n"
            "earlier = module.to_sql\nimportlib.reload(module)\nassert earlier is not module.to_sql\n"
            "from generators.core import pipeline\n"
            "try:\n    pipeline.dependencies()\n"
            "except generators.LibraryChanged as exc:\n    print('REFUSED', exc)\n" % str(pipeline.TA))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("REFUSED", p.stdout)
        self.assertIn("generators.core.emitter: loaded again in this process", p.stdout)

    def test_a_library_module_executed_again_is_refused(self):
        for again in ("importlib.reload(sqlvalue)",
                      "del sys.modules['generators.core.sqlvalue']\nimport generators.core.sqlvalue"):
            with self.subTest(again=again):
                p = _run_py(
                    "import importlib, sys\nsys.path.insert(0, %r)\n"
                    "import generators\nfrom generators.core import pipeline, sqlvalue\n%s\n"
                    "try:\n    pipeline.dependencies()\n"
                    "except generators.LibraryChanged as exc:\n    print('REFUSED', exc)\n"
                    % (str(pipeline.TA), again))
                self.assertEqual(p.returncode, 0, p.stderr)
                self.assertIn("REFUSED", p.stdout)
                self.assertIn("generators.core.sqlvalue: loaded again in this process", p.stdout)


class CompileFlagsTest(unittest.TestCase):
    """Formal gate, round 3: loaded code runs with its own __future__ flags, as Python runs it, never the loader's."""

    SOURCE = b"def f(x: int) -> int:\n    return x\n"

    def test_library_finder(self):
        self.assertIs(sys.modules[__name__].__spec__.loader, generators._FINDER)
        self.assertIs(_annotated.__annotations__["x"], int)

    def test_eval_tokenizer_loader(self):
        module = parse_back._load_module("gen_flags_probe", Path("gen_flags_probe.py"), self.SOURCE)
        try:
            self.assertIs(module.f.__annotations__["x"], int)
        finally:
            sys.modules.pop("gen_flags_probe", None)

    def test_pinned_tools_loader(self):
        finder = context._Pinned({"gen_flags_probe_tool": (Path("gen_flags_probe_tool.py"), self.SOURCE)})
        sys.meta_path.insert(0, finder)
        try:
            self.assertIs(importlib.import_module("gen_flags_probe_tool").f.__annotations__["x"], int)
        finally:
            sys.meta_path.remove(finder)
            sys.modules.pop("gen_flags_probe_tool", None)


class PinnedToolsTest(unittest.TestCase):
    """Formal gate, round 2: the tools/ code validation runs is the code the build record pins."""

    def run_py(self, code):
        return _run_py(code)

    def test_tools_run_from_the_bytes_they_are_pinned_by(self):
        p = self.run_py(
            "import hashlib, sys\nsys.path.insert(0, %r)\n"
            "from generators.core import context\n"
            "loaded = context.load_tools()\n"
            "for name in ('task_context', 'runtime_context', 'sql_lint', 'base_check'):\n"
            "    m = sys.modules[name]\n"
            "    assert type(m.__spec__.loader).__name__ == '_Pinned', name\n"
            "    assert loaded[name + '.py'] == hashlib.sha256(open(m.__file__, 'rb').read()).hexdigest(), name\n"
            "    assert context.tools_module(name) is m, name\n"
            "print('PINNED', sorted(loaded))\n" % str(pipeline.TA))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("PINNED", p.stdout)

    def test_tools_imported_before_the_library_are_refused(self):
        p = self.run_py(
            "import sys\nsys.path[:0] = [%r, %r]\n"
            "import sql_lint\n"
            "from generators.core import context\n"
            "try:\n    context.load_tools()\nexcept context.ToolsChanged as exc:\n    print('REFUSED', exc)\n"
            % (str(pipeline.TA), str(pipeline.TA / "tools")))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("REFUSED", p.stdout)
        self.assertIn("sql_lint", p.stdout)

    def test_tools_changed_on_disk_after_loading_are_refused(self):
        loaded = context.load_tools()
        changed = dict(loaded, **{"sql_lint.py": "0" * 64})
        on_disk = mock.Mock(return_value=changed)            # both names, so no module holds the earlier function
        with mock.patch.object(context, "tool_closure", on_disk), mock.patch.object(pipeline, "tool_closure", on_disk):
            with self.assertRaisesRegex(context.ToolsChanged, "sql_lint.py"):
                context.tools_module("sql_lint")
            with self.assertRaisesRegex(context.ToolsChanged, "new process"):
                pipeline.dependencies()
            self.assertIn("tools/ sql_lint.py: changed on disk", pipeline._moved(pipeline._fingerprint(loaded)))
        context.ensure_tools_current()

    # -- formal gate, round 3
    def test_a_module_named_like_a_tool_imported_from_elsewhere_is_refused(self):
        p = self.run_py(
            "import sys, types\nsys.path.insert(0, %r)\n"
            "fake = types.ModuleType('sql_lint')\nfake.__file__ = '/elsewhere/other_checkout/tools/sql_lint.py'\n"
            "sys.modules['sql_lint'] = fake\n"
            "from generators.core import context\n"
            "try:\n    context.load_tools()\nexcept context.ToolsChanged as exc:\n    print('REFUSED', exc)\n"
            "else:\n    print('LOADED, foreign module used:', context.tools_module('sql_lint') is fake)\n"
            % str(pipeline.TA))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("REFUSED", p.stdout)
        self.assertIn("other_checkout", p.stdout)

    def test_a_tools_module_executed_again_by_another_loader_is_refused(self):
        p = self.run_py(
            "import importlib, sys\nsys.path.insert(0, %r)\n"
            "from generators.core import context, pipeline\n"
            "module = context.tools_module('base_check')\n"
            "sys.path.insert(0, str(context.TOOLS))\nimportlib.reload(module)\n"
            "try:\n    pipeline.dependencies()\nexcept context.ToolsChanged as exc:\n    print('REFUSED', exc)\n"
            % str(pipeline.TA))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("REFUSED", p.stdout)
        self.assertIn("base_check: executed again by another loader", p.stdout)

    def test_an_absent_dependency_created_and_removed_again_is_refused(self):
        p = self.run_py(
            "import shutil, sys, tempfile\nfrom pathlib import Path\nsys.path.insert(0, %r)\n"
            "from generators.core import context, pipeline\n"
            "folder = Path(tempfile.mkdtemp())\nabsent = folder / 'optional.json'\n"
            "context.DEPENDENCY_FILES = (*context.DEPENDENCY_FILES, absent)\ncontext.load_tools()\n"
            "absent.write_text('{}')\nabsent.unlink()            # created, read, removed: absent both times\n"
            "try:\n    pipeline.dependencies()\nexcept context.ToolsChanged as exc:\n    print('REFUSED', exc)\n"
            "shutil.rmtree(folder)\n" % str(pipeline.TA))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("REFUSED", p.stdout)
        self.assertIn("an entry was added or removed since this process loaded tools/", p.stdout)

    def test_a_tools_module_run_again_by_a_loader_called_directly_is_refused(self):
        p = self.run_py(
            "import sys\nfrom importlib.machinery import SourceFileLoader\nsys.path.insert(0, %r)\n"
            "from generators.core import context, pipeline\n"
            "module = context.tools_module('base_check')\n"
            "SourceFileLoader(module.__name__, module.__file__).exec_module(module)\n"
            "try:\n    pipeline.dependencies()\nexcept context.ToolsChanged as exc:\n    print('REFUSED', exc)\n"
            % str(pipeline.TA))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("REFUSED", p.stdout)
        self.assertIn("base_check: its functions or classes are no longer those its pinned bytes defined", p.stdout)

    def test_a_file_modified_after_loading_is_refused_even_with_its_bytes_put_back(self):
        context.load_tools()
        real = context.file_stamp
        dependency = str(context.DEPENDENCY_FILES[0])
        closure = str(context.TOOLS / "sql_lint.py")
        for path, message in ((dependency, f"{dependency}: modified since this process loaded tools/"),
                              (closure, "sql_lint.py: modified since it was loaded")):
            def stamp(p, path=path):                        # same bytes, but the stamp moved: modified in between
                return ("moved",) if str(p) == path else real(p)
            with self.subTest(path=path), mock.patch.object(context, "file_stamp", stamp):
                self.assertIn(message, context.tools_changed())
                with self.assertRaisesRegex(context.ToolsChanged, "new process"):
                    pipeline.dependencies()
        context.ensure_tools_current()

    def test_dependency_files_cover_what_validation_reads(self):
        reads = {*pipeline.DATA_FILES.values(), pipeline.registry.CONVENTIONS_PATH,
                 *(parse_back.DEFAULT_EVALS_TOOLS / name for name in parse_back.load_eval_parser().pins)}
        self.assertEqual({p.resolve() for p in context.DEPENDENCY_FILES}, {Path(p).resolve() for p in reads})


class CachesFollowContentTest(unittest.TestCase):
    """Round 2: a validator loaded earlier in the process must not keep checking against an old file."""

    def setUp(self):
        import shutil
        import tempfile
        self.shutil = shutil
        scratch = Path(pipeline.TA) / "support" / "scratch"
        scratch.mkdir(parents=True, exist_ok=True)
        self.dir = Path(tempfile.mkdtemp(prefix="gen_cache_", dir=scratch))

    def tearDown(self):
        self.shutil.rmtree(self.dir, ignore_errors=True)

    def test_json_and_date_values_postgres_would_reject(self):
        from generators.validate import coltypes
        js = {"udt": "json", "nullable": "YES"}
        self.assertIsNone(coltypes.problem(js, '{"a": [1, 2.5, null]}'))
        self.assertIn("not JSON", coltypes.problem(js, "NaN"))
        self.assertIn("not JSON", coltypes.problem(js, '{"a": Infinity}'))
        date = {"udt": "date", "nullable": "YES"}
        self.assertIsNone(coltypes.problem(date, "2024-02-29"))
        self.assertIn("real YYYY-MM-DD", coltypes.problem(date, "2025-02-30"))
        ts = {"udt": "timestamptz", "nullable": "YES"}
        self.assertIsNone(coltypes.problem(ts, "2025-09-30T12:00:00Z"))
        self.assertIn("real ISO-8601", coltypes.problem(ts, "2025-09-30T25:00:00Z"))
        self.assertIn("real ISO-8601", coltypes.problem(ts, "2025-\uff10\uff19-30T12:00:00Z"))
        self.assertIn("real YYYY-MM-DD", coltypes.problem(date, "\uff12025-01-01"))
        jsonb = {"udt": "jsonb", "nullable": "YES"}
        self.assertIn("\\u0000", coltypes.problem(jsonb, r'{"x": "\u0000"}'))
        self.assertIsNone(coltypes.problem(js, r'{"x": "\u0000"}'))            # json (text) can hold it
        self.assertIn("surrogate", coltypes.problem(js, r'{"x": "\ud800"}'))
        self.assertIn("\\u0000", coltypes.problem(jsonb, r'{"x":"\u0000","x":"ok"}'))     # a repeated key hides nothing
        self.assertIn("surrogate", coltypes.problem(js, r'{"x":"\ud800","x":"ok"}'))
        self.assertIn("surrogate", coltypes.problem(jsonb, r'[{"a": {"b": "\udc00", "b": 1}}]'))
        self.assertIsNone(coltypes.problem(jsonb, r'{"x": 1, "x": 2, "y": [true, null]}'))
        self.assertIn("surrogate", coltypes.problem({"udt": "text", "nullable": "YES"}, "a\ud800"))

    def test_explicit_null_needs_a_nullable_column(self):
        from generators.validate import coltypes
        color = coltypes.load(pipeline.SCHEMA_LIVE)["linear.linear_projects"]["color"]
        self.assertEqual(color["nullable"], "NO")
        self.assertIsNotNone(color["default"])
        self.assertEqual(coltypes.problem(color, None), "NULL in a NOT NULL column")

    def test_schema_caches_reload_a_changed_file(self):
        from generators.validate import coltypes, parse_back
        schema = self.dir / "schema.json"
        tables = json.loads(Path(pipeline.SCHEMA_LIVE).read_text())
        schema.write_text(json.dumps(tables))
        self.assertEqual(coltypes.load(schema)["linear.linear_issues"]["title"]["max_length"], 500)
        parse_back._schema(schema)
        for t in tables:
            if t["table_name"] == "linear_issues":
                for c in t["columns"]:
                    if c["column"] == "title":
                        c["max_length"] = 100
                t["columns"] = [c for c in t["columns"] if c["column"] != "estimate"]
        changed = json.dumps(tables)
        schema.write_text(changed)
        self.assertEqual(coltypes.load(schema)["linear.linear_issues"]["title"]["max_length"], 100)
        self.assertNotIn("estimate", parse_back._schema(schema).tables["linear.linear_issues"][1])
        schema.write_text(json.dumps(json.loads(Path(pipeline.SCHEMA_LIVE).read_text())))   # back to the original
        self.assertIn("estimate", parse_back._schema(schema).tables["linear.linear_issues"][1])
        self.assertEqual(coltypes.load(schema)["linear.linear_issues"]["title"]["max_length"], 500)

    def test_eval_parser_reloads_a_changed_tokenizer(self):
        from generators.validate import parse_back
        src = parse_back.DEFAULT_EVALS_TOOLS
        for name in ("hg_injection_lint.py", "hg_universe.py"):
            (self.dir / name).write_bytes((src / name).read_bytes())
        first = parse_back.load_eval_parser(self.dir)
        with open(self.dir / "hg_injection_lint.py", "a") as fh:
            fh.write("\n# changed\n")
        second = parse_back.load_eval_parser(self.dir)
        self.assertIsNot(first, second)
        self.assertNotEqual(first.pins["hg_injection_lint.py"], second.pins["hg_injection_lint.py"])
        self.assertFalse(list(self.dir.glob("__pycache__")))


class ValueFormTest(unittest.TestCase):
    def test_keys_of_another_form_refused(self):
        for obj, pattern in (
                ({"origin": "authored", "construction": "literal", "value": 1, "ref": "X"}, "do not belong"),
                ({"origin": "authored", "construction": "literal", "value": 1, "fn": "a/1"}, "do not belong"),
                ({"origin": "authored", "construction": "reference", "ref": "X", "value": 1}, "do not belong"),
                ({"origin": "base", "construction": "reference", "ref": "X",
                  "base": {"service": "linear", "collection": "issues", "record": "E-1", "field": "/id"}},
                 "do not belong"),
                ({"origin": "authored", "construction": "transform", "fn": "a/1", "text": "texts/a.txt"},
                 "do not belong")):
            with self.subTest(obj=obj), self.assertRaisesRegex(SpecError, pattern):
                parse_value("w", obj)


if __name__ == "__main__":
    unittest.main()
