"""One streaming pass over every Slack shard -> kb_cache/kb_slack.json.

Feeds activity (per-user volumes, joins/leaves), coherence (thread counters, ids, formats),
traps (corrections in replies, redaction, bot noise), cohorts (thread roots per channel),
integrations (GitHub app, Jenkins, Linear app, Zapier/Helpshift, standup bot ...) and
conventions (length/tone per channel type, hours).
"""
import os, re, json, collections, datetime
from zoneinfo import ZoneInfo
from common import *

PT = ZoneInfo("America/Los_Angeles")
users = {u["id"]: u for u in jload(SLACK + "/users.json")}
channels = {c["id"]: c for c in jload(SLACK + "/channels.json")}


def ctype(c):
    if c.get("is_im"):
        return "im"
    if c.get("is_mpim"):
        return "mpim"
    if c.get("is_private"):
        return "private"
    return "public"


GH_FALLBACK = re.compile(r"^\[(?:harmonygames|\[SOURCE_ORG_0001\])-Games/([^\]]+)\]\s*(.*)$", re.S)
LINK_TXT = re.compile(r"<https?://[^|>]*\|([^>]*)>")
PR_NUM = re.compile(r"/pull/(\d+)")
HASHNUM = re.compile(r"#(\d+)")
JENKINS = re.compile(r"^(?P<job>[A-Za-z][A-Za-z0-9 ._-]*?) - #(?P<num>\d+)\s*(?P<rest>.*)$", re.S)
CORRECTION = re.compile(
    r"\b(actually|correction|scratch that|ignore (that|my|the previous)|my bad|i was wrong|not true|"
    r"turns out|false alarm|never ?mind|nvm|update:|edit:|wrong number|typo|instead of|"
    r"that's wrong|thats wrong|disregard|retract|revert(ed)? that|no longer)\b",
    re.I,
)
GH_PR_URL = re.compile(r"github\.com/harmonygames-Games/([A-Za-z0-9_.-]+)/pull/(\d+)")
TRELLO_URL = re.compile(r"trello\.com/c/([A-Za-z0-9]+)")
GDOC_URL = re.compile(r"docs\.google\.com/(document|spreadsheets|presentation)/d/")
EMOJI = re.compile(r":[a-z0-9_+\-]+:")


def strip_links(s):
    return LINK_TXT.sub(r"\1", s or "")


def gh_parse(att):
    fb = att.get("fallback") or ""
    m = GH_FALLBACK.match(fb)
    if not m:
        return None
    repo, rest = m.group(1), strip_links(m.group(2))
    pre = strip_links(att.get("pretext") or "")
    basis = pre or rest
    kind = basis
    kind = re.sub(r"\b\d+ new commits? pushed to\b", "N new commit(s) pushed to", kind)
    kind = re.sub(r" by .*$", "", kind)
    kind = re.sub(r"`[^`]*`|_[^_]*_", "<branch>", kind)
    kind = re.sub(r"#\d+", "#N", kind).strip()
    actor = None
    am = re.search(r" by ([^\s']+)", basis)
    if am:
        actor = am.group(1)
    num = None
    for src in (att.get("title_link") or "", att.get("title") or "", pre, fb):
        mm = PR_NUM.search(src) or HASHNUM.search(strip_links(src))
        if mm:
            num = int(mm.group(1))
            break
    if num is None:
        for a in att.get("actions") or []:
            v = a.get("value") or ""
            mm = re.search(r"number&amp;amp;quot;:(\d+)|\"number\":(\d+)", v)
            if mm:
                num = int(mm.group(1) or mm.group(2))
                break
    branch = None
    bm = re.search(r"pushed to `?<?[^`]*?\|?([A-Za-z0-9_./-]+)>?`", att.get("pretext") or "")
    if bm:
        branch = bm.group(1)
    return {"repo": repo, "kind": kind[:80], "actor": actor, "pr": num, "text": (att.get("text") or "")[:400], "branch": branch}


