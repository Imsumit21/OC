#!/usr/bin/env python3
"""Read-only exact record checks, grouped by physical source file."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import os as _ta_os
import stat
import sys
from collections import defaultdict
import uuid

import hg_search as h
import hg_search_batch as batch


CACHE_POLICY = 'complete-raw-records-v2'
CACHE_MAX_ENTRY_BYTES = 8 * 1024 * 1024
CACHE_MAX_BYTES = 32 * 1024 * 1024


def stat_identity(path):
    path = path.resolve()
    state = path.stat()
    return [str(path), state.st_dev, state.st_ino, state.st_size,
            state.st_mtime_ns, state.st_ctime_ns]


def helper_identity():
    paths = [Path(__file__), Path(h.__file__), Path(batch.__file__)]
    compact = Path(h.__file__).with_name('hg_compact_index.py')
    if compact.is_file():
        paths.append(compact)
    return [[path.name, hashlib.sha256(path.read_bytes()).hexdigest()]
            for path in paths]


def cache_path(request, threshold):
    root = h.ROOT.resolve()
    folder = root / 'Task_Authoring/support/local_search/contexts/6f0b6e7e63b7feee86db/cache/records'
    folder.resolve().relative_to(root)
    current = folder
    while current != root:
        if current.is_symlink():
            raise OSError('Record cache directories must not be symbolic links')
        current = current.parent
    path = folder / (batch.digest([CACHE_POLICY, request, threshold]) + '.json')
    if path.is_symlink():
        raise OSError('Record cache must not be a symbolic link')
    return path


def cache_directory(folder, create=False):
    """Open each cache component without following links, including during I/O."""
    root = h.ROOT.resolve()
    if folder != root / 'Task_Authoring/support/local_search/contexts/6f0b6e7e63b7feee86db/cache/records':
        raise OSError('Unexpected record cache directory')
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    descriptor = os.open(root, flags)
    try:
        for part in ('Task_Authoring', 'support', 'local_search', 'contexts', '6f0b6e7e63b7feee86db', 'cache', 'records'):
            if create:
                try:
                    os.mkdir(part, dir_fd=descriptor)
                except FileExistsError:
                    pass
            child = os.open(part, flags, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = child
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def read_record_cache(path, signature):
    if path is None or signature is None:
        return None
    directory = None
    try:
        directory = cache_directory(path.parent)
        descriptor = os.open(path.name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK,
                             dir_fd=directory)
        with os.fdopen(descriptor, 'rb') as handle:
            state = os.fstat(handle.fileno())
            if not stat.S_ISREG(state.st_mode) or state.st_size > CACHE_MAX_ENTRY_BYTES:
                return None
            raw = handle.read(CACHE_MAX_ENTRY_BYTES + 1)
        if len(raw) > CACHE_MAX_ENTRY_BYTES:
            return None
        saved = json.loads(raw, object_pairs_hook=batch.unique_object)
        if (saved['signature'] == signature and isinstance(saved['result'], dict)
                and saved['checksum'] == batch.digest(saved['result'])):
            return saved['result']
    except (OSError, ValueError, KeyError, TypeError, AttributeError, NotImplementedError):
        pass
    finally:
        if directory is not None:
            os.close(directory)
    return None


def write_record_cache(path, signature, result):
    """Atomic optional raw evidence storage; links cannot redirect cache writes."""
    if path is None or signature is None:
        return
    payload = json.dumps({'signature': signature, 'result': result,
                          'checksum': batch.digest(result)}).encode()
    if len(payload) > CACHE_MAX_ENTRY_BYTES:
        return
    directory = None
    temporary = None
    try:
        directory = cache_directory(path.parent, create=True)
        temporary = '.' + uuid.uuid4().hex + '.tmp'
        descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                             0o600, dir_fd=directory)
        with os.fdopen(descriptor, 'wb') as handle:
            handle.write(payload)
        os.replace(temporary, path.name, src_dir_fd=directory, dst_dir_fd=directory)
        temporary = None
    finally:
        if directory is not None:
            if temporary is not None:
                try:
                    os.unlink(temporary, dir_fd=directory)
                except (OSError, AttributeError, NotImplementedError):
                    pass
            os.close(directory)


def manifests_unchanged(paths, states):
    try:
        return states == [stat_identity(path) for path in paths]
    except OSError:
        return False


def cache_signature(request, threshold, jobs, manifests):
    return batch.digest([CACHE_POLICY, request, threshold, helper_identity(),
                         [stat_identity(path) for path in manifests],
                         [[key, batch.fingerprint(h, job['folder'], [job['info']])]
                          for key, job in jobs.items()]])


def complete_result(result, checks):
    if not isinstance(result, dict) or result.get('scan_complete') is not True:
        return False
    saved = result.get('checks')
    if not isinstance(saved, dict) or set(saved) != {c['id'] for c in checks}:
        return False
    for check in checks:
        item = saved[check['id']]
        if (not isinstance(item, dict) or item.get('scope') != check
                or item.get('scan_complete') is not True or item.get('errors') != []
                or type(item.get('files_selected')) is not int
                or item['files_selected'] < 1
                or item.get('files_completed') != item['files_selected']):
            return False
    return True


def trim_cache(folder):
    """Bound this helper's raw-result cache, excluding other query caches."""
    directory = None
    try:
        directory = cache_directory(folder)
        files = []
        for name in os.listdir(directory):
            suffix = '.check' if name.endswith('.check') else '.json'
            if (len(name) != 64 + len(suffix) or not name.endswith(suffix)
                    or any(c not in '0123456789abcdef' for c in name[:-len(suffix)])):
                continue
            state = os.stat(name, dir_fd=directory, follow_symlinks=False)
            if stat.S_ISREG(state.st_mode):
                files.append((state.st_mtime_ns, state.st_size, name))
        total = sum(size for _, size, _ in files)
        for _, size, name in sorted(files):
            if total <= CACHE_MAX_BYTES:
                break
            os.unlink(name, dir_fd=directory)
            total -= size
    except (OSError, AttributeError, NotImplementedError):
        pass  # Cache storage never decides evidence completeness.
    finally:
        if directory is not None:
            os.close(directory)


