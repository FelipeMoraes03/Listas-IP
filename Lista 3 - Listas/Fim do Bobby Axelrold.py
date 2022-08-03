lista_testemunhas = input()
lista_testemunhas = lista_testemunhas.split(" ")

numero_trocas = int(input())

for _ in range(numero_trocas):
    indice_testemunha1 = int(input())

    if len(lista_testemunhas) % 2 == 1 and len(lista_testemunhas) // 2 == indice_testemunha1:
    # SÓ VAI SER A MESMA TESTEMUNHA SE O TAMANHO DA LISTA FOR ÍMPAR E A TESTEMUNHA ESTIVER NO MEIO DA LISTA:

        print("Nenhuma troca foi feita")
    else:
        indice_testemunha2 = len(lista_testemunhas) - (indice_testemunha1 + 1)

        if indice_testemunha2 > indice_testemunha1:
            testemunha2 = lista_testemunhas.pop(indice_testemunha2)
            testemunha1 = lista_testemunhas.pop(indice_testemunha1)
            lista_testemunhas.insert(indice_testemunha1, testemunha2)
            lista_testemunhas.insert(indice_testemunha2, testemunha1)
        else:
            testemunha1 = lista_testemunhas.pop(indice_testemunha1)
            testemunha2 = lista_testemunhas.pop(indice_testemunha2)
            lista_testemunhas.insert(indice_testemunha2, testemunha1)
            lista_testemunhas.insert(indice_testemunha1, testemunha2)
        print(f"A testemunha {testemunha1} trocou de ordem com a testemunha {testemunha2}")

print(" ".join(lista_testemunhas))