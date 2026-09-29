# Batalha Naval — GPTech Games

Sistema de Batalha Naval desenvolvido em Python para a disciplina de **Programação em Python**, do curso de **Engenharia de Computação — CEFET-MG Campus Divinópolis**.

O projeto foi desenvolvido como um sistema de jogo em modo texto, com foco em modularização, programação orientada a objetos, listas, matrizes, arquivos JSON, validação de entradas e organização de código segundo boas práticas de programação e padrão PEP 8.

Vídeo de funcionamento: https://youtu.be/P8ukzhrLHLg

---

## 1. Sobre o projeto

O projeto consiste na implementação de uma versão em modo texto do jogo clássico **Batalha Naval**, seguindo os requisitos funcionais, requisitos não funcionais e regras de negócio definidos no enunciado do trabalho.

O sistema permite que o usuário escolha entre dois modos de jogo:

- **Jogador x Computador**
- **Dois Jogadores**

Cada jogador possui um tabuleiro de **10x10 posições** e uma frota composta por três navios:

- 1 navio pequeno, ocupando 2 posições;
- 2 navios grandes, ocupando 4 posições cada.

Os navios são posicionados automaticamente pelo sistema, sem sobreposição.

Durante a partida, os jogadores escolhem coordenadas no formato **Letra + Número**, como `C5`, e o sistema informa se a jogada atingiu água, acertou um navio ou afundou uma embarcação.

Ao final da partida, o sistema apresenta informações como vencedor, quantidade de jogadas, quantidade de acertos e tempo total de jogo. Também são armazenadas estatísticas e o histórico da última partida, permitindo consultar os resultados posteriormente e reproduzir o replay.

---

## 2. Objetivos

O principal objetivo do projeto é desenvolver um sistema funcional de Batalha Naval aplicando conceitos fundamentais da linguagem Python e boas práticas de desenvolvimento de software.

Entre os principais objetivos estão:

- Utilizar programação orientada a objetos;
- Aplicar modularização;
- Trabalhar com listas e matrizes;
- Utilizar arquivos JSON para persistência de dados;
- Implementar validação de entradas;
- Desenvolver um modo Jogador x Computador;
- Desenvolver um modo Dois Jogadores;
- Registrar estatísticas das partidas;
- Registrar o histórico das jogadas;
- Implementar um sistema de replay;
- Manter o código organizado e legível;
- Seguir o padrão PEP 8.

---

## 3. Requisitos do projeto

O sistema foi desenvolvido com base nos requisitos definidos no documento de requisitos da GPTech Games.

### 3.1 Requisitos Funcionais

| ID | Requisito | Implementação |
|---|---|---|
| RF01 | Exibir um menu principal | O arquivo `menu.py` apresenta as opções principais do sistema. |
| RF02 | Gerar tabuleiro 10x10 para cada jogador | Cada objeto `Tabuleiro` possui uma matriz de 10 linhas por 10 colunas. |
| RF03 | Suportar navios pequeno e grande | A classe `Navio` possui navio pequeno de 2 posições e navio grande de 4 posições. |
| RF04 | Posicionar navios automaticamente sem sobreposição | O método `add_navio_rand()` realiza o posicionamento automático verificando se as posições estão livres. |
| RF05 | Validar as jogadas | O sistema valida coordenadas e rejeita posições já atacadas. |
| RF06 | Exibir mensagens de água, acerto e navio afundado | O sistema informa o resultado de cada ataque. |
| RF07 | Encerrar a partida com informações do resultado | Ao final são exibidos vencedor, total de jogadas, acertos e tempo de partida. |
| RF08 | Permitir iniciar uma nova partida | A opção de nova partida está disponível no menu e na tela de fim de jogo. |
| RF09 | Suportar dois modos de jogo | O sistema possui Jogador x Computador e Dois Jogadores. |
| RF10 | Permitir posicionamento e conferência antes do início | Os navios são posicionados automaticamente e o tabuleiro é exibido antes do início para conferência. |
| RF11 | Registrar histórico das jogadas | A classe `Replay` registra turno, jogador, coordenada e resultado. |
| RF12 | Calcular e exibir estatísticas | São armazenadas partidas, acertos, jogadas e aproveitamento dos jogadores. |
| RF13 | Disponibilizar replay da última partida | O sistema salva e reproduz o histórico da última partida. |

