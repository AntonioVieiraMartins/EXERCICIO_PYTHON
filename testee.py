def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))

def verificar_vitoria(tabuleiro, jogador):
    # Lógica para verificar vitória (linhas, colunas, diagonais)
    # Retorna True se o jogador venceu, senão False
    pass

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)
        linha, coluna = map(int, input(f"Jogador {jogador_atual}, digite a posição (linha coluna): ").split())
        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            print(f"Jogador {jogador_atual} venceu!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

jogo_da_velha()