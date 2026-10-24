"""GitHub + Linear pass (both small enough to load) -> kb_cache/kb_github.json, kb_linear.json.
Joins: Linear keys found in PR titles/branches/bodies/commit messages; Slack GitHub-app mirror (kb_slack.json)."""
import re, json, collections
from common import *

LINKEY_BRANCH = re.compile(r"\b(ENG|ZOM|ART|DES|EPI)-?(\d{1,4})", re.I)
CONV = re.compile(r"^(feat|fix|chore|refactor|docs|test|perf|style|build|ci)(\(.+?\))?!?:", re.I)


def qkey(dt):
    return "%d-Q%d" % (dt.year, (dt.month - 1) // 3 + 1)


def main():
    G = jload(GITHUB)
    L = jload(LINEAR)
    S = jload(CACHE + "/kb_slack.json")

    # ---------------- Linear -----------------
    lusers = {u["id"]: u for u in L["users"]}
    issues = {i["id"]: i for i in L["issues"]}
    lin_haz = collections.defaultdict(list)
    def lh(k, rid):
        lin_haz[k].append(rid)
    DONE = {"Done"}
    CANCEL = {"Canceled", "Duplicate"}
    lperson = collections.defaultdict(lambda: {"created": collections.Counter(), "completed": collections.Counter(), "assigned_open": 0, "assigned_total": 0, "first": None, "last": None})
    def touch(uid, d, kind):
        if not uid or not d:
            return
        p = lperson[uid]
        m = d.strftime("%Y-%m")
        p[kind][m] += 1
        s = d.isoformat()
        p["first"] = s if p["first"] is None or s < p["first"] else p["first"]
        p["last"] = s if p["last"] is None or s > p["last"] else p["last"]
    team_states = collections.defaultdict(collections.Counter)
    team_labels = collections.defaultdict(collections.Counter)
    title_pref = collections.defaultdict(collections.Counter)
    desc_len = collections.defaultdict(list)
    prio = collections.defaultdict(collections.Counter)
    max_num = collections.Counter()
    for i in L["issues"]:
        iid = i["id"]
        team = (i.get("team_id") or "").replace("team_", "")
        st = i.get("state_id")
        team_states[team][st] += 1
        for l in i.get("labels") or []:
            team_labels[team][l] += 1
        prio[team][i.get("priority")] += 1
        t = i.get("title") or ""
        pm = re.match(r"^([A-Z][A-Za-z0-9 &/]{1,25}?)\s*[:>|\]-]", t)
        title_pref[team][(pm.group(1).strip() if pm else "<none>")] += 1
        if i.get("description"):
            desc_len[team].append(len(i["description"]))
        max_num[team] = max(max_num[team], i.get("number") or 0)
        ca, ua = iso_to_dt(i.get("created_at")), iso_to_dt(i.get("updated_at"))
        co, cn, sa = iso_to_dt(i.get("completed_at")), iso_to_dt(i.get("canceled_at")), iso_to_dt(i.get("started_at"))
        touch(i.get("creator_id"), ca, "created")
        if co and st in DONE:
            touch(i.get("assignee_id"), co, "completed")
        if i.get("assignee_id"):
            lperson[i["assignee_id"]]["assigned_total"] += 1
            if st not in DONE and st not in CANCEL:
                lperson[i["assignee_id"]]["assigned_open"] += 1
        # hazards
        if st in DONE and not co:
            lh("state Done but completed_at null", iid)
        if st in CANCEL and not cn and st == "Canceled":
            lh("state Canceled but canceled_at null", iid)
        if co and st not in DONE:
            lh("completed_at set but state not Done", iid)
        if cn and st not in CANCEL:
            lh("canceled_at set but state not Canceled/Duplicate", iid)
        if co and ca and co < ca:
            lh("completed_at before created_at", iid)
        if sa and co and co < sa:
            lh("completed_at before started_at", iid)
        if ua and ca and ua < ca:
            lh("updated_at before created_at", iid)
        if co and ua and ua < co:
            lh("updated_at before completed_at", iid)
        for d, nm in ((ca, "created_at"), (ua, "updated_at"), (co, "completed_at")):
            if d and d >= CLOCK:
                lh("%s on/after clock" % nm, iid)
        if i.get("assignee_id") and i["assignee_id"] not in lusers:
            lh("assignee_id not in linear users", iid)
        if i.get("creator_id") and i["creator_id"] not in lusers:
            lh("creator_id not in linear users", iid)
        if i.get("parent_id"):
            par = issues.get(i["parent_id"])
            if not par:
                lh("parent_id missing", iid)
            else:
                if par.get("state_id") in DONE and st not in DONE and st not in CANCEL:
                    lh("parent Done while child open", iid)
                if (par.get("team_id") != i.get("team_id")):
                    lh("parent in a different team (cross-team epic)", iid)
        for r in i.get("relations") or []:
            tgt = r.get("target") or r.get("related_issue_id") or r.get("issue_id")
            if tgt and tgt not in issues:
                lh("relation target missing", iid)
        if " " in (i.get("assignee_id") or "") or " " in (i.get("creator_id") or ""):
            lh("user id contains a space (usr_Victor Barnes)", iid)
        if st == "PR":
            lh("state 'PR' (awaiting merge)", iid)
        due = i.get("due_date")
        if due and st not in DONE and st not in CANCEL and due < CLOCK_ISO[:10]:
            lh("open with due_date before clock", iid)
        if i.get("estimate") is None and False:
            pass
    att_comment = [a["issue_identifier"] for a in L["attachments"] if a.get("surface") == "comment"]
    att_missing = [a["id"] for a in L["attachments"] if a.get("issue_identifier") not in issues]

    # ---------------- GitHub -----------------
    prs = {p["id"]: p for p in G["pull_requests"]}
    ghu = {u["login"]: u for u in G["users"]}
    commits = {c["sha"]: c for c in G["commits"]}
    gh_haz = collections.defaultdict(list)
    def gh(k, rid):
        gh_haz[k].append(rid)
    login = collections.defaultdict(lambda: {"commits": collections.Counter(), "prs": collections.Counter(), "reviews": collections.Counter(), "comments": collections.Counter(), "merged_by": 0, "first": None, "last": None})
    def ltouch(lg, d, kind):
        if not lg or not d:
            return
        p = login[lg]
        p[kind][d.strftime("%Y-%m")] += 1
        s = d.isoformat()
        p["first"] = s if p["first"] is None or s < p["first"] else p["first"]
        p["last"] = s if p["last"] is None or s > p["last"] else p["last"]
    repo = collections.defaultdict(lambda: {"prs": 0, "merged": 0, "closed_unmerged": 0, "open": 0, "first_pr": None, "last_pr": None, "by_quarter": collections.Counter(), "merged_by_quarter": collections.Counter()})
    reviews_by_pr = collections.defaultdict(list)
    for r in G["reviews"]:
        reviews_by_pr[r["pr_id"]].append(r)
    comments_by_pr = collections.defaultdict(list)
    for c in G["pull_request_comments"]:
        comments_by_pr[c["pr_id"]].append(c)
    rc_by_pr = collections.Counter(c["pr_id"] for c in G["review_comments"])
    tl_by_pr = collections.defaultdict(list)
    for e in G["timeline_events"]:
        tl_by_pr[e["pr_id"]].append(e)
    pr_title_pat = collections.Counter()
    branch_pat = collections.Counter()
    branch_ex = collections.defaultdict(list)
    title_ex = collections.defaultdict(list)
    pr_body_empty = 0
    pr_body_coderabbit = 0
    pr_linear_link = {}
    for p in G["pull_requests"]:
        pid = p["id"]
        rp = repo[p["repo_id"].split("/")[1]]
        ca, ma, cl, ua = iso_to_dt(p.get("created_at")), iso_to_dt(p.get("merged_at")), iso_to_dt(p.get("closed_at")), iso_to_dt(p.get("updated_at"))
        rp["prs"] += 1
        if p["merged"]:
            rp["merged"] += 1
            if ma:
                rp["merged_by_quarter"][qkey(ma)] += 1
        elif p["state"] == "closed":
            rp["closed_unmerged"] += 1
        else:
            rp["open"] += 1
        if ca:
            rp["by_quarter"][qkey(ca)] += 1
            s = ca.isoformat()
            rp["first_pr"] = s if rp["first_pr"] is None or s < rp["first_pr"] else rp["first_pr"]
            rp["last_pr"] = s if rp["last_pr"] is None or s > rp["last_pr"] else rp["last_pr"]
        ltouch(p.get("author_login"), ca, "prs")
        if p.get("merged_by_login"):
            login[p["merged_by_login"]]["merged_by"] += 1
        # hazards
        if p["merged"] and not ma:
            gh("merged=true but merged_at null", pid)
        if not p["merged"] and ma:
            gh("merged_at set but merged=false", pid)
        if p["merged"] and p["state"] != "closed":
            gh("merged but state open", pid)
        if ca and ma and ma < ca:
            gh("merged_at before created_at", pid)
        if ca and cl and cl < ca:
            gh("closed_at before created_at", pid)
        if ca and ua and ua < ca:
            gh("updated_at before created_at", pid)
        if ca and ca >= CLOCK:
            gh("created on/after clock", pid)
        if ua and ua >= CLOCK:
            gh("updated on/after clock", pid)
        if p["merged"] and p.get("merged_by_login") is None:
            gh("merged but merged_by_login null", pid)
        if p.get("author_login") and p["author_login"] not in ghu:
            gh("author_login not in github users", pid)
        revs = reviews_by_pr.get(pid, [])
        human_revs = [r for r in revs if ghu.get(r["author_login"], {}).get("type") == "User"]
        if p["merged"] and not revs:
            gh("merged with no review at all", pid)
        elif p["merged"] and not any(r["state"] == "APPROVED" and ghu.get(r["author_login"], {}).get("type") == "User" for r in revs):
            gh("merged with no human APPROVED review (bot-only or comment-only)", pid)
        for r in revs:
            sd = iso_to_dt(r.get("submitted_at"))
            if r["author_login"] == p.get("author_login") and r["state"] == "APPROVED":
                gh("self-approved review", r["id"])
            if sd and ca and sd < ca:
                gh("review submitted before PR created", r["id"])
            if sd is None:
                gh("review submitted_at null", r["id"])
        # timeline-commented pairing
        tlc = {(e.get("created_at")): e for e in tl_by_pr.get(pid, []) if e["event"] == "commented"}
        for c in comments_by_pr.get(pid, []):
            e = tlc.get(c.get("created_at"))
            if e is None:
                gh("PR comment without matching 'commented' timeline event", c["id"])
            elif e.get("actor_login") != c.get("author_login"):
                gh("comment author_login != timeline actor_login (bot token split)", c["id"])
        for e in tl_by_pr.get(pid, []):
            if e.get("created_at") is None:
                gh("timeline event created_at null (%s)" % e["event"], e["id"])
        mevents = [e for e in tl_by_pr.get(pid, []) if e["event"] == "merged"]
        if p["merged"] and not mevents:
            gh("merged PR without 'merged' timeline event", pid)
        # conventions
        t = p.get("title") or ""
        if LINEAR_KEY.match(t):
            k = "LINEARKEY: description" if re.match(r"^[A-Z]+-\d+:", t) else "LINEARKEY description"
        elif re.match(r"^[A-Za-z]+[/\\]", t):
            k = "name/branch-style title"
        elif CONV.match(t):
            k = "conventional-commit prefix"
        elif "[PERSON_NAME" in t:
            k = "redacted-name branch title"
        else:
            k = "free text"
        pr_title_pat[k] += 1
        if len(title_ex[k]) < 5:
            title_ex[k].append([pid, t[:90]])
        br = p.get("head_ref") or ""
        if re.match(r"^[a-z]+\.[a-z]+/", br):
            bk = "first.last/<Desc>"
        elif re.match(r"^\[PERSON_NAME_\d+\]/", br):
            bk = "[PERSON_NAME_n]/<desc> (redacted owner)"
        elif re.match(r"^[A-Za-z]+/", br):
            bk = "name/<desc>"
        elif re.match(r"^(feature|fix|hotfix|bugfix|release)[/-]", br, re.I):
            bk = "feature|fix/<desc>"
        elif LINKEY_BRANCH.match(br):
            bk = "<LINEARKEY>-desc"
        else:
            bk = "other"
        branch_pat[bk] += 1
        if len(branch_ex[bk]) < 6:
            branch_ex[bk].append([pid, br])
        body = p.get("body") or ""
        if not body.strip():
            pr_body_empty += 1
        if "coderabbit.ai" in body:
            pr_body_coderabbit += 1
        keys = set()
        for src in (t, br, body[:3000]):
            for m in LINKEY_BRANCH.finditer(src):
                keys.add("%s-%d" % (m.group(1).upper(), int(m.group(2))))
        if keys:
            pr_linear_link[pid] = sorted(keys)
    for r in G["reviews"]:
        ltouch(r.get("author_login"), iso_to_dt(r.get("submitted_at")), "reviews")
    for c in G["pull_request_comments"]:
        ltouch(c.get("author_login"), iso_to_dt(c.get("created_at")), "comments")
    commit_msg_len, commit_lower, commit_merge, commit_conv, commit_key = [], 0, 0, 0, 0
    commit_ex = collections.defaultdict(list)
    for c in G["commits"]:
        d = iso_to_dt(c.get("authored_date") or c.get("committed_date"))
        ltouch(c.get("author_login"), d, "commits")
        msg = (c.get("message") or "").split("\n")[0]
        commit_msg_len.append(len(msg))
        if msg[:1].islower():
            commit_lower += 1
        if msg.startswith("Merge "):
            commit_merge += 1
        if CONV.match(msg):
            commit_conv += 1
        if LINKEY_BRANCH.search(msg):
            commit_key += 1
        if d and d >= CLOCK:
            gh("commit authored on/after clock", c["sha"])
        if d is None:
            gh("commit with no authored/committed date", c["sha"])
        if c.get("committed_date") is None:
            gh_haz.setdefault("_commit committed_date null (count only)", []).append(c["sha"])
    cmap_old = {m["old_sha"] for m in G["commit_map"]}
    for b in G["branches"]:
        if b.get("head_sha") and b["head_sha"] not in commits:
            if b["head_sha"] in cmap_old:
                gh("branch head_sha is a pre-rewrite SHA (commit_map.old_sha), not in commits", b["id"])
            else:
                gh("branch head_sha not in commits or commit_map", b["id"])
    pc_missing = [pc["id"] for pc in G["pull_request_commits"] if pc["commit_sha"] not in commits]
    if pc_missing:
        gh_haz["pull_request_commits sha not in commits"] = pc_missing
    archived = [r["id"] for r in G["repositories"] if r.get("archived")]

    # ------------- Linear <-> GitHub key joins ---------------
    xjoin = collections.defaultdict(list)
    issue_prs = collections.defaultdict(list)
    for pid, keys in pr_linear_link.items():
        p = prs[pid]
        for k in keys:
            i = issues.get(k)
            if i is None:
                xjoin["PR references Linear key that does not exist"].append([pid, k])
                continue
            issue_prs[k].append(pid)
    for k, plist in issue_prs.items():
        i = issues[k]
        st = i.get("state_id")
        merged = [prs[x] for x in plist if prs[x]["merged"]]
        if st in ("Canceled",) and merged:
            xjoin["issue Canceled but a referencing PR merged"].append([k, merged[0]["id"]])
        if st in ("Todo", "Backlog") and merged:
            xjoin["issue Todo/Backlog but a referencing PR merged"].append([k, merged[0]["id"]])
        if st == "PR" and merged:
            xjoin["issue in state PR but a referencing PR merged"].append([k, merged[0]["id"]])
        if st == "Done" and plist and not merged:
            xjoin["issue Done but every referencing PR unmerged"].append([k, plist[0]])
        co = iso_to_dt(i.get("completed_at"))
        if st == "Done" and co and merged:
            first_merge = min(iso_to_dt(m["merged_at"]) for m in merged if m.get("merged_at"))
            if co < first_merge - datetime.timedelta(days=1):
                xjoin["issue completed >1 day before first referencing PR merged"].append([k, merged[0]["id"]])
    # ENG vs ZOM number collisions across repos
    zom_in_god = []
    for pid, keys in pr_linear_link.items():
        for k in keys:
            if k.startswith("ZOM") and "GameOfDominoes" in pid:
                zom_in_god.append([pid, k])
            if k.startswith("ENG") and "match3d" in pid and not pid.endswith("backend"):
                zom_in_god.append([pid, k])

    # ------------- GitHub -> Slack mirror join ---------------
    mirror = S["gh_mirror"]  # [cid, ts, tts, repo, pr, kind, actor, text, branch, subtype, org_redacted]
    mrepo = collections.Counter(m[3] for m in mirror)
    by_pr = collections.defaultdict(lambda: collections.Counter())
    actor_map = collections.defaultdict(collections.Counter)
    first_last = {}
    for m in mirror:
        if m[4] is None:
            continue
        pid = "harmonygames-Games/%s#%d" % (m[3], m[4])
        by_pr[pid][m[5]] += 1
        p = prs.get(pid)
        if p and m[5] == "Pull request opened" and m[6]:
            actor_map[p["author_login"]][m[6]] += 1
        if p and m[5] == "Pull request merged" and m[6] and p.get("merged_by_login"):
            actor_map[p["merged_by_login"]][m[6]] += 1
        r = first_last.setdefault(m[3], [m[1], m[1]])
        r[0] = min(r[0], m[1], key=float); r[1] = max(r[1], m[1], key=float)
    mirrored_repos = sorted(r for r in mrepo)
    base = {}
    for rname in sorted(set(p["repo_id"].split("/")[1] for p in G["pull_requests"])):
        rp = [p for p in G["pull_requests"] if p["repo_id"].endswith("/" + rname)]
        fl = first_last.get(rname)
        win = [p for p in rp if fl and float(fl[0]) - 86400 <= iso_to_dt(p["created_at"]).timestamp() <= float(fl[1]) + 86400] if fl else []
        opened = sum(1 for p in win if by_pr[p["id"]].get("Pull request opened"))
        merged = [p for p in win if p["merged"]]
        mm = sum(1 for p in merged if by_pr[p["id"]].get("Pull request merged"))
        ncom = sum(len(comments_by_pr.get(p["id"], [])) for p in win)
        mcom = sum(by_pr[p["id"]].get("Comment on pull request", 0) for p in win)
        nrev = sum(len(reviews_by_pr.get(p["id"], [])) for p in win)
        mrev = sum(by_pr[p["id"]].get("Review approved", 0) + by_pr[p["id"]].get("Reviewed and changes requested", 0) + by_pr[p["id"]].get("Review comment", 0) + by_pr[p["id"]].get("Reviewed", 0) for p in win)
        unm = [p["id"] for p in win if not by_pr[p["id"]].get("Pull request opened")][:10]
        base[rname] = {"prs_total": len(rp), "mirror_messages": mrepo.get(rname, 0),
                       "mirror_window": [ts_to_dt(fl[0]).isoformat(), ts_to_dt(fl[1]).isoformat()] if fl else None,
                       "prs_in_window": len(win), "prs_with_opened_mirror": opened,
                       "merged_in_window": len(merged), "merged_with_merged_mirror": mm,
                       "pr_comments_in_window": ncom, "comment_mirrors": mcom,
                       "reviews_in_window": nrev, "review_mirrors": mrev,
                       "example_prs_without_opened_mirror": unm}
    login_real = {k: dict(v.most_common(3)) for k, v in actor_map.items()}
    # text-level comment mirroring
    def nrm(t):
        t = re.sub(r"<https?://[^|>]*\|([^>]*)>", r"\1", t or "")
        t = re.sub(r"<[^>]+>", " ", t)
        t = re.sub(r"&[a-z]+;", " ", t)
        return re.sub(r"[^a-z0-9]", "", t.lower())
    sl_comments = collections.defaultdict(list)
    for m in mirror:
        if m[4] is not None and m[5] in ("Comment on pull request", "Review comment", "Review approved", "Reviewed and changes requested", "Reviewed"):
            sl_comments["harmonygames-Games/%s#%d" % (m[3], m[4])].append((m[5], nrm(m[7])[:40], m[1], m[0]))
    cm_stats = collections.defaultdict(lambda: [0, 0])
    cm_unmatched = collections.defaultdict(list)
    for rname in mirrored_repos:
        fl = first_last.get(rname)
        for c in G["pull_request_comments"]:
            if not c["pr_id"].startswith("harmonygames-Games/%s#" % rname):
                continue
            d = iso_to_dt(c.get("created_at"))
            if not d or not (float(fl[0]) <= d.timestamp() <= float(fl[1])):
                continue
            who = "bot" if ghu.get(c["author_login"], {}).get("type") != "User" else "human"
            key = nrm(c.get("body"))[:25]
            hit = any(k == "Comment on pull request" and key and (t.startswith(key[:20]) or key[:20] in t) for k, t, _, _ in sl_comments.get(c["pr_id"], []))
            cm_stats["%s/%s" % (rname, who)][0] += 1
            if hit:
                cm_stats["%s/%s" % (rname, who)][1] += 1
            elif len(cm_unmatched[rname]) < 8:
                cm_unmatched[rname].append(c["id"])
        for r in G["reviews"]:
            if not r["pr_id"].startswith("harmonygames-Games/%s#" % rname):
                continue
            d = iso_to_dt(r.get("submitted_at"))
            if not d or not (float(fl[0]) <= d.timestamp() <= float(fl[1])):
                continue
            kinds = [k for k, _, _, _ in sl_comments.get(r["pr_id"], [])]
            want = {"APPROVED": "Review approved", "CHANGES_REQUESTED": "Reviewed and changes requested", "COMMENTED": "Review comment"}.get(r["state"])
            cm_stats["%s/review_%s" % (rname, r["state"])][0] += 1
            if want in kinds:
                cm_stats["%s/review_%s" % (rname, r["state"])][1] += 1
    comment_mirror_rates = {k: {"github_records": v[0], "with_slack_copy": v[1], "rate": round(v[1] / v[0], 3) if v[0] else None} for k, v in sorted(cm_stats.items())}
    # slack comment mirrors with no github record (same PR, text not found)
    orphan_sl = collections.Counter()
    orphan_ex = collections.defaultdict(list)
    gh_by_pr_text = collections.defaultdict(list)
    for c in G["pull_request_comments"] + G["review_comments"]:
        gh_by_pr_text[c["pr_id"]].append(nrm(c.get("body"))[:400])
    for pid, lst in sl_comments.items():
        for k, t, ts_, cid_ in lst:
            if k != "Comment on pull request" or not t:
                continue
            if not any(t[:20] in g for g in gh_by_pr_text.get(pid, [])):
                rn = pid.split("/")[1].split("#")[0]
                orphan_sl[rn] += 1
                if len(orphan_ex[rn]) < 8:
                    orphan_ex[rn].append(cid_ + "/" + ts_ + " -> " + pid)

    out_gh = {
        "repos": {k: {**{kk: vv for kk, vv in v.items() if not isinstance(vv, collections.Counter)}, "by_quarter": dict(sorted(v["by_quarter"].items())), "merged_by_quarter": dict(sorted(v["merged_by_quarter"].items()))} for k, v in repo.items()},
        "repo_meta": {r["name"]: {"default_branch": r.get("default_branch"), "archived": r.get("archived"), "pushed_at": r.get("pushed_at"), "updated_at": r.get("updated_at")} for r in G["repositories"]},
        "users": {u["login"]: {"name": u.get("name"), "type": u.get("type")} for u in G["users"]},
        "login": {k: {"commits": dict(sorted(v["commits"].items())), "prs": dict(sorted(v["prs"].items())), "reviews": dict(sorted(v["reviews"].items())), "comments": dict(sorted(v["comments"].items())), "merged_by": v["merged_by"], "first": v["first"], "last": v["last"]} for k, v in login.items()},
        "hazards": {k: {"count": len(v), "examples": v[:10], "all": v if len(v) <= 5000 else None} for k, v in gh_haz.items()},
        "conventions": {"pr_title_patterns": dict(pr_title_pat), "pr_title_examples": dict(title_ex), "branch_patterns": dict(branch_pat), "branch_examples": dict(branch_ex),
                         "pr_body_empty": pr_body_empty, "pr_body_has_coderabbit_summary": pr_body_coderabbit, "prs": len(prs),
                         "commit_first_line_len": quantiles(commit_msg_len), "commit_lower_start": commit_lower, "commit_merge_msgs": commit_merge,
                         "commit_conventional": commit_conv, "commit_with_linear_key": commit_key, "commits": len(G["commits"]),
                         "labels": sorted(set(l["name"] for l in G["labels"])),
                         "review_states": dict(collections.Counter(r["state"] for r in G["reviews"])),
                         "pr_size_changed_files": quantiles([p.get("changed_files") or 0 for p in G["pull_requests"]]),
                         "pr_open_to_merge_hours": quantiles([round((iso_to_dt(p["merged_at"]) - iso_to_dt(p["created_at"])).total_seconds() / 3600, 1) for p in G["pull_requests"] if p.get("merged_at") and p.get("created_at")])},
        "pr_linear_keys": pr_linear_link,
        "linear_github_join": {k: {"count": len(v), "examples": v[:10], "all": v if len(v) <= 5000 else None} for k, v in xjoin.items()},
        "issues_with_pr_reference": len(issue_prs),
        "prs_with_linear_key": len(pr_linear_link),
        "cross_series_refs": {"count": len(zom_in_god), "examples": zom_in_god[:10]},
        "slack_mirror": {"mirrored_repos": mirrored_repos, "per_repo": base, "kind_counts": dict(collections.Counter(m[5] for m in mirror).most_common(15)),
                          "org_redacted_copies": sum(1 for m in mirror if m[10]),
                          "threaded": sum(1 for m in mirror if m[2] and m[2] != m[1]), "total": len(mirror)},
        "login_to_slack_mirror_actor": login_real,
        "comment_mirror_rates": comment_mirror_rates,
        "github_comments_without_slack_copy_examples": dict(cm_unmatched),
        "slack_comment_mirrors_without_github_record": {"counts": dict(orphan_sl), "examples": dict(orphan_ex)},
        "archived_repos": archived,
        "pr_state_counts": dict(collections.Counter("%s/%s" % (p["state"], "merged" if p["merged"] else "unmerged") for p in G["pull_requests"])),
        "bot_logins": {k: v.get("type") for k, v in ghu.items() if v.get("type") != "User"},
    }
    jdump(out_gh, CACHE + "/kb_github.json")

    out_lin = {
        "users": {u["id"]: {"email": u.get("email"), "name": u.get("name"), "active": u.get("is_active")} for u in L["users"]},
        "teams": {t["id"]: {"key": t.get("key"), "name": t.get("name"), "created_at": t.get("created_at")} for t in L["teams"]},
        "memberships": [[m["team_id"], m["user_id"]] for m in L["team_memberships"]],
        "person": {k: {"created": dict(sorted(v["created"].items())), "completed": dict(sorted(v["completed"].items())), "assigned_open": v["assigned_open"], "assigned_total": v["assigned_total"], "first": v["first"], "last": v["last"]} for k, v in lperson.items()},
        "team_states": {k: dict(v.most_common()) for k, v in team_states.items()},
        "team_labels": {k: dict(v.most_common(40)) for k, v in team_labels.items()},
        "team_label_vocab_size": {k: len(v) for k, v in team_labels.items()},
        "title_prefixes": {k: dict(v.most_common(15)) for k, v in title_pref.items()},
        "desc_len": {k: quantiles(v) for k, v in desc_len.items()},
        "priority": {k: dict(v) for k, v in prio.items()},
        "max_number": dict(max_num),
        "hazards": {k: {"count": len(v), "examples": v[:10], "all": v if len(v) <= 5000 else None} for k, v in lin_haz.items()},
        "attachments_surface_comment": {"count": len(att_comment), "issues": len(set(att_comment)), "examples": sorted(set(att_comment))[:10]},
        "attachments_missing_issue": att_missing[:10],
        "issue_index": {i["id"]: [i.get("team_id", "").replace("team_", ""), i.get("state_id"), i.get("assignee_id"), i.get("creator_id"), i.get("created_at"), i.get("updated_at"), i.get("completed_at"), i.get("canceled_at"), i.get("labels"), i.get("parent_id"), (i.get("title") or "")[:100], i.get("priority"), bool(i.get("description")), i.get("project_id"), i.get("due_date")] for i in L["issues"]},
    }
    jdump(out_lin, CACHE + "/kb_linear.json")
    print("github/linear done", len(gh_haz), len(lin_haz), len(pr_linear_link), len(issue_prs))


if __name__ == "__main__":
    main()