---

## 4. Requisitos Não Funcionais

| ID | Requisito | Implementação |
|---|---|---|
| RNF01 | Projeto individual | Projeto desenvolvido individualmente. |
| RNF02 | Python 3.10 ou superior | O projeto utiliza recursos compatíveis com Python 3.10+. |
| RNF03 | Padrão PEP 8 | O código foi organizado seguindo boas práticas de estilo, indentação e nomenclatura. |
| RNF04 | Organização em módulos | O sistema foi dividido em arquivos com responsabilidades específicas. |
| RNF05 | Tratamento de erros e entradas inválidas | Coordenadas inválidas, posições repetidas e arquivos JSON inválidos são tratados pelo sistema. |
| RNF06 | Execução em Linux | O projeto utiliza execução em terminal e foi estruturado para o ambiente definido no enunciado. |
| RNF07 | Interface em modo texto | A interface principal utiliza o terminal. |
| RNF08 | Interface gráfica opcional | Não foi utilizada interface gráfica nesta versão. |

---

## 5. Regras de negócio

O projeto também segue as regras de negócio definidas no enunciado.

### RN01 — Formato das coordenadas

As coordenadas devem ser informadas no formato:

```text
Letra + Número
```

As colunas disponíveis são:

```text
A B C D E F G H I J
```

As linhas disponíveis são:

```text
1 2 3 4 5 6 7 8 9 10
```

Exemplos válidos:

```text
A1
C5
J10
```

Exemplos inválidos:

```text
A0
K5
J11
ABC
```

---

### RN02 — Posição já atacada

Uma posição que já recebeu um ataque não pode ser utilizada novamente.

Quando o jogador informa uma posição repetida, o sistema apresenta uma mensagem indicando que a posição já foi atacada.

A jogada inválida não é registrada como uma nova jogada no histórico.

---

### RN03 — Navio afundado

Um navio é considerado afundado quando todas as suas posições forem atingidas.

Cada navio possui seu próprio contador de acertos.

Quando a quantidade de acertos de um navio alcança seu tamanho, o sistema informa que ele foi afundado.

---

### RN04 — Encerramento da partida

A partida termina quando todos os navios de um dos jogadores forem afundados.

Nesse momento, o jogador que ainda possui navios é declarado vencedor.

---

### RN05 — Jogadas do computador

No modo Jogador x Computador, o computador realiza suas próprias jogadas automaticamente.

O sistema mantém um conjunto com as posições que já foram utilizadas para evitar ataques repetidos.

Além disso, quando o computador acerta um navio, ele adiciona posições vizinhas como possíveis próximos alvos, tornando sua estratégia parcialmente guiada.

---

# 6. Estrutura do projeto

A estrutura principal do projeto segue a organização definida no enunciado:

```text
BatalhaNaval/
│
├── main.py
├── menu.py
├── tabuleiro.py
├── navios.py
├── jogador.py
├── computador.py
├── estatisticas.py
├── replay.py
├── utils.py
│
├── data/
│   ├── estatisticas.json
│   └── replay.json
│
├── docs/
│
└── README.md
```

---

## 7. Responsabilidade de cada arquivo

### `main.py`

É o arquivo principal da aplicação.

Responsável por:

- controlar o fluxo principal do sistema;
- iniciar o menu;
- iniciar novas partidas;
- controlar os turnos;
- controlar os modos de jogo;
- exibir os resultados dos ataques;
- calcular o tempo de partida;
- salvar estatísticas;
- salvar o replay;
- apresentar a tela de fim de jogo.

O programa é iniciado por:

```python
if __name__ == "__main__":
    main()
```

---

### `menu.py`

