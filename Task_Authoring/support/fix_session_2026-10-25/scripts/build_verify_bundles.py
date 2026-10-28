#!/usr/bin/env python3
"""Assemble the artifacts for the independent verification of P1 (AGENTS.md: verify tiers code, redteam, methodology).

Each bundle = context + the row specs it covers (quoted from plans/Learnings_And_Improvements_2026-10-25.md §4.2) +
the exact diffs (logs/verify/*.diff, built by build_verify_diffs.py against hash-verified post-move baselines) + the
raw test and acceptance outputs. Read-only on the bundle; writes logs/verify/bundle_<name>.txt.

Usage (workspace root): python3 -B Task_Authoring/support/fix_session_2026-10-25/scripts/build_verify_bundles.py [NAME ...]
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
BUNDLE = SESSION.parents[1]
LOGS = SESSION / "logs"
OUT = LOGS / "verify"
LEARN = BUNDLE / "plans" / "Learnings_And_Improvements_2026-10-25.md"

CONTEXT = """CONTEXT
- Project: Task_Authoring, Python 3 stdlib-only tools that author and check HarmonyGames benchmark tasks (V3: six
  Opus 5.5 runs per task; four difficulty gates on a rubric x run matrix). The tools grade platform trajectories against
  a "gradable surface" (a proxy grader), attribute register errors to designed mechanisms (node_verdicts), keep a
  cross-task evidence ledger (Beta priors per mechanism family), and forecast the six-run gates (hardness_forecast).
- P1 is a set of fixes ("rows"), specified below (quoted from plans/Learnings_And_Improvements_2026-10-25.md §4.2) with
  the user's decisions. Hard rules: stdlib only; SQL is parsed as data, never executed; the frozen backtest copies
  (support/backtests/season_pass/rev13, rev14) are read-only; every self-test temp folder is under support/scratch/;
  self-tests must not write the shared caches (support/local_search, support/hardness_ledger): they run in a sandbox
  workspace (tools/selftest_sandbox.py); every new test plants the failure it guards against.
- The diffs are exact: each file against its post-move content (sha256 verified against the post-move fingerprint),
  i.e. the whole P1 change of that file. "(added in P1)" files are new.
- "Falsification" scripts undo each fix in memory (monkeypatching the old behaviour back) and show that the self-test
  planting it fails; a control run (nothing undone) passes.
"""

DECISIONS = {
    "V1": """USER DECISIONS (V1): the default expected model comes from the task context (baseline_model, else the V3 policy model
claude-opus-5-5). Labels: strip only a bracketed suffix, then compare exactly. <synthetic> is excluded from the model
check but counted. An unrecognised label is UNKNOWN, never valid. mixed_model and v3_valid are separate outcomes. One
owner (difficulty_stats) shared by trajectory_ledger and the six-run model gate. Expected outcomes: default expected
model -> all five rev14 runs v3-invalid; --expected-model claude-opus-4-8 -> pre, r1, r2, r6 mixed, r3 unmixed; a
synthetic Opus 5.5 run is v3-valid.""",
    "UNGRADED": """USER DECISION (UNGRADED, G1): average and full-pass verdicts only when both bounds agree (every UNGRADED cell failed /
passed), else INCOMPLETE; SD band and failure patterns: enumerate the completions when few enough, a verdict only when
all agree, else INCOMPLETE; always list the UNGRADED cells; no unknown -> false conversion.""",
    "H1": """USER DECISIONS (H1 control records, complexity channels): when the solver declares a rule's control members and an
over-application degrade, an error on a control member whose value matches the degrade is a control trial (OVER-APPLIED,
else HELD), with its deciding event and model, beside the rule's verdict on its scope; it never counts as a landing for
the go rule or the priors. node_verdicts reports each declared complexity channel per run (failed or held, deciding
event and model). The go rule counts designed mechanisms that LANDED and pre-registered channels that FAILED in the
expected model's own decisions; control errors and unattributed slips count for neither.""",
    "H2": """USER DECISION (H2): Kish design effect, rho = 0.5 (labelled an assumption, overridable); cluster = the task (all
revisions together); n_eff per task beside each prior; one trial per (task, revision, run, family).""",
    "F1": """USER DECISIONS (F1 dependence): re-solve sampled member errors through the solver (not a formula), so a sampled
member fails at about e, aggregates compound, and opposing count errors can cancel; shared causes are latents from the
solver's rule->member, batch and run structure, plus independent slips; integrate over the uncertainty in e
(1 - E[(1 - e)^N], not the plug-in); report each slot's P(fail) and P(fails all six) (workload, never a block). Fixtures:
e = 0.02 over 40 members: independent ~0.554, fully linked 0.02; a count slot with one false inclusion and one false
exclusion passes while the affected samples fail; a cause shared across slots gives fewer failure patterns.""",
    "E2E": """USER DECISION (E2E): one command runs the five rev14 runs through trajectory_ledger -> node_verdicts ->
surface_grader -> a temp hardness_ledger -> hardness_forecast inside the sandbox. Assert: the failed-slot sets of record;
r3's S43/S44 and S69-S71 pass; the pre-check is v3-invalid and mixed with 0 designed landings, and SP-110 is a control
record for M2 from an Opus 5 brief (a fixture wrapper declares it if the frozen solver can't; never edit the snapshot).""",
    "WT": """USER DECISION (WT): tests/test_v3_stage_gate.py and difficulty_stats' self-test put their temp folders under the
scratch root, even outside the sandbox; neither is run before the fix.""",
}

