import time

from computador import Computador
from estatisticas import (
    salvar_estatistica,
    carregar_estatisticas
)
from jogador import Jogador
from menu import exibir_menu
from replay import Replay
from utils import limpar_tela

# Exibe as estatísticas das partidas
def exibir_estatisticas():
    limpar_tela()

    dados=carregar_estatisticas()

    print(
        f"==================================================\n"
        f"\tESTATISTICAS\n"
        f"==================================================\n"
    )

    if not dados:
        print("Nenhuma partida registrada ainda")
        input("\n[ENTER] para voltar...")
        return
    
    partidas = len(dados)

    print(f"Partidas registradas: {partidas}\n")

    for i, partida in enumerate(dados, start=1):
        print(
            f"Partida {i}:\n"
            f"Vencedor: {partida['vencedor']}\n"
            f"Jogador 1 ({partida['nome_jogador1']}):\n"
            f"\tJogadas: {partida['jogadas_jogador1']}\t|"
            f"\tAcertos: {partida['acertos_jogador1']}\t|"
            f"\tAproveitamento: {partida['aproveitamento_jogador1']:.2f}%\n"
            f"Jogador 2 ({partida['nome_jogador2']}):\n"
            f"\tJogadas: {partida['jogadas_jogador2']}\t|"
            f"\tAcertos: {partida['acertos_jogador2']}\t|"
            f"\tAproveitamento: {partida['aproveitamento_jogador2']:.2f}%\n"
        )

    print("--------------------------------------------------")
    input("\n[ENTER] para voltar...")

# Exibir o resultado de um ataque
# RF06 — Exibir mensagens de água, acerto e navio afundado a cada jogada.
def exibir_resultado(resultado):
    if resultado == "agua":
        print("Agua! Nenhum navio atingido nessa posicao.")

    elif resultado == "acerto":
        print("Acerto! Voce atingiu um navio inimigo.")

    elif resultado == "afundado":
        print("Navio afundado! Voce destruiu um navio do adversario.")

