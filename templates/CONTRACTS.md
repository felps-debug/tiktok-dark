# JSON contracts v1
Templates are editable contracts, not platform/API schemas. Null means unknown. All paths are repository-relative. Attach real images to generators; paths alone do not provide visual references.

## Shared values
status: draft, awaiting_approval, approved, rejected, stale.
approval: null or user_confirmation, timestamp and version; record only real user confirmation.
context_sources: files actually read.
references: objects with file, role (identity, style_only, continuity, first_frame), character_id when applicable.

## Scene
dialogue items: speaker_id, text, delivery, word_count.
edit_duration_seconds: retained edit length; generation_duration_seconds: generated length.
clip_ids permits several clips for one narrative scene.

## Image
characters items: character_id, identity_locked, outfit_this_scene, pose, limb_placement, gaze_target, expression (eyes, brows, mouth).
Use the approved anatomy, not a universal limb count.

## Video
dialogue items: speaker_id, text, delivery, word_count, start_seconds, end_seconds, off_screen.
timeline items: start_seconds, end_seconds, primary_action, secondary_actions, listener_reaction.
Times must be ordered within duration_seconds. approved_image_path must match an actual approval event.
flow_result: null or actual user feedback with status, path/version when available and notes.

## State
scenes items: scene_id, status, approved_image_path, image_version, video_status.
characters items: character_id, record_path, status.
approval_events items: item_type (story, script, character, scene_image), item_id, path, version, user_confirmation, timestamp.
No approval is implied by file presence.

## Validation limits
scripts/validate.py checks JSON syntax, minimal keys, statuses, approved asset paths and timeline bounds.
It does not authenticate user confirmation, inspect visual identity or measure rendered speech.
