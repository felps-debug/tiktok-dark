---
name: iniciar
description: Start a TikTok Dark video production when the user invokes iniciar or explicitly asks to begin from a reference video. Ask for a missing reference, ingest actual Watch evidence, analyze it, and offer modeling directions for the user to choose. Do not use for repository setup, existing scene generation, or unrelated videos.
---

# Iniciar produção

Locate the TikTok Dark repository root from the current worktree. Read AGENTS.md and docs/workflows/iniciar.md and execute the start workflow using the reference supplied in the current request.
If the reference is absent, ask for the URL or local video and wait. Do not assume a series or invent story content. Preserve the direction-choice checkpoint. Report actual evidence and tools, including a missing Watch capability.
