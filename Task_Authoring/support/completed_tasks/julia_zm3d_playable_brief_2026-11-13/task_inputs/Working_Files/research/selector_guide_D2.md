# Selector guide for the D2 gradable surface (julia_zm3d_playable_brief)

Source: `Task_Authoring/tools/surface_grader.py` (`compare` L101, `_content_strings` L692, `decode` L715, `grade` L876), `Task_Authoring/tools/trajectory_ledger.py` (`norm` L89, `_keyed_rows` L638, `table` L662, `printed_totals` L793), `Task_Authoring/tools/gradable_surface.py` (`sample_from_regex` L426, `_dry_run` L576, `validate` L979), `Task_Authoring/tools/rubric_skeleton.py` (`build_rows` L414). Every slot below was built in memory and run through `gradable_surface.validate`, `gradeable_report`, `surface_grader.decode` and `grade` (no file written); "tested" means that run. Where the grader cannot express an outcome, that is said plainly.

## 0 Five facts that decide everything else

1. **Identifier parameters are never text.** For a `json_text` deliverable the grader reads every string of every successful call of that tool, joined by newlines, except values under a key that ends in `id` or `ids` and the keys `channel`, `ts`, `thread_ts`. So `id`, `issueId`, `parentId`, `fileId`, `documentId`, `spreadsheetId`, `channel_id` are invisible to a `text` selector. D1's `.*ART-806.*[Tt]odo.*` and `.*ART-840.*` can never match a real run.
2. **One deliverable, one tool.** `tool` is a single name; the only alias is `slack_conversations_add_message` for `slack_send_message`. A `text` slot reads one deliverable. There is no "either tool" slot.
3. **Only one `text`-kind deliverable is used** (the first declared). It tracks one Linear issue (`issue`), or every update of the tool when `issue` is absent. So one ticket's final state is gradable, not five.
4. **`validate` proves only that some payload could satisfy the slot.** The fixture for a `text` slot writes a string synthesised from the regex under the keys `text`, `body` and `message` of the declared tool. It does not know the tool's real parameters, which is why D1 validated. It also writes the sample three times, so an anchored exact-count regex fails validation.
5. **`"gradable": false` does not pass `validate`** (tested: `UNGRADED with a fixture built for it`). A slot the grader cannot read has to stay out of the surface and live only in the rubric.

## 1 A named ticket is moved to Todo (`linear_update_issue`, key in `id`)

Expressible for **one** ticket.

```json
"deliverables": { "ticket_806": {"kind": "text", "tool": "linear_update_issue", "issue": "ART-806", "key_regex": "ART-\\d{3}"} }

{"id": "W4", "title": "ART-806 (Washing Machine) back to Todo", "weight": 3, "work_kind": "interpretation",
 "work_reason": "applies that line's Owed call to its own ticket", "class": "delivery", "role": "core",
 "selector": ["delivery", "tracker_state", "Todo$"], "mechanisms": ["EXPORT"]}
```

- Reads the successful `linear_update_issue` calls whose `id` (or `issueId`) equals `ART-806` exactly, takes the last one that carries `state` or `stateId`, and runs `re.match(arg, state, re.I)`.
- Passes (tested): `Todo`, `todo`, `stateId: "Todo"`; Todo on ART-806 followed by any update of another ticket.
- Fails (tested): ART-806 set to Todo and later to Done; only another ticket moved; `ART-8060`; a failed call. With `"Todo"` instead of `"Todo$"`, `Todo (reopened)` also passes (prefix match).
- The argument must not look like a Trello id (24 hex, or `T-12`) and must not be `comment`, `description` or `state` (those switch to a Trello check).
- With `issue` left out, the same slot means "the last state-setting update of any ticket set Todo" (tested: passes when only ART-807 moved).
- Pick the ticket on the weightiest mechanism. The other four D1 move samples (W5 to W8) are not expressible; the line's `State` cell on the sheet already grades the decision.

## 2 Exactly N tickets moved to Todo

Not expressible. There is no state-set or call-count selector. The closest three, with limits:

| Option | Slot | What it really checks | Limits |
|---|---|---|---|
| a. at least N | `["text", "updates", "(?:Todo[\\n ]*){48}"]` with `"updates": {"kind": "json_text", "tool": "linear_update_issue"}` | 48 or more successful update calls in a row whose only non-id string is `Todo` | Tested: 48 passes, 47 fails, 49 and 97 pass (no upper bound). Any other string in an update (a `description`, an `assignee`) breaks the run of Todos and fails a correct run. Counts calls, not distinct tickets. The anchored form `^(?:Todo[\\n ]*){48}$` grades exact calls on a real run but **fails validate** (fact 4). |
| b. a list the agent writes | `["tracker_count", "back to todo", 48]` and `["tracker_lists", "back to todo", "ART-806"]` with the `text` deliverable pinned to `ART-793` | exactly 48 distinct `ART-\d{3}` keys listed under a heading that matches, in the pack ticket's **description** | Tested: bullets or one comma list pass; 47 keys fail. Needs the notes to ask for that list on the pack ticket (a new write), needs `truth_fields.groups`, and uses up the single `text` deliverable, so option 1 above is lost. A comment on the pack ticket is not read; only `description` and patch text are. |
| c. the sheet | `["total", "Owed"]` | 54 Owed rows on the list | It grades the list, not the tickets. |

The exclusion ("Delivered and Ready tickets untouched") has no selector at all. Keep it as a rubric row.

## 3 A comment on a named ticket whose body matches

The ticket cannot be required (`issueId` is stripped). What is expressible: some comment body matches.

```json
"deliverables": { "comments": {"kind": "json_text", "tool": "linear_create_comment"} }

{"id": "K1", "title": "comment that states the empty-shell re-export", "weight": 3, "work_kind": "interpretation",
 "work_reason": "the comment carries what is owed for the batch-exported lines", "class": "write_content", "role": "core",
 "selector": ["text", "comments", "empty shell|one at a time|multi.?select"], "mechanisms": ["EXPORT"]}
```

- `re.search(regex, all comment bodies joined by "\n", re.I | re.S)`. Passes if any successful comment, on any ticket, matches.
- Bind it to the decision through words only a run that found the record would write. `.` crosses comment boundaries (re.S), so `Brian.{0,80}shell` can pair words from two comments. A same-line gap such as `[ -~]{0,80}` stays inside one line but failed in test when the owner sat on the next line of the same comment.
- D1's W12 (`.*ART-840.*`, "a comment exists on the Wooden Crate ticket") has no equivalent. A body regex on that line's own words (`prefab`) is the nearest.

## 4 A new issue under ART-793 whose title matches

`parentId` cannot be required. The title can.

```json
"deliverables": { "creates": {"kind": "json_text", "tool": "linear_create_issue"} }

{"id": "W10", "title": "new ticket for Soccer Ball", "weight": 5, "work_kind": "multi_source_reconciliation",
 "work_reason": "a line Robert added has no ticket", "class": "write_content", "role": "core",
 "selector": ["text", "creates", "Soccer Ball"], "mechanisms": ["PICKS"]}
```

Passes if any successful `linear_create_issue` carries the words in `title`, `description`, `team`, `assignee`, `state` or a label (all read as text). Case-insensitive. A ticket created with no parent passes.

## 5 The brief's text, whichever tool wrote it

One slot cannot accept several tools. Three deliverables validate side by side (tested), but each slot reads one of them, and a run that used another tool reads **False**, not UNGRADED.

```json
"deliverables": { "brief": {"kind": "json_text", "tool": "gdocs_create_document"} }

{"id": "B2", "title": "brief: scenario", "weight": 3, "work_kind": "interpretation", "work_reason": "...",
 "class": "write_content", "role": "core", "selector": ["text", "brief", "Scenario 1"]}
```

- Reads `title` and `bodyText` of every `gdocs_create_document` call (`driveFileId` is stripped).
- Choose `gdocs_create_document`: in 126 archived baseline trajectories it was called in 36 runs and carried `bodyText` in 34 of 36 calls; `gdocs_batch_update` appeared in 13 runs, `gdrive_create_file` in 19 (mostly registers).
- A run that creates an empty doc and fills it with `gdocs_batch_update`, or writes the brief with `gdrive_create_file`, fails every brief slot (tested). Check for that by hand in forensics. Three parallel slots per fact would triple-count the miss.
- Hazard: a brief written with `gdrive_create_file` is also a candidate for the **table** (see section 10) unless the table's `name_regex` rejects its name.

## 6 The sheet sits in Julia's Drive root

