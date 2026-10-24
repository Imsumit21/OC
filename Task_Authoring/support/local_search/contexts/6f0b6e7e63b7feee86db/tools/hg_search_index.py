"""Disposable per-service SQLite search/offset cache; never edits source records."""
import hashlib
import json
from pathlib import Path
import sqlite3
import time
import os
import tempfile

FORMAT_VERSION = 1


class IndexNotReady(Exception):
    """An absent/stale index is an ordinary reason to scan the source."""


def cache_path(root, service, folder):
    root, folder = Path(root), Path(folder)
    cache = root / 'Task_Authoring/support/local_search/contexts/6f0b6e7e63b7feee86db/cache/search'
    cache.resolve().relative_to(root.resolve())
    identity = json.dumps([FORMAT_VERSION, service, str(folder.resolve())])
    digest = hashlib.sha256(identity.encode()).hexdigest()[:24]
    label = ''.join(c for c in service if c.isascii() and (c.isalnum() or c == '-'))[:32]
    path = cache / f'{label}-{digest}.sqlite3'
    if path.is_symlink():
        raise ValueError('Search cache must not be a symbolic link')
    return path


def cache_failure(root, service, folder, error=None, clear=False):
    """Bound retries across CLI invocations; explicit index work can retry now."""
    try:
        path = cache_path(root, service, folder).with_suffix('.unavailable.json')
        if path.is_symlink(): return None
        if clear:
            path.unlink(missing_ok=True)
        elif error is not None:
            path.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(mode='w', dir=path.parent, delete=False) as f:
                json.dump({'until': time.time() + 300, 'error': str(error)[:300]}, f)
                tmp = Path(f.name)
            try: os.replace(tmp, path)
            finally: tmp.unlink(missing_ok=True)
        elif path.exists():
            data = json.loads(path.read_text())
            if data['until'] > time.time(): return data['error']
    except (OSError, ValueError, KeyError, TypeError):
        pass
    return None


