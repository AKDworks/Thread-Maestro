# Short chat texts

Read when preparing starting messages or handoffs. Substitute verified facts only. Remove irrelevant lines and avoid repeating long project descriptions in every chat. Adapt these texts to the user's language, including role labels and chat names.

## Scope reminder for future tasks

Append this shared block to either starting text below, in the user's language. It applies to future tasks and must not expand the first-turn acknowledgment. Specialist roles guide topic suggestions; the main chat remains available for general project questions. Do not invent a destination chat or require a new one just to enforce a role.

```text
During future work, briefly flag requests clearly outside this chat's role
before starting substantial work. Name the appropriate project chat only
if known; otherwise describe the work area. Offer to move the discussion
or continue here. If the user chooses to continue, proceed without
repeating the reminder for the same topic. Handle related questions
that support the current task normally. Do not send messages or move
the discussion automatically.
```

## Approved first-turn acknowledgment

Use only after explicit consent to an automatic acknowledgment. This limits the first turn, not future work authorized by the user.

```text
This chat's role: [role] in [project name].
Shared working folder: [verified absolute path].
Confirmed goal: [brief description].
Scope and boundaries: [this role's tasks].
Dependencies: [decisions or results needed from earlier stages].
For future tasks: [targeted links to real files and sections].
Other project chats: [relevant known titles and roles or chat-map link; omit if unknown].

In this first reply, only briefly acknowledge the chat's purpose.
Do not read additional files, invoke tools or commands, change files,
or start project analysis or implementation.
After acknowledging, wait for the user's explicit task.
The user assigns future tasks and chooses transitions between stages.
```

For a separate main chat, provide the agreed goal and scope, confirmed shared decisions, and document links. Do not copy the source conversation or present suggestions as accepted decisions.

## Manual creation or a documented no-turn mode

Provide each new chat's title and the text below. If no automatic creation occurred, say so. Explain that sending the text as a normal message may start a reply. For a completely inactive chat, save it without sending only if the interface supports this; do not promise such a mode exists.

```text
Role: [specialization] in [project name].
Shared folder: [confirmed path].
Goal and boundaries: [confirmed tasks for this role].
Dependencies: [results of earlier stages].
Context for future tasks: [relevant documents and sections].
Other project chats: [relevant known titles and roles or chat-map link; omit if unknown].
Start project work only after the user's explicit task.
The user chooses the order of stages.
```

If the tool genuinely supports saving a role without a first turn, supply this text through that mechanism. Do not invent a missing parameter.

## Handoff requested by the user

```text
For chat [exact title].
Confirmed decision: [what was agreed].
Result and changed files: [brief summary and real paths].
Open question: [if any].
Next necessary step: [recommendation for the user].
```

Preparing a handoff does not authorize sending it to another chat or starting the next stage.
