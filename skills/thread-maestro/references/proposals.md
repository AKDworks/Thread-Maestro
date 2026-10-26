# Card proposals

Read when presenting or revising a structure. Use the user's language.

## First reply

Return one short recommendation, one card diagram, and one brief question about keeping or changing the structure. Aim for at most 60 prose words outside the visual. Do not repeat totals, roles, or scopes below it.

The closing question requests design feedback, not permission to create chats. For example: "What would you change in the names or roles?" End there. Do not add an ordinary footer citing the skill, quoting its description or approval rules, or explaining that discussion must come first. This presentation rule does not suppress approval explanations required by higher-priority instructions at the actual action stage.

Recommend 3, 5, or 7 chats including the main chat. Keep other choices out of the first response unless they help the immediate decision. For an unsupported number, offer nearby supported totals. Redraw when the user selects a different total; never treat acceptance of an earlier layout as approval of its replacement.

Defer storage paths, registration steps, organizational documents, search coverage, and first-turn behavior until setup decisions are needed. Explain a blocker only when it affects the current choice, briefly with the next action. Retain disclosures required by higher-priority instructions.

## Layout

- One wide main-chat card at the top, with an outline icon, title, and short purpose.
- A small downward connector labeled "Project chats" in the user's language. It shows grouping, not automatic task assignment.
- Specialist cards beneath: 2 in one row for 3 total, a 2-by-2 grid for 5, or 3 columns and 2 rows for 7. On narrow screens, wrap into fewer columns while preserving all cards.
- Each specialist card has one matching outline icon, its title, and a short scope description. Adapt roles to the project; example interface, animation, implementation, or testing roles are not mandatory.
- Use consistent icon size and stroke, quiet neutral surfaces, rounded cards, and readable labels. Do not substitute a table, Mermaid graph, emoji, screenshot, or long list when native card rendering is available.
- Mark an existing chat only after verification. Explain a material dependency concisely when it affects selection; avoid filling every card with repeated status fields. A proposed role is not a created chat.

## Rendering

Use documented inline visual support. If `visualize` is available, read its current instructions and adapt [../assets/proposal.html](../assets/proposal.html) as a contained proposal interface. Its product-scoped styles implement the requested cards; keep the surrounding conversation surface unframed. The supplied Lucide runtime provides outline icons. Do not download an icon library; omit an unavailable icon rather than inventing an API.

Prefer [../scripts/render_proposal.py](../scripts/render_proposal.py) with Python 3. Write the plan JSON, choose an allowed absolute output path, and run:

```text
python <skill>/scripts/render_proposal.py --plan <task>/proposal-plan.json --output <task>/chat-proposal-<revision>.html
```

The helper validates 3/5/7 layouts, escapes embedded data, fills the template, and returns the absolute fragment path and the native content reference. Choose a fresh filename for each proposal revision; an existing output is not overwritten. Embed that reference in the final answer. It neither creates chats nor sends messages. If Python is unavailable, fill the template using another available file tool; do not downgrade to a table merely because the helper cannot run.

Replace `{{ROOT_ID}}` throughout with a unique safe identifier and `{{PLAN_JSON}}` with JSON. Escape less-than signs in embedded JSON to avoid closing a script through user text. The object contains `selected`, localized `countLabel` and `groupLabel`, and `variants` keyed by supported totals. Each variant has a `main` card and a `specialists` array of exactly total minus one; cards contain `title`, `description`, and a known Lucide `icon` name. Use plain text fields, not user-supplied markup.

Normally supply only the recommended variant. Supply other variants and the local count switcher only when the user requests comparisons or count controls, using a meaningful role plan for each. Switching a preview is not consent to create chats. Widget state is a presentation preference, not authorization; obtain an explicit user message for creation and resolve uncertain count selections before acting.

Write the fragment only to an explicitly writable task-owned visualization location outside the product project. Rendering a proposal does not authorize project files, folders, or chats. Do not install plugins, start a server, or build a website just to display it. If native output or a suitable location is unavailable, use one compact Markdown table with Chat, Scope, Dependencies, Status as fallback.

For an idea without a product folder yet, the current chat's own writable scratch workspace may hold the proposal; it is not the future product project. Keep it in a small task artifact folder. Do not reject an available writable task location because the app project has not been registered yet. A missing project ID does not prevent a visual proposal.

Embed the fragment using the host's documented mechanism. For `visualize`, use its actual absolute path:

```text
visualize{"path":"/absolute/task-owned/path/chat-proposal.html"}
```

Do not replace it with a link, browser tab, source code, or duplicate text table. After selection, follow [setup.md](setup.md) for the setup card and request only missing decisions. Do not ask to approve an unchanged structure again.
