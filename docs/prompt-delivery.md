# Copy-ready image and video prompts

## Non-negotiable interaction
Deliver exactly ONE prompt per response, for the requested current character/scene/clip. First show ordered actual image attachments, then the prompt, then ask in Portuguese: "Aprova este prompt ou quer ajustar algo?" STOP. Even an explicit batch request must follow this one-at-a-time gate: do not prepare the next prompt until the user approves the current one. On correction, deliver only one revised prompt and pause again. Prompt approval and generated-image approval are distinct. Do not generate media while its prompt approval is pending. A previous generic instruction to continue is not approval of a new unseen prompt.

## Attachments outside the prompt
Use a numbered list: character name or scene + exact existing image filename/path + role. For Nano Banana, list each required approved character photo in attachment order; add a real continuity image only when needed. For Flow, list the approved scene image as first frame; other images only when required by the selected mode. Missing essential images block delivery until supplied; never invent a filename or claim to inspect an unavailable image.
Repository image paths help the USER select files and belong only in this list/internal records. Inside the generation prompt refer to Attachment 1, Attachment 2 and character names/visual descriptions. Never mention AGENTS.md, historia.md, roteiro.md, character.json, state.json, prompt files, source lists or "follow the document". Both external tools receive all required visual instructions in the prompt itself.

## Image structure (Nano Banana)
One concise English copy-ready block with these sections, in this order:
- FORMAT AND STYLE: aspect ratio and explicit series style.
- ATTACHED REFERENCES: ordered attachment identities/roles. Use identity only; do not copy reference-sheet pose/background.
- SCENE AND COMPOSITION: one static instant, environment/light, shot/framing, left/right positions, critical scale/props.
- CHARACTERS AND EXPRESSIONS: who wears/holds what, gaze, posture, mouth and emotion; visual humor when relevant.
- AVOID: only relevant short constraints.
This restores the meaningful visual structure without a giant internal JSON. No placeholders in a delivered prompt. Do not provide a second JSON copy of the same prompt.

## Video structure (Flow)
One concise English copy-ready block with:
- FORMAT AND CONTINUITY: duration/aspect ratio, attached image as first frame, stable identity/environment and camera.
- ACTION: a simple chronological action with initial and final state; few broad timing ranges only when useful.
- DIALOGUE AND PERFORMANCE: exact PT-BR lines, speaker, emotion/intonation, pacing/pauses; listening characters silent.
- SOUND: relevant SFX/music/silence supporting humor/emotion.
- AVOID: concise relevant constraints.
No internal paths, schemas, statuses, source lists, budgets, QA tables, alternate prompts or Plan B. Keep mechanical details only when needed to prevent a concrete failure; more constraints do not justify contradictory or overloaded choreography.

## Internal persistence
Read full narrative context internally. Existing JSON templates remain internal metadata contracts, not external prompt formats. Source provenance can stay in internal records. Save the copy-ready block and ordered attachments in a versioned .md prompt file. Never create .txt prompt documents. Preserve existing legacy files and approved assets; do not bulk delete them or silently reapprove revised prompts. Existing drafts must be reformatted one at a time when requested, not all regenerated automatically.