No selector expresses "created by the persona in her Drive". `["delivery", "register_parent", "<folder id>"]` needs all three: the decoded sheet, a `gdrive_share_file` on it, and an explicit parent, taken from `parentId` of a `gdrive_create_file` whose result id is the sheet, or from a later `gdrive_move_file(fileId, newParentId)`.

- Tested: plain `gsheets_create_spreadsheet` + share fails; the same plus `gdrive_move_file` to the folder passes; `gdrive_create_file(parentId)` then `gsheets_create_spreadsheet(driveFileId)` passes.
- Archive: of 73 sheets created in baselines, 44 were moved, 5 were bound to a pre-created Drive file, 24 had no parent call. Those tasks named a folder. For a bare "in my Drive" most runs will not pass the root id, so the slot fails correct runs.
- Use it only if the notes name a real folder of hers (her Drive has `d_10809994aaf374642abff9` "Zombie Art"). Otherwise drop D3 from the surface.

## 7 Each of two files shared with a set of addresses as reader

`["delivery", "share_reader"]` checks one thing: some successful `gdrive_share_file` has `fileId` equal to the **sheet's** id and `role` exactly `"reader"`. It ignores recipients and ignores the brief. Role omitted or `writer` fails (tested). 61 of 73 archived sheets were shared under the id the sheet was created with, so the id match holds in practice.

Recipients need a `json_text` deliverable on the share tool (`emailAddress`, `role`, `type` are text; `fileId` is not):

```json
"deliverables": { "shares": {"kind": "json_text", "tool": "gdrive_share_file"} }

{"id": "D5", "title": "both files shared with PlayableX's intake address", "weight": 1, "work_kind": "lookup",
 "work_reason": "the notes name the address", "class": "delivery", "role": "core",
 "selector": ["text", "shares", "intake@playablex\\.ai.*intake@playablex\\.ai"]}
```

- Passes when the address appears in two successful share calls (tested: two files pass, one fails). It cannot tell two files from the same file twice, and cannot tie the address to a role.
- `addr[ \\n]{1,3}reader` ties role to address only when the agent passes `emailAddress` before `role`; with the other order it matched across two calls in test. Do not rely on it.
- One slot per recipient is four slots of weight 1 at most; "both files" for every recipient is not expressible beyond the two-occurrence form.

## 8 A Slack message in a given conversation whose text matches

Two selectors, neither does both jobs.

```json
{"id": "D1", "title": "reply in Frederick's DM", "weight": 1, "work_kind": "lookup", "work_reason": "...",
 "class": "delivery", "role": "core", "selector": ["delivery", "slack_channel_post", "D05SD5QLG94", ""]}

{"id": "W1", "title": "reply gives the owed count", "weight": 3, "work_kind": "calculation", "work_reason": "...",
 "class": "write_content", "role": "core", "fact_id": "count_owed_msg",
 "selector": ["text", "slack", "owed[ A-Za-z:=*_()|>~\\n\\t\\-–—]{0,20}54\\b|\\b54 (?:lines |line |items |are |is |still )*owed"]}
```

- `slack_channel_post` args are `[channel, text]`. The channel must equal the call's `channel` (or `channel_id`) string. The text is a **case-insensitive literal substring**, not a regex: D1's `".*"` demands the two characters dot-star and fails every real message (tested). `""` means "any message there" (tested, validates). `"54"` would also pass on `154` or a link.
- A DM addressed by user id fails the channel test (tested). In the archive 15 of 117 Slack posts used a user id or a channel name instead of an id.
- `["text", "slack", regex]` reads every Slack message of the run together (DM and channel); it cannot be limited to one conversation. `slack` needs no declaration.
- The count regex above passed on `Owed: 54`, `54 owed`, `*Owed* — 54`, `Owed (54)`, `Owed lines = 54`, `54 lines are still owed`, a Markdown table row, label and number on separate lines; and failed on `Ready 54 · Owed 30`, `Ready 54, Owed 30`, `Owed: 154`, `Owed 53 (was 54 …)`. It misses `Owed → 54` and `19/30/54 (Delivered/Ready/Owed)`.
- `["link", "slack"]` passes when the sheet's id appears as a whole token in a Slack message and the sheet was shared (tested with a `docs.google.com/spreadsheets/d/<id>/edit` URL). It cannot check the brief's link or the channel; `["text", "slack", "document/d/"]` is the nearest for the brief.

