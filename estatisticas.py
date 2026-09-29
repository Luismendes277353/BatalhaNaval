import json
import os

ARQUIVO="data/estatisticas.json"

# Salva os dados da partida
# RF12 — Calcular e exibir estatísticas de desempenho do jogador (partidas, acertos, aproveitamento).
def salvar_estatistica(
        vencedor,
        nome_jogador1,
        nome_jogador2,
        jogadas_jogador1,
        jogadas_jogador2,
        acertos_jogador1,
        acertos_jogador2
):
    os.makedirs("data", exist_ok=True)

    dados = carregar_estatisticas()
    dados.append({
        "vencedor": vencedor,
        "nome_jogador1": nome_jogador1,
        "nome_jogador2": nome_jogador2,
        "jogadas_jogador1": jogadas_jogador1,
        "jogadas_jogador2": jogadas_jogador2,
        "acertos_jogador1": acertos_jogador1,
        "acertos_jogador2": acertos_jogador2,
        "aproveitamento_jogador1": (
            acertos_jogador1 / jogadas_jogador1 * 100
            if jogadas_jogador1 > 0
            else 0
        ),
        "aproveitamento_jogador2":(
            acertos_jogador2 / jogadas_jogador2 * 100
            if jogadas_jogador2 > 0
            else 0
        )
    })
    
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# Faz o upload das estatísticas salvas no arquivo
def carregar_estatisticas():
    if not os.path.exists(ARQUIVO):
        return []
    
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
        
    except json.JSONDecodeError:
        return []