Contém a função responsável por exibir o menu principal.

O menu possui as seguintes opções:

```text
1. Nova partida
2. Ver estatisticas
3. Assistir replay da ultima partida
4. Creditos
5. Sair
```

---

### `tabuleiro.py`

Contém a classe `Tabuleiro`.

É responsável pela criação e controle do tabuleiro 10x10.

Também realiza:

- criação da matriz;
- posicionamento automático dos navios;
- verificação de posições disponíveis;
- recebimento de ataques;
- identificação de água;
- identificação de acertos;
- identificação de navios afundados;
- exibição do tabuleiro.

A representação das posições utiliza os seguintes símbolos:

| Símbolo | Significado |
|---|---|
| `~` | Água ou posição ainda não jogada |
| `N` | Navio |
| `X` | Acerto |
| `O` | Ataque que atingiu água |

---

### `navios.py`

Contém a classe `Navio`.

A classe representa cada embarcação da partida.

Cada navio possui:

- tipo;
- tamanho;
- lista de posições;
- quantidade de acertos.

Os tamanhos utilizados são:

```text
Navio pequeno → 2 posições
Navio grande  → 4 posições
```

A classe também possui métodos para:

- registrar um acerto;
- verificar se o navio foi afundado.

---

### `jogador.py`

Contém a classe `Jogador`.

Cada jogador possui:

- nome;
- tabuleiro;
- frota.

A classe cria automaticamente uma frota formada por:

```text
1 navio pequeno
2 navios grandes
```

Também é responsável por realizar ataques contra o adversário.

---

### `computador.py`

Contém a classe `Computador`, que herda da classe `Jogador`.

O computador utiliza:

```python
self.jogadas_feitas
```

para armazenar as posições que já foram atacadas.

Também possui:

```python
self.alvos_potenciais
```

para guardar posições próximas de ataques que obtiveram acerto.

A estratégia funciona da seguinte forma:

1. O computador verifica se possui algum alvo potencial.
2. Caso possua, seleciona um desses alvos.
3. Caso não possua, escolhe uma posição aleatória.
4. Verifica se a posição já foi utilizada.
5. Realiza o ataque.
6. Caso o ataque seja um acerto, adiciona posições vizinhas como possíveis novos alvos.

As posições analisadas são:

```text
acima
abaixo
esquerda
direita
```

O sistema também verifica se essas posições estão dentro do tabuleiro.

---

### `estatisticas.py`

Responsável pela persistência das estatísticas das partidas.

Os dados são armazenados no arquivo:

```text
data/estatisticas.json
```

São armazenadas informações como:

- vencedor;
- nome do jogador 1;
- nome do jogador 2;
- quantidade de jogadas;
- quantidade de acertos;
- aproveitamento.

O aproveitamento é calculado utilizando:

```text
(acertos / jogadas) × 100
```

Caso o jogador não possua jogadas registradas, o aproveitamento é considerado `0`.

---

### `replay.py`

Responsável pelo sistema de replay.

Durante a partida, cada jogada é armazenada contendo:

- número do turno;
- jogador;
- coordenada;
- resultado.

O histórico é salvo em:

```text
data/replay.json
```

O replay pode ser reproduzido posteriormente pelo menu principal.

Durante a reprodução, o usuário pode utilizar:

```text
ENTER
```

para avançar para a próxima jogada ou:

```text
Q
```

para sair do replay.

---

### `utils.py`

Contém funções auxiliares utilizadas por diferentes partes do sistema.

Atualmente possui:

- função para limpar a tela do terminal;
- função para converter coordenadas como `C5` para índices da matriz.

A coordenada:

```text
C5
```

é convertida para:

```text
linha = 4
coluna = 2
```

pois a matriz utiliza índices iniciando em zero.

---

# 8. Funcionamento do jogo

## 8.1 Início do programa

O programa deve ser iniciado executando:

```bash
python main.py
```

Após a inicialização, o menu principal será exibido.

Exemplo:

```text
==================================================
        BATALHA NAVAL - GPTECH GAMES
==================================================
1. Nova partida
2. Ver estatisticas
3. Assistir replay da ultima partida
4. Creditos
5. Sair
--------------------------------------------------
Escolha uma opcao:
```

---

# 9. Iniciando uma partida

Ao selecionar:

```text
1. Nova partida
```

o sistema apresenta:

```text
Selecione o modo de jogo:
        [1] Jogador vs Computador
        [2] Dois Jogadores
        [0] Voltar ao menu
```

---

## 9.1 Jogador x Computador

Ao escolher:

```text
[1] Jogador vs Computador
```

o sistema solicita o nome do jogador.

O segundo participante será criado automaticamente como:

```text
Computador
```

A frota dos dois participantes é criada automaticamente.

Antes do início da partida, o sistema apresenta a frota do jogador e solicita confirmação para iniciar.

---

## 9.2 Dois Jogadores

Ao selecionar:

```text
[2] Dois Jogadores
```

o sistema solicita:

```text
Digite o nome do Jogador 1:
Digite o nome do Jogador 2:
```

Após informar os nomes, os dois jogadores recebem seus respectivos tabuleiros e frotas.

---

# 10. Tabuleiro

Cada jogador possui um tabuleiro de:

```text
10 x 10
```

As colunas são identificadas pelas letras:

```text
A B C D E F G H I J
```

As linhas são identificadas pelos números:

```text
1 até 10
```

Exemplo:

```text
   A B C D E F G H I J
 1 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 2 ~ ~ X ~ ~ ~ ~ ~ ~ ~
 3 ~ ~ ~ N N N N ~ ~ ~
 4 ~ ~ ~ ~ ~ ~ ~ O ~ ~
 5 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 6 ~ ~ N N ~ ~ ~ ~ ~ ~
 7 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 8 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 9 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
10 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Legenda: ~ agua nao jogada | N navio | X acerto | O agua jogada
```

---

# 11. Sistema de ataques

Durante o turno do jogador, o sistema solicita:

```text
Sua jogada (ex: C5):
```

O jogador deve informar uma coordenada válida.

Por exemplo:

```text
C5
```

A coordenada é convertida para os índices utilizados internamente pela matriz.

O sistema verifica:

1. Se a coordenada está dentro do tabuleiro.
2. Se a posição já foi atacada.
3. Se existe um navio na posição.
4. Qual foi o resultado do ataque.

---

# 12. Resultados das jogadas

Existem três resultados principais.

## Água

Quando o jogador ataca uma posição sem navio:

```text
Agua! Nenhum navio atingido nessa posicao.
```

A posição passa a ser marcada como:

```text
O
```

---

## Acerto

Quando um navio é atingido:

```text
Acerto! Voce atingiu um navio inimigo.
```

A posição passa a ser marcada como:

```text
X
```

---

## Navio afundado

Quando todas as posições de um navio são atingidas:

```text
Navio afundado! Voce destruiu um navio do adversario.
```

---

# 13. Validação das coordenadas

O sistema rejeita coordenadas inválidas.

Exemplos:

```text
A0
K1
J11
ABC
1A
```

Quando uma coordenada não pode ser convertida ou está fora dos limites do tabuleiro, o sistema informa o erro e solicita uma nova entrada.

Também são rejeitadas posições que já receberam ataques.

Exemplo:

```text
Posição já atacada
```

Nesse caso, o jogador pode informar outra posição sem que a tentativa repetida seja contabilizada como uma nova jogada.

---

# 14. Posicionamento dos navios

Os navios são posicionados automaticamente pelo sistema.

A frota possui:

```text
1 navio pequeno → 2 posições
2 navios grandes → 4 posições cada
```

O posicionamento é realizado de forma aleatória.

Antes de posicionar um navio, o sistema verifica se todas as posições desejadas estão livres.

Somente após encontrar um espaço disponível, o navio é colocado no tabuleiro.

Dessa forma, os navios não ocupam a mesma posição.