def validate(request):
    if not isinstance(request, dict) or set(request) != {'checks'}:
        raise ValueError('Expected {"checks": [...]}')
    checks = request['checks']
    if not isinstance(checks, list) or not checks:
        raise ValueError('Supply at least one check')
    ids = set()
    required = {'id', 'service', 'file', 'pointer', 'field', 'values'}
    for check in checks:
        if not isinstance(check, dict) or set(check) != required:
            raise ValueError('Each check needs id, service, file, pointer, field, values')
        for key in required - {'values'}:
            if not isinstance(check[key], str) or (key != 'pointer' and not check[key]):
                raise ValueError(key + ' must be a string (only pointer may be empty)')
        if check['id'] in ids:
            raise ValueError('Check IDs must be unique')
        ids.add(check['id'])
        h.parse_pointer(check['pointer'])
        if not isinstance(check['values'], list) or not check['values']:
            raise ValueError('values must be a nonempty list of strings or integers')
        if any(type(v) not in (str, int) for v in check['values']):
            raise ValueError('Only exact strings and integers are supported')
    return checks


def strict_events(path, threshold):
    """Reject duplicate object keys, including outside the selected records."""
    fields = {}
    for event, parts, value in batch.events(h, path, threshold):
        if event == 'end':
            fields.pop(parts, None)
        else:
            if parts and parts[:-1] in fields:
                seen = fields[parts[:-1]]
                if parts[-1] in seen:
                    raise ValueError('Duplicate JSON object key: ' + parts[-1])
                seen.add(parts[-1])
            if event == 'object':
                fields[parts] = set()
        yield event, parts, value


def at_pointer(data, parts):
    for part in parts:
        if isinstance(data, dict) and part in data:
            data = data[part]
        elif (isinstance(data, list) and part.isdecimal()
              and str(int(part)) == part and int(part) < len(data)):
            data = data[int(part)]
        else:
            raise ValueError('Record array pointer not found')
    if not isinstance(data, list):
        raise ValueError('Expected an array at the record pointer')
    return data


