<PARSED TEXT FOR PAGE: 1 / 8>
IMAGE-TO-VIDEO SYSTEM (baratas, Ep. 01)
Análise forense do que está nos arquivos do projeto: prompts/videos/*.json (21 arquivos), _prompt-prompts-de-
video.md , a memória do projeto e o histórico de edições visíveis nos próprios arquivos.


0. Limite honesto desta análise

Não existe registro de qual vídeo funcionou. Nenhum arquivo marca "aprovado" ou "falhou", e o feedback
sobre os vídeos não está nesta conversa (só o feedback sobre as imagens). O que dá para ver:

         Fato: o que está escrito em cada JSON e o que mudou entre versões (A/B, splits, frases novas).
         Inferência: o que a mudança sugere ter dado errado. Cada inferência abaixo vem marcada como
          [inferido] .
         Pendente: quais clipes realmente ficaram bons. Sem isso, "o que funcionou" é hipótese. Ao fim há uma
         tabela para você preencher.


0.1 Resultados informados (10/10/2026) — agora são dados, não hipóteses

         Funcionaram sem problema: todos os clipes exceto os dois abaixo (01A, 01B, 02, 03, 04A, 04B, 05, 06A,
         06B, 07, 08, 09, 10, 11A, 13, 14).
         FALHOU: 12. Cerca de 10 variações geradas; na maioria o personagem virava humano (o usuário citou
         "Rocco"; o Rocco nem está na imagem, então provavelmente é o Rochito ou o nome na fala induzindo o
         modelo; confirmar qual).
         FALHOU: 11B. "Tudo ruim no geral."

Diagnóstico da cena 12 (causas encontradas no próprio arquivo)

 Causa                           Evidência

 Fala muito acima do limite      29 palavras (Rochito) + 31 (Blatta) = 60 em 8 s = 7,5 palavras/s. O limite do projeto é ~3,3/s
                                 (≈ 26 em 8 s). Os clipes que funcionaram têm 8 a 31 palavras. Esta é a maior causa provável

 Dois falantes no mesmo          Viola a regra já seguida em 01A/B, 04A/B, 06A/B (todos bons)
 clipe

 Abraço com rosto                O Rochito está "face pressed against his mother's chest": o modelo não tem rosto para
 escondido                       ancorar e, quando ele vira, inventa um rosto, o que explica "virar humano"

 Corpos sobrepostos              Braços, avental e cabeça no mesmo ponto; membros de inseto se fundem e viram braços
                                 humanos

 Choro + soluço + fala           "sobs between words, hiccuping, tears running" pede movimento de boca/ombro que
                                 briga com o lip sync

 Nome "Rocco" na fala            O modelo pode ter desenhado um segundo personagem

 Câmera pull-back com troca      Mais um movimento acontecendo junto com a troca
 de falante no meio


Diagnóstico da cena 11B

 Causa                                  Evidência

 Corrida + rastreio lateral + fala de   A câmera tinha classificação "alto risco" (§10) e foi combinada com correria e fala
 31 palavras                            longa, os três mais instáveis
<PARSED TEXT FOR PAGE: 2 / 8>
 Frame inicial divergente               O prompt descreve Rochito "leaning back on one arm", pé gigante atrás, "fallen cadet
                                        shape"; a imagem foi trocada depois

 "Fallen cadet shape" fora da           Pede ao modelo um corpo que não está no frame
 imagem

 Muitas ações em 8 s                    Flip do chão, corrida, olhar para o corpo, olhar para trás, grito

 Violência                              O bloqueio que você relatou antes


Novas regras (F11 a F15)

 #       Regra permanente

 F11     Cena com dois falantes, ou 2 falas somando mais de ~26 palavras, vira dois clipes. Sem exceção (o 12 provou)

 F12     Rosto de todo personagem principal visível na imagem inicial. Se o rosto está escondido (abraço, de costas), o
         modelo inventa; refazer a imagem com o rosto de três-quartos voltado à câmera

 F13     Abraço e contato corporal: só um personagem em ação por vez, o outro quase imóvel; evitar braços cruzados e
         sobrepostos

 F14     Corrida + fala longa = nunca. Dividir: clipe 1 parado/reagindo com metade da fala; clipe 2 só a saída de quadro com
         o resto, câmera estática

 F15     Choro: lágrimas e olhos vermelhos sim; soluço e engasgo durante a fala não


Correção proposta para as duas cenas (sem gerar os prompts agora)

         12 → 12A + 12B: 12A Rochito fala (29 palavras: no limite, risco de corte; aceitável só se a imagem mostrar
         o rosto dele voltado à câmera), 12B Dona Blatta fala (31 palavras: dividir em 12B1 e 12B2 se ainda estourar).
         Antes disso, refazer a imagem 12 com os dois rostos visíveis (Rochito com a bochecha no ombro dela,
         olhos abertos).
         11B → 11B1 + 11B2: 11B1 = "Que porra foi essa, mataram o Rocco, ele estava ali do meu lado agora
         mesmo" (15 palavras), Rochito em pé, em choque, câmera estática, olhando para o pé. 11B2 = "eu tô fora
         dessa merda, eu não vou morrer por causa de uma migalha de pizza" (16 palavras), ele corre para fora do
         quadro, câmera estática. Sem rastreio.


1. Os prompts mais fortes (candidatos, não confirmados)

Critério: aparecem as correções mais maduras, ou seja, o prompt já absorveu falhas.

 Clipe               Por que parece o mais maduro

 scene_14            Estado final fechado (clique do interruptor aos 7.6 s), instrução de tamanho do Rochito, uma câmera, fala
                     completa que termina antes do evento final

 scene_11B           Corrige silêncio/áudio fraco ("IMPORTANT: ... voice clearly audible, main sound"), nunca mostra violência,
                     personagem imóvel descrito como "does not move or change"

 scene_01A +         Fala longa cortada no ponto natural; B usa o último frame de A como início; o silencioso tem boca
 01B                 fechada

 scene_04A +         Dois falantes em dois clipes; quem não fala tem "his mouth stays closed"
 04B


Elementos que se repetem em todos e que provavelmente seguram a qualidade [inferido] :

         Frame de origem como verdade ("exact first frame and the strict identity anchor").
         Uma tomada contínua, um movimento de câmera suave.
<PARSED TEXT FOR PAGE: 3 / 8>
       Linha do tempo com bloco 0-0.5 s em que o falante já abre a boca.
       Falas copiadas literalmente, em frase corrida, sem ponto final.
       Parágrafo de continuidade de áudio ("speech starts within 0.5 s, ends at the final frame, no falling
       intonation").
       SFX só diegéticos e rodapé negativo (sem música, legenda, logo, personagem novo).


2. Falhas: causa → resultado → correção → regra permanente

Tudo marcado [inferido] a partir de edições. Confirme com seus resultados.

 #     Causa                Resultado [inferido]       Correção já presente nos            Regra permanente
                                                       arquivos

 F1    37 palavras (cena    Fala atropelada ou         Cena 1 virou 01A (29 palavras) +    Máx. ~3.3 palavras/s úteis (≈
       1) em 8 s = 4.6      cortada                    01B (8 palavras, 5 s)               26 palavras em 8 s). Acima
       palavras/s                                                                          disso, dividir no ponto de troca
                                                                                           de falante

 F2    Frase "Rochito é     O Veo encolheu o           Cena 14: "Rochito is a teenage      Em toda cena com personagem
       teenage cadet"       Rochito para               cadet, not a baby or small child:   que cresceu, travar tamanho e
       ausente              bebê/criança               keep his exact size"                idade em texto

 F3    Frase de copyright   Recusa ou mutação          Memória pediu a frase;              Teste A/B por clipe. Não assumir
       / moderação                                     scene_14_variantes testa            que a frase sempre ajuda
                                                       V01-V05 com e V06-V10 sem

 F4    Falante sem voz      Rochito mudo ou voz        "IMPORTANT: Rochito speaks out      Dizer quem é o som principal do
       audível na 11B       baixa                      loud for the whole clip..."         clipe

 F5    Violência na         Bloqueio (você confirmou   Rosto do homem nunca                Violência = som + sombra +
       11A/11B              o bloqueio da 11A/11B,     mostrado, mão bate no sofá          reação. Nunca contato visível
                            só das imagens/vídeos)     nunca na barata

 F6    Personagem fora      Invenção de design         "Rocco is the only new character    Todo personagem que fala ou
       da imagem inicial                               allowed"                            age deve estar na imagem
       (Rocco na 11A)                                                                      inicial. Se não está, fazer outra
                                                                                           imagem, não descrever no vídeo

 F7    Dois falantes num    Troca de voz e lábios      04A/04B, 06A/06B, 01A/01B           Um falante principal por clipe; o
       clipe                errados                                                        outro só reage

 F8    Silencioso mexe a    Lip sync trocado           "his mouth stays closed" / "stays   Declarar a boca do ouvinte
       boca                                            silent"                             fechada em toda cena de
                                                                                           diálogo

 F9    Câmera que corta     Falante sai do quadro      04B: Blatta fica só uma fatia no    Câmera deve manter no quadro
       o ouvinte ou                                    canto                               todo quem fala
       perde o falante

 F10   Frame inicial ≠ o    Prompt descreve o que      11A/11B de vídeo foram escritos     Reescrever o prompt de vídeo
       descrito no          não existe                 para outra imagem que a atual       depois que a imagem é
       prompt                                                                              aprovada (ver §0, as duas cenas
                                                                                           11 estão desatualizadas)


Contradição encontrada: o gabarito diz "ONE SCENE = ONE PROMPT, never split", mas os arquivos têm 01A/B,
04A/B e 06A/B. A regra real do projeto é: dividir quando a fala passa de ~26 palavras ou tem dois falantes. O
gabarito precisa ser atualizado.


3. O JSON atual
<PARSED TEXT FOR PAGE: 4 / 8>
 Campo                           Função real                      Veredito

 scene_id , aspect_ratio         Identificação                    Mantém

 duration_seconds                Orçamento de fala                Mantém e ligar ao nº de palavras

 main_character_reference        Caminho do arquivo + quem está   Ótimo para você, inútil para o modelo; manter só
                                 na imagem                        como nota humana

 reference_continuity            Frase idêntica em 100% dos       Redundante: já está no passo 1 do veo_3_prompt
                                 arquivos

 camera_movement                 Um movimento                     Mantém, mas falta "onde começa / onde termina"

 character_animation             Linha do tempo                   Mantém; precisa ser estruturada por bloco

 dialogue                        Falas                            Falta falante em/fora de quadro, tempo de início/fim
                                                                  e contagem

 sfx_only                        Áudio                            Mantém

 veo_3_prompt                    Texto final                      Hoje duplica os outros campos à mão. Deve ser
                                                                  compilado deles


Faltavam: estado da imagem inicial, personagens ausentes, boca de quem escuta, estado do último frame, riscos
de moderação e contagem de palavras.


4. Imagem como verdade

Fórmula que aparece e que deve virar permanente:

  "Use the attached approved scene image as the exact first frame and the strict identity anchor. Keep every
  character exactly consistent with the image. Do not redesign, recolor or alter any character, the set or the
  props. Animate only expression, gaze, gestures, pose, motion, camera and lighting."

Regra de continuidade: descrever no prompt só o que está visível na imagem (tamanho relativo, roupa,
adereço) e o que deve mudar. Quando a imagem não dá uma informação crítica (idade, escala), travar em texto,
como na F2.


5. Responsabilidade: imagem × vídeo

Imagem resolve: quem está no quadro, escala (barata minúscula, homem gigante), roupa, adereços, cenário,
posição, expressão inicial, caixa/objetos, olhar.

Vídeo resolve: atuação, olhar em movimento, gesto, fala, câmera, micro-movimento.

Casos em que o vídeo foi obrigado a inventar o que a imagem devia ter:

       Rocco entrando por uma corda na 11A (deveria estar na imagem).
       O "corpo caído" na 11B descrito no texto, sem estar na imagem (virou "fallen shape").
       Escala do Rochito (F2).

Regra: se o prompt de vídeo precisa descrever um personagem, objeto ou tamanho que não está na
imagem, volte e gere outra imagem.


6. Linha do tempo
<PARSED TEXT FOR PAGE: 5 / 8>
Padrão observado: blocos 0-0.5 , 0.5-X , X-final , 3 a 4 blocos em 8 s. É razoável e provavelmente ajuda no
ritmo [inferido] .

        Bloco 1 (0-0.5 s): o falante abre a boca, olhar e postura iniciais.
        Bloco 2 (a fala): uma ação principal + 1-2 gestos. Não mais.
        Bloco 3 (últimos 0.4-1 s): o evento final ou a última palavra.
        Máx. 1 ação principal, 2 secundárias e 1 reação por bloco.


7. Hierarquia de atuação

Por clipe: PRIMARY (1 coisa), SECONDARY (até 2), FACIAL (olhos, sobrancelha, boca), REACTION (quem escuta),
CAMERA (1 movimento), ENV (só se der leitura, ex.: poeira, zumbido). Os melhores arquivos têm ~1 primária e ~3
pequenos gestos por bloco; a 11B é a mais cheia (flip + corrida + olhar + grito) e é a mais arriscada.


8. Diálogo e lip sync

        A fala começa em até 0.5 s (já está nos arquivos).
        Limite: ~26 palavras por 8 s. Entre 26 e 32, avisar "risco de corte". Acima disso, dividir.
        Quem escuta: "mouth stays closed" explícito.
        Fora de quadro: marcar "off-screen, no on-screen mouth" (11A).
        Emoção vocal: uma descrição por falante, igual em todos os clipes (tabela de vozes do gabarito).
        Fala sem ponto final e entonação aberta (memória do projeto).
        Quando gravar mudo: cenas com 2+ falantes simultâneos, correria + fala longa (11B) ou palavrão pesado
        que o Veo muta. Nesses casos, gerar o vídeo sem fala e dublar na edição.


9. Continuidade entre clipes

        Começa falando em 0.5 s, termina na última palavra, sem pausa final.
        Clipe B usa o último frame de A (01B, 04B).
        Manter olhar, pose e câmera do fim de A no início de B.
        Fim de clipe: o último frame precisa ser um estado estável e descrito ( end_state ).


10. Câmera

 Movimento              Uso observado               Risco

 Estática               V01/V06 da cena 14          Seguro

 Push-in lento          Cena 1                      Seguro

 Pull-back lento        Cena 14                     Seguro se o quadro inicial já tem o fundo (interruptor)

 Dolly lateral          04A/04B                     Médio: desloca o fundo

 Tilt                   11A, V02/V10                Médio: precisa de dois pontos nítidos

 Arco / foco            V05, V09                    Alto: pode mudar rosto

 Rastreio rápido        11B                         Alto: corrida + câmera


Regra: um movimento, com ponto de partida e de chegada descritos. Se o personagem corre, câmera estática
ou rastreio simples.


11. Densidade
<PARSED TEXT FOR PAGE: 6 / 8>
      MANDATORY: frame de origem, uma tomada, câmera única, linha do tempo, fala literal, voz, áudio
      contínuo, SFX diegéticos, negativos, boca do ouvinte.
      USEFUL: instrução de tamanho (cenas com personagem que cresceu), end_state , marcador off-screen.
      REDUNDANT: reference_continuity repetida; caminho do arquivo no JSON; SFX duplicado ("No music"
      aparece duas vezes na 11A).
      HARMFUL: "Rocco is the only new character allowed" (contradiz "no new characters"); "nothing graphic is
      added" em cena que já foi bloqueada (chama atenção para o risco); gestos demais em corrida.


12. Feedback seu convertido em regras (do que existe nesta conversa)

Você disse                                Regra

"o tamanho da barata e a percepção ta     Em cena com humano, escala vira regra no texto da imagem (barata ≈ dedão
errado"                                   do homem)

"estão olhando pro lugar errado"          Definir sempre para onde cada personagem olha, e que ninguém olha para a
                                          câmera

"a professora ta com 3 braços"            "Exatamente dois braços" em todo personagem com gesto

"os figurantes tão todos iguais"          Figurantes sempre listados um a um, diferentes

"a pizza em cima da mesa sendo que tava   A imagem precisa herdar o objeto e o lugar da take anterior
na perna"

"ESSA DESGRAÇA TA BLOQUEANDO"             Violência e ódio explícitos = risco; esconder o impacto, sem arma levantada
                                          na imagem inicial

"tem que estar na esquerda do homem"      Posição relativa: dizer "no lado esquerdo do QUADRO, ao lado, nunca
                                          embaixo"



13. IMAGE-TO-VIDEO SYSTEM: fluxo

   1. Inspecionar a imagem aprovada. Listar quem está, onde, pose, bocas, olhar, objetos, escala.
   2. Travar identidade e escala (texto curto).
   3. Propósito dramático em uma frase.
   4. Ação principal.
   5. Reações de quem escuta (boca fechada).
   6. Atuação facial início → fim.
   7. Câmera: precisa de movimento? Escolher o mais seguro.
   8. Orçamento de tempo: calcular palavras ÷ segundos. Dividir se passar de ~26 palavras ou 2 falantes.
   9. Encaixar a fala no bloco 2, começando em 0.5 s.
  10. SFX só o que ajuda a história.
  11. Gerar o JSON canônico.
  12. Compilar o veo_3_prompt a partir do JSON (sem digitar de novo).
  13. Autoverificação (abaixo).


14. JSON canônico proposto
<PARSED TEXT FOR PAGE: 7 / 8>
 {
     "scene_id": "EP01_SHOT14",
     "clip_role": "single | A | B",
     "duration_seconds": 8,
     "aspect_ratio": "9:16 (Vertical)",
     "start_frame": {
      "source": "path da imagem aprovada OU 'last frame of EP01_SHOTxxA'",
      "visible": ["quem e o que está na imagem, com tamanho relativo"],
      "absent": ["personagens/objetos que NÃO estão (e portanto não podem entrar)"],
      "mouths": "todas fechadas ou entreabertas"
     },
     "identity_lock": [
       { "name": "Rochito", "size_note": "teenage cadet, not a baby", "arms": 2 }
     ],
     "camera": {
       "movement": "static | slow push-in | slow pull-back | tilt | dolly",
      "start_framing": "...",
      "end_framing": "...",
      "must_keep_in_frame": ["quem fala"]
     },
     "timeline": [
     { "t": "0-0.5", "primary": "...", "secondary": "...", "face": "...", "reactions": { "Rochito": "mouth
 closed, ..." } }
     ],
     "dialogue": [
     { "speaker": "Dona Blatta", "on_screen": true, "voice": "...", "text": "...", "start_s": 0.4, "end_s": 7.6,
 "words": 28 }
     ],
     "silent_characters": [ { "name": "Rochito", "mouth": "closed for the whole clip" } ],
   "end_state": { "last_frame": "...", "intonation": "open, sentence continues", "handoff": "o que o próximo
 clipe espera" },
     "sfx_only": "...",
     "safety": { "shown": [], "never_shown": [], "mute_risk": "palavrão X" },
     "negative_constraints": "No music, subtitles, logos, text, new characters or objects.",
     "word_budget": { "words": 28, "max_for_duration": 26, "verdict": "tight" },
     "veo_3_prompt": "COMPILADO dos campos acima"
 }



15. GOLDEN RULES / FAILURE RULES / WORKFLOW / SELF-CHECK

GOLDEN RULES

     1. A imagem aprovada é a verdade. O vídeo só anima.
     2. Uma tomada, um movimento de câmera suave, com início e fim descritos.
     3. O falante abre a boca em 0.5 s e a última palavra termina no último frame.
     4. Um falante principal por clipe; o ouvinte tem boca fechada declarada.
     5. Quem fala ou age já está na imagem.
     6. Fala literal, sem ponto final, ≤ ~26 palavras em 8 s.
     7. Violência só em som, sombra e reação.
     8. Tamanho e idade travados em texto quando a imagem não deixa claro.

FAILURE RULES

     1. Nunca descrever personagem, objeto ou tamanho que não está na imagem.
     2. Nunca juntar dois falantes e fala longa no mesmo clipe.
     3. Nunca reaproveitar o prompt de vídeo depois de trocar a imagem sem reescrever.
     4. Nunca usar câmera de rastreio rápido com fala longa.
     5. Nunca pôr "nothing graphic" ou descrição de gore: isso chama o filtro.
<PARSED TEXT FOR PAGE: 8 / 8>
      6. Nunca repetir texto idêntico em reference_continuity e no prompt.

DEFAULT WORKFLOW

Os 13 passos da §13.

SELF-CHECK (antes de entregar qualquer prompt de vídeo)

☐ Olhei a imagem aprovada, e o prompt só descreve o que existe nela?
☐ Todo personagem que age está na imagem?
☐ Contei as palavras e comparei com a duração?
☐ Um falante principal? O ouvinte tem boca fechada?
☐ Uma câmera, com início e fim?
☐ Fala em 0.5 s, termina no último frame, sem entonação final?
☐ Escala e idade travadas em texto?
☐ Violência só por som/sombra/reação?
☐ O último frame é descrito e serve ao próximo clipe?
☐ O veo_3_prompt foi compilado do JSON?


Tabela de resultados (10/10/2026)

 Clipe                     Funcionou?    Observação

 01A, 01B, 02, 03          sim

 04A, 04B, 05, 06A, 06B    sim

 07, 08, 09, 10            sim

 11A                       sim           Prompt prevê quadro fechado na caixa de pizza

 11B                       não           Corrida + rastreio + 31 palavras + frame divergente

 12                        não           ~10 tentativas; personagem virava humano; 60 palavras e 2 falantes

 13, 14                    sim


Medida de calibração: os clipes bons têm 8 a 31 palavras e um falante principal; os dois que falharam têm 31
(com correria) e 60 (dois falantes).
