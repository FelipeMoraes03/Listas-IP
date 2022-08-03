continuar = True
lista_pretendentes = []
while continuar:
    entrada = input()
    if entrada == "fim":
        continuar = False

    elif entrada == "adicionar":
        nome = input()
        if nome not in lista_pretendentes:
            lista_pretendentes.append(nome)
            print(f"{nome} foi adicionada ao final da lista")

    elif entrada == "remover":
        nome = input()
        lista_pretendentes.remove(nome)
        print(f"{nome} foi removida da lista")

    elif entrada == "atualizar posiçao":
        nome = input()
        indice = int(input())

        indice_nome = lista_pretendentes.index(nome)
        if indice == indice_nome:
            print(f"Nada mudou, {nome} ja esta na posiçao certa")
        elif indice != indice_nome:
            lista_pretendentes.remove(nome)
            lista_pretendentes.insert(indice, nome)
            print(f"{nome} foi inserida na posição {indice} da lista")

if len(lista_pretendentes) == 0:
    print("Não sobraram pretendentes para voce, Ted")
elif len(lista_pretendentes) > 0:
    print(" ".join(lista_pretendentes))