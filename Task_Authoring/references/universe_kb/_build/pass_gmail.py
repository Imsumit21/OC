"""One pass over all Gmail thread files (one file at a time) -> kb_cache/kb_gmail.json."""
import os, re, json, collections, datetime
from email.utils import parseaddr, getaddresses
from common import *

TD = GMAIL + "/threads"
RE_PREFIX = re.compile(r"^((re|fwd?|fw|aw)\s*:\s*)+", re.I)
CAL = re.compile(r"^(Updated invitation with note|Updated invitation|Invitation from Google Calendar|Invitation|Accepted|Declined|Tentatively accepted|Canceled event with note|Canceled event|Event canceled|New event)\s*:\s*(.+?) @ (.+?)(?:\s*\(([^()]*@[^()]*|[A-Z_0-9]+_EMAIL)\))?\s*$")
HELP = re.compile(r"New (.+?) (iOS|Android|Web)?\s*issue #(\d+)", re.I)
GHMAIL = re.compile(r"\[(?:harmonygames|\[SOURCE_ORG_\d+\])-Games/([^\]]+)\].*?\((PR|Issue) #(\d+)\)")
DIST = re.compile(r"Version (\d+(?:\.\d+)*) \((\d+)\) of (.+?) for (Android|iOS) Available")
TFLIGHT = re.compile(r"^(.+?) (\d+(?:\.\d+)*) \((\d+)\) for (iOS|tvOS|macOS) is now available to test")
RED_ANY = re.compile(r"\[[A-Z_]+_\d+\]|\b[A-Z]+_\d+_[A-Z_]+\b|[\w.+-]+@[\w-]+\.[\w.]+|<[^>]*>|\s+")
APPSTORE = re.compile(r"(Review of your (.+?) submission is complete|The status of your .+? is now|is now available to test|is ready (?:to test|for (?:review|sale|distribution))|submission (?:is complete|was rejected)|App Store Connect)", re.I)
CRASH = re.compile(r"Trending stability issues|Crashlytics|velocity alert|new fatal issue|regressed issue", re.I)
QUOTE_CUT = re.compile(r"(\r?\n>|\r?\nOn .{5,120}wrote:|\r?\n-{2,}\s*Original Message|\r?\n-{5,} Forwarded message)", re.S)
GREET = re.compile(r"^\s*(hi|hey|hello|dear|good (morning|afternoon)|team|all)\b", re.I)
SIGN = re.compile(r"\n\s*(best|thanks|thank you|cheers|regards|best regards|kind regards|thx)\b[ ,!.]*\r?\n", re.I)


def email_of(s):
    a = parseaddr(s or "")[1].lower()
    if not a:
        m = re.search(r"([A-Z]+_\d+_EMAIL|[\w.+-]+@[\w.-]+)", s or "")
        a = m.group(1).lower() if m else ""
    return a


def subj_pattern(s):
    s = RE_PREFIX.sub("", s or "").strip()
    s = re.sub(r"\[harmonygames-Games/[^\]]+\]", "[REPO]", s)
    s = re.sub(r"\b[A-Z]{2,}_\d+_[A-Z_]+\b", "<TOK>", s)
    s = re.sub(r"\[[A-Z_]+_\d+\]", "<RED>", s)
    s = re.sub(r"\d+", "N", s)
    return s[:60]


