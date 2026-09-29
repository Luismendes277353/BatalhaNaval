import os

# Limpa a tela do terminal
def limpar_tela():
    os.system("clear" if os.name == "posix" else "cls")

# Converte letra e num em coordenadas
# (RN01 — As coordenadas são informadas no formato Letra + Número (ex.: C5), com colunas de A a J e linhas de 1 a 10.)
def traduzir_coordenada(entrada):
    try:
        entrada = entrada.strip().upper()
        coluna = ord(entrada[0]) - ord("A")
        linha = int(entrada[1:]) - 1

        if (0 <= linha <= 9 and 0 <= coluna <= 9):
            return linha, coluna
        
        return None, None

    except (ValueError, IndexError):
        return None, None