Nesta versão do projeto, o posicionamento é feito automaticamente, em vez de solicitar ao jogador que escolha manualmente a posição de cada navio.

---

# 15. Condição de vitória

Cada jogador pode verificar se ainda possui algum navio não afundado.

Enquanto ambos os jogadores possuírem navios:

```text
a partida continua
```

Quando um dos jogadores perde todos os seus navios:

```text
a partida termina
```

O jogador que ainda possuir navios é declarado vencedor.

---

# 16. Controle de turnos

Durante uma partida, os jogadores alternam ataques.

O sistema mantém duas contagens:

### Turno

Representa a rodada atual da partida.

### Total de jogadas

Representa a quantidade individual de ataques realizados.

Por exemplo:

```text
Turno 1

Jogador 1 → uma jogada
Jogador 2 → uma jogada

Total de jogadas = 2
```

O histórico também registra cada ataque individualmente.

---

# 17. Tempo de partida

O tempo da partida é iniciado depois da confirmação:

```text
[ENTER] para iniciar a partida...
```

O sistema utiliza o módulo `time` da biblioteca padrão do Python para registrar o início e o final da partida.

Ao término, o tempo é convertido para o formato:

```text
MM:SS
```

Exemplo:

```text
Tempo de partida: 07:52
```

---

# 18. Estatísticas

Após cada partida concluída, o sistema salva automaticamente as informações no arquivo:

```text
data/estatisticas.json
```

Entre os dados armazenados estão:

```text
Vencedor
Nome do Jogador 1
Nome do Jogador 2
Jogadas do Jogador 1
Jogadas do Jogador 2
Acertos do Jogador 1
Acertos do Jogador 2
Aproveitamento do Jogador 1
Aproveitamento do Jogador 2
```

O aproveitamento é calculado por:

```text
Acertos ÷ Jogadas × 100
```

Exemplo:

```text
20 jogadas
8 acertos

8 ÷ 20 × 100 = 40%
```

---

# 19. Consulta das estatísticas

No menu principal, a opção:

```text
2. Ver estatisticas
```

permite consultar todas as partidas registradas.

O sistema informa a quantidade total de partidas e apresenta os dados de cada uma.

Exemplo:

```text
==================================================
        ESTATISTICAS
==================================================

Partidas registradas: 2

Partida 1:
Vencedor: Luis
Jogador 1 (Luis):
        Jogadas: 23    |       Acertos: 8    |       Aproveitamento: 34.78%
Jogador 2 (Computador):
        Jogadas: 22    |       Acertos: 6    |       Aproveitamento: 27.27%
```

---

# 20. Sistema de replay

Durante cada partida, o sistema registra todas as jogadas realizadas.

São armazenadas informações como:

```text
Turno
Jogador
Coordenada
Resultado
```

Após a partida, essas informações são salvas no arquivo:

```text
data/replay.json
```

O arquivo representa o histórico da última partida concluída.

---

# 21. Reproduzindo o replay

O replay pode ser acessado pelo menu principal:

```text
3. Assistir replay da ultima partida
```

Também pode ser acessado diretamente na tela de fim de jogo.

Durante a reprodução, cada jogada é apresentada individualmente.

Exemplo:

```text
Reproduzindo replay da ultima partida...

Jogada 01/34 - Luis - C5 - Agua
[ENTER] Próxima jogada [Q] Sair do replay
```

Ao pressionar `ENTER`, a próxima jogada é exibida.

Ao pressionar `Q`, o replay é encerrado.

---

# 22. Tela de fim de jogo

Ao terminar uma partida, o sistema apresenta:

```text
==================================================
        FIM DE JOGO
==================================================
Vencedor: Luis
Total de jogadas: 34
Acertos de Luis: 12
Acertos de Computador: 9
Tempo de partida: 07:52
--------------------------------------------------
[1] Ver replay [2] Nova partida [3] Menu principal
```

São disponibilizadas três opções:

### `[1] Ver replay`

Reproduz as jogadas da partida recém-finalizada.

