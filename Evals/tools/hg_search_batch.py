"""Batched literal searches and exact ID lookups; source exports are read-only."""
import hashlib
import json
import os
from pathlib import Path
from collections import Counter
import sys
import tempfile
import time


class Pairs(list):
    """Preserve object order and duplicate keys, distinguish objects from arrays."""


def walk(value, parts=()):
    if isinstance(value, Pairs):
        yield 'object',parts,None
        for key,item in value:
            yield from walk(item,parts+(key,))
        yield 'end',parts,None
    elif isinstance(value,list):
        yield 'array',parts,None
        for i,item in enumerate(value):
            yield from walk(item,parts+(str(i),))
        yield 'end',parts,None
    else:
        yield 'value',parts,value


def events(h,path,threshold):
    if path.stat().st_size <= threshold:
        try:
            with path.open(encoding='utf-8-sig') as f:
                data=json.load(f,object_pairs_hook=Pairs)
        except (ValueError,UnicodeError,RecursionError):
            pass
        else:
            yield from walk(data)
            return
    with path.open(encoding='utf-8-sig') as f:
        stream=h.Stream(f)
        yield from stream.events()
        if stream.peek():
            raise ValueError('Trailing content after JSON value')


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True).encode()).hexdigest()


def cache_file(root, kind, request):
    import hg_universe
    folder = root / 'Evals/.cache/queries'
    folder.resolve().relative_to(root.resolve())
    path = folder / (digest([kind, request, hg_universe.selected(root)]) + '.json')
    if path.is_symlink():
        raise OSError('Query cache must not be a symbolic link')
    return path


def read_cache(path, signature):
    if path is None or signature is None:
        return None
    try:
        if path.stat().st_size > 8 * 1024 * 1024:
            return None
        saved = json.loads(path.read_text())
        if (saved['signature'] == signature and isinstance(saved['result'], dict)
                and saved['checksum'] == digest(saved['result'])):
            return saved['result']
    except (OSError, ValueError, KeyError, TypeError):
        pass
    return None


def write_cache(path, signature, result):
    if path is None:
        return
    tmp = None
    try:
        payload = json.dumps({'signature': signature, 'result': result, 'checksum': digest(result)})
        if len(payload.encode()) > 8 * 1024 * 1024:
            return  # Large result sets remain usable without a disk cache.
        path.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(mode='w', dir=path.parent, delete=False) as f:
            tmp = Path(f.name)
            f.write(payload)
        os.replace(tmp, path)
    except OSError as error:
        result['cache_warning'] = str(error)
    finally:
        if tmp is not None:
            tmp.unlink(missing_ok=True)


def validate_request(request):
    if not isinstance(request, dict) or not isinstance(request.get('queries'), list):
        raise ValueError('Expected an object with service, optional file, and a queries array')
    allowed = {'id', 'query', 'limit', 'key', 'pointer', 'case_sensitive'}
    for query in request['queries']:
        if not isinstance(query, dict) or set(query) - allowed:
            raise ValueError('Each query uses id, query, limit, key, pointer and case_sensitive only')
        if not isinstance(query.get('id'), str) or not query['id']:
            raise ValueError('Every query needs a nonempty string id')
        if not isinstance(query.get('query'), str) or not query['query']:
            raise ValueError('Every query needs nonempty query text')
        limit = query.get('limit', 20)
        if type(limit) is not int or limit < 1:
            raise ValueError('Query limits must be positive integers')
        for key in ('key', 'pointer'):
            if key in query and not isinstance(query[key], str):
                raise ValueError(key + ' must be a string')
        if 'case_sensitive' in query and type(query['case_sensitive']) is not bool:
            raise ValueError('case_sensitive must be a boolean')
    if not isinstance(request.get('service'), str):
        raise ValueError('service must be a string')
    if request.get('file') is not None and not isinstance(request['file'], str):
        raise ValueError('file must be a service-relative glob string')


def fingerprint(h,folder,selected):
    rows=[]
    for info in selected:
        path=h.safe_file(folder,info['path']); s=path.stat()
        rows.append([info,str(path),s.st_dev,s.st_ino,s.st_size,s.st_mtime_ns,s.st_ctime_ns])
    return digest(rows)


