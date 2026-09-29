# Diário de Desenvolvimento — Batalha Naval

## Informações do projeto

**Projeto:** Batalha Naval — GPTech Games  
**Disciplina:** Programação em Python  
**Curso:** Engenharia de Computação  
**Professor:** Guido Pantuza  
**Aluno:** Luís Mendes  
**Ano:** 2026  

---

## 1. Planejamento inicial

O projeto foi iniciado a partir dos requisitos definidos no enunciado do trabalho. A primeira etapa consistiu em analisar as funcionalidades necessárias e definir a divisão do sistema em módulos.

Foi definida a seguinte estrutura:

- `main.py`
- `menu.py`
- `tabuleiro.py`
- `navios.py`
- `jogador.py`
- `computador.py`
- `estatisticas.py`
- `replay.py`
- `utils.py`

Também foram definidos os arquivos JSON utilizados para persistência dos dados.

---

## 2. Implementação do tabuleiro e dos navios

Foi implementada a classe `Tabuleiro`, responsável pela criação da matriz 10x10, posicionamento dos navios, recebimento dos ataques e exibição do tabuleiro.

Também foi criada a classe `Navio`, responsável por armazenar o tipo, tamanho, posições e quantidade de acertos de cada embarcação.

A frota definida pelo projeto é composta por um navio pequeno e dois navios grandes.

---

## 3. Implementação dos jogadores

Foi criada a classe `Jogador`, responsável por armazenar o nome, tabuleiro e frota do participante.

Também foi implementada a validação das coordenadas informadas pelo jogador, impedindo entradas fora dos limites do tabuleiro e ataques repetidos.

---

## 4. Implementação do computador

Foi criada a classe `Computador`, que herda as características da classe `Jogador`.

O computador utiliza posições aleatórias quando não possui alvos potenciais. Quando consegue acertar um navio, posições vizinhas são adicionadas à lista de possíveis alvos.

Também foi implementado um conjunto para armazenar as posições já atacadas, evitando repetições.

---

## 5. Implementação dos modos de jogo

Foram implementados os dois modos solicitados:

- Jogador x Computador;
- Dois Jogadores.

O sistema passou a controlar os turnos, ataques, resultados das jogadas e condição de encerramento da partida.

---

## 6. Implementação das estatísticas

Foi implementado o armazenamento das estatísticas das partidas utilizando o formato JSON.

São registrados:

- vencedor;
- nomes dos jogadores;
- quantidade de jogadas;
- quantidade de acertos;
- aproveitamento.

Também foi criada uma opção no menu principal para consultar as partidas registradas.

---

## 7. Implementação do replay

Foi criada a classe `Replay` para registrar as jogadas realizadas durante a partida.

Cada registro contém o jogador, a coordenada, o resultado e o número do turno.

Após o término da partida, o histórico é salvo em `data/replay.json`.

Também foi implementada a reprodução da última partida, permitindo avançar entre as jogadas ou sair do replay.

---

## 8. Validação e testes

Foram realizados testes das principais funcionalidades do sistema.

Foram testados:

- menu principal;
- criação de novas partidas;
- modo Jogador x Computador;
- modo Dois Jogadores;
- coordenadas válidas;
- coordenadas inválidas;
- ataques repetidos;
- acertos;
- ataques em água;
- navios afundados;
- encerramento da partida;
- estatísticas;
- replay;
- nova partida após o término;
- retorno ao menu principal.

Também foram verificadas as informações armazenadas nos arquivos JSON.

---

## 9. Organização e PEP 8

Após a implementação das funcionalidades, o código foi revisado para melhorar a organização e a legibilidade.

Foram ajustados:

- indentação;
- espaçamento;
- nomes de variáveis;
- organização dos imports;
- separação entre funções;
- comentários dos principais métodos;
- estrutura dos módulos.

---

## 10. Situação final

Ao final do desenvolvimento, o sistema apresenta:

- menu principal;
- tabuleiro 10x10;
- três navios por jogador;
- posicionamento automático;
- modo Jogador x Computador;
- modo Dois Jogadores;
- validação de coordenadas;
- validação de ataques repetidos;
- mensagens de água, acerto e navio afundado;
- condição de vitória;
- controle do tempo da partida;
- estatísticas;
- histórico de jogadas;
- replay da última partida;
- persistência dos dados em arquivos JSON.