**Regex rules that survive the synthesiser** (tested with `sample_from_regex`; the sample must full-match the regex, and the regex must not match the empty string):

| Works | Fails (no sample, slot UNGRADABLE) |
|---|---|
| literals, `.`, `\d`, `\w`, `\s`, positive classes `[ A-Za-z:=-]`, `{m,n}`, `*`, `+`, `?`, groups, `(?:…)`, top-level and grouped alternation, `^`, `$` | `\D`, `\W`, `\S`, negated classes `[^…]`, inline flags `(?i)`, `(?s)`, lookaheads and lookbehinds, lazy quantifiers `*?` `{0,20}?` |
| `\b` at the outer ends of the match (`owed.{0,20}54\b`) | `\b` between two literals when the gap between them can be empty (`Owed[…]{0,20}\b54\b`) |
| a positive class standing in for "no digits": `[ A-Za-z:=*_()\-]{0,20}` | a class that starts with an escape and must match at least once (`[\n ]{1,3}`: write `[ \n]{1,3}`) |

Flags are already `re.I | re.S` for `text` and `re.I` for `reason_matches`, so `(?i)` and `(?s)` are never needed. **Never** put a quantified group around a gap that can also match the token: `(?:Todo.*){48}` and `(?:owed[ -~\n]{0,300}){48}` hung the validator (catastrophic backtracking); `(?:Todo[\n ]*){48}` is safe because the gap cannot contain a `T`.

## 9 A register cell compared tolerantly for a person

Comparators (per column, in the table's `comparators`; default `norm`; anything else fails `validate`):

| Comparator | Rule | For a person |
|---|---|---|
| `norm` | letters and digits only, case-folded, equal | `Brian` does not equal `Brian Foster` |
| `issue_key` | `re.search(r"\b" + escape(expected) + r"\b", cell, re.I)` | **Use this.** Put the first name in the truth (`"Who has it": "Brian"`). Tested: `Brian`, `Brian Foster`, `Brian Foster (re-export)` pass; `Arthur Blake` fails; `Arthur / Brian` also passes. |
| `yes_no` | the cell, normalised, equals one of the spellings listed for the truth value in the table's `yes_no` map; unlisted truth values fall back to `norm` | An alias list: `"yes_no": {"Brian": ["Brian", "Brian Foster"], "Owed": ["Owed", "Owing"]}`. One map per table. Tested: aliases pass, `Brian Foster (re-export)` fails (whole cell, no substring). |
| `pr_number` | `#N`, `/pull/N`, `PR N` | not relevant |
| `sha_prefix` | equal, or a 7 to 39 hex prefix | not relevant |

- Truth `None` for a column accepts the missing spellings: empty, `missing`, `na`, `none`, `withdrawn`, `unavailable`, and anything that normalises to empty (`-`, `—`, `n/a`). Tested: a Delivered line with owner `Brian` fails, with `—` passes.
- A slot may carry `"accepted_outcomes": ["Extra (added)", "Added"]`: extra expected values tried with the same comparator (tested).
- The truth row must carry a field named exactly like the column (`"Who has it"`).
- There is no regex comparator for a cell. Two workarounds, both tested:
  - `["reason_matches", key, regex]` runs a regex on the table's one `reason_column`. A **second table deliverable** over the same sheet, keyed by the ticket cell, gives a second regex column: `"by_ticket": {"kind": "table", "name_regex": <same>, "key_column": "Ticket", "key_regex": "ART-\\d{3}", "columns": <same>, "class_column": "State", "reason_column": "Who has it"}` and `["reason_matches", "ART-806", "\\bBrian\\b"]`. The ticket cell must be exactly the key. It needs the sheet's header to carry the spec's column names (it failed with renamed headers in test).
  - `["text", "handoff", "Washing Machine,[ -~–—’]{0,300}Brian"]` runs a regex on the sheet's raw rows (cells joined by commas, rows by newlines). It ignores header names and column order, as long as the name comes before the cell in its row.

## 10 `register_keys_exact`, keys and `name_regex`

```json
"handoff": {"kind": "table",
  "name_regex": "(?!.*brief).*(?:hand.?off|list|sheet|status|tracker|register|pack|asset|owed|deliverable)",
  "key_column": "Line",
  "key_regex": "ZZ\\d|Grenade|Couch|Iron|…all 103 names…|Toy Hammer",
  "columns": ["Line", "Kind", "Board set", "State", "What's owed", "Who has it", "Ticket", "Notes", "Delivery", "Set", "Extra 1", "Extra 2"],
  "class_column": "State", "reason_column": "What's owed",
  "comparators": {"State": "norm", "Board set": "norm", "Who has it": "issue_key", "Ticket": "issue_key"}}

{"id": "V1", "title": "hand-off list lines", "weight": 5, "work_kind": "multi_source_reconciliation", "work_reason": "...",
 "class": "delivery", "role": "volume", "volume_for": ["state", "owed", "owner", "set"],
 "selector": ["delivery", "register_keys_exact"], "expected_keys": ["Grenade", "…103 names…"], "mechanisms": ["PICKS"]}
```

How a key is read (`_keyed_rows`):
- A row whose cells include the key column's name (normalised: `Line`, `LINE`, `line.`) is a **header**: it sets the column mapping by header name (normalised equality with the spec's column names) and is skipped.
- With no such header, columns are taken **by position in the spec's order**.
- In every other row the key cell, stripped, must **full-match `key_regex`, case-sensitively**; the row is stored under that exact string. Rows that do not match are dropped silently.
- `register_keys_exact` is `set(decoded keys) == set(expected_keys)` (else `truth_keys`, else every truth key matching the regex). **No normalisation**: `Grand Piano` for `GrandPiano` or `soccer ball` for `Soccer Ball` drops the row (tested: 101 rows, V1 and the Owed total fail). A case-insensitive `key_regex` does not help, the stored string is still what was written.

