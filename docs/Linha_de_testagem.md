# Linha de testagem

Lista completa de testes para validar o projeto **Batalha Naval ---
GPTech Games**.

A ideia é executar os testes abaixo antes da entrega, marcando cada item
como concluído e anotando qualquer comportamento inesperado.

------------------------------------------------------------------------

## 1. Inicialização do programa

-   [ ] Executar `main.py` sem erros.
-   [ ] Verificar se o programa abre diretamente no menu principal.
-   [ ] Verificar se não aparecem mensagens de erro no terminal.
-   [ ] Verificar se todos os módulos são importados corretamente.
-   [ ] Verificar se as pastas e arquivos necessários são criados quando
    necessário.
-   [ ] Fechar o programa pela opção `5. Sair`.
-   [ ] Abrir o programa novamente depois de fechá-lo.
-   [ ] Confirmar que o programa continua funcionando após reiniciar.

------------------------------------------------------------------------

## 2. Menu principal

### Opção 1 --- Nova partida

-   [ ] Selecionar `1`.
-   [ ] Verificar se aparece a tela de seleção do modo.
-   [ ] Selecionar `0` para voltar.
-   [ ] Confirmar que retorna ao menu principal.
-   [ ] Digitar uma opção inexistente no menu de modos.
-   [ ] Confirmar que a opção inválida não inicia uma partida.
-   [ ] Confirmar que o programa permite voltar ao menu depois do erro.

### Opção 2 --- Estatísticas

-   [ ] Selecionar `2`.
-   [ ] Verificar a tela de estatísticas.
-   [ ] Abrir as estatísticas sem nenhuma partida registrada.
-   [ ] Confirmar a mensagem de ausência de partidas.
-   [ ] Registrar partidas e abrir as estatísticas novamente.
-   [ ] Confirmar que as partidas aparecem corretamente.

### Opção 3 --- Replay

-   [ ] Selecionar `3` sem existir replay.
-   [ ] Confirmar a mensagem de ausência de replay.
-   [ ] Jogar uma partida.
-   [ ] Selecionar `3` novamente.
-   [ ] Confirmar que o último replay é carregado.
-   [ ] Sair do replay com `Q`.
-   [ ] Confirmar que retorna ao menu.

### Opção 4 --- Créditos

-   [ ] Selecionar `4`.
-   [ ] Confirmar que a tela de créditos aparece.
-   [ ] Confirmar nome do projeto.
-   [ ] Confirmar nome do desenvolvedor.
-   [ ] Confirmar disciplina.
-   [ ] Confirmar professor.
-   [ ] Pressionar ENTER.
-   [ ] Confirmar retorno ao menu.

### Opção 5 --- Sair

-   [ ] Selecionar `5`.
-   [ ] Confirmar mensagem de saída.
-   [ ] Confirmar encerramento do programa.
-   [ ] Abrir o programa novamente e confirmar que os dados anteriores
    continuam salvos.

### Opções inválidas

-   [ ] Digitar `0` no menu principal.
-   [ ] Digitar `6`.
-   [ ] Digitar `10`.
-   [ ] Digitar `-1`.
-   [ ] Digitar uma letra.
-   [ ] Digitar uma palavra.
-   [ ] Apenas pressionar ENTER.
-   [ ] Confirmar que nenhuma entrada inválida quebra o programa.

------------------------------------------------------------------------

## 3. Seleção de modo

### Jogador vs Computador

-   [ ] Selecionar modo `1`.
-   [ ] Informar um nome válido.
-   [ ] Confirmar criação do jogador.
-   [ ] Confirmar criação do computador.
-   [ ] Confirmar que ambos recebem uma frota.
-   [ ] Confirmar que a partida começa normalmente.

### Dois jogadores

-   [ ] Selecionar modo `2`.
-   [ ] Informar o nome do Jogador 1.
-   [ ] Informar o nome do Jogador 2.
-   [ ] Confirmar criação dos dois jogadores.
-   [ ] Confirmar que ambos recebem uma frota.
-   [ ] Confirmar alternância entre os jogadores.

