#!/usr/bin/env python3
"""Falsification of the P0 fixes: undo one fix at a time in a copy of the tool inside a staged-layout sandbox
(support/pending_tools/selftest_sandbox.py; leak-checked) and run that tool's self-test, which must now FAIL.
Then the unmodified copy must PASS. Real files are never changed.  Usage: python3 -B falsify_p0.py [--only NAME]
"""
import subprocess
import sys
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(BUNDLE / "support" / "pending_tools"))
import selftest_sandbox as s  # noqa: E402

# (name, file in the sandbox bundle, old text, new text that undoes the fix, the self-test to run)
CASES = [
    ("B1 rollback keeps new targets", "support/pending_edits/apply_pending.py",
     "            if s[\"original\"] is None:\n                if target.exists():\n                    target.unlink()",
     "            if s[\"original\"] is None:\n                pass", "apply_pending"),
    ("B1 check misses 'already applied'", "support/pending_edits/apply_pending.py",
     "            if j.has(\"applied\"):\n                changed",
     "            if False:\n                changed", "apply_pending"),
    ("B1 no backup before writing", "support/pending_edits/apply_pending.py",
     "                shutil.copy2(live, dst)\n                if sha(dst) != s[\"original\"]:",
     "                if False:", "apply_pending"),
    ("B2 one candidate binds (old SINGLE/any-hit)", "tools/trajectory_ledger.py",
     "        else:\n            verdict = \"INSUFFICIENT\"\n    elif len(hits) == 1:",
     "        else:\n            verdict, basis, bound = \"BOUND\", \"discriminating content\", out[0][\"labels\"]\n"
     "    elif len(hits) == 1:", "trajectory_ledger"),
    ("B2 proposals take the first run's revision", "tools/node_verdicts.py",
     "\"revision\": b[\"revision\"], \"sql_sha256\": b[\"sql_sha256\"],",
     "\"revision\": next(iter(report[\"runs\"].values()))[\"binding\"][\"revision\"], "
     "\"sql_sha256\": next(iter(report[\"runs\"].values()))[\"binding\"][\"sql_sha256\"],", "node_verdicts"),
    ("B2 unbound run falls back to the first SQL", "tools/node_verdicts.py",
     "        ok_, why = tl.binding_ok(b)\n        if not ok_:",
     "        ok_, why = tl.binding_ok(b)\n        b = dict(b, verdict=\"BOUND\", basis=\"discriminating content\", "
     "bound_to=b.get(\"bound_to\") or [sqls[0][0]], evidence={\"discriminating_seen\": 1})\n        if False:",
     "node_verdicts"),
    ("H3 linked-folder writes unchecked", "tools/selftest_sandbox.py",
     "        changed = self.check_linked()\n        if changed:",
     "        changed = []\n        if changed:", "selftest_sandbox"),
    ("H3 write paths unchecked", "tools/selftest_sandbox.py",
     "        outside = {k: str(Path(v).resolve()) for k, v in paths.items() if not _inside(Path(v), self.root)}",
     "        outside = {}", "selftest_sandbox"),
    ("D3 surface.coverage a no-op", "tools/stage_gate.py",
     "    ok = not bad and not unknown\n    ctx.add(\"surface.coverage\", ok,",
     "    ok = True\n    ctx.add(\"surface.coverage\", ok,", "stage_gate"),
    ("D5 rule placement on every legacy node", "tools/trap_liveness.py",
     "    return {\"nodes\": nodes | own, \"source\": src, \"why\": why}",
     "    return {\"nodes\": (nodes | own) or {t.get(\"id\") for t in manifest.get(\"traps\") or []}, "
     "\"source\": src, \"why\": why}", "trap_liveness"),
    ("D6 duplicates.fact not checked", "tools/gradable_surface.py",
     "        if len(members) >= 3:", "        if len(members) >= 99:", "gradable_surface"),
    ("D6 gate blocks on structure only (the old deviation 6)", "tools/stage_gate.py",
     "    fails = [f for f in r[\"findings\"] if f[\"severity\"] == \"FAIL\"]\n    rep = r[\"report\"]",
     "    fails = [f for f in r[\"findings\"] if f[\"severity\"] == \"FAIL\" and f[\"check\"].split(\".\")[0] in "
     "(\"structure\", \"weights\")]\n    rep = r[\"report\"]", "stage_gate"),
    ("MK --max-k above 8 without the override", "tools/difficulty_mutation.py",
     "    if allow is not None and int(allow) == k:", "    if True:", "difficulty_mutation"),
]


def run_selftest(sb, tool):
    if tool == "apply_pending":
        r = subprocess.run([sys.executable, "-B", str(sb.bundle / "support/pending_edits/apply_pending.py"),
                            "--self-test"], cwd=str(sb.ws), env=sb.env(), capture_output=True, text=True, timeout=1200)
        changed = sb.check_linked()
        if changed:
            raise s.Leak(f"linked folders changed: {changed[:3]}")
        return r.returncode, (r.stdout + r.stderr).strip().splitlines()
    rc = sb.run([f"{tool}.py", "--self-test"], quiet=True)
    return rc, (sb.last["stdout"] + sb.last["stderr"]).strip().splitlines()


def main(argv):
    only = argv[argv.index("--only") + 1] if "--only" in argv else None
    ok = True
    with s.Sandbox("staged") as sb:
        pe = sb.bundle / "support" / "pending_edits"
        pe.mkdir(parents=True, exist_ok=True)
        (pe / "apply_pending.py").write_text((BUNDLE / "support/pending_edits/apply_pending.py").read_text())
        print(f"sandbox {sb.root.relative_to(BUNDLE)} (staged layout)", flush=True)
        for name, rel, old, new, tool in CASES:
            if only and only not in name:
                continue
            f = sb.bundle / rel
            orig = f.read_text()
            if orig.count(old) != 1:
                print(f"SKIP {name}: anchor found {orig.count(old)} time(s) in {rel}")
                ok = False
                continue
            f.write_text(orig.replace(old, new))
            rc, out = run_selftest(sb, tool)
            f.write_text(orig)
            caught = rc != 0
            ok = ok and caught
            tail = next((ln for ln in reversed(out) if "Error" in ln or "FAIL" in ln), out[-1] if out else "")
            print(f"{'ok  ' if caught else 'MISS'} {name}: {tool} --self-test exit {rc} -> {tail.strip()[:170]}",
                  flush=True)
        for tool in sorted({c[4] for c in CASES if not only or only in c[0]}):
            rc, out = run_selftest(sb, tool)
            ok = ok and rc == 0
            print(f"{'ok  ' if rc == 0 else 'FAIL'} control: unmodified {tool} --self-test exit {rc}", flush=True)
    print("FALSIFICATION " + ("PASS (every undone fix is caught)" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
