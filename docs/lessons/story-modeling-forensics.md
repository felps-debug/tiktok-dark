**# Análise forense: como modelamos a história original e criamos a nossa (baratas)**



**\*\*Objetivo deste documento:\*\*** registrar o PROCESSO que aconteceu e o conhecimento que surgiu, para virar um agente especializado em modelagem de histórias a partir de uma história de referência. Não cria história, cena nem prompt.



**## Convenções**

\- **\*\*[EVIDÊNCIA]\*\***: está escrito na conversa, num arquivo do projeto ou nas memórias do projeto. Indico a fonte.

\- **\*\*[INFERÊNCIA]\*\***: conclusão minha a partir de evidência. Pode estar errada.

\- Fontes: a **\*\*conversa\*\*** (esta sessão); \`historia.md\`; \`ep-01/roteiro_ptbr_v2.md\`; \`referencia-original/analise_parte2.md\`; \`\_sistema-image-to-video.md\` e \`\_licoes-prompts-de-imagem.md\` (escritos por outras sessões); \`prompts/videos/\*.json\`; as 4 memórias do projeto.



**## Limites desta análise (ler primeiro)**

1\. **\*\*Os frames extraídos não existem mais.\*\*** [EVIDÊNCIA: apaguei as duas pastas temporárias do \`/watch\` depois de cada análise, na conversa.] Só restam as minhas leituras deles, na conversa.

2\. **\*\*A análise do vídeo original, Parte 1, não foi salva em arquivo.\*\*** Ela existe só na conversa. A da Parte 2 foi salva (\`analise_parte2.md\`). [EVIDÊNCIA]

3\. **\*\*As transcrições não foram salvas.\*\*** Elas estão no relatório de cada rodada, na conversa. A do WhisperX tinha erros de nome ("Bobbytoe", "Bobbito", "big backs" incerto). [EVIDÊNCIA: relatório do \`/watch\` e minha nota na análise.]

4\. **\*\*A Parte 3 do original nunca foi enviada nem analisada.\*\*** [EVIDÊNCIA: você disse "vou te mandar o 3" e depois definiu "dois episódios".]

5\. **\*\*Parte do histórico está fora desta conversa.\*\*** O roteiro v2, as cenas de imagem e vídeo (11A/11B, 04A/04B...) e os resultados dos clipes vieram de outras sessões. Só os vejo pelos arquivos e pelas memórias. [EVIDÊNCIA: datas dos arquivos e memória \`baratas-video-limites-comprovados\`.]

6\. **\*\*Não ouvi áudio nem trilha do original.\*\*** Tudo sobre som é fala transcrita e legenda. [EVIDÊNCIA: disse isso na primeira análise.]



\---



**# 1. COMO ANALISAMOS O VÍDEO ORIGINAL**



**## 1.1 Ferramenta e coleta**

\- **\*\*Setup:\*\*** você chamou o \`/watch\` com um pedido de 8 pontos (estrutura, personagens, enredo, cena por cena, ambientes, falas, linguagem cinematográfica, fórmula). Na primeira execução escolheu o engine **\*\*local\*\***. Instalei ffmpeg, yt-dlp e WhisperX. [EVIDÊNCIA: conversa]

\- **\*\*Parte 1 (73,8 s):\*\*** 57 frames escolhidos de 60 candidatos, amostragem **\*\*uniforme\*\*** (≈1 por segundo; o relatório indica "uniform fallback", sem eu ter investigado o motivo), 3 quase-duplicados descartados. Transcrição WhisperX "small", 3 segmentos. Li os 57 frames. [EVIDÊNCIA: relatório e minhas leituras]

\- **\*\*Parte 2 (70,1 s):\*\*** 59 de 60 frames; transcrição em 4 segmentos. Li 39 dos 59 (cobertura de cerca de 1 frame a cada 2 s). [EVIDÊNCIA]

\- **\*\*Margem:\*\*** os timestamps têm ±1 s. Os frames 17 a 19 da Parte 1 (00:19 a 00:22) foram descartados como duplicados. [EVIDÊNCIA]



**## 1.2 Como cada tipo de informação foi extraído**

\| O que | Como foi identificado | Fonte |

\|---|---|---|

\| **\*\*Personagens\*\*** | Leitura visual dos frames (roupa, cabelo, adereços, expressão), comparando entre cenas | frames |

\| **\*\*Enredo\*\*** | Frames em ordem + transcrição; reconstruí cena por cena e dei timestamp aproximado | frames + transcrição |

\| **\*\*Falas-chave\*\*** | Transcrição, corrigida pelas **\*\*legendas queimadas na tela\*\***, que mostram o nome correto e destacam em amarelo a palavra-chave | transcrição + frames |

\| **\*\*Ritmo\*\*** | Mudanças de enquadramento entre frames consecutivos: blocos de 3 a 11 s, mais curtos no fim | frames |

\| **\*\*Viradas\*\*** | Pontos em que o tom muda de modo visível: o corte para a morte (00:52), o escurecimento antes de cada local novo, a promessa final | frames + transcrição |

\| **\*\*Padrões de edição\*\*** | Fades para preto em ≈0:05, ≈0:15, ≈0:28, ≈0:47, ≈0:55, ≈1:06; câmera quase estática; legendas palavra por palavra; cartão de marca em 0:11 | frames |

\| **\*\*Retenção\*\*** | Hook visual+verbal nos 5 primeiros segundos; piadas curtas; pausa antes da piada; final em aberto | frames + transcrição |

\| **\*\*Estrutura narrativa\*\*** | Agrupei os blocos pela função (perda, exposição, dúvida, autoridade...) e não pelo local | síntese |



[INFERÊNCIA] Cada cena do original parece ser um clipe de vídeo de IA de 3 a 8 s emendado (cortes coincidem com mudanças de cenário e com os fades). Não verifiquei.



**## 1.3 Superfície vs estrutura (Parte 1 original)**

\| ELEMENTOS DE SUPERFÍCIE (trocáveis) | ESTRUTURA NARRATIVA (preservar) |

\|---|---|

\| Mosquitos, sangue, mosquito-mãe de camisola de hospital, médico de óculos | Uma perda irreparável dita com calma logo no começo |

\| "Machos vivem 2 semanas" | Uma regra do mundo que cria prazo, dita em diálogo |

\| Cartão "3 days later", marca @fruitheatre | Um salto de tempo marcado |

\| Academia, aula sobre humano "big back", sargento, pântano | O herói entra numa instituição que normaliza o ato violento |

\| Reggie, a "mordida" no braço do humano | Um colega simpático que existe só para morrer |

\| Tapa fora de quadro | Choque cômico-violento que acontece fora da tela |

\| "Jeito ético de sugar sem morrer" | A mãe oferece uma regra moral que abre um loop |

\| Família no churrasco, mosquito no pulso do avô | Cliffhanger com o payoff escondido |



**\*\*Fórmula real do original (Parte 1)\*\*** [EVIDÊNCIA: a primeira análise, na conversa]:

\> perda irreparável (hook) → exposição disfarçada de conversa + prazo → salto de tempo marcado → o mundo normaliza o ato → herói duvida → mentor empurra com "decida depois" → autoridade grita + colega simpático → ordem com ironia ("gentilmente") → pausa → morte fora de quadro → pânico → refúgio na mãe → promessa de um jeito ético → cliffhanger.



**\*\*Parte 2 do original:\*\*** é outra fórmula, de **\*\*vingança e corrupção\*\*** [EVIDÊNCIA: \`analise_parte2.md\`]:

\> cena de perda (mãe morta) → promessa de vingança → mentor avisa → salto de tempo → herói mudou (visto pelos outros) → crueldade com quem o ama → aviso ignorado → upgrade → discurso de multidão → ataque → morte do herói → semente da próxima (esposa grávida).



\---



**# 2. COMO EXTRAÍMOS A "FÓRMULA" (beats do original, Parte 1)**



**\*\*Observação de método [EVIDÊNCIA/INFERÊNCIA]:\*\*** na conversa eu extraí a **\*\*sequência\*\*** e as funções em prosa (seções "Estrutura" e "Fórmula"), mas **\*\*não fiz uma tabela formal por beat com função, emoção e pergunta aberta\*\***. A tabela abaixo é a reconstrução dessa operação a partir da análise que existe. As colunas "função", "emoção" e "pergunta" são **\*\*[INFERÊNCIA]\*\***; o evento literal é **\*\*[EVIDÊNCIA]\*\***.



**\*\*BEAT 1: Perda (0:00–0:05)\*\***

\- Evento literal: a mãe-mosquito pergunta pelos bebês; o médico diz que morreram, só o menino sobreviveu.

\- Função: hook por perda irreparável; define o protagonista como único sobrevivente.

\- Emoção: choque e tristeza com humor sombrio (contraste fofo × trágico).

\- Pergunta aberta: o que será desse sobrevivente?

\- Preservar: abrir com uma perda, dita com calma, nos 5 primeiros segundos, e um único sobrevivente.

\- Trocar: espécie, lugar, causa da morte.



**\*\*BEAT 2: Exposição e prazo (0:05–0:11)\*\***

\- Evento: levar o bebê à Academia em 3 dias; machos vivem 2 semanas; boa sorte.

\- Função: regra do mundo + prazo + presságio.

\- Emoção: fatalismo e curiosidade.

\- Pergunta: que Academia é essa? por que a pressa?

\- Preservar: um fato do mundo e um prazo, entregues em diálogo emocional.

\- Trocar: o fato em si (envelhecimento rápido).



**\*\*BEAT 3: Salto de tempo (0:11–0:12)\*\***

\- Evento: cartão de marca "3 days later"; o bebê agora é um garoto.

\- Função: pula o tempo morto; reaproveita o fato do beat 2 como piada visual.

\- Emoção: alívio cômico.

\- Preservar: o salto marcado e a piada do crescimento.

\- Trocar: o cartão (você recusou o de marca, ver 5.1).



**\*\*BEAT 4: Despedida (0:12–0:15)\*\***

\- Evento: a mãe diz "be safe out there", o garoto responde "Yes, ma", sai voando.

\- Função: laço mãe-filho; o herói obediente indo para o perigo.

\- Emoção: ternura.

\- Preservar: um gesto afetivo curto antes de a história endurecer.

\- Trocar: tudo o mais.



**\*\*BEAT 5: Aula (0:16–0:19)\*\***

\- Evento: a professora mostra que humanos "big backs" são alvo ideal.

\- Função: normaliza o ato violento como currículo.

\- Emoção: humor sombrio.

\- Pergunta: o herói vai aceitar isso?

\- Preservar: a instituição que trata o dano como matéria escolar.

\- Trocar: o alvo ideal.



**\*\*BEAT 6: A dúvida (0:20–0:31)\*\***

\- Evento: em casa o herói diz que não nasceu pra isso; a mãe: "prove o primeiro sangue, depois decida".

\- Função: conflito moral e mentora que empurra sem forçar.

\- Emoção: empatia.

\- Pergunta: ele vai provar?

\- Preservar: a dúvida em voz alta, e a resposta "faça e depois decida".

\- Trocar: o ato.



**\*\*BEAT 7: Autoridade (0:32–0:37)\*\***

\- Evento: o sargento grita "hoje transformamos vocês em monstros de verdade".

\- Função: escalada e tom militar exagerado.

\- Emoção: tensão cômica.

\- Preservar: o instrutor caricato e a frase de "monstro".

\- Trocar: o cenário.



**\*\*BEAT 8: O colega (0:38–0:42)\*\***

\- Evento: Reggie se apresenta; o herói diz "ainda não sei, depois de hoje eu sei".

\- Função: criar um colega simpático em segundos para a morte doer; espelha a dúvida do herói.

\- Emoção: afeto.

\- Preservar: apresentação rápida e confiante do colega, e a frase de dúvida do herói.

\- Trocar: o nome, a mania do colega.



**\*\*BEAT 9: A ordem irônica (0:43–0:47)\*\***

\- Evento: "pouse gentilmente nesse humano; drene sangue do dobro do seu tamanho".

\- Função: preparação da piada ("gentilmente" × morte) e do excesso ("dobro").

\- Emoção: suspense.

\- Preservar: uma ordem com palavra irônica e um excesso.

\- Trocar: o conteúdo da ordem.



**\*\*BEAT 10: Pausa (0:48–0:50)\*\***

\- Evento: macro do colega na pele do humano; quase silêncio.

\- Função: respiro antes do choque; contraste de escala.

\- Emoção: dread e segurança juntos.

\- Preservar: uma pausa quieta imediatamente antes da virada.



**\*\*BEAT 11: Morte fora de quadro (0:52–0:55)\*\***

\- Evento: corte seco para os dois gritando; o tapa nunca é mostrado.

\- Função: choque cômico-violento; o herói foge.

\- Emoção: pânico.

\- Preservar: violência por efeito, não por imagem.

\- Trocar: o meio (tapa → chinelada).



**\*\*BEAT 12: Refúgio e promessa (0:57–1:05)\*\***

\- Evento: o herói chora; a mãe: "você tem que sugar sangue... vou mostrar um jeito mais ético sem morrer".

\- Função: fundo emocional e virada; o mentor reformula o dilema; abre loop.

\- Emoção: tristeza→esperança.

\- Pergunta: que jeito é esse?

\- Preservar: o dilema "é o que somos" + a promessa de um jeito de sobreviver.



**\*\*BEAT 13: Setup do demonstrar (1:06–1:09)\*\***

\- Evento: a mãe e o filho numa folha, vendo uma família jantar; "me observe e aprenda".

\- Função: ligar a promessa a um alvo concreto.

\- Preservar: o alvo concreto e o "aprenda".



**\*\*BEAT 14: Cliffhanger (1:10–1:14)\*\***

\- Evento: a família ri; um mosquito pousa no pulso do avô; corta.

\- Função: payoff escondido.

\- Preservar: terminar antes de mostrar o jeito "ético".



**\*\*Parte 2 do original (8 beats, resumido)\*\*** [EVIDÊNCIA: \`analise_parte2.md\`]: hook = herói chora sobre a mãe morta e jura vingança; pedido de treino ao mentor; fofoca no bar mostrando a mudança; crueldade com a esposa grávida; aviso do mentor; oficina com equipamento; discurso de multidão; ataque ao pé do humano e morte.



\---



**# 3. O QUE DECIDIMOS PRESERVAR**



\| Elemento preservado | Por quê | Evidência |

\|---|---|---|

\| **\*\*Hook de perda\*\*** | É o gancho do original e você pediu o "mesmo enredo" | Você: "eu quero, sinceramente, copiar a história... o mesmo enredo, só que com outro inseto". Roteiro v2, cena 1 |

\| **\*\*Ordem dos eventos\*\*** | Pedido de cópia fiel; eu disse "o original já era linear" | Conversa; v2 mantém a ordem das 14 cenas |

\| **\*\*Mentor (mãe) e autoridade (sargento)\*\*** | São as funções que empurram o herói | \`historia.md\`, personagens |

\| **\*\*Colega descartável\*\*** | Existe para a morte doer | Você escolheu o Rocco entre 4 opções ("1-colega descartável quero o Rocco") |

\| **\*\*Treinamento/Academia\*\*** | É o "mundo que normaliza o ato" | Você definiu "academia" como o cenário na primeira mensagem do pedido |

\| **\*\*Regra moral que abre loop\*\*** | É o cliffhanger | Você: "2-perfeito" (a regra estruturada por episódio) |

\| **\*\*Morte fora de quadro\*\*** | É o choque cômico do original | v2 cabeçalho: "Violência nunca aparece em quadro" |

\| **\*\*Salto de tempo marcado\*\*** | Reaproveita o prazo do beat 2 | Você: "3 noites depois"; v2: "3 DIAS DEPOIS" |

\| **\*\*Cliffhanger sem payoff\*\*** | É a retenção | v2 cena 14 termina no clique e na luz acendendo |

\| **\*\*Escalada ("monstro de verdade")\*\*** | Está nas falas do sargento original | v2 cena 7 |

\| **\*\*Pausa silenciosa antes da piada\*\*** | Cria o contraste | v2 cena 10 sem fala |



[INFERÊNCIA] O que mais pesou na decisão de preservar foi a sua instrução de copiar a história. As razões narrativas (função de cada beat) eu expliquei, mas nunca foram debatidas por você.



\---



**# 4. O QUE DECIDIMOS TROCAR (e a lógica de cada troca)**



\| Original | Nossa versão | Lógica da troca |

\|---|---|---|

\| Mosquito | **\*\*Barata\*\*** | Variável que você escolheu ("quero usar barata"). Funciona porque a barata também é um inseto mal visto que invade casas |

\| Sangue | **\*\*Comida roubada\*\*** (migalhas, pizza) | O mosquito "rouba" o que precisa do humano; a barata faz o mesmo com comida. [INFERÊNCIA] mantém a função "o ato que a espécie pratica e o herói rejeita" |

\| Hospital humano | **\*\*Maternidade na parede, atrás da geladeira\*\*** | Você exigiu um ambiente nativo da espécie ("o mosquito não está dando luz no hospital"). Mantém a função "lugar da perda e da vulnerabilidade" |

\| Pântano, árvore, jardim | **\*\*Vãos de parede, embaixo da pia, rodapé, cozinha\*\*** | O mosquito vive na natureza; a barata vive dentro da casa humana |

\| Aula sobre humano "big back" | **\*\*Aula embaixo da pia sobre o humano bagunceiro\*\*** | O alvo ideal da barata é a cozinha suja |

\| Reggie / "pouse gentilmente" | **\*\*Rocco / "entra de mansinho"\*\*** | A ironia se mantém ("nada nos para" × chinelada) |

\| Mordida e **\*\*tapa\*\*** | Pega a pizza e **\*\*chinelada\*\*** | O chinelo é o "tapa" brasileiro doméstico. [INFERÊNCIA] é a troca com mais sabor local |

\| "Machos vivem 2 semanas" | **\*\*"Barata cresce rápido"\*\*** | Preserva a função "regra do mundo que justifica o salto de tempo" |

\| "Jeito ético de sugar" | **\*\*Regra 1: só come o que cai no chão, nunca do prato, nunca com a luz acesa\*\*** | Regra concreta que cabe na barata e é visual |

\| Cartão @fruitheatre em 0:11 | **\*\*Texto "3 DIAS DEPOIS" + clique do interruptor\*\*** | Você recusou o cartão de marca. O clique do interruptor substituiu os fades para preto [EVIDÊNCIA: minha tabela de variáveis; sua aceitação] |

\| Mosquito pousa no pulso do avô | **\*\*A luz acende, fim\*\*** | A barata equivalente é o interruptor; a luz acesa é o perigo |

\| Família no churrasco | **\*\*O homem sozinho comendo pizza na cozinha\*\*** | Mantém o "mesmo alvo humano" como callback. Você aprovou o callback ("3-sim") |

\| Humano gordo/magro no quadro | **\*\*Humano bagunceiro vs arrumado\*\*** | O alvo ideal da barata |



\---



**# 5. TODAS AS IDEIAS QUE MUDARAM NO CAMINHO**



Formato: IDEIA ORIGINAL → PROBLEMA → SEU FEEDBACK → NOVA DECISÃO → POR QUE FICOU MELHOR.



**### 5.1 Cartão "Fruitheatre"**

\- Ideia: manter o cartão de marca como transição.

\- Problema: era a marca de outro canal.

\- Feedback: "não quero nada de cartão Fruitheatre." [EVIDÊNCIA]

\- Decisão: só texto "3 noites depois" + clique do interruptor.

\- Melhor porque: a transição passa a ser parte do mundo (a luz).



**### 5.2 Palavra-gancho "sio" → "sió" → "cria" → removida**

\- Ideia: eu inventei "sio" e coloquei em todas as frases.

\- Problema: eu não consegui verificar que era uma gíria real; você: "o sió ficou paia" [EVIDÊNCIA].

\- Feedback: "uma palavra gancho... gíria".

\- Decisão intermediária: **\*\*"cria"\*\***, "fazendo sentido no contexto" [EVIDÊNCIA].

\- Depois: você removeu "cria" de vez ("nunca a palavra cria") [EVIDÊNCIA: memória \`baratas-formato-das-falas\`].

\- Melhor porque: a fala fica natural; eu parei de forçar um bordão.



**### 5.3 "Uma regra por parte" (arco inventado)**

\- Ideia: Parte 2 = Regra 2; Parte 3 = Regra 3; o homem poupa o herói [EVIDÊNCIA: proposta salva em \`historia.md\` v1].

\- Problema: eu **\*\*não tinha visto\*\*** as Partes 2 e 3.

\- Evento: você enviou a Parte 2; eu a analisei: era **\*\*vingança\*\***, mãe morta, herói vira monstro e morre.

\- Decisão: apagar o arco de regras e copiar o de vingança, com dois episódios.

\- Melhor porque: deixou de ser invenção e passou a seguir a fonte.



**### 5.4 "Barata não mata humano"**

\- Ideia: manter "sugar sangue → terror".

\- Problema: o ato violento do original não funcionava para a barata.

\- Feedback: você: "Barata não mata humano" [EVIDÊNCIA].

\- Decisão: o terror do herói vira **\*\*assustar\*\*** (voar na cara, pousar no prato), o mal humano é o dedetizador e a chinelada.

\- Melhor porque: cada lado tem um dano plausível.



**### 5.5 ooteca / ninfa / casca → "algo humano"**

\- Ideia: eu usei "ooteca", "ninfa", "muda de casca" para dar sabor de barata.

\- Problema: virava aula de biologia.

\- Feedback: "não vou falar de ooteca... tem que ser algo humano" [EVIDÊNCIA].

\- Decisão: "bebê", "esposa grávida", "escola"; biologia só no cenário.

\- Melhor porque: o drama é humano e universal.



**### 5.6 O ambiente da maternidade (3 versões)**

\- 1: "atrás da geladeira", em miniatura → gerou imagem **\*\*escura e granulada\*\*** [EVIDÊNCIA: sua reclamação "não gostei, diferente do vídeo"].

\- 2: hospital claro (copiando a referência) → barata virou **\*\*mascote fofo\*\*** [EVIDÊNCIA: "tudo tá parecendo personagem... tem que ser bizarro"].

\- 3: você: "barata dando luz dentro de hospital não faz sentido" → ambiente nativo da barata, mas **\*\*limpo\*\***: vila em miniatura dentro da casa.

\- Melhor porque: o mundo é da espécie e a imagem continua charmosa.

\- Observação: [EVIDÊNCIA] o original **\*\*tem\*\*** um hospital humano (Parte 1), então a sua crítica foi sobre a lógica da espécie, não uma cópia fiel.



**### 5.7 Visual da barata (realista → mascote → semi-estilizado)**

\- Esses três passos afetaram a história indiretamente (o tom "bizarro mas expressivo"). Detalhe em \`\_licoes-prompts-de-imagem.md\`.



**### 5.8 Nome "Cuco" → "Rochito"**

\- Problema: "Cuco" lembrava "Coco" (você: "não quero que seja coco").

\- Decisão: algo de barata, que funcione em inglês e português, na lógica de "Bobito". Opções: Rochito, Baratito, Blattito, Roachy. Você: "nome é Rochito" [EVIDÊNCIA].



**### 5.9 Número de episódios: 3 → 2**

\- Você: "vamos fazer dois episódios" [EVIDÊNCIA].



**### 5.10 Falas: curtas → longas, com palavrão, sem "cria", sem ponto final**

\- Eram frases curtas e leves. Você pediu palavrão pesado e frases corridas [EVIDÊNCIA: memórias \`baratas-palavrao-liberado\`, \`baratas-formato-das-falas\`].

\- O roteiro v2 passou a ter 20 falas, de 8 a 39 palavras (média 27; 13 das 20 têm 28 palavras ou mais). [EVIDÊNCIA: contagem do arquivo]

\- **\*\*Isso é a maior causa da duração, ver seção 12.\*\***



**### 5.11 "3 noites" → "3 DIAS DEPOIS"**

\- O v2 usa "dias"; \`historia.md\` e o roteiro antigo ainda dizem "noites". [EVIDÊNCIA: v2 "Pontos para você decidir"]



**### 5.12 "Jeito ético" → "jeito de comer sem morrer"**

\- No v2 a palavra "ético" some (cena 12). [EVIDÊNCIA: texto do v2]. [INFERÊNCIA] ficou mais coloquial.



**### 5.13 Um prompt por cena × divisão em A/B**

\- Você disse "1 cena, 1 prompt"; os arquivos têm 01A/B, 04A/B, 06A/B, 11A/B porque a fala passa de \~26 palavras. [EVIDÊNCIA: \`\_sistema-image-to-video.md\` aponta a contradição.]



**### 5.14 Callback do homem**

\- Proposto por mim ("o mesmo homem que matou o Rocco"); você aprovou ("3-sim"). Aparece nas cenas 13 e 14 do v2. [EVIDÊNCIA]



\---



**# 6. COMO MODELAMOS PARA O BRASIL**



**## ADAPTAÇÃO LITERAL (só troca de palavras)**

\- "I'm sorry, they all died" → "Sinto muito... o dedetizador passou o rodo em todo mundo" (a parte do dedetizador já é localização).

\- Mãe preocupada, filho obediente, aula, sargento berrando: mantidos do original.



**## LOCALIZAÇÃO REAL (onde a história ficou brasileira)**

\| Item | O que fizemos | Evidência |

\|---|---|---|

\| **\*\*Chinelada\*\*** | O tapa vira a chinelada, a arma doméstica brasileira. Chinelo vermelho | v2 cena 11 e 14 |

\| **\*\*Dedetizador\*\*** | A causa da perda é um agente humano reconhecível ("passou o rodo em todo mundo") | v2 cena 1 |

\| **\*\*Casa brasileira\*\*** | Geladeira, pia, rodapé, sofá, pizza | \`historia.md\` |

\| **\*\*Linguagem\*\*** | PT-BR de rua, "tu", "moleque", "meu filho", "rango", "merda", "caralho", "porra" | v2 |

\| **\*\*Palavrão\*\*** | Pesado e com sentido, pedido por você | memória \`baratas-palavrao-liberado\` |

\| **\*\*Relação mãe-filho\*\*** | Mãe que diz "não vai fazer nenhuma merda" e filho que responde "não pega no meu pé" | v2 cena 4 |

\| **\*\*Humor\*\*** | Ironia ("barata vive uma semana sem cabeça, nada nos para") mantida do original, mas dita com gíria | v2 cena 8 |

\| **\*\*Ritmo de fala\*\*** | Frases longas e corridas, ritmo de conversa real | memória \`baratas-formato-das-falas\` |



[INFERÊNCIA] A localização **\*\*mais forte veio de você reescrevendo as cenas 1 e 2\*\*** (memória diz que você as reescreveu como modelo), e não da minha primeira versão (onde o "toque local" foi o "sio", que não funcionou). Eu também ofereci "barata voa" (gíria real) como bordão; não entrou no roteiro. [EVIDÊNCIA: não aparece no v2]



\---



**# 7. COMO CRIAMOS OS PERSONAGENS (função narrativa)**



\| Personagem | Equivalente no original | Função | Personalidade criada | Papel na progressão | Mudanças no caminho |

\|---|---|---|---|---|---|

\| **\*\*Rochito\*\*** | Bobito | Herói que duvida e depois se corrompe | Gentil, de paz, obediente (Ep 1); vingativo e cruel (Ep 2, planejado) | Ele é o motor: dúvida → choque → vingança | Nome: Cuco → Rochito. v2 dá a ele mais fala de resistência ("não sou mais um bebê") |

\| **\*\*Dona Blatta\*\*** | Mãe-mosquito (Ms. Mosquitos) | Mentora que empurra e promete o jeito de sobreviver; morre (Ep 2, planejado) | Protetora, pragmática, firme. No v2 grita no hospital | Linka a perda (cena 1) e a regra (cena 14) | v2 deixa a mãe mais agressiva na cena 1 e mais dura em "não vai fazer merda" |

\| **\*\*Rocco\*\*** | Reggie | Colega descartável | Confiante, "imortal" | Faz a morte doer | Você escolheu entre 4 opções; v2 mantém a mania de "semana sem cabeça" |

\| **\*\*Doutor Antenor\*\*** | Médico do hospital | Entrega a perda e a regra do mundo | Calmo, triste, formal ("senhora") | Só no início | v2 amplia a fala dele (exposição mais longa) |

\| **\*\*Sargento Carapaça\*\*** | Sargento / "Major" | Autoridade caricata; no Ep 2 tenta frear o herói | Berrante, teatral | Escalada e ordem irônica | Nome é meu; "Major" do original vira o mesmo personagem |

\| **\*\*Prof. Quitina\*\*** | Professora | Normaliza o ato | Seca, severa; v2 dá palavrão a ela | Uma cena | Papel pequeno |

\| **\*\*Homem (humano)\*\*** | Humano deitado / família | O alvo e o perigo; o callback | Não é vilão, só um humano | Mata o Rocco e reaparece | Camiseta amarela manchada e chinelo vermelho [EVIDÊNCIA: \`historia.md\`] |

\| **\*\*Esposa do Rochito\*\*** (Ep 2) | Esposa-mosquito grávida | Mostra o que o herói perdeu | Preocupada; nome indefinido | Gancho final | Só planejada |

\| **\*\*Engenheiro\*\*** (Ep 2) | Mosquito engenheiro | Upgrade | Inventor entusiasmado | Escalada | Só planejado |

\| **\*\*Cadetes, alunos\*\*** | Recrutas e alunos do original | Coro | Anônimos | Escala o grupo | Figurantes; geraram problemas visuais (clonagem) [EVIDÊNCIA: \`\_licoes...\`] |



[INFERÊNCIA] Os personagens nasceram por **\*\*função do original → nome e traço novo\*\***, e só depois ganharam personalidade pelas falas do v2. Eu não debati a personalidade deles com você antes.



\---



**# 8. COMO CRIAMOS O MUNDO**



\| Regra do mundo | Nasceu de | Quando | Evidência |

\|---|---|---|---|

\| Baratas vivem **\*\*dentro da casa humana\*\*** | Sua crítica ao hospital | Depois das primeiras imagens | Conversa: "o mosquito não está dando luz no hospital" |

\| Vila **\*\*limpa e charmosa\*\*** de objetos domésticos | Correção do visual granulado | Idem | \`historia.md\` regra 2 |

\| **\*\*Escala:\*\*** barata minúscula, humano gigante | Necessidade do cliffhanger e do chinelo | Desde a proposta | \`historia.md\` |

\| **\*\*Dedetizador\*\*** como mal | Hook (a causa da perda) | Primeira versão | Conversa e v2 |

\| **\*\*Luz\*\*** como perigo (luz acesa = perigo) | Substituto dos fades para preto | Primeira proposta de transição | Minha tabela de variáveis; aceita |

\| **\*\*Chinelo\*\*** como arma | Substituto do tapa | Primeira versão | v2 cena 11 |

\| **\*\*Escola/academia\*\*** | Original | Desde o começo | — |

\| **\*\*Família\*\*** (mãe e filho, esposa grávida) | Original | — | — |

\| **\*\*Comida:\*\*** migalhas, "só o que cai" | Regra 1 | Proposta da regra | v2 cena 14 |

\| **\*\*"Barata cresce rápido"\*\*** | Substitui "machos vivem 2 semanas" | Primeira versão | v2 cena 2 |

\| **\*\*Barata não mata humano\*\*** | Sua correção | Ao copiar a Parte 2 | \`historia.md\` regra 3 |



**\*\*Nasceram da história:\*\*** escola, mentor, perda, dedetizador, chinelo, luz, Regra 1.

**\*\*Adicionadas depois (por correção):\*\*** casa como mundo, vila limpa, humano como gigante estilizado, "barata não mata humano", "história humana" (sem ooteca).



\---



**# 9. COMO TRANSFORMAMOS A ESTRUTURA EM UMA HISTÓRIA NOVA**



**\*\*Hipótese de operação mental que você descreveu:\*\***

1\. identificar função do beat → 2. ignorar a superfície → 3. escolher equivalente → 4. verificar a emoção → 5. adaptar ao Brasil → 6. conectar causalmente → 7. escrever diálogo.



**\*\*O que realmente aconteceu [INFERÊNCIA a partir do histórico]:\*\***

1\. **\*\*Análise\*\*** da fonte (frames, transcrição) com **\*\*sequência e funções em prosa\*\*** (passo 1 feito, mas informal).

2\. **\*\*Brainstorm de 3 variáveis\*\*** que você pediu (colega, regra, marca de transição). Não foi um mapeamento beat a beat.

3\. **\*\*Tabela original → nossa\*\*** (superfície por superfície) + **\*\*esboço de 12 beats\*\***.

4\. **\*\*Texto das 14 cenas\*\***, com falas inventadas por mim (e o bordão "sio").

5\. **\*\*Rodadas de correção\*\*** pela sua reação (ambiente, humano, "barata não mata humano", nome, fala).

6\. **\*\*Segunda fonte (Parte 2)\*\*** mudou o arco para vingança.

7\. **\*\*Você reescreveu o diálogo\*\*** (v2) em PT-BR de rua, longo e com palavrão.



**\*\*Veredito:\*\*** o processo real foi **\*\*"preservar a sequência, trocar a superfície e corrigir por feedback"\*\***, e não "função primeiro". Os passos 4 (verificar a emoção) e 6 (conectar causalmente) **\*\*não foram feitos de forma explícita\*\***; aconteceram por acaso ou pela sua revisão. A localização (passo 5) veio **\*\*tarde\*\***, depois do "sio", e foi sobretudo trabalho seu.



**\*\*Processo correto reconstruído:\*\*** ver seção 13.



\---



**# 10. O QUE FUNCIONOU MELHOR**



\| Decisão | Motivo | Evidência no histórico | Impacto |

\|---|---|---|---|

\| **\*\*Rocco como colega\*\*** | Ironia "nada nos para" × chinelada | Você escolheu em primeira ordem; v2 mantém e até estende a fala | O choque funciona; vira o motor do Ep 2 |

\| **\*\*Regra 1 (só o que cai, nunca com a luz acesa)\*\*** | Regra concreta, visual e curta | Você: "perfeito"; ela está no cliffhanger do v2 | Dá o loop e liga com a luz |

\| **\*\*Chinelada fora de quadro + capacete rolando\*\*** | Violência por efeito | v2 cabeçalho e cenas 11, 14; bloqueios de moderação em tentativas com chinelo levantado [EVIDÊNCIA: \`\_licoes...\` F9] | Mantém o humor sombrio e passa pelo filtro |

\| **\*\*Luz acendendo no final\*\*** | Substitui o mosquito no pulso | v2 cena 14 | Cliffhanger visual |

\| **\*\*Vila doméstica\*\*** | Resolve "a barata no hospital" | Você pediu; \`historia.md\` | O mundo faz sentido |

\| **\*\*Relação mãe/filho\*\*** | Mantida e aprofundada | v2 cenas 4, 6, 12 (as falas mais longas e específicas) | É o coração emocional |

\| **\*\*Callback do homem\*\*** | Dá motivo para a vingança do Ep 2 | Você: "3-sim"; v2 cenas 13 e 14 | Amarra os dois episódios |

\| **\*\*Treinamento adaptado (aula embaixo da pia)\*\*** | Cenário nativo | Cena 5: o ambiente nunca foi questionado [EVIDÊNCIA: \`\_licoes...\` seção 1] | Funciona sem esforço |



**\*\*Cuidado:\*\*** só considerei "funcionou" o que você escolheu, elogiou ou manteve ao reescrever. Itens como "dedetizador" e "luz como perigo" nunca foram contestados, mas também nunca elogiados: ficam como [INFERÊNCIA].



\---



**# 11. O QUE NÃO FUNCIONOU**



**\*\*PROBLEMA: arco "uma regra por parte"\*\***

→ POR QUE NÃO FUNCIONAVA: foi inventado sem ter visto as Partes 2 e 3 do original, e o original era outra coisa (vingança).

→ COMO CORRIGIMOS: analisei a Parte 2 e reescrevi o plano.

→ REGRA FUTURA: analisar todas as partes da fonte antes de projetar o arco.



**\*\*PROBLEMA: palavra-gancho inventada ("sio")\*\***

→ POR QUE: eu não consegui provar que era uma gíria real; soou forçada.

→ CORREÇÃO: opções de gírias reais; "cria"; depois removida.

→ REGRA: nunca inventar gíria; usar o léxico que o usuário fornece e testar em voz.



**\*\*PROBLEMA: jargão de biologia (ooteca, ninfa, casca)\*\***

→ POR QUE: transformava drama em aula de zoologia.

→ CORREÇÃO: linguagem humana (bebê, grávida).

→ REGRA: a linguagem da história é humana; biologia só aparece no cenário.



**\*\*PROBLEMA: adaptação literal de "sugar sangue"\*\***

→ POR QUE: o ato era inviável para a barata (não mata humano).

→ CORREÇÃO: terror = assustar.

→ REGRA: traduzir o verbo do dano por um equivalente plausível da espécie, não copiar o ato.



**\*\*PROBLEMA: ambiente genérico ou errado (hospital, miniatura suja)\*\***

→ POR QUE: o primeiro gerou imagem granulada, o segundo, mascote humano em cenário humano.

→ CORREÇÃO: vila doméstica limpa.

→ REGRA: o mundo precisa ser nativo da espécie, mas com direção "limpo e charmoso".



**\*\*PROBLEMA: nome parecido com um IP conhecido ("Cuco" ≈ "Coco")\*\***

→ POR QUE: risco de confusão e de filtro.

→ CORREÇÃO: Rochito.

→ REGRA: checar nomes contra IPs conhecidos.



**\*\*PROBLEMA: roteiro longo demais\*\***

→ POR QUE: falas de \~27 palavras em média (13 das 20 com 28 ou mais), cenas de 8 s fixos (ver seção 12).

→ CORREÇÃO: dividir cenas em A/B; contradiz "1 cena = 1 prompt".

→ REGRA: orçamento de palavras por cena antes de escrever.



**\*\*PROBLEMA: documentos fora de sincronia\*\***

→ POR QUE: \`historia.md\` ainda diz "cria", "noites", "nome a definir"; o roteiro v2 já mudou.

→ REGRA: uma fonte da verdade; atualizar \`historia.md\` quando o roteiro muda.



**\*\*PROBLEMA: conhecimento perdido\*\***

→ POR QUE: frames e transcrições apagados; a análise da Parte 1 não foi salva.

→ REGRA: salvar a análise da fonte (beats, falas, tempos) antes de apagar o material.



**\*\*PROBLEMA: afirmei duas vezes que um arquivo estava salvo sem estar\*\*** (\`\_prompt-folha-personagem\` e \`\_prompt-prompts-de-cena\`)

→ POR QUE: falha de verificação minha.

→ REGRA: conferir a existência do arquivo antes de dizer que está salvo.



**\*\*PROBLEMA: regras conflitantes entre documentos\*\***

→ POR QUE: o documento mestre pede falas de 12 palavras; o v2 usa \~27; o sistema de vídeo adotou um limite empírico de \~26 palavras em 8 s.

→ REGRA: decidir qual regra manda e registrar.



\---



**# 12. ANÁLISE DA DURAÇÃO (onde cresceu)**



**\*\*Pergunta:\*\*** o vídeo ficou com cerca de 2 minutos [EVIDÊNCIA: sua mensagem]. O original tinha 73,8 s.



**## 12.1 Números**

\| Medida | Original (Parte 1) | Nossa versão | Fonte |

\|---|---|---|---|

\| Duração | 73,8 s | **\*\*134 s (2:14)\*\*** soma das \`duration_seconds\` dos 18 clipes | [EVIDÊNCIA] transcrição; JSONs de vídeo |

\| Palavras faladas | 251 | **\*\*540\*\*** (2,15×) | [EVIDÊNCIA] contagem |

\| Ritmo de fala | 3,40 pal/s | \~3,75 pal/s por clipe de 8 s | [EVIDÊNCIA] cálculo |

\| Frases/falas | 41 frases | 20 falas | [EVIDÊNCIA] |

\| Palavras por frase/fala | **\*\*6,1\*\*** (maior frase: 18) | **\*\*27\*\*** | [EVIDÊNCIA] |

\| Cenas (beats) | 14 | 14 | [EVIDÊNCIA] |

\| Clipes | ≈14 blocos | **\*\*18\*\*** | [EVIDÊNCIA] |



**\*\*Se as nossas 540 palavras fossem faladas no ritmo do original (3,4 pal/s), dariam 159 s.\*\*** [EVIDÊNCIA: cálculo]



**## 12.2 Duração por cena (planejada na conversa × realizada)**

\| Cena | Original (≈, ±1 s) | Planejado por mim | Clipes realizados | Palavras (v2) |

\|---|---|---|---|---|

\| 1 | 5 s | 5 s | 13 s (8+5) | 37 |

\| 2 | 6 s | 6 s | 8 s | 38 |

\| 3 | 2 s | 2 s | 4 s | 0 |

\| 4 | 3 s | 3 s | **\*\*16 s (8+8)\*\*** | 63 |

\| 5 | 5 s | 5 s | 8 s | 36 |

\| 6 | 11 s | 11 s | 16 s (8+8) | 62 |

\| 7 | 6 s | 6 s | 8 s | 52 |

\| 8 | 6 s | 6 s | 8 s | 60 |

\| 9 | 5 s | 5 s | 8 s | 28 |

\| 10 | 3 s | 3 s | 5 s | 0 |

\| 11 | 4 s | 4 s | **\*\*16 s (8+8)\*\*** | 49 |

\| 12 | 8 s | 8 s | 8 s | 63 |

\| 13 | 3 s | 3 s | 8 s | 24 |

\| 14 | 4 s | 4 s | 8 s | 28 |

\| **\*\*Total\*\*** | **\*\*≈71 s\*\*** | **\*\*≈71 s\*\*** | **\*\*134 s\*\*** | **\*\*540\*\*** |



[EVIDÊNCIA: planejado = minha tabela de duração na conversa; realizado = JSONs de vídeo; original = minha análise.]



**## 12.3 Onde a duração cresceu**

Em ordem de impacto [INFERÊNCIA a partir dos números]:

1\. **\*\*Comprimento das falas.\*\*** O original falava em frases de \~6 palavras; o v2 em falas de \~27. Cada fala virou um mini-monólogo. Isso é a **\*\*decisão de você\*\*** (memória: "frases bem longas e corridas").

2\. **\*\*Unidade mínima de 8 s por clipe.\*\*** Uma cena de 3 s no original (cenas 4, 13) virou 8 s ou 16 s.

3\. **\*\*Divisão por limite de palavras.\*\*** As cenas 1, 4, 6 e 11 viraram dois clipes cada (+4 clipes). [EVIDÊNCIA: nomes dos arquivos e \`\_sistema-image-to-video.md\`]

4\. **\*\*Dois falantes em cenas que no original tinham uma ou duas linhas.\*\*** Cena 4: no original eram \~6 palavras ("be safe out there / yes ma"); no v2, 63.

5\. **\*\*Exposição repetida.\*\*** Cena 1 e cena 2 contam a mesma ideia (perda, "só sobrou esse", "leve esse moleque à Academia", "cuide bem desse moleque"); no original eram 11 s juntas, no v2 são 21 s.

6\. **\*\*Reação.\*\*** A cena 11 (pânico) virou 16 s com duas falas (o herói e o humano), e no original eram \~4 s de grito.



**## 12.4 O que \*\*não\*\* explica o aumento**

\- **\*\*Número de beats:\*\*** igual (14).

\- **\*\*Número de personagens:\*\*** parecido com o original.

\- **\*\*Ritmo de fala:\*\*** parecido (3,4 vs \~3,75 pal/s).



**## 12.5 O que poderia ser fundido ou cortado [INFERÊNCIA]**

\- Cenas 1 e 2 (a perda e o prazo) num só momento.

\- Cena 4 (portinha) reduzida ao gesto afetivo, como no original.

\- Cenas 7, 8 e 9 (sargento, Rocco, ordem) condensadas, já que cada uma tem 28 a 60 palavras.

\- Cenas 13 e 14 (setup e regra) numa só.

\- A cena 11 sem a fala do humano.



Não reescrevi o roteiro, como você pediu.



\---



**# 13. REFERENCE STORY MODELING SYSTEM**



**\*\*ENTRADA:\*\*** vídeo(s) de referência, frames, transcrição, e o universo/variável novo escolhido pelo usuário.



**\*\*PROCESSO\*\***

1\. **\*\*Entender a história literal.\*\*** Assistir a todas as partes da fonte antes de projetar qualquer arco (falha 5.3). Guardar frames e transcrição até a adaptação ser validada (falha: material apagado).

2\. **\*\*Extrair os beats\*\*** com timestamps. Salvar a análise em arquivo.

3\. **\*\*Extrair a função de cada beat:\*\*** evento literal, função narrativa, emoção, pergunta aberta, o que preservar, o que trocar (modelo da seção 2).

4\. **\*\*Identificar o DNA narrativo:\*\*** a sequência de funções, os tipos de gancho, a regra moral, o tipo de morte, o tipo de final, a razão de cada beat prender atenção.

5\. **\*\*Escolher o novo universo\*\*** e descrever as regras do mundo nativas da espécie ou do tema.

6\. **\*\*Mapear equivalentes\*\*** por função (tabela da seção 14), nunca por superfície.

7\. **\*\*Adaptar ao Brasil:\*\*** objetos, hábitos, comida, relações, linguagem; usar o léxico do usuário e verificar gírias reais.

8\. **\*\*Testar a lógica causal:\*\*** cada beat precisa nascer do anterior no novo universo; o "ato" do original precisa ter equivalente plausível na espécie nova.

9\. **\*\*Criar personagens funcionais:\*\*** cada um nasce de uma função do original; depois ganha traço próprio.

10\. **\*\*Escrever o diálogo\*\*** com o orçamento de palavras já definido por cena.

11\. **\*\*Comprimir:\*\*** funde beats redundantes, corta exposição repetida, mede palavras por frase.

12\. **\*\*Validar a duração\*\*** antes de gerar qualquer imagem ou vídeo: palavras ÷ ritmo do original, comparada à duração da fonte.



**\*\*SAÍDA:\*\*** história modelada; lista de beats com função; personagens com função; diálogo; duração estimada; arquivo único de verdade (\`historia.md\`) sincronizado com o roteiro.



\---



**# 14. TABELA DE MAPEAMENTO**



\| ORIGINAL | FUNÇÃO | NOSSA VERSÃO | POR QUE FUNCIONA |

\|---|---|---|---|

\| Hospital, mãe de camisola e médico | Apresentar a perda e a vulnerabilidade | Maternidade na parede atrás da geladeira | Preserva o impacto emocional e muda o mundo para o da barata |

\| "Só este menino sobreviveu" | Definir o protagonista pela perda | "Só sobrou esse aqui" | Mesmo estímulo de pena e esperança |

\| Médico entrega o prazo ("Academia em 3 dias") | Exposição + prazo | Doutor: "leve o moleque em três dias" | Prazo em diálogo emocional |

\| "Machos vivem 2 semanas" | Regra do mundo que justifica o salto | "Barata cresce rápido" | Mesma função sem copiar a biologia |

\| Cartão "3 days later" | Salto marcado | Texto "3 DIAS DEPOIS" | O salto continua; a marca de outro canal sai |

\| Casa/porta, "be safe out there" | Laço mãe-filho antes do perigo | Portinha do rodapé; "fica no escuro lá fora" | Afeto + perigo do mundo (o escuro) |

\| Aula: humano gordo é o alvo | Normalizar o dano como currículo | Aula embaixo da pia: humano bagunceiro | Alvo coerente com a barata |

\| Casa na árvore: "prove e depois decida" | Conflito moral + mentora | Casa na parede: "prova a migalha e depois decide" | Mantém a frase-chave |

\| Sargento: "monstros de verdade" | Autoridade caricata e escalada | Sargento Carapaça | Mantém o tom |

\| Reggie "I'm Reggie" | Colega simpático | Rocco "nada nos para" | Cria afeto e ironia |

\| "Pouse gentilmente, o dobro do tamanho" | Ordem irônica | "Entra de mansinho, comida do dobro do teu tamanho" | Mantém o paradoxo |

\| Macro do mosquito no braço | Pausa de suspense | Close da pizza, silêncio | Mesmo respiro antes do choque |

\| Tapa fora de quadro | Choque cômico | Chinelada fora de quadro + capacete rolando | Chinelo é o "tapa" brasileiro |

\| "Ethical way" + mãe | Promessa que abre loop | "Regra 1" + mãe | Regra concreta e visual |

\| Mosquito pousa no pulso do avô | Cliffhanger | Luz acende, clique do interruptor | Perigo + payoff escondido |

\| *\*(Parte 2)\** mãe morta, hook | Hook da vingança | Rochito sobre a mãe imóvel (planejado) | Preserva o choque inicial |

\| *\*(Parte 2)\** "terrorizar e sugar sangue" | O ato corruptor | "Assustar" (planejado) | Barata não mata humano |

\| *\*(Parte 2)\** motor mais alto | Upgrade da vingança | Exo-pernas + chiado mais alto (planejado) | Equivalente plausível |

\| *\*(Parte 2)\** ataque à perna e tapa | Final trágico | Pé do homem e chinelada (planejado) | Fecha o arco |



\---



**# 15. REGRAS PERMANENTES**



**## GOLDEN RULES**

1\. A história nova **\*\*copia a sequência de funções\*\***, não a superfície.

2\. O hook é uma **\*\*perda irreparável\*\*** nos primeiros segundos.

3\. A violência acontece **\*\*fora de quadro\*\***; o efeito é a imagem.

4\. O colega descartável é **\*\*apresentado em segundos\*\*** e tem uma mania que vira ironia.

5\. O mentor oferece uma **\*\*regra concreta\*\*** e o episódio termina **\*\*antes\*\*** do payoff.

6\. A linguagem é **\*\*humana\*\***; biologia só aparece no cenário.

7\. O mundo é **\*\*nativo da espécie\*\***, mas apresentado limpo e charmoso.



**## FAILURE RULES**

1\. Nunca projetar um arco sem ter visto **\*\*todas\*\*** as partes da fonte.

2\. Nunca inventar gíria ou bordão; usar o léxico do usuário.

3\. Nunca copiar o ato violento literalmente se a espécie nova não pode fazê-lo.

4\. Nunca usar jargão de biologia nas falas.

5\. Nunca apagar frames ou análise antes da adaptação ser validada; salvar a análise da Parte 1.

6\. Nunca deixar \`historia.md\` e roteiro dessincronizados.

7\. Nunca afirmar que um arquivo está salvo sem conferir.

8\. Nunca usar nome parecido com IP conhecido.



**## MODELING RULES**

1\. Para cada beat: **\*\*evento, função, emoção, pergunta aberta, o que preservar, o que trocar\*\***.

2\. A troca é feita **\*\*por função\*\***; depois se verifica se a **\*\*emoção\*\*** se mantém.

3\. Cada beat novo **\*\*nasce do anterior\*\*** no universo novo (teste causal).

4\. Os personagens nascem de funções, depois ganham traços.

5\. O número de episódios segue a fonte (partes), e cada parte tem a sua própria fórmula (Parte 1: dúvida e perda; Parte 2: vingança e corrupção).

6\. Marcar o que é **\*\*evidência\*\*** e o que é **\*\*inferência\*\*** ao analisar a fonte.



**## LOCALIZATION RULES**

1\. **\*\*Localizar objetos e gestos\*\*** (chinelo, geladeira, pia, rodapé) antes de localizar palavras.

2\. O palavrão e a gíria vêm **\*\*do usuário\*\***, com sentido na frase.

3\. Relações familiares ganham **\*\*conflito cotidiano\*\*** (preocupação, "não pega no meu pé").

4\. Evitar traduzir piada: reconstruir a ironia com elementos do novo universo.

5\. A comida e o ambiente reais do Brasil (pizza, sofá, pia) são parte da piada.



**## COMPRESSION RULES**

1\. **\*\*Frases curtas\*\*** (a referência tinha \~6 palavras por frase).

2\. Medir palavras **\*\*antes de gerar\*\***: palavras totais × ritmo da fonte = duração esperada.

3\. Fundir beats redundantes; **\*\*não repetir exposição\*\*** entre cenas vizinhas.

4\. Cenas que na fonte duram 3 s **\*\*não podem virar 8 s\*\*** com fala.

5\. Cenas com dois falantes têm orçamento próprio; não somar falas longas.

6\. A pausa e o cliffhanger **\*\*não têm fala\*\***.

7\. Comparar a duração final com a da fonte; só então gerar imagem e vídeo.



\---



**## Pendências de sincronia (para quem for usar este documento)**

\- \`historia.md\`: ainda diz "cria", "3 NOITES", "esposa: nome a definir"; o v2 já mudou.

\- A análise da Parte 1 original está só na conversa; esta seção 2 é a reconstrução.

\- Parte 3 do original: não analisada.
