import random

from jogador import Jogador

class Computador(Jogador):
    # Cria o jogador computador
    #RF09 — Suportar dois modos de jogo: Jogador x Computador e Dois Jogadores.
    def __init__(self):
        super().__init__("Computador")
        self.jogadas_feitas = set()
        self.alvos_potenciais = []

    # Realiza o ataque automatico e inteligente
    # RN05 — No modo Jogador x Computador, o computador deve escolher jogadas válidas de forma
    # autônoma (escolha aleatória ou guiada por IA, por exemplo, ou outra forma inteligente com pontuação extra).
    def atacar(self, adversario):
        while True:
            if self.alvos_potenciais:
                linha, col = self.alvos_potenciais.pop()

            else:
                linha = random.randint(0,9)
                col = random.randint(0,9)

            if(linha,col) not in self.jogadas_feitas:
                self.jogadas_feitas.add((linha, col))

                resultado = adversario.tabuleiro.receber_ataque(
                    linha, col
                )

                letra = chr(col + 65)
                coord = f"{letra}{linha + 1}"

                self.processar_resultado_ai(
                    linha, col, resultado
                )

                return coord, resultado

    # Adiciona alvos próximos após um acerto
    # RN05 ai ó        
    def processar_resultado_ai(self, linha, col, resultado):
        if resultado == "acerto":
            vizinhos = [
                (linha - 1,col),
                (linha + 1, col),
                (linha, col - 1),
                (linha, col + 1)
            ]

            for v_l, v_c in vizinhos:
                if(
                    0 <= v_l < 10
                    and 0 <= v_c < 10
                    and (v_l, v_c) not in self.jogadas_feitas
                ):
                    self.alvos_potenciais.append((v_l, v_c))