from pyparsing import col


def imprimir_tabuleiro(tabuleiro):
    print("JOGO DA 👵!")
    print("\n" + "-"*13)
    for linha in tabuleiro:
        print("|", end="")
        for posicao in linha:
            print(f"{posicao:^3}", end="|")
        print("\n" + "-"*13)

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all([posicao == jogador for posicao in linha]):
            return True

    for coluna in range(3):
        if all([tabuleiro[linha][coluna] == jogador for linha in range(3)]):
            return True

    if all([tabuleiro[i][i] == jogador for i in range(3)]) or all([tabuleiro[i][2-i] == jogador for i in range(3)]):
        return True

    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador = "X"

    while True:
        imprimir_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogador}, digite o número da linha (0, 1, 2): "))
        coluna = int(input(f"Jogador {jogador}, digite o número da coluna (0, 1, 2): "))

        if tabuleiro[linha][coluna] != " ":
            print("Posição ocupada. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador

        if verificar_vitoria(tabuleiro, jogador):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador} venceu!")
            if jogador == "O":
                contO = 0
                contO +=1
                print(contO)
                # tabuleiro.remove(linha)
            else:
                contX = 0
                contX +=1
                print(contX)
                tabuleiro.clear(linha)
                tabuleiro.clear(coluna)
                

            

        if all([posicao != " " for linha in tabuleiro for posicao in linha]):
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            contEmpate = 0
            contEmpate += 1
            print(contEmpate)

        jogador = "O" if jogador == "X" else "X"

jogo_da_velha()
