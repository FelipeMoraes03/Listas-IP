#CRIAR UMA LISTA COM O TAMANHO DE CADA BATALHÃO: 
def listar_batalhoes(num: int) -> list:
    lista_batalhoes = []
    for i in range(num):
        tamanho_batalhao = int(input())
        if tamanho_batalhao >= 0:
            lista_batalhoes.append(tamanho_batalhao)

    return lista_batalhoes

#ORDENAR A LISTA DO TAMANHO DE CADA BATALHÃO:
def ordenar_lista(lista: list) -> list:
    for _ in range(len(lista) - 1):
        for i in range(len(lista) - 1):
            num1 = lista[i]
            num2 = lista[i + 1]
            if num1 > num2:
                lista[i] = num2
                lista[i + 1] = num1

    return lista

#REALIZAR A BUSCA BINÁRIA:
def busca_binaria(lista: list, num: int, x: int = 0) -> int:
    tamanho_lista = len(lista)
    index_meio = int(tamanho_lista / 2)

    if tamanho_lista == 0:
        return -1
        
    else:
        teste = lista[0]
        if tamanho_lista == 1 and teste != num:
            return -1 - x
        elif lista[index_meio] == num:
            return index_meio
        elif lista[index_meio] < num:
            x += index_meio
            return index_meio + busca_binaria(lista[index_meio:], num, x)
        elif lista[index_meio] > num:
            return busca_binaria(lista[:index_meio], num, x)

def analisar_resultado(num_buscas: int, lista: list) -> None:
    for i in range(num_buscas):
        numero_buscado = int(input())
        resultado = busca_binaria(lista, numero_buscado)
        if resultado == -1:
            print(f"Busca falhou: {resultado}")
        else:
            print(f"Busca com sucesso: {resultado}")


numero_batalhoes = int(input())

lista = listar_batalhoes(numero_batalhoes)
lista = ordenar_lista(lista)

numero_buscas = int(input())

analisar_resultado(numero_buscas, lista)