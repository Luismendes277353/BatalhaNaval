import json
import os

class Replay:
    # Cria o histórico da partida
    # RF11 — Registrar o histórico de jogadas realizadas durante a partida.
    def __init__(self):
        self.historico = []

    # Registra cada uma das jogadas realizadas
    def registrar(self, turno, jogador, coord, resultado):
        self.historico.append({
            "turno": turno,
            "jogador": jogador,
            "coord": coord,
            "resultado": resultado
        })

    # Salva o replay em arquivo
    # RF13 — Disponibilizar um modo replay que reproduza as jogadas da última partida.
    def salvar(self):
        os.makedirs("data", exist_ok=True)

        with open('data/replay.json', "w", encoding="utf-8") as f:
            json.dump(self.historico, f, indent=4, ensure_ascii=False)

    # Reproduz as jogadas da última partida
    def reproduzir(self):
        if not os.path.exists('data/replay.json'):
            print("Nenhum replay encontrado")
            return
        
        with open('data/replay.json', "r", encoding="utf-8") as f:
            dados=json.load(f)

        print(f"\n\tReproduzindo replay da última partida..:\n")

        for i, jogada in enumerate(dados):
            print(
                f"Jogada {i + 1:02d}/{len(dados)} - "
                f"{jogada['jogador']} - "
                f"{jogada['coord']} - "
                f"{jogada['resultado'].capitalize()}"
            )

            q=input("[ENTER] Próxima jogada [Q] Sair do replay")

            if q.upper() == "Q":
                print("Saindo do replay...")
                return