class SearchIndex:
    def __init__(self, root, service, folder, records, stream, pointer, decode, progress=None, rebuild=False, readonly=False):
        self.root, self.service, self.folder = Path(root), service, Path(folder)
        self.stream, self.pointer, self.decode = stream, pointer, decode
        self.progress, self.last_progress = progress, 0
        self.built = self.reused = 0
        self.readonly = readonly
        self.writer = None
        self.db = None
        self.path = cache_path(self.root, service, self.folder)
        try:
            if readonly:
                if not self.path.is_file(): raise IndexNotReady('No existing index')
                self.db = sqlite3.connect(self.path.as_uri() + '?mode=ro', uri=True, timeout=0.2)
                self.db.row_factory = sqlite3.Row
                self.trigram = bool(self.db.execute("SELECT 1 FROM sqlite_master WHERE name='grams'").fetchone())
                return
            self.path.parent.mkdir(parents=True, exist_ok=True)
            # One writer per service, including schema initialization. Never wait
            # indefinitely or launch another competing build in a second CLI.
            import fcntl
            lock = self.path.with_suffix('.writer.lock')
            if lock.is_symlink(): raise ValueError('Index lock must not be a symbolic link')
            self.writer = lock.open('a')
            try: fcntl.flock(self.writer, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError: raise sqlite3.OperationalError('database is locked: another index writer is active')
            if rebuild and self.path.exists(): self._recover_corruption()
            self.db = sqlite3.connect(self.path, timeout=0.2)
            self.db.row_factory = sqlite3.Row
            self.db.execute('PRAGMA journal_mode=WAL')
            self.db.execute('PRAGMA synchronous=NORMAL')
            self.db.execute('PRAGMA foreign_keys=ON')
            self.db.execute('PRAGMA cache_size=-8192')
            self.db.executescript('''
                CREATE TABLE IF NOT EXISTS files (
                    id INTEGER PRIMARY KEY, path TEXT UNIQUE NOT NULL,
                    signature TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS nodes (
                    id INTEGER PRIMARY KEY, file_id INTEGER NOT NULL REFERENCES files(id),
                    pointer TEXT NOT NULL, field TEXT, kind TEXT NOT NULL,
                    byte_offset INTEGER NOT NULL, raw TEXT, decoded TEXT, search_text TEXT);
                CREATE INDEX IF NOT EXISTS nodes_pointer ON nodes(file_id, pointer, id);
                CREATE INDEX IF NOT EXISTS nodes_field ON nodes(file_id, field, id);
                CREATE INDEX IF NOT EXISTS nodes_file ON nodes(file_id, id);
            ''')
            self.trigram = self._fts()
            current = {record['path'] for record in records}
            with self.db:
                for row in self.db.execute('SELECT id, path FROM files').fetchall():
                    if row['path'] not in current:
                        self.db.execute('DELETE FROM nodes WHERE file_id=?', (row['id'],))
                        self.db.execute('DELETE FROM files WHERE id=?', (row['id'],))
        except BaseException:
            if self.db is not None: self.db.close()
            if self.writer is not None: self.writer.close()
            raise

    def _recover_corruption(self):
        """Explicit rebuild can discard a broken disposable database."""
        check = sqlite3.connect(self.path, timeout=5)
        try:
            bad = check.execute('PRAGMA quick_check').fetchone()[0] != 'ok'
        except sqlite3.DatabaseError as error:
            if getattr(error, 'sqlite_errorcode', None) not in (sqlite3.SQLITE_CORRUPT, sqlite3.SQLITE_NOTADB):
                raise
            bad = True
        finally:
            check.close()
        if bad:
            for suffix in ('', '-wal', '-shm'):
                Path(str(self.path) + suffix).unlink(missing_ok=True)

    def _fts(self):
        # An external-content trigram index stores postings, not another copy of
        # the corpus. Casefold before indexing, then verify every candidate with
        # the original matcher (including punctuation, Unicode and short IDs).
        exists = self.db.execute("SELECT 1 FROM sqlite_master WHERE name='grams'").fetchone()
        try:
            self.db.execute("CREATE VIRTUAL TABLE IF NOT EXISTS grams USING fts5(search_text, content='nodes', content_rowid='id', tokenize='trigram case_sensitive 1', detail='none')")
        except sqlite3.OperationalError as error:
            if 'no such module' in str(error) or 'tokenizer' in str(error):
                return False
            raise
        self.db.executescript('''
            CREATE TRIGGER IF NOT EXISTS nodes_insert AFTER INSERT ON nodes
            WHEN new.search_text IS NOT NULL BEGIN
                INSERT INTO grams(rowid, search_text) VALUES (new.id, new.search_text);
            END;
            CREATE TRIGGER IF NOT EXISTS nodes_delete AFTER DELETE ON nodes
            WHEN old.search_text IS NOT NULL BEGIN
                INSERT INTO grams(grams, rowid, search_text)
                VALUES ('delete', old.id, old.search_text);
            END;
        ''')
        if not exists:
            self.db.execute("INSERT INTO grams(grams) VALUES ('rebuild')")
        self.db.commit()
        return True

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.db.close()
        if self.writer is not None: self.writer.close()

    @staticmethod
    def signature(path, info):
        stat = path.stat()
        return json.dumps([str(path.resolve()), stat.st_dev, stat.st_ino,
                           stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns,
                           info.get('sha256')], separators=(',', ':'))

    def check_signature(self, path, info, expected):
        if self.signature(path, info) != expected:
            raise OSError('Source changed during indexed read: ' + info['path'])

    def ensure(self, path, info, force=False):
        signature = self.signature(path, info)
        row = self.db.execute('SELECT id, signature FROM files WHERE path=?', (info['path'],)).fetchone()
        if row and row['signature'] == signature and not force:
            self.reused += 1
            return row['id'], signature
        if self.readonly:
            raise IndexNotReady('Selected source is not indexed at its current version')
        now = time.monotonic()
        if self.progress and now - self.last_progress >= 5:
            self.progress(f'Indexing {self.service}/{info["path"]}; subsequent reads reuse this cache.')
            self.last_progress = now
        # Build a file in one transaction. Interrupted/failed builds are never
        # visible as complete. Writers serialize; readers can use committed data.
        self.db.execute('BEGIN IMMEDIATE')
        try:
            self.db.execute('INSERT INTO files(path, signature) VALUES (?, ?) ON CONFLICT(path) DO NOTHING', (info['path'], signature))
            file_id = self.db.execute('SELECT id FROM files WHERE path=?', (info['path'],)).fetchone()[0]
            self.db.execute('DELETE FROM nodes WHERE file_id=?', (file_id,))
            with path.open('rb') as source:
                bom = 3 if source.read(3) == b'\xef\xbb\xbf' else 0
            with path.open(encoding='utf-8-sig', newline='') as source:
                parser = self.stream(source, track_offsets=True, byte_offset=bom)
                batch = []
                batch_chars = 0
                for event, parts, value in parser.events():
                    if event == 'end':
                        continue
                    raw = decoded = folded = None
                    if event == 'value':
                        raw = value if isinstance(value, str) else json.dumps(value)
                        decoded = self.decode(self.service, parts, value)
                        folded = raw.casefold()
                        if decoded is not None:
                            folded += '\n' + decoded.casefold()
                        # FTS tokenizers stop at NUL. Preserve the raw values for
                        # verification, but keep text after NUL searchable too.
                        folded = folded.replace('\x00', '\n')
                    batch.append((file_id, self.pointer(parts), parts[-1] if parts else None,
                                  event, parser.event_offset, raw, decoded, folded))
                    batch_chars += sum(len(v) for v in (raw, decoded, folded) if v is not None)
                    if len(batch) >= 500 or batch_chars >= 1048576:
                        self._insert(batch)
                        batch.clear()
                        batch_chars = 0
                if parser.peek():
                    raise ValueError('Trailing content after JSON value')
                self._insert(batch)
            self.check_signature(path, info, signature)
            self.db.execute('UPDATE files SET signature=? WHERE id=?', (signature, file_id))
            self.db.commit()
        except BaseException:
            self.db.rollback()
            raise
        self.built += 1
        return file_id, signature

    def _insert(self, batch):
        self.db.executemany('INSERT INTO nodes(file_id,pointer,field,kind,byte_offset,raw,decoded,search_text) VALUES (?,?,?,?,?,?,?,?)', batch)

    def matches(self, file_id, prefix, key, query):
        sql = "SELECT pointer, raw, decoded FROM nodes WHERE file_id=? AND kind='value'"
        params = [file_id]
        if prefix:
            sql += ' AND (pointer=? OR instr(pointer,?)=1)'
            params.extend([prefix, prefix + '/'])
        if key:
            sql += ' AND field=?'
            params.append(key)
        folded = query.casefold()
        if self.trigram and len(folded) >= 3 and '\x00' not in folded:
            # A bounded set of mandatory trigrams is a candidate filter only.
            # Exact snippet matching in hg_search remains the authority.
            end = len(folded) - 3
            starts = sorted({end * i // 7 for i in range(8)})
            grams = sorted({folded[i:i+3] for i in starts})
            expression = ' AND '.join('"' + gram.replace('"', '""') + '"' for gram in grams)
            sql += ' AND id IN (SELECT rowid FROM grams WHERE grams MATCH ?)'
            params.append(expression)
        elif '\x00' not in folded:
            # Short queries and Python builds without trigram support still use
            # cached scalar text; no JSON reparse is necessary.
            sql += ' AND instr(search_text,?)>0'
            params.append(folded)
        sql += ' ORDER BY id'
        yield from self.db.execute(sql, params)

    def locate(self, file_id, pointer):
        return self.db.execute('SELECT kind, byte_offset FROM nodes WHERE file_id=? AND pointer=? ORDER BY id LIMIT 1', (file_id, pointer)).fetchone()

    def metadata(self):
        return {'backend': 'sqlite-trigram' if self.trigram else 'sqlite-scan',
                'cache': {'path': self.path.relative_to(self.root).as_posix(),
                          'files_built': self.built, 'files_reused': self.reused,
                          'freshness': 'source path, device/inode, size, mtime_ns, ctime_ns and manifest SHA-256'}}
