"""Compact manifest routing and validated JSON collection/record byte offsets.

Prepared package indexes are imported on first use only after checking their
pinned digest and the actual source SHA256. Runtime caches bind the local source,
manifest and helper versions; missing or invalid caches fall back to streaming.
This module never builds an index implicitly or changes a universe source.
"""
from contextvars import ContextVar
from functools import wraps
import argparse
import base64
import zlib
import hashlib
import io
import json
from pathlib import Path
import sys
import hg_search_batch as batch

VERSION = 'compact-offset-v1'
PACKAGE_VERSION = 'compact-offset-package-v1'
_OPERATIONS = ContextVar('compact_operations', default=None)


def stat_signature(path):
    s = path.stat()
    return [str(path.resolve()), s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns, s.st_ctime_ns]


def watch_manifest(path):
    """Also used for code/package files; check again at the operation boundary."""
    state = _OPERATIONS.get()
    if state is not None:
        current = stat_signature(path)
        if path in state['files'] and state['files'][path] != current:
            raise ValueError('Source, manifest or helper changed during operation')
        state['files'][path] = current


def manifest_operation(fallback=False, reuse_loads=False):
    def decorate(fn):
        @wraps(fn)
        def run(*args, **kwargs):
            if _OPERATIONS.get() is not None:
                return fn(*args, **kwargs)
            token = _OPERATIONS.set({'files': {}, 'hashes': {}, 'reuse_loads': reuse_loads})
            try:
                result = fn(*args, **kwargs)
                for path in list(_OPERATIONS.get()['files']):
                    watch_manifest(path)
                return result
            except (OSError, ValueError, KeyError, TypeError, UnicodeError, RecursionError):
                if fallback:
                    return None
                raise
            finally:
                _OPERATIONS.reset(token)
        return run
    return decorate


def content_sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def helper_signature(h):
    """Hash code once within this operation, never reuse hashes across calls."""
    paths = getattr(h, 'helper_paths', (Path(__file__), Path(batch.__file__),
                                      Path(__file__).with_name('hg_search.py')))
    output = []
    state = _OPERATIONS.get()
    for name in paths:
        path = Path(name).resolve()
        watch_manifest(path)
        signature = stat_signature(path)
        key = tuple(signature)
        known = state['hashes'] if state is not None else {}
        digest = known.get(key)
        if digest is None:
            digest = content_sha256(path)
            if signature != stat_signature(path):
                raise ValueError('Helper changed during hashing')
            known[key] = digest
        output.append([path.name, digest])
    return output


def compact_cache(h, kind, request):
    folder = h.ROOT / 'Evals/.cache/compact'
    folder.resolve().relative_to(h.ROOT.resolve())
    cursor = folder
    while cursor != h.ROOT:
        if cursor.is_symlink():
            raise OSError('Compact cache directories must not be symbolic links')
        if cursor == cursor.parent:
            raise OSError('Compact cache must stay inside workspace')
        cursor = cursor.parent
    path = folder / (batch.digest([kind, request]) + '.json')
    if path.is_symlink():
        raise OSError('Compact cache must not be a symbolic link')
    return path


def write_cache(path, signature, result):
    # The underlying helper may attach an IO warning; keep it out of evidence.
    batch.write_cache(path, signature, dict(result))


MANIFEST_MAX_DECODED = 64 * 1024 * 1024


def pack_manifest(records):
    raw = json.dumps(records, ensure_ascii=False, separators=(',', ':')).encode()
    if len(raw) <= 1024 * 1024 or len(raw) > MANIFEST_MAX_DECODED:
        return {'files': records}
    return {'files_zlib_base64': base64.b64encode(zlib.compress(raw, level=1)).decode()}


