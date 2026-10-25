# Revision checks and creation recovery

Read before rendering the final setup and before creation or recovery. Use [../scripts/setup_guard.py](../scripts/setup_guard.py) with an available Python 3 runtime. It has no third-party dependencies or app access. It checks consistency and records tool results; human consent and verification through real app tools remain necessary.

Keep the plan, confirmation, and state JSON in an explicitly writable durable task location outside the project being organized. Do not add logs, test records, or a guard database to the user's product. Use one state path for this setup across replies. If Python is unavailable, preserve the same plan and step checks in the task's records and disclose only a resulting practical limitation.

## Register the displayed plan

The plan JSON contains `planId` (a new unique revision identifier), `projectName`, `totalChats`, `newChats`, ordered `chatNames`, equally sized ordered `chatRoles`, `files` (relative filenames), and `firstReplyMode`. Optional `chatDependencies` captures the agreed dependencies. `reusedChats` maps verified reused titles to their real IDs; omit it for all-new chats. `newChats` must equal the total minus those reused chats. Keep this richer plan alongside the rendering config; no need to repeat all these fields in prose.

```text
python <skill>/scripts/setup_guard.py --state <task>/setup-state.json register <task>/setup-plan.json
```

Register before showing a final card. A changed plan needs a new `planId`; retired revisions cannot be reactivated. The helper refuses changed content under an unchanged ID. Selecting a custom folder in that card is allowed; the first final confirmation binds the actual verified folder and project ID to that revision. A later change of target requires a new displayed revision and confirmation.

## Validate the final confirmation

Confirm the deliberate user message matches the latest displayed revision, complete roles and dependencies, file choices, startup mode, counts, and reuse choices. Do not copy current plan values over conflicting incoming fields merely to make validation pass. Widget state is not consent. Stale messages produce no creations; refer briefly to the current plan.

After verifying the actual folder and matching project with app tools, prepare confirmation JSON with the same complete plan plus `folder` and the real `projectId`. Then run:

```text
python <skill>/scripts/setup_guard.py --state <task>/setup-state.json --plan-id <current-id> begin <task>/setup-confirmation.json
```

`begin` is repeatable: it keeps earlier results for the same approved target. It never grants permission on its own. Check its `pending`, `unresolved`, and `complete` fields. For an already complete setup, report its existing result and create nothing. A repeated message or an enabled retry control does not reset progress.

## Claim, create, record, verify

For each missing chat, in the agreed order:

```text
python <skill>/scripts/setup_guard.py --state <task>/setup-state.json --plan-id <current-id> claim "<exact title>"
```

Call the app's creation tool only when this returns `create: true`. The claim is written before the external call, so an interruption leaves an unresolved attempt rather than an apparently missing chat. Immediately record the real returned ID and host:

```text
python <skill>/scripts/setup_guard.py --state <task>/setup-state.json --plan-id <current-id> record "<exact title>" --status created --thread-id <real-id> --host <host>
```

For a preparing result, use `--status preparing --client-thread-id <returned-id>`; never invent a ready ID. Verify existence, title, project membership, and acknowledgment using the app tools. Mark `ready` with the real thread ID only after those checks. Keep unknown outcomes as `outcome_unknown`; retrying a claim will not create another chat. Use `failed` only when it is established that no creation took place. A tool error alone is not such proof, and any returned ID must be investigated before retrying.

After interruption, run `status` with the same `--state` and `--plan-id`. Reconcile `unresolved` entries against the app, then continue only `pending` entries. The same plan needs no fresh approval. The state file uses an exclusive lock and atomic replacement; if a crash leaves a lock, first establish that no writer is running before removing only that task-owned lock. Do not infer app state from the local ledger alone.

Finish with a short verified result and supported opening elements. For example: "Done. Created 3 chats." For partial success, state the actual count and one practical issue. Keep tool logs, revision IDs, and recovery details out of ordinary success replies.
