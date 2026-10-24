#!/usr/bin/env python3
"""Read-only, bounded search over the bundled universe; Python standard library only."""
import argparse
import base64
import fnmatch
import json
from pathlib import Path
import os as _ta_os
import sqlite3
import sys
from types import SimpleNamespace
from hg_compact_index import manifest_operation, watch_manifest

ROOT = Path(__file__).resolve().parents[4]
DECODER = json.JSONDecoder()


class Stream:
    """Incremental JSON tokenizer; memory scales with the largest scalar, not file."""
    def __init__(self, handle, chunk=65536, track_offsets=False, byte_offset=0):
        self.handle, self.chunk = handle, chunk
        self.buf, self.pos, self.eof = '', 0, False
        self.track_offsets = track_offsets
        self.byte_offset, self.byte_pos = byte_offset, 0
        self.event_offset = byte_offset

    def tell_bytes(self):
        """UTF-8 source offset; tracked reads must preserve source newlines."""
        self.byte_offset += len(self.buf[self.byte_pos:self.pos].encode('utf-8'))
        self.byte_pos = self.pos
        return self.byte_offset

    def more(self):
        if self.track_offsets:
            self.tell_bytes()
        self.buf = self.buf[self.pos:]
        self.pos = self.byte_pos = 0
        part = self.handle.read(self.chunk)
        self.buf += part
        if not part:
            self.eof = True

    def peek(self):
        while True:
            while self.pos < len(self.buf) and self.buf[self.pos].isspace():
                self.pos += 1
            if self.pos < len(self.buf):
                return self.buf[self.pos]
            if self.eof:
                return ''
            self.more()

    def expect(self, token):
        if self.peek() != token:
            raise ValueError('Malformed JSON: expected ' + token)
        self.pos += 1

    def scalar(self):
        if not self.peek():
            raise ValueError('Unexpected end of JSON')
        while True:
            try:
                value, end = DECODER.raw_decode(self.buf, self.pos)
                # A number may continue across a buffer boundary.
                if end == len(self.buf) and not self.eof:
                    self.more()
                    continue
                if isinstance(value, (int, float)) and not isinstance(value, bool) and end < len(self.buf) and self.buf[end] not in ' \t\r\n,]}':
                    if self.eof:
                        raise ValueError('Malformed JSON number')
                    self.more()
                    continue
                self.pos = end
                return value
            except json.JSONDecodeError:
                if self.eof:
                    raise
                self.more()

    def events(self, path=()):
        token = self.peek()
        if self.track_offsets:
            self.event_offset = self.tell_bytes()
        if token == '{':
            self.pos += 1
            yield ('object', path, None)
            if self.peek() != '}':
                while True:
                    key = self.scalar()
                    if not isinstance(key, str):
                        raise ValueError('JSON object key must be a string')
                    self.expect(':')
                    yield from self.events(path + (key,))
                    if self.peek() != ',':
                        break
                    self.pos += 1
            self.expect('}')
            yield ('end', path, None)
        elif token == '[':
            self.pos += 1
            yield ('array', path, None)
            if self.peek() != ']':
                index = 0
                while True:
                    yield from self.events(path + (str(index),))
                    index += 1
                    if self.peek() != ',':
                        break
                    self.pos += 1
            self.expect(']')
            yield ('end', path, None)
        else:
            value = self.scalar()
            if isinstance(value, (dict, list)):
                raise ValueError('Unexpected container token')
            yield ('value', path, value)


def pointer(path):
    return ''.join('/' + p.replace('~', '~0').replace('/', '~1') for p in path)


def parse_pointer(value):
    if value == '':
        return ()
    if not value.startswith('/'):
        raise ValueError('Use a JSON pointer starting with /, or empty string for the root')
    return tuple(s.replace('~1', '/').replace('~0', '~') for s in value[1:].split('/'))


def manifest():
    return json.loads((Path(_ta_os.environ.get('TASK_AUTHORING_UNIVERSE_MANIFEST', str(ROOT / 'Evals/references/universe_manifest.json')))).read_text())