def unpack_manifest(saved):
    if 'files' in saved:
        records = saved['files']
    else:
        compressed = base64.b64decode(saved['files_zlib_base64'], validate=True)
        decoder = zlib.decompressobj()
        raw = decoder.decompress(compressed, MANIFEST_MAX_DECODED + 1)
        if len(raw) > MANIFEST_MAX_DECODED or not decoder.eof or decoder.unused_data:
            raise ValueError('Invalid or oversized structured manifest cache')
        records = json.loads(raw, object_pairs_hook=batch.unique_object)
    if not isinstance(records, list) or any(not isinstance(row, dict) for row in records):
        raise ValueError('Invalid structured manifest records')
    return records


@manifest_operation()
def structured_info(h, service):
    universe = h.ROOT / 'Evals/references/universe_manifest.json'
    watch_manifest(universe)
    services = h.manifest()['services']
    if service not in services:
        raise ValueError('Unknown service: ' + service)
    folder = h.ROOT / services[service]['path']
    path = folder / 'source_manifest.json'
    watch_manifest(path)
    before = [stat_signature(universe), stat_signature(path), helper_signature(h)]
    try:
        cache = compact_cache(h, VERSION + '-manifest-v2', [service, str(path.resolve())])
    except (OSError, ValueError):
        cache = None
    saved = batch.read_cache(cache, before)
    if saved is not None and before[:2] == [stat_signature(universe), stat_signature(path)]:
        try:
            return folder, unpack_manifest(saved)
        except (ValueError, KeyError, TypeError, zlib.error):
            pass
    records = list(h.candidates(json.loads(path.read_text())['files']))
    if before[:2] != [stat_signature(universe), stat_signature(path)]:
        raise ValueError('Source manifest changed during read')
    write_cache(cache, before, pack_manifest(records))
    return folder, records


def index_path(h, service, rel):
    return compact_cache(h, VERSION + '-offsets', [service, rel])


def source_signature(h, folder, info):
    return {'version': VERSION, 'source': batch.fingerprint(h, folder, [info]),
            'universe': stat_signature(h.ROOT / 'Evals/references/universe_manifest.json'),
            'manifest': stat_signature(folder / 'source_manifest.json'),
            'helpers': helper_signature(h)}


@manifest_operation()
def source(h, service, rel):
    folder, records = structured_info(h, service)
    info = next((r for r in records if r['path'] == rel), None)
    if info is None:
        raise ValueError('Source not in structured manifest')
    path = h.safe_file(folder, rel)
    watch_manifest(path)
    return folder, info, path, source_signature(h, folder, info)


def checked_data(data, size):
    if not isinstance(data, dict) or data.get('validated_full_json') is not True:
        raise ValueError('Index lacks complete JSON validation')
    nodes = data.get('nodes')
    if not isinstance(nodes, list):
        raise ValueError('Invalid compact index nodes')
    for node in nodes:
        if (not isinstance(node, list) or len(node) != 4 or not isinstance(node[0], str)
                or type(node[1]) is not int or type(node[2]) is not int
                or not 0 <= node[1] < node[2] <= size
                or node[3] not in ('value', 'object', 'array')):
            raise ValueError('Invalid compact index offset')
    return data


@manifest_operation()
def build(h, service, rel):
    """Explicit developer operation; ordinary searches never call this."""
    folder, info, path, before = source(h, service, rel)
    nodes, opened = [], {}
    with path.open(encoding='utf-8-sig', newline='') as handle:
        with path.open('rb') as prefix:
            bom = 3 if prefix.read(3) == b'\xef\xbb\xbf' else 0
        stream = h.Stream(handle, track_offsets=True, byte_offset=bom)
        for event, parts, value in stream.events():
            if len(parts) > 2:
                continue
            if event == 'end':
                start, kind = opened.pop(parts)
                nodes.append([h.pointer(parts), start, stream.tell_bytes(), kind])
            elif event == 'value':
                nodes.append([h.pointer(parts), stream.event_offset, stream.tell_bytes(), event])
            else:
                opened[parts] = [stream.event_offset, event]
        if stream.peek():
            raise ValueError('Trailing content after JSON value')
    if before != source_signature(h, folder, info):
        raise ValueError('Source changed during index build')
    data = checked_data({'nodes': nodes, 'validated_full_json': True}, path.stat().st_size)
    cache = index_path(h, service, rel)
    write_cache(cache, before, data)
    if batch.read_cache(cache, before) is None:
        raise ValueError('Index exceeds cache cap or cannot be saved')
    return {'nodes': len(nodes), 'cache_bytes': cache.stat().st_size,
            'scope': 'Top-level collections and immediate records only', 'complete': True}