def main():
    files = sorted(os.listdir(TD))
    fmt = collections.Counter()
    fex = collections.defaultdict(list)
    def F(k, rid, n=10):
        fmt[k] += 1
        if len(fex[k]) < n:
            fex[k].append(rid)
    groups = collections.defaultdict(list)  # rfc -> [(mailbox, file, subj, from, epoch, bodyhash, natt)]
    sent = collections.defaultdict(collections.Counter)
    sent_first, sent_last = {}, {}
    recv = collections.defaultdict(collections.Counter)
    mbox_first, mbox_last = {}, {}
    sent_hours = collections.defaultdict(lambda: [0] * 24)
    sent_wd = collections.defaultdict(lambda: [0] * 7)
    internal_len = collections.defaultdict(list)
    internal_subj_len = []
    internal_marks = collections.Counter()
    pat = collections.Counter()
    pat_ex = {}
    pat_sender = collections.defaultdict(collections.Counter)
    cal = []
    helpshift = []
    ghmail = []
    appstore = []
    crash = []
    linear_mail = []
    dist = []
    tflight = []
    ooo_threads = 0
    ooo_ex = []
    redact = {}
    redact_ex = {}
    alias_pairs = collections.Counter()
    thread_sizes = collections.Counter()
    mailbox_threads = collections.Counter()
    mailbox_msgs = collections.Counter()
    thrids = collections.defaultdict(set)
    date_fmt = collections.Counter()
    for fn in files:
        try:
            t = jload(TD + "/" + fn)
        except Exception:
            F("unreadable thread file", fn)
            continue
        mb = t.get("user_email") or ""
        tid = t.get("id") or ""
        if "_" in fn and "@" in fn:
            alias = fn.split("_")[0]
            alias_pairs[(alias, mb)] += 1
            if alias != mb:
                fmt["file-name mailbox alias != user_email (e.g. leonard@ vs leonard.hayes@)"] += 1
                if len(fex["file-name mailbox alias != user_email (e.g. leonard@ vs leonard.hayes@)"]) < 10:
                    fex["file-name mailbox alias != user_email (e.g. leonard@ vs leonard.hayes@)"].append(fn)
            fmt["_file naming <alias>@harmonygames.co_<thrid>.json"] += 1
        else:
            fmt["_file naming NNNNNNNN.json"] += 1
        if not tid.startswith(mb + "/"):
            F("thread id prefix != user_email", fn)
        thrid = tid.split("/", 1)[1] if "/" in tid else tid
        thrids[mb].add(thrid)
        msgs = t.get("messages") or []
        thread_sizes[min(len(msgs), 12)] += 1
        mailbox_threads[mb] += 1
        prev = None
        ooo_flag = False
        for m in msgs:
            mailbox_msgs[mb] += 1
            mid = m.get("id") or ""
            rid = "gmail:" + mid
            if not mid.startswith(mb + "/"):
                F("message id prefix != thread user_email", fn)
            if m.get("user_email") and m["user_email"] != mb:
                F("message user_email != thread user_email", fn)
            if m.get("thread_id") and m["thread_id"] != tid:
                F("message thread_id != file thread id", fn)
            rfc = mid.split("/", 1)[1] if "/" in mid else mid
            hdr = {h.get("name", "").lower(): h.get("value") for h in (m.get("headers") or [])}
            if hdr.get("x-gm-thrid") and hdr["x-gm-thrid"] != thrid:
                F("X-GM-THRID header != thread id", fn)
            raw_date = m.get("date") or ""
            date_fmt["ISO-Z" if re.match(r"^\d{4}-\d\d-\d\dT", raw_date) else ("RFC-2822" if raw_date else "missing")] += 1
            d = iso_to_dt(m.get("date_parsed")) or iso_to_dt(raw_date)
            d2 = iso_to_dt(raw_date)
            if d is None:
                F("message date unparseable/missing", fn)
            else:
                if d2 and abs((d - d2).total_seconds()) > 60:
                    F("date vs date_parsed differ >60s", fn)
                if m.get("internal_date_ms") and abs(int(m["internal_date_ms"]) / 1000 - d.timestamp()) > 60:
                    F("internal_date_ms vs date differ >60s", fn)
                if d >= CLOCK:
                    F("message dated on/after clock", fn)
                if prev and d < prev - datetime.timedelta(minutes=1) and not ooo_flag:
                    ooo_flag = True
                prev = d if prev is None or d > prev else prev
            subj = m.get("subject") or ""
            frm = email_of(m.get("from"))
            labels = m.get("labelIds") or []
            body = m.get("body") or ""
            natt = len(m.get("attachments") or [])
            groups[rfc].append((mb, fn, norm_text(RE_PREFIX.sub("", subj))[:120], frm, int(d.timestamp()) if d else None, text_hash(body[:4000]), natt, "SENT" in labels,
                                text_hash(RED_ANY.sub(" ", RE_PREFIX.sub("", subj))), text_hash(RED_ANY.sub(" ", body[:4000])), len(body)))
            dm = DIST.search(subj)
            if dm:
                dist.append([dm.group(3), dm.group(4), dm.group(1), int(dm.group(2)), mb, d.isoformat() if d else None, rid])
            tm = TFLIGHT.search(subj)
            if tm:
                tflight.append([tm.group(1), tm.group(2), int(tm.group(3)), mb, d.isoformat() if d else None, rid])
            if re.match(r"^(re|fwd?)\s*:", subj, re.I) and not m.get("in_reply_to") and not m.get("references"):
                fmt["Re:/Fwd: subject without in_reply_to/references"] += 1
            if "SENT" in labels and frm and frm != mb and mb.split("@")[0].split(".")[0] not in frm:
                F("SENT label but From is not the mailbox owner", fn)
            mon = d.strftime("%Y-%m") if d else "unknown"
            if "SENT" in labels or frm == mb:
                sent[frm][mon] += 1
                if d:
                    s = d.isoformat()
                    sent_first[frm] = min(sent_first.get(frm, s), s)
                    sent_last[frm] = max(sent_last.get(frm, s), s)
                    sent_hours[frm][d.hour] += 1
                    sent_wd[frm][d.weekday()] += 1
            else:
                recv[mb][mon] += 1
            if d:
                s = d.isoformat()
                mbox_first[mb] = min(mbox_first.get(mb, s), s)
                mbox_last[mb] = max(mbox_last.get(mb, s), s)
            # internal human-written mail conventions
            if frm.endswith("@harmonygames.co") and ("SENT" in labels):
                new = QUOTE_CUT.split(body, 1)[0]
                internal_len[frm].append(len(new))
                internal_subj_len.append(len(subj))
                internal_marks["n"] += 1
                if GREET.search(new):
                    internal_marks["greeting"] += 1
                if SIGN.search("\n" + new + "\n"):
                    internal_marks["sign_off"] += 1
                if QUOTE_CUT.search(body):
                    internal_marks["quoted_history"] += 1
                if re.match(r"^(re|fwd?)\s*:", subj, re.I):
                    internal_marks["re_fwd_subject"] += 1
                if natt:
                    internal_marks["has_attachment"] += 1
            sp = subj_pattern(subj)
            k = (frm if not frm.endswith("@harmonygames.co") else "<internal>", sp)
            pat[k] += 1
            if k not in pat_ex:
                pat_ex[k] = rid
            # integrations
            cm = CAL.match(subj.strip())
            if cm:
                cal.append([cm.group(1), cm.group(2).strip(), cm.group(3).strip(), mb, d.isoformat() if d else None, rid, frm])
            hm = HELP.search(subj)
            if hm and ("helpshift" in body.lower() or "issue #" in subj):
                helpshift.append([hm.group(1), hm.group(2), int(hm.group(3)), mb, d.isoformat() if d else None, bool(RE_PREFIX.match(subj)), rid, frm])
            gm = GHMAIL.search(subj)
            if gm:
                first = body.strip().split("\n")[0][:80]
                ghmail.append([gm.group(1), gm.group(2), int(gm.group(3)), mb, d.isoformat() if d else None, re.sub(r"\[PERSON_NAME_\d+\]|@[\w.]+", "<p>", first)[:60], rid])
            if APPSTORE.search(subj):
                appstore.append([subj[:120], mb, d.isoformat() if d else None, rid, frm])
            if CRASH.search(subj):
                crash.append([subj_pattern(subj), mb, d.isoformat() if d else None, rid])
            lk = LINEAR_KEY.findall(subj)
            if lk or "linear.app/" in body[:3000]:
                keys = sorted(set("%s-%s" % x for x in LINEAR_KEY.findall(subj + " " + body[:3000])))
                linear_mail.append([subj_pattern(subj), keys[:6], mb, d.isoformat() if d else None, rid, frm])
            redaction_counts(subj + "\n" + body[:20000], redact, redact_ex, rid)
        if ooo_flag:
            ooo_threads += 1
            if len(ooo_ex) < 10:
                ooo_ex.append(fn)
    # cross-mailbox comparison
    xm = collections.Counter()
    xpairs = collections.Counter()
    xpairs_dis = collections.Counter()
    xpairs_mat = collections.Counter()
    xex = collections.defaultdict(list)
    dup_same_mb = 0
    dup_ex = []
    multi = 0
    copies_dist = collections.Counter()
    for rfc, lst in groups.items():
        mbs = [x[0] for x in lst]
        if len(set(mbs)) < len(mbs):
            dup_same_mb += 1
            if len(dup_ex) < 10:
                dup_ex.append(rfc[:120])
        copies_dist[min(len(set(mbs)), 10)] += 1
        if len(set(mbs)) < 2:
            continue
        multi += 1
        base = lst[0]
        for o in lst[1:]:
            if o[0] == base[0]:
                continue
            diffs = []
            if o[2] != base[2]:
                diffs.append("subject (raw)")
                if o[8] != base[8]:
                    diffs.append("subject (after stripping redaction tokens/addresses)")
            if o[3] != base[3]:
                diffs.append("from")
            if o[4] and base[4] and abs(o[4] - base[4]) > 120:
                diffs.append("date>2min")
            if o[5] != base[5]:
                diffs.append("body (raw)")
                if o[9] != base[9]:
                    diffs.append("body (after stripping redaction tokens/addresses/whitespace)")
                    if base[10] and abs(o[10] - base[10]) / max(base[10], 1) > 0.2:
                        diffs.append("body length differs >20%")
            if o[6] != base[6]:
                diffs.append("attachment count")
            pair = " | ".join(sorted([base[0], o[0]]))
            xpairs[pair] += 1
            if diffs:
                xpairs_dis[pair] += 1
                if "body (after stripping redaction tokens/addresses/whitespace)" in diffs or "subject (after stripping redaction tokens/addresses)" in diffs:
                    xpairs_mat[pair] += 1
            for df in diffs:
                xm[df] += 1
                if len(xex[df]) < 10:
                    xex[df].append([base[0] + " " + base[1], o[0] + " " + o[1], rfc[:90]])
            break
    def fin_q(d):
        return {k: quantiles(v) for k, v in d.items() if len(v) >= 5}
    pats = [{"sender": k[0], "pattern": k[1], "n": v, "example": pat_ex[k]} for k, v in pat.most_common(700)]
    out = {
        "files": len(files),
        "mailboxes": {k: {"threads": mailbox_threads[k], "messages": mailbox_msgs[k], "first": mbox_first.get(k), "last": mbox_last.get(k)} for k in mailbox_threads},
        "alias_pairs": [[a, b, n] for (a, b), n in alias_pairs.most_common()],
        "thread_size_dist": dict(sorted(thread_sizes.items())),
        "date_formats": dict(date_fmt),
        "format": dict(fmt), "format_examples": dict(fex),
        "cross_mailbox": {"messages_with_copies_in_2plus_mailboxes": multi, "copies_dist": dict(sorted(copies_dist.items())), "disagreements": dict(xm), "examples": dict(xex),
                           "pairs_compared": dict(xpairs.most_common(40)), "pairs_any_disagreement": dict(xpairs_dis.most_common(40)), "pairs_material_disagreement": dict(xpairs_mat.most_common(40)),
                           "same_rfc_twice_in_one_mailbox": dup_same_mb, "same_rfc_examples": dup_ex, "distinct_rfc": len(groups)},
        "sent_monthly": {k: dict(sorted(v.items())) for k, v in sent.items()},
        "sent_first": sent_first, "sent_last": sent_last,
        "sent_hours_utc": dict(sent_hours), "sent_weekday": dict(sent_wd),
        "recv_monthly": {k: dict(sorted(v.items())) for k, v in recv.items()},
        "internal_new_text_len": fin_q(internal_len),
        "internal_new_text_len_all": quantiles([x for v in internal_len.values() for x in v]),
        "internal_subject_len": quantiles(internal_subj_len),
        "internal_marks": dict(internal_marks),
        "subject_patterns": pats,
        "calendar_mails": cal,
        "helpshift_mails": helpshift,
        "github_mails": ghmail,
        "appstore_mails": appstore,
        "crash_mails": crash,
        "linear_mails": linear_mail,
        "distribution_mails": dist,
        "testflight_mails": tflight,
        "threads_out_of_order": {"count": ooo_threads, "examples": ooo_ex},
        "redaction": redact, "redaction_examples": redact_ex,
        "thread_ids": {k: sorted(v) for k, v in thrids.items()},
        "multi_copy_files": {rfc: [[x[0], x[1]] for x in lst] for rfc, lst in groups.items() if len(set(x[0] for x in lst)) > 1},
    }
    jdump(out, CACHE + "/kb_gmail.json")
    print("gmail done", len(files), len(groups), multi, len(cal), len(helpshift), len(ghmail), len(linear_mail))


if __name__ == "__main__":
    main()