def search_many(h,request,no_cache=False,threshold=8*1024*1024,progress=False):
    validate_request(request)
    root=h.ROOT; service=request['service']
    folder,records=h.service_info(service)
    selected=list(h.candidates(records,request.get('file')))
    if not selected:
        raise ValueError('No structured JSON files match; use files to inspect paths')
    queries=request['queries']
    if not queries or len({q['id'] for q in queries})!=len(queries):
        raise ValueError('Supply unique query IDs')
    state={};prefixes={};folded={}
    for q in queries:
        key=q['id']
        if not q['query'] or q.get('limit',20)<1:
            raise ValueError('Query and positive limit required')
        prefixes[key]=h.parse_pointer(q.get('pointer',''))
        folded[key]=q['query'] if q.get('case_sensitive') else q['query'].casefold()
        state[key]={'matches':[],'files_selected':len(selected),'files_started':0,
                    'files_completed':0,'scan_complete':True,'errors':[],
                    'persona_filtered':False,
                    'scope':'JSON scalar values; excludes root/ blobs and non-JSON attachments'}
    try: cache=cache_file(root, 'batch-text-v1', request)
    except (OSError, ValueError): cache=None
    before=None
    try: before=fingerprint(h,folder,selected)
    except (OSError,ValueError): pass
    saved = read_cache(cache, before) if not no_cache else None
    if saved is not None:
        return {**saved, 'backend':'query-cache', 'files_read_this_call':0}
    active=[];physical_files=0;last_progress=0;indexed_count=0;read_paths=set()
    # A broad query already needs the common scan. Keep that whole batch in
    # one pass rather than repeating large overlapping subtrees per query.
    scoped_batch = all(len(prefixes[q['id']]) >= 2 for q in queries)
    if scoped_batch and hasattr(h, 'prefer_compact_batch'):
        scoped_batch = h.prefer_compact_batch(service, request.get('file'), queries)
    for q in queries:
        indexed = (h.indexed_search(service, request.get('file'), q, progress)
                   if scoped_batch and hasattr(h, 'indexed_search') else None)
        if indexed is None:
            active.append(q)
        else:
            state[q['id']] = {k: v for k, v in indexed.items() if k != 'backend'}
            indexed_count += 1
            read_paths.update(info['path'] for info in selected[:indexed['files_started']])
    for info in selected:
        if not active: break
        for q in active: state[q['id']]['files_started']+=1
        physical_files+=1;read_paths.add(info['path']);now=time.monotonic()
        if progress and now-last_progress>=5:
            print(f'Scanning {service}: {physical_files}/{len(selected)} files; {len(active)} active queries',
                  file=sys.stderr,flush=True)
            last_progress=now
        try:
            path=h.safe_file(folder,info['path']);source=path.relative_to(h.ROOT).as_posix()
            iterator=events(h,path,threshold)
            try:
                for event,parts,value in iterator:
                    if event!='value': continue
                    relevant=[q for q in active if parts[:len(prefixes[q['id']])]==prefixes[q['id']]
                              and (not q.get('key') or (parts and parts[-1]==q['key']))]
                    if not relevant: continue
                    raw=value if isinstance(value,str) else json.dumps(value)
                    raw_folded=raw.casefold();decoded=decoded_folded=None;decoded_checked=False;finished=[]
                    for q in relevant:
                        key=q['id'];needle=folded[key];sensitive=q.get('case_sensitive',False)
                        if needle in (raw if sensitive else raw_folded):
                            matched,encoding=raw,'json'
                        else:
                            if not decoded_checked:
                                decoded=h.decoded_gmail(service,parts,value)
                                decoded_folded=decoded.casefold() if decoded is not None else None
                                decoded_checked=True
                            if decoded is None or needle not in (decoded if sensitive else decoded_folded): continue
                            matched,encoding=decoded,'base64url-utf8'
                        target=state[key]
                        target['matches'].append({'file':source,'service_file':info['path'],
                            'pointer':h.pointer(parts),'parent_pointer':h.pointer(parts[:-1]),
                            'encoding':encoding,**h.snippet(matched,q['query'],sensitive)})
                        if len(target['matches'])>=q.get('limit',20):
                            target['scan_complete']=False
                            target['stop_reason']='match limit reached; narrow by file/pointer/key or raise limit'
                            finished.append(key)
                    if finished: active=[q for q in active if q['id'] not in finished]
                    if not active: break
            finally: iterator.close()
            for q in active: state[q['id']]['files_completed']+=1
        except (OSError,ValueError,UnicodeError,RecursionError) as error:
            for q in active:
                target=state[q['id']];target['scan_complete']=False
                target['errors'].append({'file':info['path'],'error':str(error)[:300]})
    try: after=fingerprint(h,folder,selected)
    except (OSError,ValueError): after=None
    if before is None or before!=after:
        for target in state.values():
            target['scan_complete']=False;target['errors'].append({'error':'Source freshness could not be verified'})
    result={'queries':state,
            'backend':'batch-compact-offset' if indexed_count else 'batch-text-scan',
            'files_read_this_call':len(read_paths),
            'scope':{'service':service,'file_pattern':request.get('file')}}
    if not no_cache and before is not None and before==after and not any(q['errors'] for q in state.values()):
        write_cache(cache, before, result)
    return result


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON object key: ' + key)
        result[key] = value
    return result


