lista_advogado = []
lista_tipo_caso = []
lista_pontuacao_caso = []

# LISTAS = [PONTUAÇÃO MÁXIMA, QNT PRÓ BONOS, PONTUAÇÃO TOTAL]
lista_mike = [0, 0, 0]
lista_louis = [0, 0, 0]
lista_harvey = [0, 0, 0]

numero_casos = int(input())
for _ in range(numero_casos):
    advogado, caso, pontuacao = input().split()

    lista_advogado.append(advogado)
    lista_tipo_caso.append(caso)
    lista_pontuacao_caso.append(int(pontuacao))

# ADICIONAR A PONTUAÇÃO MÁXIMA, A QNT DE PRÓ BONOS E A PONTUAÇÃO TOTAL NA LISTA DE CADA ADVOGADO INDIVIDUALMENTE
index = 0
for advogado in lista_advogado:
    if advogado == "Mike":
        if lista_pontuacao_caso[index] > lista_mike[0]:
            lista_mike[0] = lista_pontuacao_caso[index]
        if lista_tipo_caso[index] == "pro-bono":
            lista_mike[1] += 1
        lista_mike[2] += lista_pontuacao_caso[index]

    elif advogado == "Louis":
        if lista_pontuacao_caso[index] > lista_louis[0]:
            lista_louis[0] = lista_pontuacao_caso[index]
        if lista_tipo_caso[index] == "pro-bono":
            lista_louis[1] += 1
        lista_louis[2] += lista_pontuacao_caso[index]

    elif advogado == "Harvey":
        if lista_pontuacao_caso[index] > lista_harvey[0]:
            lista_harvey[0] = lista_pontuacao_caso[index]
        if lista_tipo_caso[index] == "pro-bono":
            lista_harvey[1] += 1
        lista_harvey[2] += lista_pontuacao_caso[index]
    index += 1

# TRANSFORMAR A PONTUAÇÃO MÁXIMA NA MÉDIA, EM CADA LISTA
lista_mike[2] = lista_mike[2] / lista_advogado.count("Mike")
lista_louis[2] = lista_louis[2] / lista_advogado.count("Louis")
lista_harvey[2] = lista_harvey[2] / lista_advogado.count("Harvey")

# LISTA DA LISTA DE CADA ADVOGADO
lista_final = [lista_mike, lista_louis, lista_harvey] # O TAMANHO DA LISTA SEMPRE VAI SER 3!

# ORDENAR A LISTA FINAL DE ACORDO COM A PONTUAÇÃO MÁXIMA
for _ in range(2):
    for index in range(2):
        num1 = (lista_final[index])[0] #num1 = PONTUAÇÃO MÁXIMA DO ADOGADO "x"
        var1 = lista_final[index] #va1 = LISTA DO ADVOGADO "x"
        num2 = (lista_final[index + 1])[0] #num2 = PONTUAÇÃO MÁXIMA DO ADVOGADO "y"
        var2 = lista_final[index + 1] #var2 = LISTA DO ADVOGADO "y"
        if num1 < num2:
            lista_final[index] = var2
            lista_final[index + 1] = var1

# ORDENAR A LISTA FINAL DE ACORDO COM QNT DE CASOS PRÓ BONOS
for _ in range(2):
    for index in range(2):
        num1 = (lista_final[index])[1] #num1 = QNT PRÓ BONOS DO ADOGADO "x"
        var1 = lista_final[index] #va1 = LISTA DO ADVOGADO "x"
        num2 = (lista_final[index + 1])[1] #num2 = QNT PRÓ BONOS DO ADVOGADO "y"
        var2 = lista_final[index + 1] #var2 = LISTA DO ADVOGADO "y"
        if num1 < num2:
            lista_final[index] = var2
            lista_final[index + 1] = var1

# ORDENAR A LISTA FINAL DE ACORDO COM A MÉDIA
for _ in range(2):
    for index in range(2):
        num1 = (lista_final[index])[2] #num1 = MÉDIA DO ADOGADO "x"
        var1 = lista_final[index] #va1 = LISTA DO ADVOGADO "x"
        num2 = (lista_final[index + 1])[2] #num2 = MÉDIA DO ADVOGADO "y"
        var2 = lista_final[index + 1] #var2 = LISTA DO ADVOGADO "y"
        if num1 < num2:
            lista_final[index] = var2
            lista_final[index + 1] = var1

# DEFINIR O VENCEDOR
if lista_final[0] == lista_mike:
    vencedor = "Mike"
elif lista_final[0] == lista_louis:
    vencedor = "Louis"
else:
    vencedor = "Harvey"

# DEFINIR O PERDEDOR
if lista_final[2] == lista_harvey:
    perdedor = "Harvey"
elif lista_final[2] == lista_louis:
    perdedor = "Louis"
else:
    perdedor = "Mike"

print(f"""Mike;\nMédia: {lista_mike[2]:.2f}\nQuantidade de Pró-bonos: {lista_mike[1]}\nMáximo: {lista_mike[0]}\n
Louis;\nMédia: {lista_louis[2]:.2f}\nQuantidade de Pró-bonos: {lista_louis[1]}\nMáximo: {lista_louis[0]}\n
Harvey;\nMédia: {lista_harvey[2]:.2f}\nQuantidade de Pró-bonos: {lista_harvey[1]}\nMáximo: {lista_harvey[0]}\n
Quem ganhou a competição e vai ficar com a sala nova foi o {vencedor}!!! \
E o coitado que vai ter que comprar os móveis vai ser o {perdedor}.""")