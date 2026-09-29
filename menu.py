from utils import limpar_tela

# Exibe o menu principal
# RF01 — Exibir um menu principal com as opções do sistema.
def exibir_menu():
    limpar_tela()

    print(
        f"==================================================\n"
        f"\tBATALHA NAVAL - GPTECH GAMES\n"
        f"==================================================\n"
        f"1. Nova partida\n"
        f"2. Ver estatisticas\n"
        f"3. Assistir replay da ultima partida\n"
        f"4. Creditos\n"
        f"5. Sair\n"
        f"--------------------------------------------------\n"
    )

    return input("Escolha uma opcao: ")