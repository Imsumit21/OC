#!/usr/bin/env python3
"""Rehearse the real move on a scratch copy of the bundle (never the live tree).

Copies the parts the move touches (tools/, references/, playbooks/, skills/, setup/, Guide/, README.md,
support/examples/, support/pending_edits/ without .rollback/, support/pending_tools/, support/hardness_ledger/) into
support/scratch/<tmp>/Task_Authoring/ and runs the copy's apply_pending.py there:
  A. check-only says ready; --apply killed (SIGKILL) mid-way; --check says partial; --resume finishes; every target
     equals its staged copy; the gate-policy hash equals the prediction from the staged files; write-priors makes
     references/mechanism_priors.json; --rollback restores everything: the edited originals (sha256 = base_sha256),
     the new files and mechanism_priors.json removed, pending_tools/ restored, the gate-policy hash back.
  B. --apply killed mid-way, then --rollback directly: the same checks.
Prints one line per check and removes the scratch copy.  Usage: python3 -B rehearse_move.py [--keep]
"""
import hashlib
import json
import os
import shutil
import signal
import subprocess
import sys
import tempfile
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[3]
PARTS = ["tools", "references", "playbooks", "skills", "setup", "Guide", "README.md", "support/examples",
         "support/pending_edits", "support/pending_tools", "support/hardness_ledger"]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None


def policy(tools):
    files = sorted(tools.glob("*.py"))
    return hashlib.sha256(b"".join(p.read_bytes() for p in files)).hexdigest()[:12], len(files)


def predicted_policy(b, m):
    """The post-move gate-policy hash: live tools/*.py with the staged tools/ files and the pending tools."""
    files = {p.name: p.read_bytes() for p in (b / "tools").glob("*.py")}
    for e in m["files"]:
        if e["target"].startswith("tools/") and e["target"].count("/") == 1 and e["target"].endswith(".py"):
            files[e["target"][6:]] = (b / "support/pending_edits" / e["staged"]).read_bytes()
    for t in m["tools"]:
        files[t] = (b / m["pending_tools"] / t).read_bytes()
    return hashlib.sha256(b"".join(files[k] for k in sorted(files))).hexdigest()[:12], len(files)


def run(b, *args, kill=None):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    env.pop("APPLY_PENDING_KILL_AT", None)
    if kill:
        env["APPLY_PENDING_KILL_AT"] = kill
    return subprocess.run([sys.executable, "-B", str(b / "support/pending_edits/apply_pending.py"), *args],
                          capture_output=True, text=True, env=env, timeout=600)


def copy_bundle(dst):
    for part in PARTS:
        src = BUNDLE / part
        if src.is_dir():
            shutil.copytree(src, dst / part, symlinks=True,
                            ignore=shutil.ignore_patterns(".rollback", "__pycache__"))
        else:
            (dst / part).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst / part)


def main(argv):
    scratch = BUNDLE / "support" / "scratch"
    scratch.mkdir(parents=True, exist_ok=True)
    root = Path(tempfile.mkdtemp(prefix="rehearse_move_", dir=scratch))
    ok = True

    def say(cond, msg):
        nonlocal ok
        ok = ok and bool(cond)
        print(("ok   " if cond else "FAIL ") + msg)

    try:
        for scenario in ("A", "B"):
            b = root / scenario / "Task_Authoring"
            copy_bundle(b)
            m = json.loads((b / "support/pending_edits/MANIFEST.json").read_text())
            edited = [e for e in m["files"] if e["base_sha256"]]
            new = [e for e in m["files"] if not e["base_sha256"]]
            pol0 = policy(b / "tools")
            pred = predicted_policy(b, m)
            pend0 = {t: sha(b / m["pending_tools"] / t) for t in m["tools"]}
            print(f"--- scenario {scenario}: {len(edited)} edited, {len(new)} new, {len(m['tools'])} tools; policy "
                  f"before {pol0[0]} ({pol0[1]} files), predicted after {pred[0]} ({pred[1]} files)")
            r = run(b)
            say(r.returncode == 0 and r.stdout.startswith("ready:"), f"check-only: {r.stdout.strip()}")
            mid = len(edited) + 3
            r = run(b, "--apply", kill=f"step:{mid}:after")
            say(r.returncode == -signal.SIGKILL, f"--apply killed at step {mid} (returncode {r.returncode})")
            r = run(b)
            say(r.returncode == 3, f"check after the kill: {r.stdout.strip()}")
            if scenario == "A":
                r = run(b, "--resume")
                say(r.returncode == 0, "--resume: " + r.stdout.strip().splitlines()[0][:150])
                staged_ok = all(sha(b / e["target"]) == sha(b / "support/pending_edits" / e["staged"]) for e in m["files"])
                tools_ok = all(sha(b / "tools" / t) == pend0[t] for t in m["tools"])
                gone = not any((b / m["pending_tools"] / t).exists() for t in m["tools"])
                say(staged_ok and tools_ok and gone, f"after resume: {len(m['files'])} targets = staged, "
                    f"{len(m['tools'])} tools in tools/, pending_tools emptied")
                pol1 = policy(b / "tools")
                say(pol1 == pred, f"policy after the move {pol1[0]} ({pol1[1]} files) = predicted {pred[0]}")
                r = subprocess.run([sys.executable, "-B", str(b / "tools/hardness_ledger.py"), "write-priors",
                                    str(b / "references/mechanism_priors.json"), "--model", "claude-opus-4-8"],
                                   capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"),
                                   timeout=600)
                say(r.returncode == 0 and (b / "references/mechanism_priors.json").is_file(),
                    f"write-priors (copy): exit {r.returncode}, {r.stdout.strip()[:120]}")
                r = run(b)
                say(r.returncode == 0 and "already applied" in r.stdout, f"check: {r.stdout.strip()[:120]}")
            r = run(b, "--rollback")
            say(r.returncode == 0, "--rollback: " + (r.stdout.strip() or r.stderr.strip())[:200])
            say(all(sha(b / e["target"]) == e["base_sha256"] for e in edited), f"{len(edited)} originals restored "
                "(sha256 = base_sha256)")
            say(not any((b / e["target"]).exists() for e in new), f"{len(new)} new files removed")
            say(not (b / "references/mechanism_priors.json").exists(), "references/mechanism_priors.json removed")
            say(all(sha(b / m["pending_tools"] / t) == pend0[t] for t in m["tools"]),
                f"{len(m['tools'])} pending tools restored")
            say(not any((b / "tools" / t).exists() for t in m["tools"]), "no pending tool left in tools/")
            pol2 = policy(b / "tools")
            say(pol2 == pol0, f"policy after rollback {pol2[0]} ({pol2[1]} files) = before {pol0[0]}")
            say(not list(b.rglob("*.apply_pending.tmp")), "no temp file left")
            r = run(b)
            say(r.returncode == 0 and r.stdout.startswith("ready:"), f"check after rollback: {r.stdout.strip()}")
    finally:
        if "--keep" not in argv:
            shutil.rmtree(root, ignore_errors=True)
    print("REHEARSAL " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
