---
name: thread-maestro
description: "Organize new project ideas into focused Codex chats with visual role cards. Use when the user describes an app or project they want to start, or asks to split an existing project across chats. Routine coding tasks and authoring this skill do not start chat setup."
license: "MIT"
---

# Thread Maestro

Help the user choose a chat structure, approve it, and prepare the workspace using available features. Chats are independent user conversations in the app. The user assigns tasks and decides when to move between stages.

## First response: automatic and explicit use

Automatic selection changes how this skill is discovered, not its output. Follow the same card workflow whether or not the user mentioned Thread Maestro.

Before answering with a structure, read [references/proposals.md](references/proposals.md) and the available host's visualization contract. Read large instructions separately or in bounded ranges; do not combine the full visual contract, asset source, and runtime guide into one output that may be truncated. Build the approved card layout with [scripts/render_proposal.py](scripts/render_proposal.py), which fills the bundled template without rewriting its HTML. No creation tools are needed to draft it.

The reply contains one short recommendation, the actual embedded card fragment, and one question about names or roles. Reading the asset is not rendering it. A table is not an equivalent successful result when inline cards and a writable task location are available. Use a table only if the host genuinely lacks the visual facility or an allowed output location, or if the user asks for text. Verify that limitation rather than assuming it because the trigger was automatic.

This first question is design feedback, not an execution approval request. Do not cite the skill, link its instructions, quote its description, or add "this is only a proposal" to justify showing the structure. Creation consent belongs to the later complete setup card. Keep any disclosure actually required by higher-priority instructions at that later action gate.

## Invocation boundaries

- When the user describes a new project they want to start, propose its chat structure without requiring a skill mention. Also use this workflow when asked to organize an existing project's chats, or when explicitly invoked as Thread Maestro or `$thread-maestro`.
- Routine fixes, individual features, questions, and editing or discussing this skill do not start chat setup. Honor a request to stay in one chat or skip organization. Do not repeat initial setup in an already organized project unless the user asks to revise it.
- Automatic selection starts the proposal, not creation. Receiving a document or describing an idea does not approve chats, files, or project changes.
- A reply to a clarification or approval request continues the current setup; another `$thread-maestro` call is unnecessary. Retain the agreed plan and completed steps across replies.
- Separate analysis, approval of a concrete plan, and creation. Workspace setup must not start product development.
- Do not substitute subagents, copies of the source conversation, background jobs, or automatic task dispatch for user chats. Do not create schedules or continuation loops.
- Respond in the user's language. Choose chat names with the user; do not impose English names.

## Keep responses focused

The default first reply is one short recommendation, a compact card diagram, and one question about the structure. Use the host's inline visualization when available, with a plain table as fallback. Read [references/proposals.md](references/proposals.md) when presenting a proposal. Keep analysis and tool checks internal; disclose only facts needed for the user's current decision. Explain setup details when they become actionable. Keep later replies brief too: report changed state and the next decision, expanding only when asked or needed for a material issue. Preserve any disclosure required by higher-priority instructions.

Use ordinary, direct language at every stage, including setup and connection checks. Do not append skill names, instruction quotes, or explanations such as "Thread Maestro requires approval" merely to justify a question. End normal replies after the useful question or next action. Keep actual approvals intact and preserve explanations required by higher-priority instructions; the skill cannot disable host policy.

## 1. Establish the starting point

Use the user's description and known preferences. For a fresh idea, draft the roles first; defer project registration checks, chat searches, and startup-mode details until setup. Discover the app tools and read [references/runtime.md](references/runtime.md) before promising or performing automatic creation.

**Starting from an idea:** an idea description is enough. Propose or clarify the name and storage location; do not require a prepared folder or repository. Discuss the structure without creating a folder, project, or chats until the plan is approved. Do not invent an absolute path when the location is unknown.

**An existing folder or project:** identify the working folder and matching app project. Match verified paths and membership; use the real project ID. Avoid duplicates. Read project instructions, brief documentation, structure, and the current plan. Inspect source files selectively when needed to identify work areas.

The file folder, app project, and main chat are separate entities. Naming a chat `General` or a localized equivalent does not require renaming its folder. Offer to use the current chat as the main chat if it fits and belongs to the project. Include a move or rename as a separate planned action and obtain permission for that action. If moving is unavailable, propose a separate main chat with a short summary, without copying the full history.

Once the target project is identified, find suitable existing chats, including pinned ones. A new idea can receive a provisional structure before its folder or project is selected; do not scan unrelated chats just to draft it. Before creation, match project, purpose, and work state, not just names. Read candidates selectively. Absence from a short sample does not establish that a chat is missing: expand the sample, use available pagination, or check known IDs. If completeness cannot be established, disclose that before deciding to create a possible duplicate. Preserve existing titles verbatim.

## 2. Propose a structure

Identify the current goal and scope, independent work areas, shared decisions, and stage dependencies. Ask only for information needed for a useful plan; do not repeat answered questions.

Choose one recommended total from **3, 5, or 7 chats**, including the main chat, according to the scope and useful separation of work. These are this skill's supported layouts, not a technical limit of Codex. Use three for compact work; separate more substantial areas when five or seven is justified. Derive roles from actual tasks, not a fixed list or empty roles added just to fill the layout.

The user may rename or regroup roles within these totals. For an unsupported count, briefly offer the nearest supported options and wait for a selection; do not silently round or claim that Codex cannot create that count. For six, offer five or seven. For more than seven, briefly explain the additional switching and context handoffs and recommend seven. When the user changes the count, revise the roles and redraw the proposal before creation. Do not create chats until the latest concrete plan is approved.

