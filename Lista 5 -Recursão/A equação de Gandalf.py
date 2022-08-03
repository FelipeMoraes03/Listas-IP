#LISTA, EM QUE CADA ELEMENTO É UM DÍGITO DO NÚMERO:
def transformar_num_lista(num: int) -> list:
    num_str = str(num)
    lista = [i for i in num_str]
    return lista

#CRIAR OS PARES DE NÚMEROS, ORDENAR ESSES PARES E TRANSFORMAR A LISTA EM UM NÚMERO INTEIRO:
def ordenar_digitos(lista: list) -> int:
    lista_pares = []

    for i in range(10):
        digito = str(i)
        repeticoes = lista.count(digito)

        if repeticoes > 0:
            par_repeticoes_numero = str(repeticoes) + digito
            lista_pares.append(par_repeticoes_numero)

    lista_pares.sort()
    numero_ordenado = int("".join(lista_pares))
    return numero_ordenado

#RECEBER O NÚMERO INICIAL E TRANSFORMÁ-LO EM UM NÚMERO COM 8 OU MAIS DÍGITOS:
def funcao(num: int) -> int:
    lista = transformar_num_lista(num)
    if len(lista) >= 8:
        return int("".join(lista))
    else:
        num = ordenar_digitos(lista)
        return funcao(num)


numero = int(input())
novo_numero = funcao(numero)
print(novo_numero)