@manifest_operation()
def service_info(service):
    watch_manifest(Path(_ta_os.environ.get('TASK_AUTHORING_UNIVERSE_MANIFEST', str(ROOT / 'Evals/references/universe_manifest.json'))))
    services = manifest()['services']
    if service not in services:
        raise ValueError('Unknown service: ' + service)
    info = services[service]
    folder = ROOT / info['path']
    watch_manifest(folder / 'source_manifest.json')
    records = json.loads((folder / 'source_manifest.json').read_text())['files']
    return folder, records


def compact_api():
    return SimpleNamespace(ROOT=ROOT, manifest=manifest, candidates=candidates,
        safe_file=safe_file, Stream=Stream, pointer=pointer, parse_pointer=parse_pointer,
        snippet=snippet, decoded_gmail=decoded_gmail, render_subtree=render_subtree)


def structured_service_info(service):
    from hg_compact_index import structured_info
    return structured_info(compact_api(), service)


def get_service_info(args):
    if args.file.endswith('.json') and not args.file.startswith('root/'):
        return structured_service_info(args.service)
    return service_info(args.service)


def safe_file(folder, rel):
    resolved = (folder / rel).resolve()
    try:
        resolved.relative_to(folder.resolve())
    except ValueError:
        raise ValueError('Path must stay inside the selected service')
    watch_manifest(resolved)
    return resolved


def candidates(records, pattern=None, blobs=False):
    for record in sorted(records, key=lambda r: r['path']):
        rel = record['path']
        if pattern and not fnmatch.fnmatchcase(rel, pattern):
            continue
        if blobs or (rel.endswith('.json') and not rel.startswith('root/')):
            yield record


def snippet(text, query, case_sensitive, width=600):
    found = text.find(query) if case_sensitive else text.casefold().find(query.casefold())
    if found < 0:
        return None
    start = max(0, found - 150)
    return {'text': text[start:start + width], 'truncated': start > 0 or start + width < len(text)}


def decoded_gmail(service, path, value):
    if service == 'gmail' and path and path[-1] == 'data' and 'body' in path and isinstance(value, str):
        try:
            return base64.b64decode(value + '=' * (-len(value) % 4), altchars=b'-_', validate=True).decode('utf-8')
        except (ValueError, UnicodeError):
            pass
    return None


@manifest_operation()
def scan_search(args):
    folder, records = structured_service_info(args.service)
    selected = list(candidates(records, args.file))
    if not selected:
        raise ValueError('No structured JSON files match; use files to inspect paths')
    prefix = parse_pointer(args.pointer)
    result = {'matches': [], 'files_selected': len(selected), 'files_started': 0,
              'files_completed': 0, 'scan_complete': True, 'errors': [],
              'persona_filtered': False, 'scope': 'JSON scalar values; excludes root/ blobs and non-JSON attachments'}
    for info in selected:
        result['files_started'] += 1
        try:
            p = safe_file(folder, info['path'])
            with p.open(encoding='utf-8-sig') as f:
                stream = Stream(f)
                for event, path, value in stream.events():
                    if event != 'value' or path[:len(prefix)] != prefix:
                        continue
                    if args.key and (not path or path[-1] != args.key):
                        continue
                    raw = value if isinstance(value, str) else json.dumps(value)
                    hit = snippet(raw, args.query, args.case_sensitive)
                    encoding = 'json'
                    if hit is None:
                        decoded = decoded_gmail(args.service, path, value)
                        if decoded is not None:
                            hit = snippet(decoded, args.query, args.case_sensitive)
                            encoding = 'base64url-utf8'
                    if hit is not None:
                        result['matches'].append({'file': p.relative_to(ROOT).as_posix(),
                            'service_file': info['path'], 'pointer': pointer(path),
                            'parent_pointer': pointer(path[:-1]), 'encoding': encoding, **hit})
                        if len(result['matches']) >= args.limit:
                            result['scan_complete'] = False
                            result['stop_reason'] = 'match limit reached; narrow by file/pointer/key or raise limit'
                            return result
                if stream.peek():
                    raise ValueError('Trailing content after JSON value')
            result['files_completed'] += 1
        except (OSError, ValueError, RecursionError) as error:
            result['errors'].append({'file': info['path'], 'error': str(error)[:300]})
            result['scan_complete'] = False
    return result