def canonical_check(check):
    values = sorted(set(check['values']), key=lambda v: (type(v).__name__, str(v)))
    return {**check, 'id': 'check', 'values': values}


def check_snapshot(jobs, manifests):
    return {'helpers': helper_identity(),
            'manifests': {str(path): stat_identity(path) for path in manifests},
            'sources': {key: batch.fingerprint(h, job['folder'], [job['info']])
                        for key, job in jobs.items()}}


def individual_binding(check, threshold, keys, manifests, snapshot):
    return batch.digest([CACHE_POLICY, {'checks': [check]}, threshold,
                         snapshot['helpers'],
                         [snapshot['manifests'][str(path)] for path in manifests],
                         [[key, snapshot['sources'][key]] for key in keys]])


def individual_path(check, threshold):
    path = cache_path({'checks': [check]}, threshold).with_suffix('.check')
    if path.is_symlink():
        raise OSError('Individual cache must not be a symbolic link')
    return path


def run(request, threshold=32 * 1024 * 1024, no_cache=False):
    checks = validate(request)
    universe_path = Path(_ta_os.environ.get('TASK_AUTHORING_UNIVERSE_MANIFEST', str(h.ROOT / 'Evals/references/universe_manifest.json')))
    manifest_paths = [universe_path]
    manifest_states = [stat_identity(universe_path)]
    routing = h.manifest()['services']
    sources = {}
    jobs = {}
    results = {}
    for check in checks:
        service = check['service']
        if service not in sources:
            if service not in routing:
                raise ValueError('Unknown service: ' + service)
            source_manifest = h.ROOT / routing[service]['path'] / 'source_manifest.json'
            manifest_paths.append(source_manifest)
            manifest_states.append(stat_identity(source_manifest))
            structured_info = getattr(h, 'structured_service_info', None)
            sources[service] = (structured_info(service) if callable(structured_info)
                                else h.service_info(service))
        folder, manifest = sources[service]
        selected = list(h.candidates(manifest, check['file']))
        results[check['id']] = {
            'scope': dict(check), 'matches': [], 'records_checked': 0,
            'files_selected': len(selected), 'files_completed': 0,
            'scan_complete': bool(selected), 'errors': [],
        }
        if not selected:
            results[check['id']]['errors'].append({'error': 'No matching source files'})
        for info in selected:
            key = (service, info['path'])
            job = jobs.setdefault(key, {'folder': folder, 'info': info, 'checks': []})
            job['checks'].append(check)

    # Validate original request relationships before removing cached checks.
    all_jobs = {key: {**job, 'checks': list(job['checks'])} for key, job in jobs.items()}
    for job in jobs.values():
        prefixes = {h.parse_pointer(check['pointer']) for check in job['checks']}
        if any(a != b and a[:len(b)] == b for a in prefixes for b in prefixes):
            raise ValueError('Overlapping record arrays require separate requests')

    cache = signature = None
    cache_allowed = not no_cache
    try:
        manifests_stable = manifests_unchanged(manifest_paths, manifest_states)
        if not no_cache and manifests_stable:
            cache = cache_path(request, threshold)
            signature = cache_signature(request, threshold, all_jobs, manifest_paths)
            saved = read_record_cache(cache, signature)
            if (complete_result(saved, checks)
                    and signature == cache_signature(request, threshold, all_jobs, manifest_paths)
                    and manifests_unchanged(manifest_paths, manifest_states)):
                return {**saved, 'backend': 'record-query-cache', 'files_read_this_call': 0,
                        'checks_reused': [check['id'] for check in checks]}
    except (OSError, ValueError, KeyError, TypeError, AttributeError, NotImplementedError):
        cache = signature = None
        cache_allowed = False

    reusable, bindings, cached_sources = {}, {}, {}
    initial = None
    # Existing but invalid whole-request caches take the conservative fresh path.
    try:
        if cache_allowed and manifests_unchanged(manifest_paths, manifest_states):
            initial = check_snapshot(all_jobs, manifest_paths)
            allow_reuse = cache is None or not cache.exists()
            for check in checks:
                canonical = canonical_check(check)
                keys = [key for key, job in all_jobs.items()
                        if any(item['id'] == check['id'] for item in job['checks'])]
                required_manifests = [universe_path,
                    h.ROOT / routing[check['service']]['path'] / 'source_manifest.json']
                path = individual_path(canonical, threshold)
                binding = individual_binding(canonical, threshold, keys, required_manifests, initial)
                bindings[check['id']] = (canonical, path, binding, keys, required_manifests)
                saved = read_record_cache(path, binding) if allow_reuse else None
                if complete_result(saved, [canonical]):
                    reusable[check['id']] = saved
            current = check_snapshot(all_jobs, manifest_paths)
            for check in checks:
                saved = reusable.get(check['id'])
                if saved is None:
                    continue
                canonical, path, binding, keys, required = bindings[check['id']]
                if (binding != individual_binding(canonical, threshold, keys, required, current)
                        or not manifests_unchanged(manifest_paths, manifest_states)):
                    reusable.pop(check['id'])
                    continue
                results[check['id']] = {**saved['checks']['check'], 'scope': dict(check)}
                for receipt in saved['sources']:
                    cached_sources[receipt['file']] = receipt
            jobs = {key: {**job, 'checks': [c for c in job['checks'] if c['id'] not in reusable]}
                    for key, job in jobs.items()}
            jobs = {key: job for key, job in jobs.items() if job['checks']}
    except (OSError, ValueError, KeyError, TypeError, AttributeError, NotImplementedError):
        reusable, bindings, cached_sources = {}, {}, {}
        initial = None
        jobs = all_jobs
        # A partial cache probe must not leak its restored matches into the scan.
        for check in checks:
            target = results[check['id']]
            target.update(scope=dict(check), matches=[], records_checked=0, files_completed=0,
                          scan_complete=bool(target['files_selected']))

    def accept(check, record, parts, source):
        if not isinstance(record, dict):
            raise ValueError('Expected an object record')
        result = results[check['id']]
        result['records_checked'] += 1
        value = record.get(check['field'])
        if any(type(value) is type(wanted) and value == wanted for wanted in check['values']):
            result['matches'].append({'file': source, 'pointer': h.pointer(parts),
                                      'field': check['field'], 'value': value, 'record': record})

    receipts = []
    for (service, rel), job in jobs.items():
        grouped = defaultdict(list)
        for check in job['checks']:
            grouped[h.parse_pointer(check['pointer'])].append(check)
        prefixes = list(grouped)
        for prefix in prefixes:
            if any(prefix != other and prefix[:len(other)] == other for other in prefixes):
                raise ValueError('Overlapping record arrays require separate requests')
        try:
            folder, info = job['folder'], job['info']
            before = batch.fingerprint(h, folder, [info])
            path = h.safe_file(folder, rel)
            source = path.relative_to(h.ROOT).as_posix()
            receipts.append({'file': source, 'manifest_sha256': info.get('sha256'),
                             'freshness': before})
            if path.stat().st_size <= threshold:
                with path.open(encoding='utf-8-sig') as handle:
                    data = json.load(handle, object_pairs_hook=batch.unique_object)
                for prefix, group in grouped.items():
                    try:
                        records = at_pointer(data, prefix)
                        for i, record in enumerate(records):
                            for check in group:
                                accept(check, record, prefix + (str(i),), source)
                        for check in group:
                            results[check['id']]['files_completed'] += 1
                    except ValueError as error:
                        for check in group:
                            result = results[check['id']]
                            result['scan_complete'] = False
                            result['errors'].append({'file': rel, 'error': str(error)})
            else:
                seen = set()
                iterator = strict_events(path, threshold)
                try:
                    for event, parts, value in iterator:
                        if parts in grouped and event != 'end':
                            if event != 'array':
                                raise ValueError('Expected an array at ' + h.pointer(parts))
                            seen.add(parts)
                        if parts and parts[:-1] in grouped and event != 'end':
                            if event != 'object':
                                raise ValueError('Expected an object record')
                            record = json.loads(''.join(h.render_subtree((event, parts, value), iterator)),
                                                object_pairs_hook=batch.unique_object)
                            for check in grouped[parts[:-1]]:
                                accept(check, record, parts, source)
                finally:
                    iterator.close()
                for prefix, group in grouped.items():
                    for check in group:
                        result = results[check['id']]
                        if prefix in seen:
                            result['files_completed'] += 1
                        else:
                            result['scan_complete'] = False
                            result['errors'].append({'file': rel, 'error': 'Record array pointer not found'})
            if before != batch.fingerprint(h, folder, [info]):
                raise ValueError('Source changed during the read')
        except (OSError, ValueError, UnicodeError, RecursionError) as error:
            for check in job['checks']:
                result = results[check['id']]
                result['scan_complete'] = False
                result['errors'].append({'file': rel, 'error': str(error)[:300]})
    if not manifests_unchanged(manifest_paths, manifest_states):
        for result in results.values():
            result['scan_complete'] = False
            result['errors'].append({'error': 'Source manifest changed during the read'})
    scanned_files = len(receipts)
    current = None
    if initial is not None:
        try:
            current = check_snapshot(all_jobs, manifest_paths)
        except (OSError, ValueError):
            pass
        for check in checks:
            if check['id'] in reusable:
                canonical, path, binding, keys, required = bindings[check['id']]
                if current is None or binding != individual_binding(canonical, threshold, keys, required, current):
                    results[check['id']]['scan_complete'] = False
                    results[check['id']]['errors'].append({'error': 'Cached source changed during the operation'})
    by_source = {**cached_sources, **{row['file']: row for row in receipts}}
    receipts = [by_source[source] for key, job in all_jobs.items()
                if (source := (job['folder'] / job['info']['path']).relative_to(h.ROOT).as_posix()) in by_source]
    result = {'checks': results, 'files_read_this_call': scanned_files, 'sources': receipts,
            'scan_complete': all(r['scan_complete'] for r in results.values()),
            'persona_filtered': False, 'backend': 'record-check-cache' if reusable and not scanned_files else 'grouped-record-scan',
            'scope_note': 'Exact direct fields in selected arrays. No SQL is applied. '
                          'Absence/uniqueness is supported only within complete declared scopes. '
                          'Manifest hashes are declared provenance, not fresh full-content hashes.'}
    if reusable:
        result['checks_reused'] = list(reusable)
    if current is not None and manifests_unchanged(manifest_paths, manifest_states):
        for check in checks:
            data = bindings.get(check['id'])
            if data is None:
                continue
            canonical, path, binding, keys, required = data
            one = {**result, 'checks': {'check': {**results[check['id']], 'scope': canonical}},
                   'scan_complete': results[check['id']]['scan_complete'],
                   'sources': [row for row in receipts if row['file'] in
                               {(all_jobs[key]['folder'] / all_jobs[key]['info']['path']).relative_to(h.ROOT).as_posix()
                                for key in keys}]}
            if complete_result(one, [canonical]) and binding == individual_binding(canonical, threshold, keys, required, current):
                try:
                    write_record_cache(path, binding, one)
                    trim_cache(path.parent)
                except (OSError, ValueError, AttributeError, NotImplementedError):
                    pass
    if signature is not None and complete_result(result, checks):
        try:
            if (signature == cache_signature(request, threshold, all_jobs, manifest_paths)
                    and manifests_unchanged(manifest_paths, manifest_states)):
                write_record_cache(cache, signature, result)
                trim_cache(cache.parent)
        except (OSError, ValueError, KeyError, TypeError, AttributeError, NotImplementedError):
            pass
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--request', required=True, help='JSON checks with explicit source paths/pointers')
    parser.add_argument('--no-cache', action='store_true', help='Read sources even for a fresh cached request')
    args = parser.parse_args()
    try:
        result = run(json.loads(open(args.request, encoding='utf-8').read(),
                                object_pairs_hook=batch.unique_object), no_cache=args.no_cache)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({'error': str(error), 'scan_complete': False}))
        return 1
    print(json.dumps(result, ensure_ascii=False, separators=(',', ':')))
    return 0 if result['scan_complete'] else 1


if __name__ == '__main__':
    sys.exit(main())
