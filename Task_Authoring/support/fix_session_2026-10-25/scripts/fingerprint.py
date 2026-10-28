#!/usr/bin/env python3
"""Fingerprint files under Task_Authoring/ (read-only on everything it walks).

Usage:
  python3 -B fingerprint.py OUT.tsv [--only REL ...]
  python3 -B fingerprint.py --diff A.tsv B.tsv [--only REL ...]

Columns: path (bundle-relative), kind (file|symlink), size, sha256 (or link target), mtime_ns.
Excluded (never walked): support/archive/ (read-only records, 5.7 GB), support/scratch/ (the self-test scratch
root) and support/fix_session_2026-10-25/ (this session's logs). --only limits the walk to the given bundle-relative
folders. Symlinked folders are recorded, never followed. --diff prints ADDED / REMOVED / CHANGED lines and a count.
"""
import hashlib
import os
import sys

BUNDLE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
EXCLUDE_REL = ("support/archive", "support/scratch", "support/fix_session_2026-10-25")
EXCLUDE = {os.path.join(BUNDLE, p) for p in EXCLUDE_REL}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def walk(roots):
    rows = []
    for top in roots:
        for root, dirs, files in os.walk(top, followlinks=False):
            keep = []
            for d in sorted(dirs):
                p = os.path.join(root, d)
                if p in EXCLUDE:
                    continue
                if os.path.islink(p):
                    st = os.lstat(p)
                    rows.append((os.path.relpath(p, BUNDLE), "symlink", st.st_size, os.readlink(p), st.st_mtime_ns))
                    continue
                keep.append(d)
            dirs[:] = keep
            for f in sorted(files):
                p = os.path.join(root, f)
                st = os.lstat(p)
                rel = os.path.relpath(p, BUNDLE)
                if os.path.islink(p):
                    rows.append((rel, "symlink", st.st_size, os.readlink(p), st.st_mtime_ns))
                else:
                    rows.append((rel, "file", st.st_size, sha256(p), st.st_mtime_ns))
    rows.sort()
    return rows


def load(path, only):
    out = {}
    with open(path) as fh:
        next(fh)
        for line in fh:
            p, kind, size, digest, mtime = line.rstrip("\n").split("\t")
            if only and not any(p == o or p.startswith(o.rstrip("/") + "/") for o in only):
                continue
            out[p] = (kind, size, digest, mtime)
    return out


def main(argv):
    only = []
    if "--only" in argv:
        i = argv.index("--only")
        only, argv = argv[i + 1:], argv[:i]
    if argv and argv[0] == "--diff":
        a, b = load(argv[1], only), load(argv[2], only)
        n = 0
        for p in sorted(set(a) | set(b)):
            if p not in a:
                print(f"ADDED\t{p}\t{b[p][1]}")
            elif p not in b:
                print(f"REMOVED\t{p}")
            elif a[p][:3] != b[p][:3]:
                print(f"CHANGED\t{p}\t{a[p][2][:12]} -> {b[p][2][:12]}")
            elif a[p][3] != b[p][3]:
                print(f"TOUCHED\t{p}\t(mtime only)")
            else:
                continue
            n += 1
        print(f"{n} difference(s) over {len(set(a) | set(b))} path(s)" + (f" under {only}" if only else ""))
        return 0 if n == 0 else 1
    assert os.path.basename(BUNDLE) == "Task_Authoring", BUNDLE
    roots = [os.path.join(BUNDLE, o) for o in only] if only else [BUNDLE]
    rows = walk(roots)
    with open(argv[0], "w") as fh:
        fh.write("path\tkind\tsize\tsha256\tmtime_ns\n")
        for r in rows:
            fh.write("\t".join(str(x) for x in r) + "\n")
    print(f"{len(rows)} entries -> {argv[0]} (excluded: {', '.join(EXCLUDE_REL)}"
          + (f"; only {only}" if only else "") + ")")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
