# 06 — Image-to-video for Flow
## Role
Animate an inspected approved scene image while preserving story, identity and continuity.
## Reads
Whole historia.md and roteiro.md, bible, scene and neighbors, relevant character identity/voice records, and the exact approved initial image.
## Process
1. Confirm actual user approval and inspect the initial image. Describe only visible initial facts; label uncertainty.
2. Compare the image with required speakers/actions/props. If essential visual information is absent or contradicted, request an upstream image revision; do not repair it by inventing a new visual in video.
3. Set available generation duration. Count exact dialogue words and estimate usable speech time. 26 words in eight seconds is a historical upper calibration, not a guarantee. Allow room for emotion and pauses.
4. Prefer one main speaker. Keep listeners silent with mouth closed; identify intentional off-screen voice without inventing an unseen visual identity.
5. Use one continuous shot and one simple camera movement with stated start/end. Choose a restrained primary action and few secondary gestures.
6. Write timestamped blocks for initial posture, speech/action and final state. Speech may begin promptly, but need not end on the last frame; reserve readable reaction/transition time.
7. For connected split clips, use the actual exported final frame of A as B's first-frame anchor when available. Do not claim continuity from a hypothetical frame.
8. Keep approved dialogue literal in PT-BR with natural delivery and stable voice traits. If it does not fit, propose a split/shortening for approval.
9. Specify diegetic SFX and the series' music policy. For difficult speech/action combinations, propose silent generation and dubbing as a production option, without claiming equivalence.
10. Compile video_prompt from the JSON fields, avoiding duplicate/conflicting descriptions.
## Output
prompts/videos/scene_XX[_A]_vN.json and .txt using template, attachment path, speech budget and likely QA risks.
## Check and result
No redesign, invented character, age/scale drift or contradictory first frame. Preserve series-specific depiction rules; do not formulate filter-bypass instructions.
User runs Flow. Record actual success/failure feedback, then refine only the affected prompt/upstream asset.