def lookup(h, service, ids, pattern, pointer='', key='id', no_cache=False,
           threshold=8 * 1024 * 1024, progress=False):
    """Check exact string IDs in an explicitly selected array of records."""
    if not isinstance(ids, list) or not ids or not all(isinstance(v, str) and v for v in ids):
        raise ValueError('ids-file must contain a nonempty JSON array of nonempty string IDs')
    if not pattern:
        raise ValueError('Select the complete relevant collection with --file')
    prefix = h.parse_pointer(pointer)
    folder, records = h.service_info(service)
    selected = list(h.candidates(records, pattern))
    wanted = set(ids)
    request = {'service': service, 'file': pattern, 'pointer': pointer, 'key': key, 'ids': sorted(wanted)}
    result = {'matches': {v: [] for v in sorted(wanted)}, 'files_selected': len(selected),
              'files_completed': 0, 'records_checked': 0, 'errors': [],
              'scan_complete': bool(selected), 'persona_filtered': False,
              'scope': {'service': service, 'file_pattern': pattern, 'records_pointer': pointer,
                        'record_shape': 'array of objects', 'field': key,
                        'match': 'exact case-sensitive string'}}
    if not selected:
        result['errors'].append({'error': 'No matching source files'})
        return result
    try: cache = cache_file(h.ROOT, 'exact-ids-v1', request)
    except (OSError, ValueError): cache = None
    before = None
    try: before = fingerprint(h, folder, selected)
    except (OSError, ValueError): pass
    saved = read_cache(cache, before) if not no_cache else None
    duplicates = sorted(v for v, count in Counter(ids).items() if count > 1)
    if saved is not None:
        return {**saved, 'backend': 'query-cache', 'duplicate_requested_ids': duplicates,
                'files_read_this_call': 0}

    indexed_lookup = getattr(h, 'indexed_lookup', None)
    if not no_cache and callable(indexed_lookup):
        indexed = indexed_lookup(service, ids, pattern, pointer, key)
        if indexed is not None:
            return indexed

    def accept(value, parts, source):
        if isinstance(value, str) and value in wanted:
            result['matches'][value].append({'file': source, 'pointer': h.pointer(parts), 'value': value})

    last_progress = 0
    for number, info in enumerate(selected, 1):
        now = time.monotonic()
        if progress and now - last_progress >= 5:
            print(f'Checking {service} IDs: {number}/{len(selected)} files', file=sys.stderr, flush=True)
            last_progress = now
        try:
            path = h.safe_file(folder, info['path'])
            source = path.relative_to(h.ROOT).as_posix()
            if path.stat().st_size <= threshold:
                with path.open(encoding='utf-8-sig') as handle:
                    data = json.load(handle, object_pairs_hook=unique_object)
                for part in prefix:
                    if isinstance(data, dict) and part in data:
                        data = data[part]
                    elif isinstance(data, list) and part.isdecimal() and str(int(part)) == part and int(part) < len(data):
                        data = data[int(part)]
                    else:
                        raise ValueError('Record array pointer not found')
                if not isinstance(data, list):
                    raise ValueError('Expected an array at the record pointer')
                for index, record in enumerate(data):
                    if not isinstance(record, dict):
                        raise ValueError('Expected an object record')
                    result['records_checked'] += 1
                    accept(record.get(key), prefix + (str(index), key), source)
            else:
                seen_array = False
                fields = {}
                with path.open(encoding='utf-8-sig') as handle:
                    stream = h.Stream(handle)
                    for event, parts, value in stream.events():
                        if event == 'end':
                            fields.pop(parts, None)
                        elif parts and parts[:-1] in fields:
                            seen = fields[parts[:-1]]
                            if parts[-1] in seen:
                                raise ValueError('Duplicate JSON object key: ' + parts[-1])
                            seen.add(parts[-1])
                        if event == 'object': fields[parts] = set()
                        if parts == prefix and event != 'end':
                            if event != 'array': raise ValueError('Expected an array at the record pointer')
                            seen_array = True
                        if parts[:len(prefix)] != prefix: continue
                        if len(parts) == len(prefix) + 1:
                            if event not in ('object', 'end'): raise ValueError('Expected an object record')
                            if event == 'object': result['records_checked'] += 1
                        if event == 'value' and len(parts) == len(prefix) + 2 and parts[-1] == key:
                            accept(value, parts, source)
                    if not seen_array: raise ValueError('Record array pointer not found')
                    if stream.peek(): raise ValueError('Trailing content after JSON value')
            result['files_completed'] += 1
        except (OSError, ValueError, RecursionError) as error:
            result['scan_complete'] = False
            result['errors'].append({'file': info['path'], 'error': str(error)[:300]})
    try: after = fingerprint(h, folder, selected)
    except (OSError, ValueError): after = None
    if before is None or before != after:
        result['scan_complete'] = False
        result['errors'].append({'error': 'Source freshness could not be verified'})
    result.update(backend='batch-exact-id-scan', files_read_this_call=len(selected))
    if not no_cache and result['scan_complete']:
        write_cache(cache, before, result)
    result['duplicate_requested_ids'] = duplicates
    return result