### Nome dos jogadores

-   [ ] Nome simples: `Luis`.
-   [ ] Nome com espaço: `Luis Mendes`.
-   [ ] Nome com acento.
-   [ ] Nome com números.
-   [ ] Nome vazio.
-   [ ] Confirmar que nomes válidos são exibidos corretamente durante a
    partida.

------------------------------------------------------------------------

## 4. Tabuleiro

-   [ ] Confirmar que o tabuleiro possui 10 linhas.
-   [ ] Confirmar que o tabuleiro possui 10 colunas.
-   [ ] Confirmar coordenadas de `A` até `J`.
-   [ ] Confirmar linhas de `1` até `10`.
-   [ ] Confirmar que o tabuleiro inicia com água não atacada.
-   [ ] Confirmar representação `~`.
-   [ ] Confirmar representação `N` para navios.
-   [ ] Confirmar representação `X` para acertos.
-   [ ] Confirmar representação `O` para água atacada.
-   [ ] Confirmar legenda do tabuleiro.
-   [ ] Confirmar alinhamento das coordenadas.
-   [ ] Confirmar funcionamento da exibição com navios visíveis.
-   [ ] Confirmar funcionamento da exibição com navios ocultos.

------------------------------------------------------------------------

## 5. Frota

-   [ ] Confirmar existência de 1 navio pequeno.
-   [ ] Confirmar existência de 2 navios grandes.
-   [ ] Confirmar navio pequeno com 2 posições.
-   [ ] Confirmar navio grande com 4 posições.
-   [ ] Confirmar que cada navio possui suas próprias posições.
-   [ ] Confirmar que cada navio inicia com 0 acertos.
-   [ ] Confirmar que `afundou()` retorna falso antes de todos os
    acertos.
-   [ ] Confirmar que o navio pequeno afunda após 2 acertos.
-   [ ] Confirmar que o navio grande afunda após 4 acertos.

------------------------------------------------------------------------

## 6. Posicionamento automático

-   [ ] Criar uma nova partida.
-   [ ] Verificar se todos os navios são posicionados automaticamente.
-   [ ] Confirmar que nenhum navio fica fora do tabuleiro.
-   [ ] Confirmar que nenhum navio ocupa posições repetidas.
-   [ ] Confirmar que os navios possuem exatamente os tamanhos
    esperados.
-   [ ] Criar várias partidas seguidas para testar diferentes posições.
-   [ ] Criar dezenas de tabuleiros e procurar sobreposição.
-   [ ] Confirmar que o programa não entra em loop infinito durante o
    posicionamento.
-   [ ] Confirmar que o posicionamento funciona mesmo em várias
    execuções do programa.

------------------------------------------------------------------------

## 7. Coordenadas válidas

Testar todas as extremidades:

-   [ ] `A1`
-   [ ] `B1`
-   [ ] `C1`
-   [ ] `D1`
-   [ ] `E1`
-   [ ] `F1`
-   [ ] `G1`
-   [ ] `H1`
-   [ ] `I1`
-   [ ] `J1`
-   [ ] `A10`
-   [ ] `B10`
-   [ ] `C10`
-   [ ] `D10`
-   [ ] `E10`
-   [ ] `F10`
-   [ ] `G10`
-   [ ] `H10`
-   [ ] `I10`
-   [ ] `J10`

Testar algumas coordenadas centrais:

-   [ ] `A5`
-   [ ] `C5`
-   [ ] `E5`
-   [ ] `F6`
-   [ ] `H7`
-   [ ] `J5`

------------------------------------------------------------------------

## 8. Coordenadas inválidas

Testar:

-   [ ] `A0`
-   [ ] `A11`
-   [ ] `K1`
-   [ ] `K10`
-   [ ] `Z5`
-   [ ] `AA5`
-   [ ] `1A`
-   [ ] `10A`
-   [ ] `A`
-   [ ] `1`
-   [ ] `AB`
-   [ ] `ABC`
-   [ ] `123`
-   [ ] `A-1`
-   [ ] `A+1`
-   [ ] `A 1`
-   [ ] `A1`
-   [ ] `a1`
-   [ ] `j10`
-   [ ] `a10`
-   [ ] `J11`
-   [ ] `K11`
-   [ ] `@1`
-   [ ] `A!`
-   [ ] entrada vazia

Para cada entrada inválida:

-   [ ] Confirmar mensagem de coordenada inválida.
-   [ ] Confirmar que nenhuma jogada é consumida.
-   [ ] Confirmar que o turno continua normalmente.
-   [ ] Confirmar que o programa não fecha.
-   [ ] Confirmar que o jogador pode tentar novamente.

------------------------------------------------------------------------

## 9. Ataque na água

-   [ ] Atacar uma posição que contém `~`.
-   [ ] Confirmar resultado `agua`.
-   [ ] Confirmar alteração da posição para `O`.
-   [ ] Confirmar mensagem de água.
-   [ ] Confirmar que a jogada é registrada.
-   [ ] Confirmar que o ataque conta nas estatísticas de jogadas.
-   [ ] Confirmar que o ataque não conta como acerto.

------------------------------------------------------------------------

## 10. Ataque em navio

-   [ ] Atacar uma posição que contém `N`.
-   [ ] Confirmar resultado `acerto`, caso não seja o último ponto do
    navio.
-   [ ] Confirmar alteração da posição para `X`.
-   [ ] Confirmar mensagem de acerto.
-   [ ] Confirmar registro da jogada no replay.
-   [ ] Confirmar aumento da quantidade de acertos.
-   [ ] Confirmar que a jogada aparece nas estatísticas.

------------------------------------------------------------------------

## 11. Navio afundado

### Navio pequeno

-   [ ] Encontrar uma posição do navio pequeno.
-   [ ] Acertar a primeira posição.
-   [ ] Confirmar que ainda não afundou.
-   [ ] Acertar a segunda posição.
-   [ ] Confirmar resultado `afundado`.
-   [ ] Confirmar mensagem de navio afundado.
-   [ ] Confirmar que o navio passa a ser considerado afundado.

### Navio grande

-   [ ] Encontrar as quatro posições de um navio grande.
-   [ ] Acertar a primeira.
-   [ ] Acertar a segunda.
-   [ ] Acertar a terceira.
-   [ ] Confirmar que ainda não afundou.
-   [ ] Acertar a quarta.
-   [ ] Confirmar resultado `afundado`.
-   [ ] Confirmar que o navio passa a ser considerado afundado.

------------------------------------------------------------------------

## 12. Ataque repetido

-   [ ] Atacar uma posição.
-   [ ] Tentar atacar a mesma posição novamente.
-   [ ] Confirmar resultado `repetido`.
-   [ ] Confirmar mensagem `Posição já atacada`.
-   [ ] Confirmar que a segunda tentativa não é registrada como jogada.
-   [ ] Confirmar que a segunda tentativa não altera as estatísticas.
-   [ ] Confirmar que o jogador pode escolher outra posição.
-   [ ] Repetir o teste com uma posição de água.
-   [ ] Repetir o teste com uma posição de navio.
-   [ ] Repetir o teste com uma posição já marcada como `X`.
-   [ ] Repetir o teste com uma posição já marcada como `O`.

------------------------------------------------------------------------

## 13. Regras de turno

-   [ ] Fazer uma jogada válida do Jogador 1.
-   [ ] Confirmar avanço para o Jogador 2.
-   [ ] Fazer uma jogada válida do Jogador 2.
-   [ ] Confirmar retorno ao Jogador 1.
-   [ ] Confirmar que jogadas inválidas não avançam o turno.
-   [ ] Confirmar que ataques repetidos não consomem uma jogada.
-   [ ] Confirmar contador de turno.
-   [ ] Confirmar contador de jogadas.
-   [ ] Confirmar diferença entre turno e jogada individual.

