# Primeira produção
## Preparar
Abra a pasta tiktok-dark no seu editor e inicie Claude Code ou Codex nela.
Configure Watch se ainda não estiver instalado. Sua configuração local e chaves não vão no Git.

## Primeira mensagem
> Read AGENTS.md and docs/architecture.md. I want to start a new production from this reference: [URL]. Use the reference-analysis system first. Save the evidence and analysis, then use story-modeling to offer distinct directions and a custom option. Do not choose the direction or write a completed story before I choose.

## Retomar
> Read AGENTS.md and series/[series-id]/[episode-id]/state.json. Read the full current story, series bible and available script. Tell me the next pending stage and continue only the requested work, respecting recorded approvals.

## Produzir uma imagem
> Work on scene [scene-id] using system 05. Read the full story, script, character records, adjacent scenes and approved references. Inspect the images. Write the JSON and the copy-ready English prompt. Generate only if the runtime provides image generation and I requested generation. Wait for my approval of the actual image.

## Produzir um vídeo
> Work on scene [scene-id] using system 06. Inspect the approved scene image and read the full story and script. Check speech timing and continuity. Write the JSON and copy-ready Flow prompt. If the image cannot support the scene, report the precise mismatch before writing a final video prompt.

## Registrar escolha e aprovação
Diga qual versão aprovou, por exemplo: “Aprovo scene_01_v2.png”.
O agente registra caminho, versão e aprovação em state.json/registro do personagem.
Nenhuma produção de exemplo neste repositório já foi aprovada.
