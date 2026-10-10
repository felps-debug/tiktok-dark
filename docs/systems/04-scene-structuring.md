# 04 — Scenes and dialogue
## Role
Turn the whole approved story into a shootable script with explicit continuity and a realistic duration budget.
## Reads
Whole historia.md, bible, character records, narrative beats, duration target and usable generation settings.
## Process
1. Establish final edit target and supported clip lengths; mark unknown settings, do not invent platform limits.
2. Divide by narrative function/action, preserving the approved causal order and essential beats.
3. Assign characters, previous/next context, initial state, action, exact dialogue, speaker, ending state and edit duration.
4. Estimate speech using a starting calibration near 3.3 words/second, with room for reactions and physical action. This is an estimate; emotional speech usually needs more time.
5. Prefer one primary speaker per generation clip. Split two-speaker exchanges at natural turns, preserving the narrative scene ID.
6. Do not pad a short beat to eight seconds or write long exposition just to fill a clip. Separate generation duration from retained edit duration.
7. When a split threatens total duration, propose shortening dialogue, holding visuals or editing; do not silently rewrite approved lines.
## Output
roteiro.md plus cenas/scene_XX.json from templates/scene.json. Show total edit duration, speech counts and any risky clips.
## Gate
Script is awaiting_approval until the user approves it. No visual prompts in this stage.
## Check
Every scene has a narrative purpose, adjacent continuity and a feasible timeline.