------------------------------------------------------------------------

## 14. Computador

-   [ ] Iniciar partida PvC.
-   [ ] Confirmar que o computador realiza ataques automaticamente.
-   [ ] Confirmar que o computador não pede entrada pelo teclado.
-   [ ] Confirmar que o computador escolhe coordenadas válidas.
-   [ ] Confirmar que o computador não repete uma posição.
-   [ ] Confirmar que o computador registra suas jogadas.
-   [ ] Confirmar que o computador consegue acertar navios.
-   [ ] Confirmar que o computador consegue afundar navios.
-   [ ] Confirmar que o computador continua jogando após ataques
    válidos.
-   [ ] Confirmar que o computador não trava quando encontra um acerto.
-   [ ] Confirmar que o computador tenta posições próximas depois de um
    acerto.
-   [ ] Confirmar que as posições próximas estão dentro do tabuleiro.
-   [ ] Confirmar que posições já jogadas não entram novamente como
    alvo.
-   [ ] Jogar várias partidas PvC.
-   [ ] Confirmar que nenhuma partida trava por causa da inteligência do
    computador.

------------------------------------------------------------------------

## 15. Dois jogadores

-   [ ] Iniciar modo 2 jogadores.
-   [ ] Confirmar que o Jogador 1 realiza sua jogada.
-   [ ] Confirmar que o Jogador 2 realiza sua jogada.
-   [ ] Confirmar alternância correta.
-   [ ] Confirmar que o tabuleiro do adversário aparece oculto quando
    necessário.
-   [ ] Confirmar que o jogador consegue visualizar seu próprio
    tabuleiro.
-   [ ] Confirmar que ataques inválidos permitem nova tentativa.
-   [ ] Confirmar que ataques repetidos permitem nova tentativa.
-   [ ] Confirmar que os dois jogadores têm estatísticas independentes.
-   [ ] Confirmar que o vencedor é identificado corretamente.

------------------------------------------------------------------------

## 16. Ocultação dos navios

-   [ ] Exibir o próprio tabuleiro.
-   [ ] Confirmar que os `N` aparecem.
-   [ ] Exibir o tabuleiro adversário com `ocultar_navios=True`.
-   [ ] Confirmar que os `N` adversários não aparecem.
-   [ ] Confirmar que `X` continua visível.
-   [ ] Confirmar que `O` continua visível.
-   [ ] Confirmar que `~` continua visível.
-   [ ] Confirmar que o jogador não consegue descobrir visualmente
    navios ainda não atingidos.

------------------------------------------------------------------------

## 17. Condição de vitória

-   [ ] Afundar apenas um navio.
-   [ ] Confirmar que a partida continua.
-   [ ] Afundar dois navios.
-   [ ] Confirmar que a partida continua.
-   [ ] Afundar todos os navios adversários.
-   [ ] Confirmar encerramento imediato da partida.
-   [ ] Confirmar que não ocorre ataque adicional depois da vitória.
-   [ ] Confirmar que o vencedor correto aparece.
-   [ ] Confirmar quantidade total de jogadas.
-   [ ] Confirmar quantidade de acertos.
-   [ ] Confirmar tempo de partida.
-   [ ] Confirmar gravação das estatísticas.
-   [ ] Confirmar gravação do replay.

------------------------------------------------------------------------

## 18. Tela de fim de jogo

-   [ ] Confirmar título `FIM DE JOGO`.
-   [ ] Confirmar nome do vencedor.
-   [ ] Confirmar total de jogadas.
-   [ ] Confirmar acertos do Jogador 1.
-   [ ] Confirmar acertos do Jogador 2.
-   [ ] Confirmar tempo da partida.
-   [ ] Confirmar opção `[1] Ver replay`.
-   [ ] Confirmar opção `[2] Nova partida`.
-   [ ] Confirmar opção `[3] Menu principal`.

