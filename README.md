# TikTok Dark
Base de produção para analisar referências, explorar caminhos de modelagem e produzir curtas com imagens no Codex e vídeos no Google Flow.

## Comece aqui
1. Abra esta pasta no Claude Code ou Codex. Os arquivos de instrução já estão prontos; não precisa usar /init para recriá-los.
2. Confira docs/quickstart.md e configure Watch conforme docs/integrations/watch.md.
3. Inicie uma série/episódio com os modelos em templates/. Leia a história inteira em cada etapa.
4. Envie a referência. O agente analisa e oferece direções; você escolhe ou propõe outra.
5. Desenvolva e aprove a história, gere e aprove personagens de frente, depois organize as cenas.
6. Gere um prompt de imagem por cena, gere a imagem no Codex e aprove a versão.
7. Gere o prompt de vídeo a partir da imagem aprovada e leve imagem + prompt para o Flow.

## O que já está preparado
- Índice compartilhado AGENTS.md e entrada CLAUDE.md.
- Seis sistemas operacionais com entradas, leituras, saídas e limites.
- Contratos JSON e modelos de história, bíblia, análise e direções.
- Três análises históricas preservadas em docs/lessons/.
- Pasta Baratas com pendências de importação explicitadas.
- scripts/validate.py para verificar JSONs e referências aprovadas.

Os sistemas são documentos carregados sob demanda pela sessão. Não há automação de renderização, subagentes registrados nem integração autenticada com Flow incluída.

## Arquivos existentes de Baratas
A história vigente, roteiro e imagens reais ainda precisam ser importados da sua máquina. Os relatos históricos não substituem esses arquivos. Confira series/baratas/IMPORTAR.md.

## Validação
Execute na raiz: `python scripts/validate.py`.
As lições são relatos empíricos, não garantias de geração. A duração de 8 segundos é uma calibração histórica, não mínimo universal.
