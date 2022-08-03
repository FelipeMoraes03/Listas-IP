import copy

# CRIAR UMA MATRIZ PARA O LABIRINTO
def criar_labirinto(tamanho: int) -> list:
    labirinto = []
    for _ in range(tamanho):
        entrada_linha = input()
        linha = [i for i in entrada_linha]
        labirinto.append(linha)

    return labirinto

# PRINTAR A MATRIZ DO LABIRINTO
def printar_labirinto(labirinto: list, final: bool= False):
    copia = copy.deepcopy(labirinto)
    # NÃO HÁ MAIS NENHUM CAMINHO PARA VERIFICAR
    if final:
        for linha in range(len(copia)):
            if "X" in copia[linha] or "F" in copia[linha]:
                for coluna in range(len(copia[linha])):
                    if copia[linha][coluna] == "X" or copia[linha][coluna] == "F":
                        copia[linha][coluna] = "."
            print(''.join(copia[linha]))

    # AINDA HÁ OUTROS CAMINHOS PARA VERIFICAR
    else:
        for linha in range(len(copia)):
            if "X" in copia[linha]:
                for coluna in range(len(copia[linha])):
                    if copia[linha][coluna] == "X":
                        copia[linha][coluna] = "."
            print(''.join(copia[linha]))

# VERIFICAR SE CHEGOU NO FINAL DO LABIRINTO, E SE NÃO CHEGOU, VERIFICAR SE HÁ ALGUM OUTRO CAMINHO POSSÍVEL
def testar_chegada(labirinto: list, linha: int, coluna: int, direcao: str, substituir: str) -> bool:
    # CHEGOU NO FINAL DO LABIRINTO
    if labirinto[linha][coluna] == "O":
        if substituir == "F":
            labirinto[linha][coluna] = substituir
            printar_labirinto(labirinto)
            print(f"Por aqui meus amigos vamos pelo {direcao}\n")

        # CHEGOU EM UM BECO SEM SAÍDA E ESTÁ FAZENDO O CAMINHO DE VOLTA
        else:
            if direcao == "Sul":
                labirinto[linha - 1][coluna] = substituir
            elif direcao == "Leste":
                labirinto[linha][coluna - 1] = substituir
            elif direcao == "Norte":
                labirinto[linha + 1][coluna] = substituir
            elif direcao == "Oeste":
                labirinto[linha][coluna + 1] = substituir
                
            printar_labirinto(labirinto)
            print("Vamos encontrar outro caminho amigos, temos que ter fé!!\n")

        printar_labirinto(labirinto)
        print("Conseguimos!!")

    # HÁ UM CAMINHO POSSÍVEL, MAS NÃO É O FINAL
    else: 
        if substituir == "F":
            labirinto[linha][coluna] = substituir
            printar_labirinto(labirinto)
            print(f"Por aqui meus amigos vamos pelo {direcao}\n")

        # CHEGOU EM UM BECO SEM SAÍDA E ESTÁ FAZENDO O CAMINHO DE VOLTA
        else:
            if direcao == "Sul":
                labirinto[linha - 1][coluna] = substituir
            elif direcao == "Leste":
                labirinto[linha][coluna - 1] = substituir
            elif direcao == "Norte":
                labirinto[linha + 1][coluna] = substituir
            elif direcao == "Oeste":
                labirinto[linha][coluna + 1] = substituir

            printar_labirinto(labirinto)
            print("Vamos encontrar outro caminho amigos, temos que ter fé!!\n")

        return percorrer_labirinto(labirinto, linha, coluna)

# VERIFICAR SE É POSSÍVEL CONTINUAR PERCORRENDO O LABIRINTO; E SE POSSÍVEL, ESCOLHER DIREÇÃO
def percorrer_labirinto(labirinto: list, linha_inicio: int, coluna_inicio: int, \
    possibilidades_andar: list= [".", "O"], substituir:str = "F"):

    # CAMINHO POSSÍVEL PELO SUL
    if  linha_inicio + 1 < len(labirinto) and labirinto[linha_inicio + 1][coluna_inicio] in possibilidades_andar:
        testar_chegada(labirinto, linha_inicio + 1, coluna_inicio, "Sul", substituir)

    # CAMINHO POSSÍVEL PELO LESTE
    elif coluna_inicio + 1 < len(labirinto) and labirinto[linha_inicio][coluna_inicio + 1] in possibilidades_andar:
        testar_chegada(labirinto, linha_inicio, coluna_inicio + 1, "Leste", substituir)

    # CAMINHO POSSÍVEL PELO NORTE
    elif linha_inicio > 0 and labirinto[linha_inicio - 1][coluna_inicio] in possibilidades_andar:
        testar_chegada(labirinto, linha_inicio - 1, coluna_inicio, "Norte", substituir)

    # CAMINHO POSSÍVEL PELO OESTE
    elif coluna_inicio > 0 and labirinto[linha_inicio][coluna_inicio - 1] in possibilidades_andar:
        testar_chegada(labirinto, linha_inicio, coluna_inicio - 1, "Oeste", substituir)

    # CAMINHO SEM SAÍDA
    else:
        if substituir == "F":
            percorrer_labirinto(labirinto, linha_inicio, coluna_inicio, [".", "O", "F"], "X")

        # NÃO HÁ MAIS NENHUM CAMINHO PARA VERIFICAR
        else:
            printar_labirinto(labirinto, True)
            print("Vamos encontrar outro caminho amigos, temos que ter fé!!\n")
            print("Amigos a jornada foi incrível, porém ela acaba por aqui...")

tamanho_labirinto = int(input())
coord_entrada_linha = int(input())
coord_entrada_coluna = int(input())

labirinto = criar_labirinto(tamanho_labirinto)
percorrer_labirinto(labirinto, coord_entrada_linha, coord_entrada_coluna)