Include the main chat for shared requirements and decisions in the total. Present it as one wide card above the specialist grid using [references/proposals.md](references/proposals.md). Three total means two specialist cards side by side; five means a 2-by-2 grid; seven means a 3-column, 2-row grid. Each card has a matching outline icon, title, and short scope description. Show verified reuse or material dependencies only when useful; keep the diagram a proposal rather than implying completion or automatic task dispatch. Do not duplicate it as a Markdown table or repeat every card in paragraphs.

After structure selection, use the interactive setup plan in [references/setup.md](references/setup.md) to resolve missing location and connection details. Do not repeat the structure discussion or replace the setup card with a long checklist. Structure selection does not by itself approve unknown setup actions. If everything is already known, use a single compact confirmation. Before creation, the confirmed plan must cover:

- Project name and shared folder; for a new project, the proposed path and registration step.
- Which chat is the main one, total count, how many are reused, and how many are new.
- Exact names, roles, dependencies, and suggested order of manual work.
- Any proposed organizational files or changes to existing chats.
- Available creation mode: no first turn, a brief acknowledgment included in the setup confirmation, or manual setup.

Surface these details at the creation decision, not as a checklist in every first response. Keep previously agreed details and ask only about unresolved choices.

Splitting topics can reduce irrelevant context, but does not guarantee token, usage-limit, or cost savings. Account for the overhead of additional chats.

## 3. Confirm the concrete plan

Discuss the roles and layout as design choices. The first structure question does not authorize creation and must not be presented as a tool-approval gate. Obtain creation consent once through the complete setup card, covering the folder, titles, files, and startup behavior. A general request to organize a project does not approve unknown settings. Do not ask again when that concrete setup is already approved. Agree on material changes before carrying them out.

If creation starts a first turn, show that behavior in the setup card before its final confirmation button: a brief automatic role acknowledgment without extra file reads, tools, commands, changes, or development. The button confirms this behavior together with the displayed folder, files, and chats. Do not leave startup consent pending until after the folder is connected. Structure selection alone is not this final confirmation.

After the user confirms that complete setup, verify the folder and project, then execute the approved actions directly. Do not propose the same chats again, request another creation or acknowledgment confirmation, or add a footer explaining the skill's approval rules. A connection check is verification, not a new approval stage. Ask again only for a material plan change or a genuine unresolved blocker; explain the practical issue briefly.

Use the current revision and creation ledger in [references/creation.md](references/creation.md). Old cards and repeated confirmation messages must not start another copy of an approved setup. Check the entire plan, not only its count and titles.

If the user declines the acknowledgment, prepare titles and starting texts for manual setup using [references/templates.md](references/templates.md). State that no chats were automatically created. Do not work around the limit with a hidden executor.

## 4. Prepare the workspace and create chats

After approval, perform only the agreed organizational actions.

For a new project requiring manual registration, follow [references/setup.md](references/setup.md): the user chooses or creates a folder and adds it to Codex first; verify its app registration before writing project documents or creating chats. Do not alternate between Codex creating files, a user registration step, and Codex creating chats. An automated bootstrap is appropriate only when supported and explicitly chosen in the plan. Reuse an existing suitable folder without overwriting its files. Never substitute unrelated projectless chats.

Use one project and one shared working folder. Do not create copies or Git worktrees by default. Set a model or reasoning override only when explicitly requested and supported by the tools.

Create only the agreed missing chats. Use independent histories, not a fork of the source conversation. Give each a short role, confirmed goal, dependencies, and targeted links to shared files. For the approved acknowledgment, use [references/templates.md](references/templates.md). File links provide context for future tasks, not an instruction to read files during setup.

Include the future-task scope reminder from [references/templates.md](references/templates.md) in each new chat's starting instructions. Supply relevant known chat titles or a chat-map reference when useful. Treat roles as guidance: flag clear topic changes briefly, allow related discussion, and respect the user's choice to continue in the current chat. Keep role-specific guidance out of global project instructions.

An existing chat can be included without messaging it. Do not rename, move, or message existing chats without authorization for that action. Permission to create missing chats does not automatically grant it.

Record returned IDs and each step's status immediately. After an ambiguous result, verify existence before deciding to retry. After partial success, continue only with missing chats. If the outcome cannot be established, stop retrying that creation and report the uncertainty. Do not delete created chats as a rollback without the user's instruction.

## 5. Shared context and results

Reuse suitable documents. Create only the minimum needed, such as a brief, decisions, or chat map. `PROJECT_BRIEF.md`, `DECISIONS.md`, and `CHAT_MAP.md` are optional names, not a required set. Include document creation in the plan for approval; avoid duplicates.

A map may record title, role, real ID and host, dependencies, and status. Distinguish proposed, preparing, created, reused, manual setup required, and outcome unknown. Separate confirmed decisions from suggestions and open questions. Do not store full transcripts.

Give each chat only relevant context and links to specific documents and sections. Do not add global instructions requiring every chat to read the entire project. Change shared instruction files only when needed for the agreed outcome. Separate histories do not guarantee technical isolation of access; do not promise it.

File overlap between roles is allowed. Explain dependencies and edit order; the user ensures sequential work. Completing a stage does not start the next chat. When explicitly asked, prepare a short handoff: decision, changed files, open question, and next necessary step. Do not send it to another chat without authorization to send.

After creation, verify each new chat's existence, title, project membership, and completion of any acknowledgment as far as tools allow. Follow [references/runtime.md](references/runtime.md). Distinguish observed results from behavior inferred from tool descriptions.

For success, finish with one short sentence giving the verified number created and, if relevant, reused, followed by supported opening elements with real IDs. Do not repeat roles, settings, paths, limits, or approval explanations. For partial success, give the actual count and only the remaining practical issue. Never call setup complete while creation or acknowledgment is unverified. Workspace organization is not completion of the project's tasks.