def classify(x, cname):
    """Return (integration_name, detail) or None for human messages."""
    u = x.get("user") or ""
    atts = x.get("attachments") or []
    a0 = atts[0] if atts else {}
    fb = a0.get("fallback") or ""
    bp = (x.get("bot_profile") or {}).get("name")
    isbot = bool(x.get("bot_id") or x.get("subtype") == "bot_message" or u.startswith("SLACK_BOT") or u == "USLACKBOT" or bp)
    if fb.startswith("[harmonygames-Games/") or fb.startswith("[[SOURCE_ORG_0001]-Games/"):
        d = gh_parse(a0)
        if d is not None:
            d["org_redacted"] = fb.startswith("[[SOURCE_ORG")
        return "github_app", d
    if not isbot:
        return None
    text = x.get("text") or ""
    src = fb or text
    named = {"SLACK_BOT_0002_SLACK_ID": "google_drive_app", "SLACK_BOT_0003_SLACK_ID": "lucidchart_app",
             "SLACK_BOT_0019_SLACK_ID": "cursor_app", "SLACK_BOT_0009_SLACK_ID": "metabase_app",
             "PERSON_6089_SLACK_ID": "slack_connect_notice"}
    if u in named:
        return named[u], None
    if bp == "giphy":
        return "giphy", None
    if cname == "engineering-bots" and not u:
        return "github_app_legacy_text", {"kind": re.sub(r"\d+", "N", strip_links(text))[:50]}
    if u == "SLACK_BOT_0007_SLACK_ID" or "linear.app/" in json.dumps(a0)[:3000] or a0.get("color") == "#5e6ad2":
        km = LINEAR_KEY.search(src)
        act = re.sub(r"^\S.*? - ", "", src.split(" for ")[0]) if " - " in src else src[:40]
        return "linear_app", {"key": km.group(0) if km else None, "action": re.sub(r"\[PERSON_NAME_\d+\]", "<person>", act)[:60]}
    if "#ZapierBot" in text or "Sent by Zapier" in text:
        kind = "new_issue" if "New Issue" in text else ("issue_update" if "Issue Update" in text else "other")
        return "zapier_helpshift", {"kind": kind}
    if cname == "builds":
        m = JENKINS.match(src.strip())
        if m:
            rest = m.group("rest")
            st = "started" if rest.startswith("Started") else ("success" if "Success" in rest else ("failure" if ("Failure" in rest or "Failed" in rest) else ("aborted" if "Aborted" in rest else ("unknown" if "Unknown" in rest else ("fixed" if "Back to normal" in rest else "other")))))
            return "jenkins", {"job": m.group("job").strip(), "num": int(m.group("num")), "status": st}
        kind = re.sub(r"\d+", "N", src.strip().split("\n")[0])[:40]
        return "jenkins_buildscript", {"kind": kind}
    if u == "SLACK_BOT_0006_SLACK_ID":
        return "standup_bot", None
    if u == "SLACK_BOT_0012_SLACK_ID" or "monkey" in (cname or ""):
        return "qa_monkey_bot", None
    if u == "SLACK_BOT_0013_SLACK_ID":
        return "harmony_gpt_bot", None
    if u == "USLACKBOT":
        return "slackbot", None
    return "other_bot:" + (u or x.get("bot_id") or "?") + ("|" + bp if bp else ""), None