### `[2] Nova partida`

Inicia outra partida.

### `[3] Menu principal`

Retorna ao menu inicial.

---

# 23. Arquivos de dados

O projeto utiliza arquivos JSON para armazenar informações persistentes.

## `data/estatisticas.json`

Armazena as estatísticas das partidas concluídas.

Exemplo simplificado:

```json
[
    {
        "vencedor": "Luis",
        "nome_jogador1": "Luis",
        "nome_jogador2": "Computador",
        "jogadas_jogador1": 20,
        "jogadas_jogador2": 19,
        "acertos_jogador1": 7,
        "acertos_jogador2": 5,
        "aproveitamento_jogador1": 35.0,
        "aproveitamento_jogador2": 26.31578947368421
    }
]
```

## `data/replay.json`

Armazena o histórico da última partida.

Exemplo:

```json
[
    {
        "turno": 1,
        "jogador": "Luis",
        "coord": "C5",
        "resultado": "agua"
    },
    {
        "turno": 2,
        "jogador": "Computador",
        "coord": "F7",
        "resultado": "acerto"
    }
]
```

---

# 24. Bibliotecas utilizadas

O projeto foi desenvolvido utilizando apenas bibliotecas da própria instalação do Python.

### `random`

Utilizada para:

- posicionamento aleatório dos navios;
- escolha aleatória de jogadas do computador.

### `json`

Utilizada para:

- salvar estatísticas;
- carregar estatísticas;
- salvar replay;
- carregar replay.

### `os`

Utilizada para:

- limpar a tela do terminal;
- criar a pasta `data`;
- verificar a existência dos arquivos JSON.

### `time`

Utilizada para:

- registrar o início da partida;
- registrar o fim da partida;
- calcular o tempo total de jogo.

Não são necessárias bibliotecas externas ou pacotes adicionais para executar o projeto.

---

# 25. Programação orientada a objetos

O projeto utiliza classes para representar os principais elementos do sistema.

As principais classes são:

```text
Navio
Tabuleiro
Jogador
Computador
Replay
```

A relação principal entre os objetos pode ser representada da seguinte maneira:

```text
Jogador
  │
  ├── possui um Tabuleiro
  │      │
  │      └── possui Navios
  │
  └── realiza ataques
```

O `Computador` herda da classe `Jogador`:

```text
Jogador
   ↑
   │ herança
   │
Computador
```

Isso permite reutilizar a estrutura básica de um jogador e acrescentar o comportamento específico da inteligência do computador.

---

# 26. Decisões de projeto

## 26.1 Matriz para representar o tabuleiro

Foi utilizada uma matriz de 10x10 para representar o tabuleiro.

Cada posição contém um símbolo que representa seu estado atual.

Essa abordagem facilita:

- acesso às posições;
- verificação de ataques;
- posicionamento de navios;
- exibição no terminal.

---

## 26.2 Lista de posições dos navios

Cada navio possui uma lista com as posições que ocupa no tabuleiro.

Exemplo:

```python
[(2, 3), (2, 4), (2, 5), (2, 6)]
```

Essa estrutura permite verificar se uma posição atingida pertence a determinado navio.

---

## 26.3 Conjunto de jogadas do computador

O computador utiliza um `set` para armazenar as jogadas já realizadas.

Isso evita ataques repetidos.

Exemplo:

```python
self.jogadas_feitas = set()
```

Uma posição como:

```python
(4, 7)
```

é adicionada ao conjunto depois de ser utilizada.

---

## 26.4 Arquivos JSON

Foi escolhido o formato JSON para os dados persistentes por ser simples, legível e suportado diretamente pela biblioteca padrão do Python.

O formato permite armazenar os dados entre diferentes execuções do programa.

---

## 26.5 Separação por módulos

Cada arquivo possui uma responsabilidade específica.

Isso facilita:

- manutenção;
- leitura do código;
- localização de erros;
- reutilização de funções e classes;
- compreensão da arquitetura.

---

# 27. Fluxo geral da aplicação