Consequences for `key_regex`:
- D1's generic `[A-Z][A-Za-z ]+` turns a header such as `Asset | Status | Owner` and any `Totals` or `Owed` label in column A into phantom keys, and V1 fails.
- An explicit alternation of the 103 names avoids that. Extra rows the agent adds (for example `Item visuals`) then vanish: V1 and the totals still pass (tested). Over-inclusion is not detectable with this shape.
- The alternation must **start with a synthetic alternative that ends in a digit** (`ZZ\d|…`). `total` and `printed_total` need two keys from the synthesiser, which it makes by incrementing a trailing number; with names only the slot is UNGRADABLE ("cannot synthesize two keys"). That is why D1 had the odd digit branch.

`name_regex` is `re.search(name_regex, title, re.I)` on the sheet's title (when `gsheets_create_spreadsheet` returned a `spreadsheetId`) or on the `name` of a `gdrive_create_file`.
- A sheet whose known title does not match is skipped entirely and every table slot fails. Keep it wide.
- Any `gdrive_create_file` with `content` whose name matches is a table candidate, and among shared candidates **the last one written wins**. With `name_regex` `.` a brief created through `gdrive_create_file` and shared after the sheet replaced the table (tested: 0 rows, every table slot False). The regex above rejects names containing `brief` and validated; `^(?!.*brief)` alone also validates (the fixture then uses the name `deliverable`).
- D1's `(?i).*(hand-?off|pack|playable).*` matches `ZM3D playable brief` and misses `Hand off list`.

Decoder limits that fail a correct sheet (all from `trajectory_ledger.table`, the starred ones tested):
- Rows written with `gsheets_batch_update` are not read* (only `gsheets_values_update`, `gsheets_values_append`, `gsheets_values_batch_update`, and `gdrive_create_file` content).
- The range must contain a cell: `Sheet1!A1:G104` and `A1` work; `Sheet1` and `Sheet1!A:G` do not*. All 199 archived `gsheets_values_update` ranges had a cell.
- A tab name that begins with capitals then a digit is mis-read as a cell (`ZM3D list!A1:G104` gave 0 rows*). A quoted name is fine (`'Hand-off list'!A1`).
- For a native sheet only the first `len(columns)` grid columns are kept, so pad `columns` (as above) to at least the widest sheet you expect. Columns are then found by header name.
- Renamed headers work only when the order is the spec's and no header cell is `Line`*. Spec names in any order work*. **So the notes must state the column names**, or half the runs will be unreadable.
- The delivered table is the shared candidate written last; with no share, the one with most keyed rows.

## 11 `total`

