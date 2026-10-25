# Runtime capability checks

Read before promising automatic creation and before organizational changes. The names below guide tool discovery; they are not a universal API. Current tool schemas and restrictions take precedence.

## Conditions to check

| Capability | Acceptable evidence | If unconfirmed |
| --- | --- | --- |
| The project matches the folder | Project listing with a verified path and real ID | Clarify the match; do not guess IDs |
| A new folder can be registered as a project | An available registration tool with a suitable schema | Create the approved folder; ask the user to connect it in the UI, then verify |
| A separate user chat can be created in the project | A creation tool that selects a project | Prepare materials for manual setup |
| Title and short role are supported | Documented parameters | Explain any remaining manual step |
| Chats share the same folder | Local environment of the selected project, without copying | Do not substitute separate checkouts or worktrees |
| History is independent | A new conversation without inherited history | Do not substitute a fork |
| No first turn or automatic file reads | An explicit documented tool mode | Treat as unestablished; agree on an acknowledgment or use manual setup |
| The source chat can join the project | A supported move and the user's permission | Offer a separate main chat with a brief summary |
| Readiness and IDs can be verified | Creation result, listing, reading, or waiting | Disclose unverified details; do not invent readiness |

A missing schema parameter means this tool does not establish the capability; it does not prove the feature is absent from every app version. Do not probe creation with live test chats without separate authorization for that test. Project listings and targeted checks of existing chats are appropriate during analysis.

## When Codex app tools are available

- `list_projects`: match the project and working folder; use the returned `projectId`. A sidebar section is not a project.
- `list_threads`: include pinned and ordinary chats, project membership, and host. Expand incomplete samples or use available search and pagination; do not invent parameters. If a candidate is absent from the available sample, do not claim the search was exhaustive.
- `read_thread`: clarify a candidate's role or state selectively; do not load every chat history.
- `create_thread`: read the current schema. Where supported, use `target.type="project"`, the confirmed `projectId`, and `environment.type="local"`. Do not substitute worktree, projectless, or cloud for the shared local project. Supply the agreed title and short prompt. If `prompt` is required and no mode omitting the first turn is documented, do not promise an inactive chat. A prompt saying "wait" does not disable an automatic reply.
- `move_thread_to_project` and `set_thread_title`: use only with permission for the specific move or rename. Check source and destination restrictions. If a UI action is required, explain it and continue after verifying the change.
- `wait_threads`: explicitly check preparation or acknowledgment after actual creation. Use the real `threadId`, host, and returned cursor; `timeoutMs: 0` requests a compact snapshot. Use bounded waits and avoid frequent unchanged polling. If the acknowledgment starts project work, report the actual outcome and stop further creations until the startup behavior is resolved.

A preparing `clientThreadId` is not a ready `threadId`. Obtain the ready ID only through a documented mechanism; do not pass a temporary ID to tools that require the real one. If preparation cannot be awaited, report "preparing" and avoid duplicate creation.

In this environment, show each created chat on its own line:

```text
::created-thread{threadId="REAL_THREAD_ID"}
```

If creation is still preparing and returns only a temporary ID, use the supported preparing variant:

```text
::created-thread{clientThreadId="RETURNED_TEMPORARY_ID"}
```

This indicates preparation, not confirmed readiness. For reused chats, use only supported links or navigation; do not invent URL formats. In other environments, use their own supported opening elements.

## Recovery

After an ambiguous response, match listed chat data by project, title, and attempt time where available. Similar titles alone are insufficient evidence. Record confirmed success before the next creation. Retry only a step known not to have completed. If the outcome cannot be established, keep "outcome unknown" and explain what needs checking.

Do not edit internal app databases or service files to register projects, create chats, or bypass limitations. A Markdown map records real chats; it does not create them.