GROUPS = {
    "code_g1": dict(rows=["G1"], decisions=["UNGRADED"],
                    diffs=["tools/surface_grader.py", "tools/gradable_surface.py", "tools/trajectory_ledger.py",
                           "support/fixtures/surface_formats/build_fixtures.py",
                           "support/fixtures/surface_formats/README.md"],
                    logs=["final4/rev13_truth.txt", "final4/rev13_solver.txt", "final4/rev14_grades.txt",
                          "final4/build_fixtures_check.txt", "g1/falsify_g1.round16.txt", "p1_suite_round16.log",
                          "e2e/e2e_round22.log"],
                    extra=[("support/backtests/season_pass/rev14/README.md", 27, 43)]),
    "code_h1": dict(rows=["H1", "H2", "E2E"], decisions=["H1", "H2"],
                    diffs=["tools/node_verdicts.py", "tools/hardness_ledger.py"],
                    logs=["final4/c05.txt", "h1/falsify_h1.round39.txt", "h2_round2_rho0.5.txt",
                          "h2_round2_A17_exclude_season_pass.txt", "p1_suite_round16.log", "e2e/e2e_round22.log"],
                    files=["references/mechanism_priors.json"],
                    notes=["### H1 (node_verdicts)", "### E2E ("]),
    "code_f1": dict(rows=["F1", "M6", "M2", "H2"], decisions=["F1", "H2"],
                    diffs=["tools/hardness_forecast.py", "tools/difficulty_mutation.py", "tools/preflight_report.py",
                           "tools/hardness_gate.py"],
                    logs=["p1_suite_round16.log", "h1/falsify_h1.round39.txt", "f1/f1_protocol4_summary.txt",
                          "f1/protocol4_seed1.out", "f1/protocol4_seed2.out", "f1/protocol4_seed3.out",
                          "e2e/e2e_round22.log"],
                    files=["references/mechanism_priors.json",
                           "support/fix_session_2026-10-25/scripts/f1_protocol.py",
                           "support/fix_session_2026-10-25/scripts/f1_audited_ledger.py"]),
    "code_misc": dict(rows=["V1", "M5", "M7", "WT", "E2E"], decisions=["V1", "WT", "E2E"],
                      diffs=["tools/difficulty_stats.py", "tools/stage_gate.py", "tools/test_difficulty_v3.py",
                             "tests/test_v3_stage_gate.py", "support/examples/calibration/stage_gate/bad/cases.json",
                             "tools/oracle_kit.py", "tools/selftest_sandbox.py", "tools/gradable_surface.py",
                             "tools/surface_grader.py",
                             "support/fixtures/season_pass_rev14/solver.py",
                             "support/fixtures/season_pass_rev14/e2e_rev14.py"],
                      logs=["final4/v1_acceptance.txt", "tests_round4.txt", "p1_suite_round16.log",
                            "e2e/e2e_round22.log", "h1/falsify_h1.round39.txt", "final4/task1_surface_gradeable.txt"],
                      notes=["### Incident (shared cache)"]),
    "redteam_grading": dict(rows=["G1"], decisions=["UNGRADED"],
                            diffs=["tools/surface_grader.py", "tools/gradable_surface.py"],
                            logs=["final4/rev13_truth.txt", "final4/rev14_grades.txt", "g1/falsify_g1.round16.txt",
                                  "final4/build_fixtures_check.txt", "e2e/e2e_round22.log"],
                            extra=[("support/backtests/season_pass/rev14/README.md", 27, 43)]),
    "redteam_attribution": dict(rows=["H1", "H2"], decisions=["H1", "H2"],
                                diffs=["tools/node_verdicts.py", "tools/hardness_ledger.py"],
                                logs=["final4/c05.txt", "h1/falsify_h1.round39.txt",
                                      "h2_round2_rho0.5.txt", "e2e/e2e_round22.log"],
                                files=["references/mechanism_priors.json"],
                                notes=["### H1 (node_verdicts)"]),
    "redteam_forecast": dict(rows=["F1", "M6"], decisions=["F1"],
                             diffs=["tools/hardness_forecast.py", "tools/difficulty_mutation.py"],
                             logs=["f1/f1_protocol4_summary.txt", "f1/protocol4_seed1.out", "f1/protocol4_seed2.out",
                                   "f1/protocol4_seed3.out", "h1/falsify_h1.round39.txt", "p1_suite_round16.log",
                                   "e2e/e2e_round22.log"],
                             files=["support/fix_session_2026-10-25/scripts/f1_acceptance.py",
                                    "support/fix_session_2026-10-25/scripts/f1_protocol.py",
                                    "support/fix_session_2026-10-25/scripts/f1_audited_ledger.py",
                                    "support/fix_session_2026-10-25/f1_acceptance/summary.json",
                                    "support/fix_session_2026-10-25/f1_acceptance/F1_AUDITED_LEDGER.jsonl",
                                    "support/fix_session_2026-10-25/logs/verify/claims_methodology.md"]),
    "methodology": dict(rows=["F1", "M6", "H2"], decisions=["F1", "H2"],
                        diffs=["tools/hardness_forecast.py"],
                        logs=["h2_round2_rho0.txt", "h2_round2_rho0.5.txt", "h2_round2_rho1.txt",
                              "h2_round2_A17_exclude_season_pass.txt", "f1/f1_protocol4_summary.txt",
                              "f1/protocol4_seed1.out", "f1/protocol4_seed2.out", "f1/protocol4_seed3.out",
                              "p1_suite_round16.log", "final4/c05.txt"],
                        files=["support/fix_session_2026-10-25/scripts/f1_acceptance.py",
                               "support/fix_session_2026-10-25/scripts/f1_protocol.py",
                               "support/fix_session_2026-10-25/scripts/f1_audited_ledger.py",
                               "support/fix_session_2026-10-25/logs/verify/claims_methodology.md",
                               "support/fix_session_2026-10-25/f1_acceptance/F1_STATUS.md",
                               "support/fix_session_2026-10-25/f1_acceptance/F1_ACCEPTANCE_AMENDMENT.md",
                               "support/fix_session_2026-10-25/f1_acceptance/F1_PROTOCOL_MANIFEST.json",
                               "support/fix_session_2026-10-25/f1_acceptance/F1_PROVENANCE_AUDIT.txt",
                               "support/fix_session_2026-10-25/f1_acceptance/summary.json",
                               "references/mechanism_priors.json"],
                        extra=[("support/backtests/season_pass/rev14/working_files/rev14_platform_runs/"
                                "Rev14_Precheck_Findings.md", 109, 124)]),
}