```json
{"id": "A1", "title": "owed count on the list", "weight": 3, "work_kind": "calculation", "work_reason": "...",
 "class": "aggregate", "role": "core", "selector": ["total", "Owed"], "fact_id": "count_owed"}
```

- Written side: over the keyed rows of the **first** table deliverable, the number of rows whose `class_column` cell, normalised (letters and digits, case-folded), equals the class name lower-cased. `OWED` and `Owed.` count; `Owed (re-export)` and `Owing` do not (tested). The `yes_no` aliases do not apply here.
- Truth side: the number of truth rows whose key full-matches the first table's `key_regex` and whose `truth_fields.class` value is the class.
- Passes when a table was decoded and the two numbers are equal. The class must be in `classes`.
- Fails when: no table is decoded (title, range, tool, or displacement, section 10); the header was not recognised and the order differs (State read from the wrong column); a row's key is not an exact key (not counted); a class cell carries anything beyond the class word; rows are missing. Duplicate keys count once. Extra unknown rows are ignored.
- A class name with a space or punctuation can never match (the comparison is against `class.lower()`, not its normalised form). `Delivered`, `Ready`, `Owed` are safe.
- `["printed_total", "Owed"]` reads a totals block outside the keyed rows (`Owed` followed within 20 non-digits by a number, case-sensitive). It fails when the agent prints no totals (tested), so use it only if the notes ask for totals on the sheet. It shares a fact id with `total` (`total:Owed`).

## 12 Reference

**Deliverable kinds**

| Kind | Meaning |
|---|---|
| `table` | the sheet or CSV: `name_regex`, `key_column`, `key_regex`, `columns` (required), `class_column`, `reason_column`, `comparators`, `missing_values`, `yes_no`. Several may be declared; a per-key slot reads the first whose `key_regex` matches the key; totals read the first table. |
| `text` | one Linear issue's replayed description and final state: `tool` (default `linear_update_issue`), `issue`, `key_regex`, `groups`. Only the first is used. |
| `json_text` | the text of every successful call of one `tool` (section 0, fact 1). `slide`, `email`, `slack` exist without declaration. |
| `calls` | inert: no selector reads it. `share_reader` reads `gdrive_share_file` directly. |

**Selector kinds** (number of arguments after the kind)

| Selector | Meaning |
|---|---|
| `field` key column (2) | the cell equals the truth under the column's comparator (or an `accepted_outcomes` value) |
| `total` class (1) | section 11 |
| `printed_total` class (1) | a printed totals block gives the truth's count |
| `reason_matches` key regex (2) | `re.search(regex, reason cell, re.I)` |
| `text` deliverable regex (2) | `re.search(regex, deliverable text, re.I, re.S)`; the target may be a table (raw rows), a `json_text`, or the tracker |
| `link` deliverable (1) | the sheet's id appears as a token in the deliverable and the sheet was shared |
| `group_count`, `group_size` group (1); `group_key` key group (2); `groups_of` key (1); `sole_reason` key group (2) | groups stated in the tracker description ("Review (2): K-01, K-02") against the truth's group lists |
| `tracker_lists` heading key (2) | the key is listed in the section under a heading matching the regex |
| `tracker_count` heading n (2) | exactly n distinct keys in list-like lines of that section |
| `tracker_entry` heading key [patterns] (3) | the key's own line carries every value pattern |
| `delivery` check … | below |

**Delivery checks** (arguments after the check name)

| Check | Meaning |
|---|---|
| `register_keys_exact` (0, optional table name) | section 10 |
| `register_is_csv` (0) | the table was delivered as a CSV upload |
| `register_parent` folder (1) | section 6 |
| `share_reader` (0) | section 7 |
| `tracker_state` regex (1) | section 1 |
| `tracker_preserves` text (1) | the original text survives every description update |
| `slack_channel_post` channel literal (2) | section 8 |
| `slack_thread` ts (1) | a Slack call's `thread_ts` equals the ts (must look like `1759255800.418239`) |
| `slack_after_email` (0), `email_reply` message id (1), `slide_updated` (0), `trello_card` card literal (2) | not relevant here |