O funcionamento geral pode ser resumido da seguinte forma:

```text
                    INÍCIO
                       │
                       ▼
                Menu principal
                       │
          ┌────────────┼─────────────┐
          │            │             │
          ▼            ▼             ▼
     Nova partida   Estatísticas   Replay
          │
          ▼
      Escolha do modo
          │
       ┌──┴──┐
       ▼     ▼
      PvC    2P
       │     │
       └──┬──┘
          ▼
   Criação dos jogadores
          │
          ▼
   Criação das frotas
          │
          ▼
 Posicionamento automático
          │
          ▼
     Início da partida
          │
          ▼
      Turnos e ataques
          │
          ▼
    Validação da jogada
          │
          ▼
 Água / Acerto / Afundado
          │
          ▼
  Verificação dos navios
          │
      ┌───┴────┐
      │        │
    Continua   Fim
      │        │
      └────►   ▼
           Resultado final
                │
       ┌────────┼─────────┐
       ▼        ▼         ▼
     Replay  Estatísticas  Menu
```

---

# 28. Como executar

## Requisitos

É necessário ter:

```text
Python 3.10 ou superior
```

O projeto não necessita de instalação de bibliotecas externas.

---

## Execução pelo terminal

Entre na pasta do projeto:

```bash
cd BatalhaNaval
```

Execute:

```bash
python main.py
```

Em ambientes nos quais o comando `python` aponta para outra versão, pode ser utilizado:

```bash
python3 main.py
```

---

# 29. Execução no Linux

Como o ambiente definido no projeto é Linux, a execução recomendada é feita pelo terminal:

```bash
python3 main.py
```

O projeto utiliza comandos diferentes para a limpeza da tela dependendo do sistema operacional:

```python
os.system("clear" if os.name == "posix" else "cls")
```

Dessa forma, a função de limpeza pode funcionar tanto em ambientes Unix/Linux quanto em sistemas Windows.

---

# 30. Exemplo de uma partida

Uma partida pode seguir o fluxo:

```text
BATALHA NAVAL - GPTECH GAMES

1. Nova partida
2. Ver estatisticas
3. Assistir replay da ultima partida
4. Creditos
5. Sair
```

O usuário escolhe:

```text
1
```

Depois:

```text
Selecione o modo de jogo:

[1] Jogador vs Computador
[2] Dois Jogadores
[0] Voltar ao menu
```

O usuário escolhe:

```text
1
```

Informa o nome:

```text
Digite seu nome: Luis
```

O sistema cria:

```text
Luis
Computador
```

Após a criação das frotas, o tabuleiro é apresentado.

A partida começa depois da confirmação:

```text
[ENTER] para iniciar a partida...
```

Durante o jogo, o jogador pode informar:

```text
C5
```

O sistema pode responder:

```text
Agua! Nenhum navio atingido nessa posicao.
```

Ou:

```text
Acerto! Voce atingiu um navio inimigo.
```

Caso todas as posições daquele navio sejam atingidas:

```text
Navio afundado! Voce destruiu um navio do adversario.
```

Quando todos os navios de um jogador forem destruídos, a partida termina.

---

# 31. Tratamento de entradas inválidas

O projeto possui mecanismos para impedir que entradas incorretas interrompam o fluxo da partida.

São tratados casos como:

```text
Coordenada fora do tabuleiro
Posição já atacada
Formato incorreto de coordenada
Modo de jogo inexistente
Opção de menu inexistente
Arquivo JSON inválido
Replay inexistente
```

Em situações como um arquivo JSON vazio ou inválido, as funções de carregamento retornam uma lista vazia em vez de interromper o programa.

---

# 32. Organização e PEP 8

O código foi revisado para seguir boas práticas de organização e estilo.

Entre as práticas utilizadas estão:

- indentação consistente;
- nomes descritivos;
- separação entre módulos;
- espaçamento entre funções e classes;
- imports organizados;
- funções com responsabilidades específicas;
- comentários curtos nos principais métodos;
- uso de classes para representar entidades do jogo.

