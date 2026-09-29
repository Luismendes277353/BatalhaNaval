import random

class Tabuleiro:
    # Cria o tabuleiro vazio
    # RF02 — Gerar um tabuleiro de 10x10 posições para cada jogador
    def __init__(self):
        self.tamanho = 10
        self.grid = [
            ["~" for _ in range(self.tamanho)]
            for _ in range(self.tamanho)
        ]
        self.navios = []

    # Adiciona / Posiciona um navio aleatoriamente com o randint
    # RF04 — Posicionar os navios automaticamente no tabuleiro, sem sobreposição entre eles.
    def add_navio_rand(self, navio):
        posicionado = False

        while not posicionado:
            linha = random.randint(0, self.tamanho - 1)
            coluna = random.randint(0, self.tamanho - navio.tamanho)
            espaco_livre = all(
                self.grid[linha][c] == "~"
                for c in range(coluna, coluna + navio.tamanho)
            )

            if espaco_livre:
                for c in range(coluna, coluna + navio.tamanho):
                    self.grid[linha][c] = "N"
                    navio.posicoes.append((linha, c))

                self.navios.append(navio)
                posicionado = True

    # Processa o ataque recebido, se foi válido ou não
    # RF05 — Validar todas as jogadas informadas pelo usuário (coordenadas dentro do tabuleiro e não repetidas).
    def receber_ataque(self, linha, col):
        if (linha < 0
            or linha >= self.tamanho
            or col < 0
            or col >= self.tamanho
        ):
            return "invalido"
        
        alvo = self.grid[linha][col]
        
        if alvo in ["X", "O"]:
            return "repetido"
        
        if alvo == 'N':
            self.grid[linha][col] = 'X'

            for navio in self.navios:
                if(linha, col) in navio.posicoes:
                    navio.registrar_acerto()

                    if navio.afundou():
                        return "afundado"
                    
                    return "acerto"
                
        self.grid[linha][col] = 'O'
        return "agua"

    # Exibe o status atual do tabuleiro, sempre se atualizado a cada jogada
    def exibir(self, ocultar_navios=False):
        print("   A B C D E F G H I J")

        for i in range(self.tamanho):
            linha_str = f"{i+1:2d} "

            for j in range(self.tamanho):
                celula = self.grid[i][j]

                if ocultar_navios and celula=='N':
                    celula = '~'

                linha_str += f"{celula} "
            
            print(linha_str)

        print(
            "Legenda: ~ agua nao jogada | N navio | "
            "X acerto | O agua jogada"
        )