def package_entry(h, service, rel):
    directory = h.ROOT / 'Evals/references/search_indexes'
    manifest = directory / 'manifest.json'
    if not manifest.exists():
        return None
    watch_manifest(manifest)
    package = json.loads(manifest.read_text(), object_pairs_hook=batch.unique_object)
    if (not isinstance(package, dict) or package.get('version') != PACKAGE_VERSION
            or not isinstance(package.get('indexes'), list)
            or any(not isinstance(entry, dict) for entry in package['indexes'])):
        raise ValueError('Incompatible compact index package')
    entries = [entry for entry in package['indexes']
               if entry.get('service') == service and entry.get('file') == rel]
    if not entries:
        return None
    if len(entries) != 1:
        raise ValueError('Ambiguous compact index package entry')
    entry = entries[0]
    filename = (directory / entry['path']).resolve()
    filename.relative_to(directory.resolve())
    for field in ('sha256', 'source_sha256'):
        value = entry[field]
        if not isinstance(value, str) or len(value) != 64 or any(c not in '0123456789abcdef' for c in value):
            raise ValueError('Invalid compact index digest')
    watch_manifest(filename)
    return filename, entry, {'manifest': stat_signature(manifest), 'entry': entry,
                              'artifact': stat_signature(filename)}


def read_portable(filename, expected_sha256, service, rel, source_sha256):
    if filename.stat().st_size > 8 * 1024 * 1024:
        raise ValueError('Portable compact index exceeds size limit')
    raw = filename.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected_sha256:
        raise ValueError('Portable index differs from the pinned package artifact')
    saved = json.loads(raw)
    payload = saved['payload']
    if (saved['checksum'] != batch.digest(payload) or payload['version'] != VERSION
            or payload['service'] != service or payload['file'] != rel
            or payload['source_sha256'] != source_sha256):
        raise ValueError('Corrupt, incompatible or mismatched portable index')
    return payload['data']


def _load_file(h, args, rel):
    folder, info, path, signature = source(h, args.service, rel)
    package = package_entry(h, args.service, rel)
    binding = dict(signature)
    if package is not None:
        filename, entry, package_signature = package
        binding['package'] = package_signature
    cache = index_path(h, args.service, rel)
    data = batch.read_cache(cache, binding)
    if data is not None and data.get('rejected') is True:
        return None
    if data is None and package is not None:
        try:
            if entry['source_sha256'] != info.get('sha256'):
                raise ValueError('Portable index disagrees with source manifest')
            data = read_portable(filename, entry['sha256'], args.service, rel, entry['source_sha256'])
            checked_data(data, path.stat().st_size)
            if getattr(args, 'progress', False):
                print('Validating prepared index source: ' + args.service + '/' + rel,
                      file=sys.stderr, flush=True)
            actual = content_sha256(path)
            if actual != entry['source_sha256']:
                raise ValueError('Portable index does not match actual source bytes')
            if signature != source_signature(h, folder, info):
                raise ValueError('Source changed while importing index')
            write_cache(cache, binding, data)
            # No writable cache means full streaming fallback for this call.
            data = batch.read_cache(cache, binding)
        except (ValueError, KeyError, TypeError, UnicodeError):
            # Reject repeated mismatches cheaply only for this exact source,
            # package and helper binding. Any change forces fresh validation.
            if signature == source_signature(h, folder, info):
                write_cache(cache, binding, {'rejected': True})
            return None
    if data is None:
        return None
    checked_data(data, path.stat().st_size)
    return folder, info, path, signature, data['nodes']


