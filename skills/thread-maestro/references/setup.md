# Setup after structure selection

Read once the user has chosen the chat structure. Keep the accepted count and roles. Show a compact setup view instead of a prose checklist. Ordinary setup questions and connection checks do not need a footer quoting this skill; preserve any explanation required by higher-priority instructions at a real approval gate.

## Location choice

Offer a proposed path and the user's own folder. Prefer an explicit user preference, an established project location, or a verified parent used by their projects. Do not assume that Documents, a personal username, or the current skill's source folder is their project home. If no justified absolute location is known, leave the suggested option unavailable and ask for a full path rather than inventing one.

The full-path input stays visible. In suggested mode it displays the proposed path and is disabled with readable muted text. In custom mode it is editable and retains the custom draft across switches. Switching must not add or remove the input or cause the panel to jump.

Accept paths copied with balanced outer quotes and surrounding whitespace. Remove only that wrapper; preserve internal spaces and folder names. Compare Windows paths with normalized separators and case when matching actual project membership. Reject relative paths and control characters; do not silently substitute a different location.

## User first, then Codex

When manual registration is required, show these stages clearly:

1. Choose the folder.
2. Add that folder as a project in Codex. State prominently that the user does this in the app and must first create the folder if it does not exist. Repeat the selected path in this action block. A checkbox records the user's claim of completion.
3. Show what Codex will do as a short table with prominent headings: the exact planned files, missing chats, and actual startup behavior. When the creation tool starts a reply, propose a brief automatic role acknowledgment with no file reads, tools, commands, changes, or development. Include this in the displayed plan, rather than leaving a later consent question.

Place one final "Confirm and create" button below the actions table. Its nearby label states that confirmation covers the displayed folder, files, chats, and first-reply behavior. Enable it only when an absolute path is present and the manual-step checkbox is checked. Reset that checkbox when the folder changes. An enabled button does not mean registration has been verified. If the target project is already verified, do not require the user to register it again; skip the manual action in the view. For manual setup, use an appropriate button label without promising automatic creation.

## Template and handoff

Use [../assets/setup.html](../assets/setup.html) with native inline visual support. If `visualize` is available, follow its current contract. Replace `{{ROOT_ID}}` with a unique safe identifier and `{{SETUP_JSON}}` with JSON, escaping less-than signs in embedded data. Keep the surrounding conversation unframed. Write generated views outside the product folder in an explicitly writable task-owned visualization location. Without native support, use one short table and a plain-language request for the path and registration step.

Configuration: `planId` identifies this setup revision; `projectName`, `suggestedPath` (or an empty string), `totalChats` (3, 5, or 7), `newChats`, `chatNames` (all names in the accepted structure), `files` (planned relative filenames), and `firstReplyMode` describe the plan. Choose a concrete mode before showing the final card: `acknowledgment` (offered now and approved by the final confirmation), `inactive` (supported no-turn mode), or `manual`. Do not generate a new card with a `pending` mode; the template treats that legacy value as an acknowledgment proposal and discloses it before confirmation. Set `requiresManualRegistration` to false only for an already verified project. Localize all English labels, including the confirmation and handoff text, via `labels` overrides. Do not embed personal defaults or real project IDs in the reusable asset. `previewOnly: true` is for demonstrations and must not send a message.

Before rendering, register the complete plan as described in [creation.md](creation.md). Also supply its ordered `chatRoles` and, when present, `chatDependencies` to the rendering config so they remain part of the handoff. Change `planId` whenever the project name, roles, dependencies, count, chat names, reuse choices, files, or startup behavior changes. A selected folder becomes bound to that revision at final confirmation. Never accept an old revision because its visible chat count happens to match.

On a deliberate button click, the template uses the documented `window.openai.sendFollowUpMessage({prompt, title})` mechanism. Its message explicitly confirms this plan revision, actual selected path, project name, total and new-chat counts, names, files, and displayed startup behavior, and asks Codex to verify the connection and perform those actions. This is bounded creation consent, not just a path notification or blanket permission. It sends only to the current conversation; do not dispatch another chat. If this API is unavailable or fails, show the same readable confirmation message for the user to send in the chat. A plain reply that confirms the complete displayed setup also suffices; a path alone is not creation consent. Host-required message confirmation remains under host control.

Widget state and checkbox claims are untrusted presentation data, never authorization or proof. Ignore stale state from another `planId`. When a handoff arrives, compare its name, folder, count, and roles with the latest agreed plan, check the actual folder and project listing, and use a real matching project ID. Do not read other unrelated chats to validate a visual.

The final button locks while opening a confirmation and remains locked afterwards, including after restoring that card's saved state. The host promise does not prove a message was submitted or a chat created. An explicit "Message not sent? Enable retry" action only unlocks the card and preserves its request identifier; it does not send anything. A repeated handoff must still pass the backend revision and creation ledger. Localize `confirmationOpened`, `retry`, and `requestLabel` too. Never infer approval from the local pending flag.

If the folder is not registered, tell the user what remains to do; create no project files or chats. Once the confirmed folder is verified and the complete plan is approved, start creation immediately. Do not repeat the chat proposal, insert another settings card, or ask again about the first reply. Keep verification details internal unless they block execution. If a check reveals a material change, show only the affected detail for correction. Never infer consent from restored widget state or the old "Check connection" message alone.
