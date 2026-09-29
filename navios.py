class Navio:
    # Representa um navio da frota de navios
    # RF03 — Suportar dois tipos de navio: pequeno (2 posições) e grande (4 posições).
    def __init__(self, tipo):
        self.tipo = tipo
        self.tamanho = (
            2 if tipo.strip().lower() == "pequeno" else 4
        )
        self.posicoes = []
        self.acertos = 0

    # Registra um ataque acertado
    def registrar_acerto(self):
        self.acertos += 1

    #Verifica se o navio afundou, considerei que pra afundar tem que acertar todo o navio
    #RN03 — Um navio é considerado afundado quando todas as suas posições forem atingidas
    def afundou(self):
        return self.acertos >= self.tamanho