------------------------------------------------------------------------

## 19. Nova partida após uma partida

-   [ ] Terminar uma partida.
-   [ ] Selecionar `[2] Nova partida`.
-   [ ] Confirmar abertura de uma nova partida.
-   [ ] Confirmar criação de novos tabuleiros.
-   [ ] Confirmar nova frota.
-   [ ] Confirmar que a partida anterior não interfere na nova.
-   [ ] Jogar a nova partida.
-   [ ] Confirmar que as estatísticas das duas partidas são preservadas.
-   [ ] Confirmar que o replay é atualizado para a partida mais recente.

------------------------------------------------------------------------

## 20. Retorno ao menu após uma partida

-   [ ] Terminar uma partida.
-   [ ] Selecionar `[3] Menu principal`.
-   [ ] Confirmar retorno ao menu.
-   [ ] Abrir estatísticas.
-   [ ] Confirmar que a partida recém-finalizada está registrada.
-   [ ] Abrir replay.
-   [ ] Confirmar que o replay está disponível.

------------------------------------------------------------------------

## 21. Replay

-   [ ] Jogar uma partida completa.
-   [ ] Abrir o replay.
-   [ ] Confirmar que todas as jogadas foram registradas.
-   [ ] Confirmar ordem correta das jogadas.
-   [ ] Confirmar nome do jogador em cada jogada.
-   [ ] Confirmar coordenada de cada jogada.
-   [ ] Confirmar resultado de cada jogada.
-   [ ] Confirmar contador `Jogada XX/YY`.
-   [ ] Pressionar ENTER para avançar.
-   [ ] Confirmar avanço para a próxima jogada.
-   [ ] Pressionar `Q`.
-   [ ] Confirmar saída do replay.
-   [ ] Reabrir o replay.
-   [ ] Confirmar que continua disponível.
-   [ ] Jogar uma nova partida.
-   [ ] Confirmar que o replay anterior foi substituído pelo novo
    replay.

------------------------------------------------------------------------

## 22. Arquivo de replay

-   [ ] Confirmar criação de `data/replay.json`.
-   [ ] Abrir o arquivo manualmente.
-   [ ] Confirmar que o JSON está válido.
-   [ ] Confirmar que existe um registro para cada ataque válido.
-   [ ] Confirmar campos `turno`, `jogador`, `coord` e `resultado`.
-   [ ] Confirmar que ataques inválidos não aparecem no replay.
-   [ ] Confirmar que ataques repetidos não aparecem como jogadas
    válidas.
-   [ ] Confirmar que o resultado registrado corresponde ao resultado
    exibido.

------------------------------------------------------------------------

## 23. Estatísticas

-   [ ] Jogar uma partida.
-   [ ] Abrir estatísticas.
-   [ ] Confirmar quantidade de partidas registradas.
-   [ ] Confirmar vencedor.
-   [ ] Confirmar nome do Jogador 1.
-   [ ] Confirmar nome do Jogador 2.
-   [ ] Confirmar jogadas do Jogador 1.
-   [ ] Confirmar jogadas do Jogador 2.
-   [ ] Confirmar acertos do Jogador 1.
-   [ ] Confirmar acertos do Jogador 2.
-   [ ] Confirmar aproveitamento do Jogador 1.
-   [ ] Confirmar aproveitamento do Jogador 2.
-   [ ] Jogar uma segunda partida.
-   [ ] Confirmar que o contador de partidas aumenta.
-   [ ] Confirmar que a primeira partida continua registrada.
-   [ ] Confirmar que a segunda partida aparece.
-   [ ] Fechar o programa.
-   [ ] Abrir novamente.
-   [ ] Confirmar persistência das estatísticas.

------------------------------------------------------------------------

## 24. Cálculo de aproveitamento

