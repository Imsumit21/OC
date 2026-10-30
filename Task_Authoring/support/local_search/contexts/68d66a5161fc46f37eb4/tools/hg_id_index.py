#!/usr/bin/env python3
"""Prepared exact-string identity indexes; never build implicitly during review."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

import hg_compact_index as compact
import hg_search_batch as batch

VERSION = 'exact-string-identities-v1'
FIELDS = ('id', 'identifier', 'sha', 'email', 'login')
MAX_BYTES = 8 * 1024 * 1024


def build(h, service, rel):
    """Explicit packaging operation. Validate all JSON, including unrelated keys."""
    folder, info, source, signature = compact.source(h, service, rel)
    raw = source.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if info.get('sha256') != digest:
        raise ValueError('Source manifest does not match actual bytes')
    data = json.loads(raw, object_pairs_hook=batch.unique_object)
    arrays = {'': data} if isinstance(data, list) else {
        h.pointer((key,)): value for key, value in data.items() if isinstance(value, list)
    } if isinstance(data, dict) else {}
    collections = {}
    for pointer, rows in arrays.items():
        if any(not isinstance(row, dict) for row in rows):
            continue  # This collection must use the ordinary shape-checking scan.
        fields = {field: {} for field in FIELDS}
        for ordinal, row in enumerate(rows):
            for field in FIELDS:
                value = row.get(field)
                if isinstance(value, str):
                    fields[field].setdefault(value, []).append(ordinal)
        collections[pointer] = {'count': len(rows), 'fields': fields}
    if signature != compact.source_signature(h, folder, info):
        raise ValueError('Source changed during identity index build')
    return {'version': VERSION, 'service': service, 'file': rel,
            'source_sha256': digest, 'strict_full_json_validation': True,
            'collections': collections}


def package(h, service, rel):
    payload = build(h, service, rel)
    raw = json.dumps(payload, ensure_ascii=False, separators=(',', ':')).encode()
    if len(raw) > MAX_BYTES:
        raise ValueError('Identity index exceeds portable size cap')
    folder = h.ROOT / 'Evals/references/id_indexes'
    folder.mkdir(parents=True, exist_ok=True)
    filename = batch.digest([service, rel]) + '.json'
    (folder / filename).write_bytes(raw)
    path = folder / 'manifest.json'
    manifest = json.loads(path.read_text()) if path.exists() else {'version': VERSION, 'indexes': []}
    if manifest['version'] != VERSION:
        raise ValueError('Incompatible identity index package')
    manifest['indexes'] = [entry for entry in manifest['indexes']
                           if (entry['service'], entry['file']) != (service, rel)]
    entry = {'service': service, 'file': rel, 'path': filename,
             'source_sha256': payload['source_sha256'], 'sha256': hashlib.sha256(raw).hexdigest()}
    manifest['indexes'].append(entry)
    path.write_text(json.dumps(manifest, indent=2) + '\n')
    return {**entry, 'bytes': len(raw), 'collections': len(payload['collections'])}


def load(h, service, rel, entry, package_path):
    directory = package_path.parent
    artifact = (directory / entry['path']).resolve()
    artifact.relative_to(directory.resolve())
    compact.watch_manifest(artifact)
    compact.watch_manifest(Path(__file__))
    folder, info, source, signature = compact.source(h, service, rel)
    binding = [VERSION, signature, compact.stat_signature(package_path),
               compact.stat_signature(artifact), compact.content_sha256(Path(__file__))]
    if entry['source_sha256'] != info.get('sha256'):
        raise ValueError('Identity index disagrees with source manifest')
    if artifact.stat().st_size > MAX_BYTES:
        raise ValueError('Oversized identity index')
    raw = artifact.read_bytes()
    if hashlib.sha256(raw).hexdigest() != entry['sha256']:
        raise ValueError('Identity index differs from pinned package')
    data = json.loads(raw, object_pairs_hook=batch.unique_object)
    if (data.get('version') != VERSION or data.get('service') != service
            or data.get('file') != rel or data.get('source_sha256') != entry['source_sha256']
            or data.get('strict_full_json_validation') is not True):
        raise ValueError('Incompatible or unvalidated identity index')
    cache = compact.compact_cache(h, VERSION, [service, rel])
    saved = batch.read_cache(cache, binding)
    if saved is not None and saved.get('rejected') is True:
        raise ValueError('Identity index does not match source bytes')
    hashed_bytes = 0
    if saved != {'validated': True}:
        hashed_bytes = source.stat().st_size
        valid = compact.content_sha256(source) == entry['source_sha256']
        if signature != compact.source_signature(h, folder, info):
            raise ValueError('Source changed during identity index validation')
        compact.write_cache(cache, binding, {'validated': True} if valid else {'rejected': True})
        if not valid:
            raise ValueError('Identity index does not match source bytes')
    return source, data, hashed_bytes


@compact.manifest_operation(fallback=True)
def lookup(h, service, ids, pattern, pointer, key):
    """Return complete indexed evidence, or None so the strict scanner runs."""
    if key not in FIELDS:
        return None
    path = h.ROOT / 'Evals/references/id_indexes/manifest.json'
    if not path.exists():
        return None
    compact.watch_manifest(path)
    manifest = json.loads(path.read_text(), object_pairs_hook=batch.unique_object)
    if manifest['version'] != VERSION:
        return None
    folder, files = compact.structured_info(h, service)
    selected = list(h.candidates(files, pattern))
    if not selected:
        return None
    wanted = sorted(set(ids))
    result = {'matches': {value: [] for value in wanted}, 'files_selected': len(selected),
              'files_completed': 0, 'records_checked': 0, 'errors': [],
              'scan_complete': True, 'persona_filtered': False,
              'scope': {'service': service, 'file_pattern': pattern, 'records_pointer': pointer,
                        'record_shape': 'array of objects', 'field': key,
                        'match': 'exact case-sensitive string'},
              'backend': 'verified-id-index', 'files_read_this_call': 0,
              'source_bytes_hashed_this_call': 0,
              'duplicate_requested_ids': sorted(v for v, n in Counter(ids).items() if n > 1)}
    for info in selected:
        entries = [entry for entry in manifest['indexes']
                   if entry['service'] == service and entry['file'] == info['path']]
        if len(entries) != 1:
            return None  # Never certify absence from a partially indexed glob.
        source, data, hashed_bytes = load(h, service, info['path'], entries[0], path)
        result['source_bytes_hashed_this_call'] += hashed_bytes
        collection = data['collections'].get(pointer)
        if collection is None or type(collection['count']) is not int or collection['count'] < 0:
            return None
        field = collection['fields'][key]
        for value in wanted:
            ordinals = field.get(value, [])
            if (not isinstance(ordinals, list) or any(type(n) is not int or not 0 <= n < collection['count'] for n in ordinals)
                    or ordinals != sorted(set(ordinals))):
                return None
            result['matches'][value].extend({'file': source.relative_to(h.ROOT).as_posix(),
                'pointer': h.pointer(h.parse_pointer(pointer) + (str(n), key)), 'value': value}
                for n in ordinals)
        result['records_checked'] += collection['count']
        result['files_completed'] += 1
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('service')
    parser.add_argument('--file', required=True)
    args = parser.parse_args()
    import hg_search as h
    print(json.dumps(package(h, args.service, args.file)))


if __name__ == '__main__':
    main()
