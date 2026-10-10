# Comandos de produção

| Ambiente | Iniciar sem referência | Iniciar com referência |
|---|---|---|
| Claude Code | `/iniciar` | `/iniciar https://www.tiktok.com/@perfil/video/ID` |
| Codex CLI / extensão | `$iniciar` | `$iniciar Analise esta referência: https://www.tiktok.com/@perfil/video/ID` |

Sem referência, o agente pede o link ou arquivo. Com a referência, confere o Watch, preserva evidências, analisa e oferece caminhos de modelagem. Você escolhe ou propõe outra direção antes da história ser desenvolvida.

O `/init` do programa continua com sua função original. Para iniciar a produção use a entrada acima. O Maestro é o ambiente que hospeda a sessão; a sintaxe depende do agente aberto nela.

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