**What `validate` enforces** (each is a FAIL)
- `kind` `GRADABLE_SURFACE`, `version` 1; deliverable kinds and table fields; comparator names.
- Slot ids present and unique; known selector with enough arguments; a `text` or `link` target that is a declared deliverable (or `slide`, `tracker`, `email`, `slack`); a `field` key that matches a table's `key_regex` and a column of that table; a `total` class in `classes`; regexes that compile.
- `weight` 1, 3 or 5 and equal to the work kind's band: `lookup` 1; `interpretation`, `calculation`, `comparison`, `limited_reconciliation` 3; `multi_source_reconciliation`, `deeper_reasoning`, `cross_modal`, `tracing` 5; a non-empty `work_reason`.
- `class` in `direct`, `aggregate`, `write_content`, `delivery`; `role` in `sample`, `exception`, `volume`, `core` (default `sample` for `field`, else `core`).
- Gradeable: every slot reads True on its fixture and False on an empty run. Group and tracker slots need `truth_fields.groups` (a field name that is not a table column). `register_keys_exact` needs `truth_keys` or `expected_keys` unless it is a volume slot.
- One fact in at most two slots: the fact is `fact_id`, else `total:<class>`, else the selector itself; three or more fail.
- At most five `sample` slots per group (the slot's `group`, or `<table>:<column>` for a `field` slot), and every sampled group covered by a `volume` slot whose `volume_for` lists it (or `<table>:*`).
- An `exception` slot names `singled_out_by` (an authority, fragment or anchor id of the manifest).
- Every `mechanisms` entry is an id of the manifest's `mechanism_portfolio`.
- Reported, not gated: total weight, weight by class, mechanism share.

## 13 `rubric_skeleton.py`: where the rows come from

1. **One row per surface slot**, at the band of its work kind. More than one only on an explicit signal: `"atoms": N` (N of 2 or more), a `tracker_entry` with N patterns, a `groups_of` whose truth lists N groups, or a regex of top-level lookaheads.
2. **Then each manifest `writes` entry**, its `tool` split on `+`:
   - Tools starting `gsheets_`, `gdocs_`, `gslides_` are one artifact: no row.
   - `count` of 1 or less: no row.
   - Otherwise the entry's slots are those graded on that tool: a `text` or `link` slot whose deliverable has that `tool`; tracker selectors (the `text` deliverable's tool); `delivery` checks through a fixed map (`tracker_state` and `tracker_preserves` to `linear_update_issue`, `share_reader` to `gdrive_share_file`, `register_parent` to `gdrive_move_file`, the Slack checks to `slack_send_message`). Table slots belong to no tool.
   - **Not a template:** each non-volume slot names one target (the delivery argument, else an issue key such as `ART-840` in its selector or title, else a truth key of four or more characters, else itself). `count` minus the distinct targets named is added as rows, at `interpretation` (3), or `lookup` (1) when the tool is a share, move, copy or folder call.
   - **A template:** no per-target rows. If no non-volume slot is graded on the tool, up to five sample rows at `lookup` (1) are added. One volume row at `lookup` (1) is added unless the surface has a `volume` slot on that tool, or one whose `volume_for` names the template group.
3. Added rows carry no budget unit until the budget names them (`rebase`), so they count as always-pass.

**Why 47:** D1's `linear_create_comment` entry had `count` 48 and no template; the only slot on that tool was W12, naming `ART-840`; 48 minus 1 gives 47 rows at weight 3 (141 of the 326). `linear_update_issue` and `gdrive_share_file` carried `"template": true`, which is why they added 0 and 1.

**What makes a write entry a template** (either is enough; all four cases tested with `build_rows`):
- **Manifest:** `"template": true` on the entry. Comments: 48 writes become 1 volume row when a slot is graded on comments, 6 rows (5 samples and a volume, weight 1 each) when none is, 0 when the surface also has a volume slot on that tool.
- **Surface:** two or more slots with `"role": "sample"` and the same explicit `"group"`, graded on that tool, whose selectors are identical once issue keys and truth keys are masked and still hold a literal of three or more letters or digits. Tested: three slots `["text", "comments", "<line name>[ -~]{0,120}owed"]` in group `comment` plus a volume slot gave `template=True` and 0 added rows, and the surface validated.

The tool does not judge whether the writes really follow one template; it takes the flag. The forecast then holds only if the final rubric is written the same way (`rubric_skeleton.py drift` compares them), and added template rows weigh 1, not 3. For `linear_create_issue` (6 writes): two named slots leave 4 added rows at weight 3, or 1 volume row with `"template": true`. For `slack_send_message` (2 writes): two slots that name the two conversations leave nothing to add.
