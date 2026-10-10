# TikTok Dark
This repository guides a human-directed short-video production workflow.
Speak to Welison in Brazilian Portuguese. Write operational instructions and generation prompts in English; keep approved dialogue in its original language, normally PT-BR.

## Start
Read docs/architecture.md and the relevant system below. For an existing episode, read its state.json, the entire historia.md, roteiro.md when it exists, the series bible, involved character records, and relevant adjacent scenes. Missing files are missing evidence, not permission to invent canon.

## Production entry point
For a new production, follow docs/workflows/iniciar.md. Claude Code uses /iniciar; Codex uses $iniciar. See docs/commands.md for setup and invocation. Preserve the reference-first and user-selected-direction gates.

## Prompt delivery and approval (mandatory)
Read docs/prompt-delivery.md for all character, scene-image and video prompts. Deliver exactly ONE copy-ready prompt, list the actual image attachments in order separately, then STOP for explicit approval of that prompt. Never auto-generate the image, write the next prompt, produce alternate prompts or a Plan B before that approval. Approval of a prompt does not approve its eventual rendered image. Read internal narrative documents but never reference documents/paths/metadata inside the external generation prompt. Never create .txt prompt files; use versioned .md. These current rules override older templates, historical examples and command instructions.

## Stage router
- Reference ingestion and analysis: docs/systems/01-reference-analysis.md
- Narrative DNA, direction options and collaborative story: docs/systems/02-story-modeling.md
- Character design and front reference: docs/systems/03-character-creation.md
- Scenes, dialogue and duration: docs/systems/04-scene-structuring.md
- Still-image prompt: docs/systems/05-image-prompting.md
- Approved-image animation prompt: docs/systems/06-video-prompting.md

Use templates/ for output contracts. Read relevant docs/lessons/ as historical evidence, not universal instructions. docs/integrations/watch.md describes the external ingestion dependency.

## Boundaries
- Present modeling directions and allow a custom direction. Wait for selection before developing that story.
- Story, character design and scene-image approvals belong to the user. Silence is not approval.
- Default character reference is one front image. Additional views require a concrete need and user request.
- Inspect available tools. A prompt file is not a generated image; a generated image is not approved.
- Character images anchor identity, not pose. Approved scene images anchor video's initial visual state.
- Do not overwrite approved assets. Write a new version and mark downstream work stale after upstream changes.
- Never claim to have watched, generated, uploaded or published without evidence.
- Keep reference-specific hooks, anatomy, scale and violence rules in that series, not the global engine.
- Work on the requested stage/scene. Do not launch agents or generate an entire batch implicitly.
- Do not expose secrets. Keep keys, local environments and binary media out of Git.
