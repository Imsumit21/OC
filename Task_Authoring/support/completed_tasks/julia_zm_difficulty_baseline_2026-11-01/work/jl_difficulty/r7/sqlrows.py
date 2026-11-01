"""Parse the injection SQL into rows: {id: {'table':..., col: value}} (INSERT ... VALUES (...); one row each)."""
import re


def _values(s, i):
    out, cur, n = [], None, len(s)
    assert s[i] == '('
    i += 1
    while i < n:
        c = s[i]
        if c in ' \n\t,':
            i += 1
            continue
        if c == ')':
            return out, i + 1
        if c == 'E' and s[i + 1] == "'":
            i += 1
            c = "'"
            esc = True
        else:
            esc = False
        if c == "'":
            j = i + 1
            buf = []
            while True:
                ch = s[j]
                if ch == "'" and s[j + 1:j + 2] == "'":
                    buf.append("'"); j += 2; continue
                if ch == "'":
                    break
                if esc and ch == '\\' and j + 1 < n:
                    nx = s[j + 1]
                    buf.append({'n': '\n', 't': '\t', '\\': '\\', "'": "'"}.get(nx, '\\' + nx)); j += 2; continue
                buf.append(ch); j += 1
            out.append(''.join(buf)); i = j + 1
        else:
            m = re.match(r"[^,)]+", s[i:])
            tok = m.group(0).strip()
            out.append(None if tok == 'NULL' else tok)
            i += len(m.group(0))
    raise ValueError('unterminated')


def load_all(path):
    s = open(path).read()
    out = []
    for m in re.finditer(r"INSERT INTO ([\w.]+) \(([^)]*)\)\s*VALUES\s*", s):
        cols = [c.strip().strip('"') for c in m.group(2).split(',')]
        vals, _ = _values(s, m.end())
        r = dict(zip(cols, vals)); r['table'] = m.group(1); out.append(r)
    return out


def load(path):
    s = open(path).read()
    rows = {}
    for m in re.finditer(r"INSERT INTO ([\w.]+) \(([^)]*)\)\s*VALUES\s*", s):
        cols = [c.strip().strip('"') for c in m.group(2).split(',')]
        vals, _ = _values(s, m.end())
        r = dict(zip(cols, vals)); r['table'] = m.group(1)
        key = r.get(cols[0])
        rows.setdefault(key, r) if key not in rows else rows.setdefault(f"{key}@{r['table']}", r)
    return rows


if __name__ == '__main__':
    import sys, collections
    R = load(sys.argv[1])
    print(len(R), collections.Counter(r['table'] for r in R.values()).most_common())
