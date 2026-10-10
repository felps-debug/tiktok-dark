# Comandos de produção

| Ambiente | Iniciar sem referência | Iniciar com referência |
|---|---|---|
| Claude Code | `/iniciar` | `/iniciar https://www.tiktok.com/@perfil/video/ID` |
| Codex CLI / extensão | `$iniciar` | `$iniciar Analise esta referência: https://www.tiktok.com/@perfil/video/ID` |

Sem referência, o agente pede o link ou arquivo. Com a referência, confere o Watch, preserva evidências, analisa e oferece caminhos de modelagem. Você escolhe ou propõe outra direção antes da história ser desenvolvida.

O `/init` do programa continua com sua função original. Para iniciar a produção use a entrada acima. O Maestro é o ambiente que hospeda a sessão; a sintaxe depende do agente aberto nela.

## Personagem animado a partir de uma foto
No Codex, envie `$profilepic` com a foto anexada ou um caminho acessível. No Claude Code, use `/profilepic`; sem gerador de imagens, ele prepara o prompt para levar ao Codex junto com a mesma foto.

Sem foto, a entrada pede a referência e espera. O padrão é um personagem 3D animado reconhecível, corpo inteiro de frente, fundo branco e formato 9:16. Pode pedir outro estilo na mesma mensagem. Entrega um único prompt, com a lista de fotos a anexar, e espera sua aprovação. Só depois gera uma candidata quando solicitado e houver ferramenta real de imagem; a imagem também precisa de aprovação separada. Não é avatar do TikTok; é a referência de identidade do personagem para as cenas.

A skill não instala nem habilita um gerador: em um Codex sem geração de imagens disponível, entrega o prompt e avisa a limitação. O fluxo está em `docs/workflows/profilepic.md`.

## Atualizar uma cópia já clonada
Na pasta do projeto, execute `git pull --ff-only`. Se houver alterações locais conflitantes, preserve-as antes de resolver o conflito. Reinicie a sessão Claude Code ou Codex se a nova entrada não aparecer. No Codex, também é possível conferir a skill pelo `/skills`.

## Arquivos e dependências
- `.claude/commands/iniciar.md`: entrada do Claude Code.
- `.agents/skills/iniciar/SKILL.md`: entrada do Codex.
- `docs/workflows/iniciar.md`: procedimento compartilhado.
- Watch: dependência externa; consulte `docs/integrations/watch.md`.

Uma referência nova ainda sem universo escolhido fica provisoriamente em `reference/<reference-id>/`. Depois da sua escolha, as evidências passam para `series/<series>/<episode>/referencia-original/`. O comando não escolhe Baratas automaticamente.

Os comandos orientam o agente a usar suas ferramentas disponíveis. Não fornecem download próprio, não iniciam outro agente automaticamente e não substituem sua aprovação. Claude produz prompts; a geração de imagens usa o Codex quando disponível e os clipes continuam no Google Flow.

Documentação dos formatos:
- Claude Code: https://code.claude.com/docs/en/skills
- Codex: https://learn.chatgpt.com/docs/build-skills

## Prompts de cenas e vídeos
Siga `docs/prompt-delivery.md`: anexos visuais em ordem, um único prompt pronto para copiar e pausa obrigatória para aprovação. Imagens de cenas usam Nano Banana; vídeo usa a imagem de cena aprovada como primeiro frame no Flow. Sem referências a documentos dentro do prompt, sem JSON de controle na entrega e sem arquivos .txt de prompts.
