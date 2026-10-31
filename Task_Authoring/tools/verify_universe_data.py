#!/usr/bin/env python3
"""verify_universe_data.py - check installed universe data against its shipped manifests (read-only).

  python3 -B Task_Authoring/tools/verify_universe_data.py                       # both universes: presence + sizes
  python3 -B Task_Authoring/tools/verify_universe_data.py --universe synthcut   # one universe
  python3 -B Task_Authoring/tools/verify_universe_data.py --sha256              # also hash every file (slow)
  python3 -B Task_Authoring/tools/verify_universe_data.py --self-test

Each universe's routing manifest (Evals/references/universes/<key>/universe_manifest.json) names
its service folders and pins each export's file count, total bytes and archive (entry + SHA-256);
each folder's source_manifest.json lists every exported file with its size and SHA-256. A service is
OK when its source manifest agrees with those pins, every listed file is at its path with that size
(and hash, with --sha256) and nothing unlisted is present. Names compare in Unicode NFC (macOS may store decomposed
names); two spellings of one name are reported, never merged. Only regular files count: a symlink, a
directory (or a link to one) or other special file at a listed path is a problem. Finder metadata (.DS_Store, ._*) is ignored unless
the export lists it. A full run walks ~700k files (a few minutes). Split extractions ("<folder> 2"),
base folders left outside their Universe_* folder and doubly nested base folders are reported.
Exit 0 when every checked service is OK, 1 when anything is wrong.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import sys
import tempfile
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from task_context import WORKSPACE, ContextError, _universe_module  # noqa: E402

SAMPLE = 3          # example paths shown per problem kind
PROBLEM_KINDS = ("missing", "extra", "size_mismatch", "hash_mismatch", "not_regular_file", "name_collision",
                 "routing_manifest_mismatch")
PINNED = ("file_count", "total_bytes", "source", "archive_entry")   # routing-manifest fields a source manifest must match


def _nfc(text: str) -> str:
    return unicodedata.normalize("NFC", text)


def _ignored(name: str) -> bool:
    return name == ".DS_Store" or name.startswith("._")


def _sha256(path: Path) -> str | None:
    """SHA-256 of a regular file, never through a link (None when it cannot be opened that way)."""
    digest = hashlib.sha256()
    try:
        fd = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
    except OSError:
        return None
    with os.fdopen(fd, "rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _listing(folder: Path, walk=os.walk):
    """(path as spelled on disk, Path, is_directory_entry) for every entry os.walk lists: files, and directory entries
    (real directories and links to directories, never followed), so that one standing at a listed path is reported
    and takes part in the NFC collision check."""
    for root, dirs, names in walk(folder):
        for name in names:
            full = Path(root) / name
            yield full.relative_to(folder).as_posix(), full, False
        for name in dirs:
            full = Path(root) / name
            yield full.relative_to(folder).as_posix(), full, True


def check_service(folder: Path, sha256: bool = False, listing=None, pinned=None) -> dict:
    """Compare one service folder with its source_manifest.json.

    Two spellings that normalize to one NFC name (on disk or in the manifest) are reported, never merged, so a
    second copy cannot hide behind the first. Sizes and hashes are read only from regular files: a symlink
    (dangling or not) or other special file at a listed path is reported instead. `pinned` is the service's entry
    in the Evals routing manifest: the source manifest (shipped inside the data) must agree with its file count,
    total bytes, archive identity (sha256) and archive entry, which ties the per-file hashes to the bundle."""
    manifest = folder / "source_manifest.json"
    if not manifest.is_file():
        return {"ok": False, "problem": f"{'source_manifest.json' if folder.is_dir() else 'folder'} missing"}
    try:
        data = json.loads(manifest.read_text())
        files = data["files"]
        for f in files:
            if not (isinstance(f["path"], str) and isinstance(f["sha256"], str)
                    and isinstance(f["bytes"], int) and not isinstance(f["bytes"], bool)):
                raise TypeError(f"entry {f!r} needs a string path, an integer bytes and a string sha256")
        declared = {"file_count": len(files), "total_bytes": sum(f["bytes"] for f in files),
                    "source": data.get("source"), "archive_entry": data.get("archive_entry")}
        keys = [_nfc(f["path"]) for f in files]
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        return {"ok": False, "problem": f"source_manifest.json is malformed ({type(exc).__name__}: {str(exc)[:200]})"}
    disagree = [f"{field}: source manifest {declared[field]!r} vs routing manifest {pinned[field]!r}"
                for field in PINNED if pinned and field in pinned and declared[field] != pinned[field]]
    if pinned and "file_count" in pinned and data.get("file_count") not in (None, len(files)):
        disagree.append(f"file_count field {data['file_count']!r} vs {len(files)} listed files")
    want, collisions = {}, []
    for entry, key in zip(files, keys):
        if key in want:
            collisions.append(f"manifest lists {key} twice")
        want[key] = entry
    have, spelled, irregular = {}, {}, set()
    for item in (_listing(folder) if listing is None else listing):
        raw, full, is_dir = (tuple(item) + (False,))[:3]
        rel = _nfc(raw)
        # Unlisted directories are only traversal; Finder metadata counts only when the export itself lists it.
        if rel == "source_manifest.json" or (rel not in want and (is_dir or _ignored(full.name))):
            continue
        if rel in have:
            collisions.append(f"{spelled[rel]!r} and {raw!r} are one name after NFC")
            continue
        have[rel], spelled[rel] = full, raw
        if is_dir or not stat.S_ISREG(full.lstat().st_mode):
            irregular.add(rel)
    regular = (set(want) & set(have)) - irregular
    size = sorted(r for r in regular if have[r].lstat().st_size != want[r]["bytes"])
    hashes = sorted(r for r in regular - set(size) if _sha256(have[r]) != want[r]["sha256"]) if sha256 else []
    result = {"expected": len(want), "found": len(have), "missing": sorted(set(want) - set(have)),
              "extra": sorted(set(have) - set(want)), "size_mismatch": size, "hash_mismatch": hashes,
              "not_regular_file": sorted(irregular), "name_collision": collisions,
              "routing_manifest_mismatch": disagree}
    result["ok"] = not any(result[k] for k in PROBLEM_KINDS)
    return result


def layout_problems(workspace: Path, entry: dict, bases: set[str]) -> list[str]:
    """Split, misplaced or doubly nested base folders of one universe."""
    problems = []
    folder, prefix = entry["folder"], entry["prefix"] + "_HarmonyGames_"
    for parent in (workspace, workspace / folder):
        if not parent.is_dir():
            continue
        for child in sorted(p for p in parent.iterdir() if p.is_dir() and p.name.startswith(prefix)):
            if re.search(r" \d+$", child.name):
                problems.append(f"{child.relative_to(workspace)}/ looks like a split extraction: merge it into "
                                f"{child.name.rsplit(' ', 1)[0]}/ or re-extract per Evals/UNIVERSE_MAP.md")
            elif parent == workspace:
                problems.append(f"{child.name}/ sits at the workspace root: move it to {folder}/{child.name}/")
    for base in sorted(bases):
        nested = workspace / base / Path(base).name
        if nested.is_dir():
            problems.append(f"{base}/ is doubly nested ({base}/{Path(base).name}/): move the inner folder up one level")
    return problems


def verify(workspace: Path, keys: list[str], sha256: bool = False, out=print) -> bool:
    module = _universe_module()
    all_ok = True
    for key in keys:
        entry = module.UNIVERSES[key]
        out(f"== {key}: {entry['label']} -> {entry['folder']}/")
        manifest_path = module.manifest_path(workspace, key)
        services = json.loads(manifest_path.read_text())["services"]
        bases = {"/".join(Path(s["path"]).parts[:2]) for s in services.values()}
        if not (workspace / entry["folder"]).is_dir():
            out(f"   PROBLEM  {entry['folder']}/ is not installed (see the root README and Evals/UNIVERSE_MAP.md)")
            all_ok = False
        for problem in layout_problems(workspace, entry, bases):
            out(f"   PROBLEM  {problem}")
            all_ok = False
        if not (workspace / entry["folder"]).is_dir():
            continue
        for name, service in sorted(services.items()):
            result = check_service(workspace / service["path"], sha256=sha256, pinned=service)
            all_ok &= result["ok"]
            if "problem" in result:
                out(f"   PROBLEM  {name:11} {service['path']}: {result['problem']}")
                continue
            line = f"   {'OK     ' if result['ok'] else 'PROBLEM'}  {name:11} expected={result['expected']:>7} found={result['found']:>7}"
            for kind in PROBLEM_KINDS:
                if result[kind]:
                    line += f" {kind}={len(result[kind])} (e.g. {', '.join(result[kind][:SAMPLE])})"
            out(line)
    out(f"{'ALL OK' if all_ok else 'PROBLEMS FOUND'} ({'presence, sizes and SHA-256' if sha256 else 'presence and sizes'}"
        f"; universes: {', '.join(keys)})")
    return all_ok


def _self_test() -> int:
    module = _universe_module()
    scratch = HERE.parent / "support" / "scratch"
    scratch.mkdir(parents=True, exist_ok=True)
    ws = Path(tempfile.mkdtemp(prefix="verify_universe_", dir=scratch))
    checks = 0

    def run(keys, sha=False):
        lines = []
        return verify(ws, keys, sha256=sha, out=lines.append), "\n".join(lines)

    try:
        entry = module.UNIVERSES["normal"]
        base = f"{entry['folder']}/{entry['prefix']}_HarmonyGames_Other_Services"
        decomposed = unicodedata.normalize("NFD", "Español.png")
        files = {"alpha": {"data.json": b"{}", decomposed: b"png"}, "beta": {"sub/x.txt": b"hello", "sub/.DS_Store": b"ds"}}
        services = {}
        for name, content in files.items():
            folder = ws / base / "Services_Data" / name
            listed = []
            for rel, data in content.items():
                (folder / rel).parent.mkdir(parents=True, exist_ok=True)
                (folder / rel).write_bytes(data)
                listed.append({"path": _nfc(rel), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
            archive = {"bytes": 10 + len(name), "sha256": hashlib.sha256(name.encode()).hexdigest()}
            (folder / "source_manifest.json").write_text(json.dumps({"source": archive, "files": listed}))
            services[name] = {"path": f"{base}/Services_Data/{name}", "file_count": len(listed),
                              "total_bytes": sum(f["bytes"] for f in listed), "source": archive}
        manifest = module.manifest_path(ws, "normal")
        manifest.parent.mkdir(parents=True)
        manifest.write_text(json.dumps({"universe": "normal", "services": services}))
        alpha = ws / base / "Services_Data" / "alpha"

        ok, text = run(["normal"])
        assert ok and "ALL OK" in text, text                            # decomposed name matches its NFC entry
        checks += 1
        # A source manifest from another export (other archive hash) fails against the routing-manifest pins,
        # even though every file it lists is present with its listed size.
        beta_manifest = ws / base / "Services_Data" / "beta" / "source_manifest.json"
        original = beta_manifest.read_text()
        beta_manifest.write_text(json.dumps(dict(json.loads(original), source={"bytes": 11, "sha256": "0" * 64})))
        ok, text = run(["normal"])
        assert not ok and "routing_manifest_mismatch=1" in text, text
        listed = json.loads(original)["files"]
        for broken in ([{"path": "sub/x.txt"}],                                     # no size or hash
                       [dict(listed[0], path=None)], [dict(listed[0], path=7)]):    # a null or numeric path
            beta_manifest.write_text(json.dumps({"files": broken}))
            ok, text = run(["normal"])
            assert not ok and "source_manifest.json is malformed" in text, text
            assert re.search(r"OK\s+alpha", text), text                          # the other service is still checked
        beta_manifest.write_text(original)
        checks += 4
        (alpha / ".DS_Store").write_bytes(b"x")
        ok, text = run(["normal"])
        assert ok, text                                                 # unlisted Finder metadata is ignored
        listed_ds = ws / base / "Services_Data" / "beta" / "sub" / ".DS_Store"
        listed_ds.unlink()
        ok, text = run(["normal"])
        assert not ok and "missing=1" in text and ".DS_Store" in text, text   # a listed one is required
        listed_ds.write_bytes(b"ds")
        checks += 2
        (alpha / "data.json").write_bytes(b"{} ")
        ok, text = run(["normal"])
        assert not ok and "size_mismatch=1" in text, text
        checks += 1
        (alpha / "data.json").write_bytes(b"[]")                        # same size, other content
        ok, text = run(["normal"])
        assert ok, text                                                 # sizes only without --sha256
        ok, text = run(["normal"], sha=True)
        assert not ok and "hash_mismatch=1" in text, text
        checks += 2
        (alpha / "data.json").write_bytes(b"{}")
        (alpha / "stray.json").write_bytes(b"1")
        (ws / base / "Services_Data" / "beta" / "sub" / "x.txt").unlink()
        ok, text = run(["normal"])
        assert not ok and "extra=1" in text and "missing=1" in text, text
        checks += 1
        (alpha / "stray.json").unlink()
        (ws / base / "Services_Data" / "beta" / "sub" / "x.txt").write_bytes(b"hello")
        # A listed file replaced by a link is never sized or hashed through it: dangling (link text "xy" has
        # the listed 2 bytes), then pointing at a same-content file outside the service folder.
        data = alpha / "data.json"
        data.unlink()
        data.symlink_to("xy")
        ok, text = run(["normal"], sha=True)
        assert not ok and "not_regular_file=1" in text, text
        data.unlink()
        (ws / "target.json").write_bytes(b"{}")
        data.symlink_to(ws / "target.json")
        ok, text = run(["normal"], sha=True)
        assert not ok and "not_regular_file=1" in text, text
        data.unlink()
        (ws / "target_dir").mkdir()
        data.symlink_to(ws / "target_dir", target_is_directory=True)    # os.walk lists it among the directories
        ok, text = run(["normal"], sha=True)
        assert not ok and "not_regular_file=1" in text and "missing=" not in text, text
        data.unlink()
        data.mkdir()                                                      # an empty real directory at the path
        ok, text = run(["normal"])
        assert not ok and "not_regular_file=1" in text and "missing=" not in text, text
        data.rmdir()
        data.write_bytes(b"{}")
        (ws / "target.json").unlink()
        (ws / "target_dir").rmdir()
        checks += 4
        # Two spellings of one name: the second copy (other bytes, same size) is reported, never merged away.
        # Listed explicitly, since a normalization-insensitive filesystem cannot hold both names at once.
        nfc_name = "Español.png"
        twin = ws / "twin.png"
        twin.write_bytes(b"bad")
        result = check_service(alpha, sha256=True, listing=[("data.json", data), (decomposed, alpha / decomposed),
                                                            (nfc_name, twin)])
        assert not result["ok"] and len(result["name_collision"]) == 1 and not result["hash_mismatch"], result
        twin.unlink()
        # The same through the real enumeration: a directory entry (here a link to a directory, as os.walk reports it)
        # at the NFC spelling beside the NFD regular copy is a collision, with and without hashing.
        walked = lambda folder: iter([(str(folder), [nfc_name], ["data.json", decomposed])])
        for sha in (False, True):
            result = check_service(alpha, sha256=sha, listing=_listing(alpha, walk=walked))
            assert not result["ok"] and len(result["name_collision"]) == 1, result
        dup = ws / "dup"
        dup.mkdir()
        (dup / nfc_name).write_bytes(b"png")
        entry_png = {"bytes": 3, "sha256": hashlib.sha256(b"png").hexdigest()}
        (dup / "source_manifest.json").write_text(json.dumps(
            {"files": [{"path": nfc_name, **entry_png}, {"path": decomposed, **entry_png}]}))
        result = check_service(dup)
        assert not result["ok"] and any("twice" in c for c in result["name_collision"]), result
        shutil.rmtree(dup)
        checks += 4
        (ws / f"{base} 2").mkdir()
        (ws / f"{entry['prefix']}_HarmonyGames_Gmail").mkdir()
        (ws / base / Path(base).name).mkdir()
        ok, text = run(["normal"])
        assert not ok and "split extraction" in text and "workspace root" in text and "doubly nested" in text, text
        checks += 1
        for path in (ws / f"{base} 2", ws / f"{entry['prefix']}_HarmonyGames_Gmail", ws / base / Path(base).name):
            path.rmdir()
        shutil.rmtree(ws / entry["folder"])
        ok, text = run(["normal"])
        assert not ok and "is not installed" in text, text
        checks += 1
    finally:
        shutil.rmtree(ws, ignore_errors=True)
    print(f"self-test: ok ({checks} cases: clean incl. an NFD file name, a source manifest disagreeing with the "
          f"routing-manifest pins, malformed source manifests incl. null/numeric paths, unlisted Finder metadata "
          f"ignored but a listed .DS_Store required, size mismatch, same-size change caught only by --sha256, "
          f"missing + extra, a dangling and a live file link, a directory link and an empty directory at a listed "
          f"path, two spellings of one name on disk (also through os.walk) and in the manifest, split / root-level / "
          f"doubly nested folders, universe not installed)")
    return 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["--self-test"]:
        return _self_test()
    try:
        keys = sorted(_universe_module().UNIVERSES)
    except ContextError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--universe", choices=keys, action="append",
                        help="check only this universe (repeatable; default: all)")
    parser.add_argument("--sha256", action="store_true", help="also verify every file's SHA-256 (reads all data)")
    args = parser.parse_args(argv)
    return 0 if verify(WORKSPACE, args.universe or keys, sha256=args.sha256) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