-   [ ] Fazer uma partida sem nenhum acerto.
-   [ ] Confirmar aproveitamento de 0%.
-   [ ] Fazer uma partida com acertos.
-   [ ] Conferir manualmente `acertos / jogadas * 100`.
-   [ ] Comparar com o valor exibido.
-   [ ] Confirmar duas casas decimais.
-   [ ] Confirmar que não ocorre divisão por zero.
-   [ ] Verificar uma partida com 100% de aproveitamento possível.
-   [ ] Verificar partidas com valores intermediários.

------------------------------------------------------------------------

## 25. Arquivo de estatísticas

-   [ ] Confirmar criação de `data/estatisticas.json`.
-   [ ] Confirmar que o arquivo contém uma lista JSON.
-   [ ] Confirmar que cada partida possui os campos esperados.
-   [ ] Abrir o arquivo depois de uma partida.
-   [ ] Confirmar que os dados correspondem à partida.
-   [ ] Jogar várias partidas.
-   [ ] Confirmar que os registros anteriores não são apagados.
-   [ ] Fechar e abrir o programa.
-   [ ] Confirmar persistência.
-   [ ] Testar arquivo vazio.
-   [ ] Testar arquivo contendo `[]`.
-   [ ] Testar arquivo JSON inválido.
-   [ ] Confirmar que o programa não quebra diante de JSON inválido.

------------------------------------------------------------------------

## 26. Persistência

-   [ ] Jogar uma partida.
-   [ ] Fechar o programa.
-   [ ] Abrir novamente.
-   [ ] Abrir estatísticas.
-   [ ] Confirmar dados da partida.
-   [ ] Abrir replay.
-   [ ] Confirmar replay da última partida.
-   [ ] Jogar outra partida.
-   [ ] Fechar o programa.
-   [ ] Abrir novamente.
-   [ ] Confirmar todas as estatísticas anteriores.
-   [ ] Confirmar que o replay corresponde à partida mais recente.

------------------------------------------------------------------------

## 27. Tempo da partida

-   [ ] Iniciar uma partida.
-   [ ] Confirmar que o cronômetro começa depois do ENTER de início.
-   [ ] Jogar rapidamente.
-   [ ] Conferir tempo exibido.
-   [ ] Jogar uma partida mais longa.
-   [ ] Confirmar aumento do tempo.
-   [ ] Confirmar formato `MM:SS`.
-   [ ] Confirmar que segundos aparecem com dois dígitos.
-   [ ] Confirmar que minutos aparecem com dois dígitos.
-   [ ] Confirmar que o tempo é calculado somente durante a partida.

------------------------------------------------------------------------

## 28. Testes de estresse

-   [ ] Criar 10 partidas.
-   [ ] Criar 20 partidas.
-   [ ] Criar 50 tabuleiros automaticamente.
-   [ ] Criar 100 tabuleiros automaticamente.
-   [ ] Jogar várias partidas PvC consecutivas.
-   [ ] Jogar várias partidas 2P consecutivas.
-   [ ] Criar muitos registros de estatísticas.
-   [ ] Criar muitos registros de replay.
-   [ ] Confirmar que o programa continua respondendo.
-   [ ] Confirmar que nenhum arquivo JSON fica corrompido.
-   [ ] Confirmar que não ocorre loop infinito no posicionamento.
-   [ ] Confirmar que o computador não entra em loop ao escolher
    ataques.

------------------------------------------------------------------------

## 29. Testes de entradas estranhas

-   [ ] Espaços antes da coordenada.
-   [ ] Espaços depois da coordenada.
-   [ ] Espaços antes e depois.
-   [ ] Letras minúsculas.
-   [ ] Letras maiúsculas.
-   [ ] Números fora do intervalo.
-   [ ] Caracteres especiais.
-   [ ] Strings muito longas.
-   [ ] Entrada vazia.
-   [ ] Apenas espaços.
-   [ ] Números sem letras.
-   [ ] Letras sem números.
-   [ ] Várias letras.
-   [ ] Coordenada com sinal negativo.
-   [ ] Coordenada com número decimal.
-   [ ] Confirmar que nenhuma dessas entradas encerra o programa
    inesperadamente.

