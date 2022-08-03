# CRIAR UMA MATRIZ PARA O LABIRINTO
def criar_labirinto(tamanho: int) -> list:
    labirinto = []
    for _ in range(tamanho):
        entrada_linha = input()
        linha = [i for i in entrada_linha]
        labirinto.append(linha)

    return labirinto

# PRINTAR A MATRIZ DO LABIRINTO
def printar_labirinto(labirinto: list):
    for i in range(len(labirinto)):
        print(''.join(labirinto[i]))

# VERIFICAR SE CHEGOU NO FINAL DO LABIRINTO
def testar_chegada(labirinto: list, linha: int, coluna: int, direcao) -> bool:
    if labirinto[linha][coluna] == "O": # CHEGOU NO FINAL DO LABIRINTO
        labirinto[linha][coluna] = "F"
        printar_labirinto(labirinto)
        print(f"Por aqui meus amigos vamos pelo {direcao}\n")
        printar_labirinto(labirinto)
        print("Conseguimos!!")

    else: # HÁ UM CAMINHO POSSÍVEL, MAS NÃO É O FINAL
        labirinto[linha][coluna] = "F"
        printar_labirinto(labirinto)
        print(f"Por aqui meus amigos vamos pelo {direcao}\n")
        return percorrer_labirinto(labirinto, linha, coluna)

# VERIFICAR SE É POSSÍVEL CONTINUAR PERCORRENDO O LABIRINTO; E SE POSSÍVEL, ESCOLHER DIREÇÃO
def percorrer_labirinto(labirinto: list, linha_inicio: int, coluna_inicio: int) -> list:
    possibilidades_andar = [".", "O"]

    # CAMINHO POSSÍVEL PELO SUL
    if  linha_inicio + 1 < len(labirinto) and labirinto[linha_inicio + 1][coluna_inicio] in possibilidades_andar:
        return testar_chegada(labirinto, linha_inicio + 1, coluna_inicio, "Sul")

    # CAMINHO POSSÍVEL PELO LESTE
    elif coluna_inicio + 1 < len(labirinto) and labirinto[linha_inicio][coluna_inicio + 1] in possibilidades_andar:
        return testar_chegada(labirinto, linha_inicio, coluna_inicio + 1, "Leste")

    # CAMINHO POSSÍVEL PELO NORTE
    elif linha_inicio > 0 and labirinto[linha_inicio - 1][coluna_inicio] in possibilidades_andar:
        return testar_chegada(labirinto, linha_inicio - 1, coluna_inicio, "Norte")

    # CAMINHO POSSÍVEL PELO OESTE
    elif coluna_inicio > 0 and labirinto[linha_inicio][coluna_inicio - 1] in possibilidades_andar:
        return testar_chegada(labirinto, linha_inicio, coluna_inicio - 1, "Oeste")

    else: # CAMINHO SEM SAÍDA
        print("Amigos a jornada foi incrível, porém ela acaba por aqui...")

tamanho_labirinto = int(input())
coord_entrada_linha = int(input())
coord_entrada_coluna = int(input())

labirinto = criar_labirinto(tamanho_labirinto)
percorrer_labirinto(labirinto, coord_entrada_linha, coord_entrada_coluna)