def render_subtree(first, iterator):
    """Render selected event subtree incrementally, keeping no full record in RAM."""
    event, path, value = first
    if event == 'value':
        yield json.dumps(value, ensure_ascii=False)
        return
    stack = [(event, True)]
    yield '{' if event == 'object' else '['
    for event, path, value in iterator:
        if event == 'end':
            kind, _ = stack.pop()
            yield '}' if kind == 'object' else ']'
            if not stack:
                return
            continue
        kind, first_item = stack[-1]
        if not first_item:
            yield ','
        stack[-1] = kind, False
        if kind == 'object':
            yield json.dumps(path[-1], ensure_ascii=False) + ':'
        if event in ('object', 'array'):
            yield '{' if event == 'object' else '['
            stack.append((event, True))
        else:
            yield json.dumps(value, ensure_ascii=False)


@manifest_operation()
def scan_get(args):
    folder, records = get_service_info(args)
    if args.file not in {r['path'] for r in records}:
        raise ValueError('File is not in the source manifest; use files to find its service-relative path')
    p = safe_file(folder, args.file)
    desired = parse_pointer(args.pointer)
    with p.open(encoding='utf-8-sig') as f:
        stream = Stream(f)
        events = stream.events()
        for event in events:
            if event[0] == 'end' or event[1] != desired:
                continue
            if args.decode_base64:
                decoded = decoded_gmail(args.service, desired, event[2])
                if event[0] != 'value' or decoded is None:
                    raise ValueError('Decoding is only supported for UTF-8 Gmail body.data strings')
                pieces = iter([decoded])
            else:
                pieces = render_subtree(event, events)
            position, text, complete = 0, '', True
            boundary = args.offset + args.max_chars
            for piece in pieces:
                end = position + len(piece)
                if end > args.offset and position < boundary:
                    text += piece[max(0, args.offset-position):max(0, boundary-position)]
                position = end
                if position > boundary:
                    complete = False
                    break
            return {'file': p.relative_to(ROOT).as_posix(), 'pointer': args.pointer,
                    'text': text, 'encoding': 'decoded-utf8' if args.decode_base64 else 'rendered-json',
                    'offset': args.offset, 'truncated': not complete,
                    'next_offset': boundary if not complete else None,
                    'persona_filtered': False}
        if stream.peek():
            raise ValueError('Trailing content after JSON value')
    raise ValueError('JSON pointer not found')


def open_index(args, folder, records, readonly=None):
    from hg_search_index import SearchIndex
    progress = (lambda message: print(message, file=sys.stderr, flush=True)) if getattr(args, 'progress', False) else None
    if readonly is None:
        readonly = not getattr(args, 'build_index', False)
    return SearchIndex(ROOT, args.service, folder, records, Stream, pointer,
                       decoded_gmail, progress=progress, rebuild=getattr(args, 'rebuild', False), readonly=readonly)


@manifest_operation()
def indexed_search(args):
    folder, records = structured_service_info(args.service)
    selected = list(candidates(records, args.file))
    if not selected:
        raise ValueError('No structured JSON files match; use files to inspect paths')
    prefix = pointer(parse_pointer(args.pointer))
    result = {'matches': [], 'files_selected': len(selected), 'files_started': 0,
              'files_completed': 0, 'scan_complete': True, 'errors': [],
              'persona_filtered': False, 'scope': 'JSON scalar values; excludes root/ blobs and non-JSON attachments'}
    with open_index(args, folder, records) as index:
        checked = []
        for info in selected:
            result['files_started'] += 1
            p = safe_file(folder, info['path'])
            file_id, signature = index.ensure(p, info)
            checked.append((p, info, signature))
            for row in index.matches(file_id, prefix, args.key, args.query):
                hit = snippet(row['raw'], args.query, args.case_sensitive)
                encoding = 'json'
                if hit is None and row['decoded'] is not None:
                    hit = snippet(row['decoded'], args.query, args.case_sensitive)
                    encoding = 'base64url-utf8'
                if hit is None:
                    continue
                result['matches'].append({'file': p.relative_to(ROOT).as_posix(),
                    'service_file': info['path'], 'pointer': row['pointer'],
                    'parent_pointer': row['pointer'].rpartition('/')[0], 'encoding': encoding, **hit})
                if len(result['matches']) >= args.limit:
                    result['scan_complete'] = False
                    result['stop_reason'] = 'match limit reached; narrow by file/pointer/key or raise limit'
                    break
            if not result['scan_complete']:
                break
            result['files_completed'] += 1
        for p, info, signature in checked:
            index.check_signature(p, info, signature)
        result.update(index.metadata())
    return result


