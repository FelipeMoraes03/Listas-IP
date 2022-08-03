doug_judy = False
lista_criminosos = []
lista_crimes = []
lista_assassinos = []
lista_ladroes = []

while not doug_judy:
    crime_criminoso = input()
    crime, criminoso = crime_criminoso.split(": ")
    if criminoso == "Doug Judy":
        doug_judy = True
    else:
        lista_crimes.append(crime)
        lista_criminosos.append(criminoso)

numero_operacoes = int(input())

for _ in range(numero_operacoes):
    operacao_da_vez = int(input())

    if operacao_da_vez == 1:
        criminoso_procurado = input()
        numero_crimes_do_procurado = lista_criminosos.count(criminoso_procurado)
        print(f"Na ficha de {criminoso_procurado} constam {numero_crimes_do_procurado} infrações este mês.")

    elif operacao_da_vez == 2:
        crime_procurado = input()
        numero_ocorrencia_crimes = lista_crimes.count(crime_procurado)
        print(f"Neste mês foram cometidos {numero_ocorrencia_crimes} {crime_procurado}")

    elif operacao_da_vez == 3:
        indice = 0
        for ocorrencia in lista_crimes:
            if ocorrencia == "Furto" or ocorrencia == "Roubo":
                index_ocorrencia = lista_crimes.index(ocorrencia, indice)
                criminoso = lista_criminosos.pop(index_ocorrencia)
                lista_criminosos.insert(index_ocorrencia, criminoso)
                if criminoso not in lista_ladroes:
                    lista_ladroes.append(criminoso)

            elif ocorrencia == "Assassinato":
                index_ocorrencia = lista_crimes.index(ocorrencia, indice)
                criminoso = lista_criminosos.pop(index_ocorrencia)
                lista_criminosos.insert(index_ocorrencia, criminoso)
                if criminoso not in lista_assassinos:
                    lista_assassinos.append(criminoso)

            indice += 1

        ladroes = ", ".join(lista_ladroes)
        assassinos = ", ".join(lista_assassinos)

        print(f"Boletim de Ocorrências:\nAssassinos: {assassinos}\nLadroes: {ladroes}")
