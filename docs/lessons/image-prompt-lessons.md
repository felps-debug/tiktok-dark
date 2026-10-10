<PARSED TEXT FOR PAGE: 1 / 6>
Análise forense: o que funcionou e o que falhou nos
prompts de imagem (Baratas, Ep. 01)
Base de evidência: a conversa inteira (cenas 1 a 14), os JSONs em ep-01/prompts/imagens/, as folhas de
personagem e as suas reações. Aviso de método: silêncio não é aprovação. Só considero "funcionou" quando
você reaproveitou, elogiou ("não tá feia") ou pediu ajuste pequeno. Cenas sem retorno (1, 2, 3, 4, 6, 8, 10, 12)
ficam como "sem veredito".



1. Melhores exemplos

              Exemplo                   Evidência de que funcionou                   Por que funcionou
 Cena 5, ambiente (cano de cobre        Você só reclamou das baratas; Objetos domésticos reaproveitados + 3 pistas do
 em arco, tampa de panela como          o cenário nunca foi           lugar ("embaixo da pia"). O gerador tem um
 quadro, luzinhas, carteiras de         questionado e eu o mantive    vocabulário visual claro para isso
 tampinha)                              nas duas reescritas
 Cena 7, composição (contra-            Você só reclamou dos cadetes Uma câmera única e nomeada + um personagem
 plongée, fogão/grelha ao fundo,        e da roupa do Sargento;      herói + lugar concreto
 tampinhas no chão)                     câmera e cenário ficaram
 Cena 9                                 "não ta feia nem nada", só a   Pose, emoção e adereços (capacete de dedal,
                                        escala estava errada           corda com gancho) estavam certos; faltava só
                                                                       âncora de escala
 Referência 11A (a sua imagem do        Você a usou como alvo ("tem    Ângulo alto em três-quartos, um objeto, dois
 homem no sofá, caixa aberta, Rocco     que ser parecido com o que     personagens, relação clara olhar → alvo
 na fatia)                              já tem")
 Fluxo de 3 passos dos prompts: ler     Nenhuma reclamação de          A identidade sempre veio da folha; o prompt só
 historia.md + roteiro, abrir folhas,   identidade (rosto, casca,      listava 4 a 5 traços-chave e dizia "NÃO copie
 decidir posicionamento, só então       cabelo) em nenhuma cena        pose/fundo/enquadramento"
 escrever

O que se repete nos acertos: 1. Um enquadramento nomeado por cena (plano médio de dois, contra-
plongée, simétrico por trás). 2. Traços de identidade curtos + a frase "use só para identidade". 3. Roupa
explícita quando a folha não tem (camisola, vestido de casa, camisa de cadete). 4. Ambiente com 3+ pistas
concretas do mundo da barata. 5. Boca fechada / primeiro frame: nunca houve reclamação de personagem
falando. 6. Emoção traduzida em partes do corpo (sobrancelha, pescoço, mãos), não só o nome da emoção.



2. Maus exemplos: CAUSA → RESULTADO → CORREÇÃO → REGRA
PERMANENTE

F1. Mundo errado (hospital humano) - CAUSA: imagens iniciais saíram sem o mundo da barata (cama de
hospital, monitor, cortina); isso está nas _descartadas/ e o style.json ainda mandava "não enquadrar como
miniatura". - RESULTADO: ambiente humano, barata como "ator em cenário humano". - CORREÇÃO: obrigar 3
pistas do mundo da barata (serpentinas da geladeira, caixa de fósforo, dedal, luzinhas). - REGRA: todo prompt
lista 3+ objetos domésticos em escala de barata. style.json precisa ser atualizado, pois ainda contradiz.
<PARSED TEXT FOR PAGE: 2 / 6>
F2. Figurantes viram baratas de verdade (cena 5) - CAUSA: "small roach pupils seen from behind". -
RESULTADO: cascos lisos, sem braços, baratas de quatro patas. - CORREÇÃO: "upright humanoid", camisa
cobrindo as costas, proibir "bare insect shell back"; anexar a folha do Rochito como molde. - REGRA: figurante
sem folha = definição humanoide explícita + molde de estilo anexado + proibição do corpo de inseto.

F3. Figurantes clonados (cenas 5 e 7) - CAUSA: o molde (Rochito) foi copiado N vezes; fileiras longas. -
RESULTADO: todos iguais, dezenas de figuras minúsculas. - CORREÇÃO: no máximo 4 a 8 figurantes, cada um
numerado com cabelo, altura, tom de casco e pose diferentes, e a frase "NOT copies of the Rochito sheet". -
REGRA: figurantes sempre enumerados e individualizados; quantidade pequena; molde só "loose style
template".

F4. Membro extra (professora com 3 braços, cena 5) - CAUSA: "uma mão com ponteiro, a outra atrás das
costas" + asas dobradas lidas como braço. - RESULTADO: três braços. - CORREÇÃO: "EXACTLY TWO arms: right
holds the pointer, left hangs at the side"; sem mão atrás das costas. - REGRA: poses com membros ocultos são
proibidas; declarar a contagem de membros e a posição de cada um.

F5. Roupa inventada (Sargento de calça, cena 7) - CAUSA: eu escrevi "olive uniform" genérico, sem as peças
da folha (short cargo, abdômen aparente). - RESULTADO: calça comprida. - CORREÇÃO: nomear as peças-
assinatura da folha ("cargo shorts, bare abdomen segments, black gloves/boots"). - REGRA: o que não é
nomeado é reinventado. Listar as peças-assinatura de cada folha.

F6. Escala quebrada (cenas 9, 11, 13, 14) - CAUSA: o prompt pedia "escala humano vs barata" mas sem âncora
numérica; a barata aparece perto do tamanho humano. - RESULTADO: barata do tamanho da perna do homem;
props (corda, tampinha) gigantes ao lado. - CORREÇÃO: âncoras absolutas ("do tamanho do dedão", "chinelo
mais comprido que os dois juntos", "12 a 15% da altura do quadro", "migalha do tamanho da cabeça de uma
barata"); remover props em escala de barata. - REGRA: toda cena com humano tem bloco SCALE com 3 âncoras
comparativas + % do quadro.

F7. Olhar errado (cena 13) - CAUSA: folhas de frente + nenhuma direção de olhar. - RESULTADO: os dois
encarando a câmera. - CORREÇÃO: vistos de trás em três-quartos, cabeça virada para o alvo, "nobody looks at
the camera". - REGRA: todo personagem tem gaze_target explícito; folha só de frente exige "rear three-quarter"
no texto.

F8. Continuidade e lógica espacial (11A, 4 tentativas) - CAUSA: gerei a cena isolada, sem ancorar nas takes 9
e 10 (caixa na coxa, sofá cinza, corda pendurada). Depois usei "esquerda" ambíguo (lado do quadro ou lado do
corpo?). - RESULTADO: caixa numa mesa; segunda caixa vazia; homem por cima da caixa; Rochito no meio do
caminho; caixa do lado errado. - CORREÇÃO: bloco CONTINUITY copiando fatos das takes anteriores + layout
horizontal em lado do quadro + tirar personagens não essenciais. - REGRA: antes de escrever, listar
objetos/posições herdados da cena anterior; sempre dizer "lado do quadro". Em dúvida de lateralidade, nomear
as duas.

F9. Bloqueio de conteúdo (11A e 11B) - CAUSA: homem com chinelo levantado + Rocco agonizando/braço
arrancado. - RESULTADO: você relatou bloqueio nas duas. - CORREÇÃO: 11A sem arma levantada; 11B com
impacto escondido por nuvem de poeira, sem corpo. - REGRA: o primeiro frame mostra a antecipação, não o
dano. Violência fica no vídeo, ocultada por poeira/sombra.

F10. Uso errado do material (print do Gemini) - CAUSA: JSON de vídeo (duration_seconds) colado no lugar
do gemini_prompt; anexos errados. - RESULTADO: o Gemini respondeu em texto. - REGRA: colar só o texto de
<PARSED TEXT FOR PAGE: 3 / 6>
gemini_prompt; anexar na ordem listada.

F11. Prompt grande demais - CAUSA: acrescentar blocos (SCALE, CONTINUITY, figurantes) sem cortar nada.
Passei do limite de 350 palavras em várias cenas (até ~410). - RESULTADO: não há prova direta de falha, mas a
taxa de correção subiu nas cenas mais longas (5, 7, 13). - REGRA: ao inserir um bloco obrigatório, cortar o
cenário e a repetição de identidade.



3. JSON estruturado

Por que existe a separação cena → prompt: a lógica da cena (quem fica onde, o que olha, escala, herança da
cena anterior) precisa existir como dados antes de virar prosa. Quando eu pulei isso (11A inicial, 13, 14),
apareceram os erros de layout, olhar e escala.

Campos por utilidade observada: - Sempre melhoraram: shot_type, main_character_reference,
character_reference_instruction, character_details, environment_details. - Redundantes: aspect_ratio (fixo
9:16), character_reference_instruction (texto idêntico em todas as cenas; pode virar constante). - Faltavam e
causaram erro: continuidade, escala, direção do olhar, contagem de membros, layout em lado do quadro, lista
de figurantes individualizados, proibições, checagem pós-geração.

Schema canônico proposto

 {
     "scene_id": "EP01_SHOT0X",
     "aspect_ratio": "9:16 (Vertical)",
     "story_beat": "o que acontece na história (1 linha, não vai para o prompt)",
     "frame_moment": "o instante exato capturado, ANTES da fala/ação",
     "continuity": {
          "previous_shot": "scene_id ou null",
          "carry_over": ["objetos, roupas, estado, lado do quadro que devem se repetir"]
     },
     "camera": {
       "shot_type": "um tipo por cena",
          "angle_height": "ex.: contra-plongée, nível da pizza",
          "differs_from_previous": true
     },
     "layout": {
       "frame_left": "...", "frame_right": "...", "foreground": "...", "background": "...",
       "note": "sempre lado do quadro, nunca lado do corpo"
     },
     "scale": {
        "anchors": ["3 comparações absolutas"],
        "roach_frame_height_percent": 15
     },
     "references": [
          { "role": "identity", "file": "path.png", "character": "Nome" },
          { "role": "style_template_only", "file": "path.png", "character": "Nome" },
        { "role": "continuity", "file": "imagem aprovada anterior", "keep": ["o que preservar"] }
     ],
     "characters": [
<PARSED TEXT FOR PAGE: 4 / 6>
          {
              "name": "",
              "identity_locked": ["4 a 5 traços da folha"],
              "outfit_this_scene": "",
              "pose": "",
              "limbs": "exatamente dois braços; qual segura o quê",
              "expression": { "eyes": "", "brows": "", "mouth": "fechada/entreaberta", "neck_hands": "" },
              "gaze_target": "quem/o que olha; nunca a câmera salvo pedido"
          }
     ],
     "extras": [ { "id": 1, "hair": "", "height": "", "shell_tone": "", "pose": "" } ],
     "props": ["objetos obrigatórios com escala"],
     "environment": { "place": "", "roach_world_cues": ["mínimo 3"], "light": "" },
   "forbidden": ["texto na imagem", "corpo de inseto nos figurantes", "violência explícita", "pose da
 folha"],
   "first_frame_rule": "boca fechada ou entreaberta, ninguém fala ainda",
     "gemini_prompt": "texto final, até ~350 palavras, ordem das 8 etapas",
     "check_after_generation": ["3 pontos mais prováveis de errar"]
 }


O que permanece estruturado e não vira prosa cedo: layout, escala, olhar, membros, figurantes e continuidade.
A prosa final só junta esses campos.



4. Sistema de referências

Folha de personagem (CHARACTER MODEL SHEET) → só identidade: rosto, tom de casco, cabelo, antenas,
proporção, roupa quando a folha mostra, acessórios. Não controla: pose, fundo, enquadramento, câmera,
composição, expressão. Todos os prompts bons traziam a frase "Use ONLY for identity... Do NOT copy their
standing pose, framing or white background". Lacuna: só há folha de frente para Rochito, Dona Blatta, Rocco,
Sargento e Quitina; isso pesa quando a cena pede costas ou perfil (cena 13).

Folha como molde de estilo → papel separado (caso Rochito nas cenas 5/7/8): "loose style template, not a
main character, do not copy". Sem essa linha ele é clonado.

Referência de continuidade (cena anterior aprovada) → preserva: roupa atual, ferimentos, props, ambiente,
luz, estado do personagem, lado do quadro. Diferença: a folha diz "quem é"; a continuidade diz "como estão as
coisas agora". Nunca misturar os dois papéis no mesmo anexo, e declarar o papel de cada imagem no prompt
("Image 3 is the approved previous shot: same sofa, same box"). Estado atual: os JSONs só anexam folhas;
nenhuma cena anexa imagem de continuidade ainda. As recomendações para 11A foram dadas como texto.



5. História vs. quadro

Regra: o prompt descreve um instante estático, não a ação. - História: "o homem acorda e pega o Rocco
roubando". - Quadro: homem na metade direita, torso meio levantado, cabeça virada para a esquerda, olhos
fixos na caixa, sobrancelhas franzidas, boca fechada, mãos paradas; Rocco na fatia, encolhido, ombros curvados,
mãos no pepperoni.
<PARSED TEXT FOR PAGE: 5 / 6>
Nível de especificidade que funcionou: 1. Olhar (para quê/quem). 2. Sobrancelha e olho (inclinação, abertura).
3. Estado da boca (fechada ou entreaberta). 4. Posição das mãos e dos membros (e quantos). 5. Relação
entre personagens (quem está onde, em lado do quadro). 6. Altura e tipo de câmera.

Abaixo disso o gerador improvisa (olha para a câmera, pose neutra). Acima disso (micro-layout de "rostos na
metade de cima") o seu prompt original já proibia, e eu respeitei. Conflito resolvido: "boca fechada no primeiro
frame" vs. cenas de dor/choro. Solução usada: a emoção vai para olhos, sobrancelha e corpo; a boca aberta só
aparece se o momento capturado for justamente o grito/suspiro.



6. Continuidade de personagem (leitura até onde o texto chegou)

Identity-locked (quase nunca muda) | Personagem | Travado | |---|---| | Dona Blatta | casca cobre-laranja lisa,
olhos castanhos grandes, coque castanho com fios soltos, antenas longas de ponta enrolada, silhueta esguia | |
Rochito | casca cobre-laranja, olhos grandes castanhos com sobrancelhas preocupadas, cabelo castanho-escuro
bagunçado, duas antenas finas, proporção de menino | | Rocco | magro, topete castanho, manchas laranja na
cabeça, uma antena curva e uma com ponta de clava, colete azul-petróleo com cinto | | Sargento Carapaça |
grande e musculoso, casco avermelhado escuro, cicatriz no olho, presas, boina, short cargo, abdômen aparente,
luvas e botas | | Prof. Quitina | casco mogno, cabeça pontuda, coque, óculos de gatinho, blazer e saia lápis cinza
| | Dr. Antenor | casco avermelhado, cabelo grisalho para trás, cavanhaque, óculos redondos dourados, jaleco
com estetoscópio | | Homem | cabelo escuro cacheado, barba por fazer, camiseta amarela manchada de molho,
short azul-marinho, chinelo vermelho |

Variáveis por cena: pose, expressão, direção do olhar, câmera, luz, roupas quando a folha não tem (Blatta:
camisola → vestido damasco com avental; Rochito: camisa de cadete; Rocco: capacete de dedal), estado
(lágrimas, olhos vermelhos, poeira), posição no quadro.

Roupas já fixadas para o episódio (manter igual em todas as cenas) - Dona Blatta: vestido de casa damasco
com avental creme (cenas 4, 6, 12, 13, 14); camisola pálida na maternidade (1, 2). - Rochito: camisa de cadete
verde-oliva com botões dourados. - Rocco: colete da folha + capacete de dedal grande.



Regras permanentes (resumo)

   1. Um enquadramento nomeado por cena, diferente do anterior.
   2. Identidade só da folha, com 4 a 5 traços; sempre "não copie pose/fundo".
   3. Nomear as peças-assinatura da folha; vestir quem não tem roupa.
   4. Mundo da barata: 3+ objetos domésticos em escala de barata.
   5. Humano na cena: bloco SCALE com âncoras + % do quadro; sem props em escala de barata.
   6. Todo personagem: direção do olhar, contagem de membros, estado da boca.
   7. Figurantes: poucos, enumerados, individualizados, humanoides, molde só de estilo.
   8. Continuidade: copiar fatos da cena anterior e anexar a imagem aprovada, com papel declarado.
   9. Lateralidade sempre em lado do quadro.
  10. Primeiro frame mostra a antecipação; dano e violência ficam no vídeo ou ocultos (poeira/sombra).
  11. Remover personagens não essenciais do quadro de revelação.
  12. Colar só gemini_prompt; anexar na ordem da lista.
<PARSED TEXT FOR PAGE: 6 / 6>
 13. Manter ~350 palavras: ao inserir um bloco obrigatório, cortar cenário ou repetição.
 14. Atualizar style.json (ainda manda não usar mundo em miniatura e luz fria militar).


Limites desta análise

    Várias cenas não tiveram retorno; tratei como "sem veredito".
    O seu texto terminou no meio da seção 6 (a lista "pose, expression, -" ficou cortada). Se houver seções 7
    em diante (por exemplo, checklist final ou formato de saída), me mande para eu completar.