@manifest_operation()
def indexed_get(args):
    folder, records = get_service_info(args)
    info = next((r for r in records if r['path'] == args.file), None)
    if info is None:
        raise ValueError('File is not in the source manifest; use files to find its service-relative path')
    p = safe_file(folder, args.file)
    desired = parse_pointer(args.pointer)
    with open_index(args, folder, records) as index:
        file_id, signature = index.ensure(p, info)
        node = index.locate(file_id, pointer(desired))
        if node is None:
            raise ValueError('JSON pointer not found')
        # Seek in the original UTF-8 file, then render only the selected subtree.
        # newline='' is essential: cached offsets count bytes, including CRLF.
        with p.open('rb') as source:
            source.seek(node['byte_offset'])
            import io
            with io.TextIOWrapper(source, encoding='utf-8', newline='') as f:
                stream = Stream(f)
                events = stream.events(desired)
                first = next(events)
                if first[0] != node['kind']:
                    raise ValueError('Cached record location no longer matches the source')
                if args.decode_base64:
                    decoded = decoded_gmail(args.service, desired, first[2])
                    if first[0] != 'value' or decoded is None:
                        raise ValueError('Decoding is only supported for UTF-8 Gmail body.data strings')
                    pieces = iter([decoded])
                else:
                    pieces = render_subtree(first, events)
                position, text, complete = 0, '', True
                boundary = args.offset + args.max_chars
                for piece in pieces:
                    end = position + len(piece)
                    if end > args.offset and position < boundary:
                        text += piece[max(0, args.offset-position):max(0, boundary-position)]
                    position = end
                    if position > boundary:
                        complete = False
                        break
        index.check_signature(p, info, signature)
        return {'file': p.relative_to(ROOT).as_posix(), 'pointer': args.pointer,
                'text': text, 'encoding': 'decoded-utf8' if args.decode_base64 else 'rendered-json',
                'offset': args.offset, 'truncated': not complete,
                'next_offset': boundary if not complete else None,
                'persona_filtered': False, **index.metadata()}


def with_fallback(args, indexed, scan):
    if getattr(args, 'no_index', False):
        return {**scan(args), 'backend': 'stream'}
    from hg_search_index import IndexNotReady, cache_failure, cache_path
    services = manifest()['services']
    if args.service not in services:
        raise ValueError('Unknown service: ' + args.service)
    folder = ROOT / services[args.service]['path']
    retry = getattr(args, 'build_index', False)
    warning = None if retry else cache_failure(ROOT, args.service, folder)
    if warning:
        return {**scan(args), 'backend': 'stream',
                'cache_warning': 'Index temporarily bypassed after a cache error: ' + warning}
    try:
        if not retry and not cache_path(ROOT, args.service, folder).is_file():
            return {**scan(args), 'backend': 'stream'}
        return indexed(args)
    except IndexNotReady:
        return {**scan(args), 'backend': 'stream'}
    except (OSError, ValueError, sqlite3.Error, UnicodeError, RecursionError, ImportError) as error:
        # A malformed source, busy/unwritable/corrupt cache, or unsupported SQLite
        # must not turn old index contents into current evidence.
        if isinstance(error, sqlite3.Error):
            cache_failure(ROOT, args.service, folder, error=error)
        return {**scan(args), 'backend': 'stream',
                'cache_warning': 'Index unavailable; streaming scan used: ' + str(error)[:300]}


def search(args):
    from hg_compact_index import search_existing
    result = search_existing(compact_api(), args)
    return result if result is not None else with_fallback(args, indexed_search, scan_search)


def get(args):
    from hg_compact_index import get_existing
    result = get_existing(compact_api(), args)
    return result if result is not None else with_fallback(args, indexed_get, scan_get)


@manifest_operation()
def build_index(args):
    folder, records = structured_service_info(args.service)
    selected = list(candidates(records, args.file))
    if not selected:
        raise ValueError('No structured JSON files match; use files to inspect paths')
    from hg_search_index import cache_failure
    with open_index(args, folder, records, readonly=False) as index:
        for info in selected:
            index.ensure(safe_file(folder, info['path']), info, force=args.rebuild)
        cache_failure(ROOT, args.service, folder, clear=True)
        return {'service': args.service, 'files_selected': len(selected),
                'index_complete': True, **index.metadata()}