A organização também evita concentrar todas as funcionalidades em um único arquivo.

---

# 33. Testes realizados

Durante o desenvolvimento, foram realizados testes envolvendo diferentes partes do sistema.

### Menu

Foram testadas:

```text
Nova partida
Estatísticas
Replay
Créditos
Sair
```

### Modos de jogo

Foram testados:

```text
Jogador x Computador
Dois Jogadores
```

### Coordenadas

Foram verificadas entradas como:

```text
A1
C5
J10
A0
K1
J11
```

Também foram verificadas entradas com formatos inválidos.

### Ataques repetidos

Foi testado o comportamento ao atacar novamente uma posição já utilizada.

### Estatísticas

Foi verificado o armazenamento de múltiplas partidas e a recuperação dos dados salvos.

### Replay

Foi testado:

- reprodução da última partida;
- avanço com `ENTER`;
- saída utilizando `Q`;
- acesso pelo menu;
- acesso pela tela de fim de jogo.

### Nova partida

Foi testada a criação de uma nova partida após o término de outra.

### Persistência

Também foi verificado que os dados salvos permanecem disponíveis por meio dos arquivos JSON.

---

# 34. Possíveis extensões futuras

Embora a versão atual cumpra a proposta de um jogo em modo texto, algumas funcionalidades poderiam ser adicionadas em versões futuras.

Entre elas:

- posicionamento manual dos navios;
- escolha de orientação horizontal ou vertical;
- diferentes níveis de dificuldade para o computador;
- inteligência artificial mais avançada;
- ranking de jogadores;
- histórico completo de partidas;
- interface gráfica;
- efeitos sonoros;
- animações;
- sistema de pontuação;
- diferentes tamanhos de tabuleiro;
- diferentes tipos de navios.

Essas funcionalidades não fazem parte da implementação principal desta versão.

---

# 35. Bônus e possibilidades de evolução

O enunciado permite funcionalidades extras, incluindo interface gráfica, inteligência artificial e outros recursos adicionais.

Nesta versão, foi implementada uma estratégia simples de computador que, além das escolhas aleatórias, utiliza posições vizinhas após um acerto.

Essa abordagem permite que o computador continue procurando um navio próximo depois de encontrar uma posição pertencente a uma embarcação.

---

# 36. Relação entre os arquivos e requisitos

| Arquivo | Principais responsabilidades |
|---|---|
| `main.py` | Fluxo geral, partidas, turnos e integração dos módulos |
| `menu.py` | Menu principal |
| `tabuleiro.py` | Tabuleiro, ataques e posicionamento |
| `navios.py` | Representação dos navios |
| `jogador.py` | Jogadores, frota e ataques |
| `computador.py` | Comportamento automático do computador |
| `estatisticas.py` | Persistência das estatísticas |
| `replay.py` | Histórico e replay |
| `utils.py` | Funções auxiliares |

---

# 37. Conclusão

O projeto **Batalha Naval — GPTech Games** implementa uma versão funcional do jogo em modo texto utilizando Python.

A solução aplica conceitos de:

```text
Programação Orientada a Objetos
Modularização
Listas
Matrizes
Conjuntos
Arquivos JSON
Validação de entradas
Tratamento de exceções
Persistência de dados
Controle de fluxo
Herança
```

O sistema possui dois modos de jogo, tabuleiros 10x10, posicionamento automático de navios, validação de coordenadas, controle de ataques, identificação de navios afundados, condição de vitória, registro de estatísticas e sistema de replay.

A organização dos arquivos separa as responsabilidades do sistema e permite que cada parte do projeto possa ser compreendida e mantida de forma independente.

---

# 38. Créditos

**Batalha Naval — GPTech Games**

Desenvolvido por:

**Luís Mendes**

Disciplina:

**Programação em Python**

Professor:

**Guido Pantuza**

Curso:

**Engenharia de Computação**

Instituição:

**CEFET-MG — Campus Divinópolis**

Ano:

**2026**