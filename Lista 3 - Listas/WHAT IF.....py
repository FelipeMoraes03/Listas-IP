entrada = ""
lista = []
tamanho_lista = 0

while entrada != "fim":
    entrada = input()
    if entrada != "fim":
        lista.append(int(entrada))
        tamanho_lista += 1

for _ in range(tamanho_lista - 1):
    for index in range(tamanho_lista - 1):
        num1 = lista[index]
        num2 = lista[index + 1]
        if num1 > num2:
            lista[index] = num2
            lista[index + 1] = num1

for numero in lista:
    print(numero)