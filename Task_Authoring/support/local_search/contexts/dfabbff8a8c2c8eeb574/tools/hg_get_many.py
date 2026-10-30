"""Bounded batched reads, preserving existing get evidence and pagination."""
import argparse
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import hg_search as h
from hg_compact_index import manifest_operation


@manifest_operation(reuse_loads=True)
def get_many(request, progress=False):
    if not isinstance(request, dict) or set(request) != {'items'}:
        raise ValueError('Expected items array')
    items = request['items']
    if not isinstance(items, list) or not 1 <= len(items) <= 50:
        raise ValueError('Supply 1 to 50 reads')
    allowed = {'id', 'service', 'file', 'pointer', 'offset', 'max_chars', 'decode_base64'}
    seen = set()
    total = 0
    args = []
    for item in items:
        if not isinstance(item, dict) or set(item) - allowed:
            raise ValueError('Unknown read field')
        for field in ('id', 'service', 'file'):
            if not isinstance(item.get(field), str) or not item[field]:
                raise ValueError('Supply id, service and file strings')
        if item['id'] in seen:
            raise ValueError('Read IDs must be unique')
        seen.add(item['id'])
        pointer = item.get('pointer', '')
        if not isinstance(pointer, str):
            raise ValueError('pointer must be a string')
        h.parse_pointer(pointer)
        offset, limit = item.get('offset', 0), item.get('max_chars', 12000)
        if type(offset) is not int or offset < 0 or type(limit) is not int or limit < 1:
            raise ValueError('Invalid pagination')
        decode = item.get('decode_base64', False)
        if type(decode) is not bool:
            raise ValueError('decode_base64 must be boolean')
        total += limit
        args.append((item['id'], SimpleNamespace(service=item['service'], file=item['file'],
            pointer=pointer, offset=offset, max_chars=limit, decode_base64=decode,
            no_index=False, build_index=False, progress=progress)))
    if total > 600000:
        raise ValueError('Combined output limit exceeds 600000 characters')
    results = {}
    for key, arg in args:
        try:
            results[key] = h.get(arg)
        except (OSError, ValueError, UnicodeError, RecursionError) as error:
            results[key] = {'error': str(error), 'complete': False}
    return {'items': results,
            'complete': all(not v.get('error') and not v.get('truncated') for v in results.values())}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--request', required=True)
    parser.add_argument('--progress', action='store_true')
    parser.add_argument('--compact', action='store_true')
    opts = parser.parse_args()
    try:
        request = json.load(sys.stdin) if opts.request == '-' else json.loads(Path(opts.request).read_text())
        result = get_many(request, progress=opts.progress)
        print(json.dumps(result, ensure_ascii=False, indent=None if opts.compact else 2))
        raise SystemExit(1 if any(v.get('error') for v in result['items'].values()) else 0)
    except (ValueError, OSError, RecursionError) as error:
        print(json.dumps({'error': str(error), 'complete': False}), file=sys.stderr)
        raise SystemExit(1)
