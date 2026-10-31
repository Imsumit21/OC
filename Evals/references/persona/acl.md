# Persona ACL Policy

Persona ACL is active and fully implemented for HarmonyGames. This document is
the authority for task-visible identities and persona-scoped read visibility.
[`Evals/references/tools/catalog.json`](../tools/catalog.json) remains the authority for service
capabilities, exact tools, parameters, and available read and write operations.

## Two policy layers

1. **Identity configuration:** the assigned taxonomy persona resolves to one
   exact roster email. The environment uses that email as the acting user.
2. **Read enforcement:** Gmail, Slack, GCal, GDrive, GDocs, GSheets, and
   GSlides filter reads to data visible to the acting user. Contacts, GitHub,
   Trello, Linear, Snowflake, and Confluence have no persona-scoped read
   filtering (QC Rating Form V12, Prompt - Feasibility, 2026-09-27).

Persona ACL does not govern writes. A cataloged write may still be available,
but this policy must not be cited as granting or denying it.

## Task-visible personas

The exact 17-record roster is
[`Evals/references/persona/roster.json`](roster.json).
Use its `persona_key`, `name`, `email`, `role`, and `department` values exactly.
Never construct, normalize, or infer an email from a person's name.

There is no task-visible Finance persona or CFO. Finance remains a business
function, not an identity; assign it only to an appropriate persona from the
roster.

## Access matrix

Here, **unscoped** means shared across task personas, not public outside the
HarmonyGames evaluation environment.

| Service | Persona-scoped reads | Visibility |
|---|:---:|---|
| Gmail | Yes | Acting user's mailbox-visible messages, threads, labels, profile, and attachment names and metadata |
| Slack | Yes | Conversations, messages, threads, file names and metadata, and related records visible to the acting Slack user |
| GCal | Yes | Calendars, events, and free/busy data visible to the acting user |
| Contacts | No | Unscoped |
| GDrive | Yes | Files and folders the acting user owns or that are shared with them, including metadata, content, and search results |
| GDocs | Yes | Documents readable by the acting user through the same Drive file visibility |
| GSheets | Yes | Spreadsheets, sheet metadata, and cell ranges readable by the acting user through the same Drive file visibility |
| GSlides | Yes | Presentations, pages, and page elements readable by the acting user through the same Drive file visibility |
| GitHub | No | Unscoped |
| Trello | No | Unscoped |
| Linear | No | Unscoped |
| Snowflake | No | Unscoped |
| Confluence | No | Unscoped |

**Attachment content (2026-10-17).** The tool catalog lists
`gmail_get_attachment`, `slack_read_file`, `linear_get_attachment` and
`trello_get_attachment` but not what they return, so this note rests on export
and run evidence. Gmail attachment reads return no bytes
(`no_attachment_root_configured` in the HarmonyGames runs), although the local
export keeps the files under `root/attachments/`. Slack file records carry no
content (`content_path` and `content_inline` are null on all 53,422 records).
Linear attachments (2,027 files) and Drive-family files ship real content;
Trello ships bytes for 42 of its 106 attachments. Evidence that exists only
inside a Gmail or Slack attachment is not readable by the Agent as content.

Contacts, GitHub, Trello, Linear, Snowflake, and Confluence form the
**public-service group**. This is a read-filtering classification, not an
exhaustive list of available services.

**Service clarification (2026-09-27):** QC Rating Form V12 (Prompt -
Feasibility) states that reads are persona-scoped in seven services (Gmail,
Slack, GCal and the Drive family) and unscoped in the other six (Contacts,
GitHub, Snowflake, Trello, Linear, Confluence), and that writes are not blocked
by ACL. This supersedes the 2026-09-23 `service-availability-v1` note, which
left Snowflake and Confluence read filtering unspecified. Both services remain
live; see [ENVIRONMENT.md](../../ENVIRONMENT.md#live-service-availability).

The four Google document services share Drive's underlying file ACL. A file that
is invisible to the acting user in GDrive is also invisible through GDocs,
GSheets, and GSlides, including by-ID reads.

## Scoped read behavior

For Gmail, Slack, GCal, GDrive, GDocs, GSheets, and GSlides:

- **List operations** return only records visible to the acting user.
- **Search operations** search only within that visible set and do not reveal
  inaccessible matches.
- **Get/read operations** enforce the same visibility rule. Supplying a known
  object ID does not bypass the ACL.
- A by-ID request for an inaccessible object is denied or returned as not
  found; its protected content is not disclosed.
- Child and related reads, such as a thread, attachment, event, conversation,
  document body, cell range, or slide page lookup, inherit the applicable scoped
  visibility.

Authors must not treat a read denial or filtered result as proof that the
underlying company record does not exist globally. It establishes only that the
record is unavailable to the selected persona.

## Author, Agent, and verifier contexts

- **Universe Explorer:** authors operate in god-mode so they can inspect the
  full universe while designing and validating a task.
- **Agent Runner:** the run uses the task's required persona and therefore its
  scoped read visibility.
- **Run Verifiers:** every verifier uses the same required persona as the Agent
  Runner. A verifier must not depend on broader author visibility.

Author god-mode is for universe inspection only. It does not make author-visible
evidence in any of the seven scoped services reachable by the Agent or verifier.

## Persona lifecycle and precedence

1. Select the required persona through the task taxonomy.
2. Resolve the persona through the exact ACL roster email.
3. For Agent Runner and Run Verifiers, the taxonomy sends that exact roster
   email as `persona_email` in the run payload. Universe Explorer omits
   `persona_email` and remains author god-mode.
4. After the universe loads, the environment automatically applies
   `set_acting_user` with that email.
5. The environment reapplies the same acting user on every agent or verifier
   run and every turn.

Do not touch the separate platform AMV persona dropdown: it overrides the
taxonomy selection and persists. Taxonomy selection plus the exact roster
mapping is the required source of persona identity.

`set_acting_user` requires the exact `email`. It is environment configuration,
not an Agent tool, not a rubric process requirement, and not a
task call to include in complexity or trajectory call counts.

## Google viewer-context tools

Some Google service catalogs expose service-specific `*_get_viewer` or
`*_set_viewer` tools. Viewer context is not task persona identity and does not
replace taxonomy, the roster, `persona_email`, or `set_acting_user`. It cannot
authorize an ACL bypass, and viewer calls earn no Process or
complexity credit.

If a manual viewer change causes scoped Google reads under the wrong identity or
otherwise defeats the assigned persona scope, classify the execution as
**Excluded (environment/config/path violation)**. This now applies to GDrive,
GDocs, GSheets, and GSlides as well as GCal.

## Task-authoring and evaluation rules

- Validate every required read in the seven scoped services from the assigned
  persona's Agent/Verifier view, not only from Universe Explorer.
- Design prompts so all required evidence is reachable by that persona. A
  deliberate read denial may be contextual evidence, but inaccessible content
  cannot be required ground truth.
- Treat list/search omissions and by-ID denied/not-found results consistently;
  do not instruct the Agent to bypass persona visibility.
- Keep implementation-specific ACL configuration out of natural task prompts.
- Use the same persona for trial runs, final runs, and Run Verifiers.
- Do not assume an ACL-based write denial or make one necessary to a prompt,
  Oracle Events, or rubric. Determine write feasibility only from the
  authoritative tool catalogs.
- A shared catalog does not imply shared read visibility: all personas have the
  same 11 task-visible services, while seven of those services enforce
  persona-scoped reads.
