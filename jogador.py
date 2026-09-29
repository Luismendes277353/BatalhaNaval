from tabuleiro import Tabuleiro
from navios import Navio
from utils import traduzir_coordenada

class Jogador:
    # Cria um jogador e já monta a frota, eu considerei que o RF04 significaria
    # criar automaticamente o tabuleiro e mostrar para o jogador, só que o RF10 diz
    # para permitir o posicionamento, espero que eu não tenha entendido errado, tipo
    # eu coloquei pra visualizar antes da partida começar mas não a escolha :( só notei
    # esse possível erro hoje, na semana da entrega...
    def __init__(self, nome):
        self.nome = nome
        self.tabuleiro = Tabuleiro()
        self.preparar_frota()

    # Cria e posiciona a frota
    def preparar_frota(self):
        navio1 = Navio("pequeno")
        navio2 = Navio("grande")
        navio3 = Navio("grande")

        self.tabuleiro.add_navio_rand(navio1)
        self.tabuleiro.add_navio_rand(navio2)
        self.tabuleiro.add_navio_rand(navio3)

    # Verifica se ainda há navios
    # RN04 — A partida termina quando um dos jogadores afundar todos os navios do adversário
    def tem_navios(self):
        return any(
            not navio.afundou()
            for navio in self.tabuleiro.navios
        )

    # Realiza um ataque no adversário
    # RN02 — Uma jogada em posição já jogada deve ser rejeitada com mensagem explicativa, sem consumir a rodada.
    def atacar(self, adversario):
        while True:
            coord = input(
                f"{self.nome}, sua jogada (ex: C5): "
            )

            linha, col = traduzir_coordenada(coord)

            if linha is None or col is None:
                print(
                    f"Coordenada '{coord}' inválida (Tente A-J e 1-10)\n"
                )
                continue

            resultado = adversario.tabuleiro.receber_ataque(linha, col)

            if resultado == "invalido":
                print("Coordenada invalida")

            elif resultado == "repetido":
                print("Posição já atacada")

            else:
                return coord, resultado