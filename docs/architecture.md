# Production architecture
## Knowledge layers
1. Engine: docs/systems/ and templates/ define reusable methods.
2. Series: series/<id>/series-bible.md and personagens/ define universe and identity.
3. Episode: series/<id>/<episode>/historia.md, roteiro.md, cenas/ and state.json define current production.
4. Research: docs/lessons/ records historical findings, including conflicts and uncertainty.

Do not elevate Baratas-specific anatomy, losses, miniature environments or off-screen violence to global rules. Treat numerical prompt limits as starting calibration, not platform guarantees.

## Canonical paths
- Series bible: series/<id>/series-bible.md
- Character record: series/<id>/personagens/<character>/character.json
- Character images: same folder/imagens/
- Reference evidence: series/<id>/<episode>/referencia-original/
- Whole approved episode story: series/<id>/<episode>/historia.md
- Scene script: same episode/roteiro.md
- Scene definitions: same episode/cenas/scene_XX.json
- Image/video prompts: same episode/prompts/imagens/ and prompts/videos/
- Media: same episode/imagens/ and videos/, each with approved/ and discarded/
- Workflow state: same episode/state.json

All recorded paths are relative to repository root and use forward slashes.
A legacy series/<id>/historia.md is import material until explicitly reconciled with episode stories; never maintain two competing canonical stories.
A narrative scene can require several generation clips (01A/01B). A clip is not automatically a new narrative beat.

## Stage contract
| System | Reads | Writes | Gate |
|---|---|---|---|
| 01 | Reference media and actual Watch outputs | Evidence index, transcript, analysis | Evidence coverage reported |
| 02 | Complete analysis and series constraints | DNA, directions, selected direction, whole story | Direction chosen, then story approved |
| 03 | Approved story, bible, character briefs/style anchors | Character record, front prompt, generated candidate when available | User approves exact character version |
| 04 | Whole approved story, characters, target duration | Script and scene definitions | User approves script |
| 05 | Whole story, script, scene and neighbors, actual references | Image JSON + prompt; generated candidate if requested | User approves exact scene image |
| 06 | Same narrative context + inspected approved image | Video JSON + prompt | User generates in Flow and records result |

Stages can be revisited. Do not skip a missing approval by inferring it from file existence.
Use draft, awaiting_approval, approved, rejected and stale. Record approval event as item, path, version, user confirmation and timestamp. Do not impersonate a user approval.

## Source precedence
A current user correction sets intended changes; it does not make an old visual match those changes.
Approved current story governs plot; approved script governs exact dialogue; character reference governs identity; approved scene image governs the video initial visual state.
If these conflict, explain the concrete mismatch and update the upstream asset/version. Do not quietly change plot to match an image or redesign characters in video.
Historical lessons and old drafts never override current approved canon.

## Context protocol
Before an individual scene: read the complete story and existing script, the series bible, involved character records, scene definition and adjacent scene states.
Inspect visual references instead of inferring them from filenames. Write a short context check with files read, narrative function, initial/end state and missing inputs. Do not expose private reasoning.
References have explicit roles: identity, style_only, continuity or first_frame.

## Duration and revision
Set the desired final edit duration and available generation durations before dividing the story.
Track speech time, reaction time and transition allowance. Generated clip length and retained edit length differ.
Changing story/script invalidates affected downstream scenes/prompts. Changing the approved image invalidates its video prompt.
Preserve older approved versions. Write new versioned candidates, update state, and keep superseded approval records.

## Capabilities and failures
Watch is an external dependency, not bundled or installed by this repository.
Image generation requires the runtime's real capability. Without it, supply a copy-ready prompt.
Google Flow generation remains manual. No upload or successful render is implied by a prompt.
When evidence or tools are unavailable, record the blocker and work only on independent tasks.
