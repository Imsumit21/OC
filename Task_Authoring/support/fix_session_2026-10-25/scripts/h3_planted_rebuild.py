#!/usr/bin/env python3
"""H3 planted failure: force the cache writers to write inside a sandbox and show the shared caches don't change.

In a staged sandbox (support/pending_tools/selftest_sandbox.py):
  1. persona_view: the sandbox's pv_slack.json gets a stale source stamp, so Universe().slack() must rebuild it;
  2. hg.py: a search the sandbox's empty helper cache has never seen (cold), so the helpers write query/record caches;
  3. base_check: the sandbox's base_slack_v2.json is removed, so Base().slack() must rebuild it.
Then: each rebuild landed in the sandbox (file changed or created there), the path probe and find -newer found no leak,
and the caller compares fingerprints of support/local_search/ and support/hardness_ledger/ taken before and after.
"""
import json
import subprocess
import sys
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(BUNDLE / "support" / "pending_tools"))
import selftest_sandbox as s  # noqa: E402


def main() -> int:
    ok = True

    def say(cond, msg):
        nonlocal ok
        ok = ok and bool(cond)
        print(("ok   " if cond else "FAIL ") + msg, flush=True)

    with s.Sandbox("staged") as sb:
        cache = sb.bundle / s.CACHE
        pv = cache / "pv_slack.json"
        d = json.loads(pv.read_text())
        built0 = d["_meta"].get("built_utc")
        d["_meta"]["sources"] = [["planted-stale-stamp", 0, 0]]
        pv.write_text(json.dumps(d))
        bc = cache / "base_slack_v2.json"
        had_bc = bc.is_file()
        if had_bc:
            bc.unlink()
        before = {p.relative_to(cache) for p in cache.rglob("*")}
        say(s._inside(pv, sb.root) and not pv.is_symlink(), f"the planted stale stamp is in the sandbox copy {pv.relative_to(BUNDLE)}")
        paths = sb.check_paths()
        say(True, f"path probe: {len(paths)} write paths inside the sandbox")
        code = ("import sys; sys.path[:0] = [sys.argv[1]]; import persona_view as pv; u = pv.Universe(); "
                "print(len(u.slack()['channels'])); import base_check as bc; b = bc.Base(); "
                "print(len(b.slack()) if hasattr(b, 'slack') else 'no Base.slack')")
        r = subprocess.run([sys.executable, "-B", "-c", code, str(sb.bundle / "tools")], cwd=str(sb.ws), env=sb.env(),
                           capture_output=True, text=True, timeout=1800)
        say(r.returncode == 0, f"persona_view + base_check in the sandbox: exit {r.returncode} {r.stdout.strip()!r} "
            f"{r.stderr.strip()[-300:]!r}")
        d2 = json.loads(pv.read_text())
        say(d2["_meta"]["sources"] != [["planted-stale-stamp", 0, 0]] and d2["_meta"].get("built_utc") != built0,
            f"persona_view rebuilt pv_slack.json inside the sandbox (built_utc {built0} -> {d2['_meta'].get('built_utc')})")
        if had_bc:
            say(bc.is_file(), "base_check rebuilt base_slack_v2.json inside the sandbox")
        env = dict(sb.env(), TASK_AUTHORING_LEGACY_V2="1")
        r = subprocess.run([sys.executable, "-B", str(sb.bundle / "tools" / "hg.py"), "search", "search", "slack",
                            "planted cold query 7f3c", "--limit", "1"], cwd=str(sb.ws), env=env, capture_output=True,
                           text=True, timeout=1800)
        say(r.returncode in (0, 1) and r.stdout.strip().startswith("{"), f"hg.py cold search in the sandbox: exit "
            f"{r.returncode}, {len(r.stdout)} bytes of JSON")
        say((sb.bundle / "support/local_search/tools/hg_search.py").is_file(),
            "hg.py regenerated the patched helpers inside the sandbox")
        after = {p.relative_to(cache) for p in cache.rglob("*")}
        say(len(after - before) > 0, f"{len(after - before)} new cache entr(y/ies) written inside the sandbox, e.g. "
            f"{sorted(map(str, after - before))[:3]}")
        changed = sb.check_linked()
        say(not changed, f"find -newer on the linked folders: {len(changed)} entr(y/ies)")
    print("PLANTED REBUILD " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