def prefer_compact_batch(service, pattern, queries):
    # Conservative planner: avoid repeating large indexed ranges.
    # These verified loads are reused within the same manifest operation.
    from hg_compact_index import load
    try:
        api = compact_api()
        folder, records = structured_service_info(service)
        selected = list(candidates(records, pattern))
        if not selected:
            return False
        for info in selected:
            read_bytes = 0
            for query in queries:
                args = SimpleNamespace(service=service, pointer=query['pointer'], progress=False)
                loaded = load(api, args, info['path'])
                if loaded is None:
                    return False
                read_bytes += sum(node[2]-node[1] for node in loaded[4])
            size = safe_file(folder, info['path']).stat().st_size
            if size > 128 * 1024 and read_bytes > min(size // 4, 8 * 1024 * 1024):
                return False
        return True
    except (OSError, ValueError, KeyError, TypeError, UnicodeError, RecursionError):
        return False


def try_compact_query(service, pattern, query, progress=False):
    from hg_compact_index import search_existing
    args = SimpleNamespace(service=service, file=pattern,
        pointer=query.get('pointer', ''), key=query.get('key'),
        query=query['query'], limit=query.get('limit', 20),
        case_sensitive=query.get('case_sensitive', False), progress=progress)
    return search_existing(compact_api(), args)


def try_identity_index(service, ids, pattern, pointer, key):
    try:
        from hg_id_index import lookup
    except ImportError:
        return None
    try:
        return lookup(compact_api(), service, ids, pattern, pointer, key)
    except (OSError, ValueError, KeyError, TypeError, AttributeError, UnicodeError, RecursionError):
        return None


def batch_api():
    return SimpleNamespace(indexed_search=try_compact_query, indexed_lookup=try_identity_index, prefer_compact_batch=prefer_compact_batch,
        ROOT=ROOT, Stream=Stream, parse_pointer=parse_pointer,
        pointer=pointer, service_info=structured_service_info, candidates=candidates,
        safe_file=safe_file, snippet=snippet, decoded_gmail=decoded_gmail)


@manifest_operation(reuse_loads=True)
def batch_search(request, **options):
    from hg_search_batch import search_many
    return search_many(batch_api(), request, **options)


@manifest_operation()
def batch_lookup(service, ids, file, pointer, key, **options):
    from hg_search_batch import lookup
    return lookup(batch_api(), service, ids, file, pointer, key, **options)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('inventory', help='Service coverage and source version; does not hash all files')
    listing = commands.add_parser('files', help='Find source paths, including blobs, by name')
    listing.add_argument('service')
    listing.add_argument('query', nargs='?', default='')
    listing.add_argument('--limit', type=int, default=20)
    find = commands.add_parser('search', help='Literal substring search of structured JSON values')
    find.add_argument('service')
    find.add_argument('query')
    find.add_argument('--file', help='Service-relative glob, for example messages/CHANNEL/*')
    find.add_argument('--pointer', default='', help='Restrict to this JSON subtree')
    find.add_argument('--key', help='Match values only under this field name')
    find.add_argument('--case-sensitive', action='store_true')
    find.add_argument('--limit', type=int, default=20)
    find_mode = find.add_mutually_exclusive_group()
    find_mode.add_argument('--no-index', action='store_true', help='Use the original streaming scan')
    find_mode.add_argument('--build-index', action='store_true', help='Explicitly build missing indexes; default reuses validated prepared or runtime indexes')
    read = commands.add_parser('get', help='Read an exact JSON pointer with bounded output')
    read.add_argument('service')
    read.add_argument('--file', required=True, help='Exact service-relative source file')
    read.add_argument('--pointer', default='')
    read.add_argument('--offset', type=int, default=0)
    read.add_argument('--max-chars', type=int, default=12000)
    read.add_argument('--decode-base64', action='store_true')
    read_mode = read.add_mutually_exclusive_group()
    read_mode.add_argument('--no-index', action='store_true', help='Read with the original streaming scanner')
    read_mode.add_argument('--build-index', action='store_true', help='Explicitly build an index for this file before reading')
    warm = commands.add_parser('index', help='Optional: build/refresh selected service files in advance')
    warm.add_argument('service')
    warm.add_argument('--file', help='Service-relative glob; omitted means all structured JSON')
    warm.add_argument('--rebuild', action='store_true', help='Force rebuilding selected cached files')
    batch = commands.add_parser('search-many', help='Search several terms using verified offsets or one shared scan')
    batch.add_argument('--request', required=True, help='JSON request path, or - for stdin')
    batch.add_argument('--no-cache', action='store_true', help='Bypass query-result cache')
    reads = commands.add_parser('get-many', help='Read several known JSON pointers with per-item pagination')
    reads.add_argument('--request', required=True, help='JSON items request path, or - for stdin')
    lookup = commands.add_parser('lookup', help='Check exact string IDs across a complete array-of-records collection')
    lookup.add_argument('service')
    lookup.add_argument('--ids-file', required=True, help='JSON array of string IDs, or - for stdin')
    lookup.add_argument('--file', required=True, help='Service-relative glob covering the full relevant collection')
    lookup.add_argument('--pointer', default='', help='JSON pointer to the record array in each selected file')
    lookup.add_argument('--key', default='id', help='Direct record field containing the unique ID')
    lookup.add_argument('--no-cache', action='store_true')
    for command in [find, read, warm, batch, lookup, reads]:
        command.add_argument('--progress', action='store_true', help='Write progress to stderr; stdout remains JSON')
    for command in [find, read, warm, batch, lookup, listing, reads]:
        command.add_argument('--compact', action='store_true', help='Emit compact JSON without dropping citations or coverage')
    args = parser.parse_args()
    try:
        if getattr(args, 'limit', 1) < 1 or getattr(args, 'offset', 0) < 0 or getattr(args, 'max_chars', 1) < 1:
            raise ValueError('Limit/max-chars must be positive and offset nonnegative')
        if args.command == 'inventory':
            m = manifest()
            rows = []
            for service, info in m['services'].items():
                p = ROOT / info['path']
                rows.append({'service': service, 'path': info['path'], 'directory_present': p.is_dir(),
                    'manifest_present': (p / 'source_manifest.json').is_file(),
                    'source_file_count': info['file_count'], 'source_bytes': info['total_bytes'],
                    'empty_export': info.get('empty_export')})
            result = {'archive': m['archive'], 'archive_sha256': m['archive_sha256'],
                      'services': rows, 'individual_files_verified': False, 'persona_filtered': False}
        elif args.command == 'files':
            folder, records = service_info(args.service)
            hits = [r for r in candidates(records, blobs=True) if args.query.casefold() in r['path'].casefold()]
            result = {'service_path': folder.relative_to(ROOT).as_posix(), 'matches': hits[:args.limit],
                      'total_matching_paths': len(hits), 'truncated': len(hits) > args.limit}
        elif args.command == 'search':
            if not args.query:
                raise ValueError('Supply a nonempty literal query')
            result = search(args)
        elif args.command == 'index':
            result = build_index(args)
        elif args.command == 'search-many':
            request = json.load(sys.stdin) if args.request == '-' else json.loads(Path(args.request).read_text())
            result = batch_search(request, no_cache=args.no_cache, progress=args.progress)
        elif args.command == 'get-many':
            from hg_get_many import get_many
            request = json.load(sys.stdin) if args.request == '-' else json.loads(Path(args.request).read_text())
            result = get_many(request, progress=args.progress)
        elif args.command == 'lookup':
            ids = json.load(sys.stdin) if args.ids_file == '-' else json.loads(Path(args.ids_file).read_text())
            result = batch_lookup(args.service, ids, args.file, args.pointer, args.key,
                                no_cache=args.no_cache, progress=args.progress)
        else:
            result = get(args)
        print(json.dumps(result, ensure_ascii=False, indent=None if getattr(args, 'compact', False) else 2))
        failed = (result.get('errors')
                  or any(v.get('errors') for v in result.get('queries', {}).values())
                  or any(v.get('error') for v in result.get('items', {}).values()))
        return 1 if failed else 0
    except (OSError, ValueError, RecursionError, sqlite3.Error) as error:
        print(json.dumps({'error': str(error), 'complete': False}), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
