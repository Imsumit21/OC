def mtext(m):
    t = m.get('text') or ''
    if not t.strip() and m.get('attachments'):
        t = ' / '.join(((a.get('title') or '') + ' ' + (a.get('text') or a.get('fallback') or '')).strip() for a in m['attachments'])
    return t