def load(h, args, rel):
    # Reuse verified metadata only inside this bounded operation.
    # All watched sources, manifests and helper files are rechecked on exit.
    state = _OPERATIONS.get()
    reuse = state is not None and state.get('reuse_loads', False)
    memo = state.setdefault('loaded_files', {}) if reuse else {}
    key = (str(h.ROOT.resolve()), args.service, rel)
    if key not in memo:
        memo[key] = _load_file(h, args, rel)
    loaded = memo[key]
    if loaded is None:
        return None
    folder, info, path, signature, all_nodes = loaded
    anchor = h.parse_pointer(args.pointer)[:2]
    if reuse:
        maps = state.setdefault('node_maps', {})
        if key not in maps:
            maps[key] = {}
            for node in all_nodes:
                maps[key].setdefault(h.parse_pointer(node[0]), []).append(node)
        nodes = maps[key].get(anchor)
    else:
        # Keep the original individual-read path: no full dictionary allocation.
        nodes = [node for node in all_nodes if h.parse_pointer(node[0]) == anchor]
    if not nodes:
        return None
    return folder, info, path, signature, nodes


def scoped_events(h, path, node):
    with path.open('rb') as handle:
        handle.seek(node[1])
        with io.TextIOWrapper(handle, encoding='utf-8', newline='') as text:
            stream = h.Stream(text)
            yield from stream.events(h.parse_pointer(node[0]))


@manifest_operation(fallback=True)
def search_existing(h, args):
    if not args.pointer or getattr(args, 'no_index', False) or getattr(args, 'build_index', False):
        return None
    try:
        folder, records = structured_info(h, args.service)
        selected = list(h.candidates(records, args.file))
        if not selected:
            return None
        loaded = [load(h, args, info['path']) for info in selected]
        if any(item is None for item in loaded):
            return None
        result = {'matches': [], 'files_selected': len(selected), 'files_started': 0,
                  'files_completed': 0, 'scan_complete': True, 'errors': [],
                  'persona_filtered': False, 'scope': 'JSON scalar values; excludes root/ blobs and non-JSON attachments'}
        prefix = h.parse_pointer(args.pointer)
        stop = False
        for folder, info, path, signature, nodes in loaded:
            result['files_started'] += 1
            for node in nodes:
                events = scoped_events(h, path, node)
                try:
                    for event, parts, value in events:
                        if event != 'value' or parts[:len(prefix)] != prefix:
                            continue
                        if args.key and (not parts or parts[-1] != args.key):
                            continue
                        raw = value if isinstance(value, str) else json.dumps(value)
                        hit, encoding = h.snippet(raw, args.query, args.case_sensitive), 'json'
                        if hit is None:
                            decoded = h.decoded_gmail(args.service, parts, value)
                            if decoded is not None:
                                hit = h.snippet(decoded, args.query, args.case_sensitive)
                                encoding = 'base64url-utf8'
                        if hit is not None:
                            result['matches'].append({'file': path.relative_to(h.ROOT).as_posix(),
                                'service_file': info['path'], 'pointer': h.pointer(parts),
                                'parent_pointer': h.pointer(parts[:-1]), 'encoding': encoding, **hit})
                            if len(result['matches']) >= args.limit:
                                result['scan_complete'] = False
                                result['stop_reason'] = 'match limit reached; narrow by file/pointer/key or raise limit'
                                stop = True
                                break
                finally:
                    events.close()
                if stop:
                    break
            if stop:
                break
            result['files_completed'] += 1
        for folder, info, path, signature, nodes in loaded:
            if signature != source_signature(h, folder, info):
                raise ValueError('Source changed during scoped search')
        return {**result, 'backend': 'compact-offset'}
    except (OSError, ValueError, KeyError, TypeError, UnicodeError, RecursionError):
        return None