------------------------------------------------------------------------

## 30. Testes de arquivos

-   [ ] Executar sem a pasta `data`.
-   [ ] Confirmar criação automática da pasta.
-   [ ] Executar sem `estatisticas.json`.
-   [ ] Confirmar criação automática do arquivo após uma partida.
-   [ ] Executar sem `replay.json`.
-   [ ] Confirmar mensagem adequada no menu de replay.
-   [ ] Criar `estatisticas.json` vazio.
-   [ ] Criar `replay.json` vazio.
-   [ ] Inserir JSON inválido em `estatisticas.json`.
-   [ ] Verificar comportamento.
-   [ ] Inserir JSON inválido em `replay.json`.
-   [ ] Verificar comportamento.
-   [ ] Confirmar que o programa não fecha de forma inesperada.

------------------------------------------------------------------------

## 31. Testes de código e organização

-   [ ] Confirmar nomes dos arquivos conforme a arquitetura proposta.
-   [ ] Confirmar `main.py`.
-   [ ] Confirmar `menu.py`.
-   [ ] Confirmar `tabuleiro.py`.
-   [ ] Confirmar `navios.py`.
-   [ ] Confirmar `jogador.py`.
-   [ ] Confirmar `computador.py`.
-   [ ] Confirmar `estatisticas.py`.
-   [ ] Confirmar `replay.py`.
-   [ ] Confirmar `utils.py`.
-   [ ] Confirmar pasta `data`.
-   [ ] Verificar imports não utilizados.
-   [ ] Verificar variáveis não utilizadas.
-   [ ] Verificar funções sem uso.
-   [ ] Verificar nomes das funções.
-   [ ] Verificar nomes das variáveis.
-   [ ] Verificar indentação.
-   [ ] Verificar linhas excessivamente longas.
-   [ ] Verificar comentários.
-   [ ] Verificar docstrings, caso utilizadas.
-   [ ] Verificar PEP 8.
-   [ ] Confirmar que cada módulo possui responsabilidade clara.

------------------------------------------------------------------------

## 32. Testes de documentação

-   [ ] Conferir `README.md`.
-   [ ] Conferir instruções de execução.
-   [ ] Conferir descrição do projeto.
-   [ ] Conferir estrutura de arquivos.
-   [ ] Conferir instruções de jogo.
-   [ ] Conferir requisitos necessários.
-   [ ] Conferir integrantes/desenvolvedor.
-   [ ] Conferir informações da disciplina.
-   [ ] Conferir se os comandos apresentados no README funcionam.
-   [ ] Conferir se os nomes dos arquivos do README correspondem aos
    arquivos reais.
-   [ ] Conferir se não existem informações desatualizadas.

------------------------------------------------------------------------

## 33. Teste de apresentação

-   [ ] Abrir o programa antes da apresentação.
-   [ ] Confirmar que inicia sem erro.
-   [ ] Mostrar menu.
-   [ ] Mostrar seleção PvC.
-   [ ] Mostrar tabuleiro.
-   [ ] Mostrar ataque na água.
-   [ ] Mostrar ataque em navio.
-   [ ] Mostrar navio afundado.
-   [ ] Mostrar comportamento do computador.
-   [ ] Mostrar fim de partida.
-   [ ] Mostrar estatísticas.
-   [ ] Mostrar replay.
-   [ ] Mostrar créditos.
-   [ ] Confirmar que todos os arquivos necessários estão no projeto.
-   [ ] Confirmar que os JSON de teste não possuem dados inadequados
    para apresentação.
-   [ ] Fazer uma partida de demonstração antes da apresentação.

------------------------------------------------------------------------

## 34. Teste completo de ponta a ponta

### Fluxo 1 --- PvC