def rows(ids) -> str:
    lines = LEARN.read_text().splitlines()
    return "\n".join(line for line in lines if any(line.startswith(f"| {r} |") for r in ids))


def notes(headings) -> str:
    text = (SESSION / "NOTES.md").read_text().split("\n### ")
    return "\n".join("### " + part for part in text if any(("### " + part).startswith(h) for h in headings))


def build(name: str, g: dict) -> Path:
    parts = [CONTEXT, f"ROW SPECS ({', '.join(g['rows'])})\n" + rows(g["rows"])]
    parts += [DECISIONS[d] for d in g.get("decisions", [])]
    for rel in g["diffs"]:
        d = OUT / (rel.replace("/", "__") + ".diff")
        parts.append(f"===== DIFF {rel} =====\n" + d.read_text())
    for rel in g.get("files", []):
        parts.append(f"===== FILE {rel} =====\n" + (BUNDLE / rel).read_text())
    for rel in g["logs"]:
        p = LOGS / rel
        parts.append(f"===== OUTPUT logs/{rel} =====\n" + (p.read_text() if p.is_file() else "(missing)"))
    for rel, a, b in g.get("extra", []):
        parts.append(f"===== EXCERPT {rel}:{a}-{b} =====\n" + "\n".join((BUNDLE / rel).read_text().splitlines()[a - 1:b]))
    if g.get("notes"):
        parts.append("===== SESSION NOTES (excerpt) =====\n" + notes(g["notes"]))
    out = OUT / f"bundle_{name}.txt"
    out.write_text("\n\n".join(parts) + "\n")
    return out


def main(argv) -> int:
    for name in argv or list(GROUPS):
        p = build(name, GROUPS[name])
        print(f"{p.name}: {p.stat().st_size // 1024} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