@manifest_operation(fallback=True)
def get_existing(h, args):
    if not args.pointer or getattr(args, 'no_index', False) or getattr(args, 'build_index', False):
        return None
    try:
        item = load(h, args, args.file)
        if item is None:
            return None
        folder, info, path, signature, nodes = item
        wanted = h.parse_pointer(args.pointer)
        # Ordinary get reads the first occurrence at an ambiguous JSON pointer.
        for node in nodes:
            events = scoped_events(h, path, node)
            try:
                for event in events:
                    if event[0] == 'end' or event[1] != wanted:
                        continue
                    if args.decode_base64:
                        decoded = h.decoded_gmail(args.service, wanted, event[2])
                        if event[0] != 'value' or decoded is None:
                            raise ValueError('Not a Gmail UTF8 body')
                        pieces = iter([decoded])
                    else:
                        pieces = h.render_subtree(event, events)
                    position, content, complete = 0, '', True
                    boundary = args.offset + args.max_chars
                    for piece in pieces:
                        end = position + len(piece)
                        if end > args.offset and position < boundary:
                            content += piece[max(0,args.offset-position):max(0,boundary-position)]
                        position = end
                        if position > boundary:
                            complete = False
                            break
                    if signature != source_signature(h, folder, info):
                        raise ValueError('Source changed during scoped read')
                    return {'file': path.relative_to(h.ROOT).as_posix(), 'pointer': args.pointer,
                            'text': content, 'encoding': 'decoded-utf8' if args.decode_base64 else 'rendered-json',
                            'offset': args.offset, 'truncated': not complete,
                            'next_offset': boundary if not complete else None,
                            'persona_filtered': False, 'backend': 'compact-offset'}
            finally:
                events.close()
        return None
    except (OSError, ValueError, KeyError, TypeError, UnicodeError, RecursionError):
        return None


@manifest_operation()
def export_portable(h, service, rel, destination):
    folder, info, path, before = source(h, service, rel)
    data = batch.read_cache(index_path(h, service, rel), before)
    if not data:
        raise ValueError('Build and validate the source index first')
    checked_data(data, path.stat().st_size)
    actual = content_sha256(path)
    if actual != info.get('sha256'):
        raise ValueError('Source content differs from the declared export hash')
    if before != source_signature(h, folder, info):
        raise ValueError('Source changed while exporting index')
    payload = {'version': VERSION, 'service': service, 'file': rel,
               'source_sha256': actual, 'data': data}
    destination.write_text(json.dumps({'payload': payload, 'checksum': batch.digest(payload)}))
    return {'bytes': destination.stat().st_size, 'source_sha256': actual,
            'artifact_sha256': content_sha256(destination)}


@manifest_operation()
def import_portable(h, filename, expected_artifact_sha256):
    """Explicit import for package preparation/tests; normal use imports via load."""
    watch_manifest(filename)
    raw = filename.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected_artifact_sha256:
        raise ValueError('Portable index differs from the pinned package artifact')
    payload = json.loads(raw)['payload']
    folder, info, path, before = source(h, payload['service'], payload['file'])
    data = read_portable(filename, expected_artifact_sha256, payload['service'],
                         payload['file'], info.get('sha256'))
    checked_data(data, path.stat().st_size)
    actual = content_sha256(path)
    if actual != payload['source_sha256']:
        raise ValueError('Portable index does not match actual source bytes')
    if before != source_signature(h, folder, info):
        raise ValueError('Source changed while importing index')
    cache = index_path(h, payload['service'], payload['file'])
    write_cache(cache, before, data)
    if batch.read_cache(cache, before) is None:
        raise ValueError('Could not save imported index')
    return {'bytes': cache.stat().st_size, 'source_sha256': actual, 'complete': True}


if __name__ == '__main__':
    import hg_search as h
    parser = argparse.ArgumentParser(description='Explicitly prepare a compact source index')
    parser.add_argument('service')
    parser.add_argument('file')
    args = parser.parse_args()
    print(json.dumps(build(h, args.service, args.file)))
