"""coherence_hazards.json + trap_catalog.json (and the cross-service join stats reused by integrations)."""
import re, json, collections, datetime
from common import *
from pass_other import norm_title

MON = {m: i for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}


def H(cat, hid, service, title, count, examples, guidance, denominator=None, source="computed", detail=None):
    return {"id": hid, "category": cat, "service": service, "title": title, "count": count, "denominator": denominator,
            "examples": examples[:10] if isinstance(examples, list) else examples, "keep_out_guidance": guidance, "source": source, **({"detail": detail} if detail else {})}


def parse_invite_date(when):
    m = re.search(r"\b([A-Z][a-z]{2}) (\d{1,2}), (\d{4})\b", when or "")
    if not m or m.group(1) not in MON:
        return None
    try:
        return datetime.date(int(m.group(3)), MON[m.group(1)], int(m.group(2)))
    except ValueError:
        return None


def main():
    S = jload(CACHE + "/kb_slack.json")
    SC = jload(CACHE + "/kb_slack_claims.json")
    GM = jload(CACHE + "/kb_gmail.json")
    GC = jload(CACHE + "/kb_gmail_copies.json")
    GH = jload(CACHE + "/kb_github.json")
    LI = jload(CACHE + "/kb_linear.json")
    O = jload(CACHE + "/kb_other.json")
    B = jload(CACHE + "/kb_beats.json")
    A = jload(OUT + "/activity.json")
    E = jload(OUT + "/entities.json")
    G = jload(GITHUB)
    pr_ids = {p["id"] for p in G["pull_requests"]}
    pr_by_repo_num = {(p["repo_id"].split("/")[1], p["number"]): p for p in G["pull_requests"]}
    ghu = {u["login"]: u for u in G["users"]}
    linbot_comments = [c for c in G["pull_request_comments"] if "linear.app/" in (c.get("body") or "")[:600]]
    cr_comments = [c for c in G["pull_request_comments"] if c.get("author_login") == "PERSON_6026_GITHUB_USERNAME"]
    cr_rc = [c for c in G["review_comments"] if c.get("author_login") == "PERSON_6026_GITHUB_USERNAME"]
    cr_rev = [r for r in G["reviews"] if r.get("author_login") == "PERSON_6026_GITHUB_USERNAME"]
    del G
    issues = LI["issue_index"]  # id -> [team, state, assignee, creator, created, updated, completed, canceled, labels, parent, title, prio, hasdesc, project, due]
    chans = {c["id"]: c for c in jload(SLACK + "/channels.json")}
    status = {em: v["status_at_clock"] for em, v in A["people"].items()}
    luser_email = {k: v.get("email") for k, v in LI["users"].items()}

    hz = []
    # ---------------- TEMPORAL ----------------
    gh = GH["hazards"]
    hz.append(H("temporal", "T01", "github", "Timeline 'reviewed' events have null created_at (and empty actor)", gh.get("timeline event created_at null (reviewed)", {}).get("count", 0),
                gh.get("timeline event created_at null (reviewed)", {}).get("examples", []), "Never order or date reviews from the timeline; use github_reviews.submitted_at. Do not seed timeline 'reviewed' rows with timestamps unless you also fill the base pattern consistently.", denominator="12,435 timeline events"))
    hz.append(H("temporal", "T02", "gmail", "Thread files whose messages are not in chronological order", GM["threads_out_of_order"]["count"], GM["threads_out_of_order"]["examples"],
                "Do not let 'the latest message in the thread' be decided by array order; sort by date. Seeded replies must be dated after the parent.", denominator="88,726 thread files"))
    hz.append(H("temporal", "T03", "gmail", "Messages with missing/unparseable date", GM["format"].get("message date unparseable/missing", 0), GM["format_examples"].get("message date unparseable/missing", []),
                "Keep these threads out of any date-ordered question."))
    lj = GH["linear_github_join"]
    k = "issue completed >1 day before first referencing PR merged"
    hz.append(H("temporal", "T04", "linear+github", "Linear issue completed more than a day before the first PR that names it was merged", lj.get(k, {}).get("count", 0), lj.get(k, {}).get("examples", []),
                "If a task asks 'when did X ship', define whether Linear completion or PR merge is authoritative, or avoid these issues.", denominator="%d issues referenced by a PR title/branch/body" % GH["issues_with_pr_reference"]))
    lh = LI["hazards"]
    hz.append(H("temporal", "T05", "linear", "updated_at earlier than completed_at", lh.get("updated_at before completed_at", {}).get("count", 0), lh.get("updated_at before completed_at", {}).get("examples", []), "Avoid in recency questions."))
    th = O["trello"]["hazards"]
    hz.append(H("temporal", "T06", "trello", "Card has an action later than its dateLastActivity", th.get("card action later than dateLastActivity", {}).get("count", 0), th.get("card action later than dateLastActivity", {}).get("examples", []),
                "When seeding a Trello comment, bump dateLastActivity; avoid these cards for 'last touched' questions."))
    miss_beats = [m for b in B for m in b["missing"]]
    hz.append(H("temporal", "T07", "metadata", "Storyline YAML artifacts that do not exist in the base (incl. 3 Slack messages dated 2026-02-13 in #prototype)", len(miss_beats), miss_beats,
                "Never treat metadata/*.yaml as ground truth; the cited 2026-02-13 #prototype messages are absent from the export.", denominator="%d artifact ids in 451 beats" % sum(len(b["artifacts"]) for b in B)))
    # confluence activity after the person is otherwise silent
    late_conf = []
    for em, v in A["people"].items():
        la = v["last_activity_by_service"]
        conf = la.get("confluence")
        others = [d for s, d in la.items() if s not in ("confluence", "gcal_attended")]
        if conf and others and conf > max(others) and (datetime.date.fromisoformat(conf) - datetime.date.fromisoformat(max(others))).days > 30:
            late_conf.append("%s confluence %s vs other services last %s" % (em, conf, max(others)))
    hz.append(H("temporal", "T08", "confluence", "Confluence edits/comments dated >30 days after the author's last activity anywhere else (synthetic-looking authorship)", len(late_conf), late_conf,
                "Do not use Confluence authorship as evidence that someone was still active; check activity.json first."))
    strikes = SC["strikethrough_messages"]
    # ---------------- SEMANTIC / CATEGORY ----------------
    xs = GH["cross_series_refs"]
    hz.append(H("semantic_category", "S01", "github+linear", "match3d PRs that cite ENG-#### keys (Domino Delights series) instead of ZOM-###", xs["count"], xs["examples"],
                "ENG-n and ZOM-n are different issues; never join on the number alone.", denominator="%d PRs with a Linear key" % GH["prs_with_linear_key"]))
    hz.append(H("semantic_category", "S02", "linear", "Issues whose parent is in another team (cross-team epics: ART/DES children under EPI/ENG parents)", lh.get("parent in a different team (cross-team epic)", {}).get("count", 0),
                lh.get("parent in a different team (cross-team epic)", {}).get("examples", []), "Team-scoped cohorts must say whether children of other-team epics count."))
    hz.append(H("semantic_category", "S03", "linear", "Label vocabulary mixes sprint names, release codenames, platforms and categories (%s labels across teams)" % sum(LI["team_label_vocab_size"].values()), sum(LI["team_label_vocab_size"].values()),
                list(LI["team_labels"].get("ENG", {}).keys())[:10], "Never use a label as a category without an incorporated definition (e.g. 'Baklava Hot Fix' is a release, 'Bug' a type).", source="computed"))
    hz.append(H("semantic_category", "S04", "github", "GitHub user display names that disagree with the person (PERSON_2314 shows 'Ryan' but is Frederick Stone; two logins named 'Calvin Price'; 'Marcus' PERSON_0396)", 3,
                ["PERSON_2314_GITHUB_USERNAME", "PERSON_0003_GITHUB_USERNAME", "PERSON_2137_GITHUB_USERNAME", "PERSON_0396_GITHUB_USERNAME"], "Resolve GitHub authors through entities.json, never by display name.", source="computed+entities.json"))
    hz.append(H("semantic_category", "S05", "snowflake", "PAYROLL_ROSTER rows carry an undeclared 'title' key; roster roles disagree with persona briefs (EMPLOYEE_0032 'Josh Dempsey, product' vs Senior Unity Engineer; Frederick is_founder=false vs 'Co-founder')", 371,
                ["ROSTER-0001", "EMPLOYEE_0032", "EMPLOYEE_0008"], "Do not ask for job titles from Snowflake; if roles matter, cite one authority.", source="computed+Scenario_Atlas"))
    hz.append(H("semantic_category", "S06", "contacts", "Contacts job titles that differ from the roster (Leonard 'Co-founder & CEO' vs Creative Director; Robert 'CPO'; Frederick 'Commercial Lead')", 3,
                ["/contacts/170", "/contacts/108", "/contacts/139"], "Pick one authority for titles in the prompt.", source="Scenario_Atlas"))
    hz.append(H("semantic_category", "S07", "docs", "Gemini meeting notes misname the entity ('Robert Incorporated') in the wind-down notes", 1, ["f_0c37bb7235683d73569903"], "Keep entity-name questions off this doc.", source="Scenario_Atlas"))
    cf = O["confluence"]
    hz.append(H("semantic_category", "S08", "confluence", "Overlapping / contradictory Confluence pages: %s; page_live_ops_engine blames 'a deploy that leaves the job unscheduled' while page_liveops_calendar blames a generator date bug; page_quest_postmortem body says the auto-deploy 'was left running' while Arthur's comment says it 'stays off'; page_support_playbook insists the lives bug is not the scheduler stall; %d page versions are flagged synthesized" % (", ".join("%s~%s (Jaccard %.2f)" % (a, b, j) for a, b, j in cf["similar_page_pairs"]), cf["synthesized_versions"]),
                len(cf["similar_page_pairs"]) + 3, ["confluence:page_live_ops_engine", "confluence:page_liveops_calendar", "confluence:page_quest_postmortem", "confluence:comment_quest_postmortem_c1", "confluence:page_support_playbook", "confluence:page_qa_runbook", "confluence:page_release_checklist"],
                "Two pages stating different root causes as fact fail coherence on presence; use one as the authority by an incorporated rule, or keep both out.", source="computed+Scenario_Atlas"))
    # ---------------- CROSS-SERVICE REFERENTIAL ----------------
    lm = S["linear_mentions"]
    ghost = sorted([k for k in lm if k not in issues], key=lambda k: -lm[k][0])
    hz.append(H("cross_service_referential", "R01", "slack+linear", "Slack messages citing Linear keys that do not exist in Linear", sum(lm[k][0] for k in ghost),
                ["%s (x%d, e.g. slack:%s)" % (k, lm[k][0], lm[k][3]) for k in ghost[:10]], "Do not build a chain through these keys; if seeding a Slack mention, use an existing key.", denominator="%d distinct keys mentioned" % len(lm)))
    prm = S["pr_mention_counts"]
    ghost_pr = [k for k in prm if k not in pr_ids]
    hz.append(H("cross_service_referential", "R02", "slack+github", "Slack messages linking PRs that are not in the GitHub export", sum(prm[k] for k in ghost_pr), ["%s (x%d, e.g. %s)" % (k, prm[k], S["pr_mentions"][k][0]) for k in ghost_pr[:10]],
                "PR links outside the 16 repos (or deleted PRs) cannot be fetched.", denominator="%d distinct PR URLs" % len(prm)))
    known_repos = set(r for r, n in pr_by_repo_num)
    gm_ghost = [g for g in GM["github_mails"] if g[1] == "PR" and g[0] in known_repos and (g[0], g[2]) not in pr_by_repo_num]
    gm_red = [g for g in GM["github_mails"] if g[0] not in known_repos]
    hz.append(H("cross_service_referential", "R03", "gmail+github", "GitHub notification mails whose subject has the repo name redacted ('[[SOURCE_ORG_0001]-Games/[USERNAME_0351]] ...'): %d mails; mails naming a PR absent from the export: %d" % (len(gm_red), len(gm_ghost)), len(gm_red), [g[6] for g in gm_ghost[:6]] + [g[6] for g in gm_red[:4]], "The PR is recoverable only from the Message-ID (<org/repo/pull/N/...@github.com>); do not rely on subject parsing.",
                denominator="%d GitHub notification mails" % len(GM["github_mails"])))
    hz.append(H("cross_service_referential", "R04", "slack+drive", "Slack links to Google Docs/Sheets/Slides use Google-native ids (docs.google.com/.../d/1X...) that never equal the export's f_ ids", S["gdoc_links"], ["#winddown folder link 1XQAild72BAz_A-Wo-bvTBX7oZjygP53H (Scenario_Atlas)"],
                "A Slack link never resolves to a Drive record by id; a task must name the file by title or path. Seeded links should mimic this (Google-native id) and be paired with an exact title.", source="computed"))
    hz.append(H("cross_service_referential", "R05", "github", "Branch head_sha values are pre-rewrite SHAs (present only as commit_map.old_sha)", gh.get("branch head_sha is a pre-rewrite SHA (commit_map.old_sha), not in commits", {}).get("count", 0),
                gh.get("branch head_sha is a pre-rewrite SHA (commit_map.old_sha), not in commits", {}).get("examples", []), "Do not ask for the commit at a branch head; use PR head_sha.", denominator="2,011 branches"))
    hz.append(H("cross_service_referential", "R06", "github+slack", "GitHub-app Slack mirrors with no matching GitHub comment text (per PR, first 20 normalised chars; heuristic, includes CodeRabbit multi-part renders)",
                sum(GH["slack_comment_mirrors_without_github_record"]["counts"].values()), sum(GH["slack_comment_mirrors_without_github_record"]["examples"].values(), []),
                "A PR whose Slack mirror says more than GitHub (or vice versa) cannot carry a 'what did the review say' requirement; seed both sides together."))
    unm = sum(GH["github_comments_without_slack_copy_examples"].values(), [])
    rates = GH["comment_mirror_rates"]
    missing_copy = sum(v["github_records"] - v["with_slack_copy"] for k, v in rates.items() if "/review_" not in k)
    hz.append(H("cross_service_referential", "R07", "github+slack", "GitHub PR comments (inside a mirrored repo's window) with no Slack mirror copy", missing_copy, unm,
                "Mirror coverage is not 100%; do not claim 'every comment is in Slack'.", detail={k: v for k, v in rates.items()}))
    th = O["trello"]["hazards"]
    # gmail calendar invites vs gcal
    idx = O["gcal"]["mail_index"]
    inv_total = inv_dated = inv_match = 0
    inv_unmatched = []
    for kind, summ, when, mb, d, rid, frm in GM["calendar_mails"]:
        if kind not in ("Invitation", "Updated invitation", "Canceled event"):
            continue
        inv_total += 1
        dt = parse_invite_date(when)
        if not dt:
            continue
        inv_dated += 1
        key = norm_text(summ)
        hit = any((key + "|" + (dt + datetime.timedelta(days=o)).isoformat()) in idx for o in (-1, 0, 1))
        if hit:
            inv_match += 1
        elif len(inv_unmatched) < 10 and dt >= datetime.date(2024, 1, 1):
            inv_unmatched.append(rid + " (" + summ[:50] + " @ " + dt.isoformat() + ")")
    hz.append(H("cross_service_referential", "R08", "gmail+gcal", "Dated calendar-invitation mails (Invitation/Updated/Canceled) with no GCal instance of the same summary within +/-1 day", inv_dated - inv_match, inv_unmatched,
                "Invites and calendars were exported separately; an invite mail does not prove a GCal row exists (and vice versa). Seed both, or neither.", denominator="%d dated invite mails (of %d invite-type mails)" % (inv_dated, inv_total)))
    # linear auto-closed mails vs state
    ac = [x for x in GM["linear_mails"] if "auto-closed" in x[0]]
    ac_bad = []
    for x in ac:
        for kk in x[1]:
            st = (issues.get(kk) or [None, None])[1]
            if st and st not in ("Canceled", "Duplicate"):
                ac_bad.append("%s state=%s (%s)" % (kk, st, x[4]))
    hz.append(H("cross_service_referential", "R09", "gmail+linear", "Linear 'auto-closed ... changed the status to Canceled' mails whose issue is not Canceled in Linear", len(ac_bad), ac_bad,
                "Linear state at the clock wins over notification mail; avoid these issues if a task reads the mails.", denominator="%d auto-close mails" % len(ac)))
    # ---------------- QUANTITATIVE ----------------
    t = S["thread"]
    hz.append(H("quantitative", "Q01", "slack", "Thread parent reply_count != replies in export", len(t["reply_count_mismatch"]), ["%s claimed %s actual %s" % tuple(x) for x in t["reply_count_mismatch"]],
                "Keep these two threads out of 'how many replies' questions; when seeding replies, update reply_count/reply_users_count/latest_reply together.", denominator="%d parents with counters" % (t["parents"] - t["raw_parents_no_counters"])))
    hz.append(H("quantitative", "Q02", "slack", "Thread parent reply_users_count != distinct repliers", len(t["reply_users_mismatch"]), ["%s claimed %s actual %s" % tuple(x) for x in t["reply_users_mismatch"]], "As Q01."))
    hz.append(H("quantitative", "Q03", "slack", "Thread parent latest_reply != newest reply ts", len(t["latest_reply_mismatch"]), ["%s claimed %s actual %s" % tuple(x) for x in t["latest_reply_mismatch"]], "As Q01."))
    hz.append(H("quantitative", "Q04", "slack", "Raw-shaped thread parents with no reply_count/latest_reply at all (counter fields absent)", t["raw_parents_no_counters"], [], "Thread size for these parents must be counted from replies, not read from a field."))
    sh = O["snowflake"]["hazards"]
    burn = sh.get("MONTHLY_BURN total != FINANCE_LEDGER outflows for month", {})
    hz.append(H("quantitative", "Q05", "snowflake", "MONTHLY_BURN total != FINANCE_LEDGER outflows for the month", burn.get("count", 0), burn.get("examples", []),
                "Burn questions for 2023-09 have two answers; avoid or name the table.", denominator="35 burn months"))
    hz.append(H("quantitative", "Q06", "snowflake+sheets", "Snowflake CASH_BALANCE vs P&L sheets month-end cash differ by ~$33-37K in Sep-Nov 2025 (157,538 vs 194,133; 99,701 vs 137,855; 52,965 vs 85,868); the Jan-2026 P&L breaks internally (Dec end 52,686 vs Jan start 29,636)", 4,
                ["snowflake:CASH_BALANCE 2025-09-30", "sheets:f_605121f4a36752645e0ac3", "sheets:f_28ecc492b19f3696a19a97"], "System-vs-system: keep cash questions on ONE named source or make reconciliation the explicit job.", source="Scenario_Atlas"))
    hz.append(H("quantitative", "Q07", "slack+sheets+snowflake", "Vendor amounts quoted three ways: Helpshift balance $1,500/$1,200/$300; Sunset fee $11.7K/$13-15K/~$15K; Unity ~2.348x9 vs 1,200/mo; AWS ~$1k vs $1,550 vs $1,485 vs 0", 4,
                ["slack:C0ADGSZKR3R:1770673467.186629", "slack:C07C2866011:1770765511.243329", "slack:C04UEQVDVB7:1770765910.100299", "snowflake:FINANCE_LEDGER/FIN-000702", "docs:f_0c37bb7235683d73569903"],
                "Human claims vs records are legitimate A1 traps only if the task defines which record is authoritative.", source="Scenario_Atlas"))
    hz.append(H("quantitative", "Q08", "slack+snowflake+gmail", "UA claims vs warehouse: '$50K Adjoe / 10K installs' vs $46,202 / 8,730; 'CPI ~$5' vs Jan $7.02; Meta Feb receipts ~$1,257 vs ledger $956.45", 3,
                ["slack:publishing-ext 1764022591.269199", "snowflake:AD_SPEND_DAILY", "gmail:leonard@harmonygames.co_1856612239565121370.json"], "Same rule as Q07.", source="Scenario_Atlas"))
    mirrors_ok = [k for k in ("spend differs AD_SPEND_DAILY vs AD_SPEND", "spend differs AD_SPEND_DAILY vs UA_SPEND_UNIFIED_V2", "revenue differs REVENUE_DAILY vs _V2", "dau differs DAILY_ACTIVE_USERS vs DAILY_METRICS_AGG", "total revenue differs DAILY_METRICS_AGG vs REVENUE_DAILY", "HEADCOUNT vs PAYROLL_ROSTER line differs (cost/start/end/employee)", "review differs APP_STORE_REVIEWS vs STORE_REVIEWS (rating/text/date)") if k in sh]
    hz.append(H("quantitative", "Q09", "snowflake", "Mirrored warehouse tables checked row-by-row (AD_SPEND_DAILY/AD_SPEND/UA_SPEND_UNIFIED_V2, REVENUE_DAILY/_V2, DAU/DAILY_METRICS_AGG, HEADCOUNT/PAYROLL_ROSTER, APP_STORE_REVIEWS/STORE_REVIEWS, IAP/STORE_TRANSACTIONS): disagreeing pairs listed in examples (empty = all agree)", len(mirrors_ok),
                [k + ": " + str(sh[k]["count"]) for k in mirrors_ok] + [k + ": " + str(v["count"]) for k, v in sh.items() if k.startswith("IAP") or k.startswith("price")],
                "Mirrors agree, so a seeded row must be written to every mirror (and table comments that quote counts updated)."))
    cp = GC["classes"]
    hz.append(H("quantitative", "Q10", "gmail", "Same RFC message stored in 2+ mailboxes but with different content", cp.get("materially different (<0.80)", 0) + cp.get("partly different (0.80-0.97)", 0),
                GC["examples"].get("materially different (<0.80)", [])[:5] + GC["examples"].get("partly different (0.80-0.97)", [])[:5],
                "Differences are mostly Google-Groups footers, quoted-history truncation and differential redaction ('Harmony Games' vs [SOURCE_ORG_0001]); quote a mail from the persona's own copy only.",
                denominator="%d cross-mailbox copy pairs compared" % sum(cp.values()), detail={"classes": cp, "by_mailbox_pair": GC["by_pair"]}))
    gcd = O["gcal"]["copy_disagreements"]
    hz.append(H("quantitative", "Q11", "gcal", "Calendar copies of one instance (same ical_uid + start) that disagree (first differing field counted)", sum(gcd["counts"].values()), sum(gcd["examples"].values(), [])[:10],
                "Read the persona's own copy; never assert attendee lists or summaries from another calendar's copy.", denominator="%d instances" % O["gcal"]["instances"], detail=gcd["counts"]))
    # ---------------- STATE / LIFECYCLE ----------------
    for k, hid in (("issue in state PR but a referencing PR merged", "L01"), ("issue Canceled but a referencing PR merged", "L02"), ("issue Todo/Backlog but a referencing PR merged", "L03"), ("issue Done but every referencing PR unmerged", "L04")):
        v = lj.get(k, {"count": 0, "examples": []})
        hz.append(H("state_lifecycle", hid, "linear+github", k[0].upper() + k[1:], v["count"], ["%s / %s" % tuple(x) for x in v["examples"]], "Keep these issues out of cohorts whose predicate is 'shipped' or 'open'.", denominator="%d issues referenced by PRs" % GH["issues_with_pr_reference"]))
    for k, hid in (("completed_at set but state not Done", "L05"), ("parent Done while child open", "L06"), ("state 'PR' (awaiting merge)", "L07")):
        v = lh.get(k, {"count": 0, "examples": []})
        hz.append(H("state_lifecycle", hid, "linear", k[0].upper() + k[1:], v["count"], v["examples"], "Exclude from state-based cohorts or define the rule explicitly.", denominator="3,852 issues"))
    open_states = {"Done", "Canceled", "Duplicate"}
    dead = []
    for iid, r in issues.items():
        if r[1] in open_states or not r[2]:
            continue
        em = luser_email.get(r[2])
        st = status.get(em)
        if st and st.startswith("quiet_since"):
            dead.append("%s -> %s (%s)" % (iid, em, st))
    hz.append(H("state_lifecycle", "L08", "linear", "Open issues assigned to people who are quiet/departed at the clock (per activity.json)", len(dead), dead,
                "An 'owner' requirement on these issues points to someone who cannot act; seeded follow-ups must not come from them.", denominator="%d open issues" % sum(1 for r in issues.values() if r[1] not in open_states)))
    hz.append(H("state_lifecycle", "L09", "github", "Merged PRs with no review at all", gh.get("merged with no review at all", {}).get("count", 0), gh.get("merged with no review at all", {}).get("examples", []),
                "Avoid 'was it approved' criteria unless the review rule is incorporated.", denominator="2,498 merged PRs"))
    hz.append(H("state_lifecycle", "L10", "github", "Merged PRs whose only reviews are bot or COMMENTED (no human APPROVED)", gh.get("merged with no human APPROVED review (bot-only or comment-only)", {}).get("count", 0),
                gh.get("merged with no human APPROVED review (bot-only or comment-only)", {}).get("examples", []), "As L09; CodeRabbit (PERSON_6026, type Organization) reviews are not human approvals."))
    for k, hid in (("open card in closed (archived) list", "L11"), ("card in Done list with incomplete checklist items", "L12")):
        v = th.get(k, {"count": 0, "examples": []})
        hz.append(H("state_lifecycle", hid, "trello", k[0].upper() + k[1:], v["count"], v["examples"], "Exclude from list-based cohorts."))
    hz.append(H("state_lifecycle", "L13", "github+slack", "Work merged after the shutdown announcement (Combo-Fighters#37 merged 2026-02-13 by Oliver; CodeRabbit comment after cancellation); 16 repos never archived; 275 Linear issues still open", 3,
                ["github:harmonygames-Games/Combo-Fighters#37", "github:harmonygames-Games/Combo-Fighters#37#c_1", "slack:C05KNDCHAAG:1770842137.835489"], "'Everything stopped on Feb 9' is false; define the cut-off explicitly.", source="Scenario_Atlas"))
    hz.append(H("state_lifecycle", "L14", "snowflake+slack", "Warehouse rows 'completed' where Slack reports outages (EVT-0324/0325 29 Jun 2025; EVT-0592 27 Oct; EVT-0608/0625/0640/0656 Nov leaderboards)", 7,
                ["snowflake:LIVE_EVENT_PERFORMANCE/EVT-0324", "snowflake:LIVE_EVENT_PERFORMANCE/EVT-0592", "slack:C080X4GTZ0E:1751200739.524289", "slack:C080X4GTZ0E:1764532627.291559"],
                "System-vs-claim: allowed only if the task makes reconciling them the job.", source="Scenario_Atlas"))
    # ---------------- IDENTIFIER / FORMAT ----------------
    f = S["format"]
    hz.append(H("identifier_format", "I01", "slack", "Raw-shaped Slack records (no id, no reply_count; blocks + client_msg_id + user_profile)", f.get("raw-shaped record (no id/reply_count; blocks+client_msg_id)", 0),
                S["format_examples"].get("raw-shaped record (no id/reply_count; blocks+client_msg_id)", []), "Collision-check (channel, ts) before seeding; their DB id is not exported.", denominator="687,230 records"))
    hz.append(H("identifier_format", "I02", "slack", "Message id != sha256(channel|ts)[:32]", f.get("message id != sha256(channel|ts)[:32]", 0), S["format_examples"].get("message id != sha256(channel|ts)[:32]", []), "Mint ids with the sha rule anyway."))
    hz.append(H("identifier_format", "I03", "gmail", "Thread file name uses a mailbox alias different from user_email (leonard@ -> leonard.hayes@, blake@ -> arthur.blake@, jlawson@ -> julia.lawson@ ...)", GM["format"].get("file-name mailbox alias != user_email (e.g. leonard@ vs leonard.hayes@)", 0),
                ["%s -> %s (%d)" % tuple(x) for x in GM["alias_pairs"] if x[0] != x[1]][:10], "Search by both alias and roster address.", denominator="88,726 files"))
    hz.append(H("identifier_format", "I04", "gmail", "Mixed date formats (RFC-2822 vs ISO-Z) across messages", GM["date_formats"].get("RFC-2822", 0), [str(GM["date_formats"])], "Normalise before comparing; seeded rows follow the sibling's format."))
    hz.append(H("identifier_format", "I05", "gmail", "Mailboxes whose owner is a token (EMPLOYEE_0011_EMAIL, EMPLOYEE_0020_EMAIL, EMPLOYEE_0032_EMAIL, SVC_0009_EMAIL, SVC_0019_EMAIL, SVC_0293_EMAIL)", 6,
                [k for k in GM["mailboxes"] if "@" not in k], "No persona can read these; do not place evidence there."))
    hz.append(H("identifier_format", "I06", "gmail", "Re:/Fwd: subjects without in_reply_to/references", GM["format"].get("Re:/Fwd: subject without in_reply_to/references", 0), [], "Seeded replies need in_reply_to + references."))
    hz.append(H("identifier_format", "I07", "github", "Bot comments whose author_login differs from the paired timeline actor_login (CodeRabbit PERSON_6026 vs SVC_0321; linear[bot] PERSON_6028 vs SVC_0323)", gh.get("comment author_login != timeline actor_login (bot token split)", {}).get("count", 0),
                gh.get("comment author_login != timeline actor_login (bot token split)", {}).get("examples", []), "A seeded bot comment must copy this split exactly; counting 'comments by X' differs by table."))
    hz.append(H("identifier_format", "I08", "github+slack", "GitHub logins are tokens; the Slack GitHub-app mirror shows real logins (EMPLOYEE_0025 -> arthur.blake, PERSON_5877 -> owen.baker, PERSON_0396 -> MarcusBennett)", len(GH["login_to_slack_mirror_actor"]),
                ["%s -> %s" % (k, list(v)[0]) for k, v in list(GH["login_to_slack_mirror_actor"].items())[:10]], "Seeded mirrors must use the real login style; seeded GitHub rows the token."))
    hz.append(H("identifier_format", "I09", "slack", "GitHub-app mirror copies with the org redacted ('[SOURCE_ORG_0001]-Games/...')", GH["slack_mirror"]["org_redacted_copies"], [], "Search for repo names, not the org string."))
    hz.append(H("identifier_format", "I10", "linear", "Linear user ids that are not usr_<16hex> ('usr_Victor Barnes' with a space, 'usr_Robert', 'usr_Lucas', 'usr_EMPLOYEE_0024')", lh.get("user id contains a space (usr_Victor Barnes)", {}).get("count", 0),
                lh.get("user id contains a space (usr_Victor Barnes)", {}).get("examples", []), "Quote ids exactly; never derive them."))
    gch = O["gcal"]
    hz.append(H("identifier_format", "I11", "gcal", "Same calendar holds two rows for one meeting start (recurring master with rrule + a standalone instance row)", gch["duplicate_copy_same_calendar"]["count"], gch["duplicate_copy_same_calendar"]["examples"],
                "Counting meetings by rows double-counts; count by (ical_uid, start) per calendar."))
    hz.append(H("identifier_format", "I12", "gcal", "ical_uid + start shared by different meetings (summary differs between copies)", gcd["counts"].get("summary", 0), gcd["examples"].get("summary", []), "Never join calendar copies on ical_uid alone."))
    hz.append(H("identifier_format", "I13", "gcal", "Instances with a copy on a calendar whose owner is not an attendee", gch["instances_with_copy_on_non_attendee_calendar"]["count"], gch["instances_with_copy_on_non_attendee_calendar"]["examples"], "Visibility != invitation; do not infer attendance from presence on a calendar."))
    dh = O["drive"]["hazards"]
    hz.append(H("identifier_format", "I14", "drive", "owner_email is not an email ('Resource: -6481757892984311338', 'Resource: 7240535625619857401' ...)", dh.get("owner_email is not an email (Resource:/token)", {}).get("count", 0), dh.get("owner_email is not an email (Resource:/token)", {}).get("examples", []),
                "Resource-owned files with empty sharing (%d) are readable by no persona." % O["drive"]["unreadable_resource_owned_no_share"], denominator="53,866 drive rows"))
    nat = O["native"]
    hz.append(H("identifier_format", "I15", "drive+docs+sheets", "Drive name keeps the source extension while the Docs/Sheets title does not ('Creative Concepts.docx' vs 'Creative Concepts')", nat["docs"]["mirror_mismatch"].get("title != drive name", 0) + nat["sheets"]["mirror_mismatch"].get("title != drive name", 0),
                nat["docs"]["mirror_examples"].get("title != drive name", [])[:5], "Search both forms; a seeded native file should follow the same split. Sharing, owner and modified_time agree on all 633 docs, 398 sheets and 164 slides."))
    hz.append(H("identifier_format", "I16", "trello", "Action ids whose embedded timestamp != action date (Welcome Board template rows)", th.get("action id timestamp != action date", {}).get("count", 0), th.get("action id timestamp != action date", {}).get("examples", []), "Mint Trello ids from the record's own time."))
    hz.append(H("identifier_format", "I17", "trello", "Trello list names and members redacted to tokens ('[PERSON_NAME_35449]' lists on DD Product Roadmap; Leonard is PERSON_6094_TRELLO_USER_ID)", 6,
                [l["name"] for l in O["trello"]["lists"].values() if "PERSON_NAME" in l["name"]], "Name lists by id in tasks."))
    hz.append(H("identifier_format", "I18", "slack", "In-place retractions written as ~strikethrough~ (claims withdrawn inside the same message)", strikes["count"], ["slack:%s:%s" % (x[0], x[1]) for x in strikes["examples"][:10]],
                "A struck-through clause is not a live claim; never quote it as one.", detail=strikes["by_year"]))
    cats = collections.defaultdict(list)
    for h in hz:
        cats[h["category"]].append(h)
    out = {"_meta": {"generated_by": "Task_Authoring/references/universe_kb/_build/assemble_hazards_traps.py", "clock": "2026-02-14T00:00:00Z",
                     "use": "Pre-existing inconsistencies. The Evals fail Cross-Service Coherence on any inconsistency in task-touched data, so keep these records out of a task's scope, or make reconciling them the explicit, incorporated job.",
                     "sources": "kb_cache passes over every export (computed) plus Scenario_Atlas.md items re-cited with ids (source=Scenario_Atlas).",
                     "checked_and_clean": ["Slack: 0 orphan reply groups, 0 replies earlier than parent, 0 messages on/after clock, 0 posts by unknown users",
                                           "Linear: 0 Done without completed_at, 0 Canceled without canceled_at, 0 dates after clock, 0 missing parents/assignees",
                                           "GitHub: 0 merged without merged_at, 0 merged_at < created_at, every PR comment has a 'commented' timeline event",
                                           "Confluence: versions contiguous, latest version == page body/title on all 31 pages",
                                           "Trello: badges.comments/checkItems agree with actions/check items on all 803 cards",
                                           "GCal: 0 end<=start, every copy has self:true on the owner, 0 instances missing an attendee copy",
                                           "Drive family: sharing/owner/modified agree between Drive and Docs/Sheets/Slides rows",
                                           "Snowflake: CASH_BALANCE rolls forward (cash_n = cash_n-1 - monthly_net_burn) for all 34 months; mirrored tables agree row-for-row"]},
           "categories": {k: v for k, v in cats.items()}, "index": [{"id": h["id"], "category": h["category"], "title": h["title"], "count": h["count"]} for h in hz]}
    jdump(out, OUT + "/coherence_hazards.json", indent=1)

    # ================= TRAPS =================
    traps = []
    def T(tid, kind, title, ids, risk, legit_use, count=None, detail=None, source="computed"):
        traps.append({"id": tid, "kind": kind, "title": title, "count": count, "ids": ids[:12] if isinstance(ids, list) else ids, "risk": risk, "legitimate_use": legit_use, "source": source, **({"detail": detail} if detail else {})})
    col = E.get("collisions", {})
    T("P01", "lookalike_people", "Shared first names across people and tokens (entities.json collisions)", [f"{k}: {v}" for k, v in list(col.get("shared_first_names", {}).items())[:10]],
      "An agent resolves 'Marcus'/'Claire'/'Thomas' to the wrong person or the wrong mailbox.", "Ask for the person by role or by a record they authored; make the right one decidable by an exact email/id in an incorporated record.", count=len(col.get("shared_first_names", {})), source="entities.json")
    surn = collections.defaultdict(set)
    for em, v in A["people"].items():
        nm = (v.get("name") or "").split()
        if len(nm) >= 2:
            surn[nm[-1].lower()].add(v["name"] + " <" + em + ">")
    sh_ = {k: sorted(v) for k, v in surn.items() if len(v) > 1}
    T("P02", "lookalike_people", "Shared surnames (Bennett: Marcus/Oscar; Brooks: Oliver/Lauren; Baker: Owen/Thomas Baker; Lawson: Julia/Peter; Price: Calvin/Nathan)", [f"{k}: {v}" for k, v in sh_.items()],
      "Surname-only references ('Bennett said…', 'Brooks's PR') resolve wrongly.", "Use surname-only mentions in seeded human messages only when a second record disambiguates.", count=len(sh_))
    T("P03", "lookalike_people", "marcus@harmonygames.co mailbox (a different Marcus, shown as 'Marcus Bennett <marcus@…>') vs persona Marcus Bennett (no mailbox) vs Marcus Lee (UA)", ["gmail mailbox marcus@harmonygames.co", "slack EMPLOYEE_0002_SLACK_ID", "linear usr_d7ae9de750a5640a", "linear usr_b501f018a4c5319f"],
      "Mail evidence attributed to Marcus Bennett is really another person's.", "A trap where the agent must notice the address, not the display name.", source="Ask_Carriers+entities.json")
    T("P04", "lookalike_people", "Tokenised GitHub contributors whose real login only appears in the Slack GitHub-app mirror", ["%s -> %s" % (k, v) for k, v in GH["login_to_slack_mirror_actor"].items()],
      "Authorship questions answered from GitHub alone return tokens; mirrors reveal real logins (sometimes redacted again: '[PERSON_NAME_0212]').", "Authorship chains that require joining a PR to its Slack mirror (record-level join).", count=len(GH["login_to_slack_mirror_actor"]))
    both = sorted(int(k.split("-")[1]) for k in issues if k.startswith("ZOM-") and ("ENG-" + k.split("-")[1]) in issues)
    pairs = [["ENG-%d" % n, (issues["ENG-%d" % n][10] or "")[:50], "ZOM-%d" % n, (issues["ZOM-%d" % n][10] or "")[:50]] for n in both[::max(1, len(both) // 10)][:10]]
    T("N01", "ticket_series_collision", "ENG-n and ZOM-n both exist for %d numbers (every ZOM number has an unrelated ENG twin); ART/DES/EPI numbers overlap too" % len(both), pairs,
      "A bare number ('ticket 412') or a mis-keyed PR (S01) lands on the wrong issue.", "Use full keys in prompts; a trap that relies on a team-key mismatch must be decidable by title/assignee.", count=len(both))
    numoverlap = sum(1 for (r, n) in pr_by_repo_num if r == "GameOfDominoes" and ("ENG-%d" % n) in issues)
    T("N02", "ticket_series_collision", "GameOfDominoes PR numbers overlap ENG issue numbers (#1458 vs ENG-1458) and Helpshift issue numbers (#118)", ["github:harmonygames-Games/GameOfDominoes#1458", "linear:ENG-1458", "gmail helpshift issue #118 00000543.json"],
      "'#1458' is ambiguous across three systems.", "Name the system with every number.", count=numoverlap)
    T("N03", "ticket_series_collision", "Branch keys without hyphen ('ENG1229QuestCollectChapterRewards') and redacted owners ('[PERSON_NAME_0067]/ENG-1622-1')", GH["conventions"]["branch_examples"].get("first.last/<Desc>", [])[:5] + GH["conventions"]["branch_examples"].get("[PERSON_NAME_n]/<desc> (redacted owner)", [])[:5],
      "Regex joins on 'ENG-\\d+' miss hyphen-less branch keys.", "Linear<->GitHub reconciliation through branch names is real friction (links_json is empty on all issues).")
    # near-duplicate titles across owners
    dups = [d for d in O["drive"]["duplicate_titles"] if len(d["owners"]) > 1]
    T("D01", "near_duplicate_documents", "Drive titles that normalise to the same name under different owners (%d groups; %d groups overall)" % (len(dups), O["drive"]["duplicate_title_groups"]),
      [{"norm": d["norm"], "owners": d["owners"][:4], "ids": [x[0] for x in d["files"][:4]]} for d in dups[:12]],
      "Search returns the wrong owner's copy; persona may only see one of them.", "A12-style decoy: same purpose, different issuer; the incorporated rule (owner/date/scope) decides.", count=len(dups))
    bh = collections.defaultdict(list)
    for r in nat["docs"]["rows"]:
        if r[4] > 200:
            bh[r[5]].append(r)
    same_body = [[x[0] for x in v][:4] + [v[0][1][:40]] for v in bh.values() if len(v) > 1]
    T("D02", "near_duplicate_documents", "Docs with identical bodies under different ids/owners", same_body, "Two ids, one content: citing either may be judged wrong if the rubric names one.", "Pick the persona-readable copy explicitly.", count=len(same_body))
    sh2 = collections.defaultdict(list)
    for r in nat["slides"]["rows"]:
        sh2[norm_title(r[1])].append(r)
    deck_groups = [[x[0] for x in v][:6] + [v[0][1]] for k, v in sh2.items() if len(v) > 2]
    T("D03", "near_duplicate_documents", "Slide decks that share a title family (Weekly Update, publisher pitch decks, BoD decks)", deck_groups[:12], "Eleven 29-page publisher decks and many 'Weekly Update' decks look alike.", "Per-deck differences (partner name, date) are legitimate evidence; define which deck governs.", count=len(deck_groups))
    ssh = collections.defaultdict(list)
    for r in nat["sheets"]["rows"]:
        ssh[norm_title(r[1])].append(r)
    sheet_groups = [{"norm": k, "ids": [x[0] for x in v][:5], "owners": sorted(set(x[2] or "" for x in v))[:4], "titles": sorted(set(x[1] for x in v))[:4]} for k, v in ssh.items() if len(v) > 1 and len(k) > 3]
    T("D04", "near_duplicate_documents", "Spreadsheets whose titles normalise to the same name (P&L versions, investor lists, KPI exports)", sheet_groups[:12], "Agent reads the wrong version or owner.", "Stale-vs-current trap: same title family, the governing one picked by an incorporated rule (latest closed month, owner).", count=len(sheet_groups))
    stale = [d for d in O["drive"]["duplicate_titles"] if any(re.search(r"(?i)\b(v\d|final|draft|old|copy of|updated|new)\b", n) for n in d["distinct_names"])]
    T("D05", "stale_vs_current", "Drive title families with version markers (v1/v2/final/draft/copy of/updated)", [{"names": d["distinct_names"][:4], "ids": [x[0] for x in d["files"][:4]], "modified": [x[3] for x in d["files"][:4]]} for d in stale[:12]],
      "'final' is not the latest; latest is not authoritative.", "Supersession traps: make the winning version decidable by an incorporated rule, never by the label (Hardness_Mastery §2.6 #4).", count=len(stale))
    cpages = {pid: p for pid, p in O["confluence"]["pages"].items() if p["version"] and p["version"] > 1}
    T("D06", "stale_vs_current", "Confluence pages with version history and edit messages (old bodies readable via get_page_version / diff)", [{"page": pid, "versions": p["version"], "messages": p["version_messages"][:2]} for pid, p in list(cpages.items())[:12]],
      "An agent quoting v1 of a page reports a superseded fact.", "Effective-date regimes: the version in force at a record's date decides.", count=len(cpages))
    T("D07", "stale_vs_current", "Trello roadmap is stale against Linear (boards quiet since 2025-11-13; Linear last issue created 2025-11-07, updated to 2026-01-28)", [b["name"] + " last " + (b["last_activity"] or "")[:10] for b in O["trello"]["boards"].values()],
      "Roadmap status on Trello disagrees with Linear state.", "Ask which system governs status in the prompt.")
    T("D08", "stale_vs_current", "P&L workbook versions project different zero-cash months (Jun, Jul, Sep-30, Oct, Jan versions)", ["sheets:f_846ac…", "sheets:f_a5e9…", "sheets:f_dd0b…", "sheets:f_28ecc492b19f3696a19a97", "sheets:f_605121f4a36752645e0ac3"],
      "Latest-is-right fails if the question is 'what did the board see in October'.", "Board-date-scoped questions.", source="Scenario_Atlas")
    cand = [c for c in S["corrections"] if c["marker"] in ("correction", "scratch that", "my bad", "i was wrong", "turns out", "false alarm", "not true", "disregard", "that's wrong", "thats wrong", "ignore that", "ignore my", "revert that", "reverted that", "typo") and float(c["reply_ts"]) >= 1704067200]
    T("C01", "superseded_claims", "Thread replies that correct or retract (marker phrases; heuristic candidates from %d marker hits, %d strong markers since 2024)" % (len(S["corrections"]), len(cand)),
      [{"thread": "slack:%s:%s" % (c["channel"], c["thread_ts"]), "reply": c["reply_ts"], "marker": c["marker"], "parent": (c["parent"] or "")[:90], "reply_text": c["reply"][:90]} for c in cand[:12]],
      "An agent that reads only the parent reports the withdrawn claim.", "A14 behavioural trap: put the correction in a reply (most runs never open replies). Verify each candidate by reading the thread; markers are noisy.", count=len(cand))
    T("C02", "superseded_claims", "Thread parent states a resolution ('done', 'fixed', 'deployed') and another person replies it still fails", [{"thread": "slack:%s:%s" % (p["channel"], p["thread_ts"]), "reply": p["reply_ts"], "parent": p["parent"][:90], "reply_text": p["reply"][:90]} for p in SC["parent_claim_overturned_by_other"]][:12],
      "Parent says fixed; replies say not.", "Strongest natural precedent for 'conclusion overturned in replies' (e.g. mpdm 1750275343.826629 'Deployment done…' -> 'still not working').", count=len(SC["parent_claim_overturned_by_other"]))
    T("C03", "superseded_claims", "Struck-through in-place retractions (~text~)", ["slack:%s:%s" % (x[0], x[1]) for x in strikes["examples"][:12]], "Struck text read as a live statement.", "Seeded supersession inside one message; low realism risk because the base has %d." % strikes["count"], count=strikes["count"])
    T("C04", "superseded_claims", "Documented human-claim vs record contradictions (quest auto-deploy 'stays off' vs postmortem 'left running'; postmortem 'resolved 18 Nov' vs 'broken again 19 Nov'; 'exclusive launch' vs non-exclusive licence; CPI ~$5 vs $7.02; Sherwood consulted but Sunset signed)",
      ["confluence:page_quest_postmortem", "slack:C080X4GTZ0E:1732005140.008099", "slack:C09Q4S613CN:1762361357.317589", "slack:C0ADGSZKR3R:1770931777.561519", "gmail:leonard@harmonygames.co_1856688113228112603.json"],
      "Latest/most senior statement is not automatically right.", "A1 traps framed as dated human claims overturned by records.", source="Scenario_Atlas")
    # bot noise
    si = S["integrations"]
    T("B01", "bot_noise", "Slack bot volume by integration", {k: v["n"] for k, v in sorted(si.items(), key=lambda kv: -kv[1]["n"]) if v["n"] >= 10},
      "Bot messages swamp channel histories and searches (#builds ~38K, #[ORG]-monkey ~15K, #engineering-bots ~10K).", "Volume that must be filtered, not read; never place a load-bearing fact in a bot-shaped message unless the integration's exact shape is copied (integrations.json).", count=sum(v["n"] for v in si.values()))
    top_mail = collections.Counter()
    for p in GM["subject_patterns"]:
        if p["sender"] != "<internal>":
            top_mail[p["sender"]] += p["n"]
    T("B02", "bot_noise", "Gmail automated senders (Firebase App Distribution svc_0107 ~44K, TestFlight/App Store Connect svc_4131, Crashlytics svc_2398, Linear svc_0251, Helpshift svc_0143, GitHub svc_0248, Slack svc_0240, Meta svc_0521, SVB svc_4249)",
      dict(top_mail.most_common(15)), "Inbox searches return notification floods; tokenised senders hide the service name.", "Decode senders via subject patterns (conventions.json gmail.subject_patterns).", count=sum(top_mail.values()))
    T("B03", "bot_noise", "GitHub bot activity: CodeRabbit (PERSON_6026, Organization) %d PR comments, %d review comments, %d reviews; linear[bot] %d PR comments" % (len(cr_comments), len(cr_rc), len(cr_rev), len(linbot_comments)),
      ["github:" + c["id"] for c in cr_comments[:3]] + ["github:" + c["id"] for c in linbot_comments[:3]], "Bot reviews look like approvals; bot comments dominate PR conversation.", "Criteria about human review must exclude bots explicitly.")
    T("B04", "bot_noise", "Jenkins in #builds: %d job messages + %d build-script messages; statuses %s" % (si.get("jenkins", {}).get("n", 0), si.get("jenkins_buildscript", {}).get("n", 0), si.get("jenkins", {}).get("detail")),
      si.get("jenkins", {}).get("samples", []), "'Unknown after N' and 'Started' rows look like failures/successes.", "Build-history questions need the status vocabulary defined.")
    T("B05", "bot_noise", "Helpshift issues via Zapier in #issuefeed often have empty payloads ('#ZapierBot: Issue Update has arrived. author: ; Message:')", si.get("zapier_helpshift", {}).get("samples", []),
      "Counts of 'issues' from Slack differ from Helpshift mails.", "Use Gmail Helpshift mails as the issue-of-record; Slack is noise.", count=si.get("zapier_helpshift", {}).get("n"))
    # redaction
    T("X01", "redaction", "Redaction tokens by service", {"slack_human": S["redaction"].get("human"), "slack_bot": S["redaction"].get("bot"), "gmail": GM["redaction"]},
      "Names, orgs, emails, phones and ids replaced by [PERSON_NAME_n], PERSON_n_<FIELD>, [SOURCE_ORG_n], [EMAIL_n], [IDENTIFIER_n]: name resolution, joins and full-text search break (searching 'Harmony Games' misses '[SOURCE_ORG_0001]' copies).",
      "Never build unique ground truth on a token; a token can be a legitimate 'unresolvable – say so' trap.", detail={"slack_examples": S["redaction_examples"].get("human"), "gmail_examples": GM["redaction_examples"]})
    T("X02", "redaction", "Same token used for different things across services (EMPLOYEE_0032 is a Slack user, a Gmail mailbox, Josh Dempsey in PAYROLL_ROSTER and a GitHub login; numbers do not align: Brian is EMPLOYEE_0026 in Slack but PERSON_0180 in GitHub)",
      ["EMPLOYEE_0032_SLACK_ID", "EMPLOYEE_0032_EMAIL", "EMPLOYEE_0032_GITHUB_USERNAME", "snowflake PAYROLL_ROSTER EMPLOYEE_0032", "PERSON_0180_GITHUB_USERNAME"], "Joining on token numbers is wrong.", "Only exact email / Slack id joins (entities.json).", source="computed+entities.json")
    T("X03", "redaction", "Redacted values inside structured data: HG Costs line '[PERSON_NAME_0499]' (= Singular), Trello list names, branch owners, Linear users PERSON_2218/3138/3233", ["sheets:f_605121f4a36752645e0ac3 HG Costs", "trello lists", "github head_ref [PERSON_NAME_0067]/ENG-1622-1"],
      "Aggregations by vendor or owner silently drop redacted rows.", "Make the agent infer the vendor from amount/cadence only if a record states the mapping.", source="computed+Scenario_Atlas")
    T("X04", "redaction", "Company name masked unevenly across copies of the same mail ('Harmony Games' vs '[SOURCE_ORG_0001]')", GC["examples"].get("differs only by redaction tokens / company-name masking", [])[:6],
      "Exact-quote rubrics fail depending on which mailbox copy the agent read.", "Quote-free criteria, or the persona's own copy.", count=GC["classes"].get("differs only by redaction tokens / company-name masking"))
    # similar containers
    fc = [c for c in chans.values() if (c.get("name") or "").startswith("FC:")]
    T("K01", "lookalike_containers", "Canvas pseudo-channels named 'FC:<file id>:<title>' (32) and per-title channel families (god-* vs zombie-*), 90 archived channels",
      [c["id"] + " " + c["name"][:50] for c in fc[:8]] + ["C05V5FNLB9V god-bugs", "C08R27X0EAH zombie-bugs"], "Searching 'bugs' or 'season pass issues' returns sibling containers for another game.", "Distractor containers with the same vocabulary.", count=len(fc))
    T("K02", "lookalike_containers", "App-name lineage: GoD -> Domino Delights -> '[ORG] DD' -> 'Harmony Games DD'; 'Puzzles vs Zombies' / 'Match 3D' / 'Zombie Game 3D' -> Zombie Match 3D; 'Combo Fighter' vs repo 'Combo-Fighters'; TestFlight-only 'Domino Adventure' (2023-12..2024-09) and 'Trump Billionaires Club' (2026-01-20..02-13)",
      ["gmail distribution 'GoD iOS' 2023-04", "testflight 'Puzzles vs Zombies' 2025-03..07", "testflight 'Trump Billionaires Club' 2026-01-20"], "Name-based counts across eras undercount.", "Rename-aware questions (one record states the rename).")
    T("K03", "lookalike_containers", "Calendar lookalikes: two 'All Hands' on 2025-10-24 (16:00Z and 16:30Z); recurring master + instance duplicates; reused ical_uids", ["gcal:evt_0a0658fbb9bbebae7f962a", "gcal:evt_11530fad245bf030e8563b"] + ["%s/%s" % (x[0], x[2]) for x in gch["duplicate_copy_same_calendar"]["examples"][:4]],
      "Wrong meeting chosen.", "Meeting-selection traps decided by attendees or time.", source="Scenario_Atlas+computed")
    tcat = collections.defaultdict(list)
    for t_ in traps:
        tcat[t_["kind"]].append(t_)
    outt = {"_meta": {"generated_by": "Task_Authoring/references/universe_kb/_build/assemble_hazards_traps.py", "clock": "2026-02-14T00:00:00Z",
                      "use": "Natural traps already in the data. Use them only as traps whose correct resolution is decidable from incorporated records; heuristic lists (C01, C02) must be read before use."},
            "kinds": dict(tcat), "index": [{"id": t_["id"], "kind": t_["kind"], "title": t_["title"], "count": t_["count"]} for t_ in traps]}
    jdump(outt, OUT + "/trap_catalog.json", indent=1)
    # stats reused by integrations
    jdump({"invites": {"total_invite_type": inv_total, "dated": inv_dated, "matched": inv_match}, "linear_bot_comments": len(linbot_comments),
           "linear_bot_prs": sorted(set(c["pr_id"] for c in linbot_comments)), "coderabbit": [len(cr_comments), len(cr_rc), len(cr_rev)]}, CACHE + "/kb_join_stats.json")
    print("hazards", len(hz), "traps", len(traps))


if __name__ == "__main__":
    main()
