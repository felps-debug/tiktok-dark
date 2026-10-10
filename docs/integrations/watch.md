# Watch integration
Upstream: https://github.com/bradautomates/claude-video
Documentation checked on 2026-10-10. Watch supplies timestamped frames and transcripts; native captions are preferred, with optional transcription fallbacks.

## Claude Code
Inside the Claude Code session, one command at a time:
```
/plugin marketplace add bradautomates/claude-video
/plugin install watch@claude-video
```
Follow activation/restart instructions. Invoke the installed skill through autocomplete, normally /watch:watch, or ask to use Watch.
If already installed, do not reinstall automatically.

## Codex
Upstream suggests asking a local Codex session:
```
Use $skill-installer to install the watch skill from:
https://github.com/bradautomates/claude-video/tree/main/skills/watch
```
This depends on the local skill-installer actually being available. Follow upstream/runtime setup when absent.
This repository does not claim that Watch is installed on your computer.

## Evidence handling
Copy the actual report, transcript and evidence index into the episode's referencia-original/ before temporary output is deleted.
Keep local media/frames available for inspection. Record extraction coverage, engine and uncertainty. Never commit keys or cookies.
A cloud/browser runtime may not support the local dependencies or video download. Report this and accept user-supplied evidence instead; never pretend a URL alone was watched.