# Executa uma nova partida
def jogar_partida():
    limpar_tela()

    print(
        f"Selecione o modo de jogo:\n"
        f"\t[1] Jogador vs Computador\n"
        f"\t[2] Dois Jogadores\n"
        f"\t[0] Voltar ao menu\n"
    )

    modo=input(">> ")

    if modo == '0':
        return
    
    if modo not in ("1", "2"):
        input("Modo inexistente\n[ENTER] para voltar...")
        return
    
    limpar_tela()

    if modo == "1":
        nome = input("Digite seu nome: ")
        jogador1 = Jogador(nome)
        jogador2 = Computador()

    else:
        nome1 = input("Digite o nome do Jogador 1: ")
        nome2 = input("Digite o nome do Jogador 2: ")
        jogador1=Jogador(nome1)
        jogador2 = Jogador(nome2)

    replay = Replay()

    turno = 1
    total_jogadas = 0
    jogadas_jogador1 = 0
    jogadas_jogador2 = 0
    acertos_jogador1 = 0
    acertos_jogador2 = 0

    limpar_tela()

    print(f"Frota de {jogador1.nome}: ")
    jogador1.tabuleiro.exibir()

    input("[ENTER] para iniciar a partida...")

    inicio = time.time()

    while (jogador1.tem_navios() and jogador2.tem_navios()):
        # Começa o turno do jogador 1
        limpar_tela()

        print(f"\n\t|\tTURNO {turno}\t|\n")

        print(f"\nTabuleiro de {jogador1.nome}: ")
        jogador1.tabuleiro.exibir()

        print(f"\nTabuleiro de {jogador2.nome}: ")
        jogador2.tabuleiro.exibir(ocultar_navios=True)

        print(f"\nVez de {jogador1.nome}")

        coord, resultado=jogador1.atacar(jogador2)

        total_jogadas += 1
        jogadas_jogador1 += 1

        if resultado in ("acerto", "afundado"):
            acertos_jogador1 += 1

        replay.registrar(
            total_jogadas,
            jogador1.nome,
            coord,
            resultado
        )

        exibir_resultado(resultado)

        if not jogador2.tem_navios():
            break

        input("[ENTER] para continuar...")

        limpar_tela()

        # Comeca o turno do jogador 2
        if isinstance(jogador2, Computador):
            print(f"\nO computador esta escolhendo uma jogada...")

            coord, resultado = jogador2.atacar(jogador1)
            
            total_jogadas += 1
            jogadas_jogador2 += 1

            if resultado in ("acerto", "afundado"):
                acertos_jogador2 += 1

            replay.registrar(
                total_jogadas,
                jogador2.nome,
                coord,
                resultado
            )

            print(f"\nO computador atacou {coord}.")

        else:
            print(f"\nTabuleiro de {jogador2.nome}:")
            jogador2.tabuleiro.exibir()

            print(f"\nTabuleiro de {jogador1.nome}:")
            jogador1.tabuleiro.exibir(ocultar_navios=True)

            print(f"\nVez de {jogador2.nome}")

            coord, resultado = jogador2.atacar(jogador1)

            total_jogadas += 1
            jogadas_jogador2 += 1

            if resultado in ("acerto", "afundado"):
                acertos_jogador2 += 1

            replay.registrar(
                total_jogadas,
                jogador2.nome,
                coord,
                resultado
            )

        exibir_resultado(resultado)

        turno += 1

        if jogador1.tem_navios():
            input("\n[ENTER] para continuar...")

    tempo_total = time.time() - inicio

    if jogador1.tem_navios():
        vencedor = jogador1.nome

    else:
        vencedor = jogador2.nome

    #Salva o replay e as estatísticas
    replay.salvar()

    salvar_estatistica(
        vencedor,
        jogador1.nome,
        jogador2.nome,
        jogadas_jogador1,
        jogadas_jogador2,
        acertos_jogador1,
        acertos_jogador2
    )

    # Exibe o resultado final da partida
    # RF07 — Encerrar a partida exibindo o vencedor, o número de jogadas e o tempo total de jogo.
    while True:
        limpar_tela()

        minutos = int(tempo_total // 60)
        segundos = int(tempo_total % 60)

        print(
            f"==================================================\n"
            f"\tFIM DE JOGO\n"
            f"==================================================\n"
            f"Vencedor: {vencedor}\n"
            f"Total de jogadas: {total_jogadas}\n"
            f"Acertos de {jogador1.nome}: {acertos_jogador1}\n"
            f"Acertos de {jogador2.nome}: {acertos_jogador2}\n"
            f"Tempo de partida: {minutos:02d}:{segundos:02d}\n"
            f"--------------------------------------------------\n"
            f"[1] Ver replay [2] Nova partida [3] Menu principal\n"
        )
        # RF08 — Permitir iniciar uma nova partida a qualquer momento pelo menu. (e no menu tambem)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            limpar_tela()
            replay.reproduzir()
            input("\n[ENTER] para voltar...")

        elif opcao == "2":
            jogar_partida()
            return
        
        elif opcao == "3":
            return
        
        else:
            input(
                "Opção Inválida\n"
                "[ENTER] para tentar novamente..."
            )

# Controla o menu principal
def main():
    while True:
        opcao = exibir_menu()

        match opcao:
            case "1":
                jogar_partida()

            case "2":
                exibir_estatisticas()
                
            case "3":
                limpar_tela()
                Replay().reproduzir()
                input("\n[ENTER] para voltar ao menu...")

            case "4":
                limpar_tela()

                print(
                    f"=================================================="
                    f"\n\t\tCRÉDITOS\n"
                    f"==================================================\n"
                    f"Batalha Naval - GPTech Games\n"
                    f"Desenvolvido por Luís Mendes\n"
                    f"Programação em Python\n"
                    f"Prof. Guido Pantuza\n"
                )

                input("\n[ENTER] para voltar ao menu...")

            case "5":
                limpar_tela()
                print("Saindo do Batalha Naval...")
                break
            
            case _:
                input("Opção inválida\n[ENTER] para tentar novamente")

if __name__ == "__main__":
    main()