-   [ ] Abrir programa.
-   [ ] Selecionar Nova partida.
-   [ ] Selecionar Jogador vs Computador.
-   [ ] Informar nome.
-   [ ] Conferir frota.
-   [ ] Iniciar partida.
-   [ ] Fazer ataques válidos.
-   [ ] Testar ataque repetido.
-   [ ] Testar coordenada inválida.
-   [ ] Observar ataques do computador.
-   [ ] Afundar todos os navios.
-   [ ] Conferir vencedor.
-   [ ] Conferir tempo.
-   [ ] Conferir jogadas.
-   [ ] Conferir acertos.
-   [ ] Conferir estatísticas.
-   [ ] Conferir replay.

### Fluxo 2 --- Dois jogadores

-   [ ] Abrir nova partida.
-   [ ] Selecionar Dois Jogadores.
-   [ ] Informar os dois nomes.
-   [ ] Conferir as frotas.
-   [ ] Fazer ataques alternados.
-   [ ] Testar coordenada inválida.
-   [ ] Testar ataque repetido.
-   [ ] Afundar todos os navios de um jogador.
-   [ ] Conferir vencedor.
-   [ ] Conferir estatísticas.
-   [ ] Conferir replay.

### Fluxo 3 --- Persistência

-   [ ] Jogar uma partida.
-   [ ] Fechar o programa.
-   [ ] Abrir novamente.
-   [ ] Conferir estatísticas.
-   [ ] Conferir replay.
-   [ ] Jogar outra partida.
-   [ ] Confirmar atualização dos dados.

------------------------------------------------------------------------

## 35. Teste final antes da entrega

-   [ ] Executar o projeto do zero.
-   [ ] Apagar temporariamente arquivos de dados de teste.
-   [ ] Executar uma partida PvC completa.
-   [ ] Executar uma partida 2P completa.
-   [ ] Conferir estatísticas.
-   [ ] Conferir replay.
-   [ ] Conferir retorno ao menu.
-   [ ] Conferir nova partida.
-   [ ] Conferir créditos.
-   [ ] Conferir saída.
-   [ ] Fechar e reabrir o programa.
-   [ ] Conferir persistência.
-   [ ] Revisar todos os arquivos `.py`.
-   [ ] Revisar README.
-   [ ] Revisar estrutura de pastas.
-   [ ] Remover arquivos temporários desnecessários.
-   [ ] Remover prints de depuração.
-   [ ] Remover dados de teste que não devem ser entregues.
-   [ ] Confirmar que não existem caminhos absolutos no código.
-   [ ] Confirmar que o projeto funciona na máquina usada para
    apresentação.
-   [ ] Confirmar que o vídeo de demonstração está pronto.
-   [ ] Confirmar que a apresentação está pronta.
-   [ ] Confirmar que todos os requisitos da atividade foram
    contemplados.

------------------------------------------------------------------------

## 36. Registro de problemas encontrados

  Teste   Resultado   Problema encontrado   Solução   Refeito?
  ------- ----------- --------------------- --------- ----------
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      

------------------------------------------------------------------------

## 37. Resultado final

-   [ ] Todos os testes críticos passaram.
-   [ ] Não existem erros conhecidos que impeçam a execução.
-   [ ] PvC funciona.
-   [ ] Dois jogadores funciona.
-   [ ] Coordenadas são validadas.
-   [ ] Ataques repetidos são bloqueados.
-   [ ] Navios são posicionados corretamente.
-   [ ] Navios afundam corretamente.
-   [ ] A partida termina corretamente.
-   [ ] O vencedor é identificado corretamente.
-   [ ] Estatísticas são salvas.
-   [ ] Estatísticas são carregadas.
-   [ ] Replay é salvo.
-   [ ] Replay é reproduzido.
-   [ ] Tempo de partida é registrado.
-   [ ] README está atualizado.
-   [ ] Estrutura do projeto está organizada.
-   [ ] Projeto está pronto para apresentação.
