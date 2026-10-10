#!/usr/bin/env python3
"""Validate metadata; visual QA and actual user approval remain separate."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
STATUSES = {"draft", "awaiting_approval", "approved", "rejected", "stale"}
errors = []
count = 0

def fail(path, message):
    errors.append(f"{path.relative_to(ROOT)}: {message}")

def asset(path, value):
    if not isinstance(value, str) or not value:
        fail(path, "missing approved asset path")
        return
    candidate = ROOT / value
    if Path(value).is_absolute() or ROOT not in candidate.resolve().parents:
        fail(path, "asset path must be inside repository")
    elif not candidate.is_file():
        fail(path, f"asset does not exist: {value}")

for path in sorted(ROOT.rglob("*.json")):
    if ".git" in path.parts:
        continue
    count += 1
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        fail(path, str(exc))
        continue
    if not isinstance(data, dict):
        fail(path, "expected JSON object")
        continue
    if "status" in data and data["status"] not in STATUSES:
        fail(path, "invalid status")
    if "templates" in path.relative_to(ROOT).parts:
        continue
    contract = None
    parts = path.relative_to(ROOT).parts
    if path.name in {"state.json", "character.json"}:
        contract = path.name
    elif "cenas" in parts:
        contract = "scene.json"
    elif "prompts" in parts:
        if "imagens" in parts:
            contract = "image-prompt.json"
        elif "videos" in parts:
            contract = "video-prompt.json"
    if contract:
        required = json.loads((ROOT / "templates" / contract).read_text())
        for key in required:
            if key not in data:
                fail(path, f"missing contract key: {key}")
    if data.get("status") == "approved":
        if contract == "character.json":
            asset(path, data.get("approved_reference"))
        if contract in {"character.json", "scene.json"} and not data.get("approval"):
            fail(path, "approved item needs recorded user approval")
    if contract == "video-prompt.json" and data.get("status") in {"awaiting_approval", "approved"}:
        asset(path, data.get("approved_image_path"))
    if contract == "state.json":
        events = data.get("approval_events", [])
        for event in events:
            if not isinstance(event, dict) or not all(event.get(k) for k in ("item_type", "item_id", "path", "version", "user_confirmation", "timestamp")):
                fail(path, "invalid approval event")
        for scene in data.get("scenes", []):
            if scene.get("approved_image_path"):
                asset(path, scene["approved_image_path"])
                if not any(e.get("item_type") == "scene_image" and e.get("item_id") == scene.get("scene_id") and e.get("path") == scene["approved_image_path"] for e in events if isinstance(e, dict)):
                    fail(path, "scene image lacks matching approval event")
    duration = data.get("duration_seconds")
    previous_end = 0
    for block in data.get("timeline", []):
        start, end = block.get("start_seconds"), block.get("end_seconds")
        if not all(isinstance(v, (int, float)) for v in (start, end, duration)):
            fail(path, "timeline requires numeric start/end/duration")
            continue
        if not (previous_end <= start < end <= duration):
            fail(path, "unordered or out-of-bounds timeline")
        previous_end = end

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {count} JSON files checked; visual QA and user approvals remain separate.")