def main():
    person = {}  # uid -> stats
    def P(uid):
        p = person.get(uid)
        if p is None:
            p = person[uid] = {"first": None, "last": None, "n": 0, "monthly": collections.Counter(),
                               "by_type": collections.Counter(), "replies": 0, "roots": 0,
                               "hours_pt": [0] * 24, "hours_utc": [0] * 24, "weekday_pt": [0] * 7,
                               "chan": {}, "lens": [], "lower_start": 0, "all_lower": 0, "ends_punct": 0,
                               "emoji": 0, "url": 0, "mention": 0, "question": 0, "multiline": 0, "textn": 0}
        return p

    joins = []  # [uid, cid, ts, subtype]
    chan_month = collections.defaultdict(collections.Counter)
    chan_n = collections.Counter()
    parents = {}  # (cid, ts) -> [claimed_rc, claimed_ruc, latest_reply, user, excerpt, raw]
    replies = collections.defaultdict(lambda: [0, set(), None, None])  # (cid,thread_ts) -> [n, users, max, min]
    reply_before_parent = []
    type_lens = collections.defaultdict(list)
    type_marks = collections.defaultdict(collections.Counter)
    chan_lens = collections.defaultdict(list)
    integ = collections.defaultdict(lambda: {"n": 0, "monthly": collections.Counter(), "channels": collections.Counter(), "samples": [], "first": None, "last": None, "detail": collections.Counter()})
    gh_mirror = []
    jenkins_builds = []
    corrections = []
    linear_mentions = {}
    pr_mentions = collections.defaultdict(list)
    trello_links = 0
    gdoc_links = 0
    redact = {}
    redact_ex = {}
    fmt = collections.Counter()
    fmt_ex = collections.defaultdict(list)
    after_clock = []
    unknown_users = collections.Counter()
    nonmember_posts = collections.defaultdict(collections.Counter)
    edited = 0
    total = 0

    def ex(key, rid, k=10):
        if len(fmt_ex[key]) < k:
            fmt_ex[key].append(rid)

    for cid in sorted(os.listdir(SLACK + "/messages")):
        c = channels.get(cid)
        if c is None:
            fmt["shard dir without channel row"] += 1
            ex("shard dir without channel row", cid)
            continue
        cname = c.get("name") or cid
        ct = ctype(c)
        members = set(c.get("members") or [])
        seen_ts = set()
        for fn in sorted(os.listdir(SLACK + "/messages/" + cid)):
            for x in jload(SLACK + "/messages/" + cid + "/" + fn):
                total += 1
                ts = x.get("ts")
                rid = cid + "/" + str(ts)
                raw = "id" not in x
                if raw:
                    fmt["raw-shaped record (no id/reply_count; blocks+client_msg_id)"] += 1
                    ex("raw-shaped record (no id/reply_count; blocks+client_msg_id)", rid)
                else:
                    if x["id"] != sha32(cid + "|" + ts):
                        fmt["message id != sha256(channel|ts)[:32]"] += 1
                        ex("message id != sha256(channel|ts)[:32]", rid)
                if ts in seen_ts:
                    fmt["duplicate (channel, ts)"] += 1
                    ex("duplicate (channel, ts)", rid)
                seen_ts.add(ts)
                if x.get("channel") and x.get("channel") != cid:
                    fmt["record channel != shard channel"] += 1
                    ex("record channel != shard channel", rid)
                tsf = float(ts)
                mon = month_of_ts(tsf)
                if fn[:7] != mon:
                    fmt["message month != shard month"] += 1
                    ex("message month != shard month", rid)
                if tsf >= CLOCK_TS:
                    after_clock.append(rid)
                if x.get("edited"):
                    edited += 1
                chan_month[cid][mon] += 1
                chan_n[cid] += 1
                uid = x.get("user")
                sub = x.get("subtype")
                text = x.get("text") or ""
                tts = x.get("thread_ts")
                is_reply = bool(tts) and tts != ts
                if sub in ("channel_join", "channel_leave", "group_join", "group_leave"):
                    joins.append([uid, cid, ts, sub])
                    continue
                cl = classify(x, cname)
                if cl:
                    name, det = cl
                    I = integ[name]
                    I["n"] += 1
                    I["monthly"][mon] += 1
                    I["channels"][cname] += 1
                    I["first"] = ts if I["first"] is None else min(I["first"], ts, key=float)
                    I["last"] = ts if I["last"] is None else max(I["last"], ts, key=float)
                    if len(I["samples"]) < 5:
                        I["samples"].append(rid)
                    if det:
                        k = det.get("kind") or det.get("status") or det.get("action")
                        if k:
                            I["detail"][k] += 1
                    if name == "github_app" and det:
                        gh_mirror.append([cid, ts, tts, det["repo"], det["pr"], det["kind"], det["actor"], det["text"], det.get("branch"), sub, det.get("org_redacted")])
                    if name == "jenkins" and det:
                        jenkins_builds.append([ts, det["job"], det["num"], det["status"]])
                    redaction_counts(text + json.dumps(x.get("attachments") or [])[:2000], redact.setdefault("bot", {}), redact_ex.setdefault("bot", {}), "slack:" + rid)
                    # bot threads still count for thread integrity
                else:
                    if uid and uid not in users:
                        unknown_users[uid] += 1
                    if uid and members and uid not in members and ct in ("public", "private"):
                        nonmember_posts[cid][uid] += 1
                    if uid:
                        p = P(uid)
                        p["n"] += 1
                        p["first"] = tsf if p["first"] is None else min(p["first"], tsf)
                        p["last"] = tsf if p["last"] is None else max(p["last"], tsf)
                        p["monthly"][mon] += 1
                        p["by_type"][ct] += 1
                        if is_reply:
                            p["replies"] += 1
                        elif x.get("reply_count"):
                            p["roots"] += 1
                        d = ts_to_dt(tsf)
                        lp = d.astimezone(PT)
                        p["hours_pt"][lp.hour] += 1
                        p["hours_utc"][d.hour] += 1
                        p["weekday_pt"][lp.weekday()] += 1
                        ch = p["chan"].get(cid)
                        if ch is None:
                            p["chan"][cid] = [tsf, tsf, 1]
                        else:
                            ch[0] = min(ch[0], tsf); ch[1] = max(ch[1], tsf); ch[2] += 1
                        if text.strip():
                            L = len(text)
                            p["lens"].append(L)
                            type_lens[ct].append(L)
                            chan_lens[cid].append(L)
                            tm = type_marks[ct]
                            p["textn"] += 1
                            tm["n"] += 1
                            alpha = [ch_ for ch_ in text if ch_.isalpha()]
                            if alpha and alpha[0].islower():
                                p["lower_start"] += 1; tm["lower_start"] += 1
                            if alpha and not any(ch_.isupper() for ch_ in alpha):
                                p["all_lower"] += 1; tm["all_lower"] += 1
                            if text.rstrip()[-1:] in ".!?":
                                p["ends_punct"] += 1; tm["ends_punct"] += 1
                            if EMOJI.search(text):
                                p["emoji"] += 1; tm["emoji"] += 1
                            if "<http" in text:
                                p["url"] += 1; tm["url"] += 1
                            if "<@" in text:
                                p["mention"] += 1; tm["mention"] += 1
                            if "?" in text:
                                p["question"] += 1; tm["question"] += 1
                            if "\n" in text.strip():
                                p["multiline"] += 1; tm["multiline"] += 1
                    redaction_counts(re.sub(r"<[@#!][^>]*>", "", text), redact.setdefault("human", {}), redact_ex.setdefault("human", {}), "slack:" + rid)
                    for m in LINEAR_KEY.finditer(text):
                        k = m.group(0)
                        e = linear_mentions.get(k)
                        if e is None:
                            linear_mentions[k] = [1, tsf, tsf, rid]
                        else:
                            e[0] += 1; e[1] = min(e[1], tsf); e[2] = max(e[2], tsf)
                    for m in GH_PR_URL.finditer(text):
                        pr_mentions["harmonygames-Games/%s#%s" % (m.group(1), m.group(2))].append(rid)
                    trello_links += len(TRELLO_URL.findall(text))
                    gdoc_links += len(GDOC_URL.findall(text))
                    if is_reply and CORRECTION.search(text):
                        corrections.append([cid, tts, ts, uid, CORRECTION.search(text).group(0).lower(), text[:220]])
                # thread bookkeeping (human and bot)
                if tts and tts == ts:
                    parents[(cid, ts)] = [x.get("reply_count"), x.get("reply_users_count"), x.get("latest_reply"), uid, text[:200], raw, bool(cl)]
                elif tts and tts != ts:
                    r = replies[(cid, tts)]
                    r[0] += 1
                    r[1].add(uid or x.get("bot_id") or x.get("username") or "bot")
                    r[2] = ts if r[2] is None else max(r[2], ts, key=float)
                    r[3] = ts if r[3] is None else min(r[3], ts, key=float)
                    if tsf < float(tts):
                        reply_before_parent.append(rid)
                elif not tts and x.get("reply_count"):
                    fmt["reply_count>0 but thread_ts null"] += 1
                    ex("reply_count>0 but thread_ts null", rid)

    # thread integrity
    rc_mismatch, ruc_mismatch, lr_mismatch, orphan, raw_parent = [], [], [], [], 0
    roots_by_chan = collections.defaultdict(lambda: collections.Counter())
    for key, pv in parents.items():
        cid, ts = key
        r = replies.get(key)
        actual = r[0] if r else 0
        if r:
            roots_by_chan[cid][month_of_ts(float(ts))] += 1
        if pv[5]:
            raw_parent += 1
            continue
        if pv[0] is not None and pv[0] != actual:
            rc_mismatch.append([cid + "/" + ts, pv[0], actual])
        if r and pv[1] is not None and pv[1] != len(r[1]):
            ruc_mismatch.append([cid + "/" + ts, pv[1], len(r[1])])
        if r and pv[2] and pv[2] != r[2]:
            lr_mismatch.append([cid + "/" + ts, pv[2], r[2]])
    for key, r in replies.items():
        if key not in parents:
            orphan.append([key[0] + "/" + key[1], r[0]])
    thread_roots = {}
    for key, pv in parents.items():
        r = replies.get(key)
        if r:
            thread_roots.setdefault(key[0], []).append([key[1], r[0], pv[3], pv[6]])

    # corrections: attach parent excerpt
    corr_out = []
    for cid, tts, ts, uid, phrase, txt in corrections:
        pv = parents.get((cid, tts))
        corr_out.append({"channel": cid, "channel_name": channels[cid].get("name"), "thread_ts": tts, "reply_ts": ts, "user": uid,
                         "marker": phrase, "reply": txt, "parent_user": pv[3] if pv else None, "parent": (pv[4] if pv else None)})

    def fin_person(p):
        out = {k: v for k, v in p.items() if k not in ("lens", "monthly", "by_type", "chan")}
        out["monthly"] = dict(sorted(p["monthly"].items()))
        out["by_type"] = dict(p["by_type"])
        out["len_q"] = quantiles(p["lens"])
        out["chan"] = {k: v for k, v in sorted(p["chan"].items(), key=lambda kv: -kv[1][2])}
        return out

    out = {
        "total_records": total,
        "edited": edited,
        "person": {u: fin_person(p) for u, p in person.items()},
        "joins": joins,
        "chan_month": {k: dict(sorted(v.items())) for k, v in chan_month.items()},
        "chan_n": dict(chan_n),
        "thread": {
            "parents": len(parents), "parents_with_replies": sum(1 for k in parents if k in replies),
            "raw_parents_no_counters": raw_parent,
            "reply_count_mismatch": rc_mismatch, "reply_users_mismatch": ruc_mismatch,
            "latest_reply_mismatch": lr_mismatch, "orphan_reply_groups": orphan,
            "reply_before_parent": reply_before_parent,
        },
        "roots_by_chan_month": {k: dict(sorted(v.items())) for k, v in roots_by_chan.items()},
        "thread_roots": thread_roots,
        "type_len_q": {k: quantiles(v) for k, v in type_lens.items()},
        "type_marks": {k: dict(v) for k, v in type_marks.items()},
        "chan_len_q": {k: quantiles(v) for k, v in chan_lens.items() if len(v) >= 50},
        "integrations": {k: {"n": v["n"], "first": v["first"], "last": v["last"], "monthly": dict(sorted(v["monthly"].items())),
                              "channels": dict(v["channels"].most_common(10)), "samples": v["samples"], "detail": dict(v["detail"].most_common(25))}
                         for k, v in integ.items()},
        "gh_mirror": gh_mirror,
        "jenkins_builds": jenkins_builds,
        "corrections": corr_out,
        "linear_mentions": linear_mentions,
        "pr_mentions": {k: v[:5] + ([len(v)] if len(v) > 5 else []) for k, v in pr_mentions.items()},
        "pr_mention_counts": {k: len(v) for k, v in pr_mentions.items()},
        "trello_links": trello_links, "gdoc_links": gdoc_links,
        "redaction": redact, "redaction_examples": redact_ex,
        "format": dict(fmt), "format_examples": dict(fmt_ex),
        "after_clock": after_clock,
        "unknown_users": dict(unknown_users),
        "nonmember_posts": {k: dict(v) for k, v in nonmember_posts.items()},
    }
    jdump(out, CACHE + "/kb_slack.json")
    print("slack done", total, len(person), len(gh_mirror), len(jenkins_builds), len(corr_out))


if __name__ == "__main__":
    main()
