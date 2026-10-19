# Open Nectar iOS continuation

Read `ios/OPEN_NECTAR_IOS_STATUS.md` first. It records both games, preservation rules, verified baseline, investigations, validation boundaries, and exact next actions.

Before edits: verify origin, branch, `git status`, fetch, compare HEAD and origin/ios-experimental, and preserve unexpected changes. Never run downloaded patch installers blindly.

Priorities: preserve working Pikmin 1 framebuffer behavior; improve settings clarity; resolve Pikmin 2 compiler failures; then test existing camera dragging and work toward Pikmin 2 runtime.

Retrieve Actions logs through existing authenticated GitHub access. Keep proprietary assets and credentials outside Git. A Windows source/semantic check is not iOS compilation, and successful iOS compilation is not phone runtime validation.

Update the status journal at milestones and provide self-contained progress reports in chat. Before ending, export a complete CODEX TO CHATGPT MASTER HANDOFF including exact local/remote commits, dirty files, changes, tests, run IDs, artifacts, remaining issues, and next steps. Avoid `[ios-build]` on documentation-only commits.
